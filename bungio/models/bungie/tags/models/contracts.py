# DO NOT CHANGE ANY CODE BELOW
# This file is generated automatically by `generate_api_schema.py` and will be overwritten
# Instead, change functions / models by subclassing them in the `./overwrites/` folder. They will be used instead.

from typing import TYPE_CHECKING

import attr

from bungio.models.base import BaseModel

if TYPE_CHECKING:
    from bungio.models import IgnoreResponse


@attr.define
class TagResponse(BaseModel):
    """
    _No description given by bungie._

    None
    Attributes:
        ignore_status: _No description given by bungie._
        tag_text: _No description given by bungie._
    """

    ignore_status: "IgnoreResponse" = attr.field()
    tag_text: str = attr.field()
