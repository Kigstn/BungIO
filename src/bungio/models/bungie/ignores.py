# DO NOT CHANGE ANY CODE BELOW
# This file is generated automatically by `generate_api_schema.py` and will be overwritten
# Instead, change functions / models by subclassing them in the `./overwrites/` folder. They will be used instead.

from typing import Union

from bungio.models.base import BaseEnum, BaseFlagEnum, BaseModel, custom_define, custom_field
from bungio.utils import enum_converter


@custom_define()
class IgnoreResponse(BaseModel):
    """
    _No description given by bungie._

    None
    Attributes:
        ignore_flags: _No description given by bungie._
        is_ignored: _No description given by bungie._
    """

    ignore_flags: Union["IgnoreStatus", int] = custom_field(converter=enum_converter("IgnoreStatus"))
    is_ignored: bool = custom_field()


class IgnoreStatus(BaseFlagEnum):
    """
    _No description given by bungie._
    """

    NOT_IGNORED = 0
    """_No description given by bungie._ """
    IGNORED_USER = 1
    """_No description given by bungie._ """
    IGNORED_GROUP = 2
    """_No description given by bungie._ """
    IGNORED_BY_GROUP = 4
    """_No description given by bungie._ """
    IGNORED_POST = 8
    """_No description given by bungie._ """
    IGNORED_TAG = 16
    """_No description given by bungie._ """
    IGNORED_GLOBAL = 32
    """_No description given by bungie._ """


class IgnoreLength(BaseEnum):
    """
    _No description given by bungie._
    """

    NONE = 0
    """_No description given by bungie._ """
    WEEK = 1
    """_No description given by bungie._ """
    TWO_WEEKS = 2
    """_No description given by bungie._ """
    THREE_WEEKS = 3
    """_No description given by bungie._ """
    MONTH = 4
    """_No description given by bungie._ """
    THREE_MONTHS = 5
    """_No description given by bungie._ """
    SIX_MONTHS = 6
    """_No description given by bungie._ """
    YEAR = 7
    """_No description given by bungie._ """
    FOREVER = 8
    """_No description given by bungie._ """
    THREE_MINUTES = 9
    """_No description given by bungie._ """
    HOUR = 10
    """_No description given by bungie._ """
    THIRTY_DAYS = 11
    """_No description given by bungie._ """
