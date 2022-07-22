# DO NOT CHANGE ANY CODE BELOW
# This file is generated automatically by `generate_api_schema.py` and will be overwritten
# Instead, change functions / models by subclassing them in the `./overwrites/` folder. They will be used instead.

from datetime import datetime
from typing import TYPE_CHECKING, Union

import attr

from bungio.models.base import BaseEnum, BaseFlagEnum, BaseModel
from bungio.models.mixins import DestinyClanMixin, DestinyUserMixin
from bungio.utils import enum_converter

if TYPE_CHECKING:
    from bungio.models import (
        BungieMembershipType,
        DestinyProgression,
        IgnoreLength,
        PagedQuery,
        UserInfoCard,
        UserMembership,
    )


@attr.define
class GroupUserInfoCard(BaseModel, DestinyUserMixin):
    """
    _No description given by bungie._

    None
    Attributes:
        applicable_membership_types: The list of Membership Types indicating the platforms on which this Membership can be used.  Not in Cross Save = its original membership type. Cross Save Primary = Any membership types it is overridding, and its original membership type Cross Save Overridden = Empty list
        bungie_global_display_name: The bungie global display name, if set.
        bungie_global_display_name_code: The bungie global display name code, if set.
        cross_save_override: If there is a cross save override in effect, this value will tell you the type that is overridding this one.
        display_name: Display Name the player has chosen for themselves. The display name is optional when the data type is used as input to a platform API.
        icon_path: URL the Icon if available.
        is_public: If True, this is a public user membership.
        last_seen_display_name: This will be the display name the clan server last saw the user as. If the account is an active cross save override, this will be the display name to use. Otherwise, this will match the displayName property.
        last_seen_display_name_type: The platform of the LastSeenDisplayName
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
    icon_path: str = attr.field()
    is_public: bool = attr.field()
    last_seen_display_name: str = attr.field()
    last_seen_display_name_type: Union["BungieMembershipType", int] = attr.field(
        converter=enum_converter("BungieMembershipType")
    )
    membership_id: int = attr.field()
    membership_type: Union["BungieMembershipType", int] = attr.field(converter=enum_converter("BungieMembershipType"))
    supplemental_display_name: str = attr.field()


@attr.define
class GroupResponse(BaseModel):
    """
    _No description given by bungie._

    None
    Attributes:
        alliance_status: _No description given by bungie._
        allied_ids: _No description given by bungie._
        current_user_member_map: This property will be populated if the authenticated user is a member of the group. Note that because of account linking, a user can sometimes be part of a clan more than once. As such, this returns the highest member type available.
        current_user_memberships_inactive_for_destiny: A convenience property that indicates if every membership you (the current user) have that is a part of this group are part of an account that is considered inactive - for example, overridden accounts in Cross Save.
        current_user_potential_member_map: This property will be populated if the authenticated user is an applicant or has an outstanding invitation to join. Note that because of account linking, a user can sometimes be part of a clan more than once.
        detail: _No description given by bungie._
        founder: _No description given by bungie._
        group_join_invite_count: _No description given by bungie._
        parent_group: _No description given by bungie._
    """

    alliance_status: Union["GroupAllianceStatus", int] = attr.field(converter=enum_converter("GroupAllianceStatus"))
    allied_ids: list[int] = attr.field(metadata={"type": """list[int]"""})
    current_user_member_map: dict[Union["BungieMembershipType", int], "GroupMember"] = attr.field(
        metadata={"type": """dict[BungieMembershipType, GroupMember]"""}
    )
    current_user_memberships_inactive_for_destiny: bool = attr.field()
    current_user_potential_member_map: dict[Union["BungieMembershipType", int], "GroupPotentialMember"] = attr.field(
        metadata={"type": """dict[BungieMembershipType, GroupPotentialMember]"""}
    )
    detail: "GroupV2" = attr.field()
    founder: "GroupMember" = attr.field()
    group_join_invite_count: int = attr.field()
    parent_group: "GroupV2" = attr.field()


@attr.define
class GroupV2(BaseModel, DestinyClanMixin):
    """
    _No description given by bungie._

    None
    Attributes:
        about: _No description given by bungie._
        allow_chat: _No description given by bungie._
        avatar_image_index: _No description given by bungie._
        avatar_path: _No description given by bungie._
        ban_expire_date: _No description given by bungie._
        banner_path: _No description given by bungie._
        chat_security: _No description given by bungie._
        clan_info: _No description given by bungie._
        conversation_id: _No description given by bungie._
        creation_date: _No description given by bungie._
        default_publicity: _No description given by bungie._
        enable_invitation_messaging_for_admins: _No description given by bungie._
        features: _No description given by bungie._
        group_id: _No description given by bungie._
        group_type: _No description given by bungie._
        homepage: _No description given by bungie._
        is_default_post_public: _No description given by bungie._
        is_public: _No description given by bungie._
        is_public_topic_admin_only: _No description given by bungie._
        locale: _No description given by bungie._
        member_count: _No description given by bungie._
        membership_id_created: _No description given by bungie._
        membership_option: _No description given by bungie._
        modification_date: _No description given by bungie._
        motto: _No description given by bungie._
        name: _No description given by bungie._
        tags: _No description given by bungie._
        theme: _No description given by bungie._
    """

    about: str = attr.field()
    allow_chat: bool = attr.field()
    avatar_image_index: int = attr.field()
    avatar_path: str = attr.field()
    ban_expire_date: datetime = attr.field()
    banner_path: str = attr.field()
    chat_security: Union["ChatSecuritySetting", int] = attr.field(converter=enum_converter("ChatSecuritySetting"))
    clan_info: "GroupV2ClanInfoAndInvestment" = attr.field()
    conversation_id: int = attr.field()
    creation_date: datetime = attr.field()
    default_publicity: Union["GroupPostPublicity", int] = attr.field(converter=enum_converter("GroupPostPublicity"))
    enable_invitation_messaging_for_admins: bool = attr.field()
    features: "GroupFeatures" = attr.field()
    group_id: int = attr.field()
    group_type: Union["GroupType", int] = attr.field(converter=enum_converter("GroupType"))
    homepage: Union["GroupHomepage", int] = attr.field(converter=enum_converter("GroupHomepage"))
    is_default_post_public: bool = attr.field()
    is_public: bool = attr.field()
    is_public_topic_admin_only: bool = attr.field()
    locale: str = attr.field()
    member_count: int = attr.field()
    membership_id_created: int = attr.field()
    membership_option: Union["MembershipOption", int] = attr.field(converter=enum_converter("MembershipOption"))
    modification_date: datetime = attr.field()
    motto: str = attr.field()
    name: str = attr.field()
    tags: list[str] = attr.field(metadata={"type": """list[str]"""})
    theme: str = attr.field()


class GroupType(BaseEnum):
    """
    _No description given by bungie._
    """

    GENERAL = 0
    """_No description given by bungie._ """
    CLAN = 1
    """_No description given by bungie._ """


class ChatSecuritySetting(BaseEnum):
    """
    _No description given by bungie._
    """

    GROUP = 0
    """_No description given by bungie._ """
    ADMINS = 1
    """_No description given by bungie._ """


class GroupHomepage(BaseEnum):
    """
    _No description given by bungie._
    """

    WALL = 0
    """_No description given by bungie._ """
    FORUM = 1
    """_No description given by bungie._ """
    ALLIANCE_FORUM = 2
    """_No description given by bungie._ """


class MembershipOption(BaseEnum):
    """
    _No description given by bungie._
    """

    REVIEWED = 0
    """_No description given by bungie._ """
    OPEN = 1
    """_No description given by bungie._ """
    CLOSED = 2
    """_No description given by bungie._ """


class GroupPostPublicity(BaseEnum):
    """
    _No description given by bungie._
    """

    PUBLIC = 0
    """_No description given by bungie._ """
    ALLIANCE = 1
    """_No description given by bungie._ """
    PRIVATE = 2
    """_No description given by bungie._ """


@attr.define
class GroupFeatures(BaseModel):
    """
    _No description given by bungie._

    None
    Attributes:
        capabilities: _No description given by bungie._
        host_guided_game_permission_override: Minimum Member Level allowed to host guided games Always Allowed: Founder, Acting Founder, Admin Allowed Overrides: None, Member, Beginner Default is Member for clans, None for groups, although this means nothing for groups.
        invite_permission_override: Minimum Member Level allowed to invite new members to group Always Allowed: Founder, Acting Founder True means admins have this power, false means they don't Default is false for clans, true for groups.
        join_level: Level to join a member at when accepting an invite, application, or joining an open clan Default is Beginner.
        maximum_members: _No description given by bungie._
        maximum_memberships_of_group_type: Maximum number of groups of this type a typical membership may join. For example, a user may join about 50 General groups with their Bungie.net account. They may join one clan per Destiny membership.
        membership_types: _No description given by bungie._
        update_banner_permission_override: Minimum Member Level allowed to update banner Always Allowed: Founder, Acting Founder True means admins have this power, false means they don't Default is false for clans, true for groups.
        update_culture_permission_override: Minimum Member Level allowed to update group culture Always Allowed: Founder, Acting Founder True means admins have this power, false means they don't Default is false for clans, true for groups.
    """

    capabilities: Union["Capabilities", int] = attr.field(converter=enum_converter("Capabilities"))
    host_guided_game_permission_override: Union["HostGuidedGamesPermissionLevel", int] = attr.field(
        converter=enum_converter("HostGuidedGamesPermissionLevel")
    )
    invite_permission_override: bool = attr.field()
    join_level: Union["RuntimeGroupMemberType", int] = attr.field(converter=enum_converter("RuntimeGroupMemberType"))
    maximum_members: int = attr.field()
    maximum_memberships_of_group_type: int = attr.field()
    membership_types: list[Union["BungieMembershipType", int]] = attr.field(
        converter=enum_converter("BungieMembershipType")
    )
    update_banner_permission_override: bool = attr.field()
    update_culture_permission_override: bool = attr.field()


class Capabilities(BaseFlagEnum):
    """
    _No description given by bungie._
    """

    NONE = 0
    """_No description given by bungie._ """
    LEADERBOARDS = 1
    """_No description given by bungie._ """
    CALLSIGN = 2
    """_No description given by bungie._ """
    OPTIONAL_CONVERSATIONS = 4
    """_No description given by bungie._ """
    CLAN_BANNER = 8
    """_No description given by bungie._ """
    D2_INVESTMENT_DATA = 16
    """_No description given by bungie._ """
    TAGS = 32
    """_No description given by bungie._ """
    ALLIANCES = 64
    """_No description given by bungie._ """


class HostGuidedGamesPermissionLevel(BaseEnum):
    """
    Used for setting the guided game permission level override (admins and founders can always host guided games).
    """

    NONE = 0
    """_No description given by bungie._ """
    BEGINNER = 1
    """_No description given by bungie._ """
    MEMBER = 2
    """_No description given by bungie._ """


class RuntimeGroupMemberType(BaseEnum):
    """
    The member levels used by all V2 Groups API. Individual group types use their own mappings in their native storage (general uses BnetDbGroupMemberType and D2 clans use ClanMemberLevel), but they are all translated to this in the runtime api. These runtime values should NEVER be stored anywhere, so the values can be changed as necessary.
    """

    NONE = 0
    """_No description given by bungie._ """
    BEGINNER = 1
    """_No description given by bungie._ """
    MEMBER = 2
    """_No description given by bungie._ """
    ADMIN = 3
    """_No description given by bungie._ """
    ACTING_FOUNDER = 4
    """_No description given by bungie._ """
    FOUNDER = 5
    """_No description given by bungie._ """


@attr.define
class GroupV2ClanInfo(BaseModel):
    """
    This contract contains clan-specific group information. It does not include any investment data.

    None
    Attributes:
        clan_banner_data: _No description given by bungie._
        clan_callsign: _No description given by bungie._
    """

    clan_banner_data: "ClanBanner" = attr.field()
    clan_callsign: str = attr.field()


@attr.define
class ClanBanner(BaseModel):
    """
    _No description given by bungie._

    None
    Attributes:
        decal_background_color_id: _No description given by bungie._
        decal_color_id: _No description given by bungie._
        decal_id: _No description given by bungie._
        gonfalon_color_id: _No description given by bungie._
        gonfalon_detail_color_id: _No description given by bungie._
        gonfalon_detail_id: _No description given by bungie._
        gonfalon_id: _No description given by bungie._
    """

    decal_background_color_id: int = attr.field()
    decal_color_id: int = attr.field()
    decal_id: int = attr.field()
    gonfalon_color_id: int = attr.field()
    gonfalon_detail_color_id: int = attr.field()
    gonfalon_detail_id: int = attr.field()
    gonfalon_id: int = attr.field()


@attr.define
class GroupV2ClanInfoAndInvestment(BaseModel):
    """
    The same as GroupV2ClanInfo, but includes any investment data.

    None
    Attributes:
        clan_banner_data: _No description given by bungie._
        clan_callsign: _No description given by bungie._
        d2_clan_progressions: _No description given by bungie._
    """

    clan_banner_data: "ClanBanner" = attr.field()
    clan_callsign: str = attr.field()
    d2_clan_progressions: dict[int, "DestinyProgression"] = attr.field(
        metadata={"type": """dict[int, DestinyProgression]"""}
    )


@attr.define
class GroupUserBase(BaseModel, DestinyClanMixin):
    """
    _No description given by bungie._

    None
    Attributes:
        bungie_net_user_info: _No description given by bungie._
        destiny_user_info: _No description given by bungie._
        group_id: _No description given by bungie._
        join_date: _No description given by bungie._
    """

    bungie_net_user_info: "UserInfoCard" = attr.field()
    destiny_user_info: "GroupUserInfoCard" = attr.field()
    group_id: int = attr.field()
    join_date: datetime = attr.field()


@attr.define
class GroupMember(BaseModel, DestinyClanMixin):
    """
    _No description given by bungie._

    None
    Attributes:
        bungie_net_user_info: _No description given by bungie._
        destiny_user_info: _No description given by bungie._
        group_id: _No description given by bungie._
        is_online: _No description given by bungie._
        join_date: _No description given by bungie._
        last_online_status_change: _No description given by bungie._
        member_type: _No description given by bungie._
    """

    bungie_net_user_info: "UserInfoCard" = attr.field()
    destiny_user_info: "GroupUserInfoCard" = attr.field()
    group_id: int = attr.field()
    is_online: bool = attr.field()
    join_date: datetime = attr.field()
    last_online_status_change: int = attr.field()
    member_type: Union["RuntimeGroupMemberType", int] = attr.field(converter=enum_converter("RuntimeGroupMemberType"))


class GroupAllianceStatus(BaseEnum):
    """
    _No description given by bungie._
    """

    UNALLIED = 0
    """_No description given by bungie._ """
    PARENT = 1
    """_No description given by bungie._ """
    CHILD = 2
    """_No description given by bungie._ """


@attr.define
class GroupPotentialMember(BaseModel, DestinyClanMixin):
    """
    _No description given by bungie._

    None
    Attributes:
        bungie_net_user_info: _No description given by bungie._
        destiny_user_info: _No description given by bungie._
        group_id: _No description given by bungie._
        join_date: _No description given by bungie._
        potential_status: _No description given by bungie._
    """

    bungie_net_user_info: "UserInfoCard" = attr.field()
    destiny_user_info: "GroupUserInfoCard" = attr.field()
    group_id: int = attr.field()
    join_date: datetime = attr.field()
    potential_status: Union["GroupPotentialMemberStatus", int] = attr.field(
        converter=enum_converter("GroupPotentialMemberStatus")
    )


class GroupPotentialMemberStatus(BaseEnum):
    """
    _No description given by bungie._
    """

    NONE = 0
    """_No description given by bungie._ """
    APPLICANT = 1
    """_No description given by bungie._ """
    INVITEE = 2
    """_No description given by bungie._ """


class GroupDateRange(BaseEnum):
    """
    _No description given by bungie._
    """

    ALL = 0
    """_No description given by bungie._ """
    PAST_DAY = 1
    """_No description given by bungie._ """
    PAST_WEEK = 2
    """_No description given by bungie._ """
    PAST_MONTH = 3
    """_No description given by bungie._ """
    PAST_YEAR = 4
    """_No description given by bungie._ """


@attr.define
class GroupV2Card(BaseModel, DestinyClanMixin):
    """
    A small infocard of group information, usually used for when a list of groups are returned

    None
    Attributes:
        about: _No description given by bungie._
        avatar_path: _No description given by bungie._
        capabilities: _No description given by bungie._
        clan_info: _No description given by bungie._
        creation_date: _No description given by bungie._
        group_id: _No description given by bungie._
        group_type: _No description given by bungie._
        locale: _No description given by bungie._
        member_count: _No description given by bungie._
        membership_option: _No description given by bungie._
        motto: _No description given by bungie._
        name: _No description given by bungie._
        theme: _No description given by bungie._
    """

    about: str = attr.field()
    avatar_path: str = attr.field()
    capabilities: Union["Capabilities", int] = attr.field(converter=enum_converter("Capabilities"))
    clan_info: "GroupV2ClanInfo" = attr.field()
    creation_date: datetime = attr.field()
    group_id: int = attr.field()
    group_type: Union["GroupType", int] = attr.field(converter=enum_converter("GroupType"))
    locale: str = attr.field()
    member_count: int = attr.field()
    membership_option: Union["MembershipOption", int] = attr.field(converter=enum_converter("MembershipOption"))
    motto: str = attr.field()
    name: str = attr.field()
    theme: str = attr.field()


@attr.define
class GroupSearchResponse(BaseModel):
    """
    _No description given by bungie._

    None
    Attributes:
        has_more: _No description given by bungie._
        query: _No description given by bungie._
        replacement_continuation_token: _No description given by bungie._
        results: _No description given by bungie._
        total_results: _No description given by bungie._
        use_total_results: If useTotalResults is true, then totalResults represents an accurate count. If False, it does not, and may be estimated/only the size of the current page. Either way, you should probably always only trust hasMore. This is a long-held historical throwback to when we used to do paging with known total results. Those queries toasted our database, and we were left to hastily alter our endpoints and create backward- compatible shims, of which useTotalResults is one.
    """

    has_more: bool = attr.field()
    query: "PagedQuery" = attr.field()
    replacement_continuation_token: str = attr.field()
    results: list["GroupV2Card"] = attr.field(metadata={"type": """list[GroupV2Card]"""})
    total_results: int = attr.field()
    use_total_results: bool = attr.field()


@attr.define
class OverwrittenGroupQuery(BaseModel):
    """
    NOTE: GroupQuery, as of Destiny 2, has essentially two totally different and incompatible "modes". If you are querying for a group, you can pass any of the properties below. If you are querying for a Clan, you MUST NOT pass any of the following properties (they must be null or undefined in your request, not just empty string/default values): - groupMemberCountFilter - localeFilter - tagText If you pass these, you will get a useless InvalidParameters error.

    None
    Attributes:
        creation_date: _No description given by bungie._
        current_page: _No description given by bungie._
        group_member_count_filter: _No description given by bungie._
        group_type: _No description given by bungie._
        items_per_page: _No description given by bungie._
        locale_filter: _No description given by bungie._
        name: _No description given by bungie._
        request_continuation_token: _No description given by bungie._
        sort_by: _No description given by bungie._
        tag_text: _No description given by bungie._
    """

    creation_date: Union["GroupDateRange", int] = attr.field(converter=enum_converter("GroupDateRange"))
    current_page: int = attr.field()
    group_member_count_filter: int = attr.field()
    group_type: Union["GroupType", int] = attr.field(converter=enum_converter("GroupType"))
    items_per_page: int = attr.field()
    locale_filter: str = attr.field()
    name: str = attr.field()
    request_continuation_token: str = attr.field()
    sort_by: Union["GroupSortBy", int] = attr.field(converter=enum_converter("GroupSortBy"))
    tag_text: str = attr.field()


class GroupSortBy(BaseEnum):
    """
    _No description given by bungie._
    """

    NAME = 0
    """_No description given by bungie._ """
    DATE = 1
    """_No description given by bungie._ """
    POPULARITY = 2
    """_No description given by bungie._ """
    ID = 3
    """_No description given by bungie._ """


class GroupMemberCountFilter(BaseEnum):
    """
    _No description given by bungie._
    """

    ALL = 0
    """_No description given by bungie._ """
    ONE_TO_TEN = 1
    """_No description given by bungie._ """
    ELEVEN_TO_ONE_HUNDRED = 2
    """_No description given by bungie._ """
    GREATER_THAN_ONE_HUNDRED = 3
    """_No description given by bungie._ """


@attr.define
class GroupNameSearchRequest(BaseModel):
    """
    _No description given by bungie._

    None
    Attributes:
        group_name: _No description given by bungie._
        group_type: _No description given by bungie._
    """

    group_name: str = attr.field()
    group_type: Union["GroupType", int] = attr.field(converter=enum_converter("GroupType"))


@attr.define
class GroupOptionalConversation(BaseModel, DestinyClanMixin):
    """
    _No description given by bungie._

    None
    Attributes:
        chat_enabled: _No description given by bungie._
        chat_name: _No description given by bungie._
        chat_security: _No description given by bungie._
        conversation_id: _No description given by bungie._
        group_id: _No description given by bungie._
    """

    chat_enabled: bool = attr.field()
    chat_name: str = attr.field()
    chat_security: Union["ChatSecuritySetting", int] = attr.field(converter=enum_converter("ChatSecuritySetting"))
    conversation_id: int = attr.field()
    group_id: int = attr.field()


@attr.define
class GroupEditAction(BaseModel):
    """
    _No description given by bungie._

    None
    Attributes:
        about: _No description given by bungie._
        allow_chat: _No description given by bungie._
        avatar_image_index: _No description given by bungie._
        callsign: _No description given by bungie._
        chat_security: _No description given by bungie._
        default_publicity: _No description given by bungie._
        enable_invitation_messaging_for_admins: _No description given by bungie._
        homepage: _No description given by bungie._
        is_public: _No description given by bungie._
        is_public_topic_admin_only: _No description given by bungie._
        locale: _No description given by bungie._
        membership_option: _No description given by bungie._
        motto: _No description given by bungie._
        name: _No description given by bungie._
        tags: _No description given by bungie._
        theme: _No description given by bungie._
    """

    about: str = attr.field()
    allow_chat: bool = attr.field()
    avatar_image_index: int = attr.field()
    callsign: str = attr.field()
    chat_security: int = attr.field()
    default_publicity: int = attr.field()
    enable_invitation_messaging_for_admins: bool = attr.field()
    homepage: int = attr.field()
    is_public: bool = attr.field()
    is_public_topic_admin_only: bool = attr.field()
    locale: str = attr.field()
    membership_option: int = attr.field()
    motto: str = attr.field()
    name: str = attr.field()
    tags: str = attr.field()
    theme: str = attr.field()


@attr.define
class GroupOptionsEditAction(BaseModel):
    """
    _No description given by bungie._

    None
    Attributes:
        host_guided_game_permission_override: Minimum Member Level allowed to host guided games Always Allowed: Founder, Acting Founder, Admin Allowed Overrides: None, Member, Beginner Default is Member for clans, None for groups, although this means nothing for groups.
        invite_permission_override: Minimum Member Level allowed to invite new members to group Always Allowed: Founder, Acting Founder True means admins have this power, false means they don't Default is false for clans, true for groups.
        join_level: Level to join a member at when accepting an invite, application, or joining an open clan Default is Beginner.
        update_banner_permission_override: Minimum Member Level allowed to update banner Always Allowed: Founder, Acting Founder True means admins have this power, false means they don't Default is false for clans, true for groups.
        update_culture_permission_override: Minimum Member Level allowed to update group culture Always Allowed: Founder, Acting Founder True means admins have this power, false means they don't Default is false for clans, true for groups.
    """

    host_guided_game_permission_override: int = attr.field()
    invite_permission_override: bool = attr.field()
    join_level: int = attr.field()
    update_banner_permission_override: bool = attr.field()
    update_culture_permission_override: bool = attr.field()


@attr.define
class GroupOptionalConversationAddRequest(BaseModel):
    """
    _No description given by bungie._

    None
    Attributes:
        chat_name: _No description given by bungie._
        chat_security: _No description given by bungie._
    """

    chat_name: str = attr.field()
    chat_security: Union["ChatSecuritySetting", int] = attr.field(converter=enum_converter("ChatSecuritySetting"))


@attr.define
class GroupOptionalConversationEditRequest(BaseModel):
    """
    _No description given by bungie._

    None
    Attributes:
        chat_enabled: _No description given by bungie._
        chat_name: _No description given by bungie._
        chat_security: _No description given by bungie._
    """

    chat_enabled: bool = attr.field()
    chat_name: str = attr.field()
    chat_security: int = attr.field()


@attr.define
class GroupMemberLeaveResult(BaseModel):
    """
    _No description given by bungie._

    None
    Attributes:
        group: _No description given by bungie._
        group_deleted: _No description given by bungie._
    """

    group: "GroupV2" = attr.field()
    group_deleted: bool = attr.field()


@attr.define
class GroupBanRequest(BaseModel):
    """
    _No description given by bungie._

    None
    Attributes:
        comment: _No description given by bungie._
        length: _No description given by bungie._
    """

    comment: str = attr.field()
    length: Union["IgnoreLength", int] = attr.field(converter=enum_converter("IgnoreLength"))


@attr.define
class GroupBan(BaseModel, DestinyClanMixin):
    """
    _No description given by bungie._

    None
    Attributes:
        bungie_net_user_info: _No description given by bungie._
        comment: _No description given by bungie._
        created_by: _No description given by bungie._
        date_banned: _No description given by bungie._
        date_expires: _No description given by bungie._
        destiny_user_info: _No description given by bungie._
        group_id: _No description given by bungie._
        last_modified_by: _No description given by bungie._
    """

    bungie_net_user_info: "UserInfoCard" = attr.field()
    comment: str = attr.field()
    created_by: "UserInfoCard" = attr.field()
    date_banned: datetime = attr.field()
    date_expires: datetime = attr.field()
    destiny_user_info: "GroupUserInfoCard" = attr.field()
    group_id: int = attr.field()
    last_modified_by: "UserInfoCard" = attr.field()


@attr.define
class GroupMemberApplication(BaseModel, DestinyClanMixin):
    """
    _No description given by bungie._

    None
    Attributes:
        bungie_net_user_info: _No description given by bungie._
        creation_date: _No description given by bungie._
        destiny_user_info: _No description given by bungie._
        group_id: _No description given by bungie._
        request_message: _No description given by bungie._
        resolve_date: _No description given by bungie._
        resolve_message: _No description given by bungie._
        resolve_state: _No description given by bungie._
        resolved_by_membership_id: _No description given by bungie._
    """

    bungie_net_user_info: "UserInfoCard" = attr.field()
    creation_date: datetime = attr.field()
    destiny_user_info: "GroupUserInfoCard" = attr.field()
    group_id: int = attr.field()
    request_message: str = attr.field()
    resolve_date: datetime = attr.field()
    resolve_message: str = attr.field()
    resolve_state: Union["GroupApplicationResolveState", int] = attr.field(
        converter=enum_converter("GroupApplicationResolveState")
    )
    resolved_by_membership_id: int = attr.field()


class GroupApplicationResolveState(BaseEnum):
    """
    _No description given by bungie._
    """

    UNRESOLVED = 0
    """_No description given by bungie._ """
    ACCEPTED = 1
    """_No description given by bungie._ """
    DENIED = 2
    """_No description given by bungie._ """
    RESCINDED = 3
    """_No description given by bungie._ """


@attr.define
class GroupApplicationRequest(BaseModel):
    """
    _No description given by bungie._

    None
    Attributes:
        message: _No description given by bungie._
    """

    message: str = attr.field()


@attr.define
class GroupApplicationListRequest(BaseModel):
    """
    _No description given by bungie._

    None
    Attributes:
        memberships: _No description given by bungie._
        message: _No description given by bungie._
    """

    memberships: list["UserMembership"] = attr.field(metadata={"type": """list[UserMembership]"""})
    message: str = attr.field()


class GroupsForMemberFilter(BaseEnum):
    """
    _No description given by bungie._
    """

    ALL = 0
    """_No description given by bungie._ """
    FOUNDED = 1
    """_No description given by bungie._ """
    NON_FOUNDED = 2
    """_No description given by bungie._ """


@attr.define
class GroupMembershipBase(BaseModel):
    """
    _No description given by bungie._

    None
    Attributes:
        group: _No description given by bungie._
    """

    group: "GroupV2" = attr.field()


@attr.define
class GroupMembership(BaseModel):
    """
    _No description given by bungie._

    None
    Attributes:
        group: _No description given by bungie._
        member: _No description given by bungie._
    """

    group: "GroupV2" = attr.field()
    member: "GroupMember" = attr.field()


@attr.define
class GroupMembershipSearchResponse(BaseModel):
    """
    _No description given by bungie._

    None
    Attributes:
        has_more: _No description given by bungie._
        query: _No description given by bungie._
        replacement_continuation_token: _No description given by bungie._
        results: _No description given by bungie._
        total_results: _No description given by bungie._
        use_total_results: If useTotalResults is true, then totalResults represents an accurate count. If False, it does not, and may be estimated/only the size of the current page. Either way, you should probably always only trust hasMore. This is a long-held historical throwback to when we used to do paging with known total results. Those queries toasted our database, and we were left to hastily alter our endpoints and create backward- compatible shims, of which useTotalResults is one.
    """

    has_more: bool = attr.field()
    query: "PagedQuery" = attr.field()
    replacement_continuation_token: str = attr.field()
    results: list["GroupMembership"] = attr.field(metadata={"type": """list[GroupMembership]"""})
    total_results: int = attr.field()
    use_total_results: bool = attr.field()


@attr.define
class GetGroupsForMemberResponse(BaseModel):
    """
    _No description given by bungie._

    None
    Attributes:
        are_all_memberships_inactive: A convenience property that indicates if every membership this user has that is a part of this group are part of an account that is considered inactive - for example, overridden accounts in Cross Save.  The key is the Group ID for the group being checked, and the value is true if the users' memberships for that group are all inactive.
        has_more: _No description given by bungie._
        query: _No description given by bungie._
        replacement_continuation_token: _No description given by bungie._
        results: _No description given by bungie._
        total_results: _No description given by bungie._
        use_total_results: If useTotalResults is true, then totalResults represents an accurate count. If False, it does not, and may be estimated/only the size of the current page. Either way, you should probably always only trust hasMore. This is a long-held historical throwback to when we used to do paging with known total results. Those queries toasted our database, and we were left to hastily alter our endpoints and create backward- compatible shims, of which useTotalResults is one.
    """

    are_all_memberships_inactive: dict[int, bool] = attr.field(metadata={"type": """dict[int, bool]"""})
    has_more: bool = attr.field()
    query: "PagedQuery" = attr.field()
    replacement_continuation_token: str = attr.field()
    results: list["GroupMembership"] = attr.field(metadata={"type": """list[GroupMembership]"""})
    total_results: int = attr.field()
    use_total_results: bool = attr.field()


@attr.define
class GroupPotentialMembership(BaseModel):
    """
    _No description given by bungie._

    None
    Attributes:
        group: _No description given by bungie._
        member: _No description given by bungie._
    """

    group: "GroupV2" = attr.field()
    member: "GroupPotentialMember" = attr.field()


@attr.define
class GroupPotentialMembershipSearchResponse(BaseModel):
    """
    _No description given by bungie._

    None
    Attributes:
        has_more: _No description given by bungie._
        query: _No description given by bungie._
        replacement_continuation_token: _No description given by bungie._
        results: _No description given by bungie._
        total_results: _No description given by bungie._
        use_total_results: If useTotalResults is true, then totalResults represents an accurate count. If False, it does not, and may be estimated/only the size of the current page. Either way, you should probably always only trust hasMore. This is a long-held historical throwback to when we used to do paging with known total results. Those queries toasted our database, and we were left to hastily alter our endpoints and create backward- compatible shims, of which useTotalResults is one.
    """

    has_more: bool = attr.field()
    query: "PagedQuery" = attr.field()
    replacement_continuation_token: str = attr.field()
    results: list["GroupPotentialMembership"] = attr.field(metadata={"type": """list[GroupPotentialMembership]"""})
    total_results: int = attr.field()
    use_total_results: bool = attr.field()


@attr.define
class GroupApplicationResponse(BaseModel):
    """
    _No description given by bungie._

    None
    Attributes:
        resolution: _No description given by bungie._
    """

    resolution: Union["GroupApplicationResolveState", int] = attr.field(
        converter=enum_converter("GroupApplicationResolveState")
    )
