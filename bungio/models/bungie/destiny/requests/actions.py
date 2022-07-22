# DO NOT CHANGE ANY CODE BELOW
# This file is generated automatically by `generate_api_schema.py` and will be overwritten
# Instead, change functions / models by subclassing them in the `./overwrites/` folder. They will be used instead.

from typing import TYPE_CHECKING, Optional, Union

import attr

from bungio.models.base import BaseEnum, BaseModel
from bungio.utils import enum_converter

if TYPE_CHECKING:
    from bungio.models import BungieMembershipType, DestinyInventoryItemDefinition


@attr.define
class DestinyActionRequest(BaseModel):
    """
    _No description given by bungie._

    None
    Attributes:
        membership_type: _No description given by bungie._
    """

    membership_type: Union["BungieMembershipType", int] = attr.field(converter=enum_converter("BungieMembershipType"))


@attr.define
class DestinyCharacterActionRequest(BaseModel):
    """
    _No description given by bungie._

    None
    Attributes:
        character_id: _No description given by bungie._
        membership_type: _No description given by bungie._
    """

    character_id: int = attr.field()
    membership_type: Union["BungieMembershipType", int] = attr.field(converter=enum_converter("BungieMembershipType"))


@attr.define
class DestinyItemActionRequest(BaseModel):
    """
    _No description given by bungie._

    None
    Attributes:
        character_id: _No description given by bungie._
        item_id: The instance ID of the item for this action request.
        membership_type: _No description given by bungie._
    """

    character_id: int = attr.field()
    item_id: int = attr.field()
    membership_type: Union["BungieMembershipType", int] = attr.field(converter=enum_converter("BungieMembershipType"))


@attr.define
class DestinyPostmasterTransferRequest(BaseModel):
    """
    _No description given by bungie._

    Tip: Manifest Information
        This model has some attributes which can be filled with additional information found in the manifest (`manifest_...`).
        Without additional work, these attributes will be `None`, since they require additional requests and database lookups.

        To fill the manifest dependent attributes, either:

        - Run `await ThisClass.fetch_manifest_information()`, see [here](/API Reference/Models/base)
        - Set `Client.always_return_manifest_information` to `True`, see [here](/API Reference/client)

    Attributes:
        character_id: _No description given by bungie._
        item_id: The instance ID of the item for this action request.
        item_reference_hash: _No description given by bungie._
        membership_type: _No description given by bungie._
        stack_size: _No description given by bungie._
        manifest_item_reference_hash: Manifest information for `item_reference_hash`
    """

    character_id: int = attr.field()
    item_id: int = attr.field()
    item_reference_hash: int = attr.field()
    membership_type: Union["BungieMembershipType", int] = attr.field(converter=enum_converter("BungieMembershipType"))
    stack_size: int = attr.field()
    manifest_item_reference_hash: Optional["DestinyInventoryItemDefinition"] = attr.field(default=None)


@attr.define
class DestinyItemSetActionRequest(BaseModel):
    """
    _No description given by bungie._

    None
    Attributes:
        character_id: _No description given by bungie._
        item_ids: _No description given by bungie._
        membership_type: _No description given by bungie._
    """

    character_id: int = attr.field()
    item_ids: list[int] = attr.field(metadata={"type": """list[int]"""})
    membership_type: Union["BungieMembershipType", int] = attr.field(converter=enum_converter("BungieMembershipType"))


@attr.define
class DestinyItemStateRequest(BaseModel):
    """
    _No description given by bungie._

    None
    Attributes:
        character_id: _No description given by bungie._
        item_id: The instance ID of the item for this action request.
        membership_type: _No description given by bungie._
        state: _No description given by bungie._
    """

    character_id: int = attr.field()
    item_id: int = attr.field()
    membership_type: Union["BungieMembershipType", int] = attr.field(converter=enum_converter("BungieMembershipType"))
    state: bool = attr.field()


@attr.define
class DestinyInsertPlugsActionRequest(BaseModel):
    """
    _No description given by bungie._

    None
    Attributes:
        action_token: Action token provided by the AwaGetActionToken API call.
        character_id: _No description given by bungie._
        item_instance_id: The instance ID of the item having a plug inserted. Only instanced items can have sockets.
        membership_type: _No description given by bungie._
        plug: The plugs being inserted.
    """

    action_token: str = attr.field()
    character_id: int = attr.field()
    item_instance_id: int = attr.field()
    membership_type: Union["BungieMembershipType", int] = attr.field(converter=enum_converter("BungieMembershipType"))
    plug: "DestinyInsertPlugsRequestEntry" = attr.field()


@attr.define
class DestinyInsertPlugsRequestEntry(BaseModel):
    """
    Represents all of the data related to a single plug to be inserted. Note that, while you *can* point to a socket that represents infusion, you will receive an error if you attempt to do so. Come on guys, let's play nice.

    None
    Attributes:
        plug_item_hash: Plugs are never instanced (except in infusion). So with the hash alone, we should be able to: 1) Infer whether the player actually needs to have the item, or if it's a reusable plug 2) Perform any operation needed to use the Plug, including removing the plug item and running reward sheets.
        socket_array_type: This property, combined with the socketIndex, tells us which socket we are referring to (since operations can be performed on both Intrinsic and "default" sockets, and they occupy different arrays in the Inventory Item Definition). I know, I know. Don't give me that look.
        socket_index: The index into the socket array, which identifies the specific socket being operated on. We also need to know the socketArrayType in order to uniquely identify the socket. Don't point to or try to insert a plug into an infusion socket. It won't work.
    """

    plug_item_hash: int = attr.field()
    socket_array_type: Union["DestinySocketArrayType", int] = attr.field(
        converter=enum_converter("DestinySocketArrayType")
    )
    socket_index: int = attr.field()


class DestinySocketArrayType(BaseEnum):
    """
    If you look in the DestinyInventoryItemDefinition's "sockets" property, you'll see that there are two types of sockets: intrinsic, and "socketEntry." Unfortunately, because Intrinsic sockets are a whole separate array, it is no longer sufficient to know the index into that array to know which socket we're talking about. You have to know whether it's in the default "socketEntries" or if it's in the "intrinsic" list.
    """

    DEFAULT = 0
    """_No description given by bungie._ """
    INTRINSIC = 1
    """_No description given by bungie._ """


@attr.define
class DestinyInsertPlugsFreeActionRequest(BaseModel):
    """
    _No description given by bungie._

    None
    Attributes:
        character_id: _No description given by bungie._
        item_id: The instance ID of the item for this action request.
        membership_type: _No description given by bungie._
        plug: The plugs being inserted.
    """

    character_id: int = attr.field()
    item_id: int = attr.field()
    membership_type: Union["BungieMembershipType", int] = attr.field(converter=enum_converter("BungieMembershipType"))
    plug: "DestinyInsertPlugsRequestEntry" = attr.field()
