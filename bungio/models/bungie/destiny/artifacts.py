# DO NOT CHANGE ANY CODE BELOW
# This file is generated automatically by `generate_api_schema.py` and will be overwritten
# Instead, change functions / models by subclassing them in the `./overwrites/` folder. They will be used instead.

from typing import TYPE_CHECKING, Optional

import attr

from bungio.models.base import BaseModel

if TYPE_CHECKING:
    from bungio.models import (
        DestinyArtifactDefinition,
        DestinyInventoryItemDefinition,
        DestinyProgression,
    )


@attr.define
class DestinyArtifactProfileScoped(BaseModel):
    """
    Represents a Seasonal Artifact and all data related to it for the requested Account. It can be combined with Character-scoped data for a full picture of what a character has available/has chosen, or just these settings can be used for overview information.

    Tip: Manifest Information
        This model has some attributes which can be filled with additional information found in the manifest (`manifest_...`).
        Without additional work, these attributes will be `None`, since they require additional requests and database lookups.

        To fill the manifest dependent attributes, either:

        - Run `await ThisClass.fetch_manifest_information()`, see [here](/API Reference/Models/base)
        - Set `Client.always_return_manifest_information` to `True`, see [here](/API Reference/client)

    Attributes:
        artifact_hash: _No description given by bungie._
        point_progression: _No description given by bungie._
        points_acquired: _No description given by bungie._
        power_bonus: _No description given by bungie._
        power_bonus_progression: _No description given by bungie._
        manifest_artifact_hash: Manifest information for `artifact_hash`
    """

    artifact_hash: int = attr.field()
    point_progression: "DestinyProgression" = attr.field()
    points_acquired: int = attr.field()
    power_bonus: int = attr.field()
    power_bonus_progression: "DestinyProgression" = attr.field()
    manifest_artifact_hash: Optional["DestinyArtifactDefinition"] = attr.field(default=None)


@attr.define
class DestinyArtifactCharacterScoped(BaseModel):
    """
    _No description given by bungie._

    Tip: Manifest Information
        This model has some attributes which can be filled with additional information found in the manifest (`manifest_...`).
        Without additional work, these attributes will be `None`, since they require additional requests and database lookups.

        To fill the manifest dependent attributes, either:

        - Run `await ThisClass.fetch_manifest_information()`, see [here](/API Reference/Models/base)
        - Set `Client.always_return_manifest_information` to `True`, see [here](/API Reference/client)

    Attributes:
        artifact_hash: _No description given by bungie._
        points_used: _No description given by bungie._
        reset_count: _No description given by bungie._
        tiers: _No description given by bungie._
        manifest_artifact_hash: Manifest information for `artifact_hash`
    """

    artifact_hash: int = attr.field()
    points_used: int = attr.field()
    reset_count: int = attr.field()
    tiers: list["DestinyArtifactTier"] = attr.field(metadata={"type": """list[DestinyArtifactTier]"""})
    manifest_artifact_hash: Optional["DestinyArtifactDefinition"] = attr.field(default=None)


@attr.define
class DestinyArtifactTier(BaseModel):
    """
    _No description given by bungie._

    None
    Attributes:
        is_unlocked: _No description given by bungie._
        items: _No description given by bungie._
        points_to_unlock: _No description given by bungie._
        tier_hash: _No description given by bungie._
    """

    is_unlocked: bool = attr.field()
    items: list["DestinyArtifactTierItem"] = attr.field(metadata={"type": """list[DestinyArtifactTierItem]"""})
    points_to_unlock: int = attr.field()
    tier_hash: int = attr.field()


@attr.define
class DestinyArtifactTierItem(BaseModel):
    """
    _No description given by bungie._

    Tip: Manifest Information
        This model has some attributes which can be filled with additional information found in the manifest (`manifest_...`).
        Without additional work, these attributes will be `None`, since they require additional requests and database lookups.

        To fill the manifest dependent attributes, either:

        - Run `await ThisClass.fetch_manifest_information()`, see [here](/API Reference/Models/base)
        - Set `Client.always_return_manifest_information` to `True`, see [here](/API Reference/client)

    Attributes:
        is_active: _No description given by bungie._
        item_hash: _No description given by bungie._
        manifest_item_hash: Manifest information for `item_hash`
    """

    is_active: bool = attr.field()
    item_hash: int = attr.field()
    manifest_item_hash: Optional["DestinyInventoryItemDefinition"] = attr.field(default=None)
