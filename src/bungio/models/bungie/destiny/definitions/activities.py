# DO NOT CHANGE ANY CODE BELOW
# This file is generated automatically by `generate_api_schema.py` and will be overwritten
# Instead, change functions / models by subclassing them in the `./overwrites/` folder. They will be used instead.

from typing import TYPE_CHECKING, Optional, Union

from bungio.models.base import BaseModel, HashObject, ManifestModel, custom_define, custom_field
from bungio.utils import enum_converter

if TYPE_CHECKING:
    from bungio.models import (
        DestinyActivityDefinition,
        DestinyActivityDifficultyId,
        DestinyActivityDifficultyTierType,
        DestinyActivityModifierConnotation,
        DestinyActivityModifierDisplayCategory,
        DestinyActivitySkullDynamicUse,
        DestinyDisplayPropertiesDefinition,
        DestinyTraitDefinition,
    )


@custom_define()
class DestinyActivityFamilyDefinition(ManifestModel, HashObject):
    """
    _No description given by bungie._

    None
    Attributes:
        disabled_skull_category_hashes: _No description given by bungie._
        disabled_skull_subcategory_hashes: _No description given by bungie._
        fixed_skull_subcategory_hashes: _No description given by bungie._
        hash: The unique identifier for this entity. Guaranteed to be unique for the type of entity, but not globally. When entities refer to each other in Destiny content, it is this hash that they are referring to.
        index: The index of the entity as it was found in the investment tables.
        redacted: If this is true, then there is an entity with this identifier/type combination, but BNet is not yet allowed to show it. Sorry!
        traits: _No description given by bungie._
    """

    disabled_skull_category_hashes: list[int] = custom_field(metadata={"type": """list[int]"""})
    disabled_skull_subcategory_hashes: list[int] = custom_field(metadata={"type": """list[int]"""})
    fixed_skull_subcategory_hashes: list[int] = custom_field(metadata={"type": """list[int]"""})
    index: int = custom_field()
    redacted: bool = custom_field()
    traits: list[int] = custom_field(metadata={"type": """list[int]"""})


@custom_define()
class DestinyActivitySkullCategoryDefinition(ManifestModel, HashObject):
    """
    _No description given by bungie._

    None
    Attributes:
        display_properties: _No description given by bungie._
        hash: The unique identifier for this entity. Guaranteed to be unique for the type of entity, but not globally. When entities refer to each other in Destiny content, it is this hash that they are referring to.
        index: The index of the entity as it was found in the investment tables.
        redacted: If this is true, then there is an entity with this identifier/type combination, but BNet is not yet allowed to show it. Sorry!
    """

    display_properties: "DestinyDisplayPropertiesDefinition" = custom_field()
    index: int = custom_field()
    redacted: bool = custom_field()


@custom_define()
class DestinyActivitySkullSubcategoryDefinition(ManifestModel, HashObject):
    """
    _No description given by bungie._

    Tip: Manifest Information
        This model has some attributes which can be filled with additional information found in the manifest (`manifest_...`).
        Without additional work, these attributes will be `None`, since they require additional requests and database lookups.

        To fill the manifest dependent attributes, either:

        - Run `await ThisClass.fetch_manifest_information()`, see [here](/API Reference/Models/base)
        - Set `Client.always_return_manifest_information` to `True`, see [here](/API Reference/client)

    Attributes:
        availability_tier_rank: _No description given by bungie._
        default_skull_hashes: _No description given by bungie._
        display_properties: _No description given by bungie._
        hash: The unique identifier for this entity. Guaranteed to be unique for the type of entity, but not globally. When entities refer to each other in Destiny content, it is this hash that they are referring to.
        index: The index of the entity as it was found in the investment tables.
        parent_skull_category_hash: _No description given by bungie._
        redacted: If this is true, then there is an entity with this identifier/type combination, but BNet is not yet allowed to show it. Sorry!
        manifest_parent_skull_category_hash: Manifest information for `parent_skull_category_hash`
    """

    availability_tier_rank: int = custom_field()
    default_skull_hashes: list[int] = custom_field(metadata={"type": """list[int]"""})
    display_properties: "DestinyDisplayPropertiesDefinition" = custom_field()
    index: int = custom_field()
    parent_skull_category_hash: int = custom_field()
    redacted: bool = custom_field()
    manifest_parent_skull_category_hash: Optional["DestinyActivitySkullCategoryDefinition"] = custom_field(default=None)


