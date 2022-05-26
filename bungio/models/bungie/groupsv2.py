import datetime
from typing import TYPE_CHECKING, Any, Optional

import attr

from bungio.models.base import BaseEnum, BaseModel


@attr.define
class GroupUserInfoCard(BaseModel):
    """
       Not specified.

       Attributes:
           last_seen_display_name: This will be the display name the clan server last saw the user as. If the account is an active cross save override, this will be the display name to use. Otherwise, this will match the displayName property.
           last_seen_display_name_type: The platform of the LastSeenDisplayName
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

    last_seen_display_name: str = attr.field()
    last_seen_display_name_type: int = attr.field()
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


@attr.define
class GroupResponse(BaseModel):
    """
    Not specified.

    Attributes:
        detail: Not specified.
        founder: Not specified.
        allied_ids: Not specified.
        parent_group: Not specified.
        alliance_status: Not specified.
        group_join_invite_count: Not specified.
        current_user_memberships_inactive_for_destiny: A convenience property that indicates if every membership you (the current user) have that is a part of this group are part of an account that is considered inactive - for example, overridden accounts in Cross Save.
        current_user_member_map: This property will be populated if the authenticated user is a member of the group. Note that because of account linking, a user can sometimes be part of a clan more than once. As such, this returns the highest member type available.
        current_user_potential_member_map: This property will be populated if the authenticated user is an applicant or has an outstanding invitation to join. Note that because of account linking, a user can sometimes be part of a clan more than once.
    """

    detail: "GroupV2" = attr.field()
    founder: "GroupMember" = attr.field()
    allied_ids: list[int] = attr.field()
    parent_group: "GroupV2" = attr.field()
    alliance_status: int = attr.field()
    group_join_invite_count: int = attr.field()
    current_user_memberships_inactive_for_destiny: bool = attr.field()
    current_user_member_map: Any = attr.field()
    current_user_potential_member_map: Any = attr.field()


@attr.define
class GroupV2(BaseModel):
    """
    Not specified.

    Attributes:
        group_id: Not specified.
        name: Not specified.
        group_type: Not specified.
        membership_id_created: Not specified.
        creation_date: Not specified.
        modification_date: Not specified.
        about: Not specified.
        tags: Not specified.
        member_count: Not specified.
        is_public: Not specified.
        is_public_topic_admin_only: Not specified.
        motto: Not specified.
        allow_chat: Not specified.
        is_default_post_public: Not specified.
        chat_security: Not specified.
        locale: Not specified.
        avatar_image_index: Not specified.
        homepage: Not specified.
        membership_option: Not specified.
        default_publicity: Not specified.
        theme: Not specified.
        banner_path: Not specified.
        avatar_path: Not specified.
        conversation_id: Not specified.
        enable_invitation_messaging_for_admins: Not specified.
        ban_expire_date: Not specified.
        features: Not specified.
        clan_info: Not specified.
    """

    group_id: int = attr.field()
    name: str = attr.field()
    group_type: int = attr.field()
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
    chat_security: int = attr.field()
    locale: str = attr.field()
    avatar_image_index: int = attr.field()
    homepage: int = attr.field()
    membership_option: int = attr.field()
    default_publicity: int = attr.field()
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
    Not specified.
    """

    GENERAL = 0
    """Not specified. """
    CLAN = 1
    """Not specified. """


class ChatSecuritySetting(BaseEnum):
    """
    Not specified.
    """

    GROUP = 0
    """Not specified. """
    ADMINS = 1
    """Not specified. """


class GroupHomepage(BaseEnum):
    """
    Not specified.
    """

    WALL = 0
    """Not specified. """
    FORUM = 1
    """Not specified. """
    ALLIANCE_FORUM = 2
    """Not specified. """


class MembershipOption(BaseEnum):
    """
    Not specified.
    """

    REVIEWED = 0
    """Not specified. """
    OPEN = 1
    """Not specified. """
    CLOSED = 2
    """Not specified. """


class GroupPostPublicity(BaseEnum):
    """
    Not specified.
    """

    PUBLIC = 0
    """Not specified. """
    ALLIANCE = 1
    """Not specified. """
    PRIVATE = 2
    """Not specified. """


