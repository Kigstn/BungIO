# DO NOT CHANGE ANY CODE BELOW
# This file is generated automatically by `generate_api_schema.py` and will be overwritten
# Instead, change functions / models by subclassing them in the `./overwrites/` folder. They will be used instead.

from datetime import datetime
from typing import TYPE_CHECKING, Union

import attr

from bungio.models.base import BaseEnum, BaseModel
from bungio.models.mixins import DestinyClanMixin, DestinyUserMixin
from bungio.utils import enum_converter

if TYPE_CHECKING:
    from bungio.models import BungieMembershipType, UserInfoCard


class FireteamDateRange(BaseEnum):
    """
    _No description given by bungie._
    """

    ALL = 0
    """_No description given by bungie._ """
    NOW = 1
    """_No description given by bungie._ """
    TWENTY_FOUR_HOURS = 2
    """_No description given by bungie._ """
    FORTY_EIGHT_HOURS = 3
    """_No description given by bungie._ """
    THIS_WEEK = 4
    """_No description given by bungie._ """


class FireteamPlatform(BaseEnum):
    """
    _No description given by bungie._
    """

    ANY = 0
    """_No description given by bungie._ """
    PLAYSTATION4 = 1
    """_No description given by bungie._ """
    XBOX_ONE = 2
    """_No description given by bungie._ """
    BLIZZARD = 3
    """_No description given by bungie._ """
    STEAM = 4
    """_No description given by bungie._ """
    STADIA = 5
    """_No description given by bungie._ """


class FireteamPublicSearchOption(BaseEnum):
    """
    _No description given by bungie._
    """

    PUBLIC_AND_PRIVATE = 0
    """_No description given by bungie._ """
    PUBLIC_ONLY = 1
    """_No description given by bungie._ """
    PRIVATE_ONLY = 2
    """_No description given by bungie._ """


class FireteamSlotSearch(BaseEnum):
    """
    _No description given by bungie._
    """

    NO_SLOT_RESTRICTION = 0
    """_No description given by bungie._ """
    HAS_OPEN_PLAYER_SLOTS = 1
    """_No description given by bungie._ """
    HAS_OPEN_PLAYER_OR_ALT_SLOTS = 2
    """_No description given by bungie._ """


@attr.define
class FireteamSummary(BaseModel, DestinyClanMixin):
    """
    _No description given by bungie._

    None
    Attributes:
        activity_type: _No description given by bungie._
        alternate_slot_count: _No description given by bungie._
        available_alternate_slot_count: _No description given by bungie._
        available_player_slot_count: _No description given by bungie._
        date_created: _No description given by bungie._
        date_modified: _No description given by bungie._
        date_player_modified: _No description given by bungie._
        fireteam_id: _No description given by bungie._
        group_id: _No description given by bungie._
        is_immediate: _No description given by bungie._
        is_public: _No description given by bungie._
        is_valid: _No description given by bungie._
        locale: _No description given by bungie._
        owner_membership_id: _No description given by bungie._
        platform: _No description given by bungie._
        player_slot_count: _No description given by bungie._
        scheduled_time: _No description given by bungie._
        title: _No description given by bungie._
        title_before_moderation: _No description given by bungie._
    """

    activity_type: int = attr.field()
    alternate_slot_count: int = attr.field()
    available_alternate_slot_count: int = attr.field()
    available_player_slot_count: int = attr.field()
    date_created: datetime = attr.field()
    date_modified: datetime = attr.field()
    date_player_modified: datetime = attr.field()
    fireteam_id: int = attr.field()
    group_id: int = attr.field()
    is_immediate: bool = attr.field()
    is_public: bool = attr.field()
    is_valid: bool = attr.field()
    locale: str = attr.field()
    owner_membership_id: int = attr.field()
    platform: Union["FireteamPlatform", int] = attr.field(converter=enum_converter("FireteamPlatform"))
    player_slot_count: int = attr.field()
    scheduled_time: datetime = attr.field()
    title: str = attr.field()
    title_before_moderation: str = attr.field()


