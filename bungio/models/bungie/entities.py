# DO NOT CHANGE ANY CODE BELOW
# This file is generated automatically by `generate_api_schema.py` and will be overwritten
# Instead, change functions / models by subclassing them in the `./overwrites/` folder. They will be used instead.

from typing import TYPE_CHECKING, Union

import attr

from bungio.models.base import BaseModel
from bungio.utils import enum_converter

if TYPE_CHECKING:
    from bungio.models import PlatformErrorCodes


@attr.define
class EntityActionResult(BaseModel):
    """
    _No description given by bungie._

    None
    Attributes:
        entity_id: _No description given by bungie._
        result: _No description given by bungie._
    """

    entity_id: int = attr.field()
    result: Union["PlatformErrorCodes", int] = attr.field(converter=enum_converter("PlatformErrorCodes"))
