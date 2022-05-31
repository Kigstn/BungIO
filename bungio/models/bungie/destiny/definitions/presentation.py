from typing import TYPE_CHECKING

import attr

from bungio.models.base import BaseModel

if TYPE_CHECKING:
    from bungio.models import (
        DestinyDisplayPropertiesDefinition,
        DestinyPresentationNodeChildEntry,
        DestinyPresentationNodeChildrenBlock,
        DestinyPresentationNodeCollectibleChildEntry,
        DestinyPresentationNodeCraftableChildEntry,
        DestinyPresentationNodeMetricChildEntry,
        DestinyPresentationNodeRecordChildEntry,
        DestinyPresentationNodeRequirementsBlock,
    )


@attr.define
class DestinyPresentationNodeBaseDefinition(BaseModel):
    """
    This is the base class for all presentation system children. Presentation Nodes, Records, Collectibles, and Metrics.

    Attributes:
        presentation_node_type: _No description given by bungie_
        trait_ids: _No description given by bungie_
        trait_hashes: _No description given by bungie_
        parent_node_hashes: A quick reference to presentation nodes that have this node as a child. Presentation nodes can be parented under multiple parents.
        hash: The unique identifier for this entity. Guaranteed to be unique for the type of entity, but not globally. When entities refer to each other in Destiny content, it is this hash that they are referring to.
        index: The index of the entity as it was found in the investment tables.
        redacted: If this is true, then there is an entity with this identifier/type combination, but BNet is not yet allowed to show it. Sorry!
    """

    presentation_node_type: int = attr.field()
    trait_ids: list[str] = attr.field()
    trait_hashes: list[int] = attr.field()
    parent_node_hashes: list[int] = attr.field()
    hash: int = attr.field()
    index: int = attr.field()
    redacted: bool = attr.field()


@attr.define
class DestinyScoredPresentationNodeBaseDefinition(BaseModel):
    """
    _No description given by bungie_

    Attributes:
        max_category_record_score: _No description given by bungie_
        presentation_node_type: _No description given by bungie_
        trait_ids: _No description given by bungie_
        trait_hashes: _No description given by bungie_
        parent_node_hashes: A quick reference to presentation nodes that have this node as a child. Presentation nodes can be parented under multiple parents.
        hash: The unique identifier for this entity. Guaranteed to be unique for the type of entity, but not globally. When entities refer to each other in Destiny content, it is this hash that they are referring to.
        index: The index of the entity as it was found in the investment tables.
        redacted: If this is true, then there is an entity with this identifier/type combination, but BNet is not yet allowed to show it. Sorry!
    """

    max_category_record_score: int = attr.field()
    presentation_node_type: int = attr.field()
    trait_ids: list[str] = attr.field()
    trait_hashes: list[int] = attr.field()
    parent_node_hashes: list[int] = attr.field()
    hash: int = attr.field()
    index: int = attr.field()
    redacted: bool = attr.field()


@attr.define
class DestinyPresentationNodeDefinition(BaseModel):
    """
    A PresentationNode is an entity that represents a logical grouping of other entities visually/organizationally. For now, Presentation Nodes may contain the following... but it may be used for more in the future: - Collectibles - Records (Or, as the public will call them, "Triumphs." Don't ask me why we're overloading the term "Triumph", it still hurts me to think about it) - Metrics (aka Stat Trackers) - Other Presentation Nodes, allowing a tree of Presentation Nodes to be created Part of me wants to break these into conceptual definitions per entity being collected, but the possibility of these different types being mixed in the same UI and the possibility that it could actually be more useful to return the "bare metal" presentation node concept has resulted in me deciding against that for the time being. We'll see if I come to regret this as well.

    Attributes:
        display_properties: _No description given by bungie_
        original_icon: The original icon for this presentation node, before we futzed with it.
        root_view_icon: Some presentation nodes are meant to be explicitly shown on the "root" or "entry" screens for the feature to which they are related. You should use this icon when showing them on such a view, if you have a similar "entry point" view in your UI. If you don't have a UI, then I guess it doesn't matter either way does it?
        node_type: _No description given by bungie_
        scope: Indicates whether this presentation node's state is determined on a per-character or on an account-wide basis.
        objective_hash: If this presentation node shows a related objective (for instance, if it tracks the progress of its children), the objective being tracked is indicated here.
        completion_record_hash: If this presentation node has an associated "Record" that you can accomplish for completing its children, this is the identifier of that Record.
        children: The child entities contained by this presentation node.
        display_style: A hint for how to display this presentation node when it's shown in a list.
        screen_style: A hint for how to display this presentation node when it's shown in its own detail screen.
        requirements: The requirements for being able to interact with this presentation node and its children.
        disable_child_subscreen_navigation: If this presentation node has children, but the game doesn't let you inspect the details of those children, that is indicated here.
        max_category_record_score: _No description given by bungie_
        presentation_node_type: _No description given by bungie_
        trait_ids: _No description given by bungie_
        trait_hashes: _No description given by bungie_
        parent_node_hashes: A quick reference to presentation nodes that have this node as a child. Presentation nodes can be parented under multiple parents.
        hash: The unique identifier for this entity. Guaranteed to be unique for the type of entity, but not globally. When entities refer to each other in Destiny content, it is this hash that they are referring to.
        index: The index of the entity as it was found in the investment tables.
        redacted: If this is true, then there is an entity with this identifier/type combination, but BNet is not yet allowed to show it. Sorry!
    """

    display_properties: "DestinyDisplayPropertiesDefinition" = attr.field()
    original_icon: str = attr.field()
    root_view_icon: str = attr.field()
    node_type: int = attr.field()
    scope: int = attr.field()
    objective_hash: int = attr.field()
    completion_record_hash: int = attr.field()
    children: "DestinyPresentationNodeChildrenBlock" = attr.field()
    display_style: int = attr.field()
    screen_style: int = attr.field()
    requirements: "DestinyPresentationNodeRequirementsBlock" = attr.field()
    disable_child_subscreen_navigation: bool = attr.field()
    max_category_record_score: int = attr.field()
    presentation_node_type: int = attr.field()
    trait_ids: list[str] = attr.field()
    trait_hashes: list[int] = attr.field()
    parent_node_hashes: list[int] = attr.field()
    hash: int = attr.field()
    index: int = attr.field()
    redacted: bool = attr.field()


