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
