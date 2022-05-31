import attr

from bungio.models.base import BaseModel


@attr.define
class EntityActionResult(BaseModel):
    """
    _No description given by bungie_

    Attributes:
        entity_id: _No description given by bungie_
        result: _No description given by bungie_
    """

    entity_id: int = attr.field()
    result: int = attr.field()
