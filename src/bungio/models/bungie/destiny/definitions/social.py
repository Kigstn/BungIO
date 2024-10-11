# DO NOT CHANGE ANY CODE BELOW
# This file is generated automatically by `generate_api_schema.py` and will be overwritten
# Instead, change functions / models by subclassing them in the `./overwrites/` folder. They will be used instead.

from typing import TYPE_CHECKING, Optional

from bungio.models.base import HashObject, ManifestModel, custom_define, custom_field

if TYPE_CHECKING:
    from bungio.models import DestinyColor, DestinyDisplayPropertiesDefinition


@custom_define()
class DestinySocialCommendationNodeDefinition(ManifestModel, HashObject):
    """
    _No description given by bungie._

    Tip: Manifest Information
        This model has some attributes which can be filled with additional information found in the manifest (`manifest_...`).
        Without additional work, these attributes will be `None`, since they require additional requests and database lookups.

        To fill the manifest dependent attributes, either:

        - Run `await ThisClass.fetch_manifest_information()`, see [here](/API Reference/Models/base)
        - Set `Client.always_return_manifest_information` to `True`, see [here](/API Reference/client)

    Attributes:
        child_commendation_hashes: A list of hashes that map to child commendations.
        child_commendation_node_hashes: A list of hashes that map to child commendation nodes. Only the root commendations node is expected to have child nodes.
        color: The color associated with this group of commendations.
        display_properties: _No description given by bungie._
        hash: The unique identifier for this entity. Guaranteed to be unique for the type of entity, but not globally. When entities refer to each other in Destiny content, it is this hash that they are referring to.
        index: The index of the entity as it was found in the investment tables.
        parent_commendation_node_hash: _No description given by bungie._
        redacted: If this is true, then there is an entity with this identifier/type combination, but BNet is not yet allowed to show it. Sorry!
        tinted_icon: A version of the displayProperties icon tinted with the color of this node.
        manifest_parent_commendation_node_hash: Manifest information for `parent_commendation_node_hash`
    """

    child_commendation_hashes: list[int] = custom_field(metadata={"type": """list[int]"""})
    child_commendation_node_hashes: list[int] = custom_field(metadata={"type": """list[int]"""})
    color: "DestinyColor" = custom_field()
    display_properties: "DestinyDisplayPropertiesDefinition" = custom_field()
    index: int = custom_field()
    parent_commendation_node_hash: int = custom_field()
    redacted: bool = custom_field()
    tinted_icon: str = custom_field()
    manifest_parent_commendation_node_hash: Optional["DestinySocialCommendationNodeDefinition"] = custom_field(
        default=None
    )


@custom_define()
class DestinySocialCommendationDefinition(ManifestModel, HashObject):
    """
    _No description given by bungie._

    Tip: Manifest Information
        This model has some attributes which can be filled with additional information found in the manifest (`manifest_...`).
        Without additional work, these attributes will be `None`, since they require additional requests and database lookups.

        To fill the manifest dependent attributes, either:

        - Run `await ThisClass.fetch_manifest_information()`, see [here](/API Reference/Models/base)
        - Set `Client.always_return_manifest_information` to `True`, see [here](/API Reference/client)

    Attributes:
        activity_giving_limit: _No description given by bungie._
        card_image_path: _No description given by bungie._
        color: _No description given by bungie._
        display_activities: The display properties for the the activities that this commendation is available in.
        display_priority: _No description given by bungie._
        display_properties: _No description given by bungie._
        hash: The unique identifier for this entity. Guaranteed to be unique for the type of entity, but not globally. When entities refer to each other in Destiny content, it is this hash that they are referring to.
        index: The index of the entity as it was found in the investment tables.
        parent_commendation_node_hash: _No description given by bungie._
        redacted: If this is true, then there is an entity with this identifier/type combination, but BNet is not yet allowed to show it. Sorry!
        manifest_parent_commendation_node_hash: Manifest information for `parent_commendation_node_hash`
    """

    activity_giving_limit: int = custom_field()
    card_image_path: str = custom_field()
    color: "DestinyColor" = custom_field()
    display_activities: list["DestinyDisplayPropertiesDefinition"] = custom_field(
        metadata={"type": """list[DestinyDisplayPropertiesDefinition]"""}
    )
    display_priority: int = custom_field()
    display_properties: "DestinyDisplayPropertiesDefinition" = custom_field()
    index: int = custom_field()
    parent_commendation_node_hash: int = custom_field()
    redacted: bool = custom_field()
    manifest_parent_commendation_node_hash: Optional["DestinySocialCommendationNodeDefinition"] = custom_field(
        default=None
    )
