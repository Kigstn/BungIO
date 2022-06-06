from typing import TYPE_CHECKING, Any

import attr

from bungio.models.base import BaseModel

if TYPE_CHECKING:
    from bungio.models import (
        DestinyDisplayPropertiesDefinition,
        DestinyGenderDefinition,
        DestinyItemQuantity,
        DestinyLoreDefinition,
        DestinyObjectiveDefinition,
        DestinyPresentationChildBlock,
        DestinyPresentationNodeDefinition,
        DestinyPresentationNodeRequirementsBlock,
        DestinyPresentationNodeType,
        DestinyRecordToastStyle,
        DestinyRecordValueStyle,
        DestinyScope,
        DestinyTraitDefinition,
    )


@attr.define
class DestinyRecordDefinition(BaseModel):
    """
    _No description given by bungie_

    Attributes:
        display_properties: _No description given by bungie_
        scope: Indicates whether this Record's state is determined on a per-character or on an account-wide basis.
        presentation_info: _No description given by bungie_
        lore_hash: _No description given by bungie_
        objective_hashes: _No description given by bungie_
        record_value_style: _No description given by bungie_
        for_title_gilding: _No description given by bungie_
        should_show_large_icons: A hint to show a large icon for a reward
        title_info: _No description given by bungie_
        completion_info: _No description given by bungie_
        state_info: _No description given by bungie_
        requirements: _No description given by bungie_
        expiration_info: _No description given by bungie_
        interval_info: Some records have multiple 'interval' objectives, and the record may be claimed at each completed interval
        reward_items: If there is any publicly available information about rewards earned for achieving this record, this is the list of those items.  However, note that some records intentionally have "hidden" rewards. These will not be returned in this list.
        presentation_node_type: _No description given by bungie_
        trait_ids: _No description given by bungie_
        trait_hashes: _No description given by bungie_
        parent_node_hashes: A quick reference to presentation nodes that have this node as a child. Presentation nodes can be parented under multiple parents.
        hash: The unique identifier for this entity. Guaranteed to be unique for the type of entity, but not globally. When entities refer to each other in Destiny content, it is this hash that they are referring to.
        index: The index of the entity as it was found in the investment tables.
        redacted: If this is true, then there is an entity with this identifier/type combination, but BNet is not yet allowed to show it. Sorry!
    """

    display_properties: "DestinyDisplayPropertiesDefinition" = attr.field()
    scope: "DestinyScope" = attr.field()
    presentation_info: "DestinyPresentationChildBlock" = attr.field()
    lore_hash: "DestinyLoreDefinition" = attr.field()
    objective_hashes: list["DestinyObjectiveDefinition"] = attr.field()
    record_value_style: "DestinyRecordValueStyle" = attr.field()
    for_title_gilding: bool = attr.field()
    should_show_large_icons: bool = attr.field()
    title_info: "DestinyRecordTitleBlock" = attr.field()
    completion_info: "DestinyRecordCompletionBlock" = attr.field()
    state_info: "SchemaRecordStateBlock" = attr.field()
    requirements: "DestinyPresentationNodeRequirementsBlock" = attr.field()
    expiration_info: "DestinyRecordExpirationBlock" = attr.field()
    interval_info: "DestinyRecordIntervalBlock" = attr.field()
    reward_items: list["DestinyItemQuantity"] = attr.field()
    presentation_node_type: "DestinyPresentationNodeType" = attr.field()
    trait_ids: list[str] = attr.field()
    trait_hashes: list["DestinyTraitDefinition"] = attr.field()
    parent_node_hashes: list["DestinyPresentationNodeDefinition"] = attr.field()
    hash: int = attr.field()
    index: int = attr.field()
    redacted: bool = attr.field()


@attr.define
class DestinyRecordTitleBlock(BaseModel):
    """
    _No description given by bungie_

    Attributes:
        has_title: _No description given by bungie_
        titles_by_gender: _No description given by bungie_
        titles_by_gender_hash: For those who prefer to use the definitions.
        gilding_tracking_record_hash: _No description given by bungie_
    """

    has_title: bool = attr.field()
    titles_by_gender: Any = attr.field()
    titles_by_gender_hash: "DestinyGenderDefinition" = attr.field()
    gilding_tracking_record_hash: "DestinyRecordDefinition" = attr.field()


@attr.define
class DestinyRecordCompletionBlock(BaseModel):
    """
    _No description given by bungie_

    Attributes:
        partial_completion_objective_count_threshold: The number of objectives that must be completed before the objective is considered "complete"
        score_value: _No description given by bungie_
        should_fire_toast: _No description given by bungie_
        toast_style: _No description given by bungie_
    """

    partial_completion_objective_count_threshold: int = attr.field()
    score_value: int = attr.field()
    should_fire_toast: bool = attr.field()
    toast_style: "DestinyRecordToastStyle" = attr.field()


@attr.define
class SchemaRecordStateBlock(BaseModel):
    """
    _No description given by bungie_

    Attributes:
        featured_priority: _No description given by bungie_
        obscured_string: _No description given by bungie_
    """

    featured_priority: int = attr.field()
    obscured_string: str = attr.field()


@attr.define
class DestinyRecordExpirationBlock(BaseModel):
    """
    If this record has an expiration after which it cannot be earned, this is some information about that expiration.

    Attributes:
        has_expiration: _No description given by bungie_
        description: _No description given by bungie_
        icon: _No description given by bungie_
    """

    has_expiration: bool = attr.field()
    description: str = attr.field()
    icon: str = attr.field()


@attr.define
class DestinyRecordIntervalBlock(BaseModel):
    """
    _No description given by bungie_

    Attributes:
        interval_objectives: _No description given by bungie_
        interval_rewards: _No description given by bungie_
        original_objective_array_insertion_index: _No description given by bungie_
    """

    interval_objectives: list["DestinyRecordIntervalObjective"] = attr.field()
    interval_rewards: list["DestinyRecordIntervalRewards"] = attr.field()
    original_objective_array_insertion_index: int = attr.field()


@attr.define
class DestinyRecordIntervalObjective(BaseModel):
    """
    _No description given by bungie_

    Attributes:
        interval_objective_hash: _No description given by bungie_
        interval_score_value: _No description given by bungie_
    """

    interval_objective_hash: "DestinyObjectiveDefinition" = attr.field()
    interval_score_value: int = attr.field()


@attr.define
class DestinyRecordIntervalRewards(BaseModel):
    """
    _No description given by bungie_

    Attributes:
        interval_reward_items: _No description given by bungie_
    """

    interval_reward_items: list["DestinyItemQuantity"] = attr.field()
