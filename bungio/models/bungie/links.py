# DO NOT CHANGE ANY CODE BELOW
# This file is generated automatically by `generate_api_schema.py` and will be overwritten
# Instead, change functions / models by subclassing them in the `./overwrites/` folder. They will be used instead.

import attr

from bungio.models.base import BaseModel


@attr.define
class HyperlinkReference(BaseModel):
    """
    _No description given by bungie._

    None
    Attributes:
        title: _No description given by bungie._
        url: _No description given by bungie._
    """

    title: str = attr.field()
    url: str = attr.field()
