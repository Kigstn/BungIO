import datetime
from typing import TYPE_CHECKING, Any, Optional

import attr

from bungio.models.base import BaseEnum, BaseModel


@attr.define
class DestinyMetricDefinition(BaseModel):
    """
        Not specified.

        Attributes:
            display_properties: Not specified.
            tracking_objective_hash: Not specified.
            lower_value_is_better: Not specified.
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
    tracking_objective_hash: int = attr.field()
    lower_value_is_better: bool = attr.field()
    presentation_node_type: int = attr.field()
    trait_ids: list[str] = attr.field()
    trait_hashes: list[int] = attr.field()
    parent_node_hashes: list[int] = attr.field()
    hash: int = attr.field()
    index: int = attr.field()
    redacted: bool = attr.field()
