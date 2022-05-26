import datetime
from typing import TYPE_CHECKING, Any, Optional

import attr

from bungio.models.base import BaseEnum, BaseModel


@attr.define
class DestinyStringVariablesComponent(BaseModel):
    """
    Not specified.

    Attributes:
        integer_values_by_hash: Not specified.
    """

    integer_values_by_hash: Any = attr.field()
