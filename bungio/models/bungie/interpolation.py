import datetime
from typing import TYPE_CHECKING, Any, Optional

import attr

from bungio.models.base import BaseEnum, BaseModel


@attr.define
class InterpolationPoint(BaseModel):
    """
    Not specified.

    Attributes:
        value: Not specified.
        weight: Not specified.
    """

    value: int = attr.field()
    weight: int = attr.field()


@attr.define
class InterpolationPointFloat(BaseModel):
    """
    Not specified.

    Attributes:
        value: Not specified.
        weight: Not specified.
    """

    value: float = attr.field()
    weight: float = attr.field()
