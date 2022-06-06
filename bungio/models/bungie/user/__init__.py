import datetime
from typing import TYPE_CHECKING, Any, Optional, Union

import attr

from bungio.models.base import BaseEnum, BaseModel

if TYPE_CHECKING:
    from bungio.models import BungieMembershipType, GroupUserInfoCard, IgnoreResponse


@attr.define
class UserMembership(BaseModel):
    """
    Very basic info about a user as returned by the Account server.

    Attributes:
        membership_type: Type of the membership. Not necessarily the native type.
        membership_id: Membership ID as they user is known in the Accounts service
        display_name: Display Name the player has chosen for themselves. The display name is optional when the data type is used as input to a platform API.
        bungie_global_display_name: The bungie global display name, if set.
        bungie_global_display_name_code: The bungie global display name code, if set.
    """

    membership_type: "BungieMembershipType" = attr.field()
    membership_id: int = attr.field()
    display_name: str = attr.field()
    bungie_global_display_name: str = attr.field()
    bungie_global_display_name_code: int = attr.field()


@attr.define
class CrossSaveUserMembership(BaseModel):
    """
    Very basic info about a user as returned by the Account server, but including CrossSave information. Do NOT use as a request contract.

    Attributes:
        cross_save_override: If there is a cross save override in effect, this value will tell you the type that is overridding this one.
        applicable_membership_types: The list of Membership Types indicating the platforms on which this Membership can be used.  Not in Cross Save = its original membership type. Cross Save Primary = Any membership types it is overridding, and its original membership type Cross Save Overridden = Empty list
        is_public: If True, this is a public user membership.
        membership_type: Type of the membership. Not necessarily the native type.
        membership_id: Membership ID as they user is known in the Accounts service
        display_name: Display Name the player has chosen for themselves. The display name is optional when the data type is used as input to a platform API.
        bungie_global_display_name: The bungie global display name, if set.
        bungie_global_display_name_code: The bungie global display name code, if set.
    """

    cross_save_override: "BungieMembershipType" = attr.field()
    applicable_membership_types: list["BungieMembershipType"] = attr.field()
    is_public: bool = attr.field()
    membership_type: "BungieMembershipType" = attr.field()
    membership_id: int = attr.field()
    display_name: str = attr.field()
    bungie_global_display_name: str = attr.field()
    bungie_global_display_name_code: int = attr.field()


