import attr

from bungio.models.base import BaseModel


@attr.define
class DestinyColor(BaseModel):
    """
    Represents a color whose RGBA values are all represented as values between 0 and 255.

    Attributes:
        red: _No description given_
        green: _No description given_
        blue: _No description given_
        alpha: _No description given_
    """

    red: int = attr.field()
    green: int = attr.field()
    blue: int = attr.field()
    alpha: int = attr.field()
