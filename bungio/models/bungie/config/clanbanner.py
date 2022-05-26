import datetime
from typing import TYPE_CHECKING, Any, Optional

import attr

from bungio.models.base import BaseEnum, BaseModel


@attr.define
class ClanBannerDecal(BaseModel):
    """
    Not specified.

    Attributes:
        identifier: Not specified.
        foreground_path: Not specified.
        background_path: Not specified.
    """

    identifier: str = attr.field()
    foreground_path: str = attr.field()
    background_path: str = attr.field()
