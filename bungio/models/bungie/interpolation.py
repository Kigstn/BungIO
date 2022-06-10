import attr

from bungio.models.base import BaseModel


@attr.define
class InterpolationPoint(BaseModel):
    """
    _No description given by bungie._

    None
    Attributes:
        value: _No description given by bungie._
        weight: _No description given by bungie._
    """

    value: int = attr.field()
    weight: int = attr.field()


@attr.define
class InterpolationPointFloat(BaseModel):
    """
    _No description given by bungie._

    None
    Attributes:
        value: _No description given by bungie._
        weight: _No description given by bungie._
    """

    value: float = attr.field()
    weight: float = attr.field()
