import datetime
from typing import TYPE_CHECKING, Any, Optional

import attr

from bungio.models.base import BaseEnum, BaseModel


@attr.define
class BungieFriendListResponse(BaseModel):
    """
    Not specified.

    Attributes:
        friends: Not specified.
    """

    friends: list["BungieFriend"] = attr.field()


@attr.define
class BungieFriend(BaseModel):
    """
    Not specified.

    Attributes:
        last_seen_as_membership_id: Not specified.
        last_seen_as_bungie_membership_type: Not specified.
        bungie_global_display_name: Not specified.
        bungie_global_display_name_code: Not specified.
        online_status: Not specified.
        online_title: Not specified.
        relationship: Not specified.
        bungie_net_user: Not specified.
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
    Not specified.
    """

    OFFLINE_OR_UNKNOWN = 0
    """Not specified. """
    ONLINE = 1
    """Not specified. """


class PresenceOnlineStateFlags(BaseEnum):
    """
    Not specified.
    """

    NONE = 0
    """Not specified. """
    DESTINY1 = 1
    """Not specified. """
    DESTINY2 = 2
    """Not specified. """


class FriendRelationshipState(BaseEnum):
    """
    Not specified.
    """

    UNKNOWN = 0
    """Not specified. """
    FRIEND = 1
    """Not specified. """
    INCOMING_REQUEST = 2
    """Not specified. """
    OUTGOING_REQUEST = 3
    """Not specified. """


@attr.define
class BungieFriendRequestListResponse(BaseModel):
    """
    Not specified.

    Attributes:
        incoming_requests: Not specified.
        outgoing_requests: Not specified.
    """

    incoming_requests: list["BungieFriend"] = attr.field()
    outgoing_requests: list["BungieFriend"] = attr.field()


class PlatformFriendType(BaseEnum):
    """
    Not specified.
    """

    UNKNOWN = 0
    """Not specified. """
    XBOX = 1
    """Not specified. """
    P_S_N = 2
    """Not specified. """
    STEAM = 3
    """Not specified. """


@attr.define
class PlatformFriendResponse(BaseModel):
    """
    Not specified.

    Attributes:
        items_per_page: Not specified.
        current_page: Not specified.
        has_more: Not specified.
        platform_friends: Not specified.
    """

    items_per_page: int = attr.field()
    current_page: int = attr.field()
    has_more: bool = attr.field()
    platform_friends: list["PlatformFriend"] = attr.field()


@attr.define
class PlatformFriend(BaseModel):
    """
    Not specified.

    Attributes:
        platform_display_name: Not specified.
        friend_platform: Not specified.
        destiny_membership_id: Not specified.
        destiny_membership_type: Not specified.
        bungie_net_membership_id: Not specified.
        bungie_global_display_name: Not specified.
        bungie_global_display_name_code: Not specified.
    """

    platform_display_name: str = attr.field()
    friend_platform: int = attr.field()
    destiny_membership_id: int = attr.field()
    destiny_membership_type: int = attr.field()
    bungie_net_membership_id: int = attr.field()
    bungie_global_display_name: str = attr.field()
    bungie_global_display_name_code: int = attr.field()
