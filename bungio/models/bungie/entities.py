import attr

from bungio.models.base import BaseModel


@attr.define
class EntityActionResult(BaseModel):
    """
    _No description given_

    Attributes:
        entity_id: _No description given_
        result: _No description given_
    """

    entity_id: int = attr.field()
    result: int = attr.field()
