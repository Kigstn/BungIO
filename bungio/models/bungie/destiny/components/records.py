# DO NOT CHANGE ANY CODE BELOW
# This file is generated automatically by `generate_api_schema.py` and will be overwritten
# Instead, change functions / models by subclassing them in the `./overwrites/` folder. They will be used instead.

from typing import TYPE_CHECKING, Optional, Union

import attr

from bungio.models.base import BaseModel
from bungio.utils import enum_converter

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
    _No description given by bungie._

    Tip: Manifest Information
        This model has some attributes which can be filled with additional information found in the manifest (`manifest_...`).
        Without additional work, these attributes will be `None`, since they require additional requests and database lookups.

        To fill the manifest dependent attributes, either:

        - Run `await ThisClass.fetch_manifest_information()`, see [here](/API Reference/Models/base)
        - Set `Client.always_return_manifest_information` to `True`, see [here](/API Reference/client)

    Attributes:
        record_categories_root_node_hash: The hash for the root presentation node definition of Triumph categories.
        record_seals_root_node_hash: The hash for the root presentation node definition of Triumph Seals.
        records: _No description given by bungie._
        manifest_record_categories_root_node_hash: Manifest information for `record_categories_root_node_hash`
        manifest_record_seals_root_node_hash: Manifest information for `record_seals_root_node_hash`
    """

    record_categories_root_node_hash: int = attr.field()
    record_seals_root_node_hash: int = attr.field()
    records: dict[int, "DestinyRecordComponent"] = attr.field(
        metadata={"type": """dict[int, DestinyRecordComponent]"""}
    )
    manifest_record_categories_root_node_hash: Optional["DestinyPresentationNodeDefinition"] = attr.field(default=None)
    manifest_record_seals_root_node_hash: Optional["DestinyPresentationNodeDefinition"] = attr.field(default=None)


@attr.define
class DestinyRecordComponent(BaseModel):
    """
    _No description given by bungie._

    None
    Attributes:
        completed_count: If available, this is the number of times this record has been completed. For example, the number of times a seal title has been gilded.
        interval_objectives: _No description given by bungie._
        intervals_redeemed_count: _No description given by bungie._
        objectives: _No description given by bungie._
        reward_visibilty: If available, a list that describes which reward rewards should be shown (true) or hidden (false). This property is for regular record rewards, and not for interval objective rewards.
        state: _No description given by bungie._
    """

    completed_count: int = attr.field()
    interval_objectives: list["DestinyObjectiveProgress"] = attr.field(
        metadata={"type": """list[DestinyObjectiveProgress]"""}
    )
    intervals_redeemed_count: int = attr.field()
    objectives: list["DestinyObjectiveProgress"] = attr.field(metadata={"type": """list[DestinyObjectiveProgress]"""})
    reward_visibilty: list[bool] = attr.field(metadata={"type": """list[bool]"""})
    state: Union["DestinyRecordState", int] = attr.field(converter=enum_converter("DestinyRecordState"))


@attr.define
class DestinyProfileRecordsComponent(BaseModel):
    """
    _No description given by bungie._

    Tip: Manifest Information
        This model has some attributes which can be filled with additional information found in the manifest (`manifest_...`).
        Without additional work, these attributes will be `None`, since they require additional requests and database lookups.

        To fill the manifest dependent attributes, either:

        - Run `await ThisClass.fetch_manifest_information()`, see [here](/API Reference/Models/base)
        - Set `Client.always_return_manifest_information` to `True`, see [here](/API Reference/client)

    Attributes:
        active_score: Your 'active' Triumphs score.
        legacy_score: Your 'legacy' Triumphs score.
        lifetime_score: Your 'lifetime' Triumphs score.
        record_categories_root_node_hash: The hash for the root presentation node definition of Triumph categories.
        record_seals_root_node_hash: The hash for the root presentation node definition of Triumph Seals.
        records: _No description given by bungie._
        score: Your 'active' Triumphs score, maintained for backwards compatibility.
        tracked_record_hash: If this profile is tracking a record, this is the hash identifier of the record it is tracking.
        manifest_record_categories_root_node_hash: Manifest information for `record_categories_root_node_hash`
        manifest_record_seals_root_node_hash: Manifest information for `record_seals_root_node_hash`
        manifest_tracked_record_hash: Manifest information for `tracked_record_hash`
    """

    active_score: int = attr.field()
    legacy_score: int = attr.field()
    lifetime_score: int = attr.field()
    record_categories_root_node_hash: int = attr.field()
    record_seals_root_node_hash: int = attr.field()
    records: dict[int, "DestinyRecordComponent"] = attr.field(
        metadata={"type": """dict[int, DestinyRecordComponent]"""}
    )
    score: int = attr.field()
    tracked_record_hash: int = attr.field()
    manifest_record_categories_root_node_hash: Optional["DestinyPresentationNodeDefinition"] = attr.field(default=None)
    manifest_record_seals_root_node_hash: Optional["DestinyPresentationNodeDefinition"] = attr.field(default=None)
    manifest_tracked_record_hash: Optional["DestinyRecordDefinition"] = attr.field(default=None)


@attr.define
class DestinyCharacterRecordsComponent(BaseModel):
    """
    _No description given by bungie._

    Tip: Manifest Information
        This model has some attributes which can be filled with additional information found in the manifest (`manifest_...`).
        Without additional work, these attributes will be `None`, since they require additional requests and database lookups.

        To fill the manifest dependent attributes, either:

        - Run `await ThisClass.fetch_manifest_information()`, see [here](/API Reference/Models/base)
        - Set `Client.always_return_manifest_information` to `True`, see [here](/API Reference/client)

    Attributes:
        featured_record_hashes: _No description given by bungie._
        record_categories_root_node_hash: The hash for the root presentation node definition of Triumph categories.
        record_seals_root_node_hash: The hash for the root presentation node definition of Triumph Seals.
        records: _No description given by bungie._
        manifest_record_categories_root_node_hash: Manifest information for `record_categories_root_node_hash`
        manifest_record_seals_root_node_hash: Manifest information for `record_seals_root_node_hash`
    """

    featured_record_hashes: list[int] = attr.field(metadata={"type": """list[int]"""})
    record_categories_root_node_hash: int = attr.field()
    record_seals_root_node_hash: int = attr.field()
    records: dict[int, "DestinyRecordComponent"] = attr.field(
        metadata={"type": """dict[int, DestinyRecordComponent]"""}
    )
    manifest_record_categories_root_node_hash: Optional["DestinyPresentationNodeDefinition"] = attr.field(default=None)
    manifest_record_seals_root_node_hash: Optional["DestinyPresentationNodeDefinition"] = attr.field(default=None)
