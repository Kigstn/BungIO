from typing import TYPE_CHECKING

import attr

from bungio.models.base import BaseModel

if TYPE_CHECKING:
    from bungio.models import (
        DestinyArtifactTier,
        DestinyArtifactTierItem,
        DestinyProgression,
    )


@attr.define
class DestinyArtifactProfileScoped(BaseModel):
    """
    Represents a Seasonal Artifact and all data related to it for the requested Account. It can be combined with Character-scoped data for a full picture of what a character has available/has chosen, or just these settings can be used for overview information.

    Attributes:
        artifact_hash: _No description given by bungie_
        point_progression: _No description given by bungie_
        points_acquired: _No description given by bungie_
        power_bonus_progression: _No description given by bungie_
        power_bonus: _No description given by bungie_
    """

    artifact_hash: int = attr.field()
    point_progression: "DestinyProgression" = attr.field()
    points_acquired: int = attr.field()
    power_bonus_progression: "DestinyProgression" = attr.field()
    power_bonus: int = attr.field()


@attr.define
class DestinyArtifactCharacterScoped(BaseModel):
    """
    _No description given by bungie_

    Attributes:
        artifact_hash: _No description given by bungie_
        points_used: _No description given by bungie_
        reset_count: _No description given by bungie_
        tiers: _No description given by bungie_
    """

    artifact_hash: int = attr.field()
    points_used: int = attr.field()
    reset_count: int = attr.field()
    tiers: list["DestinyArtifactTier"] = attr.field()


@attr.define
class DestinyArtifactTier(BaseModel):
    """
    _No description given by bungie_

    Attributes:
        tier_hash: _No description given by bungie_
        is_unlocked: _No description given by bungie_
        points_to_unlock: _No description given by bungie_
        items: _No description given by bungie_
    """

    tier_hash: int = attr.field()
    is_unlocked: bool = attr.field()
    points_to_unlock: int = attr.field()
    items: list["DestinyArtifactTierItem"] = attr.field()


@attr.define
class DestinyArtifactTierItem(BaseModel):
    """
    _No description given by bungie_

    Attributes:
        item_hash: _No description given by bungie_
        is_active: _No description given by bungie_
    """

    item_hash: int = attr.field()
    is_active: bool = attr.field()
