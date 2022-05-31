import attr

from bungio.models.base import BaseModel


@attr.define
class HyperlinkReference(BaseModel):
    """
    _No description given_

    Attributes:
        title: _No description given_
        url: _No description given_
    """

    title: str = attr.field()
    url: str = attr.field()
