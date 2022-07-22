from __future__ import annotations

import datetime
import inspect
from enum import Enum, IntEnum, IntFlag
from typing import TYPE_CHECKING, Any, Optional, Type, _UnionGenericAlias

import attr
from sqlalchemy.ext.asyncio import AsyncEngine

import bungio.models as models

if TYPE_CHECKING:
    from bungio.client import Client

__all__ = (
    "MISSING",
    "BaseEnum",
    "BaseFlagEnum",
    "BaseModel",
    "ManifestModel",
    "ClientMixin",
    "UnknownEnumValue",
    "FuzzyAttrFinder",
    "EnumMixin",
)


class MISSING:
    """
    A missing entry which was not returned by bungie whatsoever.
    """

    def __bool__(self) -> bool:
        return False


MISSING = MISSING()


@attr.define
class UnknownEnumValue:
    """
    Sometimes Bungie returns information that they have not defined anywhere, so this has to do
    """

    value: int | str = attr.field()
    enum: Type[BaseEnum] = attr.field()


class EnumMixin(Enum):
    """
    Mixin for enums
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
    async def from_dict(cls, data: int | str, client: "Client", *args, **kwargs) -> EnumMixin | UnknownEnumValue:
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

        # catch unknown values
        try:
            return cls(data)
        except ValueError:
            return UnknownEnumValue(value=data, enum=cls)

    def to_dict(self) -> Any:
        """
        Convert the enum into a representation bungie accepts

        Returns:
            The value which can be sent to bungie
        """

        return self.value


class BaseEnum(EnumMixin, Enum):
    """
    Base methods which help to acquire this model from json and export it to json.
    """

    pass


class BaseFlagEnum(EnumMixin, IntFlag):
    """
    Base methods which help to acquire this model from json and export it to json.
    """

    pass


@attr.define
class ClientMixin:
    """
    Mixin that give models access to the client obj
    """

    _client: "Client" = attr.field(repr=False, init=False)

    @_client.default
    def __client_factory(self) -> "Client":
        from bungio.singleton import client

        if client is MISSING:
            raise ValueError("You have to set-up your 'Client' first")
        return client


@attr.define
class FuzzyAttrFinder:
    def _fuzzy_getattr(self, name: str) -> Any:
        """
        Returns the objs attribute that fully matches the name, or if that does not exist, the first attribute that includes the name

        Args:
            name: The name to match

        Raises:
            KeyError: If no match is found

        Returns:
            The attribute value
        """

        try:
            found_attr = getattr(self, name)
            return found_attr
        except AttributeError:
            for attr_name in self.__dir__():
                if name in attr_name:
                    return getattr(self, attr_name)
            raise KeyError(f"`{name}` not found in `{self.__dir__()}`")


@attr.define(kw_only=True)
class BaseModel(ClientMixin):
    """
    Base methods which help to acquire this model from json and export it to json.
    """

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

        if not isinstance(data, dict):
            raise ValueError

        if "Response" in data:
            data = data["Response"]

        # also use the kwargs as data
        data = kwargs | data
        data = cls.process_dict(data=data, client=client)

        prepared = {}
        for name, field in attr.fields_dict(cls).items():
            if field.init and name != "_client":
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

        # fill the manifest information
        if not recursive and res._client.always_return_manifest_information:
            await res.fetch_manifest_information()

        return res

    @staticmethod
    async def _convert_to_type(field_type: Any, field_metadata: Optional[dict], value: Any, client: Client) -> Any:
        # catch optional
        if isinstance(field_type, _UnionGenericAlias) and "Optional" in str(field_type):
            if value is None:
                return value
            field_type = str(field_type).removeprefix("typing.Optional[").removesuffix("]")

        # sometimes the field type is the attr as a string
        if isinstance(field_type, str):
            # catch build-ins
            if field_type in ["dict", "int", "str", "Any", "float", "bool"]:
                return value
            else:
                field_type = getattr(models, field_type)

        # convert models in models
        if hasattr(field_type, "from_dict"):
            value = await field_type.from_dict(data=value, client=client, recursive=True)

        # convert datetime
        elif field_type == datetime.datetime:
            # sometimes this includes milliseconds
            try:
                value = datetime.datetime.strptime(value, "%Y-%m-%dT%H:%M:%S%z")
            except ValueError:
                value = datetime.datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f%z")

        # convert lists / dict
        elif field_metadata:
            field_type = field_metadata["type"]

            # iterables:
            if "dict" in field_metadata["type"] or "list" in field_metadata["type"]:
                # split the type into the subtypes
                split_types = field_metadata["type"].replace("]", "").split("[")

                match split_types[0]:
                    case "dict":
                        # sometimes unknown dicts are returned
                        if field_type != "dict":
                            new_field_metadata = None
                            new_field_types = field_type.removeprefix("dict[").removesuffix("]").split(", ")
                            key_type = new_field_types[0]
                            value_type = ", ".join(new_field_types[1:])

                            # catch nested dicts
                            if "dict[" in value_type:
                                new_field_metadata = {"type": value_type}
                                value_type = None

                            ret = {}
                            for key, value in value.items():
                                key = await BaseModel._convert_to_type(
                                    field_type=key_type,
                                    field_metadata=new_field_metadata,
                                    value=key,
                                    client=client,
                                )
                                value = await BaseModel._convert_to_type(
                                    field_type=value_type,
                                    field_metadata=new_field_metadata,
                                    value=value,
                                    client=client,
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

            # enums
            else:
                value = await BaseModel._convert_to_type(
                    field_type=field_metadata["type"].replace('"', ""),
                    field_metadata=None,
                    value=value,
                    client=client,
                )

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
        """
        Convert the model into a dict representation bungie accepts

        Returns:
            A dict which can be sent to bungie
        """

        result = {}

        for name in self.__dir__():
            if name.startswith("_") or name.startswith("manifest_"):
                continue

            value = getattr(self, name)

            if inspect.ismethod(value) or inspect.isfunction(value):
                continue

            elif isinstance(value, dict):
                raise NotImplementedError(
                    "Nested dict conversion is not currently implemented, since bungie does never require that info"
                )

            elif isinstance(value, list):
                list_results = []
                for entry in value:
                    if hasattr(entry, "to_dict"):
                        list_results.append(entry.to_dict())
                    else:
                        list_results.append(entry)

                result[name] = list_results

            else:
                if hasattr(value, "to_dict"):
                    result[name] = value.to_dict()
                else:
                    result[name] = value

        return result

    async def fetch_manifest_information(self, _cache: Optional[dict] = None):
        """
        Fill the model in-place with information from the manifest.
        """

        if not isinstance(self._client.manifest_storage, AsyncEngine):
            raise ValueError("Client.manifest_storage must be set up to use this")

        if not _cache:
            _cache = {}

        class_definition = attr.fields_dict(type(self))  # noqa

        # loop through the class attributes
        for name in self.__dir__():
            if name.startswith("__"):
                continue

            # manifest entries
            if name.startswith("manifest_"):
                striped_name = name.removeprefix("manifest_")
                value = getattr(self, striped_name)

                if value is MISSING:
                    return

                # check the cache to avoid infinite recursion
                if cached := _cache.get(value, None):
                    manifest_value = cached

                else:
                    attr_definition = class_definition[name]
                    manifest_class_name = attr_definition.type.__str__().removesuffix("')]").split("'")[-1]
                    manifest_value = await self._client.manifest.fetch(
                        manifest_class=getattr(models, manifest_class_name), value=value
                    )

                    _cache[value] = manifest_value

                    # check if the model has manifest models itself
                    if manifest_value:
                        await manifest_value.fetch_manifest_information(_cache=_cache)

                setattr(self, name, manifest_value)

            # sub models which may have manifest entries too
            elif hasattr((value := getattr(self, name)), "fetch_manifest_information"):
                await value.fetch_manifest_information(_cache=_cache)


@attr.define
class ManifestModel(BaseModel):
    pass
