import asyncio
import datetime
import logging
import os
from base64 import b64encode
from copy import copy
from typing import TYPE_CHECKING, Callable, Optional, Type

from sqlalchemy import MetaData
from sqlalchemy.ext.asyncio import AsyncEngine, create_async_engine

import bungio.singleton as singleton
from bungio.api import ApiClient
from bungio.definitions import DEFAULT_LOGGER, ROOT_DIR
from bungio.error import InvalidAuthentication
from bungio.http.client import HttpClient
from bungio.manifest import Manifest
from bungio.models.auth import AuthData
from bungio.models.base import MISSING, custom_define, custom_field
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


@custom_define(init=False)
class Client(singleton.Singleton):
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
        api_client_class: Supply a custom class for `Client.api`
        http_client_class: Supply a custom class for `Client.http`
        manifest_client_class: Supply a custom class for `Client.manifest`
    """

    bungie_client_id: str = custom_field()
    bungie_client_secret: str = custom_field()
    bungie_token: str = custom_field()

    logger: logging.Logger = custom_field(default=DEFAULT_LOGGER)

    language: BungieLanguage = custom_field(default=BungieLanguage.ENGLISH)

    cache: Optional["CacheBackend"] = custom_field(default=None)
    manifest_storage: bool | AsyncEngine = custom_field(default=True)
    always_return_manifest_information: bool = custom_field(default=False)

    api_client_class: Type[ApiClient] = custom_field(default=ApiClient)
    http_client_class: Type[HttpClient] = custom_field(default=HttpClient)
    manifest_client_class: Type[Manifest] = custom_field(default=Manifest)

    json_dumps: Callable = custom_field(init=False, default=json_dumps)
    json_loads: Callable = custom_field(init=False, default=json_loads)

    api: ApiClient = custom_field(init=False)
    http: HttpClient = custom_field(init=False)
    manifest: Optional[Manifest] = custom_field(init=False, default=None)

    _metadata: Optional[MetaData] = custom_field(init=False, default=None)

    _tasks: set = custom_field(init=False, factory=set)

    _initialised: bool = custom_field(init=False, default=False)

    def __init__(self, *args, **kwargs):
        if not getattr(self, "_initialised", False):
            self.__attrs_init__(*args, **kwargs)
        self._initialised = True

    @manifest_storage.validator  # noqa
    def manifest_storage_check(self, attribute, value):
        if not (isinstance(value, AsyncEngine) or isinstance(value, bool)):
            raise ValueError(f"{attribute} obj must be of type `AsyncEngine`")

    @language.validator  # noqa
    def language_check(self, attribute, value):
        if not isinstance(value, BungieLanguage):
            raise ValueError(f"{attribute} must be an instance of type BungieLanguage")

    def __attrs_post_init__(self):
        try:
            assert isinstance(self.bungie_client_id, str)
            assert isinstance(self.bungie_client_secret, str)
            assert isinstance(self.bungie_token, str)
        except AssertionError as e:
            self.logger.error("Bungie auth info could not be read")
            raise e

        if self.always_return_manifest_information:
            if not isinstance(self.manifest_storage, AsyncEngine):
                raise ValueError("Client.manifest_storage must be set up to use this")

        if self.always_return_manifest_information:
            if not isinstance(self.manifest_storage, AsyncEngine):
                raise ValueError("Client.manifest_storage must be set up to use this")

        # save a reference to the client
        singleton.client = self

        # set up the api client
        self.api = self.api_client_class()

        # set up the http client
        self.http = self.http_client_class(
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
            self.manifest = self.manifest_client_class()

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

    async def generate_auth(self, code: str) -> AuthData:
        """
        Generate authentication information from a bungie code. For information on how to get that code, visit the [official documentation](https://github.com/Bungie-net/api/wiki/OAuth-Documentation)

        Tip: Staying up to date
            This dispatches the `Client.on_token_update()` event

        Args:
            code: The code bungie sent

        Raises:
            InvalidAuthentication: If authentication is invalid

        Returns:
            The working authentication info.
        """

        now = get_now_with_tz()
        data = await self.http.request_access_token(code=code)

        auth = AuthData(
            membership_type=MISSING,
            membership_id=MISSING,
            bungie_name=MISSING,
            token=data["access_token"],
            token_expiry=now + datetime.timedelta(seconds=data["expires_in"]),
            refresh_token=data["refresh_token"],
            refresh_token_expiry=now + datetime.timedelta(seconds=data["refresh_expires_in"]),
        )
        destiny_info = await self.api.get_membership_data_for_current_user(auth=auth)

        # get the user's destiny info
        # this is not set if the user has no cross save
        auth.membership_id = destiny_info.primary_membership_id or MISSING
        if auth.membership_id is MISSING:
            # if primary is not defined, use the first one and dispatch a info that the user should set up cross save
            auth.membership_id = destiny_info.destiny_memberships[0].membership_id

            # sometimes they don't have cross save set up yet have multiple entries
            if len(destiny_info.destiny_memberships) > 1:
                self.logger.warning(
                    f"User with destiny id `auth.destiny_membership_id` should set up cross save. Had to guess which one to use, since they have multiple accounts -> `{destiny_info.destiny_memberships}`"
                )
                auth.cross_save_setup = False
        auth.membership_id = int(auth.membership_id)

        # get the correct membership type and bungie name
        for entry in destiny_info.destiny_memberships:
            if entry.membership_id == auth.membership_id:
                auth.membership_type = entry.membership_type
                if not entry.bungie_global_display_name or not entry.bungie_global_display_name_code:
                    auth.bungie_name = None
                else:
                    auth.bungie_name = entry.full_bungie_name
        assert auth.membership_type is not MISSING

        # dispatch the update event
        task = asyncio.create_task(self.on_token_update(before=None, after=auth))
        self._tasks.add(task)
        task.add_done_callback(self._tasks.discard)

        return auth

    def _invalidate_token(self, auth: AuthData) -> None:
        """
        Invalidate a token

        Args:
            auth: The data to invalidate
        """

        if isinstance(auth, AuthData):
            old_auth = copy(auth)
            auth.token = None

            # dispatch the update event
            task = asyncio.create_task(self.on_token_update(before=old_auth, after=auth))
            self._tasks.add(task)
            task.add_done_callback(self._tasks.discard)

    async def get_working_auth(self, auth: AuthData) -> AuthData:
        """
        Check if tokens need to be refreshed and then do that.
        Gets called automatically when doing requests with AuthData.

        Tip: Staying up to date
            This dispatches the `Client.on_token_update()` event

        Args:
            auth: The potentially old authentication info.

        Raises:
            InvalidAuthentication: If authentication is invalid

        Returns:
            The working authentication info.
        """

        # locked this on a per-user basis
        if auth.membership_id not in token_update_lock:
            token_update_lock.update({auth.membership_id: asyncio.Lock()})
        async with token_update_lock[auth.membership_id]:
            # check that token exists
            if auth.token is None:
                raise InvalidAuthentication(auth=auth)

            # check if token is expired
            now = get_now_with_tz()
            if auth.token_expiry > (now - datetime.timedelta(minutes=5)):
                return auth

            # check the refresh token expiry
            if auth.refresh_token_expiry < (now - datetime.timedelta(minutes=5)):
                self._invalidate_token(auth=auth)
                raise InvalidAuthentication(auth=auth)

            old_auth = copy(auth)

            # refresh the data
            data = await self.http.refresh_access_token(auth=auth)
            auth.token = data["access_token"]
            auth.refresh_token = data["refresh_token"]
            auth.token_expiry = now + datetime.timedelta(seconds=data["expires_in"])
            auth.refresh_token_expiry = now + datetime.timedelta(seconds=data["refresh_expires_in"])

            # dispatch the update event
            task = asyncio.create_task(self.on_token_update(before=old_auth, after=auth))
            self._tasks.add(task)
            task.add_done_callback(self._tasks.discard)

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

        self.logger.info(f"Updated token for {before.membership_id=}: {before.token=} -> {after.token=}")

    async def on_manifest_update(self) -> None:
        """
        Dispatched whenever the manifest receives an update by bungie.
        This is checked for periodically when doing manifest dependant request.

        Tip: Subclassing
            It is highly recommended to subclass the Client and overwrite this function to suite your own needs
        """

        self.logger.info("Destiny manifest was updated by bungie")
