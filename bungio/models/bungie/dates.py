# DO NOT CHANGE ANY CODE BELOW
# This file is generated automatically by `generate_api_schema.py` and will be overwritten
# Instead, change functions / models by subclassing them in the `./overwrites/` folder. They will be used instead.

from datetime import datetime

from bungio.models.base import BaseModel, custom_define, custom_field


@custom_define()
class DateRange(BaseModel):
    """
    _No description given by bungie._

    None
    Attributes:
        end: _No description given by bungie._
        start: _No description given by bungie._
    """

    end: datetime = custom_field()
    start: datetime = custom_field()
