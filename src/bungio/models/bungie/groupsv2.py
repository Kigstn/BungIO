# DO NOT CHANGE ANY CODE BELOW
# This file is generated automatically by `generate_api_schema.py` and will be overwritten
# Instead, change functions / models by subclassing them in the `./overwrites/` folder. They will be used instead.

from datetime import datetime
from typing import TYPE_CHECKING, Union

from bungio.models.base import BaseEnum, BaseFlagEnum, BaseModel, custom_define, custom_field
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


@custom_define()
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

    applicable_membership_types: list[Union["BungieMembershipType", int]] = custom_field(
        converter=enum_converter("BungieMembershipType")
    )
    bungie_global_display_name: str = custom_field()
    bungie_global_display_name_code: int = custom_field()
    cross_save_override: Union["BungieMembershipType", int] = custom_field(
        converter=enum_converter("BungieMembershipType")
    )
    display_name: str = custom_field()
    icon_path: str = custom_field()
    is_public: bool = custom_field()
    last_seen_display_name: str = custom_field()
    last_seen_display_name_type: Union["BungieMembershipType", int] = custom_field(
        converter=enum_converter("BungieMembershipType")
    )
    membership_id: int = custom_field(metadata={"int64": True})
    membership_type: Union["BungieMembershipType", int] = custom_field(converter=enum_converter("BungieMembershipType"))
    supplemental_display_name: str = custom_field()


@custom_define()
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

    alliance_status: Union["GroupAllianceStatus", int] = custom_field(converter=enum_converter("GroupAllianceStatus"))
    allied_ids: list[int] = custom_field(metadata={"type": """list[int]"""})
    current_user_member_map: dict[Union["BungieMembershipType", int], "GroupMember"] = custom_field(
        metadata={"type": """dict[BungieMembershipType, GroupMember]"""}
    )
    current_user_memberships_inactive_for_destiny: bool = custom_field()
    current_user_potential_member_map: dict[Union["BungieMembershipType", int], "GroupPotentialMember"] = custom_field(
        metadata={"type": """dict[BungieMembershipType, GroupPotentialMember]"""}
    )
    detail: "GroupV2" = custom_field()
    founder: "GroupMember" = custom_field()
    group_join_invite_count: int = custom_field()
    parent_group: "GroupV2" = custom_field()