@custom_define()
class DestinyActivityDifficultyTierCollectionDefinition(ManifestModel, HashObject):
    """
    _No description given by bungie._

    None
    Attributes:
        difficulty_tiers: _No description given by bungie._
        hash: The unique identifier for this entity. Guaranteed to be unique for the type of entity, but not globally. When entities refer to each other in Destiny content, it is this hash that they are referring to.
        index: The index of the entity as it was found in the investment tables.
        redacted: If this is true, then there is an entity with this identifier/type combination, but BNet is not yet allowed to show it. Sorry!
    """

    difficulty_tiers: list["DestinyActivityDifficultyTierDefinition"] = custom_field(
        metadata={"type": """list[DestinyActivityDifficultyTierDefinition]"""}
    )
    index: int = custom_field()
    redacted: bool = custom_field()


@custom_define()
class DestinyActivityDifficultyTierDefinition(BaseModel):
    """
    _No description given by bungie._

    Tip: Manifest Information
        This model has some attributes which can be filled with additional information found in the manifest (`manifest_...`).
        Without additional work, these attributes will be `None`, since they require additional requests and database lookups.

        To fill the manifest dependent attributes, either:

        - Run `await ThisClass.fetch_manifest_information()`, see [here](/API Reference/Models/base)
        - Set `Client.always_return_manifest_information` to `True`, see [here](/API Reference/client)

    Attributes:
        activity_level: _No description given by bungie._
        display_properties: _No description given by bungie._
        fixed_activity_skulls: _No description given by bungie._
        maximum_fireteam_leader_power: _No description given by bungie._
        minimum_fireteam_leader_power: _No description given by bungie._
        optional_required_trait: _No description given by bungie._
        recommended_activity_level_offset: _No description given by bungie._
        score_time_limit_multiplier: _No description given by bungie._
        selectable_skull_collection_hashes: _No description given by bungie._
        skull_subcategory_overrides: _No description given by bungie._
        tier_rank: _No description given by bungie._
        tier_type: _No description given by bungie._
        manifest_optional_required_trait: Manifest information for `optional_required_trait`
    """

    activity_level: int = custom_field()
    display_properties: "DestinyDisplayPropertiesDefinition" = custom_field()
    fixed_activity_skulls: list["DestinyActivitySkull"] = custom_field(
        metadata={"type": """list[DestinyActivitySkull]"""}
    )
    maximum_fireteam_leader_power: int = custom_field()
    minimum_fireteam_leader_power: int = custom_field()
    optional_required_trait: int = custom_field()
    recommended_activity_level_offset: int = custom_field()
    score_time_limit_multiplier: int = custom_field()
    selectable_skull_collection_hashes: list[int] = custom_field(metadata={"type": """list[int]"""})
    skull_subcategory_overrides: list["DestinyActivityDifficultyTierSubcategoryOverride"] = custom_field(
        metadata={"type": """list[DestinyActivityDifficultyTierSubcategoryOverride]"""}
    )
    tier_rank: int = custom_field()
    tier_type: Union["DestinyActivityDifficultyTierType", int] = custom_field(
        converter=enum_converter("DestinyActivityDifficultyTierType")
    )
    manifest_optional_required_trait: Optional["DestinyTraitDefinition"] = custom_field(default=None)


@custom_define()
class DestinyActivitySkull(BaseModel, HashObject):
    """
    _No description given by bungie._

    Tip: Manifest Information
        This model has some attributes which can be filled with additional information found in the manifest (`manifest_...`).
        Without additional work, these attributes will be `None`, since they require additional requests and database lookups.

        To fill the manifest dependent attributes, either:

        - Run `await ThisClass.fetch_manifest_information()`, see [here](/API Reference/Models/base)
        - Set `Client.always_return_manifest_information` to `True`, see [here](/API Reference/client)

    Attributes:
        activity_modifier_connotation: _No description given by bungie._
        activity_modifier_display_category: _No description given by bungie._
        display_description_override_for_nav_mode: _No description given by bungie._
        display_in_activity_selection: _No description given by bungie._
        display_in_nav_mode: _No description given by bungie._
        display_properties: _No description given by bungie._
        dynamic_use: _No description given by bungie._
        has_ui: _No description given by bungie._
        hash: _No description given by bungie._
        modifier_multiplier_contribution: _No description given by bungie._
        modifier_power_contribution: _No description given by bungie._
        skull_exclusion_group_hash: _No description given by bungie._
        skull_identifier_hash: _No description given by bungie._
        skull_options: _No description given by bungie._
        manifest_skull_exclusion_group_hash: Manifest information for `skull_exclusion_group_hash`
    """

    activity_modifier_connotation: Union["DestinyActivityModifierConnotation", int] = custom_field(
        converter=enum_converter("DestinyActivityModifierConnotation")
    )
    activity_modifier_display_category: Union["DestinyActivityModifierDisplayCategory", int] = custom_field(
        converter=enum_converter("DestinyActivityModifierDisplayCategory")
    )
    display_description_override_for_nav_mode: str = custom_field()
    display_in_activity_selection: bool = custom_field()
    display_in_nav_mode: bool = custom_field()
    display_properties: "DestinyDisplayPropertiesDefinition" = custom_field()
    dynamic_use: Union["DestinyActivitySkullDynamicUse", int] = custom_field(
        converter=enum_converter("DestinyActivitySkullDynamicUse")
    )
    has_ui: bool = custom_field()
    modifier_multiplier_contribution: float = custom_field()
    modifier_power_contribution: int = custom_field()
    skull_exclusion_group_hash: int = custom_field()
    skull_identifier_hash: int = custom_field()
    skull_options: list["DestinyActivitySkullOption"] = custom_field(
        metadata={"type": """list[DestinyActivitySkullOption]"""}
    )
    manifest_skull_exclusion_group_hash: Optional["DestinyActivitySelectableSkullExclusionGroupDefinition"] = (
        custom_field(default=None)
    )


