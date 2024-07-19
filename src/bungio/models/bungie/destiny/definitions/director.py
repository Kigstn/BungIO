# DO NOT CHANGE ANY CODE BELOW
# This file is generated automatically by `generate_api_schema.py` and will be overwritten
# Instead, change functions / models by subclassing them in the `./overwrites/` folder. They will be used instead.

from typing import Optional, Union, TYPE_CHECKING

from bungio.utils import enum_converter
from bungio.models.base import BaseModel, HashObject, ManifestModel, custom_define, custom_field


if TYPE_CHECKING:
    from bungio.models import DestinyObjectiveDefinition
    from bungio.models import DestinyDisplayPropertiesDefinition
    from bungio.models import DestinyPositionDefinition
    from bungio.models import ActivityGraphNodeHighlightType
    from bungio.models import DestinyGraphNodeState
    from bungio.models import DestinyUnlockExpressionDefinition
    from bungio.models import DestinyActivityDefinition


@custom_define()
class DestinyActivityGraphDefinition(ManifestModel, HashObject):
    """
    Represents a Map View in the director: be them overview views, destination views, or other. They have nodes which map to activities, and other various visual elements that we (or others) may or may not be able to use. Activity graphs, most importantly, have nodes which can have activities in various states of playability. Unfortunately, activity graphs are combined at runtime with Game UI-only assets such as fragments of map images, various in-game special effects, decals etc... that we don't get in these definitions. If we end up having time, we may end up trying to manually populate those here: but the last time we tried that, before the lead-up to D1, it proved to be unmaintainable as the game's content changed. So don't bet the farm on us providing that content in this definition.

    None
    Attributes:
        art_elements: Represents one-off/special UI elements that appear on the map.
        connections: Represents connections between graph nodes. However, it lacks context that we'd need to make good use of it.
        display_objectives: Objectives can display on maps, and this is supposedly metadata for that. I have not had the time to analyze the details of what is useful within however: we could be missing important data to make this work. Expect this property to be expanded on later if possible.
        display_progressions: Progressions can also display on maps, but similarly to displayObjectives we appear to lack some required information and context right now. We will have to look into it later and add more data if possible.
        hash: The unique identifier for this entity. Guaranteed to be unique for the type of entity, but not globally. When entities refer to each other in Destiny content, it is this hash that they are referring to.
        index: The index of the entity as it was found in the investment tables.
        linked_graphs: Represents links between this Activity Graph and other ones.
        nodes: These represent the visual "nodes" on the map's view. These are the activities you can click on in the map.
        redacted: If this is true, then there is an entity with this identifier/type combination, but BNet is not yet allowed to show it. Sorry!
    """

    art_elements: list["DestinyActivityGraphArtElementDefinition"] = custom_field(
        metadata={"type": """list[DestinyActivityGraphArtElementDefinition]"""}
    )
    connections: list["DestinyActivityGraphConnectionDefinition"] = custom_field(
        metadata={"type": """list[DestinyActivityGraphConnectionDefinition]"""}
    )
    display_objectives: list["DestinyActivityGraphDisplayObjectiveDefinition"] = custom_field(
        metadata={"type": """list[DestinyActivityGraphDisplayObjectiveDefinition]"""}
    )
    display_progressions: list["DestinyActivityGraphDisplayProgressionDefinition"] = custom_field(
        metadata={"type": """list[DestinyActivityGraphDisplayProgressionDefinition]"""}
    )
    index: int = custom_field()
    linked_graphs: list["DestinyLinkedGraphDefinition"] = custom_field(
        metadata={"type": """list[DestinyLinkedGraphDefinition]"""}
    )
    nodes: list["DestinyActivityGraphNodeDefinition"] = custom_field(
        metadata={"type": """list[DestinyActivityGraphNodeDefinition]"""}
    )
    redacted: bool = custom_field()


@custom_define()
class DestinyActivityGraphNodeDefinition(BaseModel):
    """
    This is the position and other data related to nodes in the activity graph that you can click to launch activities. An Activity Graph node will only have one active Activity at a time, which will determine the activity to be launched (and, unless overrideDisplay information is provided, will also determine the tooltip and other UI related to the node)

    None
    Attributes:
        activities: The node may have various possible activities that could be active for it, however only one may be active at a time. See the DestinyActivityGraphNodeActivityDefinition for details.
        featuring_states: The node may have various visual accents placed on it, or styles applied. These are the list of possible styles that the Node can have. The game iterates through each, looking for the first one that passes a check of the required game/character/account state in order to show that style, and then renders the node in that style.
        node_id: An identifier for the Activity Graph Node, only guaranteed to be unique within its parent Activity Graph.
        override_display: The node *may* have display properties that override the active Activity's display properties.
        position: The position on the map for this node.
        states: Represents possible states that the graph node can be in. These are combined with some checking that happens in the game client and server to determine which state is actually active at any given time.
    """

    activities: list["DestinyActivityGraphNodeActivityDefinition"] = custom_field(
        metadata={"type": """list[DestinyActivityGraphNodeActivityDefinition]"""}
    )
    featuring_states: list["DestinyActivityGraphNodeFeaturingStateDefinition"] = custom_field(
        metadata={"type": """list[DestinyActivityGraphNodeFeaturingStateDefinition]"""}
    )
    node_id: int = custom_field()
    override_display: "DestinyDisplayPropertiesDefinition" = custom_field()
    position: "DestinyPositionDefinition" = custom_field()
    states: list["DestinyActivityGraphNodeStateEntry"] = custom_field(
        metadata={"type": """list[DestinyActivityGraphNodeStateEntry]"""}
    )


