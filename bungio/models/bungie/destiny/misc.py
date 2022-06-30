# DO NOT CHANGE ANY CODE BELOW
# This file is generated automatically by `generate_api_schema.py` and will be overwritten
# Instead, change functions / models by subclassing them in the `./overwrites/` folder. They will be used instead.

import attr

from bungio.models.base import BaseModel


@attr.define
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

    alpha: int = attr.field()
    blue: int = attr.field()
    green: int = attr.field()
    red: int = attr.field()
