import datetime
from typing import TYPE_CHECKING, Any, Optional

import attr

from bungio.models.base import BaseEnum, BaseModel


@attr.define
class IgnoreResponse(BaseModel):
    """
    Not specified.

    Attributes:
        is_ignored: Not specified.
        ignore_flags: Not specified.
    """

    is_ignored: bool = attr.field()
    ignore_flags: int = attr.field()


class IgnoreStatus(BaseEnum):
    """
    Not specified.
    """

    NOT_IGNORED = 0
    """Not specified. """
    IGNORED_USER = 1
    """Not specified. """
    IGNORED_GROUP = 2
    """Not specified. """
    IGNORED_BY_GROUP = 4
    """Not specified. """
    IGNORED_POST = 8
    """Not specified. """
    IGNORED_TAG = 16
    """Not specified. """
    IGNORED_GLOBAL = 32
    """Not specified. """


class IgnoreLength(BaseEnum):
    """
    Not specified.
    """

    NONE = 0
    """Not specified. """
    WEEK = 1
    """Not specified. """
    TWO_WEEKS = 2
    """Not specified. """
    THREE_WEEKS = 3
    """Not specified. """
    MONTH = 4
    """Not specified. """
    THREE_MONTHS = 5
    """Not specified. """
    SIX_MONTHS = 6
    """Not specified. """
    YEAR = 7
    """Not specified. """
    FOREVER = 8
    """Not specified. """
    THREE_MINUTES = 9
    """Not specified. """
    HOUR = 10
    """Not specified. """
    THIRTY_DAYS = 11
    """Not specified. """
