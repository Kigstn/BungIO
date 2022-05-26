import datetime
from typing import TYPE_CHECKING, Any, Optional

import attr

from bungio.models.base import BaseEnum, BaseModel


@attr.define
class EntityActionResult(BaseModel):
    """
    Not specified.

    Attributes:
        entity_id: Not specified.
        result: Not specified.
    """

    entity_id: int = attr.field()
    result: int = attr.field()
