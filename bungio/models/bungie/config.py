import datetime
from typing import TYPE_CHECKING, Any, Optional

import attr

from bungio.models.base import BaseEnum, BaseModel


@attr.define
class UserTheme(BaseModel):
    """
    Not specified.

    Attributes:
        user_theme_id: Not specified.
        user_theme_name: Not specified.
        user_theme_description: Not specified.
    """

    user_theme_id: int = attr.field()
    user_theme_name: str = attr.field()
    user_theme_description: str = attr.field()


@attr.define
class GroupTheme(BaseModel):
    """
    Not specified.

    Attributes:
        name: Not specified.
        folder: Not specified.
        description: Not specified.
    """

    name: str = attr.field()
    folder: str = attr.field()
    description: str = attr.field()
