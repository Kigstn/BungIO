# DO NOT CHANGE ANY CODE BELOW
# This file is generated automatically by `generate_api_schema.py` and will be overwritten
# Instead, change functions / models by subclassing them in the `./overwrites/` folder. They will be used instead.

from typing import Optional, TYPE_CHECKING

from bungio.models.base import BaseModel, custom_define, custom_field


if TYPE_CHECKING:
    from bungio.models import DestinyPlugSetDefinition
    from bungio.models import DestinyInventoryItemDefinition
    from bungio.models import DestinyPresentationNodeDefinition


@custom_define()
class DestinyCraftablesComponent(BaseModel):
    """
    _No description given by bungie._

    Tip: Manifest Information
        This model has some attributes which can be filled with additional information found in the manifest (`manifest_...`).
        Without additional work, these attributes will be `None`, since they require additional requests and database lookups.

        To fill the manifest dependent attributes, either:

        - Run `await ThisClass.fetch_manifest_information()`, see [here](/API Reference/Models/base)
        - Set `Client.always_return_manifest_information` to `True`, see [here](/API Reference/client)

    Attributes:
        craftables: A map of craftable item hashes to craftable item state components.
        crafting_root_node_hash: The hash for the root presentation node definition of craftable item categories.
        manifest_crafting_root_node_hash: Manifest information for `crafting_root_node_hash`
    """

    craftables: dict[int, "DestinyCraftableComponent"] = custom_field(
        metadata={"type": """dict[int, DestinyCraftableComponent]"""}
    )
    crafting_root_node_hash: int = custom_field()
    manifest_crafting_root_node_hash: Optional["DestinyPresentationNodeDefinition"] = custom_field(default=None)


@custom_define()
class DestinyCraftableComponent(BaseModel):
    """
    _No description given by bungie._

    None
    Attributes:
        failed_requirement_indexes: If the requirements are not met for crafting this item, these will index into the list of failure strings.
        sockets: Plug item state for the crafting sockets.
        visible: _No description given by bungie._
    """

    failed_requirement_indexes: list[int] = custom_field(metadata={"type": """list[int]"""})
    sockets: list["DestinyCraftableSocketComponent"] = custom_field(
        metadata={"type": """list[DestinyCraftableSocketComponent]"""}
    )
    visible: bool = custom_field()


@custom_define()
class DestinyCraftableSocketComponent(BaseModel):
    """
    _No description given by bungie._

    Tip: Manifest Information
        This model has some attributes which can be filled with additional information found in the manifest (`manifest_...`).
        Without additional work, these attributes will be `None`, since they require additional requests and database lookups.

        To fill the manifest dependent attributes, either:

        - Run `await ThisClass.fetch_manifest_information()`, see [here](/API Reference/Models/base)
        - Set `Client.always_return_manifest_information` to `True`, see [here](/API Reference/client)

    Attributes:
        plug_set_hash: _No description given by bungie._
        plugs: Unlock state for plugs in the socket plug set definition
        manifest_plug_set_hash: Manifest information for `plug_set_hash`
    """

    plug_set_hash: int = custom_field()
    plugs: list["DestinyCraftableSocketPlugComponent"] = custom_field(
        metadata={"type": """list[DestinyCraftableSocketPlugComponent]"""}
    )
    manifest_plug_set_hash: Optional["DestinyPlugSetDefinition"] = custom_field(default=None)


@custom_define()
class DestinyCraftableSocketPlugComponent(BaseModel):
    """
    _No description given by bungie._

    Tip: Manifest Information
        This model has some attributes which can be filled with additional information found in the manifest (`manifest_...`).
        Without additional work, these attributes will be `None`, since they require additional requests and database lookups.

        To fill the manifest dependent attributes, either:

        - Run `await ThisClass.fetch_manifest_information()`, see [here](/API Reference/Models/base)
        - Set `Client.always_return_manifest_information` to `True`, see [here](/API Reference/client)

    Attributes:
        failed_requirement_indexes: Index into the unlock requirements to display failure descriptions
        plug_item_hash: _No description given by bungie._
        manifest_plug_item_hash: Manifest information for `plug_item_hash`
    """

    failed_requirement_indexes: list[int] = custom_field(metadata={"type": """list[int]"""})
    plug_item_hash: int = custom_field()
    manifest_plug_item_hash: Optional["DestinyInventoryItemDefinition"] = custom_field(default=None)
