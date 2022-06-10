import attr

from bungio.models.base import BaseModel


@attr.define
class DestinyStringVariablesComponent(BaseModel):
    """
    _No description given by bungie._

    None
    Attributes:
        integer_values_by_hash: _No description given by bungie._
    """

    integer_values_by_hash: dict[int, int] = attr.field(metadata={"type": """dict[int, int]"""})
