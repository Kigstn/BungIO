import asyncio
import datetime
from typing import TYPE_CHECKING, Optional, Type

import attr
from sqlalchemy import JSON, Column, Table, Text, select
from sqlalchemy.exc import MultipleResultsFound
from sqlalchemy.ext.asyncio import AsyncConnection
from sqlalchemy.sql.ddl import CreateTable, DropTable

from bungio.http.route import Route
from bungio.models.base import ClientMixin
from bungio.utils import get_now_with_tz

if TYPE_CHECKING:
    from bungio.models.base import BaseModel, ManifestModel

__all__ = ("Manifest",)


@attr.define
class Manifest(ClientMixin):
    """
    The connector to all manifest data
    """

    __synchronised: bool = attr.field(init=False, default=False)
    __saved_manifests: dict[str, Table] = attr.field(init=False, factory=dict)
    __manifest_urls: dict[str, str] = attr.field(init=False, factory=dict)
    __locks: dict[str, asyncio.Lock] = attr.field(init=False, factory=dict)
    __manifest_lock: asyncio.Lock = attr.field(init=False, default=asyncio.Lock())
    __synchronise_lock: asyncio.Lock = attr.field(init=False, default=asyncio.Lock())
    __manifest_last_update: datetime.datetime = attr.field(init=False, default=None)
    __version_table: Table = attr.field(init=False)

    def __attrs_post_init__(self):
        # noinspection PyProtectedMember
        self.__version_table = Table(
            "destiny_manifest_version",
            self._client._metadata,
            Column("version", Text, nullable=False, primary_key=True),
        )

    async def _synchronise_with_db(self):
        """
        Synchronise this client with the tables existing in the db
        """

        async with self.__synchronise_lock:
            if self.__synchronised:
                return

            db: AsyncConnection
            async with self._client.manifest_storage.begin() as db:
                # noinspection PyProtectedMember
                await db.run_sync(self._client._metadata.reflect)

                # create version table if that does not exist
                await db.execute(CreateTable(self.__version_table, if_not_exists=True))

                # noinspection PyProtectedMember
                # get all existing db tables
                for table_name, table in self._client._metadata.tables.items():
                    if table_name.startswith("destiny_manifest_") and table_name != "destiny_manifest_version":
                        self.__saved_manifests[table_name.removeprefix("destiny_manifest_")] = table

            await self._check_for_updates()
            self.__synchronised = True

    async def fetch(self, manifest_class: Type["ManifestModel"], value: str) -> Optional["BaseModel"]:
        """
        Convert raw bungie data to the information defined in the manifest

        Args:
            manifest_class: The class the value should be converted to
            value: The value that references a manifest entry

        Returns:
            The manifest information, if found
        """

        db: AsyncConnection
        name = manifest_class.__name__

        if not self.__synchronised:
            await self._synchronise_with_db()

        await self.download(manifest_class=manifest_class)

        # get the data
        async with self._client.manifest_storage.begin() as db:
            query = select(self.__saved_manifests[name].columns.data).filter(
                self.__saved_manifests[name].columns.reference_id == str(value)
            )
            result = await db.execute(query)
            try:
                result = result.scalars().one_or_none()
            except MultipleResultsFound:
                return None

            return await manifest_class.from_dict(data=result, client=self._client, recursive=True)

    async def download(self, manifest_class: Type["ManifestModel"] | str):
        """
        Download and save the manifest with the given name

        Args:
            manifest_class: The class / name of the manifest
        """

        if not isinstance(manifest_class, str):
            manifest_class = manifest_class.__name__

        # lock this
        if manifest_class not in self.__locks:
            self.__locks[manifest_class] = asyncio.Lock()

        async with self.__locks[manifest_class]:
            await self._check_for_updates()

            # create the table if that does not exist yet
            if manifest_class not in self.__saved_manifests:
                async with self._client.manifest_storage.begin() as db:
                    # noinspection PyProtectedMember
                    self.__saved_manifests[manifest_class] = Table(
                        f"destiny_manifest_{manifest_class}",
                        self._client._metadata,
                        Column("reference_id", Text, nullable=False, primary_key=True),
                        Column("data", JSON, nullable=False),
                    )
                    await db.execute(CreateTable(self.__saved_manifests[manifest_class]))

                    # fill the table
                    raw_data = await self._client.http.request(
                        Route(path=self.__manifest_urls[manifest_class], method="GET")
                    )
                    to_insert = [{"reference_id": str(key), "data": data} for key, data in raw_data.items()]

                    await db.execute(self.__saved_manifests[manifest_class].insert(), to_insert)

    async def _check_for_updates(self):
        """
        Checks if there is an updated version of the manifest available (hourly)
        """

        now = get_now_with_tz()
        async with self.__manifest_lock:
            if self.__manifest_last_update is None or self.__manifest_last_update < (now - datetime.timedelta(hours=1)):
                manifest = await self._client.api.get_destiny_manifest()

                async with self._client.manifest_storage.begin() as db:
                    res = await db.execute(self.__version_table.select())
                    version = res.scalars().first()

                    if not version or version != manifest.version:
                        # delete tables
                        for table in self.__saved_manifests.values():
                            await db.execute(DropTable(table))
                        self.__saved_manifests = {}

                        # update version
                        await db.execute(self.__version_table.delete())
                        await db.execute(self.__version_table.insert().values(version=manifest.version))

                # set the urls
                self.__manifest_urls = {}
                for name, url in manifest.json_world_component_content_paths[self._client.language.value].items():
                    self.__manifest_urls[name] = url

            self.__manifest_last_update = now
