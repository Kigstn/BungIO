import asyncio
from typing import TYPE_CHECKING, Any, Optional, Text, Type

import attr
from sqlalchemy import JSON, Column, MetaData, Table, select, text
from sqlalchemy.exc import MultipleResultsFound
from sqlalchemy.ext.asyncio import AsyncConnection
from sqlalchemy.sql.ddl import CreateTable

from bungio.http.route import Route

if TYPE_CHECKING:
    from bungio.client import Client
    from bungio.models.base import BaseModel, ManifestModel

metadata = MetaData()
lock = asyncio.Lock()


@attr.define
class Manifest:
    _client: "Client" = attr.field()
    __saved_manifests: dict[str, Table] = attr.field(init=False, factory=dict)
    __manifest_urls: dict[str, str] = attr.field(init=False, factory=dict)

    async def synchronise_with_db(self):
        # todo version table
        # todo check which tables exist
        # todo download the manifest and compare versions
        # todo if version is different, delete all tables that start with "destiny_manifest_"
        # todo fill self.__saved_manifests
        # todo save the manifest links in self.__manifest_urls
        # todo lock this entire thing while a manifest update is checked for, maybe by awaiting it the fetch method. The update dattime needs to be saved then
        ...

    async def fetch(self, manifest_class: Type[ManifestModel], value: str) -> Optional["BaseModel"]:
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

        await self.download(manifest_class=manifest_class)

        # get the data
        async with self._client.manifest_storage.begin() as db:
            result = await db.execute(
                self.__saved_manifests[name].select().where(self.__saved_manifests[name].reference_id == str(value))
            )  # noqa
            try:
                result = result.scalars().one_or_none()
            except MultipleResultsFound:
                return None

            return await manifest_class.from_dict(data=result.data, client=self._client)  # noqa

    async def download(self, manifest_class: Type[ManifestModel] | str):
        """
        Download and save the manifest with the given name

        Args:
            manifest_class: The class / name of the manifest
        """

        if not isinstance(manifest_class, str):
            manifest_class = manifest_class.__name__

        async with lock:
            # create the table if that does not exist yet
            if manifest_class not in self.__saved_manifests:
                async with self._client.manifest_storage.begin() as db:
                    self.__saved_manifests[manifest_class] = Table(
                        f"destiny_manifest_{manifest_class}",
                        metadata,
                        Column("reference_id", Text, nullable=False, primary_key=True),
                        Column("data", JSON, nullable=False),
                    )
                    await db.execute(CreateTable(self.__saved_manifests[manifest_class]))

                    # fill the table
                    await self._download(db=db, name=manifest_class)

    async def _download(self, db: AsyncConnection, name: str):
        """
        Download and save the manifest with the given name

        Args:
            db: The db connection
            name: The name of the manifest
        """

        url = self.__manifest_urls[name]
        table = self.__saved_manifests[name]

        raw_data = await self._client.http.request(Route(path=url, method="GET"))

        # loop through the items and add them
        for key, data in raw_data.items():
            await db.execute(table.insert().values(reference_id=str(key), data=data))
