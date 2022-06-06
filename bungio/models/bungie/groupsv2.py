import datetime
from typing import TYPE_CHECKING, Any

import attr

from bungio.models.base import BaseEnum, BaseModel

if TYPE_CHECKING:
    from bungio.models import (
        BungieMembershipType,
        IgnoreLength,
        PagedQuery,
        UserInfoCard,
        UserMembership,
    )


@attr.define
class GroupUserInfoCard(BaseModel):
    """
    _No description given by bungie_

    Attributes:
        last_seen_display_name: This will be the display name the clan server last saw the user as. If the account is an active cross save override, this will be the display name to use. Otherwise, this will match the displayName property.
        last_seen_display_name_type: The platform of the LastSeenDisplayName
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

    last_seen_display_name: str = attr.field()
    last_seen_display_name_type: "BungieMembershipType" = attr.field()
    supplemental_display_name: str = attr.field()
    icon_path: str = attr.field()
    cross_save_override: "BungieMembershipType" = attr.field()
    applicable_membership_types: list["BungieMembershipType"] = attr.field()
    is_public: bool = attr.field()
    membership_type: "BungieMembershipType" = attr.field()
    membership_id: int = attr.field()
    display_name: str = attr.field()
    bungie_global_display_name: str = attr.field()
    bungie_global_display_name_code: int = attr.field()


@attr.define
class GroupResponse(BaseModel):
    """
    _No description given by bungie_

    Attributes:
        detail: _No description given by bungie_
        founder: _No description given by bungie_
        allied_ids: _No description given by bungie_
        parent_group: _No description given by bungie_
        alliance_status: _No description given by bungie_
        group_join_invite_count: _No description given by bungie_
        current_user_memberships_inactive_for_destiny: A convenience property that indicates if every membership you (the current user) have that is a part of this group are part of an account that is considered inactive - for example, overridden accounts in Cross Save.
        current_user_member_map: This property will be populated if the authenticated user is a member of the group. Note that because of account linking, a user can sometimes be part of a clan more than once. As such, this returns the highest member type available.
        current_user_potential_member_map: This property will be populated if the authenticated user is an applicant or has an outstanding invitation to join. Note that because of account linking, a user can sometimes be part of a clan more than once.
    """

    detail: "GroupV2" = attr.field()
    founder: "GroupMember" = attr.field()
    allied_ids: list[int] = attr.field()
    parent_group: "GroupV2" = attr.field()
    alliance_status: "GroupAllianceStatus" = attr.field()
    group_join_invite_count: int = attr.field()
    current_user_memberships_inactive_for_destiny: bool = attr.field()
    current_user_member_map: Any = attr.field()
    current_user_potential_member_map: Any = attr.field()


@attr.define
class GroupV2(BaseModel):
    """
    _No description given by bungie_

    Attributes:
        group_id: _No description given by bungie_
        name: _No description given by bungie_
        group_type: _No description given by bungie_
        membership_id_created: _No description given by bungie_
        creation_date: _No description given by bungie_
        modification_date: _No description given by bungie_
        about: _No description given by bungie_
        tags: _No description given by bungie_
        member_count: _No description given by bungie_
        is_public: _No description given by bungie_
        is_public_topic_admin_only: _No description given by bungie_
        motto: _No description given by bungie_
        allow_chat: _No description given by bungie_
        is_default_post_public: _No description given by bungie_
        chat_security: _No description given by bungie_
        locale: _No description given by bungie_
        avatar_image_index: _No description given by bungie_
        homepage: _No description given by bungie_
        membership_option: _No description given by bungie_
        default_publicity: _No description given by bungie_
        theme: _No description given by bungie_
        banner_path: _No description given by bungie_
        avatar_path: _No description given by bungie_
        conversation_id: _No description given by bungie_
        enable_invitation_messaging_for_admins: _No description given by bungie_
        ban_expire_date: _No description given by bungie_
        features: _No description given by bungie_
        clan_info: _No description given by bungie_
    """

    group_id: int = attr.field()
    name: str = attr.field()
    group_type: "GroupType" = attr.field()
    membership_id_created: int = attr.field()
    creation_date: datetime.datetime = attr.field()
    modification_date: datetime.datetime = attr.field()
    about: str = attr.field()
    tags: list[str] = attr.field()
    member_count: int = attr.field()
    is_public: bool = attr.field()
    is_public_topic_admin_only: bool = attr.field()
    motto: str = attr.field()
    allow_chat: bool = attr.field()
    is_default_post_public: bool = attr.field()
    chat_security: "ChatSecuritySetting" = attr.field()
    locale: str = attr.field()
    avatar_image_index: int = attr.field()
    homepage: "GroupHomepage" = attr.field()
    membership_option: "MembershipOption" = attr.field()
    default_publicity: "GroupPostPublicity" = attr.field()
    theme: str = attr.field()
    banner_path: str = attr.field()
    avatar_path: str = attr.field()
    conversation_id: int = attr.field()
    enable_invitation_messaging_for_admins: bool = attr.field()
    ban_expire_date: datetime.datetime = attr.field()
    features: "GroupFeatures" = attr.field()
    clan_info: "GroupV2ClanInfoAndInvestment" = attr.field()


class GroupType(BaseEnum):
    """
    _No description given by bungie_
    """

    GENERAL = 0
    """_No description given by bungie_ """
    CLAN = 1
    """_No description given by bungie_ """


class ChatSecuritySetting(BaseEnum):
    """
    _No description given by bungie_
    """

    GROUP = 0
    """_No description given by bungie_ """
    ADMINS = 1
    """_No description given by bungie_ """


class GroupHomepage(BaseEnum):
    """
    _No description given by bungie_
    """

    WALL = 0
    """_No description given by bungie_ """
    FORUM = 1
    """_No description given by bungie_ """
    ALLIANCE_FORUM = 2
    """_No description given by bungie_ """


class MembershipOption(BaseEnum):
    """
    _No description given by bungie_
    """

    REVIEWED = 0
    """_No description given by bungie_ """
    OPEN = 1
    """_No description given by bungie_ """
    CLOSED = 2
    """_No description given by bungie_ """


class GroupPostPublicity(BaseEnum):
    """
    _No description given by bungie_
    """

    PUBLIC = 0
    """_No description given by bungie_ """
    ALLIANCE = 1
    """_No description given by bungie_ """
    PRIVATE = 2
    """_No description given by bungie_ """


@attr.define
class GroupFeatures(BaseModel):
    """
    _No description given by bungie_

    Attributes:
        maximum_members: _No description given by bungie_
        maximum_memberships_of_group_type: Maximum number of groups of this type a typical membership may join. For example, a user may join about 50 General groups with their Bungie.net account. They may join one clan per Destiny membership.
        capabilities: _No description given by bungie_
        membership_types: _No description given by bungie_
        invite_permission_override: Minimum Member Level allowed to invite new members to group Always Allowed: Founder, Acting Founder True means admins have this power, false means they don't Default is false for clans, true for groups.
        update_culture_permission_override: Minimum Member Level allowed to update group culture Always Allowed: Founder, Acting Founder True means admins have this power, false means they don't Default is false for clans, true for groups.
        host_guided_game_permission_override: Minimum Member Level allowed to host guided games Always Allowed: Founder, Acting Founder, Admin Allowed Overrides: None, Member, Beginner Default is Member for clans, None for groups, although this means nothing for groups.
        update_banner_permission_override: Minimum Member Level allowed to update banner Always Allowed: Founder, Acting Founder True means admins have this power, false means they don't Default is false for clans, true for groups.
        join_level: Level to join a member at when accepting an invite, application, or joining an open clan Default is Beginner.
    """

    maximum_members: int = attr.field()
    maximum_memberships_of_group_type: int = attr.field()
    capabilities: "Capabilities" = attr.field()
    membership_types: list["BungieMembershipType"] = attr.field()
    invite_permission_override: bool = attr.field()
    update_culture_permission_override: bool = attr.field()
    host_guided_game_permission_override: "HostGuidedGamesPermissionLevel" = attr.field()
    update_banner_permission_override: bool = attr.field()
    join_level: "RuntimeGroupMemberType" = attr.field()


class Capabilities(BaseEnum):
    """
    _No description given by bungie_
    """

    NONE = 0
    """_No description given by bungie_ """
    LEADERBOARDS = 1
    """_No description given by bungie_ """
    CALLSIGN = 2
    """_No description given by bungie_ """
    OPTIONAL_CONVERSATIONS = 4
    """_No description given by bungie_ """
    CLAN_BANNER = 8
    """_No description given by bungie_ """
    D2_INVESTMENT_DATA = 16
    """_No description given by bungie_ """
    TAGS = 32
    """_No description given by bungie_ """
    ALLIANCES = 64
    """_No description given by bungie_ """


class HostGuidedGamesPermissionLevel(BaseEnum):
    """
    Used for setting the guided game permission level override (admins and founders can always host guided games).
    """

    NONE = 0
    """_No description given by bungie_ """
    BEGINNER = 1
    """_No description given by bungie_ """
    MEMBER = 2
    """_No description given by bungie_ """


class RuntimeGroupMemberType(BaseEnum):
    """
    The member levels used by all V2 Groups API. Individual group types use their own mappings in their native storage (general uses BnetDbGroupMemberType and D2 clans use ClanMemberLevel), but they are all translated to this in the runtime api. These runtime values should NEVER be stored anywhere, so the values can be changed as necessary.
    """

    NONE = 0
    """_No description given by bungie_ """
    BEGINNER = 1
    """_No description given by bungie_ """
    MEMBER = 2
    """_No description given by bungie_ """
    ADMIN = 3
    """_No description given by bungie_ """
    ACTING_FOUNDER = 4
    """_No description given by bungie_ """
    FOUNDER = 5
    """_No description given by bungie_ """


@attr.define
class GroupV2ClanInfo(BaseModel):
    """
    This contract contains clan-specific group information. It does not include any investment data.

    Attributes:
        clan_callsign: _No description given by bungie_
        clan_banner_data: _No description given by bungie_
    """

    clan_callsign: str = attr.field()
    clan_banner_data: "ClanBanner" = attr.field()


@attr.define
class ClanBanner(BaseModel):
    """
    _No description given by bungie_

    Attributes:
        decal_id: _No description given by bungie_
        decal_color_id: _No description given by bungie_
        decal_background_color_id: _No description given by bungie_
        gonfalon_id: _No description given by bungie_
        gonfalon_color_id: _No description given by bungie_
        gonfalon_detail_id: _No description given by bungie_
        gonfalon_detail_color_id: _No description given by bungie_
    """

    decal_id: int = attr.field()
    decal_color_id: int = attr.field()
    decal_background_color_id: int = attr.field()
    gonfalon_id: int = attr.field()
    gonfalon_color_id: int = attr.field()
    gonfalon_detail_id: int = attr.field()
    gonfalon_detail_color_id: int = attr.field()


@attr.define
class GroupV2ClanInfoAndInvestment(BaseModel):
    """
    The same as GroupV2ClanInfo, but includes any investment data.

    Attributes:
        d2_clan_progressions: _No description given by bungie_
        clan_callsign: _No description given by bungie_
        clan_banner_data: _No description given by bungie_
    """

    d2_clan_progressions: Any = attr.field()
    clan_callsign: str = attr.field()
    clan_banner_data: "ClanBanner" = attr.field()


@attr.define
class GroupUserBase(BaseModel):
    """
    _No description given by bungie_

    Attributes:
        group_id: _No description given by bungie_
        destiny_user_info: _No description given by bungie_
        bungie_net_user_info: _No description given by bungie_
        join_date: _No description given by bungie_
    """

    group_id: int = attr.field()
    destiny_user_info: "GroupUserInfoCard" = attr.field()
    bungie_net_user_info: "UserInfoCard" = attr.field()
    join_date: datetime.datetime = attr.field()


@attr.define
class GroupMember(BaseModel):
    """
    _No description given by bungie_

    Attributes:
        member_type: _No description given by bungie_
        is_online: _No description given by bungie_
        last_online_status_change: _No description given by bungie_
        group_id: _No description given by bungie_
        destiny_user_info: _No description given by bungie_
        bungie_net_user_info: _No description given by bungie_
        join_date: _No description given by bungie_
    """

    member_type: "RuntimeGroupMemberType" = attr.field()
    is_online: bool = attr.field()
    last_online_status_change: int = attr.field()
    group_id: int = attr.field()
    destiny_user_info: "GroupUserInfoCard" = attr.field()
    bungie_net_user_info: "UserInfoCard" = attr.field()
    join_date: datetime.datetime = attr.field()


class GroupAllianceStatus(BaseEnum):
    """
    _No description given by bungie_
    """

    UNALLIED = 0
    """_No description given by bungie_ """
    PARENT = 1
    """_No description given by bungie_ """
    CHILD = 2
    """_No description given by bungie_ """


@attr.define
class GroupPotentialMember(BaseModel):
    """
    _No description given by bungie_

    Attributes:
        potential_status: _No description given by bungie_
        group_id: _No description given by bungie_
        destiny_user_info: _No description given by bungie_
        bungie_net_user_info: _No description given by bungie_
        join_date: _No description given by bungie_
    """

    potential_status: "GroupPotentialMemberStatus" = attr.field()
    group_id: int = attr.field()
    destiny_user_info: "GroupUserInfoCard" = attr.field()
    bungie_net_user_info: "UserInfoCard" = attr.field()
    join_date: datetime.datetime = attr.field()


class GroupPotentialMemberStatus(BaseEnum):
    """
    _No description given by bungie_
    """

    NONE = 0
    """_No description given by bungie_ """
    APPLICANT = 1
    """_No description given by bungie_ """
    INVITEE = 2
    """_No description given by bungie_ """


class GroupDateRange(BaseEnum):
    """
    _No description given by bungie_
    """

    ALL = 0
    """_No description given by bungie_ """
    PAST_DAY = 1
    """_No description given by bungie_ """
    PAST_WEEK = 2
    """_No description given by bungie_ """
    PAST_MONTH = 3
    """_No description given by bungie_ """
    PAST_YEAR = 4
    """_No description given by bungie_ """


@attr.define
class GroupV2Card(BaseModel):
    """
    A small infocard of group information, usually used for when a list of groups are returned

    Attributes:
        group_id: _No description given by bungie_
        name: _No description given by bungie_
        group_type: _No description given by bungie_
        creation_date: _No description given by bungie_
        about: _No description given by bungie_
        motto: _No description given by bungie_
        member_count: _No description given by bungie_
        locale: _No description given by bungie_
        membership_option: _No description given by bungie_
        capabilities: _No description given by bungie_
        clan_info: _No description given by bungie_
        avatar_path: _No description given by bungie_
        theme: _No description given by bungie_
    """

    group_id: int = attr.field()
    name: str = attr.field()
    group_type: "GroupType" = attr.field()
    creation_date: datetime.datetime = attr.field()
    about: str = attr.field()
    motto: str = attr.field()
    member_count: int = attr.field()
    locale: str = attr.field()
    membership_option: "MembershipOption" = attr.field()
    capabilities: "Capabilities" = attr.field()
    clan_info: "GroupV2ClanInfo" = attr.field()
    avatar_path: str = attr.field()
    theme: str = attr.field()


@attr.define
class GroupSearchResponse(BaseModel):
    """
    _No description given by bungie_

    Attributes:
        results: _No description given by bungie_
        total_results: _No description given by bungie_
        has_more: _No description given by bungie_
        query: _No description given by bungie_
        replacement_continuation_token: _No description given by bungie_
        use_total_results: If useTotalResults is true, then totalResults represents an accurate count. If False, it does not, and may be estimated/only the size of the current page. Either way, you should probably always only trust hasMore. This is a long-held historical throwback to when we used to do paging with known total results. Those queries toasted our database, and we were left to hastily alter our endpoints and create backward- compatible shims, of which useTotalResults is one.
    """

    results: list["GroupV2Card"] = attr.field()
    total_results: int = attr.field()
    has_more: bool = attr.field()
    query: "PagedQuery" = attr.field()
    replacement_continuation_token: str = attr.field()
    use_total_results: bool = attr.field()


@attr.define
class GroupQuery(BaseModel):
    """
    NOTE: GroupQuery, as of Destiny 2, has essentially two totally different and incompatible "modes". If you are querying for a group, you can pass any of the properties below. If you are querying for a Clan, you MUST NOT pass any of the following properties (they must be null or undefined in your request, not just empty string/default values): - groupMemberCountFilter - localeFilter - tagText If you pass these, you will get a useless InvalidParameters error.

    Attributes:
        name: _No description given by bungie_
        group_type: _No description given by bungie_
        creation_date: _No description given by bungie_
        sort_by: _No description given by bungie_
        group_member_count_filter: _No description given by bungie_
        locale_filter: _No description given by bungie_
        tag_text: _No description given by bungie_
        items_per_page: _No description given by bungie_
        current_page: _No description given by bungie_
        request_continuation_token: _No description given by bungie_
    """

    name: str = attr.field()
    group_type: "GroupType" = attr.field()
    creation_date: "GroupDateRange" = attr.field()
    sort_by: "GroupSortBy" = attr.field()
    group_member_count_filter: int = attr.field()
    locale_filter: str = attr.field()
    tag_text: str = attr.field()
    items_per_page: int = attr.field()
    current_page: int = attr.field()
    request_continuation_token: str = attr.field()


class GroupSortBy(BaseEnum):
    """
    _No description given by bungie_
    """

    NAME = 0
    """_No description given by bungie_ """
    DATE = 1
    """_No description given by bungie_ """
    POPULARITY = 2
    """_No description given by bungie_ """
    ID = 3
    """_No description given by bungie_ """


class GroupMemberCountFilter(BaseEnum):
    """
    _No description given by bungie_
    """

    ALL = 0
    """_No description given by bungie_ """
    ONE_TO_TEN = 1
    """_No description given by bungie_ """
    ELEVEN_TO_ONE_HUNDRED = 2
    """_No description given by bungie_ """
    GREATER_THAN_ONE_HUNDRED = 3
    """_No description given by bungie_ """


@attr.define
class GroupNameSearchRequest(BaseModel):
    """
    _No description given by bungie_

    Attributes:
        group_name: _No description given by bungie_
        group_type: _No description given by bungie_
    """

    group_name: str = attr.field()
    group_type: "GroupType" = attr.field()


@attr.define
class GroupOptionalConversation(BaseModel):
    """
    _No description given by bungie_

    Attributes:
        group_id: _No description given by bungie_
        conversation_id: _No description given by bungie_
        chat_enabled: _No description given by bungie_
        chat_name: _No description given by bungie_
        chat_security: _No description given by bungie_
    """

    group_id: int = attr.field()
    conversation_id: int = attr.field()
    chat_enabled: bool = attr.field()
    chat_name: str = attr.field()
    chat_security: "ChatSecuritySetting" = attr.field()


@attr.define
class GroupEditAction(BaseModel):
    """
    _No description given by bungie_

    Attributes:
        name: _No description given by bungie_
        about: _No description given by bungie_
        motto: _No description given by bungie_
        theme: _No description given by bungie_
        avatar_image_index: _No description given by bungie_
        tags: _No description given by bungie_
        is_public: _No description given by bungie_
        membership_option: _No description given by bungie_
        is_public_topic_admin_only: _No description given by bungie_
        allow_chat: _No description given by bungie_
        chat_security: _No description given by bungie_
        callsign: _No description given by bungie_
        locale: _No description given by bungie_
        homepage: _No description given by bungie_
        enable_invitation_messaging_for_admins: _No description given by bungie_
        default_publicity: _No description given by bungie_
    """

    name: str = attr.field()
    about: str = attr.field()
    motto: str = attr.field()
    theme: str = attr.field()
    avatar_image_index: int = attr.field()
    tags: str = attr.field()
    is_public: bool = attr.field()
    membership_option: int = attr.field()
    is_public_topic_admin_only: bool = attr.field()
    allow_chat: bool = attr.field()
    chat_security: int = attr.field()
    callsign: str = attr.field()
    locale: str = attr.field()
    homepage: int = attr.field()
    enable_invitation_messaging_for_admins: bool = attr.field()
    default_publicity: int = attr.field()


@attr.define
class GroupOptionsEditAction(BaseModel):
    """
    _No description given by bungie_

    Attributes:
        invite_permission_override: Minimum Member Level allowed to invite new members to group Always Allowed: Founder, Acting Founder True means admins have this power, false means they don't Default is false for clans, true for groups.
        update_culture_permission_override: Minimum Member Level allowed to update group culture Always Allowed: Founder, Acting Founder True means admins have this power, false means they don't Default is false for clans, true for groups.
        host_guided_game_permission_override: Minimum Member Level allowed to host guided games Always Allowed: Founder, Acting Founder, Admin Allowed Overrides: None, Member, Beginner Default is Member for clans, None for groups, although this means nothing for groups.
        update_banner_permission_override: Minimum Member Level allowed to update banner Always Allowed: Founder, Acting Founder True means admins have this power, false means they don't Default is false for clans, true for groups.
        join_level: Level to join a member at when accepting an invite, application, or joining an open clan Default is Beginner.
    """

    invite_permission_override: bool = attr.field()
    update_culture_permission_override: bool = attr.field()
    host_guided_game_permission_override: int = attr.field()
    update_banner_permission_override: bool = attr.field()
    join_level: int = attr.field()


@attr.define
class GroupOptionalConversationAddRequest(BaseModel):
    """
    _No description given by bungie_

    Attributes:
        chat_name: _No description given by bungie_
        chat_security: _No description given by bungie_
    """

    chat_name: str = attr.field()
    chat_security: "ChatSecuritySetting" = attr.field()


@attr.define
class GroupOptionalConversationEditRequest(BaseModel):
    """
    _No description given by bungie_

    Attributes:
        chat_enabled: _No description given by bungie_
        chat_name: _No description given by bungie_
        chat_security: _No description given by bungie_
    """

    chat_enabled: bool = attr.field()
    chat_name: str = attr.field()
    chat_security: int = attr.field()


@attr.define
class GroupMemberLeaveResult(BaseModel):
    """
    _No description given by bungie_

    Attributes:
        group: _No description given by bungie_
        group_deleted: _No description given by bungie_
    """

    group: "GroupV2" = attr.field()
    group_deleted: bool = attr.field()


@attr.define
class GroupBanRequest(BaseModel):
    """
    _No description given by bungie_

    Attributes:
        comment: _No description given by bungie_
        length: _No description given by bungie_
    """

    comment: str = attr.field()
    length: "IgnoreLength" = attr.field()


@attr.define
class GroupBan(BaseModel):
    """
    _No description given by bungie_

    Attributes:
        group_id: _No description given by bungie_
        last_modified_by: _No description given by bungie_
        created_by: _No description given by bungie_
        date_banned: _No description given by bungie_
        date_expires: _No description given by bungie_
        comment: _No description given by bungie_
        bungie_net_user_info: _No description given by bungie_
        destiny_user_info: _No description given by bungie_
    """

    group_id: int = attr.field()
    last_modified_by: "UserInfoCard" = attr.field()
    created_by: "UserInfoCard" = attr.field()
    date_banned: datetime.datetime = attr.field()
    date_expires: datetime.datetime = attr.field()
    comment: str = attr.field()
    bungie_net_user_info: "UserInfoCard" = attr.field()
    destiny_user_info: "GroupUserInfoCard" = attr.field()


@attr.define
class GroupMemberApplication(BaseModel):
    """
    _No description given by bungie_

    Attributes:
        group_id: _No description given by bungie_
        creation_date: _No description given by bungie_
        resolve_state: _No description given by bungie_
        resolve_date: _No description given by bungie_
        resolved_by_membership_id: _No description given by bungie_
        request_message: _No description given by bungie_
        resolve_message: _No description given by bungie_
        destiny_user_info: _No description given by bungie_
        bungie_net_user_info: _No description given by bungie_
    """

    group_id: int = attr.field()
    creation_date: datetime.datetime = attr.field()
    resolve_state: "GroupApplicationResolveState" = attr.field()
    resolve_date: datetime.datetime = attr.field()
    resolved_by_membership_id: int = attr.field()
    request_message: str = attr.field()
    resolve_message: str = attr.field()
    destiny_user_info: "GroupUserInfoCard" = attr.field()
    bungie_net_user_info: "UserInfoCard" = attr.field()


class GroupApplicationResolveState(BaseEnum):
    """
    _No description given by bungie_
    """

    UNRESOLVED = 0
    """_No description given by bungie_ """
    ACCEPTED = 1
    """_No description given by bungie_ """
    DENIED = 2
    """_No description given by bungie_ """
    RESCINDED = 3
    """_No description given by bungie_ """


@attr.define
class GroupApplicationRequest(BaseModel):
    """
    _No description given by bungie_

    Attributes:
        message: _No description given by bungie_
    """

    message: str = attr.field()


@attr.define
class GroupApplicationListRequest(BaseModel):
    """
    _No description given by bungie_

    Attributes:
        memberships: _No description given by bungie_
        message: _No description given by bungie_
    """

    memberships: list["UserMembership"] = attr.field()
    message: str = attr.field()


class GroupsForMemberFilter(BaseEnum):
    """
    _No description given by bungie_
    """

    ALL = 0
    """_No description given by bungie_ """
    FOUNDED = 1
    """_No description given by bungie_ """
    NON_FOUNDED = 2
    """_No description given by bungie_ """


@attr.define
class GroupMembershipBase(BaseModel):
    """
    _No description given by bungie_

    Attributes:
        group: _No description given by bungie_
    """

    group: "GroupV2" = attr.field()


@attr.define
class GroupMembership(BaseModel):
    """
    _No description given by bungie_

    Attributes:
        member: _No description given by bungie_
        group: _No description given by bungie_
    """

    member: "GroupMember" = attr.field()
    group: "GroupV2" = attr.field()


@attr.define
class GroupMembershipSearchResponse(BaseModel):
    """
    _No description given by bungie_

    Attributes:
        results: _No description given by bungie_
        total_results: _No description given by bungie_
        has_more: _No description given by bungie_
        query: _No description given by bungie_
        replacement_continuation_token: _No description given by bungie_
        use_total_results: If useTotalResults is true, then totalResults represents an accurate count. If False, it does not, and may be estimated/only the size of the current page. Either way, you should probably always only trust hasMore. This is a long-held historical throwback to when we used to do paging with known total results. Those queries toasted our database, and we were left to hastily alter our endpoints and create backward- compatible shims, of which useTotalResults is one.
    """

    results: list["GroupMembership"] = attr.field()
    total_results: int = attr.field()
    has_more: bool = attr.field()
    query: "PagedQuery" = attr.field()
    replacement_continuation_token: str = attr.field()
    use_total_results: bool = attr.field()


@attr.define
class GetGroupsForMemberResponse(BaseModel):
    """
    _No description given by bungie_

    Attributes:
        are_all_memberships_inactive: A convenience property that indicates if every membership this user has that is a part of this group are part of an account that is considered inactive - for example, overridden accounts in Cross Save.  The key is the Group ID for the group being checked, and the value is true if the users' memberships for that group are all inactive.
        results: _No description given by bungie_
        total_results: _No description given by bungie_
        has_more: _No description given by bungie_
        query: _No description given by bungie_
        replacement_continuation_token: _No description given by bungie_
        use_total_results: If useTotalResults is true, then totalResults represents an accurate count. If False, it does not, and may be estimated/only the size of the current page. Either way, you should probably always only trust hasMore. This is a long-held historical throwback to when we used to do paging with known total results. Those queries toasted our database, and we were left to hastily alter our endpoints and create backward- compatible shims, of which useTotalResults is one.
    """

    are_all_memberships_inactive: Any = attr.field()
    results: list["GroupMembership"] = attr.field()
    total_results: int = attr.field()
    has_more: bool = attr.field()
    query: "PagedQuery" = attr.field()
    replacement_continuation_token: str = attr.field()
    use_total_results: bool = attr.field()


@attr.define
class GroupPotentialMembership(BaseModel):
    """
    _No description given by bungie_

    Attributes:
        member: _No description given by bungie_
        group: _No description given by bungie_
    """

    member: "GroupPotentialMember" = attr.field()
    group: "GroupV2" = attr.field()


@attr.define
class GroupPotentialMembershipSearchResponse(BaseModel):
    """
    _No description given by bungie_

    Attributes:
        results: _No description given by bungie_
        total_results: _No description given by bungie_
        has_more: _No description given by bungie_
        query: _No description given by bungie_
        replacement_continuation_token: _No description given by bungie_
        use_total_results: If useTotalResults is true, then totalResults represents an accurate count. If False, it does not, and may be estimated/only the size of the current page. Either way, you should probably always only trust hasMore. This is a long-held historical throwback to when we used to do paging with known total results. Those queries toasted our database, and we were left to hastily alter our endpoints and create backward- compatible shims, of which useTotalResults is one.
    """

    results: list["GroupPotentialMembership"] = attr.field()
    total_results: int = attr.field()
    has_more: bool = attr.field()
    query: "PagedQuery" = attr.field()
    replacement_continuation_token: str = attr.field()
    use_total_results: bool = attr.field()


@attr.define
class GroupApplicationResponse(BaseModel):
    """
    _No description given by bungie_

    Attributes:
        resolution: _No description given by bungie_
    """

    resolution: "GroupApplicationResolveState" = attr.field()