@attr.define
class GroupFeatures(BaseModel):
    """
        Not specified.

        Attributes:
            maximum_members: Not specified.
            maximum_memberships_of_group_type: Maximum number of groups of this type a typical membership may join. For example, a user may join about 50 General groups with their Bungie.net account. They may join one clan per Destiny membership.
            capabilities: Not specified.
            membership_types: Not specified.
            invite_permission_override: Minimum Member Level allowed to invite new members to group

    Always Allowed: Founder, Acting Founder

    True means admins have this power, false means they don't

    Default is false for clans, true for groups.
            update_culture_permission_override: Minimum Member Level allowed to update group culture

    Always Allowed: Founder, Acting Founder

    True means admins have this power, false means they don't

    Default is false for clans, true for groups.
            host_guided_game_permission_override: Minimum Member Level allowed to host guided games

    Always Allowed: Founder, Acting Founder, Admin

    Allowed Overrides: None, Member, Beginner

    Default is Member for clans, None for groups, although this means nothing for groups.
            update_banner_permission_override: Minimum Member Level allowed to update banner

    Always Allowed: Founder, Acting Founder

    True means admins have this power, false means they don't

    Default is false for clans, true for groups.
            join_level: Level to join a member at when accepting an invite, application, or joining an open clan

    Default is Beginner.
    """

    maximum_members: int = attr.field()
    maximum_memberships_of_group_type: int = attr.field()
    capabilities: int = attr.field()
    membership_types: list[int] = attr.field()
    invite_permission_override: bool = attr.field()
    update_culture_permission_override: bool = attr.field()
    host_guided_game_permission_override: int = attr.field()
    update_banner_permission_override: bool = attr.field()
    join_level: int = attr.field()


class Capabilities(BaseEnum):
    """
    Not specified.
    """

    NONE = 0
    """Not specified. """
    LEADERBOARDS = 1
    """Not specified. """
    CALLSIGN = 2
    """Not specified. """
    OPTIONAL_CONVERSATIONS = 4
    """Not specified. """
    CLAN_BANNER = 8
    """Not specified. """
    D2_INVESTMENT_DATA = 16
    """Not specified. """
    TAGS = 32
    """Not specified. """
    ALLIANCES = 64
    """Not specified. """


class HostGuidedGamesPermissionLevel(BaseEnum):
    """
    Used for setting the guided game permission level override (admins and founders can always host guided games).
    """

    NONE = 0
    """Not specified. """
    BEGINNER = 1
    """Not specified. """
    MEMBER = 2
    """Not specified. """


class RuntimeGroupMemberType(BaseEnum):
    """
    The member levels used by all V2 Groups API. Individual group types use their own mappings in their native storage (general uses BnetDbGroupMemberType and D2 clans use ClanMemberLevel), but they are all translated to this in the runtime api. These runtime values should NEVER be stored anywhere, so the values can be changed as necessary.
    """

    NONE = 0
    """Not specified. """
    BEGINNER = 1
    """Not specified. """
    MEMBER = 2
    """Not specified. """
    ADMIN = 3
    """Not specified. """
    ACTING_FOUNDER = 4
    """Not specified. """
    FOUNDER = 5
    """Not specified. """


@attr.define
class GroupV2ClanInfo(BaseModel):
    """
    This contract contains clan-specific group information. It does not include any investment data.

    Attributes:
        clan_callsign: Not specified.
        clan_banner_data: Not specified.
    """

    clan_callsign: str = attr.field()
    clan_banner_data: "ClanBanner" = attr.field()


@attr.define
class ClanBanner(BaseModel):
    """
    Not specified.

    Attributes:
        decal_id: Not specified.
        decal_color_id: Not specified.
        decal_background_color_id: Not specified.
        gonfalon_id: Not specified.
        gonfalon_color_id: Not specified.
        gonfalon_detail_id: Not specified.
        gonfalon_detail_color_id: Not specified.
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
        d2_clan_progressions: Not specified.
        clan_callsign: Not specified.
        clan_banner_data: Not specified.
    """

    d2_clan_progressions: Any = attr.field()
    clan_callsign: str = attr.field()
    clan_banner_data: "ClanBanner" = attr.field()


@attr.define
class GroupUserBase(BaseModel):
    """
    Not specified.

    Attributes:
        group_id: Not specified.
        destiny_user_info: Not specified.
        bungie_net_user_info: Not specified.
        join_date: Not specified.
    """

    group_id: int = attr.field()
    destiny_user_info: "GroupUserInfoCard" = attr.field()
    bungie_net_user_info: "UserInfoCard" = attr.field()
    join_date: datetime.datetime = attr.field()


