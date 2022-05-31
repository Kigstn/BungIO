from typing import TYPE_CHECKING

import attr

from bungio.models.base import BaseModel

if TYPE_CHECKING:
    from bungio.models import DestinyDisplayPropertiesDefinition


@attr.define
class DestinyMetricDefinition(BaseModel):
    """
    _No description given_

    Attributes:
        display_properties: _No description given_
        tracking_objective_hash: _No description given_
        lower_value_is_better: _No description given_
        presentation_node_type: _No description given_
        trait_ids: _No description given_
        trait_hashes: _No description given_
        parent_node_hashes: A quick reference to presentation nodes that have this node as a child. Presentation nodes can be parented under multiple parents.
        hash: The unique identifier for this entity. Guaranteed to be unique for the type of entity, but not globally. When entities refer to each other in Destiny content, it is this hash that they are referring to.
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
