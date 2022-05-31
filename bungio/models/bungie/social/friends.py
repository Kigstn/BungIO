from typing import TYPE_CHECKING

import attr

from bungio.models.base import BaseEnum, BaseModel

if TYPE_CHECKING:
    from bungio.models import BungieFriend, GeneralUser, PlatformFriend


@attr.define
class BungieFriendListResponse(BaseModel):
    """
    _No description given_

    Attributes:
        friends: _No description given_
    """

    friends: list["BungieFriend"] = attr.field()


@attr.define
class BungieFriend(BaseModel):
    """
    _No description given_

    Attributes:
        last_seen_as_membership_id: _No description given_
        last_seen_as_bungie_membership_type: _No description given_
        bungie_global_display_name: _No description given_
        bungie_global_display_name_code: _No description given_
        online_status: _No description given_
        online_title: _No description given_
        relationship: _No description given_
        bungie_net_user: _No description given_
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
    _No description given_
    """

    OFFLINE_OR_UNKNOWN = 0
    """_No description given_ """
    ONLINE = 1
    """_No description given_ """


class PresenceOnlineStateFlags(BaseEnum):
    """
    _No description given_
    """

    NONE = 0
    """_No description given_ """
    DESTINY1 = 1
    """_No description given_ """
    DESTINY2 = 2
    """_No description given_ """


class FriendRelationshipState(BaseEnum):
    """
    _No description given_
    """

    UNKNOWN = 0
    """_No description given_ """
    FRIEND = 1
    """_No description given_ """
    INCOMING_REQUEST = 2
    """_No description given_ """
    OUTGOING_REQUEST = 3
    """_No description given_ """


@attr.define
class BungieFriendRequestListResponse(BaseModel):
    """
    _No description given_

    Attributes:
        incoming_requests: _No description given_
        outgoing_requests: _No description given_
    """

    incoming_requests: list["BungieFriend"] = attr.field()
    outgoing_requests: list["BungieFriend"] = attr.field()


class PlatformFriendType(BaseEnum):
    """
    _No description given_
    """

    UNKNOWN = 0
    """_No description given_ """
    XBOX = 1
    """_No description given_ """
    P_S_N = 2
    """_No description given_ """
    STEAM = 3
    """_No description given_ """


@attr.define
class PlatformFriendResponse(BaseModel):
    """
    _No description given_

    Attributes:
        items_per_page: _No description given_
        current_page: _No description given_
        has_more: _No description given_
        platform_friends: _No description given_
    """

    items_per_page: int = attr.field()
    current_page: int = attr.field()
    has_more: bool = attr.field()
    platform_friends: list["PlatformFriend"] = attr.field()


@attr.define
class PlatformFriend(BaseModel):
    """
    _No description given_

    Attributes:
        platform_display_name: _No description given_
        friend_platform: _No description given_
        destiny_membership_id: _No description given_
        destiny_membership_type: _No description given_
        bungie_net_membership_id: _No description given_
        bungie_global_display_name: _No description given_
        bungie_global_display_name_code: _No description given_
    """

    platform_display_name: str = attr.field()
    friend_platform: int = attr.field()
    destiny_membership_id: int = attr.field()
    destiny_membership_type: int = attr.field()
    bungie_net_membership_id: int = attr.field()
    bungie_global_display_name: str = attr.field()
    bungie_global_display_name_code: int = attr.field()
