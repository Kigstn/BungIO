# DO NOT CHANGE ANY CODE BELOW
# This file is generated automatically by `generate_api_schema.py` and will be overwritten
# Instead, change functions / models by subclassing them in the `./overwrites/` folder. They will be used instead.

from datetime import datetime
from typing import TYPE_CHECKING, Any, Optional, Union

import attr

from bungio.models.base import BaseEnum, BaseFlagEnum, BaseModel, ManifestModel
from bungio.models.mixins import DestinyUserMixin
from bungio.utils import enum_converter

if TYPE_CHECKING:
    from bungio.models import BungieMembershipType, GroupUserInfoCard, IgnoreResponse


@attr.define
class UserMembership(BaseModel, DestinyUserMixin):
    """
    Very basic info about a user as returned by the Account server.

    None
    Attributes:
        bungie_global_display_name: The bungie global display name, if set.
        bungie_global_display_name_code: The bungie global display name code, if set.
        display_name: Display Name the player has chosen for themselves. The display name is optional when the data type is used as input to a platform API.
        membership_id: Membership ID as they user is known in the Accounts service
        membership_type: Type of the membership. Not necessarily the native type.
    """

    bungie_global_display_name: str = attr.field()
    bungie_global_display_name_code: int = attr.field()
    display_name: str = attr.field()
    membership_id: int = attr.field()
    membership_type: Union["BungieMembershipType", int] = attr.field(converter=enum_converter("BungieMembershipType"))


@attr.define
class CrossSaveUserMembership(BaseModel, DestinyUserMixin):
    """
    Very basic info about a user as returned by the Account server, but including CrossSave information. Do NOT use as a request contract.

    None
    Attributes:
        applicable_membership_types: The list of Membership Types indicating the platforms on which this Membership can be used.  Not in Cross Save = its original membership type. Cross Save Primary = Any membership types it is overridding, and its original membership type Cross Save Overridden = Empty list
        bungie_global_display_name: The bungie global display name, if set.
        bungie_global_display_name_code: The bungie global display name code, if set.
        cross_save_override: If there is a cross save override in effect, this value will tell you the type that is overridding this one.
        display_name: Display Name the player has chosen for themselves. The display name is optional when the data type is used as input to a platform API.
        is_public: If True, this is a public user membership.
        membership_id: Membership ID as they user is known in the Accounts service
        membership_type: Type of the membership. Not necessarily the native type.
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
    is_public: bool = attr.field()
    membership_id: int = attr.field()
    membership_type: Union["BungieMembershipType", int] = attr.field(converter=enum_converter("BungieMembershipType"))


@attr.define
class UserInfoCard(BaseModel, DestinyUserMixin):
    """
    This contract supplies basic information commonly used to display a minimal amount of information about a user. Take care to not add more properties here unless the property applies in all (or at least the majority) of the situations where UserInfoCard is used. Avoid adding game specific or platform specific details here. In cases where UserInfoCard is a subset of the data needed in a contract, use UserInfoCard as a property of other contracts.

    None
    Attributes:
        applicable_membership_types: The list of Membership Types indicating the platforms on which this Membership can be used.  Not in Cross Save = its original membership type. Cross Save Primary = Any membership types it is overridding, and its original membership type Cross Save Overridden = Empty list
        bungie_global_display_name: The bungie global display name, if set.
        bungie_global_display_name_code: The bungie global display name code, if set.
        cross_save_override: If there is a cross save override in effect, this value will tell you the type that is overridding this one.
        display_name: Display Name the player has chosen for themselves. The display name is optional when the data type is used as input to a platform API.
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
    icon_path: str = attr.field()
    is_public: bool = attr.field()
    membership_id: int = attr.field()
    membership_type: Union["BungieMembershipType", int] = attr.field(converter=enum_converter("BungieMembershipType"))
    supplemental_display_name: str = attr.field()


