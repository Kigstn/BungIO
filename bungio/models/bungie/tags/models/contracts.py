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

if TYPE_CHECKING:
    from bungio.models import IgnoreResponse


@custom_define()
class TagResponse(BaseModel):
    """
    _No description given by bungie._

    None
    Attributes:
        ignore_status: _No description given by bungie._
        tag_text: _No description given by bungie._
    """

    ignore_status: "IgnoreResponse" = custom_field()
    tag_text: str = custom_field()
