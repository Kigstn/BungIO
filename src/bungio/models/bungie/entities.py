# DO NOT CHANGE ANY CODE BELOW
# This file is generated automatically by `generate_api_schema.py` and will be overwritten
# Instead, change functions / models by subclassing them in the `./overwrites/` folder. They will be used instead.

from typing import Union, TYPE_CHECKING

from bungio.utils import enum_converter
from bungio.models.base import BaseModel, custom_define, custom_field


if TYPE_CHECKING:
    from bungio.models import PlatformErrorCodes


@custom_define()
class EntityActionResult(BaseModel):
    """
    _No description given by bungie._

    None
    Attributes:
        entity_id: _No description given by bungie._
        result: _No description given by bungie._
    """

    entity_id: int = custom_field(metadata={"int64": True})
    result: Union["PlatformErrorCodes", int] = custom_field(converter=enum_converter("PlatformErrorCodes"))