@attr.define
class FireteamResponse(BaseModel):
    """
    _No description given by bungie._

    None
    Attributes:
        alternates: _No description given by bungie._
        members: _No description given by bungie._
        summary: _No description given by bungie._
    """

    alternates: list["FireteamMember"] = attr.field(metadata={"type": """list[FireteamMember]"""})
    members: list["FireteamMember"] = attr.field(metadata={"type": """list[FireteamMember]"""})
    summary: "FireteamSummary" = attr.field()


@attr.define
class FireteamMember(BaseModel):
    """
    _No description given by bungie._

    None
    Attributes:
        bungie_net_user_info: _No description given by bungie._
        character_id: _No description given by bungie._
        date_joined: _No description given by bungie._
        destiny_user_info: _No description given by bungie._
        has_microphone: _No description given by bungie._
        last_platform_invite_attempt_date: _No description given by bungie._
        last_platform_invite_attempt_result: _No description given by bungie._
    """

    bungie_net_user_info: "UserInfoCard" = attr.field()
    character_id: int = attr.field()
    date_joined: datetime = attr.field()
    destiny_user_info: "FireteamUserInfoCard" = attr.field()
    has_microphone: bool = attr.field()
    last_platform_invite_attempt_date: datetime = attr.field()
    last_platform_invite_attempt_result: Union["FireteamPlatformInviteResult", int] = attr.field(
        converter=enum_converter("FireteamPlatformInviteResult")
    )


@attr.define
class FireteamUserInfoCard(BaseModel, DestinyUserMixin):
    """
    _No description given by bungie._

    None
    Attributes:
        applicable_membership_types: The list of Membership Types indicating the platforms on which this Membership can be used.  Not in Cross Save = its original membership type. Cross Save Primary = Any membership types it is overridding, and its original membership type Cross Save Overridden = Empty list
        bungie_global_display_name: The bungie global display name, if set.
        bungie_global_display_name_code: The bungie global display name code, if set.
        cross_save_override: If there is a cross save override in effect, this value will tell you the type that is overridding this one.
        display_name: Display Name the player has chosen for themselves. The display name is optional when the data type is used as input to a platform API.
        fireteam_display_name: _No description given by bungie._
        fireteam_membership_type: _No description given by bungie._
        icon_path: URL the Icon if available.
        is_public: If True, this is a public user membership.
        membership_id: Membership ID as they user is known in the Accounts service
        membership_type: Type of the membership. Not necessarily the native type.
        supplemental_display_name: A platform specific additional display name - ex: psn Real Name, bnet Unique Name, etc.
    """

    applicable_membership_types: list[Union["BungieMembershipType", int]] = attr.field(
        converter=enum_converter("BungieMembershipType")
    )
    bungie_global_display_name: str = attr.field()
    bungie_global_display_name_code: int = attr.field()
    cross_save_override: Union["BungieMembershipType", int] = attr.field(
        converter=enum_converter("BungieMembershipType")
    )
    display_name: str = attr.field()
    fireteam_display_name: str = attr.field()
    fireteam_membership_type: Union["BungieMembershipType", int] = attr.field(
        converter=enum_converter("BungieMembershipType")
    )
    icon_path: str = attr.field()
    is_public: bool = attr.field()
    membership_id: int = attr.field()
    membership_type: Union["BungieMembershipType", int] = attr.field(converter=enum_converter("BungieMembershipType"))
    supplemental_display_name: str = attr.field()


class FireteamPlatformInviteResult(BaseEnum):
    """
    _No description given by bungie._
    """

    NONE = 0
    """_No description given by bungie._ """
    SUCCESS = 1
    """_No description given by bungie._ """
    ALREADY_IN_FIRETEAM = 2
    """_No description given by bungie._ """
    THROTTLED = 3
    """_No description given by bungie._ """
    SERVICE_ERROR = 4
    """_No description given by bungie._ """
