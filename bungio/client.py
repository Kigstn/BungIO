import asyncio
import datetime
import logging
import os
from base64 import b64encode
from copy import copy
from typing import TYPE_CHECKING, Callable, Optional

import attr
from sqlalchemy import MetaData
from sqlalchemy.ext.asyncio import AsyncEngine, create_async_engine

import bungio.singleton as singleton
from bungio.api import ApiClient
from bungio.definitions import DEFAULT_LOGGER, LOGGER_NAME, ROOT_DIR
from bungio.error import InvalidAuthentication
from bungio.http.client import HttpClient
from bungio.manifest import Manifest
from bungio.models import BungieMembershipType
from bungio.models.auth import AuthData
from bungio.models.enums import BungieLanguage
from bungio.utils import get_now_with_tz

if TYPE_CHECKING:
    from aiohttp_client_cache import CacheBackend

__all__ = ("Client",)

# define json loading technique
try:
    import orjson

    def json_dumps(x):
        return orjson.dumps(x).decode()

    json_loads = orjson.loads
except ModuleNotFoundError:
    import json

    json_dumps = json.dumps
    json_loads = json.loads


token_update_lock: dict[int, asyncio.Lock] = {}

__all__ = ("Client",)


@attr.define
class Client(metaclass=singleton.SingletonMetaclass):
    """
    The singleton api client

    Attributes:
        bungie_client_id: The bungie.net client id
        bungie_client_secret: The bungie.net client secret
        bungie_token: The bungie.net token
        logger: If a custom logger should be used
        language: The language the manifest entries should be in
        cache: If http requests should be cached. It is recommended that you make use of this to not ratelimit yourself as quickly.
        manifest_storage: If manifest entires should be stored, and how. Disabling this stops you from querying the manifest.
        always_return_manifest_information: If manifest information should always be returned on every request. Keep in mind that this will increase requests performed / storage for an increased ease of use.
    """

    bungie_client_id: str = attr.field(repr=False)
    bungie_client_secret: str = attr.field(repr=False)
    bungie_token: str = attr.field(repr=False)

    logger: logging.Logger = attr.field(default=DEFAULT_LOGGER)

    language: BungieLanguage = attr.field(default=BungieLanguage.ENGLISH)

    cache: Optional["CacheBackend"] = attr.field(default=None)
    manifest_storage: bool | AsyncEngine = attr.field(default=True)
    always_return_manifest_information: bool = attr.field(default=False)

    json_dumps: Callable = attr.field(init=False, default=json_dumps, repr=False)
    json_loads: Callable = attr.field(init=False, default=json_loads, repr=False)

    api: ApiClient = attr.field(init=False, repr=False)
    http: HttpClient = attr.field(init=False, repr=False)
    manifest: Optional[Manifest] = attr.field(init=False, default=None, repr=False)

    _metadata: Optional[MetaData] = attr.field(init=False, default=None, repr=False)

    @manifest_storage.validator  # noqa
    def manifest_storage_check(self, attribute, value):
        if not (isinstance(value, AsyncEngine) or isinstance(value, bool)):
            raise ValueError(f"{attribute} obj must be of type `AsyncEngine`")

    @language.validator  # noqa
    def language_check(self, attribute, value):
        if not isinstance(value, BungieLanguage):
            raise ValueError(f"{attribute} must be an instance of type BungieLanguage")

    def __attrs_post_init__(self):
        if self.always_return_manifest_information:
            if not isinstance(self.manifest_storage, AsyncEngine):
                raise ValueError("Client.manifest_storage must be set up to use this")

        if self.always_return_manifest_information:
            if not isinstance(self.manifest_storage, AsyncEngine):
                raise ValueError("Client.manifest_storage must be set up to use this")

        # save a reference to the client
        singleton.client = self

        # set up the api client
        self.api = ApiClient()

        # set up the http client
        self.http = HttpClient(
            bungie_headers={
                "User-Agent": "BungIO",
                "X-API-Key": self.bungie_token,
                "Accept": "application/json",
            },
            bungie_auth_headers={
                "User-Agent": "BungIO",
                "Content-Type": "application/x-www-form-urlencoded",
                "Authorization": f"""Basic {b64encode(f"{self.bungie_client_id}:{self.bungie_client_secret}".encode()).decode()}""",
                "Accept": "application/json",
            },
        )

        if self.manifest_storage:
            if self.manifest_storage is True:
                # todo clarify where that is stored
                self.manifest_storage = create_async_engine(
                    f"""sqlite+aiosqlite:///{os.path.join(ROOT_DIR, "manifest.db")}"""
                )
            self._metadata = MetaData(bind=self.manifest_storage)
            self.manifest = Manifest()

    def get_auth_url(self, state: str) -> str:
        """
        Generate an url which users can use to authenticate with their bungie.net account.

        Warning: Requires external set up
            This requires you to have set up a redirect url (and logic handling that) on bungie.net.
            More information can be found on [the official documentation](https://github.com/Bungie-net/api/wiki/OAuth-Documentation)

        Args:
            state: An opaque value used by the client to maintain state between the request and the callback. The parameter should be used for preventing cross-site request forgery as described in section 10.12 of the OAuth 2.0 specification.

        Returns:
            The auth url
        """

        return f"https://www.bungie.net/en/oauth/authorize?client_id={self.bungie_client_id}&response_type=code&state={state}"

    async def generate_auth(
        self, membership_type: BungieMembershipType | int, destiny_membership_id: int, code: str
    ) -> AuthData:
        """
        Generate authentication information from a bungie code. For information on how to get that code, visit the [official documentation](https://github.com/Bungie-net/api/wiki/OAuth-Documentation)

        Tip: Staying up to date
            This dispatches the Client.on_token_update()

        Args:
            membership_type: The `membership_type` of the user this data belongs to
            destiny_membership_id: The `destiny_membership_id` of the user this data belongs to
            code: The code bungie sent

        Raises:
            InvalidAuthentication: If authentication is invalid

        Returns:
            The working authentication info.
        """

        if not isinstance(membership_type, BungieMembershipType):
            membership_type = BungieMembershipType(membership_type)

        now = get_now_with_tz()
        data = await self.request_access_token(code=code)

        auth = AuthData(
            membership_type=membership_type,
            destiny_membership_id=destiny_membership_id,
            token=data["access_token"],
            token_expiry=now + datetime.timedelta(seconds=data["expires_in"]),
            refresh_token=data["refresh_token"],
            refresh_token_expiry=now + datetime.timedelta(seconds=data["refresh_expires_in"]),
        )

        # dispatch the update event
        asyncio.create_task(self._client.on_token_update(before=None, after=auth))

        return auth

    async def get_working_auth(self, auth: AuthData) -> AuthData:
        """
        Check if tokens need to be refreshed and then do that.
        Gets called automatically when doing requests with AuthData.

        Tip: Staying up to date
            This dispatches the Client.on_token_update()

        Args:
            auth: The potentially old authentication info.

        Raises:
            InvalidAuthentication: If authentication is invalid

        Returns:
            The working authentication info.
        """

        # locked this on a per-user basis
        if auth.destiny_membership_id not in token_update_lock:
            token_update_lock.update({auth.destiny_membership_id: asyncio.Lock()})
        async with token_update_lock[auth.destiny_membership_id]:

            # check that token exists
            if auth.token is None:
                raise InvalidAuthentication(auth)

            # check if token is expired
            now = get_now_with_tz()
            if auth.token_expiry < (now - datetime.timedelta(minutes=5)):
                return auth

            # check the refresh token expiry
            if auth.refresh_token_expiry > (now - datetime.timedelta(minutes=5)):
                self._invalidate_token(auth=auth)
                raise InvalidAuthentication(auth)

            old_auth = copy(auth)

            # refresh the data
            data = await self.refresh_access_token(auth=auth)
            auth.token = data["access_token"]
            auth.refresh_token = data["refresh_token"]
            auth.token_expiry = now + datetime.timedelta(seconds=data["expires_in"])
            auth.refresh_expires_in = now + datetime.timedelta(seconds=data["refresh_expires_in"])

            # dispatch the update event
            asyncio.create_task(self._client.on_token_update(before=old_auth, after=auth))

        return auth

    async def on_token_update(self, before: Optional[AuthData], after: AuthData) -> None:
        """
        Dispatched whenever a token is generated, updated, or invalidated.

        Tip: Subclassing
            It is highly recommended to subclass the Client and overwrite this function to suite your own needs

        Note: Generation
            If the first token is generated, `before` will be `None`.

        Note: Invalidation
            The token can be invalidated if the auth data is expired. To prevent that, make sure your tokens are updated regularly.
            If the token is invalidated, `after.token` will be `None`.

        Args:
            before: The old auth info
            after: The new auth info
        """

        self.logger.info(f"Updated token for {before.destiny_membership_id=}: {before.token=} -> {after.token=}")
