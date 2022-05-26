import datetime
from typing import TYPE_CHECKING, Any, Optional

import attr

from bungio.models.base import BaseEnum, BaseModel


@attr.define
class DestinyColor(BaseModel):
    """
    Represents a color whose RGBA values are all represented as values between 0 and 255.

    Attributes:
        red: Not specified.
        green: Not specified.
        blue: Not specified.
        alpha: Not specified.
    """

    red: int = attr.field()
    green: int = attr.field()
    blue: int = attr.field()
    alpha: int = attr.field()
