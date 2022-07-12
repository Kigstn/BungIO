# DO NOT CHANGE ANY CODE BELOW
# This file is generated automatically by `generate_api_schema.py` and will be overwritten
# Instead, change functions / models by subclassing them in the `./overwrites/` folder. They will be used instead.

from datetime import datetime
from typing import TYPE_CHECKING, Any, Optional, Union

import attr

from bungio.models.base import BaseEnum, BaseFlagEnum, BaseModel, ManifestModel
from bungio.utils import enum_converter


@attr.define
class UserTheme(BaseModel):
    """
    _No description given by bungie._

    None
    Attributes:
        user_theme_description: _No description given by bungie._
        user_theme_id: _No description given by bungie._
        user_theme_name: _No description given by bungie._
    """

    user_theme_description: str = attr.field()
    user_theme_id: int = attr.field()
    user_theme_name: str = attr.field()


@attr.define
class GroupTheme(BaseModel):
    """
    _No description given by bungie._

    None
    Attributes:
        description: _No description given by bungie._
        folder: _No description given by bungie._
        name: _No description given by bungie._
    """

    description: str = attr.field()
    folder: str = attr.field()
    name: str = attr.field()
