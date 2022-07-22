# DO NOT CHANGE ANY CODE BELOW
# This file is generated automatically by `generate_api_schema.py` and will be overwritten
# Instead, change functions / models by subclassing them in the `./overwrites/` folder. They will be used instead.

from typing import TYPE_CHECKING, Union

import attr

from bungio.models.base import BaseEnum, BaseFlagEnum, BaseModel
from bungio.models.mixins import DestinyUserMixin
from bungio.utils import enum_converter

if TYPE_CHECKING:
    from bungio.models import BungieMembershipType, GeneralUser


@attr.define
class BungieFriendListResponse(BaseModel):
    """
    _No description given by bungie._

    None
    Attributes:
        friends: _No description given by bungie._
    """

    friends: list["BungieFriend"] = attr.field(metadata={"type": """list[BungieFriend]"""})


@attr.define
class BungieFriend(BaseModel, DestinyUserMixin):
    """
    _No description given by bungie._

    None
    Attributes:
        bungie_global_display_name: _No description given by bungie._
        bungie_global_display_name_code: _No description given by bungie._
        bungie_net_user: _No description given by bungie._
        last_seen_as_bungie_membership_type: _No description given by bungie._
        last_seen_as_membership_id: _No description given by bungie._
        online_status: _No description given by bungie._
        online_title: _No description given by bungie._
        relationship: _No description given by bungie._
    """

    bungie_global_display_name: str = attr.field()
    bungie_global_display_name_code: int = attr.field()
    bungie_net_user: "GeneralUser" = attr.field()
    last_seen_as_bungie_membership_type: Union["BungieMembershipType", int] = attr.field(
        converter=enum_converter("BungieMembershipType")
    )
    last_seen_as_membership_id: int = attr.field()
    online_status: Union["PresenceStatus", int] = attr.field(converter=enum_converter("PresenceStatus"))
    online_title: Union["PresenceOnlineStateFlags", int] = attr.field(
        converter=enum_converter("PresenceOnlineStateFlags")
    )
    relationship: Union["FriendRelationshipState", int] = attr.field(
        converter=enum_converter("FriendRelationshipState")
    )


class PresenceStatus(BaseEnum):
    """
    _No description given by bungie._
    """

    OFFLINE_OR_UNKNOWN = 0
    """_No description given by bungie._ """
    ONLINE = 1
    """_No description given by bungie._ """


class PresenceOnlineStateFlags(BaseFlagEnum):
    """
    _No description given by bungie._
    """

    NONE = 0
    """_No description given by bungie._ """
    DESTINY1 = 1
    """_No description given by bungie._ """
    DESTINY2 = 2
    """_No description given by bungie._ """


class FriendRelationshipState(BaseEnum):
    """
    _No description given by bungie._
    """

    UNKNOWN = 0
    """_No description given by bungie._ """
    FRIEND = 1
    """_No description given by bungie._ """
    INCOMING_REQUEST = 2
    """_No description given by bungie._ """
    OUTGOING_REQUEST = 3
    """_No description given by bungie._ """


@attr.define
class BungieFriendRequestListResponse(BaseModel):
    """
    _No description given by bungie._

    None
    Attributes:
        incoming_requests: _No description given by bungie._
        outgoing_requests: _No description given by bungie._
    """

    incoming_requests: list["BungieFriend"] = attr.field(metadata={"type": """list[BungieFriend]"""})
    outgoing_requests: list["BungieFriend"] = attr.field(metadata={"type": """list[BungieFriend]"""})


class PlatformFriendType(BaseEnum):
    """
    _No description given by bungie._
    """

    UNKNOWN = 0
    """_No description given by bungie._ """
    XBOX = 1
    """_No description given by bungie._ """
    P_S_N = 2
    """_No description given by bungie._ """
    STEAM = 3
    """_No description given by bungie._ """


@attr.define
class PlatformFriendResponse(BaseModel):
    """
    _No description given by bungie._

    None
    Attributes:
        current_page: _No description given by bungie._
        has_more: _No description given by bungie._
        items_per_page: _No description given by bungie._
        platform_friends: _No description given by bungie._
    """

    current_page: int = attr.field()
    has_more: bool = attr.field()
    items_per_page: int = attr.field()
    platform_friends: list["PlatformFriend"] = attr.field(metadata={"type": """list[PlatformFriend]"""})


@attr.define
class PlatformFriend(BaseModel, DestinyUserMixin):
    """
    _No description given by bungie._

    None
    Attributes:
        bungie_global_display_name: _No description given by bungie._
        bungie_global_display_name_code: _No description given by bungie._
        bungie_net_membership_id: _No description given by bungie._
        destiny_membership_id: _No description given by bungie._
        destiny_membership_type: _No description given by bungie._
        friend_platform: _No description given by bungie._
        platform_display_name: _No description given by bungie._
    """

    bungie_global_display_name: str = attr.field()
    bungie_global_display_name_code: int = attr.field()
    bungie_net_membership_id: int = attr.field()
    destiny_membership_id: int = attr.field()
    destiny_membership_type: int = attr.field()
    friend_platform: Union["PlatformFriendType", int] = attr.field(converter=enum_converter("PlatformFriendType"))
    platform_display_name: str = attr.field()
