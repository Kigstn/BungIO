# DO NOT CHANGE ANY CODE BELOW
# This file is generated automatically by `generate_api_schema.py` and will be overwritten
# Instead, change functions / models by subclassing them in the `./overwrites/` folder. They will be used instead.

from typing import TYPE_CHECKING, Optional, Union

import attr

from bungio.models.base import BaseModel, ManifestModel
from bungio.utils import enum_converter

if TYPE_CHECKING:
    from bungio.models import (
        DestinyDisplayPropertiesDefinition,
        DestinyInventoryItemDefinition,
        DestinyItemSocketEntryPlugItemRandomizedDefinition,
        DestinySocketCategoryStyle,
        DestinySocketVisibility,
        SocketTypeActionType,
    )


@attr.define
class DestinySocketTypeDefinition(ManifestModel):
    """
    All Sockets have a "Type": a set of common properties that determine when the socket allows Plugs to be inserted, what Categories of Plugs can be inserted, and whether the socket is even visible at all given the current game/character/account state. See DestinyInventoryItemDefinition for more information about Socketed items and Plugs.

    Tip: Manifest Information
        This model has some attributes which can be filled with additional information found in the manifest (`manifest_...`).
        Without additional work, these attributes will be `None`, since they require additional requests and database lookups.

        To fill the manifest dependent attributes, either:

        - Run `await ThisClass.fetch_manifest_information()`, see [here](/API Reference/Models/base)
        - Set `Client.always_return_manifest_information` to `True`, see [here](/API Reference/client)

    Attributes:
        always_randomize_sockets: _No description given by bungie._
        avoid_duplicates_on_initialization: _No description given by bungie._
        currency_scalars: _No description given by bungie._
        display_properties: There are fields for this display data, but they appear to be unpopulated as of now. I am not sure where in the UI these would show if they even were populated, but I will continue to return this data in case it becomes useful.
        hash: The unique identifier for this entity. Guaranteed to be unique for the type of entity, but not globally. When entities refer to each other in Destiny content, it is this hash that they are referring to.
        hide_duplicate_reusable_plugs: _No description given by bungie._
        index: The index of the entity as it was found in the investment tables.
        insert_action: Defines what happens when a plug is inserted into sockets of this type.
        is_preview_enabled: _No description given by bungie._
        overrides_ui_appearance: This property indicates if the socket type determines whether Emblem icons and nameplates should be overridden by the inserted plug item's icon and nameplate.
        plug_whitelist: A list of Plug "Categories" that are allowed to be plugged into sockets of this type. These should be compared against a given plug item's DestinyInventoryItemDefinition.plug.plugCategoryHash, which indicates the plug item's category. If the plug's category matches any whitelisted plug, or if the whitelist is empty, it is allowed to be inserted.
        redacted: If this is true, then there is an entity with this identifier/type combination, but BNet is not yet allowed to show it. Sorry!
        socket_category_hash: _No description given by bungie._
        visibility: Sometimes a socket isn't visible. These are some of the conditions under which sockets of this type are not visible. Unfortunately, the truth of visibility is much, much more complex. Best to rely on the live data for whether the socket is visible and enabled.
        manifest_socket_category_hash: Manifest information for `socket_category_hash`
    """

    always_randomize_sockets: bool = attr.field()
    avoid_duplicates_on_initialization: bool = attr.field()
    currency_scalars: list["DestinySocketTypeScalarMaterialRequirementEntry"] = attr.field(
        metadata={"type": """list[DestinySocketTypeScalarMaterialRequirementEntry]"""}
    )
    display_properties: "DestinyDisplayPropertiesDefinition" = attr.field()
    hash: int = attr.field()
    hide_duplicate_reusable_plugs: bool = attr.field()
    index: int = attr.field()
    insert_action: "DestinyInsertPlugActionDefinition" = attr.field()
    is_preview_enabled: bool = attr.field()
    overrides_ui_appearance: bool = attr.field()
    plug_whitelist: list["DestinyPlugWhitelistEntryDefinition"] = attr.field(
        metadata={"type": """list[DestinyPlugWhitelistEntryDefinition]"""}
    )
    redacted: bool = attr.field()
    socket_category_hash: int = attr.field()
    visibility: Union["DestinySocketVisibility", int] = attr.field(converter=enum_converter("DestinySocketVisibility"))
    manifest_socket_category_hash: Optional["DestinySocketCategoryDefinition"] = attr.field(default=None)