@custom_define()
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
        remote_group_id: _No description given by bungie._
        tags: _No description given by bungie._
        theme: _No description given by bungie._
    """

    about: str = custom_field()
    allow_chat: bool = custom_field()
    avatar_image_index: int = custom_field()
    avatar_path: str = custom_field()
    ban_expire_date: datetime = custom_field()
    banner_path: str = custom_field()
    chat_security: Union["ChatSecuritySetting", int] = custom_field(converter=enum_converter("ChatSecuritySetting"))
    clan_info: "GroupV2ClanInfoAndInvestment" = custom_field()
    conversation_id: int = custom_field(metadata={"int64": True})
    creation_date: datetime = custom_field()
    default_publicity: Union["GroupPostPublicity", int] = custom_field(converter=enum_converter("GroupPostPublicity"))
    enable_invitation_messaging_for_admins: bool = custom_field()
    features: "GroupFeatures" = custom_field()
    group_id: int = custom_field(metadata={"int64": True})
    group_type: Union["GroupType", int] = custom_field(converter=enum_converter("GroupType"))
    homepage: Union["GroupHomepage", int] = custom_field(converter=enum_converter("GroupHomepage"))
    is_default_post_public: bool = custom_field()
    is_public: bool = custom_field()
    is_public_topic_admin_only: bool = custom_field()
    locale: str = custom_field()
    member_count: int = custom_field()
    membership_id_created: int = custom_field(metadata={"int64": True})
    membership_option: Union["MembershipOption", int] = custom_field(converter=enum_converter("MembershipOption"))
    modification_date: datetime = custom_field()
    motto: str = custom_field()
    name: str = custom_field()
    remote_group_id: int = custom_field(metadata={"int64": True})
    tags: list[str] = custom_field(metadata={"type": """list[str]"""})
    theme: str = custom_field()


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


@custom_define()
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

    capabilities: Union["Capabilities", int] = custom_field(converter=enum_converter("Capabilities"))
    host_guided_game_permission_override: Union["HostGuidedGamesPermissionLevel", int] = custom_field(
        converter=enum_converter("HostGuidedGamesPermissionLevel")
    )
    invite_permission_override: bool = custom_field()
    join_level: Union["RuntimeGroupMemberType", int] = custom_field(converter=enum_converter("RuntimeGroupMemberType"))
    maximum_members: int = custom_field()
    maximum_memberships_of_group_type: int = custom_field()
    membership_types: list[Union["BungieMembershipType", int]] = custom_field(
        converter=enum_converter("BungieMembershipType")
    )
    update_banner_permission_override: bool = custom_field()
    update_culture_permission_override: bool = custom_field()


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


@custom_define()
class GroupV2ClanInfo(BaseModel):
    """
    This contract contains clan-specific group information. It does not include any investment data.

    None
    Attributes:
        clan_banner_data: _No description given by bungie._
        clan_callsign: _No description given by bungie._
    """

    clan_banner_data: "ClanBanner" = custom_field()
    clan_callsign: str = custom_field()


@custom_define()
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

    decal_background_color_id: int = custom_field()
    decal_color_id: int = custom_field()
    decal_id: int = custom_field()
    gonfalon_color_id: int = custom_field()
    gonfalon_detail_color_id: int = custom_field()
    gonfalon_detail_id: int = custom_field()
    gonfalon_id: int = custom_field()


@custom_define()
class GroupV2ClanInfoAndInvestment(BaseModel):
    """
    The same as GroupV2ClanInfo, but includes any investment data.

    None
    Attributes:
        clan_banner_data: _No description given by bungie._
        clan_callsign: _No description given by bungie._
        d2_clan_progressions: _No description given by bungie._
    """

    clan_banner_data: "ClanBanner" = custom_field()
    clan_callsign: str = custom_field()
    d2_clan_progressions: dict[int, "DestinyProgression"] = custom_field(
        metadata={"type": """dict[int, DestinyProgression]"""}
    )


@custom_define()
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

    bungie_net_user_info: "UserInfoCard" = custom_field()
    destiny_user_info: "GroupUserInfoCard" = custom_field()
    group_id: int = custom_field(metadata={"int64": True})
    join_date: datetime = custom_field()


@custom_define()
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

    bungie_net_user_info: "UserInfoCard" = custom_field()
    destiny_user_info: "GroupUserInfoCard" = custom_field()
    group_id: int = custom_field(metadata={"int64": True})
    is_online: bool = custom_field()
    join_date: datetime = custom_field()
    last_online_status_change: int = custom_field(metadata={"int64": True})
    member_type: Union["RuntimeGroupMemberType", int] = custom_field(converter=enum_converter("RuntimeGroupMemberType"))


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


@custom_define()
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

    bungie_net_user_info: "UserInfoCard" = custom_field()
    destiny_user_info: "GroupUserInfoCard" = custom_field()
    group_id: int = custom_field(metadata={"int64": True})
    join_date: datetime = custom_field()
    potential_status: Union["GroupPotentialMemberStatus", int] = custom_field(
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


@custom_define()
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
        remote_group_id: _No description given by bungie._
        theme: _No description given by bungie._
    """

    about: str = custom_field()
    avatar_path: str = custom_field()
    capabilities: Union["Capabilities", int] = custom_field(converter=enum_converter("Capabilities"))
    clan_info: "GroupV2ClanInfo" = custom_field()
    creation_date: datetime = custom_field()
    group_id: int = custom_field(metadata={"int64": True})
    group_type: Union["GroupType", int] = custom_field(converter=enum_converter("GroupType"))
    locale: str = custom_field()
    member_count: int = custom_field()
    membership_option: Union["MembershipOption", int] = custom_field(converter=enum_converter("MembershipOption"))
    motto: str = custom_field()
    name: str = custom_field()
    remote_group_id: int = custom_field(metadata={"int64": True})
    theme: str = custom_field()


@custom_define()
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

    has_more: bool = custom_field()
    query: "PagedQuery" = custom_field()
    replacement_continuation_token: str = custom_field()
    results: list["GroupV2Card"] = custom_field(metadata={"type": """list[GroupV2Card]"""})
    total_results: int = custom_field()
    use_total_results: bool = custom_field()


