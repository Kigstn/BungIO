# DO NOT CHANGE ANY CODE BELOW
# This file is generated automatically by `generate_api_schema.py` and will be overwritten
# Instead, change functions / models by subclassing them in the `./overwrites/` folder. They will be used instead.

from typing import TYPE_CHECKING, Optional, Union

from bungio.models.base import BaseModel, HashObject, ManifestModel, custom_define, custom_field
from bungio.utils import enum_converter

if TYPE_CHECKING:
    from bungio.models import (
        DestinyDisplayPropertiesDefinition,
        DestinyGender,
        DestinyItemQuantity,
        DestinyLoreDefinition,
        DestinyObjectiveDefinition,
        DestinyPresentationChildBlock,
        DestinyPresentationNodeRequirementsBlock,
        DestinyPresentationNodeType,
        DestinyRecordToastStyle,
        DestinyRecordValueStyle,
        DestinyScope,
    )


@custom_define()
class DestinyRecordDefinition(ManifestModel, HashObject):
    """
    _No description given by bungie._

    Tip: Manifest Information
        This model has some attributes which can be filled with additional information found in the manifest (`manifest_...`).
        Without additional work, these attributes will be `None`, since they require additional requests and database lookups.

        To fill the manifest dependent attributes, either:

        - Run `await ThisClass.fetch_manifest_information()`, see [here](/API Reference/Models/base)
        - Set `Client.always_return_manifest_information` to `True`, see [here](/API Reference/client)

    Attributes:
        completion_info: _No description given by bungie._
        display_properties: _No description given by bungie._
        expiration_info: _No description given by bungie._
        for_title_gilding: _No description given by bungie._
        hash: The unique identifier for this entity. Guaranteed to be unique for the type of entity, but not globally. When entities refer to each other in Destiny content, it is this hash that they are referring to.
        index: The index of the entity as it was found in the investment tables.
        interval_info: Some records have multiple 'interval' objectives, and the record may be claimed at each completed interval
        lore_hash: _No description given by bungie._
        objective_hashes: _No description given by bungie._
        parent_node_hashes: A quick reference to presentation nodes that have this node as a child. Presentation nodes can be parented under multiple parents.
        presentation_info: _No description given by bungie._
        presentation_node_type: _No description given by bungie._
        record_type_name: A display name for the type of record this is (Triumphs, Lore, Medals, Seasonal Challenge, etc.).
        record_value_style: _No description given by bungie._
        redacted: If this is true, then there is an entity with this identifier/type combination, but BNet is not yet allowed to show it. Sorry!
        requirements: _No description given by bungie._
        reward_items: If there is any publicly available information about rewards earned for achieving this record, this is the list of those items.  However, note that some records intentionally have "hidden" rewards. These will not be returned in this list.
        scope: Indicates whether this Record's state is determined on a per-character or on an account-wide basis.
        should_show_large_icons: A hint to show a large icon for a reward
        state_info: _No description given by bungie._
        title_info: _No description given by bungie._
        trait_hashes: _No description given by bungie._
        trait_ids: _No description given by bungie._
        manifest_lore_hash: Manifest information for `lore_hash`
    """

    completion_info: "DestinyRecordCompletionBlock" = custom_field()
    display_properties: "DestinyDisplayPropertiesDefinition" = custom_field()
    expiration_info: "DestinyRecordExpirationBlock" = custom_field()
    for_title_gilding: bool = custom_field()
    index: int = custom_field()
    interval_info: "DestinyRecordIntervalBlock" = custom_field()
    lore_hash: int = custom_field()
    objective_hashes: list[int] = custom_field(metadata={"type": """list[int]"""})
    parent_node_hashes: list[int] = custom_field(metadata={"type": """list[int]"""})
    presentation_info: "DestinyPresentationChildBlock" = custom_field()
    presentation_node_type: Union["DestinyPresentationNodeType", int] = custom_field(
        converter=enum_converter("DestinyPresentationNodeType")
    )
    record_type_name: str = custom_field()
    record_value_style: Union["DestinyRecordValueStyle", int] = custom_field(
        converter=enum_converter("DestinyRecordValueStyle")
    )
    redacted: bool = custom_field()
    requirements: "DestinyPresentationNodeRequirementsBlock" = custom_field()
    reward_items: list["DestinyItemQuantity"] = custom_field(metadata={"type": """list[DestinyItemQuantity]"""})
    scope: Union["DestinyScope", int] = custom_field(converter=enum_converter("DestinyScope"))
    should_show_large_icons: bool = custom_field()
    state_info: "SchemaRecordStateBlock" = custom_field()
    title_info: "DestinyRecordTitleBlock" = custom_field()
    trait_hashes: list[int] = custom_field(metadata={"type": """list[int]"""})
    trait_ids: list[str] = custom_field(metadata={"type": """list[str]"""})
    manifest_lore_hash: Optional["DestinyLoreDefinition"] = custom_field(default=None)