@attr.define
class DestinyPresentationNodeChildrenBlock(BaseModel):
    """
    As/if presentation nodes begin to host more entities as children, these lists will be added to. One list property exists per type of entity that can be treated as a child of this presentation node, and each holds the identifier of the entity and any associated information needed to display the UI for that entity (if anything)

    Attributes:
        presentation_nodes: _No description given by bungie_
        collectibles: _No description given by bungie_
        records: _No description given by bungie_
        metrics: _No description given by bungie_
        craftables: _No description given by bungie_
    """

    presentation_nodes: list["DestinyPresentationNodeChildEntry"] = attr.field()
    collectibles: list["DestinyPresentationNodeCollectibleChildEntry"] = attr.field()
    records: list["DestinyPresentationNodeRecordChildEntry"] = attr.field()
    metrics: list["DestinyPresentationNodeMetricChildEntry"] = attr.field()
    craftables: list["DestinyPresentationNodeCraftableChildEntry"] = attr.field()


@attr.define
class DestinyPresentationNodeChildEntryBase(BaseModel):
    """
    _No description given by bungie_

    Attributes:
        node_display_priority: Use this value to sort the presentation node children in ascending order.
    """

    node_display_priority: int = attr.field()


@attr.define
class DestinyPresentationNodeChildEntry(BaseModel):
    """
    _No description given by bungie_

    Attributes:
        presentation_node_hash: _No description given by bungie_
        node_display_priority: Use this value to sort the presentation node children in ascending order.
    """

    presentation_node_hash: int = attr.field()
    node_display_priority: int = attr.field()


@attr.define
class DestinyPresentationNodeCollectibleChildEntry(BaseModel):
    """
    _No description given by bungie_

    Attributes:
        collectible_hash: _No description given by bungie_
        node_display_priority: Use this value to sort the presentation node children in ascending order.
    """

    collectible_hash: int = attr.field()
    node_display_priority: int = attr.field()


@attr.define
class DestinyPresentationNodeRequirementsBlock(BaseModel):
    """
    Presentation nodes can be restricted by various requirements. This defines the rules of those requirements, and the message(s) to be shown if these requirements aren't met.

    Attributes:
        entitlement_unavailable_message: If this node is not accessible due to Entitlements (for instance, you don't own the required game expansion), this is the message to show.
    """

    entitlement_unavailable_message: str = attr.field()


@attr.define
class DestinyPresentationChildBlock(BaseModel):
    """
    _No description given by bungie_

    Attributes:
        presentation_node_type: _No description given by bungie_
        parent_presentation_node_hashes: _No description given by bungie_
        display_style: _No description given by bungie_
    """

    presentation_node_type: int = attr.field()
    parent_presentation_node_hashes: list[int] = attr.field()
    display_style: int = attr.field()


@attr.define
class DestinyPresentationNodeRecordChildEntry(BaseModel):
    """
    _No description given by bungie_

    Attributes:
        record_hash: _No description given by bungie_
        node_display_priority: Use this value to sort the presentation node children in ascending order.
    """

    record_hash: int = attr.field()
    node_display_priority: int = attr.field()


@attr.define
class DestinyPresentationNodeMetricChildEntry(BaseModel):
    """
    _No description given by bungie_

    Attributes:
        metric_hash: _No description given by bungie_
        node_display_priority: Use this value to sort the presentation node children in ascending order.
    """

    metric_hash: int = attr.field()
    node_display_priority: int = attr.field()


@attr.define
class DestinyPresentationNodeCraftableChildEntry(BaseModel):
    """
    _No description given by bungie_

    Attributes:
        craftable_item_hash: _No description given by bungie_
        node_display_priority: Use this value to sort the presentation node children in ascending order.
    """

    craftable_item_hash: int = attr.field()
    node_display_priority: int = attr.field()
