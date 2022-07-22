# DO NOT CHANGE ANY CODE BELOW
# This file is generated automatically by `generate_api_schema.py` and will be overwritten
# Instead, change functions / models by subclassing them in the `./overwrites/` folder. They will be used instead.

from typing import TYPE_CHECKING, Optional, Union

import attr

from bungio.models.base import BaseModel
from bungio.utils import enum_converter

if TYPE_CHECKING:
    from bungio.models import DestinyCollectibleState, DestinyPresentationNodeDefinition


@attr.define
class DestinyCollectiblesComponent(BaseModel):
    """
    _No description given by bungie._

    Tip: Manifest Information
        This model has some attributes which can be filled with additional information found in the manifest (`manifest_...`).
        Without additional work, these attributes will be `None`, since they require additional requests and database lookups.

        To fill the manifest dependent attributes, either:

        - Run `await ThisClass.fetch_manifest_information()`, see [here](/API Reference/Models/base)
        - Set `Client.always_return_manifest_information` to `True`, see [here](/API Reference/client)

    Attributes:
        collectibles: _No description given by bungie._
        collection_badges_root_node_hash: The hash for the root presentation node definition of Collection Badges.
        collection_categories_root_node_hash: The hash for the root presentation node definition of Collection categories.
        manifest_collection_badges_root_node_hash: Manifest information for `collection_badges_root_node_hash`
        manifest_collection_categories_root_node_hash: Manifest information for `collection_categories_root_node_hash`
    """

    collectibles: dict[int, "DestinyCollectibleComponent"] = attr.field(
        metadata={"type": """dict[int, DestinyCollectibleComponent]"""}
    )
    collection_badges_root_node_hash: int = attr.field()
    collection_categories_root_node_hash: int = attr.field()
    manifest_collection_badges_root_node_hash: Optional["DestinyPresentationNodeDefinition"] = attr.field(default=None)
    manifest_collection_categories_root_node_hash: Optional["DestinyPresentationNodeDefinition"] = attr.field(
        default=None
    )


@attr.define
class DestinyCollectibleComponent(BaseModel):
    """
    _No description given by bungie._

    None
    Attributes:
        state: _No description given by bungie._
    """

    state: Union["DestinyCollectibleState", int] = attr.field(converter=enum_converter("DestinyCollectibleState"))


@attr.define
class DestinyProfileCollectiblesComponent(BaseModel):
    """
    _No description given by bungie._

    Tip: Manifest Information
        This model has some attributes which can be filled with additional information found in the manifest (`manifest_...`).
        Without additional work, these attributes will be `None`, since they require additional requests and database lookups.

        To fill the manifest dependent attributes, either:

        - Run `await ThisClass.fetch_manifest_information()`, see [here](/API Reference/Models/base)
        - Set `Client.always_return_manifest_information` to `True`, see [here](/API Reference/client)

    Attributes:
        collectibles: _No description given by bungie._
        collection_badges_root_node_hash: The hash for the root presentation node definition of Collection Badges.
        collection_categories_root_node_hash: The hash for the root presentation node definition of Collection categories.
        newness_flagged_collectible_hashes: The list of collectibles determined by the game as having been "recently" acquired. The game client itself actually controls this data, so I personally question whether anyone will get much use out of this: because we can't edit this value through the API. But in case anyone finds it useful, here it is.
        recent_collectible_hashes: The list of collectibles determined by the game as having been "recently" acquired.
        manifest_collection_badges_root_node_hash: Manifest information for `collection_badges_root_node_hash`
        manifest_collection_categories_root_node_hash: Manifest information for `collection_categories_root_node_hash`
    """

    collectibles: dict[int, "DestinyCollectibleComponent"] = attr.field(
        metadata={"type": """dict[int, DestinyCollectibleComponent]"""}
    )
    collection_badges_root_node_hash: int = attr.field()
    collection_categories_root_node_hash: int = attr.field()
    newness_flagged_collectible_hashes: list[int] = attr.field(metadata={"type": """list[int]"""})
    recent_collectible_hashes: list[int] = attr.field(metadata={"type": """list[int]"""})
    manifest_collection_badges_root_node_hash: Optional["DestinyPresentationNodeDefinition"] = attr.field(default=None)
    manifest_collection_categories_root_node_hash: Optional["DestinyPresentationNodeDefinition"] = attr.field(
        default=None
    )
