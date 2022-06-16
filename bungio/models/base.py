from __future__ import annotations

import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Optional

import attr
from sqlalchemy.orm import sessionmaker

import bungio.models as models

if TYPE_CHECKING:
    from bungio.client import Client


__all__ = (
    "MISSING",
    "BaseEnum",
    "BaseModel",
)


class MISSING:
    def __getattr__(self, *_) -> None:
        return None

    def __bool__(self) -> bool:
        return False


MISSING = MISSING()


class ManifestModel:
    pass


class BaseEnum(Enum):
    """
    Base methods which help to acquire this model from json and export it to json.
    """

    @staticmethod
    def process_dict(data: int | str, client: "Client", *args, **kwargs) -> int | str:
        """
        Enum specific cleanup

        Args:
            data: The int / str representation of the enum, usually received by bungie
            client: The client obj

        Returns:
            Clean int / str representation
        """
        return data

    @classmethod
    async def from_dict(cls, data: int | str, client: "Client", *args, **kwargs) -> BaseEnum:
        """
        Convert data to this enum

        Args:
            data: The int / str representation of the enum, usually received by bungie
            client: The client obj

        Returns:
            The enum
        """

        if isinstance(data, cls):
            return data

        data = cls.process_dict(data=data, client=client)
        return cls(data)


@attr.define(kw_only=True)
class BaseModel:
    """
    Base methods which help to acquire this model from json and export it to json.
    """

    _client: "Client" = attr.field(init=False)

    @staticmethod
    def process_dict(data: dict, client: "Client", *args, **kwargs) -> dict:
        """
        Model specific cleanup

        Args:
            data: The json representation of the model, usually received by bungie
            client: The client obj

        Returns:
            Clean json
        """
        return data

    @classmethod
    async def from_dict(cls, data: dict, client: "Client", recursive: bool = False, *args, **kwargs) -> BaseModel:
        """
        Convert json data to this model

        Args:
            data: The json representation of the model, usually received by bungie
            client: The client obj
            recursive: If this was called recursively

        Returns:
            The model
        """

        if isinstance(data, cls):
            return data

        if "Response" in data:
            data = data["Response"]

        data = cls.process_dict(data=data, client=client)

        prepared = {}
        for name, field in attr.fields_dict(cls).items():
            if field.init:
                # todo optional[]

                # get the value we want. This also skips the manifest_... entries since they have no value and a default
                value = data.get(cls._convert_to_bungie_case(name), attr.NOTHING)
                default = field.default

                # sadly bungie sometimes does not return info without marking that fact in the api specs
                if value is attr.NOTHING and default is attr.NOTHING:
                    default = MISSING

                if value is attr.NOTHING:
                    value = default

                else:
                    value = await cls._convert_to_type(
                        field_type=field.type, field_metadata=field.metadata, value=value, client=client
                    )

                # set the attr
                prepared[name] = value

        res = cls(**prepared)  # noqa
        res._client = client

        # fill the manifest information
        if not recursive and res._client.always_return_manifest_information:
            await res.fetch_manifest_information()

        return res

    @staticmethod
    async def _convert_to_type(field_type: Any, field_metadata: Optional[dict], value: Any, client: Client) -> Any:
        # sometimes the field type is the attr as a string
        if isinstance(field_type, str):
            field_type = getattr(models, field_type)

        # convert models in models
        if hasattr(field_type, "from_dict"):
            value = await field_type.from_dict(data=value, client=client, recursive=True)

        # convert datetime
        elif field_type == datetime.datetime:
            value = datetime.datetime.strptime(value, "%Y-%m-%dT%H:%M:%S%z")

        # convert lists / dict
        elif field_metadata:
            field_type = field_metadata["type"]

            # split the type into the subtypes
            split_types = field_metadata["type"].replace("]", "").replace('"', "").split("[")

            match split_types[0]:
                case "dict":
                    new_field_types = field_type.removeprefix("dict[").removesuffix("]").split(", ")
                    key_type = new_field_types[0]
                    value_type = new_field_types[1]

                    ret = {}
                    for key, value in value.items():
                        # they are only our custom models if there are " in it, otherwise
                        if '"' in key_type:
                            key = await BaseModel._convert_to_type(
                                field_type=key_type.replace('"', ""), field_metadata=None, value=key, client=client
                            )
                        if '"' in value_type:
                            value = await BaseModel._convert_to_type(
                                field_type=value_type.replace('"', ""), field_metadata=None, value=value, client=client
                            )

                        ret[key] = value
                    value = ret

                case "list":
                    value = [
                        await BaseModel._convert_to_type(
                            field_type=split_types[1], field_metadata=None, value=entry, client=client
                        )
                        for entry in value
                    ]

                case _:
                    raise ValueError(f"Unexpected type {split_types[0]} in {split_types}")

        return value

    @staticmethod
    def _convert_to_bungie_case(string: str) -> str:
        """
        Convert a string to how it is represented by bungie: my_name_string -> myNameString

        Args:
            string: The og string

        Returns:
            The bungie string
        """

        split = string.split("_")
        if len(split) == 1:
            return split[0]
        else:
            return "".join([split[0], *[s.capitalize() for s in split[1:]]])

    def to_dict(self) -> dict:
        # todo
        ...

    async def fetch_manifest_information(self):
        """
        Fill the model in-place with information from the manifest.
        """

        if not isinstance(self._client.manifest_storage, sessionmaker):
            raise ValueError("Client.manifest_storage must be set up to use this")

        class_definition = attr.fields_dict(type(self))  # noqa

        # loop through the attr attributes
        for name in attr.asdict(self):  # noqa
            if name.startswith("manifest_"):
                attr_definition = class_definition["name"]
                striped_name = name.removeprefix("manifest_")
                manifest_class_name = attr_definition.type.__str__().removesuffix("')]").split("'")[-1]
                manifest_value = await self._client.manifest.fetch(
                    manifest_class=getattr(models, manifest_class_name), value=getattr(self, striped_name)
                )

                # check if the model has manifest models itself
                if manifest_value:
                    await manifest_value.fetch_manifest_information()

                setattr(self, name, manifest_value)

        # todo recursive for child models which are Type["BaseModel"]
        # todo gather for speed
