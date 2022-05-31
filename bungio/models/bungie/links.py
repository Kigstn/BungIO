import attr

from bungio.models.base import BaseModel


@attr.define
class HyperlinkReference(BaseModel):
    """
    _No description given by bungie_

    Attributes:
        title: _No description given by bungie_
        url: _No description given by bungie_
    """

    title: str = attr.field()
    url: str = attr.field()