@custom_define()
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

    creation_date: Union["GroupDateRange", int] = custom_field(converter=enum_converter("GroupDateRange"))
    current_page: int = custom_field()
    group_member_count_filter: int = custom_field()
    group_type: Union["GroupType", int] = custom_field(converter=enum_converter("GroupType"))
    items_per_page: int = custom_field()
    locale_filter: str = custom_field()
    name: str = custom_field()
    request_continuation_token: str = custom_field()
    sort_by: Union["GroupSortBy", int] = custom_field(converter=enum_converter("GroupSortBy"))
    tag_text: str = custom_field()


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


@custom_define()
class GroupNameSearchRequest(BaseModel):
    """
    _No description given by bungie._

    None
    Attributes:
        group_name: _No description given by bungie._
        group_type: _No description given by bungie._
    """

    group_name: str = custom_field()
    group_type: Union["GroupType", int] = custom_field(converter=enum_converter("GroupType"))


@custom_define()
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

    chat_enabled: bool = custom_field()
    chat_name: str = custom_field()
    chat_security: Union["ChatSecuritySetting", int] = custom_field(converter=enum_converter("ChatSecuritySetting"))
    conversation_id: int = custom_field(metadata={"int64": True})
    group_id: int = custom_field(metadata={"int64": True})


@custom_define()
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

    about: str = custom_field()
    allow_chat: bool = custom_field()
    avatar_image_index: int = custom_field()
    callsign: str = custom_field()
    chat_security: int = custom_field()
    default_publicity: int = custom_field()
    enable_invitation_messaging_for_admins: bool = custom_field()
    homepage: int = custom_field()
    is_public: bool = custom_field()
    is_public_topic_admin_only: bool = custom_field()
    locale: str = custom_field()
    membership_option: int = custom_field()
    motto: str = custom_field()
    name: str = custom_field()
    tags: str = custom_field()
    theme: str = custom_field()


@custom_define()
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

    host_guided_game_permission_override: int = custom_field()
    invite_permission_override: bool = custom_field()
    join_level: int = custom_field()
    update_banner_permission_override: bool = custom_field()
    update_culture_permission_override: bool = custom_field()


@custom_define()
class GroupOptionalConversationAddRequest(BaseModel):
    """
    _No description given by bungie._

    None
    Attributes:
        chat_name: _No description given by bungie._
        chat_security: _No description given by bungie._
    """

    chat_name: str = custom_field()
    chat_security: Union["ChatSecuritySetting", int] = custom_field(converter=enum_converter("ChatSecuritySetting"))


@custom_define()
class GroupOptionalConversationEditRequest(BaseModel):
    """
    _No description given by bungie._

    None
    Attributes:
        chat_enabled: _No description given by bungie._
        chat_name: _No description given by bungie._
        chat_security: _No description given by bungie._
    """

    chat_enabled: bool = custom_field()
    chat_name: str = custom_field()
    chat_security: int = custom_field()


@custom_define()
class GroupMemberLeaveResult(BaseModel):
    """
    _No description given by bungie._

    None
    Attributes:
        group: _No description given by bungie._
        group_deleted: _No description given by bungie._
    """

    group: "GroupV2" = custom_field()
    group_deleted: bool = custom_field()


@custom_define()
class GroupBanRequest(BaseModel):
    """
    _No description given by bungie._

    None
    Attributes:
        comment: _No description given by bungie._
        length: _No description given by bungie._
    """

    comment: str = custom_field()
    length: Union["IgnoreLength", int] = custom_field(converter=enum_converter("IgnoreLength"))


@custom_define()
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

    bungie_net_user_info: "UserInfoCard" = custom_field()
    comment: str = custom_field()
    created_by: "UserInfoCard" = custom_field()
    date_banned: datetime = custom_field()
    date_expires: datetime = custom_field()
    destiny_user_info: "GroupUserInfoCard" = custom_field()
    group_id: int = custom_field(metadata={"int64": True})
    last_modified_by: "UserInfoCard" = custom_field()


