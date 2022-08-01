# DO NOT CHANGE ANY CODE BELOW
# This file is generated automatically by `generate_api_schema.py` and will be overwritten
# Instead, change functions / models by subclassing them in the `./overwrites/` folder. They will be used instead.

from datetime import datetime
from typing import TYPE_CHECKING, Any, Optional, Union

from bungio.models.base import (
    BaseEnum,
    BaseFlagEnum,
    BaseModel,
    HashObject,
    ManifestModel,
    custom_define,
    custom_field,
)
from bungio.utils import enum_converter


@custom_define()
class DestinyStringVariablesComponent(BaseModel):
    """
    _No description given by bungie._

    None
    Attributes:
        integer_values_by_hash: _No description given by bungie._
    """

    integer_values_by_hash: dict[int, int] = custom_field(metadata={"type": """dict[int, int]"""})
