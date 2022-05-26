import datetime
from typing import TYPE_CHECKING, Any, Optional

import attr

from bungio.models.base import BaseEnum, BaseModel


@attr.define
class DestinyArtifactDefinition(BaseModel):
    """
        Represents known info about a Destiny Artifact.

    We cannot guarantee that artifact definitions will be immutable between seasons - in fact, we've been told that they will be replaced between seasons. But this definition is built both to minimize the amount of lookups for related data that have to occur, and is built in hope that, if this plan changes, we will be able to accommodate it more easily.

        Attributes:
            display_properties: Any basic display info we know about the Artifact. Currently sourced from a related inventory item, but the source of this data is subject to change.
            translation_block: Any Geometry/3D info we know about the Artifact. Currently sourced from a related inventory item's gearset information, but the source of this data is subject to change.
            tiers: Any Tier/Rank data related to this artifact, listed in display order.  Currently sourced from a Vendor, but this source is subject to change.
            hash: The unique identifier for this entity. Guaranteed to be unique for the type of entity, but not globally.

    When entities refer to each other in Destiny content, it is this hash that they are referring to.
            index: The index of the entity as it was found in the investment tables.
            redacted: If this is true, then there is an entity with this identifier/type combination, but BNet is not yet allowed to show it. Sorry!
    """

    display_properties: Any = attr.field()
    translation_block: Any = attr.field()
    tiers: list["DestinyArtifactTierDefinition"] = attr.field()
    hash: int = attr.field()
    index: int = attr.field()
    redacted: bool = attr.field()


@attr.define
class DestinyArtifactTierDefinition(BaseModel):
    """
    Not specified.

    Attributes:
        tier_hash: An identifier, unique within the Artifact, for this specific tier.
        display_title: The human readable title of this tier, if any.
        progress_requirement_message: A string representing the localized minimum requirement text for this Tier, if any.
        items: The items that can be earned within this tier.
        minimum_unlock_points_used_requirement: The minimum number of "unlock points" that you must have used before you can unlock items from this tier.
    """

    tier_hash: int = attr.field()
    display_title: str = attr.field()
    progress_requirement_message: str = attr.field()
    items: list["DestinyArtifactTierItemDefinition"] = attr.field()
    minimum_unlock_points_used_requirement: int = attr.field()


@attr.define
class DestinyArtifactTierItemDefinition(BaseModel):
    """
    Not specified.

    Attributes:
        item_hash: The identifier of the Plug Item unlocked by activating this item in the Artifact.
    """

    item_hash: int = attr.field()
