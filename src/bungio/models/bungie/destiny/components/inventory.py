# DO NOT CHANGE ANY CODE BELOW
# This file is generated automatically by `generate_api_schema.py` and will be overwritten
# Instead, change functions / models by subclassing them in the `./overwrites/` folder. They will be used instead.

from typing import TYPE_CHECKING, Optional, Union

from bungio.models.base import BaseModel, custom_define, custom_field

if TYPE_CHECKING:
    from bungio.models import BungieMembershipType, DestinyItemComponent, DestinyMaterialRequirementSetDefinition


@custom_define()
class DestinyPlatformSilverComponent(BaseModel):
    """
    _No description given by bungie._

    None
    Attributes:
        platform_silver: If a Profile is played on multiple platforms, this is the silver they have for each platform, keyed by Membership Type.
    """

    platform_silver: dict[Union["BungieMembershipType", int], "DestinyItemComponent"] = custom_field(
        metadata={"type": """dict[BungieMembershipType, DestinyItemComponent]"""}
    )


@custom_define()
class DestinyCurrenciesComponent(BaseModel):
    """
    This component provides a quick lookup of every item the requested character has and how much of that item they have. Requesting this component will allow you to circumvent manually putting together the list of which currencies you have for the purpose of testing currency requirements on an item being purchased, or operations that have costs. You *could* figure this out yourself by doing a GetCharacter or GetProfile request and forming your own lookup table, but that is inconvenient enough that this feels like a worthwhile (and optional) redundancy. Don't bother requesting it if you have already created your own lookup from prior GetCharacter/GetProfile calls.

    None
    Attributes:
        item_quantities: A dictionary - keyed by the item's hash identifier (DestinyInventoryItemDefinition), and whose value is the amount of that item you have across all available inventory buckets for purchasing. This allows you to see whether the requesting character can afford any given purchase/action without having to re-create this list itself.
        material_requirement_set_states: A map of material requirement hashes and their status information.
    """

    item_quantities: dict[int, int] = custom_field(metadata={"type": """dict[int, int]"""})
    material_requirement_set_states: dict[int, "DestinyMaterialRequirementSetState"] = custom_field(
        metadata={"type": """dict[int, DestinyMaterialRequirementSetState]"""}
    )


@custom_define()
class DestinyMaterialRequirementSetState(BaseModel):
    """
    _No description given by bungie._

    Tip: Manifest Information
        This model has some attributes which can be filled with additional information found in the manifest (`manifest_...`).
        Without additional work, these attributes will be `None`, since they require additional requests and database lookups.

        To fill the manifest dependent attributes, either:

        - Run `await ThisClass.fetch_manifest_information()`, see [here](/API Reference/Models/base)
        - Set `Client.always_return_manifest_information` to `True`, see [here](/API Reference/client)

    Attributes:
        material_requirement_set_hash: The hash identifier of the material requirement set. Use it to look up the DestinyMaterialRequirementSetDefinition.
        material_requirement_states: The dynamic state values for individual material requirements.
        manifest_material_requirement_set_hash: Manifest information for `material_requirement_set_hash`
    """

    material_requirement_set_hash: int = custom_field()
    material_requirement_states: list["DestinyMaterialRequirementState"] = custom_field(
        metadata={"type": """list[DestinyMaterialRequirementState]"""}
    )
    manifest_material_requirement_set_hash: Optional["DestinyMaterialRequirementSetDefinition"] = custom_field(
        default=None
    )


@custom_define()
class DestinyMaterialRequirementState(BaseModel):
    """
    _No description given by bungie._

    None
    Attributes:
        count: The amount of the material required.
        item_hash: The hash identifier of the material required. Use it to look up the material's DestinyInventoryItemDefinition.
        stack_size: A value for the amount of a (possibly virtual) material on some scope. For example: Dawning cookie baking material requirements.
    """

    count: int = custom_field()
    item_hash: int = custom_field()
    stack_size: int = custom_field()