@attr.define
class GeneralUser(BaseModel):
    """
    _No description given by bungie._

    None
    Attributes:
        about: _No description given by bungie._
        blizzard_display_name: _No description given by bungie._
        cached_bungie_global_display_name: _No description given by bungie._
        cached_bungie_global_display_name_code: _No description given by bungie._
        context: _No description given by bungie._
        display_name: _No description given by bungie._
        fb_display_name: _No description given by bungie._
        first_access: _No description given by bungie._
        is_deleted: _No description given by bungie._
        last_ban_report_id: _No description given by bungie._
        last_update: _No description given by bungie._
        legacy_portal_u_i_d: _No description given by bungie._
        locale: _No description given by bungie._
        locale_inherit_default: _No description given by bungie._
        membership_id: _No description given by bungie._
        normalized_name: _No description given by bungie._
        profile_ban_expire: _No description given by bungie._
        profile_picture: _No description given by bungie._
        profile_picture_path: _No description given by bungie._
        profile_picture_wide_path: _No description given by bungie._
        profile_theme: _No description given by bungie._
        profile_theme_name: _No description given by bungie._
        psn_display_name: _No description given by bungie._
        show_activity: _No description given by bungie._
        show_group_messaging: _No description given by bungie._
        stadia_display_name: _No description given by bungie._
        status_date: _No description given by bungie._
        status_text: _No description given by bungie._
        steam_display_name: _No description given by bungie._
        success_message_flags: _No description given by bungie._
        twitch_display_name: _No description given by bungie._
        unique_name: _No description given by bungie._
        user_title: _No description given by bungie._
        user_title_display: _No description given by bungie._
        xbox_display_name: _No description given by bungie._
    """

    about: str = attr.field()
    blizzard_display_name: str = attr.field()
    cached_bungie_global_display_name: str = attr.field()
    cached_bungie_global_display_name_code: int = attr.field()
    context: "UserToUserContext" = attr.field()
    display_name: str = attr.field()
    fb_display_name: str = attr.field()
    first_access: datetime = attr.field()
    is_deleted: bool = attr.field()
    last_ban_report_id: int = attr.field()
    last_update: datetime = attr.field()
    legacy_portal_u_i_d: int = attr.field()
    locale: str = attr.field()
    locale_inherit_default: bool = attr.field()
    membership_id: int = attr.field()
    normalized_name: str = attr.field()
    profile_ban_expire: datetime = attr.field()
    profile_picture: int = attr.field()
    profile_picture_path: str = attr.field()
    profile_picture_wide_path: str = attr.field()
    profile_theme: int = attr.field()
    profile_theme_name: str = attr.field()
    psn_display_name: str = attr.field()
    show_activity: bool = attr.field()
    show_group_messaging: bool = attr.field()
    stadia_display_name: str = attr.field()
    status_date: datetime = attr.field()
    status_text: str = attr.field()
    steam_display_name: str = attr.field()
    success_message_flags: int = attr.field()
    twitch_display_name: str = attr.field()
    unique_name: str = attr.field()
    user_title: int = attr.field()
    user_title_display: str = attr.field()
    xbox_display_name: str = attr.field()


@attr.define
class UserToUserContext(BaseModel):
    """
    _No description given by bungie._

    None
    Attributes:
        global_ignore_end_date: _No description given by bungie._
        ignore_status: _No description given by bungie._
        is_following: _No description given by bungie._
    """

    global_ignore_end_date: datetime = attr.field()
    ignore_status: "IgnoreResponse" = attr.field()
    is_following: bool = attr.field()


@attr.define
class UserMembershipData(BaseModel):
    """
    _No description given by bungie._

    None
    Attributes:
        bungie_net_user: _No description given by bungie._
        destiny_memberships: this allows you to see destiny memberships that are visible and linked to this account (regardless of whether or not they have characters on the world server)
        primary_membership_id: If this property is populated, it will have the membership ID of the account considered to be "primary" in this user's cross save relationship.  If null, this user has no cross save relationship, nor primary account.
    """

    bungie_net_user: "GeneralUser" = attr.field()
    destiny_memberships: list["GroupUserInfoCard"] = attr.field(metadata={"type": """list[GroupUserInfoCard]"""})
    primary_membership_id: int = attr.field()


