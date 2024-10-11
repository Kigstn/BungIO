# DO NOT CHANGE ANY CODE BELOW
# This file is generated automatically by `generate_api_schema.py` and will be overwritten
# Instead, change functions / models by subclassing them in the `./overwrites/` folder. They will be used instead.

from typing import TYPE_CHECKING, Optional

from bungio.models.base import BaseModel, custom_define, custom_field

if TYPE_CHECKING:
    from bungio.models import DestinyArtifactDefinition, DestinyInventoryItemDefinition, DestinyProgression


@custom_define()
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

    artifact_hash: int = custom_field()
    point_progression: "DestinyProgression" = custom_field()
    points_acquired: int = custom_field()
    power_bonus: int = custom_field()
    power_bonus_progression: "DestinyProgression" = custom_field()
    manifest_artifact_hash: Optional["DestinyArtifactDefinition"] = custom_field(default=None)


@custom_define()
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

    artifact_hash: int = custom_field()
    points_used: int = custom_field()
    reset_count: int = custom_field()
    tiers: list["DestinyArtifactTier"] = custom_field(metadata={"type": """list[DestinyArtifactTier]"""})
    manifest_artifact_hash: Optional["DestinyArtifactDefinition"] = custom_field(default=None)


@custom_define()
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

    is_unlocked: bool = custom_field()
    items: list["DestinyArtifactTierItem"] = custom_field(metadata={"type": """list[DestinyArtifactTierItem]"""})
    points_to_unlock: int = custom_field()
    tier_hash: int = custom_field()


@custom_define()
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
        is_visible: _No description given by bungie._
        item_hash: _No description given by bungie._
        manifest_item_hash: Manifest information for `item_hash`
    """

    is_active: bool = custom_field()
    is_visible: bool = custom_field()
    item_hash: int = custom_field()
    manifest_item_hash: Optional["DestinyInventoryItemDefinition"] = custom_field(default=None)
