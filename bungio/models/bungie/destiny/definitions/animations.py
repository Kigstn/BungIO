import datetime
from typing import TYPE_CHECKING, Any, Optional

import attr

from bungio.models.base import BaseEnum, BaseModel


@attr.define
class DestinyAnimationReference(BaseModel):
    """
    Not specified.

    Attributes:
        anim_name: Not specified.
        anim_identifier: Not specified.
        path: Not specified.
    """

    anim_name: str = attr.field()
    anim_identifier: str = attr.field()
    path: str = attr.field()