@custom_define()
class DestinyRecordTitleBlock(BaseModel):
    """
    _No description given by bungie._

    Tip: Manifest Information
        This model has some attributes which can be filled with additional information found in the manifest (`manifest_...`).
        Without additional work, these attributes will be `None`, since they require additional requests and database lookups.

        To fill the manifest dependent attributes, either:

        - Run `await ThisClass.fetch_manifest_information()`, see [here](/API Reference/Models/base)
        - Set `Client.always_return_manifest_information` to `True`, see [here](/API Reference/client)

    Attributes:
        gilding_tracking_record_hash: _No description given by bungie._
        has_title: _No description given by bungie._
        titles_by_gender: _No description given by bungie._
        titles_by_gender_hash: For those who prefer to use the definitions.
        manifest_gilding_tracking_record_hash: Manifest information for `gilding_tracking_record_hash`
    """

    gilding_tracking_record_hash: int = custom_field()
    has_title: bool = custom_field()
    titles_by_gender: dict[Union["DestinyGender", int], str] = custom_field(
        metadata={"type": """dict[DestinyGender, str]"""}
    )
    titles_by_gender_hash: dict[int, str] = custom_field(metadata={"type": """dict[int, str]"""})
    manifest_gilding_tracking_record_hash: Optional["DestinyRecordDefinition"] = custom_field(default=None)


@custom_define()
class DestinyRecordCompletionBlock(BaseModel):
    """
    _No description given by bungie._

    None
    Attributes:
        partial_completion_objective_count_threshold: The number of objectives that must be completed before the objective is considered "complete"
        score_value: _No description given by bungie._
        should_fire_toast: _No description given by bungie._
        toast_style: _No description given by bungie._
    """

    partial_completion_objective_count_threshold: int = custom_field()
    score_value: int = custom_field()
    should_fire_toast: bool = custom_field()
    toast_style: Union["DestinyRecordToastStyle", int] = custom_field(
        converter=enum_converter("DestinyRecordToastStyle")
    )


@custom_define()
class SchemaRecordStateBlock(BaseModel):
    """
    _No description given by bungie._

    None
    Attributes:
        featured_priority: _No description given by bungie._
        obscured_description: A display description override to show when this record is 'obscured' instead of the default obscured display description.
        obscured_name: A display name override to show when this record is 'obscured' instead of the default obscured display name.
    """

    featured_priority: int = custom_field()
    obscured_description: str = custom_field()
    obscured_name: str = custom_field()


@custom_define()
class DestinyRecordExpirationBlock(BaseModel):
    """
    If this record has an expiration after which it cannot be earned, this is some information about that expiration.

    None
    Attributes:
        description: _No description given by bungie._
        has_expiration: _No description given by bungie._
        icon: _No description given by bungie._
    """

    description: str = custom_field()
    has_expiration: bool = custom_field()
    icon: str = custom_field()


@custom_define()
class DestinyRecordIntervalBlock(BaseModel):
    """
    _No description given by bungie._

    None
    Attributes:
        interval_objectives: _No description given by bungie._
        interval_rewards: _No description given by bungie._
        original_objective_array_insertion_index: _No description given by bungie._
    """

    interval_objectives: list["DestinyRecordIntervalObjective"] = custom_field(
        metadata={"type": """list[DestinyRecordIntervalObjective]"""}
    )
    interval_rewards: list["DestinyRecordIntervalRewards"] = custom_field(
        metadata={"type": """list[DestinyRecordIntervalRewards]"""}
    )
    original_objective_array_insertion_index: int = custom_field()


@custom_define()
class DestinyRecordIntervalObjective(BaseModel):
    """
    _No description given by bungie._

    Tip: Manifest Information
        This model has some attributes which can be filled with additional information found in the manifest (`manifest_...`).
        Without additional work, these attributes will be `None`, since they require additional requests and database lookups.

        To fill the manifest dependent attributes, either:

        - Run `await ThisClass.fetch_manifest_information()`, see [here](/API Reference/Models/base)
        - Set `Client.always_return_manifest_information` to `True`, see [here](/API Reference/client)

    Attributes:
        interval_objective_hash: _No description given by bungie._
        interval_score_value: _No description given by bungie._
        manifest_interval_objective_hash: Manifest information for `interval_objective_hash`
    """

    interval_objective_hash: int = custom_field()
    interval_score_value: int = custom_field()
    manifest_interval_objective_hash: Optional["DestinyObjectiveDefinition"] = custom_field(default=None)


@custom_define()
class DestinyRecordIntervalRewards(BaseModel):
    """
    _No description given by bungie._

    None
    Attributes:
        interval_reward_items: _No description given by bungie._
    """

    interval_reward_items: list["DestinyItemQuantity"] = custom_field(
        metadata={"type": """list[DestinyItemQuantity]"""}
    )
