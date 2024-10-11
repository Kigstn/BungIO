# DO NOT CHANGE ANY CODE BELOW
# This file is generated automatically by `generate_api_schema.py` and will be overwritten
# Instead, change functions / models by subclassing them in the `./overwrites/` folder. They will be used instead.

from typing import TYPE_CHECKING, Optional, Union

from bungio.models.base import BaseModel, HashObject, ManifestModel, custom_define, custom_field
from bungio.utils import enum_converter

if TYPE_CHECKING:
    from bungio.models import (
        DestinyActivityGraphDefinition,
        DestinyActivityInteractableDefinition,
        DestinyColor,
        DestinyDisplayPropertiesDefinition,
        FireteamFinderCodeOptionType,
        FireteamFinderLabelFieldType,
        FireteamFinderOptionAvailability,
        FireteamFinderOptionControlType,
        FireteamFinderOptionDisplayFormat,
        FireteamFinderOptionSearchFilterType,
        FireteamFinderOptionValueFlags,
        FireteamFinderOptionValueProviderType,
        FireteamFinderOptionVisibility,
    )


@custom_define()
class DestinyActivityInteractableReference(BaseModel):
    """
    _No description given by bungie._

    Tip: Manifest Information
        This model has some attributes which can be filled with additional information found in the manifest (`manifest_...`).
        Without additional work, these attributes will be `None`, since they require additional requests and database lookups.

        To fill the manifest dependent attributes, either:

        - Run `await ThisClass.fetch_manifest_information()`, see [here](/API Reference/Models/base)
        - Set `Client.always_return_manifest_information` to `True`, see [here](/API Reference/client)

    Attributes:
        activity_interactable_element_index: _No description given by bungie._
        activity_interactable_hash: _No description given by bungie._
        manifest_activity_interactable_hash: Manifest information for `activity_interactable_hash`
    """

    activity_interactable_element_index: int = custom_field()
    activity_interactable_hash: int = custom_field()
    manifest_activity_interactable_hash: Optional["DestinyActivityInteractableDefinition"] = custom_field(default=None)


@custom_define()
class DestinyFireteamFinderActivityGraphDefinition(ManifestModel, HashObject):
    """
    _No description given by bungie._

    Tip: Manifest Information
        This model has some attributes which can be filled with additional information found in the manifest (`manifest_...`).
        Without additional work, these attributes will be `None`, since they require additional requests and database lookups.

        To fill the manifest dependent attributes, either:

        - Run `await ThisClass.fetch_manifest_information()`, see [here](/API Reference/Models/base)
        - Set `Client.always_return_manifest_information` to `True`, see [here](/API Reference/client)

    Attributes:
        children: _No description given by bungie._
        color: _No description given by bungie._
        display_properties: _No description given by bungie._
        hash: The unique identifier for this entity. Guaranteed to be unique for the type of entity, but not globally. When entities refer to each other in Destiny content, it is this hash that they are referring to.
        index: The index of the entity as it was found in the investment tables.
        is_player_elected_difficulty_node: _No description given by bungie._
        parent_hash: _No description given by bungie._
        redacted: If this is true, then there is an entity with this identifier/type combination, but BNet is not yet allowed to show it. Sorry!
        related_activity_hashes: _No description given by bungie._
        related_activity_set_hashes: _No description given by bungie._
        related_director_nodes: _No description given by bungie._
        related_interactable_activities: _No description given by bungie._
        related_location_hashes: _No description given by bungie._
        self_and_all_descendant_hashes: _No description given by bungie._
        specific_activity_set_hash: _No description given by bungie._
        manifest_parent_hash: Manifest information for `parent_hash`
        manifest_specific_activity_set_hash: Manifest information for `specific_activity_set_hash`
    """

    children: list[int] = custom_field(metadata={"type": """list[int]"""})
    color: "DestinyColor" = custom_field()
    display_properties: "DestinyDisplayPropertiesDefinition" = custom_field()
    index: int = custom_field()
    is_player_elected_difficulty_node: bool = custom_field()
    parent_hash: int = custom_field()
    redacted: bool = custom_field()
    related_activity_hashes: list[int] = custom_field(metadata={"type": """list[int]"""})
    related_activity_set_hashes: list[int] = custom_field(metadata={"type": """list[int]"""})
    related_director_nodes: list["DestinyActivityGraphReference"] = custom_field(
        metadata={"type": """list[DestinyActivityGraphReference]"""}
    )
    related_interactable_activities: list["DestinyActivityInteractableReference"] = custom_field(
        metadata={"type": """list[DestinyActivityInteractableReference]"""}
    )
    related_location_hashes: list[int] = custom_field(metadata={"type": """list[int]"""})
    self_and_all_descendant_hashes: list[int] = custom_field(metadata={"type": """list[int]"""})
    specific_activity_set_hash: int = custom_field()
    manifest_parent_hash: Optional["DestinyFireteamFinderActivityGraphDefinition"] = custom_field(default=None)
    manifest_specific_activity_set_hash: Optional["DestinyFireteamFinderActivitySetDefinition"] = custom_field(
        default=None
    )


