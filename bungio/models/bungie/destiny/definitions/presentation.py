# DO NOT CHANGE ANY CODE BELOW
# This file is generated automatically by `generate_api_schema.py` and will be overwritten
# Instead, change functions / models by subclassing them in the `./overwrites/` folder. They will be used instead.

from typing import TYPE_CHECKING, Optional, Union

import attr

from bungio.models.base import BaseModel, ManifestModel
from bungio.utils import enum_converter

if TYPE_CHECKING:
    from bungio.models import (
        DestinyCollectibleDefinition,
        DestinyDisplayPropertiesDefinition,
        DestinyInventoryItemDefinition,
        DestinyMetricDefinition,
        DestinyObjectiveDefinition,
        DestinyPresentationDisplayStyle,
        DestinyPresentationNodeType,
        DestinyPresentationScreenStyle,
        DestinyRecordDefinition,
        DestinyScope,
    )


@attr.define
class DestinyPresentationNodeBaseDefinition(BaseModel):
    """
    This is the base class for all presentation system children. Presentation Nodes, Records, Collectibles, and Metrics.

    None
    Attributes:
        hash: The unique identifier for this entity. Guaranteed to be unique for the type of entity, but not globally. When entities refer to each other in Destiny content, it is this hash that they are referring to.
        index: The index of the entity as it was found in the investment tables.
        parent_node_hashes: A quick reference to presentation nodes that have this node as a child. Presentation nodes can be parented under multiple parents.
        presentation_node_type: _No description given by bungie._
        redacted: If this is true, then there is an entity with this identifier/type combination, but BNet is not yet allowed to show it. Sorry!
        trait_hashes: _No description given by bungie._
        trait_ids: _No description given by bungie._
    """

    hash: int = attr.field()
    index: int = attr.field()
    parent_node_hashes: list[int] = attr.field(metadata={"type": """list[int]"""})
    presentation_node_type: Union["DestinyPresentationNodeType", int] = attr.field(
        converter=enum_converter("DestinyPresentationNodeType")
    )
    redacted: bool = attr.field()
    trait_hashes: list[int] = attr.field(metadata={"type": """list[int]"""})
    trait_ids: list[str] = attr.field(metadata={"type": """list[str]"""})


@attr.define
class DestinyScoredPresentationNodeBaseDefinition(BaseModel):
    """
    _No description given by bungie._

    None
    Attributes:
        hash: The unique identifier for this entity. Guaranteed to be unique for the type of entity, but not globally. When entities refer to each other in Destiny content, it is this hash that they are referring to.
        index: The index of the entity as it was found in the investment tables.
        max_category_record_score: _No description given by bungie._
        parent_node_hashes: A quick reference to presentation nodes that have this node as a child. Presentation nodes can be parented under multiple parents.
        presentation_node_type: _No description given by bungie._
        redacted: If this is true, then there is an entity with this identifier/type combination, but BNet is not yet allowed to show it. Sorry!
        trait_hashes: _No description given by bungie._
        trait_ids: _No description given by bungie._
    """

    hash: int = attr.field()
    index: int = attr.field()
    max_category_record_score: int = attr.field()
    parent_node_hashes: list[int] = attr.field(metadata={"type": """list[int]"""})
    presentation_node_type: Union["DestinyPresentationNodeType", int] = attr.field(
        converter=enum_converter("DestinyPresentationNodeType")
    )
    redacted: bool = attr.field()
    trait_hashes: list[int] = attr.field(metadata={"type": """list[int]"""})
    trait_ids: list[str] = attr.field(metadata={"type": """list[str]"""})


