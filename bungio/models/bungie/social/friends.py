from typing import TYPE_CHECKING

import attr

from bungio.models.base import BaseEnum, BaseModel

if TYPE_CHECKING:
    from bungio.models import BungieFriend, GeneralUser, PlatformFriend


@attr.define
class BungieFriendListResponse(BaseModel):
    """
    _No description given by bungie_

    Attributes:
        friends: _No description given by bungie_
    """

    friends: list["BungieFriend"] = attr.field()


@attr.define
class BungieFriend(BaseModel):
    """
    _No description given by bungie_

    Attributes:
        last_seen_as_membership_id: _No description given by bungie_
        last_seen_as_bungie_membership_type: _No description given by bungie_
        bungie_global_display_name: _No description given by bungie_
        bungie_global_display_name_code: _No description given by bungie_
        online_status: _No description given by bungie_
        online_title: _No description given by bungie_
        relationship: _No description given by bungie_
        bungie_net_user: _No description given by bungie_
    """

    last_seen_as_membership_id: int = attr.field()
    last_seen_as_bungie_membership_type: int = attr.field()
    bungie_global_display_name: str = attr.field()
    bungie_global_display_name_code: int = attr.field()
    online_status: int = attr.field()
    online_title: int = attr.field()
    relationship: int = attr.field()
    bungie_net_user: "GeneralUser" = attr.field()


class PresenceStatus(BaseEnum):
    """
    _No description given by bungie_
    """

    OFFLINE_OR_UNKNOWN = 0
    """_No description given by bungie_ """
    ONLINE = 1
    """_No description given by bungie_ """


class PresenceOnlineStateFlags(BaseEnum):
    """
    _No description given by bungie_
    """

    NONE = 0
    """_No description given by bungie_ """
    DESTINY1 = 1
    """_No description given by bungie_ """
    DESTINY2 = 2
    """_No description given by bungie_ """


class FriendRelationshipState(BaseEnum):
    """
    _No description given by bungie_
    """

    UNKNOWN = 0
    """_No description given by bungie_ """
    FRIEND = 1
    """_No description given by bungie_ """
    INCOMING_REQUEST = 2
    """_No description given by bungie_ """
    OUTGOING_REQUEST = 3
    """_No description given by bungie_ """


@attr.define
class BungieFriendRequestListResponse(BaseModel):
    """
    _No description given by bungie_

    Attributes:
        incoming_requests: _No description given by bungie_
        outgoing_requests: _No description given by bungie_
    """

    incoming_requests: list["BungieFriend"] = attr.field()
    outgoing_requests: list["BungieFriend"] = attr.field()


class PlatformFriendType(BaseEnum):
    """
    _No description given by bungie_
    """

    UNKNOWN = 0
    """_No description given by bungie_ """
    XBOX = 1
    """_No description given by bungie_ """
    P_S_N = 2
    """_No description given by bungie_ """
    STEAM = 3
    """_No description given by bungie_ """


@attr.define
class PlatformFriendResponse(BaseModel):
    """
    _No description given by bungie_

    Attributes:
        items_per_page: _No description given by bungie_
        current_page: _No description given by bungie_
        has_more: _No description given by bungie_
        platform_friends: _No description given by bungie_
    """

    items_per_page: int = attr.field()
    current_page: int = attr.field()
    has_more: bool = attr.field()
    platform_friends: list["PlatformFriend"] = attr.field()


@attr.define
class PlatformFriend(BaseModel):
    """
    _No description given by bungie_

    Attributes:
        platform_display_name: _No description given by bungie_
        friend_platform: _No description given by bungie_
        destiny_membership_id: _No description given by bungie_
        destiny_membership_type: _No description given by bungie_
        bungie_net_membership_id: _No description given by bungie_
        bungie_global_display_name: _No description given by bungie_
        bungie_global_display_name_code: _No description given by bungie_
    """

    platform_display_name: str = attr.field()
    friend_platform: int = attr.field()
    destiny_membership_id: int = attr.field()
    destiny_membership_type: int = attr.field()
    bungie_net_membership_id: int = attr.field()
    bungie_global_display_name: str = attr.field()
    bungie_global_display_name_code: int = attr.field()
