# DO NOT CHANGE ANY CODE BELOW
# This file is generated automatically by `generate_api_schema.py` and will be overwritten
# Instead, change functions / models by subclassing them in the `./overwrites/` folder. They will be used instead.

from datetime import datetime
from typing import Optional, Union, TYPE_CHECKING

from bungio.utils import enum_converter
from bungio.models.base import BaseModel, BaseEnum, custom_define, custom_field

from bungio.models.mixins import DestinyUserMixin
from bungio.models.mixins import DestinyClanMixin

if TYPE_CHECKING:
    from bungio.models import DestinyGuardianRankDefinition
    from bungio.models import BungieMembershipType
    from bungio.models import UserInfoCard


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
    EGS = 6
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


@custom_define()
class FireteamSummary(BaseModel, DestinyClanMixin):
    """
    _No description given by bungie._

    Tip: Manifest Information
        This model has some attributes which can be filled with additional information found in the manifest (`manifest_...`).
        Without additional work, these attributes will be `None`, since they require additional requests and database lookups.

        To fill the manifest dependent attributes, either:

        - Run `await ThisClass.fetch_manifest_information()`, see [here](/API Reference/Models/base)
        - Set `Client.always_return_manifest_information` to `True`, see [here](/API Reference/client)

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
        owner_current_guardian_rank_snapshot: _No description given by bungie._
        owner_highest_lifetime_guardian_rank_snapshot: _No description given by bungie._
        owner_membership_id: _No description given by bungie._
        owner_total_commendation_score_snapshot: _No description given by bungie._
        platform: _No description given by bungie._
        player_slot_count: _No description given by bungie._
        scheduled_time: _No description given by bungie._
        title: _No description given by bungie._
        title_before_moderation: _No description given by bungie._
        manifest_owner_current_guardian_rank_snapshot: Manifest information for `owner_current_guardian_rank_snapshot`
        manifest_owner_highest_lifetime_guardian_rank_snapshot: Manifest information for `owner_highest_lifetime_guardian_rank_snapshot`
    """

    activity_type: int = custom_field()
    alternate_slot_count: int = custom_field()
    available_alternate_slot_count: int = custom_field()
    available_player_slot_count: int = custom_field()
    date_created: datetime = custom_field()
    date_modified: datetime = custom_field()
    date_player_modified: datetime = custom_field()
    fireteam_id: int = custom_field(metadata={"int64": True})
    group_id: int = custom_field(metadata={"int64": True})
    is_immediate: bool = custom_field()
    is_public: bool = custom_field()
    is_valid: bool = custom_field()
    locale: str = custom_field()
    owner_current_guardian_rank_snapshot: int = custom_field()
    owner_highest_lifetime_guardian_rank_snapshot: int = custom_field()
    owner_membership_id: int = custom_field(metadata={"int64": True})
    owner_total_commendation_score_snapshot: int = custom_field()
    platform: Union["FireteamPlatform", int] = custom_field(converter=enum_converter("FireteamPlatform"))
    player_slot_count: int = custom_field()
    scheduled_time: datetime = custom_field()
    title: str = custom_field()
    title_before_moderation: str = custom_field()
    manifest_owner_current_guardian_rank_snapshot: Optional["DestinyGuardianRankDefinition"] = custom_field(
        default=None
    )
    manifest_owner_highest_lifetime_guardian_rank_snapshot: Optional["DestinyGuardianRankDefinition"] = custom_field(
        default=None
    )


@custom_define()
class FireteamResponse(BaseModel):
    """
    _No description given by bungie._

    None
    Attributes:
        alternates: _No description given by bungie._
        members: _No description given by bungie._
        summary: _No description given by bungie._
    """

    alternates: list["FireteamMember"] = custom_field(metadata={"type": """list[FireteamMember]"""})
    members: list["FireteamMember"] = custom_field(metadata={"type": """list[FireteamMember]"""})
    summary: "FireteamSummary" = custom_field()


@custom_define()
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

    bungie_net_user_info: "UserInfoCard" = custom_field()
    character_id: int = custom_field(metadata={"int64": True})
    date_joined: datetime = custom_field()
    destiny_user_info: "FireteamUserInfoCard" = custom_field()
    has_microphone: bool = custom_field()
    last_platform_invite_attempt_date: datetime = custom_field()
    last_platform_invite_attempt_result: Union["FireteamPlatformInviteResult", int] = custom_field(
        converter=enum_converter("FireteamPlatformInviteResult")
    )


@custom_define()
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

    applicable_membership_types: list[Union["BungieMembershipType", int]] = custom_field(
        converter=enum_converter("BungieMembershipType")
    )
    bungie_global_display_name: str = custom_field()
    bungie_global_display_name_code: int = custom_field()
    cross_save_override: Union["BungieMembershipType", int] = custom_field(
        converter=enum_converter("BungieMembershipType")
    )
    display_name: str = custom_field()
    fireteam_display_name: str = custom_field()
    fireteam_membership_type: Union["BungieMembershipType", int] = custom_field(
        converter=enum_converter("BungieMembershipType")
    )
    icon_path: str = custom_field()
    is_public: bool = custom_field()
    membership_id: int = custom_field(metadata={"int64": True})
    membership_type: Union["BungieMembershipType", int] = custom_field(converter=enum_converter("BungieMembershipType"))
    supplemental_display_name: str = custom_field()


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
