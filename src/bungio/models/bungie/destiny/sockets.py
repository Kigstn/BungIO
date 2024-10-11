# DO NOT CHANGE ANY CODE BELOW
# This file is generated automatically by `generate_api_schema.py` and will be overwritten
# Instead, change functions / models by subclassing them in the `./overwrites/` folder. They will be used instead.

from typing import TYPE_CHECKING, Optional

from bungio.models.base import BaseModel, custom_define, custom_field

if TYPE_CHECKING:
    from bungio.models import DestinyInventoryItemDefinition, DestinyObjectiveProgress


@custom_define()
class DestinyItemPlugBase(BaseModel):
    """
    _No description given by bungie._

    Tip: Manifest Information
        This model has some attributes which can be filled with additional information found in the manifest (`manifest_...`).
        Without additional work, these attributes will be `None`, since they require additional requests and database lookups.

        To fill the manifest dependent attributes, either:

        - Run `await ThisClass.fetch_manifest_information()`, see [here](/API Reference/Models/base)
        - Set `Client.always_return_manifest_information` to `True`, see [here](/API Reference/client)

    Attributes:
        can_insert: If true, this plug has met all of its insertion requirements. Big if true.
        enable_fail_indexes: If a plug is not enabled, this will be populated with indexes into the plug item definition's plug.enabledRules property, so that you can show the reasons why it is not enabled. This list will be empty if the plug is enabled.
        enabled: If true, this plug will provide its benefits while inserted.
        insert_fail_indexes: If the plug cannot be inserted for some reason, this will have the indexes into the plug item definition's plug.insertionRules property, so you can show the reasons why it can't be inserted. This list will be empty if the plug can be inserted.
        max_stack_size: If available, this is the maximum stack size to display for the socket plug item.
        plug_item_hash: The hash identifier of the DestinyInventoryItemDefinition that represents this plug.
        stack_size: If available, this is the stack size to display for the socket plug item.
        manifest_plug_item_hash: Manifest information for `plug_item_hash`
    """

    can_insert: bool = custom_field()
    enable_fail_indexes: list[int] = custom_field(metadata={"type": """list[int]"""})
    enabled: bool = custom_field()
    insert_fail_indexes: list[int] = custom_field(metadata={"type": """list[int]"""})
    max_stack_size: int = custom_field()
    plug_item_hash: int = custom_field()
    stack_size: int = custom_field()
    manifest_plug_item_hash: Optional["DestinyInventoryItemDefinition"] = custom_field(default=None)


@custom_define()
class DestinyItemPlug(BaseModel):
    """
    _No description given by bungie._

    Tip: Manifest Information
        This model has some attributes which can be filled with additional information found in the manifest (`manifest_...`).
        Without additional work, these attributes will be `None`, since they require additional requests and database lookups.

        To fill the manifest dependent attributes, either:

        - Run `await ThisClass.fetch_manifest_information()`, see [here](/API Reference/Models/base)
        - Set `Client.always_return_manifest_information` to `True`, see [here](/API Reference/client)

    Attributes:
        can_insert: If true, this plug has met all of its insertion requirements. Big if true.
        enable_fail_indexes: If a plug is not enabled, this will be populated with indexes into the plug item definition's plug.enabledRules property, so that you can show the reasons why it is not enabled. This list will be empty if the plug is enabled.
        enabled: If true, this plug will provide its benefits while inserted.
        insert_fail_indexes: If the plug cannot be inserted for some reason, this will have the indexes into the plug item definition's plug.insertionRules property, so you can show the reasons why it can't be inserted. This list will be empty if the plug can be inserted.
        max_stack_size: If available, this is the maximum stack size to display for the socket plug item.
        plug_item_hash: The hash identifier of the DestinyInventoryItemDefinition that represents this plug.
        plug_objectives: Sometimes, Plugs may have objectives: these are often used for flavor and display purposes, but they can be used for any arbitrary purpose (both fortunately and unfortunately). Recently (with Season 2) they were expanded in use to be used as the "gating" for whether the plug can be inserted at all. For instance, a Plug might be tracking the number of PVP kills you have made. It will use the parent item's data about that tracking status to determine what to show, and will generally show it using the DestinyObjectiveDefinition's progressDescription property. Refer to the plug's itemHash and objective property for more information if you would like to display even more data.
        stack_size: If available, this is the stack size to display for the socket plug item.
        manifest_plug_item_hash: Manifest information for `plug_item_hash`
    """

    can_insert: bool = custom_field()
    enable_fail_indexes: list[int] = custom_field(metadata={"type": """list[int]"""})
    enabled: bool = custom_field()
    insert_fail_indexes: list[int] = custom_field(metadata={"type": """list[int]"""})
    max_stack_size: int = custom_field()
    plug_item_hash: int = custom_field()
    plug_objectives: list["DestinyObjectiveProgress"] = custom_field(
        metadata={"type": """list[DestinyObjectiveProgress]"""}
    )
    stack_size: int = custom_field()
    manifest_plug_item_hash: Optional["DestinyInventoryItemDefinition"] = custom_field(default=None)