@custom_define()
class DestinyActivityGraphReference(BaseModel):
    """
    _No description given by bungie._

    Tip: Manifest Information
        This model has some attributes which can be filled with additional information found in the manifest (`manifest_...`).
        Without additional work, these attributes will be `None`, since they require additional requests and database lookups.

        To fill the manifest dependent attributes, either:

        - Run `await ThisClass.fetch_manifest_information()`, see [here](/API Reference/Models/base)
        - Set `Client.always_return_manifest_information` to `True`, see [here](/API Reference/client)

    Attributes:
        activity_graph_hash: _No description given by bungie._
        manifest_activity_graph_hash: Manifest information for `activity_graph_hash`
    """

    activity_graph_hash: int = custom_field()
    manifest_activity_graph_hash: Optional["DestinyActivityGraphDefinition"] = custom_field(default=None)


@custom_define()
class DestinyFireteamFinderActivitySetDefinition(ManifestModel, HashObject):
    """
    _No description given by bungie._

    None
    Attributes:
        activity_graph_hashes: _No description given by bungie._
        activity_hashes: _No description given by bungie._
        hash: The unique identifier for this entity. Guaranteed to be unique for the type of entity, but not globally. When entities refer to each other in Destiny content, it is this hash that they are referring to.
        index: The index of the entity as it was found in the investment tables.
        label_hashes: _No description given by bungie._
        maximum_party_size: _No description given by bungie._
        option_hashes: _No description given by bungie._
        redacted: If this is true, then there is an entity with this identifier/type combination, but BNet is not yet allowed to show it. Sorry!
    """

    activity_graph_hashes: list[int] = custom_field(metadata={"type": """list[int]"""})
    activity_hashes: list[int] = custom_field(metadata={"type": """list[int]"""})
    index: int = custom_field()
    label_hashes: list[int] = custom_field(metadata={"type": """list[int]"""})
    maximum_party_size: int = custom_field()
    option_hashes: list[int] = custom_field(metadata={"type": """list[int]"""})
    redacted: bool = custom_field()


@custom_define()
class DestinyFireteamFinderOptionDefinition(ManifestModel, HashObject):
    """
    _No description given by bungie._

    Tip: Manifest Information
        This model has some attributes which can be filled with additional information found in the manifest (`manifest_...`).
        Without additional work, these attributes will be `None`, since they require additional requests and database lookups.

        To fill the manifest dependent attributes, either:

        - Run `await ThisClass.fetch_manifest_information()`, see [here](/API Reference/Models/base)
        - Set `Client.always_return_manifest_information` to `True`, see [here](/API Reference/client)

    Attributes:
        availability: _No description given by bungie._
        code_option_type: _No description given by bungie._
        creator_settings: _No description given by bungie._
        descending_sort_priority: _No description given by bungie._
        display_properties: _No description given by bungie._
        group_hash: _No description given by bungie._
        hash: The unique identifier for this entity. Guaranteed to be unique for the type of entity, but not globally. When entities refer to each other in Destiny content, it is this hash that they are referring to.
        index: The index of the entity as it was found in the investment tables.
        redacted: If this is true, then there is an entity with this identifier/type combination, but BNet is not yet allowed to show it. Sorry!
        searcher_settings: _No description given by bungie._
        ui_display_style: _No description given by bungie._
        values: _No description given by bungie._
        visibility: _No description given by bungie._
        manifest_group_hash: Manifest information for `group_hash`
    """

    availability: Union["FireteamFinderOptionAvailability", int] = custom_field(
        converter=enum_converter("FireteamFinderOptionAvailability")
    )
    code_option_type: Union["FireteamFinderCodeOptionType", int] = custom_field(
        converter=enum_converter("FireteamFinderCodeOptionType")
    )
    creator_settings: "DestinyFireteamFinderOptionCreatorSettings" = custom_field()
    descending_sort_priority: int = custom_field()
    display_properties: "DestinyDisplayPropertiesDefinition" = custom_field()
    group_hash: int = custom_field()
    index: int = custom_field()
    redacted: bool = custom_field()
    searcher_settings: "DestinyFireteamFinderOptionSearcherSettings" = custom_field()
    ui_display_style: str = custom_field()
    values: "DestinyFireteamFinderOptionValues" = custom_field()
    visibility: Union["FireteamFinderOptionVisibility", int] = custom_field(
        converter=enum_converter("FireteamFinderOptionVisibility")
    )
    manifest_group_hash: Optional["DestinyFireteamFinderOptionGroupDefinition"] = custom_field(default=None)


