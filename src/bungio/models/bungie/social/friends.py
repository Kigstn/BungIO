# DO NOT CHANGE ANY CODE BELOW
# This file is generated automatically by `generate_api_schema.py` and will be overwritten
# Instead, change functions / models by subclassing them in the `./overwrites/` folder. They will be used instead.

from typing import Union, TYPE_CHECKING

from bungio.utils import enum_converter
from bungio.models.base import BaseModel, BaseEnum, BaseFlagEnum, custom_define, custom_field

from bungio.models.mixins import DestinyUserMixin

if TYPE_CHECKING:
    from bungio.models import GeneralUser
    from bungio.models import BungieMembershipType


@custom_define()
class BungieFriendListResponse(BaseModel):
    """
    _No description given by bungie._

    None
    Attributes:
        friends: _No description given by bungie._
    """

    friends: list["BungieFriend"] = custom_field(metadata={"type": """list[BungieFriend]"""})


@custom_define()
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

    bungie_global_display_name: str = custom_field()
    bungie_global_display_name_code: int = custom_field()
    bungie_net_user: "GeneralUser" = custom_field()
    last_seen_as_bungie_membership_type: Union["BungieMembershipType", int] = custom_field(
        converter=enum_converter("BungieMembershipType")
    )
    last_seen_as_membership_id: int = custom_field(metadata={"int64": True})
    online_status: Union["PresenceStatus", int] = custom_field(converter=enum_converter("PresenceStatus"))
    online_title: Union["PresenceOnlineStateFlags", int] = custom_field(
        converter=enum_converter("PresenceOnlineStateFlags")
    )
    relationship: Union["FriendRelationshipState", int] = custom_field(
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


@custom_define()
class BungieFriendRequestListResponse(BaseModel):
    """
    _No description given by bungie._

    None
    Attributes:
        incoming_requests: _No description given by bungie._
        outgoing_requests: _No description given by bungie._
    """

    incoming_requests: list["BungieFriend"] = custom_field(metadata={"type": """list[BungieFriend]"""})
    outgoing_requests: list["BungieFriend"] = custom_field(metadata={"type": """list[BungieFriend]"""})


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
    EGS = 4
    """_No description given by bungie._ """


@custom_define()
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

    current_page: int = custom_field()
    has_more: bool = custom_field()
    items_per_page: int = custom_field()
    platform_friends: list["PlatformFriend"] = custom_field(metadata={"type": """list[PlatformFriend]"""})


@custom_define()
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

    bungie_global_display_name: str = custom_field()
    bungie_global_display_name_code: int = custom_field()
    bungie_net_membership_id: int = custom_field(metadata={"int64": True})
    destiny_membership_id: int = custom_field(metadata={"int64": True})
    destiny_membership_type: int = custom_field()
    friend_platform: Union["PlatformFriendType", int] = custom_field(converter=enum_converter("PlatformFriendType"))
    platform_display_name: str = custom_field()
