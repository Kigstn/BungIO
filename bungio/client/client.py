from typing import TYPE_CHECKING, Optional

import attr
from sqlalchemy.orm import sessionmaker

from bungio.http.client import HttpClient
from bungio.models.enums import BungieLanguage

if TYPE_CHECKING:
    from aiohttp_client_cache import CacheBackend
    from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine

__all__ = ("Client",)


@attr.s()
class Client:
    """
    The api client
    """

    language: BungieLanguage = attr.field(default=BungieLanguage.ENGLISH)

    cache: Optional["CacheBackend"] = attr.field(default=None)
    use_manifest: bool | sessionmaker = attr.field(default=False)

    _http: HttpClient = attr.field(init=False, default=HttpClient())

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
