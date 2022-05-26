import datetime
from typing import TYPE_CHECKING, Any, Optional

import attr

from bungio.models.base import BaseEnum, BaseModel


@attr.define
class TagResponse(BaseModel):
    """
    Not specified.

    Attributes:
        tag_text: Not specified.
        ignore_status: Not specified.
    """

    tag_text: str = attr.field()
    ignore_status: "IgnoreResponse" = attr.field()
