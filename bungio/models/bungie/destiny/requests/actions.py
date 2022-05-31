from typing import TYPE_CHECKING

import attr

from bungio.models.base import BaseEnum, BaseModel

if TYPE_CHECKING:
    from bungio.models import DestinyInsertPlugsRequestEntry


@attr.define
class DestinyActionRequest(BaseModel):
    """
    _No description given by bungie_

    Attributes:
        membership_type: _No description given by bungie_
    """

    membership_type: int = attr.field()


@attr.define
class DestinyCharacterActionRequest(BaseModel):
    """
    _No description given by bungie_

    Attributes:
        character_id: _No description given by bungie_
        membership_type: _No description given by bungie_
    """

    character_id: int = attr.field()
    membership_type: int = attr.field()


@attr.define
class DestinyItemActionRequest(BaseModel):
    """
    _No description given by bungie_

    Attributes:
        item_id: The instance ID of the item for this action request.
        character_id: _No description given by bungie_
        membership_type: _No description given by bungie_
    """

    item_id: int = attr.field()
    character_id: int = attr.field()
    membership_type: int = attr.field()


@attr.define
class DestinyPostmasterTransferRequest(BaseModel):
    """
    _No description given by bungie_

    Attributes:
        item_reference_hash: _No description given by bungie_
        stack_size: _No description given by bungie_
        item_id: The instance ID of the item for this action request.
        character_id: _No description given by bungie_
        membership_type: _No description given by bungie_
    """

    item_reference_hash: int = attr.field()
    stack_size: int = attr.field()
    item_id: int = attr.field()
    character_id: int = attr.field()
    membership_type: int = attr.field()


@attr.define
class DestinyItemSetActionRequest(BaseModel):
    """
    _No description given by bungie_

    Attributes:
        item_ids: _No description given by bungie_
        character_id: _No description given by bungie_
        membership_type: _No description given by bungie_
    """

    item_ids: list[int] = attr.field()
    character_id: int = attr.field()
    membership_type: int = attr.field()


@attr.define
class DestinyItemStateRequest(BaseModel):
    """
    _No description given by bungie_

    Attributes:
        state: _No description given by bungie_
        item_id: The instance ID of the item for this action request.
        character_id: _No description given by bungie_
        membership_type: _No description given by bungie_
    """

    state: bool = attr.field()
    item_id: int = attr.field()
    character_id: int = attr.field()
    membership_type: int = attr.field()


@attr.define
class DestinyInsertPlugsActionRequest(BaseModel):
    """
    _No description given by bungie_

    Attributes:
        action_token: Action token provided by the AwaGetActionToken API call.
        item_instance_id: The instance ID of the item having a plug inserted. Only instanced items can have sockets.
        plug: The plugs being inserted.
        character_id: _No description given by bungie_
        membership_type: _No description given by bungie_
    """

    action_token: str = attr.field()
    item_instance_id: int = attr.field()
    plug: "DestinyInsertPlugsRequestEntry" = attr.field()
    character_id: int = attr.field()
    membership_type: int = attr.field()


@attr.define
class DestinyInsertPlugsRequestEntry(BaseModel):
    """
    Represents all of the data related to a single plug to be inserted. Note that, while you *can* point to a socket that represents infusion, you will receive an error if you attempt to do so. Come on guys, let's play nice.

    Attributes:
        socket_index: The index into the socket array, which identifies the specific socket being operated on. We also need to know the socketArrayType in order to uniquely identify the socket. Don't point to or try to insert a plug into an infusion socket. It won't work.
        socket_array_type: This property, combined with the socketIndex, tells us which socket we are referring to (since operations can be performed on both Intrinsic and "default" sockets, and they occupy different arrays in the Inventory Item Definition). I know, I know. Don't give me that look.
        plug_item_hash: Plugs are never instanced (except in infusion). So with the hash alone, we should be able to: 1) Infer whether the player actually needs to have the item, or if it's a reusable plug 2) Perform any operation needed to use the Plug, including removing the plug item and running reward sheets.
    """

    socket_index: int = attr.field()
    socket_array_type: int = attr.field()
    plug_item_hash: int = attr.field()


class DestinySocketArrayType(BaseEnum):
    """
    If you look in the DestinyInventoryItemDefinition's "sockets" property, you'll see that there are two types of sockets: intrinsic, and "socketEntry." Unfortunately, because Intrinsic sockets are a whole separate array, it is no longer sufficient to know the index into that array to know which socket we're talking about. You have to know whether it's in the default "socketEntries" or if it's in the "intrinsic" list.
    """

    DEFAULT = 0
    """_No description given by bungie_ """
    INTRINSIC = 1
    """_No description given by bungie_ """


@attr.define
class DestinyInsertPlugsFreeActionRequest(BaseModel):
    """
    _No description given by bungie_

    Attributes:
        plug: The plugs being inserted.
        item_id: The instance ID of the item for this action request.
        character_id: _No description given by bungie_
        membership_type: _No description given by bungie_
    """

    plug: "DestinyInsertPlugsRequestEntry" = attr.field()
    item_id: int = attr.field()
    character_id: int = attr.field()
    membership_type: int = attr.field()