@attr.define
class DestinyInsertPlugActionDefinition(BaseModel):
    """
    Data related to what happens while a plug is being inserted, mostly for UI purposes.

    None
    Attributes:
        action_execute_seconds: How long it takes for the Plugging of the item to be completed once it is initiated, if you care.
        action_type: The type of action being performed when you act on this Socket Type. The most common value is "insert plug", but there are others as well (for instance, a "Masterwork" socket may allow for Re-initialization, and an Infusion socket allows for items to be consumed to upgrade the item)
    """

    action_execute_seconds: int = attr.field()
    action_type: Union["SocketTypeActionType", int] = attr.field(converter=enum_converter("SocketTypeActionType"))


@attr.define
class DestinyPlugWhitelistEntryDefinition(BaseModel):
    """
    Defines a plug "Category" that is allowed to be plugged into a socket of this type. This should be compared against a given plug item's DestinyInventoryItemDefinition.plug.plugCategoryHash, which indicates the plug item's category.

    None
    Attributes:
        category_hash: The hash identifier of the Plug Category to compare against the plug item's plug.plugCategoryHash. Note that this does NOT relate to any Definition in itself, it is only used for comparison purposes.
        category_identifier: The string identifier for the category, which is here mostly for debug purposes.
        reinitialization_possible_plug_hashes: The list of all plug items (DestinyInventoryItemDefinition) that the socket may randomly be populated with when reinitialized. Which ones you should actually show are determined by the plug being inserted into the socket, and the socket’s type. When you inspect the plug that could go into a Masterwork Socket, look up the socket type of the socket being inspected and find the DestinySocketTypeDefinition. Then, look at the Plugs that can fit in that socket. Find the Whitelist in the DestinySocketTypeDefinition that matches the plug item’s categoryhash. That whitelist entry will potentially have a new “reinitializationPossiblePlugHashes” property.If it does, that means we know what it will roll if you try to insert this plug into this socket.
    """

    category_hash: int = attr.field()
    category_identifier: str = attr.field()
    reinitialization_possible_plug_hashes: list[int] = attr.field(metadata={"type": """list[int]"""})


@attr.define
class DestinySocketTypeScalarMaterialRequirementEntry(BaseModel):
    """
    _No description given by bungie._

    Tip: Manifest Information
        This model has some attributes which can be filled with additional information found in the manifest (`manifest_...`).
        Without additional work, these attributes will be `None`, since they require additional requests and database lookups.

        To fill the manifest dependent attributes, either:

        - Run `await ThisClass.fetch_manifest_information()`, see [here](/API Reference/Models/base)
        - Set `Client.always_return_manifest_information` to `True`, see [here](/API Reference/client)

    Attributes:
        currency_item_hash: _No description given by bungie._
        scalar_value: _No description given by bungie._
        manifest_currency_item_hash: Manifest information for `currency_item_hash`
    """

    currency_item_hash: int = attr.field()
    scalar_value: int = attr.field()
    manifest_currency_item_hash: Optional["DestinyInventoryItemDefinition"] = attr.field(default=None)


