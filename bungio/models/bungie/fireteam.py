import datetime
from typing import TYPE_CHECKING, Any, Optional

import attr

from bungio.models.base import BaseEnum, BaseModel


class FireteamDateRange(BaseEnum):
    """
    Not specified.
    """

    ALL = 0
    """Not specified. """
    NOW = 1
    """Not specified. """
    TWENTY_FOUR_HOURS = 2
    """Not specified. """
    FORTY_EIGHT_HOURS = 3
    """Not specified. """
    THIS_WEEK = 4
    """Not specified. """


class FireteamPlatform(BaseEnum):
    """
    Not specified.
    """

    ANY = 0
    """Not specified. """
    PLAYSTATION4 = 1
    """Not specified. """
    XBOX_ONE = 2
    """Not specified. """
    BLIZZARD = 3
    """Not specified. """
    STEAM = 4
    """Not specified. """
    STADIA = 5
    """Not specified. """


class FireteamPublicSearchOption(BaseEnum):
    """
    Not specified.
    """

    PUBLIC_AND_PRIVATE = 0
    """Not specified. """
    PUBLIC_ONLY = 1
    """Not specified. """
    PRIVATE_ONLY = 2
    """Not specified. """


class FireteamSlotSearch(BaseEnum):
    """
    Not specified.
    """

    NO_SLOT_RESTRICTION = 0
    """Not specified. """
    HAS_OPEN_PLAYER_SLOTS = 1
    """Not specified. """
    HAS_OPEN_PLAYER_OR_ALT_SLOTS = 2
    """Not specified. """


@attr.define
class FireteamSummary(BaseModel):
    """
    Not specified.

    Attributes:
        fireteam_id: Not specified.
        group_id: Not specified.
        platform: Not specified.
        activity_type: Not specified.
        is_immediate: Not specified.
        scheduled_time: Not specified.
        owner_membership_id: Not specified.
        player_slot_count: Not specified.
        alternate_slot_count: Not specified.
        available_player_slot_count: Not specified.
        available_alternate_slot_count: Not specified.
        title: Not specified.
        date_created: Not specified.
        date_modified: Not specified.
        is_public: Not specified.
        locale: Not specified.
        is_valid: Not specified.
        date_player_modified: Not specified.
        title_before_moderation: Not specified.
    """

    fireteam_id: int = attr.field()
    group_id: int = attr.field()
    platform: int = attr.field()
    activity_type: int = attr.field()
    is_immediate: bool = attr.field()
    scheduled_time: datetime.datetime = attr.field()
    owner_membership_id: int = attr.field()
    player_slot_count: int = attr.field()
    alternate_slot_count: int = attr.field()
    available_player_slot_count: int = attr.field()
    available_alternate_slot_count: int = attr.field()
    title: str = attr.field()
    date_created: datetime.datetime = attr.field()
    date_modified: datetime.datetime = attr.field()
    is_public: bool = attr.field()
    locale: str = attr.field()
    is_valid: bool = attr.field()
    date_player_modified: datetime.datetime = attr.field()
    title_before_moderation: str = attr.field()


@attr.define
class FireteamResponse(BaseModel):
    """
    Not specified.

    Attributes:
        summary: Not specified.
        members: Not specified.
        alternates: Not specified.
    """

    summary: "FireteamSummary" = attr.field()
    members: list["FireteamMember"] = attr.field()
    alternates: list["FireteamMember"] = attr.field()


@attr.define
class FireteamMember(BaseModel):
    """
    Not specified.

    Attributes:
        destiny_user_info: Not specified.
        bungie_net_user_info: Not specified.
        character_id: Not specified.
        date_joined: Not specified.
        has_microphone: Not specified.
        last_platform_invite_attempt_date: Not specified.
        last_platform_invite_attempt_result: Not specified.
    """

    destiny_user_info: "FireteamUserInfoCard" = attr.field()
    bungie_net_user_info: "UserInfoCard" = attr.field()
    character_id: int = attr.field()
    date_joined: datetime.datetime = attr.field()
    has_microphone: bool = attr.field()
    last_platform_invite_attempt_date: datetime.datetime = attr.field()
    last_platform_invite_attempt_result: int = attr.field()


@attr.define
class FireteamUserInfoCard(BaseModel):
    """
       Not specified.

       Attributes:
           fireteam_display_name: Not specified.
           fireteam_membership_type: Not specified.
           supplemental_display_name: A platform specific additional display name - ex: psn Real Name, bnet Unique Name, etc.
           icon_path: URL the Icon if available.
           cross_save_override: If there is a cross save override in effect, this value will tell you the type that is overridding this one.
           applicable_membership_types: The list of Membership Types indicating the platforms on which this Membership can be used.

    Not in Cross Save = its original membership type. Cross Save Primary = Any membership types it is overridding, and its original membership type Cross Save Overridden = Empty list
           is_public: If True, this is a public user membership.
           membership_type: Type of the membership. Not necessarily the native type.
           membership_id: Membership ID as they user is known in the Accounts service
           display_name: Display Name the player has chosen for themselves. The display name is optional when the data type is used as input to a platform API.
           bungie_global_display_name: The bungie global display name, if set.
           bungie_global_display_name_code: The bungie global display name code, if set.
    """

    fireteam_display_name: str = attr.field()
    fireteam_membership_type: int = attr.field()
    supplemental_display_name: str = attr.field()
    icon_path: str = attr.field()
    cross_save_override: int = attr.field()
    applicable_membership_types: list[int] = attr.field()
    is_public: bool = attr.field()
    membership_type: int = attr.field()
    membership_id: int = attr.field()
    display_name: str = attr.field()
    bungie_global_display_name: str = attr.field()
    bungie_global_display_name_code: int = attr.field()


class FireteamPlatformInviteResult(BaseEnum):
    """
    Not specified.
    """

    NONE = 0
    """Not specified. """
    SUCCESS = 1
    """Not specified. """
    ALREADY_IN_FIRETEAM = 2
    """Not specified. """
    THROTTLED = 3
    """Not specified. """
    SERVICE_ERROR = 4
    """Not specified. """