@custom_define()
class GroupEditHistory(BaseModel, DestinyClanMixin):
    """
    _No description given by bungie._

    None
    Attributes:
        about: _No description given by bungie._
        about_editors: _No description given by bungie._
        clan_callsign: _No description given by bungie._
        clan_callsign_editors: _No description given by bungie._
        edit_date: _No description given by bungie._
        group_editors: _No description given by bungie._
        group_id: _No description given by bungie._
        motto: _No description given by bungie._
        motto_editors: _No description given by bungie._
        name: _No description given by bungie._
        name_editors: _No description given by bungie._
    """

    about: str = custom_field()
    about_editors: int = custom_field(metadata={"int64": True})
    clan_callsign: str = custom_field()
    clan_callsign_editors: int = custom_field(metadata={"int64": True})
    edit_date: datetime = custom_field()
    group_editors: list["UserInfoCard"] = custom_field(metadata={"type": """list[UserInfoCard]"""})
    group_id: int = custom_field(metadata={"int64": True})
    motto: str = custom_field()
    motto_editors: int = custom_field(metadata={"int64": True})
    name: str = custom_field()
    name_editors: int = custom_field(metadata={"int64": True})


@custom_define()
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

    bungie_net_user_info: "UserInfoCard" = custom_field()
    creation_date: datetime = custom_field()
    destiny_user_info: "GroupUserInfoCard" = custom_field()
    group_id: int = custom_field(metadata={"int64": True})
    request_message: str = custom_field()
    resolve_date: datetime = custom_field()
    resolve_message: str = custom_field()
    resolve_state: Union["GroupApplicationResolveState", int] = custom_field(
        converter=enum_converter("GroupApplicationResolveState")
    )
    resolved_by_membership_id: int = custom_field(metadata={"int64": True})


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


@custom_define()
class GroupApplicationRequest(BaseModel):
    """
    _No description given by bungie._

    None
    Attributes:
        message: _No description given by bungie._
    """

    message: str = custom_field()


@custom_define()
class GroupApplicationListRequest(BaseModel):
    """
    _No description given by bungie._

    None
    Attributes:
        memberships: _No description given by bungie._
        message: _No description given by bungie._
    """

    memberships: list["UserMembership"] = custom_field(metadata={"type": """list[UserMembership]"""})
    message: str = custom_field()


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


@custom_define()
class GroupMembershipBase(BaseModel):
    """
    _No description given by bungie._

    None
    Attributes:
        group: _No description given by bungie._
    """

    group: "GroupV2" = custom_field()


@custom_define()
class GroupMembership(BaseModel):
    """
    _No description given by bungie._

    None
    Attributes:
        group: _No description given by bungie._
        member: _No description given by bungie._
    """

    group: "GroupV2" = custom_field()
    member: "GroupMember" = custom_field()


@custom_define()
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

    has_more: bool = custom_field()
    query: "PagedQuery" = custom_field()
    replacement_continuation_token: str = custom_field()
    results: list["GroupMembership"] = custom_field(metadata={"type": """list[GroupMembership]"""})
    total_results: int = custom_field()
    use_total_results: bool = custom_field()


@custom_define()
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

    are_all_memberships_inactive: dict[int, bool] = custom_field(metadata={"type": """dict[int, bool]"""})
    has_more: bool = custom_field()
    query: "PagedQuery" = custom_field()
    replacement_continuation_token: str = custom_field()
    results: list["GroupMembership"] = custom_field(metadata={"type": """list[GroupMembership]"""})
    total_results: int = custom_field()
    use_total_results: bool = custom_field()


@custom_define()
class GroupPotentialMembership(BaseModel):
    """
    _No description given by bungie._

    None
    Attributes:
        group: _No description given by bungie._
        member: _No description given by bungie._
    """

    group: "GroupV2" = custom_field()
    member: "GroupPotentialMember" = custom_field()


@custom_define()
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

    has_more: bool = custom_field()
    query: "PagedQuery" = custom_field()
    replacement_continuation_token: str = custom_field()
    results: list["GroupPotentialMembership"] = custom_field(metadata={"type": """list[GroupPotentialMembership]"""})
    total_results: int = custom_field()
    use_total_results: bool = custom_field()


@custom_define()
class GroupApplicationResponse(BaseModel):
    """
    _No description given by bungie._

    None
    Attributes:
        resolution: _No description given by bungie._
    """

    resolution: Union["GroupApplicationResolveState", int] = custom_field(
        converter=enum_converter("GroupApplicationResolveState")
    )