@attr.define
class DestinySocketCategoryDefinition(ManifestModel):
    """
    Sockets on an item are organized into Categories visually. You can find references to the socket category defined on an item's DestinyInventoryItemDefinition.sockets.socketCategories property. This has the display information for rendering the categories' header, and a hint for how the UI should handle showing this category. The shitty thing about this, however, is that the socket categories' UI style can be overridden by the item's UI style. For instance, the Socket Category used by Emote Sockets says it's "consumable," but that's a lie: they're all reusable, and overridden by the detail UI pages in ways that we can't easily account for in the API. As a result, I will try to compile these rules into the individual sockets on items, and provide the best hint possible there through the plugSources property. In the future, I may attempt to use this information in conjunction with the item to provide a more usable UI hint on the socket layer, but for now improving the consistency of plugSources is the best I have time to provide. (See https://github.com/Bungie-net/api/issues/522 for more info)

    None
    Attributes:
        category_style: Same as uiCategoryStyle, but in a more usable enumeration form.
        display_properties: _No description given by bungie._
        hash: The unique identifier for this entity. Guaranteed to be unique for the type of entity, but not globally. When entities refer to each other in Destiny content, it is this hash that they are referring to.
        index: The index of the entity as it was found in the investment tables.
        redacted: If this is true, then there is an entity with this identifier/type combination, but BNet is not yet allowed to show it. Sorry!
        ui_category_style: A string hinting to the game's UI system about how the sockets in this category should be displayed. BNet doesn't use it: it's up to you to find valid values and make your own special UI if you want to honor this category style.
    """

    category_style: Union["DestinySocketCategoryStyle", int] = attr.field(
        converter=enum_converter("DestinySocketCategoryStyle")
    )
    display_properties: "DestinyDisplayPropertiesDefinition" = attr.field()
    hash: int = attr.field()
    index: int = attr.field()
    redacted: bool = attr.field()
    ui_category_style: int = attr.field()


@attr.define
class DestinyPlugSetDefinition(ManifestModel):
    """
    Sometimes, we have large sets of reusable plugs that are defined identically and thus can (and in some cases, are so large that they *must*) be shared across the places where they are used. These are the definitions for those reusable sets of plugs.   See DestinyItemSocketEntryDefinition.plugSource and reusablePlugSetHash for the relationship between these reusable plug sets and the sockets that leverage them (for starters, Emotes).  As of the release of Shadowkeep (Late 2019), these will begin to be sourced from game content directly - which means there will be many more of them, but it also means we may not get all data that we used to get for them.  DisplayProperties, in particular, will no longer be guaranteed to contain valid information. We will make a best effort to guess what ought to be populated there where possible, but it will be invalid for many/most plug sets.

    None
    Attributes:
        display_properties: If you want to show these plugs in isolation, these are the display properties for them.
        hash: The unique identifier for this entity. Guaranteed to be unique for the type of entity, but not globally. When entities refer to each other in Destiny content, it is this hash that they are referring to.
        index: The index of the entity as it was found in the investment tables.
        is_fake_plug_set: Mostly for our debugging or reporting bugs, BNet is making "fake" plug sets in a desperate effort to reduce socket sizes.  If this is true, the plug set was generated by BNet: if it looks wrong, that's a good indicator that it's bungie.net that fucked this up.
        redacted: If this is true, then there is an entity with this identifier/type combination, but BNet is not yet allowed to show it. Sorry!
        reusable_plug_items: This is a list of pre-determined plugs that can be plugged into this socket, without the character having the plug in their inventory. If this list is populated, you will not be allowed to plug an arbitrary item in the socket: you will only be able to choose from one of these reusable plugs.
    """

    display_properties: "DestinyDisplayPropertiesDefinition" = attr.field()
    hash: int = attr.field()
    index: int = attr.field()
    is_fake_plug_set: bool = attr.field()
    redacted: bool = attr.field()
    reusable_plug_items: list["DestinyItemSocketEntryPlugItemRandomizedDefinition"] = attr.field(
        metadata={"type": """list[DestinyItemSocketEntryPlugItemRandomizedDefinition]"""}
    )
