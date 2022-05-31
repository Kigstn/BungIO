import datetime
from typing import TYPE_CHECKING, Any, Optional

import attr

from bungio.models.base import BaseEnum, BaseModel


@attr.define
class UserTheme(BaseModel):
    """
    _No description given_

    Attributes:
        user_theme_id: _No description given_
        user_theme_name: _No description given_
        user_theme_description: _No description given_
    """

    user_theme_id: int = attr.field()
    user_theme_name: str = attr.field()
    user_theme_description: str = attr.field()


@attr.define
class GroupTheme(BaseModel):
    """
    _No description given_

    Attributes:
        name: _No description given_
        folder: _No description given_
        description: _No description given_
    """

    name: str = attr.field()
    folder: str = attr.field()
    description: str = attr.field()
