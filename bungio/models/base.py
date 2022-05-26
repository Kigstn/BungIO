from __future__ import annotations

from enum import Enum
from typing import TYPE_CHECKING

import attr

if TYPE_CHECKING:
    from bungio.client import Client


# todo base enum
@attr.define(kw_only=True)
class BaseEnum(Enum):
    pass


@attr.define(kw_only=True)
class BaseModel:
    _client: "Client" = attr.field(init=False)

    @staticmethod
    def process_dict(data: dict, client: "Client") -> dict:
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
    def from_dict(cls, data: dict, client: "Client") -> BaseModel:
        """
        Convert json data to this model

        Args:
            data: The json representation of the model, usually received by bungie
            client: The client obj

        Returns:
            The model
        """

        if isinstance(data, cls):
            return data

        data = cls.process_dict(data=data, client=client)

        prepared = {}
        for name, field in attr.fields_dict(cls).items():
            if field.init:
                # get the value we want
                value = data.get(name, attr.NOTHING)
                default = field.default
                if value is attr.NOTHING and default is attr.NOTHING:
                    raise ValueError(
                        f"Did not receive required init field without default `{name}` for class `{cls.__name__}` in `{data}`"
                    )

                if value is attr.NOTHING:
                    value = default

                else:
                    # convert models in models
                    if hasattr(field.type, "from_dict"):
                        value = field.type.from_dict(data=value, client=client)

                # set the attr
                prepared[name] = value

        res = cls(**prepared)
        res._client = client
        return res
