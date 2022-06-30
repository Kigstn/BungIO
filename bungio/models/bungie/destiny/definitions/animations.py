# DO NOT CHANGE ANY CODE BELOW
# This file is generated automatically by `generate_api_schema.py` and will be overwritten
# Instead, change functions / models by subclassing them in the `./overwrites/` folder. They will be used instead.

import attr

from bungio.models.base import BaseModel


@attr.define
class DestinyAnimationReference(BaseModel):
    """
    _No description given by bungie._

    None
    Attributes:
        anim_identifier: _No description given by bungie._
        anim_name: _No description given by bungie._
        path: _No description given by bungie._
    """

    anim_identifier: str = attr.field()
    anim_name: str = attr.field()
    path: str = attr.field()