@attr.define
class DestinyPresentationNodeDefinition(ManifestModel):
    """
    A PresentationNode is an entity that represents a logical grouping of other entities visually/organizationally. For now, Presentation Nodes may contain the following... but it may be used for more in the future: - Collectibles - Records (Or, as the public will call them, "Triumphs." Don't ask me why we're overloading the term "Triumph", it still hurts me to think about it) - Metrics (aka Stat Trackers) - Other Presentation Nodes, allowing a tree of Presentation Nodes to be created Part of me wants to break these into conceptual definitions per entity being collected, but the possibility of these different types being mixed in the same UI and the possibility that it could actually be more useful to return the "bare metal" presentation node concept has resulted in me deciding against that for the time being. We'll see if I come to regret this as well.

    Tip: Manifest Information
        This model has some attributes which can be filled with additional information found in the manifest (`manifest_...`).
        Without additional work, these attributes will be `None`, since they require additional requests and database lookups.

        To fill the manifest dependent attributes, either:

        - Run `await ThisClass.fetch_manifest_information()`, see [here](/API Reference/Models/base)
        - Set `Client.always_return_manifest_information` to `True`, see [here](/API Reference/client)

    Attributes:
        children: The child entities contained by this presentation node.
        completion_record_hash: If this presentation node has an associated "Record" that you can accomplish for completing its children, this is the identifier of that Record.
        disable_child_subscreen_navigation: If this presentation node has children, but the game doesn't let you inspect the details of those children, that is indicated here.
        display_properties: _No description given by bungie._
        display_style: A hint for how to display this presentation node when it's shown in a list.
        hash: The unique identifier for this entity. Guaranteed to be unique for the type of entity, but not globally. When entities refer to each other in Destiny content, it is this hash that they are referring to.
        index: The index of the entity as it was found in the investment tables.
        max_category_record_score: _No description given by bungie._
        node_type: _No description given by bungie._
        objective_hash: If this presentation node shows a related objective (for instance, if it tracks the progress of its children), the objective being tracked is indicated here.
        original_icon: The original icon for this presentation node, before we futzed with it.
        parent_node_hashes: A quick reference to presentation nodes that have this node as a child. Presentation nodes can be parented under multiple parents.
        presentation_node_type: _No description given by bungie._
        redacted: If this is true, then there is an entity with this identifier/type combination, but BNet is not yet allowed to show it. Sorry!
        requirements: The requirements for being able to interact with this presentation node and its children.
        root_view_icon: Some presentation nodes are meant to be explicitly shown on the "root" or "entry" screens for the feature to which they are related. You should use this icon when showing them on such a view, if you have a similar "entry point" view in your UI. If you don't have a UI, then I guess it doesn't matter either way does it?
        scope: Indicates whether this presentation node's state is determined on a per-character or on an account-wide basis.
        screen_style: A hint for how to display this presentation node when it's shown in its own detail screen.
        trait_hashes: _No description given by bungie._
        trait_ids: _No description given by bungie._
        manifest_completion_record_hash: Manifest information for `completion_record_hash`
        manifest_objective_hash: Manifest information for `objective_hash`
    """

    children: "DestinyPresentationNodeChildrenBlock" = attr.field()
    completion_record_hash: int = attr.field()
    disable_child_subscreen_navigation: bool = attr.field()
    display_properties: "DestinyDisplayPropertiesDefinition" = attr.field()
    display_style: Union["DestinyPresentationDisplayStyle", int] = attr.field(
        converter=enum_converter("DestinyPresentationDisplayStyle")
    )
    hash: int = attr.field()
    index: int = attr.field()
    max_category_record_score: int = attr.field()
    node_type: Union["DestinyPresentationNodeType", int] = attr.field(
        converter=enum_converter("DestinyPresentationNodeType")
    )
    objective_hash: int = attr.field()
    original_icon: str = attr.field()
    parent_node_hashes: list[int] = attr.field(metadata={"type": """list[int]"""})
    presentation_node_type: Union["DestinyPresentationNodeType", int] = attr.field(
        converter=enum_converter("DestinyPresentationNodeType")
    )
    redacted: bool = attr.field()
    requirements: "DestinyPresentationNodeRequirementsBlock" = attr.field()
    root_view_icon: str = attr.field()
    scope: Union["DestinyScope", int] = attr.field(converter=enum_converter("DestinyScope"))
    screen_style: Union["DestinyPresentationScreenStyle", int] = attr.field(
        converter=enum_converter("DestinyPresentationScreenStyle")
    )
    trait_hashes: list[int] = attr.field(metadata={"type": """list[int]"""})
    trait_ids: list[str] = attr.field(metadata={"type": """list[str]"""})
    manifest_completion_record_hash: Optional["DestinyRecordDefinition"] = attr.field(default=None)
    manifest_objective_hash: Optional["DestinyObjectiveDefinition"] = attr.field(default=None)


