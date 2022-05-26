import datetime
from typing import TYPE_CHECKING, Any, Optional

import attr

from bungio.models.base import BaseEnum, BaseModel


@attr.define
class DestinyRecordsComponent(BaseModel):
    """
    Not specified.

    Attributes:
        records: Not specified.
        record_categories_root_node_hash: The hash for the root presentation node definition of Triumph categories.
        record_seals_root_node_hash: The hash for the root presentation node definition of Triumph Seals.
    """

    records: Any = attr.field()
    record_categories_root_node_hash: int = attr.field()
    record_seals_root_node_hash: int = attr.field()


@attr.define
class DestinyRecordComponent(BaseModel):
    """
    Not specified.

    Attributes:
        state: Not specified.
        objectives: Not specified.
        interval_objectives: Not specified.
        intervals_redeemed_count: Not specified.
        completed_count: If available, this is the number of times this record has been completed. For example, the number of times a seal title has been gilded.
        reward_visibilty: If available, a list that describes which reward rewards should be shown (true) or hidden (false). This property is for regular record rewards, and not for interval objective rewards.
    """

    state: int = attr.field()
    objectives: list["DestinyObjectiveProgress"] = attr.field()
    interval_objectives: list["DestinyObjectiveProgress"] = attr.field()
    intervals_redeemed_count: int = attr.field()
    completed_count: int = attr.field()
    reward_visibilty: list[bool] = attr.field()


@attr.define
class DestinyProfileRecordsComponent(BaseModel):
    """
    Not specified.

    Attributes:
        score: Your 'active' Triumphs score, maintained for backwards compatibility.
        active_score: Your 'active' Triumphs score.
        legacy_score: Your 'legacy' Triumphs score.
        lifetime_score: Your 'lifetime' Triumphs score.
        tracked_record_hash: If this profile is tracking a record, this is the hash identifier of the record it is tracking.
        records: Not specified.
        record_categories_root_node_hash: The hash for the root presentation node definition of Triumph categories.
        record_seals_root_node_hash: The hash for the root presentation node definition of Triumph Seals.
    """

    score: int = attr.field()
    active_score: int = attr.field()
    legacy_score: int = attr.field()
    lifetime_score: int = attr.field()
    tracked_record_hash: int = attr.field()
    records: Any = attr.field()
    record_categories_root_node_hash: int = attr.field()
    record_seals_root_node_hash: int = attr.field()


@attr.define
class DestinyCharacterRecordsComponent(BaseModel):
    """
    Not specified.

    Attributes:
        featured_record_hashes: Not specified.
        records: Not specified.
        record_categories_root_node_hash: The hash for the root presentation node definition of Triumph categories.
        record_seals_root_node_hash: The hash for the root presentation node definition of Triumph Seals.
    """

    featured_record_hashes: list[int] = attr.field()
    records: Any = attr.field()
    record_categories_root_node_hash: int = attr.field()
    record_seals_root_node_hash: int = attr.field()
