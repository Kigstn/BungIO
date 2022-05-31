from typing import TYPE_CHECKING

import attr

from bungio.models.base import BaseModel

if TYPE_CHECKING:
    from bungio.models import (
        DestinyCollectibleAcquisitionBlock,
        DestinyCollectibleStateBlock,
        DestinyDisplayPropertiesDefinition,
        DestinyPresentationChildBlock,
        DestinyPresentationNodeRequirementsBlock,
    )


@attr.define
class DestinyCollectibleDefinition(BaseModel):
    """
    Defines a

    Attributes:
        display_properties: _No description given by bungie_
        scope: Indicates whether the state of this Collectible is determined on a per-character or on an account-wide basis.
        source_string: A human readable string for a hint about how to acquire the item.
        source_hash: This is a hash identifier we are building on the BNet side in an attempt to let people group collectibles by similar sources. I can't promise that it's going to be 100% accurate, but if the designers were consistent in assigning the same source strings to items with the same sources, it *ought to* be. No promises though. This hash also doesn't relate to an actual definition, just to note: we've got nothing useful other than the source string for this data.
        item_hash: _No description given by bungie_
        acquisition_info: _No description given by bungie_
        state_info: _No description given by bungie_
        presentation_info: _No description given by bungie_
        presentation_node_type: _No description given by bungie_
        trait_ids: _No description given by bungie_
        trait_hashes: _No description given by bungie_
        parent_node_hashes: A quick reference to presentation nodes that have this node as a child. Presentation nodes can be parented under multiple parents.
        hash: The unique identifier for this entity. Guaranteed to be unique for the type of entity, but not globally. When entities refer to each other in Destiny content, it is this hash that they are referring to.
        index: The index of the entity as it was found in the investment tables.
        redacted: If this is true, then there is an entity with this identifier/type combination, but BNet is not yet allowed to show it. Sorry!
    """

    display_properties: "DestinyDisplayPropertiesDefinition" = attr.field()
    scope: int = attr.field()
    source_string: str = attr.field()
    source_hash: int = attr.field()
    item_hash: int = attr.field()
    acquisition_info: "DestinyCollectibleAcquisitionBlock" = attr.field()
    state_info: "DestinyCollectibleStateBlock" = attr.field()
    presentation_info: "DestinyPresentationChildBlock" = attr.field()
    presentation_node_type: int = attr.field()
    trait_ids: list[str] = attr.field()
    trait_hashes: list[int] = attr.field()
    parent_node_hashes: list[int] = attr.field()
    hash: int = attr.field()
    index: int = attr.field()
    redacted: bool = attr.field()


@attr.define
class DestinyCollectibleAcquisitionBlock(BaseModel):
    """
    _No description given by bungie_

    Attributes:
        acquire_material_requirement_hash: _No description given by bungie_
        acquire_timestamp_unlock_value_hash: _No description given by bungie_
    """

    acquire_material_requirement_hash: int = attr.field()
    acquire_timestamp_unlock_value_hash: int = attr.field()


@attr.define
class DestinyCollectibleStateBlock(BaseModel):
    """
    _No description given by bungie_

    Attributes:
        obscured_override_item_hash: _No description given by bungie_
        requirements: _No description given by bungie_
    """

    obscured_override_item_hash: int = attr.field()
    requirements: "DestinyPresentationNodeRequirementsBlock" = attr.field()
