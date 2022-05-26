import datetime
from typing import TYPE_CHECKING, Any, Optional

import attr

from bungio.models.base import BaseEnum, BaseModel


@attr.define
class HyperlinkReference(BaseModel):
    """
    Not specified.

    Attributes:
        title: Not specified.
        url: Not specified.
    """

    title: str = attr.field()
    url: str = attr.field()