@attr.define
class UserInfoCard(BaseModel):
    """
    This contract supplies basic information commonly used to display a minimal amount of information about a user. Take care to not add more properties here unless the property applies in all (or at least the majority) of the situations where UserInfoCard is used. Avoid adding game specific or platform specific details here. In cases where UserInfoCard is a subset of the data needed in a contract, use UserInfoCard as a property of other contracts.

    Attributes:
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
class GeneralUser(BaseModel):
    """
    _No description given by bungie_

    Attributes:
        membership_id: _No description given by bungie_
        unique_name: _No description given by bungie_
        normalized_name: _No description given by bungie_
        display_name: _No description given by bungie_
        profile_picture: _No description given by bungie_
        profile_theme: _No description given by bungie_
        user_title: _No description given by bungie_
        success_message_flags: _No description given by bungie_
        is_deleted: _No description given by bungie_
        about: _No description given by bungie_
        first_access: _No description given by bungie_
        last_update: _No description given by bungie_
        legacy_portal_u_i_d: _No description given by bungie_
        context: _No description given by bungie_
        psn_display_name: _No description given by bungie_
        xbox_display_name: _No description given by bungie_
        fb_display_name: _No description given by bungie_
        show_activity: _No description given by bungie_
        locale: _No description given by bungie_
        locale_inherit_default: _No description given by bungie_
        last_ban_report_id: _No description given by bungie_
        show_group_messaging: _No description given by bungie_
        profile_picture_path: _No description given by bungie_
        profile_picture_wide_path: _No description given by bungie_
        profile_theme_name: _No description given by bungie_
        user_title_display: _No description given by bungie_
        status_text: _No description given by bungie_
        status_date: _No description given by bungie_
        profile_ban_expire: _No description given by bungie_
        blizzard_display_name: _No description given by bungie_
        steam_display_name: _No description given by bungie_
        stadia_display_name: _No description given by bungie_
        twitch_display_name: _No description given by bungie_
        cached_bungie_global_display_name: _No description given by bungie_
        cached_bungie_global_display_name_code: _No description given by bungie_
    """

    membership_id: int = attr.field()
    unique_name: str = attr.field()
    normalized_name: str = attr.field()
    display_name: str = attr.field()
    profile_picture: int = attr.field()
    profile_theme: int = attr.field()
    user_title: int = attr.field()
    success_message_flags: int = attr.field()
    is_deleted: bool = attr.field()
    about: str = attr.field()
    first_access: datetime.datetime = attr.field()
    last_update: datetime.datetime = attr.field()
    legacy_portal_u_i_d: int = attr.field()
    context: "UserToUserContext" = attr.field()
    psn_display_name: str = attr.field()
    xbox_display_name: str = attr.field()
    fb_display_name: str = attr.field()
    show_activity: bool = attr.field()
    locale: str = attr.field()
    locale_inherit_default: bool = attr.field()
    last_ban_report_id: int = attr.field()
    show_group_messaging: bool = attr.field()
    profile_picture_path: str = attr.field()
    profile_picture_wide_path: str = attr.field()
    profile_theme_name: str = attr.field()
    user_title_display: str = attr.field()
    status_text: str = attr.field()
    status_date: datetime.datetime = attr.field()
    profile_ban_expire: datetime.datetime = attr.field()
    blizzard_display_name: str = attr.field()
    steam_display_name: str = attr.field()
    stadia_display_name: str = attr.field()
    twitch_display_name: str = attr.field()
    cached_bungie_global_display_name: str = attr.field()
    cached_bungie_global_display_name_code: int = attr.field()


@attr.define
class UserToUserContext(BaseModel):
    """
    _No description given by bungie_

    Attributes:
        is_following: _No description given by bungie_
        ignore_status: _No description given by bungie_
        global_ignore_end_date: _No description given by bungie_
    """

    is_following: bool = attr.field()
    ignore_status: "IgnoreResponse" = attr.field()
    global_ignore_end_date: datetime.datetime = attr.field()


@attr.define
class UserMembershipData(BaseModel):
    """
    _No description given by bungie_

    Attributes:
        destiny_memberships: this allows you to see destiny memberships that are visible and linked to this account (regardless of whether or not they have characters on the world server)
        primary_membership_id: If this property is populated, it will have the membership ID of the account considered to be "primary" in this user's cross save relationship.  If null, this user has no cross save relationship, nor primary account.
        bungie_net_user: _No description given by bungie_
    """

    destiny_memberships: list["GroupUserInfoCard"] = attr.field()
    primary_membership_id: int = attr.field()
    bungie_net_user: "GeneralUser" = attr.field()


@attr.define
class HardLinkedUserMembership(BaseModel):
    """
    _No description given by bungie_

    Attributes:
        membership_type: _No description given by bungie_
        membership_id: _No description given by bungie_
        cross_save_overridden_type: _No description given by bungie_
        cross_save_overridden_membership_id: _No description given by bungie_
    """

    membership_type: "BungieMembershipType" = attr.field()
    membership_id: int = attr.field()
    cross_save_overridden_type: "BungieMembershipType" = attr.field()
    cross_save_overridden_membership_id: int = attr.field()


@attr.define
class UserSearchResponse(BaseModel):
    """
    _No description given by bungie_

    Attributes:
        search_results: _No description given by bungie_
        page: _No description given by bungie_
        has_more: _No description given by bungie_
    """

    search_results: list["UserSearchResponseDetail"] = attr.field()
    page: int = attr.field()
    has_more: bool = attr.field()


@attr.define
class UserSearchResponseDetail(BaseModel):
    """
    _No description given by bungie_

    Attributes:
        bungie_global_display_name: _No description given by bungie_
        bungie_global_display_name_code: _No description given by bungie_
        bungie_net_membership_id: _No description given by bungie_
        destiny_memberships: _No description given by bungie_
    """

    bungie_global_display_name: str = attr.field()
    bungie_global_display_name_code: int = attr.field()
    bungie_net_membership_id: int = attr.field()
    destiny_memberships: list["UserInfoCard"] = attr.field()


@attr.define
class UserSearchPrefixRequest(BaseModel):
    """
    _No description given by bungie_

    Attributes:
        display_name_prefix: _No description given by bungie_
    """

    display_name_prefix: str = attr.field()


@attr.define
class ExactSearchRequest(BaseModel):
    """
    _No description given by bungie_

    Attributes:
        display_name: _No description given by bungie_
        display_name_code: _No description given by bungie_
    """

    display_name: str = attr.field()
    display_name_code: int = attr.field()


@attr.define
class EmailSettings(BaseModel):
    """
    The set of all email subscription/opt-in settings and definitions.

    Attributes:
        opt_in_definitions: Keyed by the name identifier of the opt-in definition.
        subscription_definitions: Keyed by the name identifier of the Subscription definition.
        views: Keyed by the name identifier of the View definition.
    """

    opt_in_definitions: Any = attr.field()
    subscription_definitions: Any = attr.field()
    views: Any = attr.field()


@attr.define
class EmailOptInDefinition(BaseModel):
    """
    Defines a single opt-in category: a wide-scoped permission to send emails for the subject related to the opt-in.

    Attributes:
        name: The unique identifier for this opt-in category.
        value: The flag value for this opt-in category. For historical reasons, this is defined as a flags enum.
        set_by_default: If true, this opt-in setting should be set by default in situations where accounts are created without explicit choices about what they're opting into.
        dependent_subscriptions: Information about the dependent subscriptions for this opt-in.
    """

    name: str = attr.field()
    value: "OptInFlags" = attr.field()
    set_by_default: bool = attr.field()
    dependent_subscriptions: list["EmailSubscriptionDefinition"] = attr.field()


class OptInFlags(BaseEnum):
    """
    _No description given by bungie_
    """

    NONE = 0
    """_No description given by bungie_ """
    NEWSLETTER = 1
    """_No description given by bungie_ """
    SYSTEM = 2
    """_No description given by bungie_ """
    MARKETING = 4
    """_No description given by bungie_ """
    USER_RESEARCH = 8
    """_No description given by bungie_ """
    CUSTOMER_SERVICE = 16
    """_No description given by bungie_ """
    SOCIAL = 32
    """_No description given by bungie_ """
    PLAY_TESTS = 64
    """_No description given by bungie_ """
    PLAY_TESTS_LOCAL = 128
    """_No description given by bungie_ """
    CAREERS = 256
    """_No description given by bungie_ """


@attr.define
class EmailSubscriptionDefinition(BaseModel):
    """
    Defines a single subscription: permission to send emails for a specific, focused subject (generally timeboxed, such as for a specific release of a product or feature).

    Attributes:
        name: The unique identifier for this subscription.
        localization: A dictionary of localized text for the EMail Opt-in setting, keyed by the locale.
        value: The bitflag value for this subscription. Should be a unique power of two value.
    """

    name: str = attr.field()
    localization: Any = attr.field()
    value: int = attr.field()


@attr.define
class EMailSettingLocalization(BaseModel):
    """
    Localized text relevant to a given EMail setting in a given localization.

    Attributes:
        title: _No description given by bungie_
        description: _No description given by bungie_
    """

    title: str = attr.field()
    description: str = attr.field()


@attr.define
class EMailSettingSubscriptionLocalization(BaseModel):
    """
    Localized text relevant to a given EMail setting in a given localization. Extra settings specifically for subscriptions.

    Attributes:
        unknown_user_description: _No description given by bungie_
        registered_user_description: _No description given by bungie_
        unregistered_user_description: _No description given by bungie_
        unknown_user_action_text: _No description given by bungie_
        known_user_action_text: _No description given by bungie_
        title: _No description given by bungie_
        description: _No description given by bungie_
    """

    unknown_user_description: str = attr.field()
    registered_user_description: str = attr.field()
    unregistered_user_description: str = attr.field()
    unknown_user_action_text: str = attr.field()
    known_user_action_text: str = attr.field()
    title: str = attr.field()
    description: str = attr.field()


@attr.define
class EmailViewDefinition(BaseModel):
    """
    Represents a data-driven view for Email settings. Web/Mobile UI can use this data to show new EMail settings consistently without further manual work.

    Attributes:
        name: The identifier for this view.
        view_settings: The ordered list of settings to show in this view.
    """

    name: str = attr.field()
    view_settings: list["EmailViewDefinitionSetting"] = attr.field()


@attr.define
class EmailViewDefinitionSetting(BaseModel):
    """
    _No description given by bungie_

    Attributes:
        name: The identifier for this UI Setting, which can be used to relate it to custom strings or other data as desired.
        localization: A dictionary of localized text for the EMail setting, keyed by the locale.
        set_by_default: If true, this setting should be set by default if the user hasn't chosen whether it's set or cleared yet.
        opt_in_aggregate_value: The OptInFlags value to set or clear if this setting is set or cleared in the UI. It is the aggregate of all underlying opt-in flags related to this setting.
        subscriptions: The subscriptions to show as children of this setting, if any.
    """

    name: str = attr.field()
    localization: Any = attr.field()
    set_by_default: bool = attr.field()
    opt_in_aggregate_value: "OptInFlags" = attr.field()
    subscriptions: list["EmailSubscriptionDefinition"] = attr.field()