@attr.define
class HardLinkedUserMembership(BaseModel, DestinyUserMixin):
    """
    _No description given by bungie._

    None
    Attributes:
        cross_save_overridden_membership_id: _No description given by bungie._
        cross_save_overridden_type: _No description given by bungie._
        membership_id: _No description given by bungie._
        membership_type: _No description given by bungie._
    """

    cross_save_overridden_membership_id: int = attr.field()
    cross_save_overridden_type: Union["BungieMembershipType", int] = attr.field(
        converter=enum_converter("BungieMembershipType")
    )
    membership_id: int = attr.field()
    membership_type: Union["BungieMembershipType", int] = attr.field(converter=enum_converter("BungieMembershipType"))


@attr.define
class UserSearchResponse(BaseModel):
    """
    _No description given by bungie._

    None
    Attributes:
        has_more: _No description given by bungie._
        page: _No description given by bungie._
        search_results: _No description given by bungie._
    """

    has_more: bool = attr.field()
    page: int = attr.field()
    search_results: list["UserSearchResponseDetail"] = attr.field(
        metadata={"type": """list[UserSearchResponseDetail]"""}
    )


@attr.define
class UserSearchResponseDetail(BaseModel):
    """
    _No description given by bungie._

    None
    Attributes:
        bungie_global_display_name: _No description given by bungie._
        bungie_global_display_name_code: _No description given by bungie._
        bungie_net_membership_id: _No description given by bungie._
        destiny_memberships: _No description given by bungie._
    """

    bungie_global_display_name: str = attr.field()
    bungie_global_display_name_code: int = attr.field()
    bungie_net_membership_id: int = attr.field()
    destiny_memberships: list["UserInfoCard"] = attr.field(metadata={"type": """list[UserInfoCard]"""})


@attr.define
class UserSearchPrefixRequest(BaseModel):
    """
    _No description given by bungie._

    None
    Attributes:
        display_name_prefix: _No description given by bungie._
    """

    display_name_prefix: str = attr.field()


@attr.define
class ExactSearchRequest(BaseModel):
    """
    _No description given by bungie._

    None
    Attributes:
        display_name: _No description given by bungie._
        display_name_code: _No description given by bungie._
    """

    display_name: str = attr.field()
    display_name_code: int = attr.field()


@attr.define
class EmailSettings(BaseModel):
    """
    The set of all email subscription/opt-in settings and definitions.

    None
    Attributes:
        opt_in_definitions: Keyed by the name identifier of the opt-in definition.
        subscription_definitions: Keyed by the name identifier of the Subscription definition.
        views: Keyed by the name identifier of the View definition.
    """

    opt_in_definitions: dict[str, "EmailOptInDefinition"] = attr.field(
        metadata={"type": """dict[str, EmailOptInDefinition]"""}
    )
    subscription_definitions: dict[str, "EmailSubscriptionDefinition"] = attr.field(
        metadata={"type": """dict[str, EmailSubscriptionDefinition]"""}
    )
    views: dict[str, "EmailViewDefinition"] = attr.field(metadata={"type": """dict[str, EmailViewDefinition]"""})


@attr.define
class EmailOptInDefinition(BaseModel):
    """
    Defines a single opt-in category: a wide-scoped permission to send emails for the subject related to the opt-in.

    None
    Attributes:
        dependent_subscriptions: Information about the dependent subscriptions for this opt-in.
        name: The unique identifier for this opt-in category.
        set_by_default: If true, this opt-in setting should be set by default in situations where accounts are created without explicit choices about what they're opting into.
        value: The flag value for this opt-in category. For historical reasons, this is defined as a flags enum.
    """

    dependent_subscriptions: list["EmailSubscriptionDefinition"] = attr.field(
        metadata={"type": """list[EmailSubscriptionDefinition]"""}
    )
    name: str = attr.field()
    set_by_default: bool = attr.field()
    value: Union["OptInFlags", int] = attr.field(converter=enum_converter("OptInFlags"))