@custom_define()
class DestinyActivitySkullOption(BaseModel):
    """
    _No description given by bungie._

    None
    Attributes:
        bool_value: _No description given by bungie._
        float_value: _No description given by bungie._
        integer_value: _No description given by bungie._
        min_display_difficulty_id: _No description given by bungie._
        option_hash: _No description given by bungie._
        string_value: _No description given by bungie._
    """

    bool_value: bool = custom_field()
    float_value: float = custom_field()
    integer_value: int = custom_field()
    min_display_difficulty_id: Union["DestinyActivityDifficultyId", int] = custom_field(
        converter=enum_converter("DestinyActivityDifficultyId")
    )
    option_hash: int = custom_field()
    string_value: str = custom_field()


@custom_define()
class DestinyActivitySelectableSkullExclusionGroupDefinition(ManifestModel, HashObject):
    """
    _No description given by bungie._

    None
    Attributes:
        hash: The unique identifier for this entity. Guaranteed to be unique for the type of entity, but not globally. When entities refer to each other in Destiny content, it is this hash that they are referring to.
        index: The index of the entity as it was found in the investment tables.
        redacted: If this is true, then there is an entity with this identifier/type combination, but BNet is not yet allowed to show it. Sorry!
    """

    index: int = custom_field()
    redacted: bool = custom_field()


@custom_define()
class DestinyActivityDifficultyTierSubcategoryOverride(BaseModel):
    """
    _No description given by bungie._

    None
    Attributes:
        refresh_time_minutes: _No description given by bungie._
        refresh_time_offset_minutes: _No description given by bungie._
        skull_subcategory_hash: _No description given by bungie._
    """

    refresh_time_minutes: int = custom_field()
    refresh_time_offset_minutes: int = custom_field()
    skull_subcategory_hash: int = custom_field()


@custom_define()
class DestinyActivitySelectableSkullCollectionDefinition(ManifestModel, HashObject):
    """
    _No description given by bungie._

    None
    Attributes:
        display_properties: _No description given by bungie._
        hash: The unique identifier for this entity. Guaranteed to be unique for the type of entity, but not globally. When entities refer to each other in Destiny content, it is this hash that they are referring to.
        index: The index of the entity as it was found in the investment tables.
        redacted: If this is true, then there is an entity with this identifier/type combination, but BNet is not yet allowed to show it. Sorry!
        selectable_activity_skulls: _No description given by bungie._
        selection_type: _No description given by bungie._
        skull_subcategory_hashes: _No description given by bungie._
    """

    display_properties: "DestinyDisplayPropertiesDefinition" = custom_field()
    index: int = custom_field()
    redacted: bool = custom_field()
    selectable_activity_skulls: list["DestinyActivitySelectableSkull"] = custom_field(
        metadata={"type": """list[DestinyActivitySelectableSkull]"""}
    )
    selection_type: "DestinyActivitySelectableSkullCollectionSelectionType" = custom_field()
    skull_subcategory_hashes: list[int] = custom_field(metadata={"type": """list[int]"""})


