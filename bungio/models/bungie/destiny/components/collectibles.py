from typing import TYPE_CHECKING

import attr

from bungio.models.base import BaseModel

if TYPE_CHECKING:
    from bungio.models import (
        DestinyCollectibleDefinition,
        DestinyCollectibleState,
        DestinyPresentationNodeDefinition,
    )


@attr.define
class DestinyCollectiblesComponent(BaseModel):
    """
    _No description given by bungie_

    Attributes:
        collectibles: _No description given by bungie_
        collection_categories_root_node_hash: The hash for the root presentation node definition of Collection categories.
        collection_badges_root_node_hash: The hash for the root presentation node definition of Collection Badges.
    """

    collectibles: "DestinyCollectibleDefinition" = attr.field()
    collection_categories_root_node_hash: "DestinyPresentationNodeDefinition" = attr.field()
    collection_badges_root_node_hash: "DestinyPresentationNodeDefinition" = attr.field()


@attr.define
class DestinyCollectibleComponent(BaseModel):
    """
    _No description given by bungie_

    Attributes:
        state: _No description given by bungie_
    """

    state: "DestinyCollectibleState" = attr.field()


@attr.define
class DestinyProfileCollectiblesComponent(BaseModel):
    """
    _No description given by bungie_

    Attributes:
        recent_collectible_hashes: The list of collectibles determined by the game as having been "recently" acquired.
        newness_flagged_collectible_hashes: The list of collectibles determined by the game as having been "recently" acquired. The game client itself actually controls this data, so I personally question whether anyone will get much use out of this: because we can't edit this value through the API. But in case anyone finds it useful, here it is.
        collectibles: _No description given by bungie_
        collection_categories_root_node_hash: The hash for the root presentation node definition of Collection categories.
        collection_badges_root_node_hash: The hash for the root presentation node definition of Collection Badges.
    """

    recent_collectible_hashes: list["DestinyCollectibleDefinition"] = attr.field()
    newness_flagged_collectible_hashes: list["DestinyCollectibleDefinition"] = attr.field()
    collectibles: "DestinyCollectibleDefinition" = attr.field()
    collection_categories_root_node_hash: "DestinyPresentationNodeDefinition" = attr.field()
    collection_badges_root_node_hash: "DestinyPresentationNodeDefinition" = attr.field()
