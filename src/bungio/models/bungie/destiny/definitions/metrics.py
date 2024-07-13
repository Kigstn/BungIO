# DO NOT CHANGE ANY CODE BELOW
# This file is generated automatically by `generate_api_schema.py` and will be overwritten
# Instead, change functions / models by subclassing them in the `./overwrites/` folder. They will be used instead.

from typing import TYPE_CHECKING, Optional, Union

from bungio.models.base import HashObject, ManifestModel, custom_define, custom_field
from bungio.utils import enum_converter

if TYPE_CHECKING:
    from bungio.models import (
        DestinyDisplayPropertiesDefinition,
        DestinyObjectiveDefinition,
        DestinyPresentationNodeType,
    )


@custom_define()
class DestinyMetricDefinition(ManifestModel, HashObject):
    """
    _No description given by bungie._

    Tip: Manifest Information
        This model has some attributes which can be filled with additional information found in the manifest (`manifest_...`).
        Without additional work, these attributes will be `None`, since they require additional requests and database lookups.

        To fill the manifest dependent attributes, either:

        - Run `await ThisClass.fetch_manifest_information()`, see [here](/API Reference/Models/base)
        - Set `Client.always_return_manifest_information` to `True`, see [here](/API Reference/client)

    Attributes:
        display_properties: _No description given by bungie._
        hash: The unique identifier for this entity. Guaranteed to be unique for the type of entity, but not globally. When entities refer to each other in Destiny content, it is this hash that they are referring to.
        index: The index of the entity as it was found in the investment tables.
        lower_value_is_better: _No description given by bungie._
        parent_node_hashes: A quick reference to presentation nodes that have this node as a child. Presentation nodes can be parented under multiple parents.
        presentation_node_type: _No description given by bungie._
        redacted: If this is true, then there is an entity with this identifier/type combination, but BNet is not yet allowed to show it. Sorry!
        tracking_objective_hash: _No description given by bungie._
        trait_hashes: _No description given by bungie._
        trait_ids: _No description given by bungie._
        manifest_tracking_objective_hash: Manifest information for `tracking_objective_hash`
    """

    display_properties: "DestinyDisplayPropertiesDefinition" = custom_field()
    index: int = custom_field()
    lower_value_is_better: bool = custom_field()
    parent_node_hashes: list[int] = custom_field(metadata={"type": """list[int]"""})
    presentation_node_type: Union["DestinyPresentationNodeType", int] = custom_field(
        converter=enum_converter("DestinyPresentationNodeType")
    )
    redacted: bool = custom_field()
    tracking_objective_hash: int = custom_field()
    trait_hashes: list[int] = custom_field(metadata={"type": """list[int]"""})
    trait_ids: list[str] = custom_field(metadata={"type": """list[str]"""})
    manifest_tracking_objective_hash: Optional["DestinyObjectiveDefinition"] = custom_field(default=None)