@custom_define()
class DestinyFireteamFinderOptionCreatorSettings(BaseModel):
    """
    _No description given by bungie._

    None
    Attributes:
        control: _No description given by bungie._
    """

    control: "DestinyFireteamFinderOptionSettingsControl" = custom_field()


@custom_define()
class DestinyFireteamFinderOptionSettingsControl(BaseModel):
    """
    _No description given by bungie._

    None
    Attributes:
        max_selected_items: _No description given by bungie._
        min_selected_items: _No description given by bungie._
        type: _No description given by bungie._
    """

    max_selected_items: int = custom_field()
    min_selected_items: int = custom_field()
    type: Union["FireteamFinderOptionControlType", int] = custom_field(
        converter=enum_converter("FireteamFinderOptionControlType")
    )


@custom_define()
class DestinyFireteamFinderOptionSearcherSettings(BaseModel):
    """
    _No description given by bungie._

    None
    Attributes:
        control: _No description given by bungie._
        search_filter_type: _No description given by bungie._
    """

    control: "DestinyFireteamFinderOptionSettingsControl" = custom_field()
    search_filter_type: Union["FireteamFinderOptionSearchFilterType", int] = custom_field(
        converter=enum_converter("FireteamFinderOptionSearchFilterType")
    )


@custom_define()
class DestinyFireteamFinderOptionValues(BaseModel):
    """
    _No description given by bungie._

    None
    Attributes:
        display_format_type: _No description given by bungie._
        optional_format_string: _No description given by bungie._
        optional_null: _No description given by bungie._
        type: _No description given by bungie._
        value_definitions: _No description given by bungie._
    """

    display_format_type: Union["FireteamFinderOptionDisplayFormat", int] = custom_field(
        converter=enum_converter("FireteamFinderOptionDisplayFormat")
    )
    optional_format_string: str = custom_field()
    optional_null: "DestinyDisplayPropertiesDefinition" = custom_field()
    type: Union["FireteamFinderOptionValueProviderType", int] = custom_field(
        converter=enum_converter("FireteamFinderOptionValueProviderType")
    )
    value_definitions: list["DestinyFireteamFinderOptionValueDefinition"] = custom_field(
        metadata={"type": """list[DestinyFireteamFinderOptionValueDefinition]"""}
    )


@custom_define()
class DestinyFireteamFinderOptionValueDefinition(BaseModel):
    """
    _No description given by bungie._

    None
    Attributes:
        display_properties: _No description given by bungie._
        flags: _No description given by bungie._
        value: _No description given by bungie._
    """

    display_properties: "DestinyDisplayPropertiesDefinition" = custom_field()
    flags: Union["FireteamFinderOptionValueFlags", int] = custom_field(
        converter=enum_converter("FireteamFinderOptionValueFlags")
    )
    value: int = custom_field()


@custom_define()
class DestinyFireteamFinderOptionGroupDefinition(ManifestModel, HashObject):
    """
    _No description given by bungie._

    None
    Attributes:
        descending_sort_priority: _No description given by bungie._
        display_properties: _No description given by bungie._
        hash: The unique identifier for this entity. Guaranteed to be unique for the type of entity, but not globally. When entities refer to each other in Destiny content, it is this hash that they are referring to.
        index: The index of the entity as it was found in the investment tables.
        redacted: If this is true, then there is an entity with this identifier/type combination, but BNet is not yet allowed to show it. Sorry!
    """

    descending_sort_priority: int = custom_field()
    display_properties: "DestinyDisplayPropertiesDefinition" = custom_field()
    index: int = custom_field()
    redacted: bool = custom_field()


