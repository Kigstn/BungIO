import attr

from bungio.models.base import BaseEnum, BaseModel


@attr.define
class IgnoreResponse(BaseModel):
    """
    _No description given by bungie_

    Attributes:
        is_ignored: _No description given by bungie_
        ignore_flags: _No description given by bungie_
    """

    is_ignored: bool = attr.field()
    ignore_flags: "IgnoreStatus" = attr.field()


class IgnoreStatus(BaseEnum):
    """
    _No description given by bungie_
    """

    NOT_IGNORED = 0
    """_No description given by bungie_ """
    IGNORED_USER = 1
    """_No description given by bungie_ """
    IGNORED_GROUP = 2
    """_No description given by bungie_ """
    IGNORED_BY_GROUP = 4
    """_No description given by bungie_ """
    IGNORED_POST = 8
    """_No description given by bungie_ """
    IGNORED_TAG = 16
    """_No description given by bungie_ """
    IGNORED_GLOBAL = 32
    """_No description given by bungie_ """


class IgnoreLength(BaseEnum):
    """
    _No description given by bungie_
    """

    NONE = 0
    """_No description given by bungie_ """
    WEEK = 1
    """_No description given by bungie_ """
    TWO_WEEKS = 2
    """_No description given by bungie_ """
    THREE_WEEKS = 3
    """_No description given by bungie_ """
    MONTH = 4
    """_No description given by bungie_ """
    THREE_MONTHS = 5
    """_No description given by bungie_ """
    SIX_MONTHS = 6
    """_No description given by bungie_ """
    YEAR = 7
    """_No description given by bungie_ """
    FOREVER = 8
    """_No description given by bungie_ """
    THREE_MINUTES = 9
    """_No description given by bungie_ """
    HOUR = 10
    """_No description given by bungie_ """
    THIRTY_DAYS = 11
    """_No description given by bungie_ """