class OptInFlags(BaseFlagEnum):
    """
    _No description given by bungie._
    """

    NONE = 0
    """_No description given by bungie._ """
    NEWSLETTER = 1
    """_No description given by bungie._ """
    SYSTEM = 2
    """_No description given by bungie._ """
    MARKETING = 4
    """_No description given by bungie._ """
    USER_RESEARCH = 8
    """_No description given by bungie._ """
    CUSTOMER_SERVICE = 16
    """_No description given by bungie._ """
    SOCIAL = 32
    """_No description given by bungie._ """
    PLAY_TESTS = 64
    """_No description given by bungie._ """
    PLAY_TESTS_LOCAL = 128
    """_No description given by bungie._ """
    CAREERS = 256
    """_No description given by bungie._ """


@attr.define
class EmailSubscriptionDefinition(BaseModel):
    """
    Defines a single subscription: permission to send emails for a specific, focused subject (generally timeboxed, such as for a specific release of a product or feature).

    None
    Attributes:
        localization: A dictionary of localized text for the EMail Opt-in setting, keyed by the locale.
        name: The unique identifier for this subscription.
        value: The bitflag value for this subscription. Should be a unique power of two value.
    """

    localization: dict[str, "EMailSettingSubscriptionLocalization"] = attr.field(
        metadata={"type": """dict[str, EMailSettingSubscriptionLocalization]"""}
    )
    name: str = attr.field()
    value: int = attr.field()


@attr.define
class EMailSettingLocalization(BaseModel):
    """
    Localized text relevant to a given EMail setting in a given localization.

    None
    Attributes:
        description: _No description given by bungie._
        title: _No description given by bungie._
    """

    description: str = attr.field()
    title: str = attr.field()


@attr.define
class EMailSettingSubscriptionLocalization(BaseModel):
    """
    Localized text relevant to a given EMail setting in a given localization. Extra settings specifically for subscriptions.

    None
    Attributes:
        description: _No description given by bungie._
        known_user_action_text: _No description given by bungie._
        registered_user_description: _No description given by bungie._
        title: _No description given by bungie._
        unknown_user_action_text: _No description given by bungie._
        unknown_user_description: _No description given by bungie._
        unregistered_user_description: _No description given by bungie._
    """

    description: str = attr.field()
    known_user_action_text: str = attr.field()
    registered_user_description: str = attr.field()
    title: str = attr.field()
    unknown_user_action_text: str = attr.field()
    unknown_user_description: str = attr.field()
    unregistered_user_description: str = attr.field()


@attr.define
class EmailViewDefinition(BaseModel):
    """
    Represents a data-driven view for Email settings. Web/Mobile UI can use this data to show new EMail settings consistently without further manual work.

    None
    Attributes:
        name: The identifier for this view.
        view_settings: The ordered list of settings to show in this view.
    """

    name: str = attr.field()
    view_settings: list["EmailViewDefinitionSetting"] = attr.field(
        metadata={"type": """list[EmailViewDefinitionSetting]"""}
    )


@attr.define
class EmailViewDefinitionSetting(BaseModel):
    """
    _No description given by bungie._

    None
    Attributes:
        localization: A dictionary of localized text for the EMail setting, keyed by the locale.
        name: The identifier for this UI Setting, which can be used to relate it to custom strings or other data as desired.
        opt_in_aggregate_value: The OptInFlags value to set or clear if this setting is set or cleared in the UI. It is the aggregate of all underlying opt-in flags related to this setting.
        set_by_default: If true, this setting should be set by default if the user hasn't chosen whether it's set or cleared yet.
        subscriptions: The subscriptions to show as children of this setting, if any.
    """

    localization: dict[str, "EMailSettingLocalization"] = attr.field(
        metadata={"type": """dict[str, EMailSettingLocalization]"""}
    )
    name: str = attr.field()
    opt_in_aggregate_value: Union["OptInFlags", int] = attr.field(converter=enum_converter("OptInFlags"))
    set_by_default: bool = attr.field()
    subscriptions: list["EmailSubscriptionDefinition"] = attr.field(
        metadata={"type": """list[EmailSubscriptionDefinition]"""}
    )