@custom_define()
class DestinyActivitySelectableSkullCollectionSelectionType(BaseModel):
    """
    _No description given by bungie._

    None
    Attributes:
        refresh_time_minutes: _No description given by bungie._
        refresh_time_offset_minutes: _No description given by bungie._
        selection_count: _No description given by bungie._
    """

    refresh_time_minutes: int = custom_field()
    refresh_time_offset_minutes: int = custom_field()
    selection_count: int = custom_field()


@custom_define()
class DestinyActivitySelectableSkull(BaseModel):
    """
    _No description given by bungie._

    Tip: Manifest Information
        This model has some attributes which can be filled with additional information found in the manifest (`manifest_...`).
        Without additional work, these attributes will be `None`, since they require additional requests and database lookups.

        To fill the manifest dependent attributes, either:

        - Run `await ThisClass.fetch_manifest_information()`, see [here](/API Reference/Models/base)
        - Set `Client.always_return_manifest_information` to `True`, see [here](/API Reference/client)

    Attributes:
        activity_skull: _No description given by bungie._
        is_empty_skull: _No description given by bungie._
        loadout_restriction_hash: _No description given by bungie._
        required_trait_existence: _No description given by bungie._
        required_trait_hash: _No description given by bungie._
        manifest_loadout_restriction_hash: Manifest information for `loadout_restriction_hash`
        manifest_required_trait_hash: Manifest information for `required_trait_hash`
    """

    activity_skull: "DestinyActivitySkull" = custom_field()
    is_empty_skull: bool = custom_field()
    loadout_restriction_hash: int = custom_field()
    required_trait_existence: bool = custom_field()
    required_trait_hash: int = custom_field()
    manifest_loadout_restriction_hash: Optional["DestinyActivityLoadoutRestrictionDefinition"] = custom_field(
        default=None
    )
    manifest_required_trait_hash: Optional["DestinyTraitDefinition"] = custom_field(default=None)


@custom_define()
class DestinyActivityLoadoutRestrictionDefinition(ManifestModel, HashObject):
    """
    _No description given by bungie._

    None
    Attributes:
        hash: The unique identifier for this entity. Guaranteed to be unique for the type of entity, but not globally. When entities refer to each other in Destiny content, it is this hash that they are referring to.
        index: The index of the entity as it was found in the investment tables.
        redacted: If this is true, then there is an entity with this identifier/type combination, but BNet is not yet allowed to show it. Sorry!
        restricted_equipment_slot_hashes: _No description given by bungie._
        restricted_item_filter_hash: _No description given by bungie._
    """

    index: int = custom_field()
    redacted: bool = custom_field()
    restricted_equipment_slot_hashes: list[int] = custom_field(metadata={"type": """list[int]"""})
    restricted_item_filter_hash: int = custom_field()


@custom_define()
class DestinyActivityInteractableDefinition(ManifestModel, HashObject):
    """
    There are times in every Activity's life when interacting with an object in the world will result in another Activity activating. Well, not every Activity. Just certain ones. Anyways, this defines a set of interactable components, the activities that they spawn when you interact with them, and the conditions under which they can be interacted with. Sadly, we don't get any *really* good data for them, like positional data... yet. I have hopes for future data that we could put on this.

    None
    Attributes:
        entries: The possible interactables in this activity interactable definition.
        hash: The unique identifier for this entity. Guaranteed to be unique for the type of entity, but not globally. When entities refer to each other in Destiny content, it is this hash that they are referring to.
        index: The index of the entity as it was found in the investment tables.
        redacted: If this is true, then there is an entity with this identifier/type combination, but BNet is not yet allowed to show it. Sorry!
    """

    entries: list["DestinyActivityInteractableEntryDefinition"] = custom_field(
        metadata={"type": """list[DestinyActivityInteractableEntryDefinition]"""}
    )
    index: int = custom_field()
    redacted: bool = custom_field()


@custom_define()
class DestinyActivityInteractableEntryDefinition(BaseModel):
    """
    Defines a specific interactable and the action that can occur when triggered.

    Tip: Manifest Information
        This model has some attributes which can be filled with additional information found in the manifest (`manifest_...`).
        Without additional work, these attributes will be `None`, since they require additional requests and database lookups.

        To fill the manifest dependent attributes, either:

        - Run `await ThisClass.fetch_manifest_information()`, see [here](/API Reference/Models/base)
        - Set `Client.always_return_manifest_information` to `True`, see [here](/API Reference/client)

    Attributes:
        activity_hash: The activity that will trigger when you interact with this interactable.
        manifest_activity_hash: Manifest information for `activity_hash`
    """

    activity_hash: int = custom_field()
    manifest_activity_hash: Optional["DestinyActivityDefinition"] = custom_field(default=None)
