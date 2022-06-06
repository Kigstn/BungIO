from typing import TYPE_CHECKING

import attr

from bungio.models.base import BaseModel

if TYPE_CHECKING:
    from bungio.models import (
        DestinyActivityDefinition,
        DestinyInventoryItemDefinition,
        DestinyLocationDefinition,
        DestinyObjectiveDefinition,
    )


@attr.define
class DestinyEnvironmentLocationMapping(BaseModel):
    """
    _No description given by bungie_

    Attributes:
        location_hash: The location that is revealed on the director by this mapping.
        activation_source: A hint that the UI uses to figure out how this location is activated by the player.
        item_hash: If this is populated, it is the item that you must possess for this location to be active because of this mapping. (theoretically, a location can have multiple mappings, and some might require an item while others don't)
        objective_hash: If this is populated, this is an objective related to the location.
        activity_hash: If this is populated, this is the activity you have to be playing in order to see this location appear because of this mapping. (theoretically, a location can have multiple mappings, and some might require you to be in a specific activity when others don't)
    """

    location_hash: "DestinyLocationDefinition" = attr.field()
    activation_source: str = attr.field()
    item_hash: "DestinyInventoryItemDefinition" = attr.field()
    objective_hash: "DestinyObjectiveDefinition" = attr.field()
    activity_hash: "DestinyActivityDefinition" = attr.field()
