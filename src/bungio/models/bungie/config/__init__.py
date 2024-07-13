# DO NOT CHANGE ANY CODE BELOW
# This file is generated automatically by `generate_api_schema.py` and will be overwritten
# Instead, change functions / models by subclassing them in the `./overwrites/` folder. They will be used instead.

from datetime import datetime
from typing import Optional, Any, Union, TYPE_CHECKING

from bungio.utils import enum_converter
from bungio.models.base import BaseModel, BaseEnum, BaseFlagEnum, HashObject, ManifestModel, custom_define, custom_field


@custom_define()
class UserTheme(BaseModel):
    """
    _No description given by bungie._

    None
    Attributes:
        user_theme_description: _No description given by bungie._
        user_theme_id: _No description given by bungie._
        user_theme_name: _No description given by bungie._
    """

    user_theme_description: str = custom_field()
    user_theme_id: int = custom_field()
    user_theme_name: str = custom_field()


@custom_define()
class GroupTheme(BaseModel):
    """
    _No description given by bungie._

    None
    Attributes:
        description: _No description given by bungie._
        folder: _No description given by bungie._
        name: _No description given by bungie._
    """

    description: str = custom_field()
    folder: str = custom_field()
    name: str = custom_field()