@attr.define
class GroupMember(BaseModel):
    """
    Not specified.

    Attributes:
        member_type: Not specified.
        is_online: Not specified.
        last_online_status_change: Not specified.
        group_id: Not specified.
        destiny_user_info: Not specified.
        bungie_net_user_info: Not specified.
        join_date: Not specified.
    """

    member_type: int = attr.field()
    is_online: bool = attr.field()
    last_online_status_change: int = attr.field()
    group_id: int = attr.field()
    destiny_user_info: "GroupUserInfoCard" = attr.field()
    bungie_net_user_info: "UserInfoCard" = attr.field()
    join_date: datetime.datetime = attr.field()


class GroupAllianceStatus(BaseEnum):
    """
    Not specified.
    """

    UNALLIED = 0
    """Not specified. """
    PARENT = 1
    """Not specified. """
    CHILD = 2
    """Not specified. """


@attr.define
class GroupPotentialMember(BaseModel):
    """
    Not specified.

    Attributes:
        potential_status: Not specified.
        group_id: Not specified.
        destiny_user_info: Not specified.
        bungie_net_user_info: Not specified.
        join_date: Not specified.
    """

    potential_status: int = attr.field()
    group_id: int = attr.field()
    destiny_user_info: "GroupUserInfoCard" = attr.field()
    bungie_net_user_info: "UserInfoCard" = attr.field()
    join_date: datetime.datetime = attr.field()


class GroupPotentialMemberStatus(BaseEnum):
    """
    Not specified.
    """

    NONE = 0
    """Not specified. """
    APPLICANT = 1
    """Not specified. """
    INVITEE = 2
    """Not specified. """


class GroupDateRange(BaseEnum):
    """
    Not specified.
    """

    ALL = 0
    """Not specified. """
    PAST_DAY = 1
    """Not specified. """
    PAST_WEEK = 2
    """Not specified. """
    PAST_MONTH = 3
    """Not specified. """
    PAST_YEAR = 4
    """Not specified. """


@attr.define
class GroupV2Card(BaseModel):
    """
    A small infocard of group information, usually used for when a list of groups are returned

    Attributes:
        group_id: Not specified.
        name: Not specified.
        group_type: Not specified.
        creation_date: Not specified.
        about: Not specified.
        motto: Not specified.
        member_count: Not specified.
        locale: Not specified.
        membership_option: Not specified.
        capabilities: Not specified.
        clan_info: Not specified.
        avatar_path: Not specified.
        theme: Not specified.
    """

    group_id: int = attr.field()
    name: str = attr.field()
    group_type: int = attr.field()
    creation_date: datetime.datetime = attr.field()
    about: str = attr.field()
    motto: str = attr.field()
    member_count: int = attr.field()
    locale: str = attr.field()
    membership_option: int = attr.field()
    capabilities: int = attr.field()
    clan_info: "GroupV2ClanInfo" = attr.field()
    avatar_path: str = attr.field()
    theme: str = attr.field()


@attr.define
class GroupSearchResponse(BaseModel):
    """
        Not specified.

        Attributes:
            results: Not specified.
            total_results: Not specified.
            has_more: Not specified.
            query: Not specified.
            replacement_continuation_token: Not specified.
            use_total_results: If useTotalResults is true, then totalResults represents an accurate count.

    If False, it does not, and may be estimated/only the size of the current page.

    Either way, you should probably always only trust hasMore.

    This is a long-held historical throwback to when we used to do paging with known total results. Those queries toasted our database, and we were left to hastily alter our endpoints and create backward- compatible shims, of which useTotalResults is one.
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
        NOTE: GroupQuery, as of Destiny 2, has essentially two totally different and incompatible "modes".

    If you are querying for a group, you can pass any of the properties below.

    If you are querying for a Clan, you MUST NOT pass any of the following properties (they must be null or undefined in your request, not just empty string/default values):

    - groupMemberCountFilter - localeFilter - tagText

    If you pass these, you will get a useless InvalidParameters error.

        Attributes:
            name: Not specified.
            group_type: Not specified.
            creation_date: Not specified.
            sort_by: Not specified.
            group_member_count_filter: Not specified.
            locale_filter: Not specified.
            tag_text: Not specified.
            items_per_page: Not specified.
            current_page: Not specified.
            request_continuation_token: Not specified.
    """

    name: str = attr.field()
    group_type: int = attr.field()
    creation_date: int = attr.field()
    sort_by: int = attr.field()
    group_member_count_filter: int = attr.field()
    locale_filter: str = attr.field()
    tag_text: str = attr.field()
    items_per_page: int = attr.field()
    current_page: int = attr.field()
    request_continuation_token: str = attr.field()


