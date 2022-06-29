from datetime import datetime

import attr

from bungio.models.base import BaseModel


@attr.define
class DateRange(BaseModel):
    """
    _No description given by bungie._

    None
    Attributes:
        end: _No description given by bungie._
        start: _No description given by bungie._
    """

    end: datetime = attr.field()
    start: datetime = attr.field()
