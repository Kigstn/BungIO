from typing import TYPE_CHECKING, Any

import attr

from bungio.models.base import BaseModel

if TYPE_CHECKING:
    from bungio.models import (
        DestinyObjectiveProgress,
        DestinyPresentationNodeDefinition,
        DestinyRecordDefinition,
        DestinyRecordState,
    )


@attr.define
class DestinyRecordsComponent(BaseModel):
    """
    _No description given by bungie_

    Attributes:
        records: _No description given by bungie_
        record_categories_root_node_hash: The hash for the root presentation node definition of Triumph categories.
        record_seals_root_node_hash: The hash for the root presentation node definition of Triumph Seals.
    """

    records: Any = attr.field()
    record_categories_root_node_hash: "DestinyPresentationNodeDefinition" = attr.field()
    record_seals_root_node_hash: "DestinyPresentationNodeDefinition" = attr.field()


@attr.define
class DestinyRecordComponent(BaseModel):
    """
    _No description given by bungie_

    Attributes:
        state: _No description given by bungie_
        objectives: _No description given by bungie_
        interval_objectives: _No description given by bungie_
        intervals_redeemed_count: _No description given by bungie_
        completed_count: If available, this is the number of times this record has been completed. For example, the number of times a seal title has been gilded.
        reward_visibilty: If available, a list that describes which reward rewards should be shown (true) or hidden (false). This property is for regular record rewards, and not for interval objective rewards.
    """

    state: "DestinyRecordState" = attr.field()
    objectives: list["DestinyObjectiveProgress"] = attr.field()
    interval_objectives: list["DestinyObjectiveProgress"] = attr.field()
    intervals_redeemed_count: int = attr.field()
    completed_count: int = attr.field()
    reward_visibilty: list[bool] = attr.field()


@attr.define
class DestinyProfileRecordsComponent(BaseModel):
    """
    _No description given by bungie_

    Attributes:
        score: Your 'active' Triumphs score, maintained for backwards compatibility.
        active_score: Your 'active' Triumphs score.
        legacy_score: Your 'legacy' Triumphs score.
        lifetime_score: Your 'lifetime' Triumphs score.
        tracked_record_hash: If this profile is tracking a record, this is the hash identifier of the record it is tracking.
        records: _No description given by bungie_
        record_categories_root_node_hash: The hash for the root presentation node definition of Triumph categories.
        record_seals_root_node_hash: The hash for the root presentation node definition of Triumph Seals.
    """

    score: int = attr.field()
    active_score: int = attr.field()
    legacy_score: int = attr.field()
    lifetime_score: int = attr.field()
    tracked_record_hash: "DestinyRecordDefinition" = attr.field()
    records: Any = attr.field()
    record_categories_root_node_hash: "DestinyPresentationNodeDefinition" = attr.field()
    record_seals_root_node_hash: "DestinyPresentationNodeDefinition" = attr.field()


@attr.define
class DestinyCharacterRecordsComponent(BaseModel):
    """
    _No description given by bungie_

    Attributes:
        featured_record_hashes: _No description given by bungie_
        records: _No description given by bungie_
        record_categories_root_node_hash: The hash for the root presentation node definition of Triumph categories.
        record_seals_root_node_hash: The hash for the root presentation node definition of Triumph Seals.
    """

    featured_record_hashes: list["DestinyRecordDefinition"] = attr.field()
    records: Any = attr.field()
    record_categories_root_node_hash: "DestinyPresentationNodeDefinition" = attr.field()
    record_seals_root_node_hash: "DestinyPresentationNodeDefinition" = attr.field()