class GroupSortBy(BaseEnum):
    """
    Not specified.
    """

    NAME = 0
    """Not specified. """
    DATE = 1
    """Not specified. """
    POPULARITY = 2
    """Not specified. """
    ID = 3
    """Not specified. """


class GroupMemberCountFilter(BaseEnum):
    """
    Not specified.
    """

    ALL = 0
    """Not specified. """
    ONE_TO_TEN = 1
    """Not specified. """
    ELEVEN_TO_ONE_HUNDRED = 2
    """Not specified. """
    GREATER_THAN_ONE_HUNDRED = 3
    """Not specified. """


@attr.define
class GroupNameSearchRequest(BaseModel):
    """
    Not specified.

    Attributes:
        group_name: Not specified.
        group_type: Not specified.
    """

    group_name: str = attr.field()
    group_type: int = attr.field()


@attr.define
class GroupOptionalConversation(BaseModel):
    """
    Not specified.

    Attributes:
        group_id: Not specified.
        conversation_id: Not specified.
        chat_enabled: Not specified.
        chat_name: Not specified.
        chat_security: Not specified.
    """

    group_id: int = attr.field()
    conversation_id: int = attr.field()
    chat_enabled: bool = attr.field()
    chat_name: str = attr.field()
    chat_security: int = attr.field()


@attr.define
class GroupEditAction(BaseModel):
    """
    Not specified.

    Attributes:
        name: Not specified.
        about: Not specified.
        motto: Not specified.
        theme: Not specified.
        avatar_image_index: Not specified.
        tags: Not specified.
        is_public: Not specified.
        membership_option: Not specified.
        is_public_topic_admin_only: Not specified.
        allow_chat: Not specified.
        chat_security: Not specified.
        callsign: Not specified.
        locale: Not specified.
        homepage: Not specified.
        enable_invitation_messaging_for_admins: Not specified.
        default_publicity: Not specified.
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
        Not specified.

        Attributes:
            invite_permission_override: Minimum Member Level allowed to invite new members to group

    Always Allowed: Founder, Acting Founder

    True means admins have this power, false means they don't

    Default is false for clans, true for groups.
            update_culture_permission_override: Minimum Member Level allowed to update group culture

    Always Allowed: Founder, Acting Founder

    True means admins have this power, false means they don't

    Default is false for clans, true for groups.
            host_guided_game_permission_override: Minimum Member Level allowed to host guided games

    Always Allowed: Founder, Acting Founder, Admin

    Allowed Overrides: None, Member, Beginner

    Default is Member for clans, None for groups, although this means nothing for groups.
            update_banner_permission_override: Minimum Member Level allowed to update banner

    Always Allowed: Founder, Acting Founder

    True means admins have this power, false means they don't

    Default is false for clans, true for groups.
            join_level: Level to join a member at when accepting an invite, application, or joining an open clan

    Default is Beginner.
    """

    invite_permission_override: bool = attr.field()
    update_culture_permission_override: bool = attr.field()
    host_guided_game_permission_override: int = attr.field()
    update_banner_permission_override: bool = attr.field()
    join_level: int = attr.field()


@attr.define
class GroupOptionalConversationAddRequest(BaseModel):
    """
    Not specified.

    Attributes:
        chat_name: Not specified.
        chat_security: Not specified.
    """

    chat_name: str = attr.field()
    chat_security: int = attr.field()


@attr.define
class GroupOptionalConversationEditRequest(BaseModel):
    """
    Not specified.

    Attributes:
        chat_enabled: Not specified.
        chat_name: Not specified.
        chat_security: Not specified.
    """

    chat_enabled: bool = attr.field()
    chat_name: str = attr.field()
    chat_security: int = attr.field()


@attr.define
class GroupMemberLeaveResult(BaseModel):
    """
    Not specified.

    Attributes:
        group: Not specified.
        group_deleted: Not specified.
    """

    group: "GroupV2" = attr.field()
    group_deleted: bool = attr.field()


@attr.define
class GroupBanRequest(BaseModel):
    """
    Not specified.

    Attributes:
        comment: Not specified.
        length: Not specified.
    """

    comment: str = attr.field()
    length: int = attr.field()


