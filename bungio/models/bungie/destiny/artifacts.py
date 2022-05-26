import datetime
from typing import TYPE_CHECKING, Any, Optional

import attr

from bungio.models.base import BaseEnum, BaseModel


@attr.define
class DestinyArtifactProfileScoped(BaseModel):
    """
        Represents a Seasonal Artifact and all data related to it for the requested Account.

    It can be combined with Character-scoped data for a full picture of what a character has available/has chosen, or just these settings can be used for overview information.

        Attributes:
            artifact_hash: Not specified.
            point_progression: Not specified.
            points_acquired: Not specified.
            power_bonus_progression: Not specified.
            power_bonus: Not specified.
    """

    artifact_hash: int = attr.field()
    point_progression: "DestinyProgression" = attr.field()
    points_acquired: int = attr.field()
    power_bonus_progression: "DestinyProgression" = attr.field()
    power_bonus: int = attr.field()


@attr.define
class DestinyArtifactCharacterScoped(BaseModel):
    """
    Not specified.

    Attributes:
        artifact_hash: Not specified.
        points_used: Not specified.
        reset_count: Not specified.
        tiers: Not specified.
    """

    artifact_hash: int = attr.field()
    points_used: int = attr.field()
    reset_count: int = attr.field()
    tiers: list["DestinyArtifactTier"] = attr.field()


@attr.define
class DestinyArtifactTier(BaseModel):
    """
    Not specified.

    Attributes:
        tier_hash: Not specified.
        is_unlocked: Not specified.
        points_to_unlock: Not specified.
        items: Not specified.
    """

    tier_hash: int = attr.field()
    is_unlocked: bool = attr.field()
    points_to_unlock: int = attr.field()
    items: list["DestinyArtifactTierItem"] = attr.field()


@attr.define
class DestinyArtifactTierItem(BaseModel):
    """
    Not specified.

    Attributes:
        item_hash: Not specified.
        is_active: Not specified.
    """

    item_hash: int = attr.field()
    is_active: bool = attr.field()
