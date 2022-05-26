import datetime
from typing import TYPE_CHECKING, Any, Optional

import attr

from bungio.models.base import BaseEnum, BaseModel


@attr.define
class DestinyPowerCapDefinition(BaseModel):
    """
        Defines a 'power cap' (limit) for gear items, based on the rarity tier and season of release.

        Attributes:
            power_cap: The raw value for a power cap.
            hash: The unique identifier for this entity. Guaranteed to be unique for the type of entity, but not globally.

    When entities refer to each other in Destiny content, it is this hash that they are referring to.
            index: The index of the entity as it was found in the investment tables.
            redacted: If this is true, then there is an entity with this identifier/type combination, but BNet is not yet allowed to show it. Sorry!
    """

    power_cap: int = attr.field()
    hash: int = attr.field()
    index: int = attr.field()
    redacted: bool = attr.field()
