import datetime
from typing import TYPE_CHECKING, Any, Optional

import attr

from bungio.models.base import BaseEnum, BaseModel


@attr.define
class DateRange(BaseModel):
    """
    Not specified.

    Attributes:
        start: Not specified.
        end: Not specified.
    """

    start: datetime.datetime = attr.field()
    end: datetime.datetime = attr.field()