@custom_define()
class DestinyFireteamFinderLabelDefinition(ManifestModel, HashObject):
    """
    _No description given by bungie._

    Tip: Manifest Information
        This model has some attributes which can be filled with additional information found in the manifest (`manifest_...`).
        Without additional work, these attributes will be `None`, since they require additional requests and database lookups.

        To fill the manifest dependent attributes, either:

        - Run `await ThisClass.fetch_manifest_information()`, see [here](/API Reference/Models/base)
        - Set `Client.always_return_manifest_information` to `True`, see [here](/API Reference/client)

    Attributes:
        allow_in_fields: _No description given by bungie._
        descending_sort_priority: _No description given by bungie._
        display_properties: _No description given by bungie._
        group_hash: _No description given by bungie._
        hash: The unique identifier for this entity. Guaranteed to be unique for the type of entity, but not globally. When entities refer to each other in Destiny content, it is this hash that they are referring to.
        index: The index of the entity as it was found in the investment tables.
        redacted: If this is true, then there is an entity with this identifier/type combination, but BNet is not yet allowed to show it. Sorry!
        manifest_group_hash: Manifest information for `group_hash`
    """

    allow_in_fields: Union["FireteamFinderLabelFieldType", int] = custom_field(
        converter=enum_converter("FireteamFinderLabelFieldType")
    )
    descending_sort_priority: int = custom_field()
    display_properties: "DestinyDisplayPropertiesDefinition" = custom_field()
    group_hash: int = custom_field()
    index: int = custom_field()
    redacted: bool = custom_field()
    manifest_group_hash: Optional["DestinyFireteamFinderLabelGroupDefinition"] = custom_field(default=None)


@custom_define()
class DestinyFireteamFinderLabelGroupDefinition(ManifestModel, HashObject):
    """
    _No description given by bungie._

    None
    Attributes:
        descending_sort_priority: _No description given by bungie._
        display_properties: _No description given by bungie._
        hash: The unique identifier for this entity. Guaranteed to be unique for the type of entity, but not globally. When entities refer to each other in Destiny content, it is this hash that they are referring to.
        index: The index of the entity as it was found in the investment tables.
        redacted: If this is true, then there is an entity with this identifier/type combination, but BNet is not yet allowed to show it. Sorry!
    """

    descending_sort_priority: int = custom_field()
    display_properties: "DestinyDisplayPropertiesDefinition" = custom_field()
    index: int = custom_field()
    redacted: bool = custom_field()


@custom_define()
class DestinyFireteamFinderConstantsDefinition(ManifestModel, HashObject):
    """
    _No description given by bungie._

    None
    Attributes:
        all_fireteam_finder_activity_hashes: _No description given by bungie._
        display_properties: _No description given by bungie._
        fireteam_finder_activity_graph_root_category_hashes: _No description given by bungie._
        guardian_oath_display_properties: _No description given by bungie._
        guardian_oath_tenets: _No description given by bungie._
        hash: The unique identifier for this entity. Guaranteed to be unique for the type of entity, but not globally. When entities refer to each other in Destiny content, it is this hash that they are referring to.
        index: The index of the entity as it was found in the investment tables.
        redacted: If this is true, then there is an entity with this identifier/type combination, but BNet is not yet allowed to show it. Sorry!
    """

    all_fireteam_finder_activity_hashes: list[int] = custom_field(metadata={"type": """list[int]"""})
    display_properties: "DestinyDisplayPropertiesDefinition" = custom_field()
    fireteam_finder_activity_graph_root_category_hashes: list[int] = custom_field(metadata={"type": """list[int]"""})
    guardian_oath_display_properties: "DestinyDisplayPropertiesDefinition" = custom_field()
    guardian_oath_tenets: list["DestinyDisplayPropertiesDefinition"] = custom_field(
        metadata={"type": """list[DestinyDisplayPropertiesDefinition]"""}
    )
    index: int = custom_field()
    redacted: bool = custom_field()
