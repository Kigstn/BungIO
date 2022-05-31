import datetime
from typing import TYPE_CHECKING

import attr

from bungio.models.base import BaseEnum, BaseModel

if TYPE_CHECKING:
    from bungio.models import (
        FireteamMember,
        FireteamSummary,
        FireteamUserInfoCard,
        UserInfoCard,
    )


class FireteamDateRange(BaseEnum):
    """
    _No description given by bungie_
    """

    ALL = 0
    """_No description given by bungie_ """
    NOW = 1
    """_No description given by bungie_ """
    TWENTY_FOUR_HOURS = 2
    """_No description given by bungie_ """
    FORTY_EIGHT_HOURS = 3
    """_No description given by bungie_ """
    THIS_WEEK = 4
    """_No description given by bungie_ """


class FireteamPlatform(BaseEnum):
    """
    _No description given by bungie_
    """

    ANY = 0
    """_No description given by bungie_ """
    PLAYSTATION4 = 1
    """_No description given by bungie_ """
    XBOX_ONE = 2
    """_No description given by bungie_ """
    BLIZZARD = 3
    """_No description given by bungie_ """
    STEAM = 4
    """_No description given by bungie_ """
    STADIA = 5
    """_No description given by bungie_ """


class FireteamPublicSearchOption(BaseEnum):
    """
    _No description given by bungie_
    """

    PUBLIC_AND_PRIVATE = 0
    """_No description given by bungie_ """
    PUBLIC_ONLY = 1
    """_No description given by bungie_ """
    PRIVATE_ONLY = 2
    """_No description given by bungie_ """


class FireteamSlotSearch(BaseEnum):
    """
    _No description given by bungie_
    """

    NO_SLOT_RESTRICTION = 0
    """_No description given by bungie_ """
    HAS_OPEN_PLAYER_SLOTS = 1
    """_No description given by bungie_ """
    HAS_OPEN_PLAYER_OR_ALT_SLOTS = 2
    """_No description given by bungie_ """


@attr.define
class FireteamSummary(BaseModel):
    """
    _No description given by bungie_

    Attributes:
        fireteam_id: _No description given by bungie_
        group_id: _No description given by bungie_
        platform: _No description given by bungie_
        activity_type: _No description given by bungie_
        is_immediate: _No description given by bungie_
        scheduled_time: _No description given by bungie_
        owner_membership_id: _No description given by bungie_
        player_slot_count: _No description given by bungie_
        alternate_slot_count: _No description given by bungie_
        available_player_slot_count: _No description given by bungie_
        available_alternate_slot_count: _No description given by bungie_
        title: _No description given by bungie_
        date_created: _No description given by bungie_
        date_modified: _No description given by bungie_
        is_public: _No description given by bungie_
        locale: _No description given by bungie_
        is_valid: _No description given by bungie_
        date_player_modified: _No description given by bungie_
        title_before_moderation: _No description given by bungie_
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
    _No description given by bungie_

    Attributes:
        summary: _No description given by bungie_
        members: _No description given by bungie_
        alternates: _No description given by bungie_
    """

    summary: "FireteamSummary" = attr.field()
    members: list["FireteamMember"] = attr.field()
    alternates: list["FireteamMember"] = attr.field()


@attr.define
class FireteamMember(BaseModel):
    """
    _No description given by bungie_

    Attributes:
        destiny_user_info: _No description given by bungie_
        bungie_net_user_info: _No description given by bungie_
        character_id: _No description given by bungie_
        date_joined: _No description given by bungie_
        has_microphone: _No description given by bungie_
        last_platform_invite_attempt_date: _No description given by bungie_
        last_platform_invite_attempt_result: _No description given by bungie_
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
    _No description given by bungie_

    Attributes:
        fireteam_display_name: _No description given by bungie_
        fireteam_membership_type: _No description given by bungie_
        supplemental_display_name: A platform specific additional display name - ex: psn Real Name, bnet Unique Name, etc.
        icon_path: URL the Icon if available.
        cross_save_override: If there is a cross save override in effect, this value will tell you the type that is overridding this one.
        applicable_membership_types: The list of Membership Types indicating the platforms on which this Membership can be used.  Not in Cross Save = its original membership type. Cross Save Primary = Any membership types it is overridding, and its original membership type Cross Save Overridden = Empty list
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
    _No description given by bungie_
    """

    NONE = 0
    """_No description given by bungie_ """
    SUCCESS = 1
    """_No description given by bungie_ """
    ALREADY_IN_FIRETEAM = 2
    """_No description given by bungie_ """
    THROTTLED = 3
    """_No description given by bungie_ """
    SERVICE_ERROR = 4
    """_No description given by bungie_ """
