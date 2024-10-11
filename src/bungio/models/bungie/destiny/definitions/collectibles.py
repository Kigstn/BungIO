# DO NOT CHANGE ANY CODE BELOW
# This file is generated automatically by `generate_api_schema.py` and will be overwritten
# Instead, change functions / models by subclassing them in the `./overwrites/` folder. They will be used instead.

from typing import TYPE_CHECKING, Optional, Union

from bungio.models.base import BaseModel, HashObject, ManifestModel, custom_define, custom_field
from bungio.utils import enum_converter

if TYPE_CHECKING:
    from bungio.models import (
        DestinyDisplayPropertiesDefinition,
        DestinyInventoryItemDefinition,
        DestinyMaterialRequirementSetDefinition,
        DestinyPresentationChildBlock,
        DestinyPresentationNodeRequirementsBlock,
        DestinyPresentationNodeType,
        DestinyScope,
        DestinyUnlockValueDefinition,
    )


@custom_define()
class DestinyCollectibleDefinition(ManifestModel, HashObject):
    """
    Defines a

    Tip: Manifest Information
        This model has some attributes which can be filled with additional information found in the manifest (`manifest_...`).
        Without additional work, these attributes will be `None`, since they require additional requests and database lookups.

        To fill the manifest dependent attributes, either:

        - Run `await ThisClass.fetch_manifest_information()`, see [here](/API Reference/Models/base)
        - Set `Client.always_return_manifest_information` to `True`, see [here](/API Reference/client)

    Attributes:
        acquisition_info: _No description given by bungie._
        display_properties: _No description given by bungie._
        hash: The unique identifier for this entity. Guaranteed to be unique for the type of entity, but not globally. When entities refer to each other in Destiny content, it is this hash that they are referring to.
        index: The index of the entity as it was found in the investment tables.
        item_hash: _No description given by bungie._
        parent_node_hashes: A quick reference to presentation nodes that have this node as a child. Presentation nodes can be parented under multiple parents.
        presentation_info: _No description given by bungie._
        presentation_node_type: _No description given by bungie._
        redacted: If this is true, then there is an entity with this identifier/type combination, but BNet is not yet allowed to show it. Sorry!
        scope: Indicates whether the state of this Collectible is determined on a per-character or on an account-wide basis.
        source_hash: This is a hash identifier we are building on the BNet side in an attempt to let people group collectibles by similar sources. I can't promise that it's going to be 100% accurate, but if the designers were consistent in assigning the same source strings to items with the same sources, it *ought to* be. No promises though. This hash also doesn't relate to an actual definition, just to note: we've got nothing useful other than the source string for this data.
        source_string: A human readable string for a hint about how to acquire the item.
        state_info: _No description given by bungie._
        trait_hashes: _No description given by bungie._
        trait_ids: _No description given by bungie._
        manifest_item_hash: Manifest information for `item_hash`
    """

    acquisition_info: "DestinyCollectibleAcquisitionBlock" = custom_field()
    display_properties: "DestinyDisplayPropertiesDefinition" = custom_field()
    index: int = custom_field()
    item_hash: int = custom_field()
    parent_node_hashes: list[int] = custom_field(metadata={"type": """list[int]"""})
    presentation_info: "DestinyPresentationChildBlock" = custom_field()
    presentation_node_type: Union["DestinyPresentationNodeType", int] = custom_field(
        converter=enum_converter("DestinyPresentationNodeType")
    )
    redacted: bool = custom_field()
    scope: Union["DestinyScope", int] = custom_field(converter=enum_converter("DestinyScope"))
    source_hash: int = custom_field()
    source_string: str = custom_field()
    state_info: "DestinyCollectibleStateBlock" = custom_field()
    trait_hashes: list[int] = custom_field(metadata={"type": """list[int]"""})
    trait_ids: list[str] = custom_field(metadata={"type": """list[str]"""})
    manifest_item_hash: Optional["DestinyInventoryItemDefinition"] = custom_field(default=None)


@custom_define()
class DestinyCollectibleAcquisitionBlock(BaseModel):
    """
    _No description given by bungie._

    Tip: Manifest Information
        This model has some attributes which can be filled with additional information found in the manifest (`manifest_...`).
        Without additional work, these attributes will be `None`, since they require additional requests and database lookups.

        To fill the manifest dependent attributes, either:

        - Run `await ThisClass.fetch_manifest_information()`, see [here](/API Reference/Models/base)
        - Set `Client.always_return_manifest_information` to `True`, see [here](/API Reference/client)

    Attributes:
        acquire_material_requirement_hash: _No description given by bungie._
        acquire_timestamp_unlock_value_hash: _No description given by bungie._
        manifest_acquire_material_requirement_hash: Manifest information for `acquire_material_requirement_hash`
        manifest_acquire_timestamp_unlock_value_hash: Manifest information for `acquire_timestamp_unlock_value_hash`
    """

    acquire_material_requirement_hash: int = custom_field()
    acquire_timestamp_unlock_value_hash: int = custom_field()
    manifest_acquire_material_requirement_hash: Optional["DestinyMaterialRequirementSetDefinition"] = custom_field(
        default=None
    )
    manifest_acquire_timestamp_unlock_value_hash: Optional["DestinyUnlockValueDefinition"] = custom_field(default=None)


@custom_define()
class DestinyCollectibleStateBlock(BaseModel):
    """
    _No description given by bungie._

    Tip: Manifest Information
        This model has some attributes which can be filled with additional information found in the manifest (`manifest_...`).
        Without additional work, these attributes will be `None`, since they require additional requests and database lookups.

        To fill the manifest dependent attributes, either:

        - Run `await ThisClass.fetch_manifest_information()`, see [here](/API Reference/Models/base)
        - Set `Client.always_return_manifest_information` to `True`, see [here](/API Reference/client)

    Attributes:
        obscured_override_item_hash: _No description given by bungie._
        requirements: _No description given by bungie._
        manifest_obscured_override_item_hash: Manifest information for `obscured_override_item_hash`
    """

    obscured_override_item_hash: int = custom_field()
    requirements: "DestinyPresentationNodeRequirementsBlock" = custom_field()
    manifest_obscured_override_item_hash: Optional["DestinyInventoryItemDefinition"] = custom_field(default=None)
