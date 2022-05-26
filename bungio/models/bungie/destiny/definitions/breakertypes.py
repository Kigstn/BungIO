import datetime
from typing import TYPE_CHECKING, Any, Optional

import attr

from bungio.models.base import BaseEnum, BaseModel


@attr.define
class DestinyBreakerTypeDefinition(BaseModel):
    """
        Not specified.

        Attributes:
            display_properties: Not specified.
            enum_value: We have an enumeration for Breaker types for quick reference. This is the current definition's breaker type enum value.
            hash: The unique identifier for this entity. Guaranteed to be unique for the type of entity, but not globally.

    When entities refer to each other in Destiny content, it is this hash that they are referring to.
            index: The index of the entity as it was found in the investment tables.
            redacted: If this is true, then there is an entity with this identifier/type combination, but BNet is not yet allowed to show it. Sorry!
    """

    display_properties: "DestinyDisplayPropertiesDefinition" = attr.field()
    enum_value: int = attr.field()
    hash: int = attr.field()
    index: int = attr.field()
    redacted: bool = attr.field()