@attr.define
class DestinyPresentationNodeChildrenBlock(BaseModel):
    """
    As/if presentation nodes begin to host more entities as children, these lists will be added to. One list property exists per type of entity that can be treated as a child of this presentation node, and each holds the identifier of the entity and any associated information needed to display the UI for that entity (if anything)

    None
    Attributes:
        collectibles: _No description given by bungie._
        craftables: _No description given by bungie._
        metrics: _No description given by bungie._
        presentation_nodes: _No description given by bungie._
        records: _No description given by bungie._
    """

    collectibles: list["DestinyPresentationNodeCollectibleChildEntry"] = attr.field(
        metadata={"type": """list[DestinyPresentationNodeCollectibleChildEntry]"""}
    )
    craftables: list["DestinyPresentationNodeCraftableChildEntry"] = attr.field(
        metadata={"type": """list[DestinyPresentationNodeCraftableChildEntry]"""}
    )
    metrics: list["DestinyPresentationNodeMetricChildEntry"] = attr.field(
        metadata={"type": """list[DestinyPresentationNodeMetricChildEntry]"""}
    )
    presentation_nodes: list["DestinyPresentationNodeChildEntry"] = attr.field(
        metadata={"type": """list[DestinyPresentationNodeChildEntry]"""}
    )
    records: list["DestinyPresentationNodeRecordChildEntry"] = attr.field(
        metadata={"type": """list[DestinyPresentationNodeRecordChildEntry]"""}
    )


@attr.define
class DestinyPresentationNodeChildEntryBase(BaseModel):
    """
    _No description given by bungie._

    None
    Attributes:
        node_display_priority: Use this value to sort the presentation node children in ascending order.
    """

    node_display_priority: int = attr.field()


@attr.define
class DestinyPresentationNodeChildEntry(BaseModel):
    """
    _No description given by bungie._

    Tip: Manifest Information
        This model has some attributes which can be filled with additional information found in the manifest (`manifest_...`).
        Without additional work, these attributes will be `None`, since they require additional requests and database lookups.

        To fill the manifest dependent attributes, either:

        - Run `await ThisClass.fetch_manifest_information()`, see [here](/API Reference/Models/base)
        - Set `Client.always_return_manifest_information` to `True`, see [here](/API Reference/client)

    Attributes:
        node_display_priority: Use this value to sort the presentation node children in ascending order.
        presentation_node_hash: _No description given by bungie._
        manifest_presentation_node_hash: Manifest information for `presentation_node_hash`
    """

    node_display_priority: int = attr.field()
    presentation_node_hash: int = attr.field()
    manifest_presentation_node_hash: Optional["DestinyPresentationNodeDefinition"] = attr.field(default=None)


@attr.define
class DestinyPresentationNodeCollectibleChildEntry(BaseModel):
    """
    _No description given by bungie._

    Tip: Manifest Information
        This model has some attributes which can be filled with additional information found in the manifest (`manifest_...`).
        Without additional work, these attributes will be `None`, since they require additional requests and database lookups.

        To fill the manifest dependent attributes, either:

        - Run `await ThisClass.fetch_manifest_information()`, see [here](/API Reference/Models/base)
        - Set `Client.always_return_manifest_information` to `True`, see [here](/API Reference/client)

    Attributes:
        collectible_hash: _No description given by bungie._
        node_display_priority: Use this value to sort the presentation node children in ascending order.
        manifest_collectible_hash: Manifest information for `collectible_hash`
    """

    collectible_hash: int = attr.field()
    node_display_priority: int = attr.field()
    manifest_collectible_hash: Optional["DestinyCollectibleDefinition"] = attr.field(default=None)


