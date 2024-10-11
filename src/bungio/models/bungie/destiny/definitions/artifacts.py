# DO NOT CHANGE ANY CODE BELOW
# This file is generated automatically by `generate_api_schema.py` and will be overwritten
# Instead, change functions / models by subclassing them in the `./overwrites/` folder. They will be used instead.

from typing import TYPE_CHECKING, Optional

from bungio.models.base import BaseModel, HashObject, ManifestModel, custom_define, custom_field

if TYPE_CHECKING:
    from bungio.models import (
        DestinyDisplayPropertiesDefinition,
        DestinyInventoryItemDefinition,
        DestinyItemTranslationBlockDefinition,
    )


@custom_define()
class DestinyArtifactDefinition(ManifestModel, HashObject):
    """
    Represents known info about a Destiny Artifact. We cannot guarantee that artifact definitions will be immutable between seasons - in fact, we've been told that they will be replaced between seasons. But this definition is built both to minimize the amount of lookups for related data that have to occur, and is built in hope that, if this plan changes, we will be able to accommodate it more easily.

    None
    Attributes:
        display_properties: Any basic display info we know about the Artifact. Currently sourced from a related inventory item, but the source of this data is subject to change.
        hash: The unique identifier for this entity. Guaranteed to be unique for the type of entity, but not globally. When entities refer to each other in Destiny content, it is this hash that they are referring to.
        index: The index of the entity as it was found in the investment tables.
        redacted: If this is true, then there is an entity with this identifier/type combination, but BNet is not yet allowed to show it. Sorry!
        tiers: Any Tier/Rank data related to this artifact, listed in display order.  Currently sourced from a Vendor, but this source is subject to change.
        translation_block: Any Geometry/3D info we know about the Artifact. Currently sourced from a related inventory item's gearset information, but the source of this data is subject to change.
    """

    display_properties: "DestinyDisplayPropertiesDefinition" = custom_field()
    index: int = custom_field()
    redacted: bool = custom_field()
    tiers: list["DestinyArtifactTierDefinition"] = custom_field(
        metadata={"type": """list[DestinyArtifactTierDefinition]"""}
    )
    translation_block: "DestinyItemTranslationBlockDefinition" = custom_field()


@custom_define()
class DestinyArtifactTierDefinition(BaseModel):
    """
    _No description given by bungie._

    None
    Attributes:
        display_title: The human readable title of this tier, if any.
        items: The items that can be earned within this tier.
        minimum_unlock_points_used_requirement: The minimum number of "unlock points" that you must have used before you can unlock items from this tier.
        progress_requirement_message: A string representing the localized minimum requirement text for this Tier, if any.
        tier_hash: An identifier, unique within the Artifact, for this specific tier.
    """

    display_title: str = custom_field()
    items: list["DestinyArtifactTierItemDefinition"] = custom_field(
        metadata={"type": """list[DestinyArtifactTierItemDefinition]"""}
    )
    minimum_unlock_points_used_requirement: int = custom_field()
    progress_requirement_message: str = custom_field()
    tier_hash: int = custom_field()


@custom_define()
class DestinyArtifactTierItemDefinition(BaseModel):
    """
    _No description given by bungie._

    Tip: Manifest Information
        This model has some attributes which can be filled with additional information found in the manifest (`manifest_...`).
        Without additional work, these attributes will be `None`, since they require additional requests and database lookups.

        To fill the manifest dependent attributes, either:

        - Run `await ThisClass.fetch_manifest_information()`, see [here](/API Reference/Models/base)
        - Set `Client.always_return_manifest_information` to `True`, see [here](/API Reference/client)

    Attributes:
        item_hash: The identifier of the Plug Item unlocked by activating this item in the Artifact.
        manifest_item_hash: Manifest information for `item_hash`
    """

    item_hash: int = custom_field()
    manifest_item_hash: Optional["DestinyInventoryItemDefinition"] = custom_field(default=None)
