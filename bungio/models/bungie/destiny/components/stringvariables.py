# DO NOT CHANGE ANY CODE BELOW
# This file is generated automatically by `generate_api_schema.py` and will be overwritten
# Instead, change functions / models by subclassing them in the `./overwrites/` folder. They will be used instead.

import attr

from bungio.models.base import BaseModel


@attr.define
class DestinyStringVariablesComponent(BaseModel):
    """
    _No description given by bungie._

    None
    Attributes:
        integer_values_by_hash: _No description given by bungie._
    """

    integer_values_by_hash: dict[int, int] = attr.field(metadata={"type": """dict[int, int]"""})
