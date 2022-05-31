import attr

from bungio.models.base import BaseEnum, BaseModel


@attr.define
class IgnoreResponse(BaseModel):
    """
    _No description given_

    Attributes:
        is_ignored: _No description given_
        ignore_flags: _No description given_
    """

    is_ignored: bool = attr.field()
    ignore_flags: int = attr.field()


class IgnoreStatus(BaseEnum):
    """
    _No description given_
    """

    NOT_IGNORED = 0
    """_No description given_ """
    IGNORED_USER = 1
    """_No description given_ """
    IGNORED_GROUP = 2
    """_No description given_ """
    IGNORED_BY_GROUP = 4
    """_No description given_ """
    IGNORED_POST = 8
    """_No description given_ """
    IGNORED_TAG = 16
    """_No description given_ """
    IGNORED_GLOBAL = 32
    """_No description given_ """


class IgnoreLength(BaseEnum):
    """
    _No description given_
    """

    NONE = 0
    """_No description given_ """
    WEEK = 1
    """_No description given_ """
    TWO_WEEKS = 2
    """_No description given_ """
    THREE_WEEKS = 3
    """_No description given_ """
    MONTH = 4
    """_No description given_ """
    THREE_MONTHS = 5
    """_No description given_ """
    SIX_MONTHS = 6
    """_No description given_ """
    YEAR = 7
    """_No description given_ """
    FOREVER = 8
    """_No description given_ """
    THREE_MINUTES = 9
    """_No description given_ """
    HOUR = 10
    """_No description given_ """
    THIRTY_DAYS = 11
    """_No description given_ """
