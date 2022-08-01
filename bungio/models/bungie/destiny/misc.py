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
class DestinyColor(BaseModel):
    """
    Represents a color whose RGBA values are all represented as values between 0 and 255.

    None
    Attributes:
        alpha: _No description given by bungie._
        blue: _No description given by bungie._
        green: _No description given by bungie._
        red: _No description given by bungie._
    """

    alpha: int = custom_field()
    blue: int = custom_field()
    green: int = custom_field()
    red: int = custom_field()
