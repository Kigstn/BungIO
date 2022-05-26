import datetime
from typing import TYPE_CHECKING, Any, Optional

import attr

from bungio.models.base import BaseEnum, BaseModel


@attr.define
class DestinyActivityModifierDefinition(BaseModel):
    """
        Modifiers - in Destiny 1, these were referred to as "Skulls" - are changes that can be applied to an Activity.

        Attributes:
            display_properties: Not specified.
            display_in_nav_mode: Not specified.
            display_in_activity_selection: Not specified.
            hash: The unique identifier for this entity. Guaranteed to be unique for the type of entity, but not globally.

    When entities refer to each other in Destiny content, it is this hash that they are referring to.
            index: The index of the entity as it was found in the investment tables.
            redacted: If this is true, then there is an entity with this identifier/type combination, but BNet is not yet allowed to show it. Sorry!
    """

    display_properties: "DestinyDisplayPropertiesDefinition" = attr.field()
    display_in_nav_mode: bool = attr.field()
    display_in_activity_selection: bool = attr.field()
    hash: int = attr.field()
    index: int = attr.field()
    redacted: bool = attr.field()
