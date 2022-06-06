from typing import TYPE_CHECKING

import attr

from bungio.models.base import BaseModel

if TYPE_CHECKING:
    from bungio.models import (
        DestinyDisplayPropertiesDefinition,
        DestinyEnergyType,
        DestinyStatDefinition,
    )


@attr.define
class DestinyEnergyTypeDefinition(BaseModel):
    """
    Represents types of Energy that can be used for costs and payments related to Armor 2.0 mods.

    Attributes:
        display_properties: The description of the energy type, icon etc...
        transparent_icon_path: A variant of the icon that is transparent and colorless.
        show_icon: If TRUE, the game shows this Energy type's icon. Otherwise, it doesn't. Whether you show it or not is up to you.
        enum_value: We have an enumeration for Energy types for quick reference. This is the current definition's Energy type enum value.
        capacity_stat_hash: If this Energy Type can be used for determining the Type of Energy that an item can consume, this is the hash for the DestinyInvestmentStatDefinition that represents the stat which holds the Capacity for that energy type. (Note that this is optional because "Any" is a valid cost, but not valid for Capacity - an Armor must have a specific Energy Type for determining the energy type that the Armor is restricted to use)
        cost_stat_hash: If this Energy Type can be used as a cost to pay for socketing Armor 2.0 items, this is the hash for the DestinyInvestmentStatDefinition that stores the plug's raw cost.
        hash: The unique identifier for this entity. Guaranteed to be unique for the type of entity, but not globally. When entities refer to each other in Destiny content, it is this hash that they are referring to.
        index: The index of the entity as it was found in the investment tables.
        redacted: If this is true, then there is an entity with this identifier/type combination, but BNet is not yet allowed to show it. Sorry!
    """

    display_properties: "DestinyDisplayPropertiesDefinition" = attr.field()
    transparent_icon_path: str = attr.field()
    show_icon: bool = attr.field()
    enum_value: "DestinyEnergyType" = attr.field()
    capacity_stat_hash: "DestinyStatDefinition" = attr.field()
    cost_stat_hash: "DestinyStatDefinition" = attr.field()
    hash: int = attr.field()
    index: int = attr.field()
    redacted: bool = attr.field()