@attr.define
class DestinyPresentationNodeRequirementsBlock(BaseModel):
    """
    Presentation nodes can be restricted by various requirements. This defines the rules of those requirements, and the message(s) to be shown if these requirements aren't met.

    None
    Attributes:
        entitlement_unavailable_message: If this node is not accessible due to Entitlements (for instance, you don't own the required game expansion), this is the message to show.
    """

    entitlement_unavailable_message: str = attr.field()


@attr.define
class DestinyPresentationChildBlock(BaseModel):
    """
    _No description given by bungie._

    None
    Attributes:
        display_style: _No description given by bungie._
        parent_presentation_node_hashes: _No description given by bungie._
        presentation_node_type: _No description given by bungie._
    """

    display_style: Union["DestinyPresentationDisplayStyle", int] = attr.field(
        converter=enum_converter("DestinyPresentationDisplayStyle")
    )
    parent_presentation_node_hashes: list[int] = attr.field(metadata={"type": """list[int]"""})
    presentation_node_type: Union["DestinyPresentationNodeType", int] = attr.field(
        converter=enum_converter("DestinyPresentationNodeType")
    )


@attr.define
class DestinyPresentationNodeRecordChildEntry(BaseModel):
    """
    _No description given by bungie._

    Tip: Manifest Information
        This model has some attributes which can be filled with additional information found in the manifest (`manifest_...`).
        Without additional work, these attributes will be `None`, since they require additional requests and database lookups.

        To fill the manifest dependent attributes, either:

        - Run `await ThisClass.fetch_manifest_information()`, see [here](/API Reference/Models/base)
        - Set `Client.always_return_manifest_information` to `True`, see [here](/API Reference/client)

    Attributes:
        node_display_priority: Use this value to sort the presentation node children in ascending order.
        record_hash: _No description given by bungie._
        manifest_record_hash: Manifest information for `record_hash`
    """

    node_display_priority: int = attr.field()
    record_hash: int = attr.field()
    manifest_record_hash: Optional["DestinyRecordDefinition"] = attr.field(default=None)


@attr.define
class DestinyPresentationNodeMetricChildEntry(BaseModel):
    """
    _No description given by bungie._

    Tip: Manifest Information
        This model has some attributes which can be filled with additional information found in the manifest (`manifest_...`).
        Without additional work, these attributes will be `None`, since they require additional requests and database lookups.

        To fill the manifest dependent attributes, either:

        - Run `await ThisClass.fetch_manifest_information()`, see [here](/API Reference/Models/base)
        - Set `Client.always_return_manifest_information` to `True`, see [here](/API Reference/client)

    Attributes:
        metric_hash: _No description given by bungie._
        node_display_priority: Use this value to sort the presentation node children in ascending order.
        manifest_metric_hash: Manifest information for `metric_hash`
    """

    metric_hash: int = attr.field()
    node_display_priority: int = attr.field()
    manifest_metric_hash: Optional["DestinyMetricDefinition"] = attr.field(default=None)


@attr.define
class DestinyPresentationNodeCraftableChildEntry(BaseModel):
    """
    _No description given by bungie._

    Tip: Manifest Information
        This model has some attributes which can be filled with additional information found in the manifest (`manifest_...`).
        Without additional work, these attributes will be `None`, since they require additional requests and database lookups.

        To fill the manifest dependent attributes, either:

        - Run `await ThisClass.fetch_manifest_information()`, see [here](/API Reference/Models/base)
        - Set `Client.always_return_manifest_information` to `True`, see [here](/API Reference/client)

    Attributes:
        craftable_item_hash: _No description given by bungie._
        node_display_priority: Use this value to sort the presentation node children in ascending order.
        manifest_craftable_item_hash: Manifest information for `craftable_item_hash`
    """

    craftable_item_hash: int = attr.field()
    node_display_priority: int = attr.field()
    manifest_craftable_item_hash: Optional["DestinyInventoryItemDefinition"] = attr.field(default=None)
