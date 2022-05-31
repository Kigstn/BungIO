import datetime

import attr

from bungio.models.base import BaseModel


@attr.define
class DateRange(BaseModel):
    """
    _No description given_

    Attributes:
        start: _No description given_
        end: _No description given_
    """

    start: datetime.datetime = attr.field()
    end: datetime.datetime = attr.field()