@custom_define()
class DestinyActivityGraphNodeFeaturingStateDefinition(BaseModel):
    """
    Nodes can have different visual states. This object represents a single visual state ("highlight type") that a node can be in, and the unlock expression condition to determine whether it should be set.

    None
    Attributes:
        highlight_type: The node can be highlighted in a variety of ways - the game iterates through these and finds the first FeaturingState that is valid at the present moment given the Game, Account, and Character state, and renders the node in that state. See the ActivityGraphNodeHighlightType enum for possible values.
    """

    highlight_type: Union["ActivityGraphNodeHighlightType", int] = custom_field(
        converter=enum_converter("ActivityGraphNodeHighlightType")
    )


@custom_define()
class DestinyActivityGraphNodeActivityDefinition(BaseModel):
    """
    The actual activity to be redirected to when you click on the node. Note that a node can have many Activities attached to it: but only one will be active at any given time. The list of Node Activities will be traversed, and the first one found to be active will be displayed. This way, a node can layer multiple variants of an activity on top of each other. For instance, one node can control the weekly Crucible Playlist. There are multiple possible playlists, but only one is active for the week.

    Tip: Manifest Information
        This model has some attributes which can be filled with additional information found in the manifest (`manifest_...`).
        Without additional work, these attributes will be `None`, since they require additional requests and database lookups.

        To fill the manifest dependent attributes, either:

        - Run `await ThisClass.fetch_manifest_information()`, see [here](/API Reference/Models/base)
        - Set `Client.always_return_manifest_information` to `True`, see [here](/API Reference/client)

    Attributes:
        activity_hash: The activity that will be activated if the user clicks on this node. Controls all activity-related information displayed on the node if it is active (the text shown in the tooltip etc)
        node_activity_id: An identifier for this node activity. It is only guaranteed to be unique within the Activity Graph.
        manifest_activity_hash: Manifest information for `activity_hash`
    """

    activity_hash: int = custom_field()
    node_activity_id: int = custom_field()
    manifest_activity_hash: Optional["DestinyActivityDefinition"] = custom_field(default=None)


@custom_define()
class DestinyActivityGraphNodeStateEntry(BaseModel):
    """
    Represents a single state that a graph node might end up in. Depending on what's going on in the game, graph nodes could be shown in different ways or even excluded from view entirely.

    None
    Attributes:
        state: _No description given by bungie._
    """

    state: Union["DestinyGraphNodeState", int] = custom_field(converter=enum_converter("DestinyGraphNodeState"))


@custom_define()
class DestinyActivityGraphArtElementDefinition(BaseModel):
    """
    These Art Elements are meant to represent one-off visual effects overlaid on the map. Currently, we do not have a pipeline to import the assets for these overlays, so this info exists as a placeholder for when such a pipeline exists (if it ever will)

    None
    Attributes:
        position: The position on the map of the art element.
    """

    position: "DestinyPositionDefinition" = custom_field()


@custom_define()
class DestinyActivityGraphConnectionDefinition(BaseModel):
    """
    Nodes on a graph can be visually connected: this appears to be the information about which nodes to link. It appears to lack more detailed information, such as the path for that linking.

    None
    Attributes:
        dest_node_hash: _No description given by bungie._
        source_node_hash: _No description given by bungie._
    """

    dest_node_hash: int = custom_field()
    source_node_hash: int = custom_field()


@custom_define()
class DestinyActivityGraphDisplayObjectiveDefinition(BaseModel):
    """
    When a Graph needs to show active Objectives, this defines those objectives as well as an identifier.

    Tip: Manifest Information
        This model has some attributes which can be filled with additional information found in the manifest (`manifest_...`).
        Without additional work, these attributes will be `None`, since they require additional requests and database lookups.

        To fill the manifest dependent attributes, either:

        - Run `await ThisClass.fetch_manifest_information()`, see [here](/API Reference/Models/base)
        - Set `Client.always_return_manifest_information` to `True`, see [here](/API Reference/client)

    Attributes:
        id: $NOTE $amola 2017-01-19 This field is apparently something that CUI uses to manually wire up objectives to display info. I am unsure how it works.
        objective_hash: The objective being shown on the map.
        manifest_objective_hash: Manifest information for `objective_hash`
    """

    id: int = custom_field()
    objective_hash: int = custom_field()
    manifest_objective_hash: Optional["DestinyObjectiveDefinition"] = custom_field(default=None)


@custom_define()
class DestinyActivityGraphDisplayProgressionDefinition(BaseModel):
    """
    When a Graph needs to show active Progressions, this defines those objectives as well as an identifier.

    None
    Attributes:
        id: _No description given by bungie._
        progression_hash: _No description given by bungie._
    """

    id: int = custom_field()
    progression_hash: int = custom_field()


@custom_define()
class DestinyLinkedGraphDefinition(BaseModel):
    """
    This describes links between the current graph and others, as well as when that link is relevant.

    None
    Attributes:
        description: _No description given by bungie._
        linked_graph_id: _No description given by bungie._
        linked_graphs: _No description given by bungie._
        name: _No description given by bungie._
        overview: _No description given by bungie._
        unlock_expression: _No description given by bungie._
    """

    description: str = custom_field()
    linked_graph_id: int = custom_field()
    linked_graphs: list["DestinyLinkedGraphEntryDefinition"] = custom_field(
        metadata={"type": """list[DestinyLinkedGraphEntryDefinition]"""}
    )
    name: str = custom_field()
    overview: str = custom_field()
    unlock_expression: "DestinyUnlockExpressionDefinition" = custom_field()


@custom_define()
class DestinyLinkedGraphEntryDefinition(BaseModel):
    """
    _No description given by bungie._

    None
    Attributes:
        activity_graph_hash: _No description given by bungie._
    """

    activity_graph_hash: int = custom_field()
