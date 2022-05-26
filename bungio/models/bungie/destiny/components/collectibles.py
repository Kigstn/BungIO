import datetime
from typing import TYPE_CHECKING, Any, Optional

import attr

from bungio.models.base import BaseEnum, BaseModel


@attr.define
class DestinyCollectiblesComponent(BaseModel):
    """
    Not specified.

    Attributes:
        collectibles: Not specified.
        collection_categories_root_node_hash: The hash for the root presentation node definition of Collection categories.
        collection_badges_root_node_hash: The hash for the root presentation node definition of Collection Badges.
    """

    collectibles: Any = attr.field()
    collection_categories_root_node_hash: int = attr.field()
    collection_badges_root_node_hash: int = attr.field()


@attr.define
class DestinyCollectibleComponent(BaseModel):
    """
    Not specified.

    Attributes:
        state: Not specified.
    """

    state: int = attr.field()


@attr.define
class DestinyProfileCollectiblesComponent(BaseModel):
    """
        Not specified.

        Attributes:
            recent_collectible_hashes: The list of collectibles determined by the game as having been "recently" acquired.
            newness_flagged_collectible_hashes: The list of collectibles determined by the game as having been "recently" acquired.

    The game client itself actually controls this data, so I personally question whether anyone will get much use out of this: because we can't edit this value through the API. But in case anyone finds it useful, here it is.
            collectibles: Not specified.
            collection_categories_root_node_hash: The hash for the root presentation node definition of Collection categories.
            collection_badges_root_node_hash: The hash for the root presentation node definition of Collection Badges.
    """

    recent_collectible_hashes: list[int] = attr.field()
    newness_flagged_collectible_hashes: list[int] = attr.field()
    collectibles: Any = attr.field()
    collection_categories_root_node_hash: int = attr.field()
    collection_badges_root_node_hash: int = attr.field()
