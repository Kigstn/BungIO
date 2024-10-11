# DO NOT CHANGE ANY CODE BELOW
# This file is generated automatically by `generate_api_schema.py` and will be overwritten
# Instead, change functions / models by subclassing them in the `./overwrites/` folder. They will be used instead.

from typing import TYPE_CHECKING, Optional

from bungio.models.base import BaseModel, custom_define, custom_field

if TYPE_CHECKING:
    from bungio.models import DestinyInventoryItemDefinition, DestinyItemPlugBase, DestinyObjectiveProgress


@custom_define()
class DestinyItemReusablePlugsComponent(BaseModel):
    """
    _No description given by bungie._

    None
    Attributes:
        plugs: If the item supports reusable plugs, this is the list of plugs that are allowed to be used for the socket, and any relevant information about whether they are "enabled", whether they are allowed to be inserted, and any other information such as objectives.  A Reusable Plug is a plug that you can always insert into this socket as long as its insertion rules are passed, regardless of whether or not you have the plug in your inventory. An example of it failing an insertion rule would be if it has an Objective that needs to be completed before it can be inserted, and that objective hasn't been completed yet.  In practice, a socket will *either* have reusable plugs *or* it will allow for plugs in your inventory to be inserted. See DestinyInventoryItemDefinition.socket for more info.  KEY = The INDEX into the item's list of sockets. VALUE = The set of plugs for that socket.  If a socket doesn't have any reusable plugs defined at the item scope, there will be no entry for that socket.
    """

    plugs: dict[int, list["DestinyItemPlugBase"]] = custom_field(
        metadata={"type": """dict[int, list[DestinyItemPlugBase]]"""}
    )


@custom_define()
class DestinyItemPlugObjectivesComponent(BaseModel):
    """
    _No description given by bungie._

    None
    Attributes:
        objectives_per_plug: This set of data is keyed by the Item Hash (DestinyInventoryItemDefinition) of the plug whose objectives are being returned, with the value being the list of those objectives.  What if two plugs with the same hash are returned for an item, you ask?  Good question! They share the same item-scoped state, and as such would have identical objective state as a result. How's that for convenient.  Sometimes, Plugs may have objectives: generally, these are used for flavor and display purposes. For instance, a Plug might be tracking the number of PVP kills you have made. It will use the parent item's data about that tracking status to determine what to show, and will generally show it using the DestinyObjectiveDefinition's progressDescription property. Refer to the plug's itemHash and objective property for more information if you would like to display even more data.
    """

    objectives_per_plug: dict[int, list["DestinyObjectiveProgress"]] = custom_field(
        metadata={"type": """dict[int, list[DestinyObjectiveProgress]]"""}
    )


@custom_define()
class DestinyItemPlugComponent(BaseModel):
    """
    Plugs are non-instanced items that can provide Stat and Perk benefits when socketed into an instanced item. Items have Sockets, and Plugs are inserted into Sockets. This component finds all items that are considered "Plugs" in your inventory, and return information about the plug aside from any specific Socket into which it could be inserted.

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
