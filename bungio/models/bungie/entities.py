from typing import TYPE_CHECKING

import attr

from bungio.models.base import BaseModel

if TYPE_CHECKING:
    from bungio.models import PlatformErrorCodes


@attr.define
class EntityActionResult(BaseModel):
    """
    _No description given by bungie_

    Attributes:
        entity_id: _No description given by bungie_
        result: _No description given by bungie_
    """

    entity_id: int = attr.field()
    result: "PlatformErrorCodes" = attr.field()
