import datetime
from typing import TYPE_CHECKING, Any, Optional

import attr

from bungio.models.base import BaseEnum, BaseModel


@attr.define
class DestinyRecordDefinition(BaseModel):
    """
        Not specified.

        Attributes:
            display_properties: Not specified.
            scope: Indicates whether this Record's state is determined on a per-character or on an account-wide basis.
            presentation_info: Not specified.
            lore_hash: Not specified.
            objective_hashes: Not specified.
            record_value_style: Not specified.
            for_title_gilding: Not specified.
            should_show_large_icons: A hint to show a large icon for a reward
            title_info: Not specified.
            completion_info: Not specified.
            state_info: Not specified.
            requirements: Not specified.
            expiration_info: Not specified.
            interval_info: Some records have multiple 'interval' objectives, and the record may be claimed at each completed interval
            reward_items: If there is any publicly available information about rewards earned for achieving this record, this is the list of those items.

     However, note that some records intentionally have "hidden" rewards. These will not be returned in this list.
            presentation_node_type: Not specified.
            trait_ids: Not specified.
            trait_hashes: Not specified.
            parent_node_hashes: A quick reference to presentation nodes that have this node as a child. Presentation nodes can be parented under multiple parents.
            hash: The unique identifier for this entity. Guaranteed to be unique for the type of entity, but not globally.

    When entities refer to each other in Destiny content, it is this hash that they are referring to.
            index: The index of the entity as it was found in the investment tables.
            redacted: If this is true, then there is an entity with this identifier/type combination, but BNet is not yet allowed to show it. Sorry!
    """

    display_properties: "DestinyDisplayPropertiesDefinition" = attr.field()
    scope: int = attr.field()
    presentation_info: "DestinyPresentationChildBlock" = attr.field()
    lore_hash: int = attr.field()
    objective_hashes: list[int] = attr.field()
    record_value_style: int = attr.field()
    for_title_gilding: bool = attr.field()
    should_show_large_icons: bool = attr.field()
    title_info: "DestinyRecordTitleBlock" = attr.field()
    completion_info: "DestinyRecordCompletionBlock" = attr.field()
    state_info: "SchemaRecordStateBlock" = attr.field()
    requirements: "DestinyPresentationNodeRequirementsBlock" = attr.field()
    expiration_info: "DestinyRecordExpirationBlock" = attr.field()
    interval_info: Any = attr.field()
    reward_items: list["DestinyItemQuantity"] = attr.field()
    presentation_node_type: int = attr.field()
    trait_ids: list[str] = attr.field()
    trait_hashes: list[int] = attr.field()
    parent_node_hashes: list[int] = attr.field()
    hash: int = attr.field()
    index: int = attr.field()
    redacted: bool = attr.field()


@attr.define
class DestinyRecordTitleBlock(BaseModel):
    """
    Not specified.

    Attributes:
        has_title: Not specified.
        titles_by_gender: Not specified.
        titles_by_gender_hash: For those who prefer to use the definitions.
        gilding_tracking_record_hash: Not specified.
    """

    has_title: bool = attr.field()
    titles_by_gender: Any = attr.field()
    titles_by_gender_hash: Any = attr.field()
    gilding_tracking_record_hash: int = attr.field()


@attr.define
class DestinyRecordCompletionBlock(BaseModel):
    """
    Not specified.

    Attributes:
        partial_completion_objective_count_threshold: The number of objectives that must be completed before the objective is considered "complete"
        score_value: Not specified.
        should_fire_toast: Not specified.
        toast_style: Not specified.
    """

    partial_completion_objective_count_threshold: int = attr.field()
    score_value: int = attr.field()
    should_fire_toast: bool = attr.field()
    toast_style: int = attr.field()


@attr.define
class SchemaRecordStateBlock(BaseModel):
    """
    Not specified.

    Attributes:
        featured_priority: Not specified.
        obscured_string: Not specified.
    """

    featured_priority: int = attr.field()
    obscured_string: str = attr.field()


@attr.define
class DestinyRecordExpirationBlock(BaseModel):
    """
    If this record has an expiration after which it cannot be earned, this is some information about that expiration.

    Attributes:
        has_expiration: Not specified.
        description: Not specified.
        icon: Not specified.
    """

    has_expiration: bool = attr.field()
    description: str = attr.field()
    icon: str = attr.field()


@attr.define
class DestinyRecordIntervalBlock(BaseModel):
    """
    Not specified.

    Attributes:
        interval_objectives: Not specified.
        interval_rewards: Not specified.
        original_objective_array_insertion_index: Not specified.
    """

    interval_objectives: list["DestinyRecordIntervalObjective"] = attr.field()
    interval_rewards: list["DestinyRecordIntervalRewards"] = attr.field()
    original_objective_array_insertion_index: int = attr.field()


@attr.define
class DestinyRecordIntervalObjective(BaseModel):
    """
    Not specified.

    Attributes:
        interval_objective_hash: Not specified.
        interval_score_value: Not specified.
    """

    interval_objective_hash: int = attr.field()
    interval_score_value: int = attr.field()


@attr.define
class DestinyRecordIntervalRewards(BaseModel):
    """
    Not specified.

    Attributes:
        interval_reward_items: Not specified.
    """

    interval_reward_items: list["DestinyItemQuantity"] = attr.field()