@attr.define
class GroupBan(BaseModel):
    """
    Not specified.

    Attributes:
        group_id: Not specified.
        last_modified_by: Not specified.
        created_by: Not specified.
        date_banned: Not specified.
        date_expires: Not specified.
        comment: Not specified.
        bungie_net_user_info: Not specified.
        destiny_user_info: Not specified.
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
    Not specified.

    Attributes:
        group_id: Not specified.
        creation_date: Not specified.
        resolve_state: Not specified.
        resolve_date: Not specified.
        resolved_by_membership_id: Not specified.
        request_message: Not specified.
        resolve_message: Not specified.
        destiny_user_info: Not specified.
        bungie_net_user_info: Not specified.
    """

    group_id: int = attr.field()
    creation_date: datetime.datetime = attr.field()
    resolve_state: int = attr.field()
    resolve_date: datetime.datetime = attr.field()
    resolved_by_membership_id: int = attr.field()
    request_message: str = attr.field()
    resolve_message: str = attr.field()
    destiny_user_info: "GroupUserInfoCard" = attr.field()
    bungie_net_user_info: "UserInfoCard" = attr.field()


class GroupApplicationResolveState(BaseEnum):
    """
    Not specified.
    """

    UNRESOLVED = 0
    """Not specified. """
    ACCEPTED = 1
    """Not specified. """
    DENIED = 2
    """Not specified. """
    RESCINDED = 3
    """Not specified. """


@attr.define
class GroupApplicationRequest(BaseModel):
    """
    Not specified.

    Attributes:
        message: Not specified.
    """

    message: str = attr.field()


@attr.define
class GroupApplicationListRequest(BaseModel):
    """
    Not specified.

    Attributes:
        memberships: Not specified.
        message: Not specified.
    """

    memberships: list["UserMembership"] = attr.field()
    message: str = attr.field()


class GroupsForMemberFilter(BaseEnum):
    """
    Not specified.
    """

    ALL = 0
    """Not specified. """
    FOUNDED = 1
    """Not specified. """
    NON_FOUNDED = 2
    """Not specified. """


@attr.define
class GroupMembershipBase(BaseModel):
    """
    Not specified.

    Attributes:
        group: Not specified.
    """

    group: "GroupV2" = attr.field()


@attr.define
class GroupMembership(BaseModel):
    """
    Not specified.

    Attributes:
        member: Not specified.
        group: Not specified.
    """

    member: "GroupMember" = attr.field()
    group: "GroupV2" = attr.field()


@attr.define
class GroupMembershipSearchResponse(BaseModel):
    """
        Not specified.

        Attributes:
            results: Not specified.
            total_results: Not specified.
            has_more: Not specified.
            query: Not specified.
            replacement_continuation_token: Not specified.
            use_total_results: If useTotalResults is true, then totalResults represents an accurate count.

    If False, it does not, and may be estimated/only the size of the current page.

    Either way, you should probably always only trust hasMore.

    This is a long-held historical throwback to when we used to do paging with known total results. Those queries toasted our database, and we were left to hastily alter our endpoints and create backward- compatible shims, of which useTotalResults is one.
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
        Not specified.

        Attributes:
            are_all_memberships_inactive: A convenience property that indicates if every membership this user has that is a part of this group are part of an account that is considered inactive - for example, overridden accounts in Cross Save.

     The key is the Group ID for the group being checked, and the value is true if the users' memberships for that group are all inactive.
            results: Not specified.
            total_results: Not specified.
            has_more: Not specified.
            query: Not specified.
            replacement_continuation_token: Not specified.
            use_total_results: If useTotalResults is true, then totalResults represents an accurate count.

    If False, it does not, and may be estimated/only the size of the current page.

    Either way, you should probably always only trust hasMore.

    This is a long-held historical throwback to when we used to do paging with known total results. Those queries toasted our database, and we were left to hastily alter our endpoints and create backward- compatible shims, of which useTotalResults is one.
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
    Not specified.

    Attributes:
        member: Not specified.
        group: Not specified.
    """

    member: "GroupPotentialMember" = attr.field()
    group: "GroupV2" = attr.field()


@attr.define
class GroupPotentialMembershipSearchResponse(BaseModel):
    """
        Not specified.

        Attributes:
            results: Not specified.
            total_results: Not specified.
            has_more: Not specified.
            query: Not specified.
            replacement_continuation_token: Not specified.
            use_total_results: If useTotalResults is true, then totalResults represents an accurate count.

    If False, it does not, and may be estimated/only the size of the current page.

    Either way, you should probably always only trust hasMore.

    This is a long-held historical throwback to when we used to do paging with known total results. Those queries toasted our database, and we were left to hastily alter our endpoints and create backward- compatible shims, of which useTotalResults is one.
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
    Not specified.

    Attributes:
        resolution: Not specified.
    """

    resolution: int = attr.field()
