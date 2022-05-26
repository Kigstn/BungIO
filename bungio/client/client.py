import logging
from base64 import b64encode
from typing import TYPE_CHECKING, Callable, Optional

import attr
from aiohttp import ClientSession, DummyCookieJar
from sqlalchemy.orm import sessionmaker

from bungio.definitions import LOGGER_NAME
from bungio.http.client import HttpClient
from bungio.models.auth import AuthData
from bungio.models.enums import BungieLanguage

if TYPE_CHECKING:
    from aiohttp_client_cache import CacheBackend
    from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine

__all__ = ("Client",)

# define json loading technique
try:
    import orjson

    def json_dumps(x):
        orjson.dumps(x).decode()

    json_loads = orjson.loads
except ModuleNotFoundError:
    import json

    json_dumps = json.dumps
    json_loads = json.loads


default_logger = logging.getLogger(LOGGER_NAME)
default_logger.setLevel(logging.ERROR)


@attr.define
class Client:
    """
    The api client

    Attributes:
        client_id: The bungie.net client id
        client_secret: The bungie.net client secret
        token: The bungie.net token
    """

    client_id: str = attr.field()
    client_secret: str = attr.field()
    token: str = attr.field()

    logger: logging.Logger = attr.field(default=default_logger)

    language: BungieLanguage = attr.field(default=BungieLanguage.ENGLISH)

    cache: Optional["CacheBackend"] = attr.field(default=None)
    use_manifest: bool | sessionmaker = attr.field(default=False)

    json_dumps: Callable = attr.field(init=False, default=json_dumps)
    json_loads: Callable = attr.field(init=False, default=json_loads)

    _http: HttpClient = attr.field(init=False)

    @use_manifest.validator  # noqa
    def use_manifest_check(self, attribute, value):
        if isinstance(value, sessionmaker):
            if not isinstance(value.class_, AsyncSession):
                raise ValueError(f"{attribute} obj must be bound to an async session")

    @language.validator  # noqa
    def language_check(self, attribute, value):
        if not isinstance(value, BungieLanguage):
            raise ValueError(f"{attribute} must be an instance of type BungieLanguage")

    def __attrs_post_init__(self):
        if self.use_manifest is True:
            engine = create_async_engine("sqlite+aiosqlite:///manifest.db")
            self.use_manifest = sessionmaker(bind=engine, class_=AsyncSession, future=True)

        # set up the http client
        self._http = HttpClient()
        self._http._client = self
        self._http._bungie_auth_headers = {
            "User-Agent": "BungIO",
            "Content-Type": "application/x-www-form-urlencoded",
            "Authorization": f"""Basic {b64encode(f"{self.client_id}:{self.client_secret}".encode()).decode()}""",
            "Accept": "application/json",
        }
        self._http._bungie_headers = {
            "User-Agent": "BungIO",
            "X-API-Key": self.token,
            "Accept": "application/json",
        }
        try:
            from aiohttp_client_cache import CachedSession

            self._http.__session = CachedSession(
                json_serialize=self.json_dumps, cookie_jar=DummyCookieJar(), cache=self.cache
            )
        except ModuleNotFoundError:
            self._http.__session = ClientSession(json_serialize=self.json_dumps, cookie_jar=DummyCookieJar())

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

        return f"https://www.bungie.net/en/oauth/authorize?client_id={self.client_id}&response_type=code&state={state}"

    async def on_token_update(self, before: AuthData, after: AuthData) -> None:
        """
        Dispatched whenever a token is updated

        Tip: Subclassing
            It is highly recommended to subclass the Client and overwrite this function to suite your own needs

        Args:
            before: The old auth info
            after: The new auth info
        """

        self.logger.info(f"Updated token for {before.destiny_membership_id=}: {before.token=} -> {after.token=}")
