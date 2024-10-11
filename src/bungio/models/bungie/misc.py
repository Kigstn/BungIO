# DO NOT CHANGE ANY CODE BELOW
# This file is generated automatically by `generate_api_schema.py` and will be overwritten
# Instead, change functions / models by subclassing them in the `./overwrites/` folder. They will be used instead.

from datetime import datetime
from typing import TYPE_CHECKING, Union

from bungio.models.base import BaseEnum, BaseModel, custom_define, custom_field
from bungio.utils import enum_converter

if TYPE_CHECKING:
    from bungio.models import (
        ComponentPrivacySetting,
        ContentItemPublicContract,
        DestinyCharacterActivitiesComponent,
        DestinyCharacterComponent,
        DestinyCharacterProgressionComponent,
        DestinyCharacterRecordsComponent,
        DestinyCharacterRenderComponent,
        DestinyCollectiblesComponent,
        DestinyCraftablesComponent,
        DestinyCurrenciesComponent,
        DestinyEntitySearchResultItem,
        DestinyInventoryComponent,
        DestinyItemComponent,
        DestinyItemInstanceComponent,
        DestinyItemObjectivesComponent,
        DestinyItemPerksComponent,
        DestinyItemPlugComponent,
        DestinyItemPlugObjectivesComponent,
        DestinyItemRenderComponent,
        DestinyItemReusablePlugsComponent,
        DestinyItemSocketsComponent,
        DestinyItemStatsComponent,
        DestinyItemTalentGridComponent,
        DestinyKiosksComponent,
        DestinyLoadoutsComponent,
        DestinyMetricsComponent,
        DestinyPlatformSilverComponent,
        DestinyPlugSetsComponent,
        DestinyPresentationNodesComponent,
        DestinyProfileCollectiblesComponent,
        DestinyProfileComponent,
        DestinyProfileProgressionComponent,
        DestinyProfileRecordsComponent,
        DestinyProfileTransitoryComponent,
        DestinyPublicVendorComponent,
        DestinyPublicVendorSaleItemComponent,
        DestinySocialCommendationsComponent,
        DestinyStringVariablesComponent,
        DestinyVendorCategoriesComponent,
        DestinyVendorComponent,
        DestinyVendorGroupComponent,
        DestinyVendorReceiptsComponent,
        DestinyVendorSaleItemComponent,
        FireteamResponse,
        FireteamSummary,
        GroupBan,
        GroupEditHistory,
        GroupMember,
        GroupMemberApplication,
        GroupMembership,
        GroupPotentialMembership,
        GroupV2Card,
        PagedQuery,
        PersonalDestinyVendorSaleItemSetComponent,
        PostResponse,
        PublicDestinyVendorSaleItemSetComponent,
        TrendingEntry,
    )


class BungieMembershipType(BaseEnum):
    """
    The types of membership the Accounts system supports. This is the external facing enum used in place of the internal-only Bungie.SharedDefinitions.MembershipType.
    """

    NONE = 0
    """_No description given by bungie._ """
    TIGER_XBOX = 1
    """_No description given by bungie._ """
    TIGER_PSN = 2
    """_No description given by bungie._ """
    TIGER_STEAM = 3
    """_No description given by bungie._ """
    TIGER_BLIZZARD = 4
    """_No description given by bungie._ """
    TIGER_STADIA = 5
    """_No description given by bungie._ """
    TIGER_EGS = 6
    """_No description given by bungie._ """
    TIGER_DEMON = 10
    """_No description given by bungie._ """
    BUNGIE_NEXT = 254
    """_No description given by bungie._ """
    ALL = -1
    """"All" is only valid for searching capabilities: you need to pass the actual matching BungieMembershipType for any query where you pass a known membershipId. """


class BungieCredentialType(BaseEnum):
    """
    The types of credentials the Accounts system supports. This is the external facing enum used in place of the internal-only Bungie.SharedDefinitions.CredentialType.
    """

    NONE = 0
    """_No description given by bungie._ """
    XUID = 1
    """_No description given by bungie._ """
    PSNID = 2
    """_No description given by bungie._ """
    WLID = 3
    """_No description given by bungie._ """
    FAKE = 4
    """_No description given by bungie._ """
    FACEBOOK = 5
    """_No description given by bungie._ """
    GOOGLE = 8
    """_No description given by bungie._ """
    WINDOWS = 9
    """_No description given by bungie._ """
    DEMON_ID = 10
    """_No description given by bungie._ """
    STEAM_ID = 12
    """_No description given by bungie._ """
    BATTLE_NET_ID = 14
    """_No description given by bungie._ """
    STADIA_ID = 16
    """_No description given by bungie._ """
    TWITCH_ID = 18
    """_No description given by bungie._ """
    EGS_ID = 20
    """_No description given by bungie._ """


@custom_define()
class SearchResultOfContentItemPublicContract(BaseModel):
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
    results: list["ContentItemPublicContract"] = custom_field(metadata={"type": """list[ContentItemPublicContract]"""})
    total_results: int = custom_field()
    use_total_results: bool = custom_field()


@custom_define()
class SearchResultOfPostResponse(BaseModel):
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
    results: list["PostResponse"] = custom_field(metadata={"type": """list[PostResponse]"""})
    total_results: int = custom_field()
    use_total_results: bool = custom_field()


@custom_define()
class SearchResultOfGroupV2Card(BaseModel):
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
class SearchResultOfGroupMember(BaseModel):
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
    results: list["GroupMember"] = custom_field(metadata={"type": """list[GroupMember]"""})
    total_results: int = custom_field()
    use_total_results: bool = custom_field()


@custom_define()
class SearchResultOfGroupBan(BaseModel):
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
    results: list["GroupBan"] = custom_field(metadata={"type": """list[GroupBan]"""})
    total_results: int = custom_field()
    use_total_results: bool = custom_field()


@custom_define()
class SearchResultOfGroupEditHistory(BaseModel):
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
    results: list["GroupEditHistory"] = custom_field(metadata={"type": """list[GroupEditHistory]"""})
    total_results: int = custom_field()
    use_total_results: bool = custom_field()


@custom_define()
class SearchResultOfGroupMemberApplication(BaseModel):
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
    results: list["GroupMemberApplication"] = custom_field(metadata={"type": """list[GroupMemberApplication]"""})
    total_results: int = custom_field()
    use_total_results: bool = custom_field()


@custom_define()
class SearchResultOfGroupMembership(BaseModel):
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
class SearchResultOfGroupPotentialMembership(BaseModel):
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
class SingleComponentResponseOfDestinyVendorReceiptsComponent(BaseModel):
    """
    _No description given by bungie._

    None
    Attributes:
        data: _No description given by bungie._
        disabled: If true, this component is disabled.
        privacy: _No description given by bungie._
    """

    data: "DestinyVendorReceiptsComponent" = custom_field()
    disabled: bool = custom_field()
    privacy: Union["ComponentPrivacySetting", int] = custom_field(converter=enum_converter("ComponentPrivacySetting"))


@custom_define()
class SingleComponentResponseOfDestinyInventoryComponent(BaseModel):
    """
    _No description given by bungie._

    None
    Attributes:
        data: _No description given by bungie._
        disabled: If true, this component is disabled.
        privacy: _No description given by bungie._
    """

    data: "DestinyInventoryComponent" = custom_field()
    disabled: bool = custom_field()
    privacy: Union["ComponentPrivacySetting", int] = custom_field(converter=enum_converter("ComponentPrivacySetting"))


@custom_define()
class SingleComponentResponseOfDestinyProfileComponent(BaseModel):
    """
    _No description given by bungie._

    None
    Attributes:
        data: _No description given by bungie._
        disabled: If true, this component is disabled.
        privacy: _No description given by bungie._
    """

    data: "DestinyProfileComponent" = custom_field()
    disabled: bool = custom_field()
    privacy: Union["ComponentPrivacySetting", int] = custom_field(converter=enum_converter("ComponentPrivacySetting"))


@custom_define()
class SingleComponentResponseOfDestinyPlatformSilverComponent(BaseModel):
    """
    _No description given by bungie._

    None
    Attributes:
        data: _No description given by bungie._
        disabled: If true, this component is disabled.
        privacy: _No description given by bungie._
    """

    data: "DestinyPlatformSilverComponent" = custom_field()
    disabled: bool = custom_field()
    privacy: Union["ComponentPrivacySetting", int] = custom_field(converter=enum_converter("ComponentPrivacySetting"))


@custom_define()
class SingleComponentResponseOfDestinyKiosksComponent(BaseModel):
    """
    _No description given by bungie._

    None
    Attributes:
        data: _No description given by bungie._
        disabled: If true, this component is disabled.
        privacy: _No description given by bungie._
    """

    data: "DestinyKiosksComponent" = custom_field()
    disabled: bool = custom_field()
    privacy: Union["ComponentPrivacySetting", int] = custom_field(converter=enum_converter("ComponentPrivacySetting"))


@custom_define()
class SingleComponentResponseOfDestinyPlugSetsComponent(BaseModel):
    """
    _No description given by bungie._

    None
    Attributes:
        data: _No description given by bungie._
        disabled: If true, this component is disabled.
        privacy: _No description given by bungie._
    """

    data: "DestinyPlugSetsComponent" = custom_field()
    disabled: bool = custom_field()
    privacy: Union["ComponentPrivacySetting", int] = custom_field(converter=enum_converter("ComponentPrivacySetting"))


@custom_define()
class SingleComponentResponseOfDestinyProfileProgressionComponent(BaseModel):
    """
    _No description given by bungie._

    None
    Attributes:
        data: _No description given by bungie._
        disabled: If true, this component is disabled.
        privacy: _No description given by bungie._
    """

    data: "DestinyProfileProgressionComponent" = custom_field()
    disabled: bool = custom_field()
    privacy: Union["ComponentPrivacySetting", int] = custom_field(converter=enum_converter("ComponentPrivacySetting"))


@custom_define()
class SingleComponentResponseOfDestinyPresentationNodesComponent(BaseModel):
    """
    _No description given by bungie._

    None
    Attributes:
        data: _No description given by bungie._
        disabled: If true, this component is disabled.
        privacy: _No description given by bungie._
    """

    data: "DestinyPresentationNodesComponent" = custom_field()
    disabled: bool = custom_field()
    privacy: Union["ComponentPrivacySetting", int] = custom_field(converter=enum_converter("ComponentPrivacySetting"))


@custom_define()
class SingleComponentResponseOfDestinyProfileRecordsComponent(BaseModel):
    """
    _No description given by bungie._

    None
    Attributes:
        data: _No description given by bungie._
        disabled: If true, this component is disabled.
        privacy: _No description given by bungie._
    """

    data: "DestinyProfileRecordsComponent" = custom_field()
    disabled: bool = custom_field()
    privacy: Union["ComponentPrivacySetting", int] = custom_field(converter=enum_converter("ComponentPrivacySetting"))


@custom_define()
class SingleComponentResponseOfDestinyProfileCollectiblesComponent(BaseModel):
    """
    _No description given by bungie._

    None
    Attributes:
        data: _No description given by bungie._
        disabled: If true, this component is disabled.
        privacy: _No description given by bungie._
    """

    data: "DestinyProfileCollectiblesComponent" = custom_field()
    disabled: bool = custom_field()
    privacy: Union["ComponentPrivacySetting", int] = custom_field(converter=enum_converter("ComponentPrivacySetting"))


@custom_define()
class SingleComponentResponseOfDestinyProfileTransitoryComponent(BaseModel):
    """
    _No description given by bungie._

    None
    Attributes:
        data: _No description given by bungie._
        disabled: If true, this component is disabled.
        privacy: _No description given by bungie._
    """

    data: "DestinyProfileTransitoryComponent" = custom_field()
    disabled: bool = custom_field()
    privacy: Union["ComponentPrivacySetting", int] = custom_field(converter=enum_converter("ComponentPrivacySetting"))


@custom_define()
class SingleComponentResponseOfDestinyMetricsComponent(BaseModel):
    """
    _No description given by bungie._

    None
    Attributes:
        data: _No description given by bungie._
        disabled: If true, this component is disabled.
        privacy: _No description given by bungie._
    """

    data: "DestinyMetricsComponent" = custom_field()
    disabled: bool = custom_field()
    privacy: Union["ComponentPrivacySetting", int] = custom_field(converter=enum_converter("ComponentPrivacySetting"))


@custom_define()
class SingleComponentResponseOfDestinyStringVariablesComponent(BaseModel):
    """
    _No description given by bungie._

    None
    Attributes:
        data: _No description given by bungie._
        disabled: If true, this component is disabled.
        privacy: _No description given by bungie._
    """

    data: "DestinyStringVariablesComponent" = custom_field()
    disabled: bool = custom_field()
    privacy: Union["ComponentPrivacySetting", int] = custom_field(converter=enum_converter("ComponentPrivacySetting"))


@custom_define()
class SingleComponentResponseOfDestinySocialCommendationsComponent(BaseModel):
    """
    _No description given by bungie._

    None
    Attributes:
        data: _No description given by bungie._
        disabled: If true, this component is disabled.
        privacy: _No description given by bungie._
    """

    data: "DestinySocialCommendationsComponent" = custom_field()
    disabled: bool = custom_field()
    privacy: Union["ComponentPrivacySetting", int] = custom_field(converter=enum_converter("ComponentPrivacySetting"))


@custom_define()
class DictionaryComponentResponseOfint64AndDestinyCharacterComponent(BaseModel):
    """
    _No description given by bungie._

    None
    Attributes:
        data: _No description given by bungie._
        disabled: If true, this component is disabled.
        privacy: _No description given by bungie._
    """

    data: dict[int, "DestinyCharacterComponent"] = custom_field(
        metadata={"type": """dict[int, DestinyCharacterComponent]"""}
    )
    disabled: bool = custom_field()
    privacy: Union["ComponentPrivacySetting", int] = custom_field(converter=enum_converter("ComponentPrivacySetting"))


@custom_define()
class DictionaryComponentResponseOfint64AndDestinyInventoryComponent(BaseModel):
    """
    _No description given by bungie._

    None
    Attributes:
        data: _No description given by bungie._
        disabled: If true, this component is disabled.
        privacy: _No description given by bungie._
    """

    data: dict[int, "DestinyInventoryComponent"] = custom_field(
        metadata={"type": """dict[int, DestinyInventoryComponent]"""}
    )
    disabled: bool = custom_field()
    privacy: Union["ComponentPrivacySetting", int] = custom_field(converter=enum_converter("ComponentPrivacySetting"))


@custom_define()
class DictionaryComponentResponseOfint64AndDestinyLoadoutsComponent(BaseModel):
    """
    _No description given by bungie._

    None
    Attributes:
        data: _No description given by bungie._
        disabled: If true, this component is disabled.
        privacy: _No description given by bungie._
    """

    data: dict[int, "DestinyLoadoutsComponent"] = custom_field(
        metadata={"type": """dict[int, DestinyLoadoutsComponent]"""}
    )
    disabled: bool = custom_field()
    privacy: Union["ComponentPrivacySetting", int] = custom_field(converter=enum_converter("ComponentPrivacySetting"))


@custom_define()
class DictionaryComponentResponseOfint64AndDestinyCharacterProgressionComponent(BaseModel):
    """
    _No description given by bungie._

    None
    Attributes:
        data: _No description given by bungie._
        disabled: If true, this component is disabled.
        privacy: _No description given by bungie._
    """

    data: dict[int, "DestinyCharacterProgressionComponent"] = custom_field(
        metadata={"type": """dict[int, DestinyCharacterProgressionComponent]"""}
    )
    disabled: bool = custom_field()
    privacy: Union["ComponentPrivacySetting", int] = custom_field(converter=enum_converter("ComponentPrivacySetting"))


@custom_define()
class DictionaryComponentResponseOfint64AndDestinyCharacterRenderComponent(BaseModel):
    """
    _No description given by bungie._

    None
    Attributes:
        data: _No description given by bungie._
        disabled: If true, this component is disabled.
        privacy: _No description given by bungie._
    """

    data: dict[int, "DestinyCharacterRenderComponent"] = custom_field(
        metadata={"type": """dict[int, DestinyCharacterRenderComponent]"""}
    )
    disabled: bool = custom_field()
    privacy: Union["ComponentPrivacySetting", int] = custom_field(converter=enum_converter("ComponentPrivacySetting"))


@custom_define()
class DictionaryComponentResponseOfint64AndDestinyCharacterActivitiesComponent(BaseModel):
    """
    _No description given by bungie._

    None
    Attributes:
        data: _No description given by bungie._
        disabled: If true, this component is disabled.
        privacy: _No description given by bungie._
    """

    data: dict[int, "DestinyCharacterActivitiesComponent"] = custom_field(
        metadata={"type": """dict[int, DestinyCharacterActivitiesComponent]"""}
    )
    disabled: bool = custom_field()
    privacy: Union["ComponentPrivacySetting", int] = custom_field(converter=enum_converter("ComponentPrivacySetting"))


@custom_define()
class DictionaryComponentResponseOfint64AndDestinyKiosksComponent(BaseModel):
    """
    _No description given by bungie._

    None
    Attributes:
        data: _No description given by bungie._
        disabled: If true, this component is disabled.
        privacy: _No description given by bungie._
    """

    data: dict[int, "DestinyKiosksComponent"] = custom_field(metadata={"type": """dict[int, DestinyKiosksComponent]"""})
    disabled: bool = custom_field()
    privacy: Union["ComponentPrivacySetting", int] = custom_field(converter=enum_converter("ComponentPrivacySetting"))


@custom_define()
class DictionaryComponentResponseOfint64AndDestinyPlugSetsComponent(BaseModel):
    """
    _No description given by bungie._

    None
    Attributes:
        data: _No description given by bungie._
        disabled: If true, this component is disabled.
        privacy: _No description given by bungie._
    """

    data: dict[int, "DestinyPlugSetsComponent"] = custom_field(
        metadata={"type": """dict[int, DestinyPlugSetsComponent]"""}
    )
    disabled: bool = custom_field()
    privacy: Union["ComponentPrivacySetting", int] = custom_field(converter=enum_converter("ComponentPrivacySetting"))


@custom_define()
class DestinyBaseItemComponentSetOfuint32(BaseModel):
    """
    _No description given by bungie._

    None
    Attributes:
        objectives: _No description given by bungie._
        perks: _No description given by bungie._
    """

    objectives: "DictionaryComponentResponseOfuint32AndDestinyItemObjectivesComponent" = custom_field()
    perks: "DictionaryComponentResponseOfuint32AndDestinyItemPerksComponent" = custom_field()


@custom_define()
class DictionaryComponentResponseOfuint32AndDestinyItemObjectivesComponent(BaseModel):
    """
    _No description given by bungie._

    None
    Attributes:
        data: _No description given by bungie._
        disabled: If true, this component is disabled.
        privacy: _No description given by bungie._
    """

    data: dict[int, "DestinyItemObjectivesComponent"] = custom_field(
        metadata={"type": """dict[int, DestinyItemObjectivesComponent]"""}
    )
    disabled: bool = custom_field()
    privacy: Union["ComponentPrivacySetting", int] = custom_field(converter=enum_converter("ComponentPrivacySetting"))


@custom_define()
class DictionaryComponentResponseOfuint32AndDestinyItemPerksComponent(BaseModel):
    """
    _No description given by bungie._

    None
    Attributes:
        data: _No description given by bungie._
        disabled: If true, this component is disabled.
        privacy: _No description given by bungie._
    """

    data: dict[int, "DestinyItemPerksComponent"] = custom_field(
        metadata={"type": """dict[int, DestinyItemPerksComponent]"""}
    )
    disabled: bool = custom_field()
    privacy: Union["ComponentPrivacySetting", int] = custom_field(converter=enum_converter("ComponentPrivacySetting"))


@custom_define()
class DictionaryComponentResponseOfint64AndDestinyPresentationNodesComponent(BaseModel):
    """
    _No description given by bungie._

    None
    Attributes:
        data: _No description given by bungie._
        disabled: If true, this component is disabled.
        privacy: _No description given by bungie._
    """

    data: dict[int, "DestinyPresentationNodesComponent"] = custom_field(
        metadata={"type": """dict[int, DestinyPresentationNodesComponent]"""}
    )
    disabled: bool = custom_field()
    privacy: Union["ComponentPrivacySetting", int] = custom_field(converter=enum_converter("ComponentPrivacySetting"))


@custom_define()
class DictionaryComponentResponseOfint64AndDestinyCharacterRecordsComponent(BaseModel):
    """
    _No description given by bungie._

    None
    Attributes:
        data: _No description given by bungie._
        disabled: If true, this component is disabled.
        privacy: _No description given by bungie._
    """

    data: dict[int, "DestinyCharacterRecordsComponent"] = custom_field(
        metadata={"type": """dict[int, DestinyCharacterRecordsComponent]"""}
    )
    disabled: bool = custom_field()
    privacy: Union["ComponentPrivacySetting", int] = custom_field(converter=enum_converter("ComponentPrivacySetting"))


@custom_define()
class DictionaryComponentResponseOfint64AndDestinyCollectiblesComponent(BaseModel):
    """
    _No description given by bungie._

    None
    Attributes:
        data: _No description given by bungie._
        disabled: If true, this component is disabled.
        privacy: _No description given by bungie._
    """

    data: dict[int, "DestinyCollectiblesComponent"] = custom_field(
        metadata={"type": """dict[int, DestinyCollectiblesComponent]"""}
    )
    disabled: bool = custom_field()
    privacy: Union["ComponentPrivacySetting", int] = custom_field(converter=enum_converter("ComponentPrivacySetting"))


@custom_define()
class DictionaryComponentResponseOfint64AndDestinyStringVariablesComponent(BaseModel):
    """
    _No description given by bungie._

    None
    Attributes:
        data: _No description given by bungie._
        disabled: If true, this component is disabled.
        privacy: _No description given by bungie._
    """

    data: dict[int, "DestinyStringVariablesComponent"] = custom_field(
        metadata={"type": """dict[int, DestinyStringVariablesComponent]"""}
    )
    disabled: bool = custom_field()
    privacy: Union["ComponentPrivacySetting", int] = custom_field(converter=enum_converter("ComponentPrivacySetting"))


@custom_define()
class DictionaryComponentResponseOfint64AndDestinyCraftablesComponent(BaseModel):
    """
    _No description given by bungie._

    None
    Attributes:
        data: _No description given by bungie._
        disabled: If true, this component is disabled.
        privacy: _No description given by bungie._
    """

    data: dict[int, "DestinyCraftablesComponent"] = custom_field(
        metadata={"type": """dict[int, DestinyCraftablesComponent]"""}
    )
    disabled: bool = custom_field()
    privacy: Union["ComponentPrivacySetting", int] = custom_field(converter=enum_converter("ComponentPrivacySetting"))


@custom_define()
class DestinyBaseItemComponentSetOfint64(BaseModel):
    """
    _No description given by bungie._

    None
    Attributes:
        objectives: _No description given by bungie._
        perks: _No description given by bungie._
    """

    objectives: "DictionaryComponentResponseOfint64AndDestinyItemObjectivesComponent" = custom_field()
    perks: "DictionaryComponentResponseOfint64AndDestinyItemPerksComponent" = custom_field()


@custom_define()
class DictionaryComponentResponseOfint64AndDestinyItemObjectivesComponent(BaseModel):
    """
    _No description given by bungie._

    None
    Attributes:
        data: _No description given by bungie._
        disabled: If true, this component is disabled.
        privacy: _No description given by bungie._
    """

    data: dict[int, "DestinyItemObjectivesComponent"] = custom_field(
        metadata={"type": """dict[int, DestinyItemObjectivesComponent]"""}
    )
    disabled: bool = custom_field()
    privacy: Union["ComponentPrivacySetting", int] = custom_field(converter=enum_converter("ComponentPrivacySetting"))


@custom_define()
class DictionaryComponentResponseOfint64AndDestinyItemPerksComponent(BaseModel):
    """
    _No description given by bungie._

    None
    Attributes:
        data: _No description given by bungie._
        disabled: If true, this component is disabled.
        privacy: _No description given by bungie._
    """

    data: dict[int, "DestinyItemPerksComponent"] = custom_field(
        metadata={"type": """dict[int, DestinyItemPerksComponent]"""}
    )
    disabled: bool = custom_field()
    privacy: Union["ComponentPrivacySetting", int] = custom_field(converter=enum_converter("ComponentPrivacySetting"))


@custom_define()
class DestinyItemComponentSetOfint64(BaseModel):
    """
    _No description given by bungie._

    None
    Attributes:
        instances: _No description given by bungie._
        objectives: _No description given by bungie._
        perks: _No description given by bungie._
        plug_objectives: _No description given by bungie._
        plug_states: _No description given by bungie._
        render_data: _No description given by bungie._
        reusable_plugs: _No description given by bungie._
        sockets: _No description given by bungie._
        stats: _No description given by bungie._
        talent_grids: _No description given by bungie._
    """

    instances: "DictionaryComponentResponseOfint64AndDestinyItemInstanceComponent" = custom_field()
    objectives: "DictionaryComponentResponseOfint64AndDestinyItemObjectivesComponent" = custom_field()
    perks: "DictionaryComponentResponseOfint64AndDestinyItemPerksComponent" = custom_field()
    plug_objectives: "DictionaryComponentResponseOfint64AndDestinyItemPlugObjectivesComponent" = custom_field()
    plug_states: "DictionaryComponentResponseOfuint32AndDestinyItemPlugComponent" = custom_field()
    render_data: "DictionaryComponentResponseOfint64AndDestinyItemRenderComponent" = custom_field()
    reusable_plugs: "DictionaryComponentResponseOfint64AndDestinyItemReusablePlugsComponent" = custom_field()
    sockets: "DictionaryComponentResponseOfint64AndDestinyItemSocketsComponent" = custom_field()
    stats: "DictionaryComponentResponseOfint64AndDestinyItemStatsComponent" = custom_field()
    talent_grids: "DictionaryComponentResponseOfint64AndDestinyItemTalentGridComponent" = custom_field()


@custom_define()
class DictionaryComponentResponseOfint64AndDestinyItemInstanceComponent(BaseModel):
    """
    _No description given by bungie._

    None
    Attributes:
        data: _No description given by bungie._
        disabled: If true, this component is disabled.
        privacy: _No description given by bungie._
    """

    data: dict[int, "DestinyItemInstanceComponent"] = custom_field(
        metadata={"type": """dict[int, DestinyItemInstanceComponent]"""}
    )
    disabled: bool = custom_field()
    privacy: Union["ComponentPrivacySetting", int] = custom_field(converter=enum_converter("ComponentPrivacySetting"))


@custom_define()
class DictionaryComponentResponseOfint64AndDestinyItemRenderComponent(BaseModel):
    """
    _No description given by bungie._

    None
    Attributes:
        data: _No description given by bungie._
        disabled: If true, this component is disabled.
        privacy: _No description given by bungie._
    """

    data: dict[int, "DestinyItemRenderComponent"] = custom_field(
        metadata={"type": """dict[int, DestinyItemRenderComponent]"""}
    )
    disabled: bool = custom_field()
    privacy: Union["ComponentPrivacySetting", int] = custom_field(converter=enum_converter("ComponentPrivacySetting"))


@custom_define()
class DictionaryComponentResponseOfint64AndDestinyItemStatsComponent(BaseModel):
    """
    _No description given by bungie._

    None
    Attributes:
        data: _No description given by bungie._
        disabled: If true, this component is disabled.
        privacy: _No description given by bungie._
    """

    data: dict[int, "DestinyItemStatsComponent"] = custom_field(
        metadata={"type": """dict[int, DestinyItemStatsComponent]"""}
    )
    disabled: bool = custom_field()
    privacy: Union["ComponentPrivacySetting", int] = custom_field(converter=enum_converter("ComponentPrivacySetting"))


@custom_define()
class DictionaryComponentResponseOfint64AndDestinyItemSocketsComponent(BaseModel):
    """
    _No description given by bungie._

    None
    Attributes:
        data: _No description given by bungie._
        disabled: If true, this component is disabled.
        privacy: _No description given by bungie._
    """

    data: dict[int, "DestinyItemSocketsComponent"] = custom_field(
        metadata={"type": """dict[int, DestinyItemSocketsComponent]"""}
    )
    disabled: bool = custom_field()
    privacy: Union["ComponentPrivacySetting", int] = custom_field(converter=enum_converter("ComponentPrivacySetting"))


@custom_define()
class DictionaryComponentResponseOfint64AndDestinyItemReusablePlugsComponent(BaseModel):
    """
    _No description given by bungie._

    None
    Attributes:
        data: _No description given by bungie._
        disabled: If true, this component is disabled.
        privacy: _No description given by bungie._
    """

    data: dict[int, "DestinyItemReusablePlugsComponent"] = custom_field(
        metadata={"type": """dict[int, DestinyItemReusablePlugsComponent]"""}
    )
    disabled: bool = custom_field()
    privacy: Union["ComponentPrivacySetting", int] = custom_field(converter=enum_converter("ComponentPrivacySetting"))


@custom_define()
class DictionaryComponentResponseOfint64AndDestinyItemPlugObjectivesComponent(BaseModel):
    """
    _No description given by bungie._

    None
    Attributes:
        data: _No description given by bungie._
        disabled: If true, this component is disabled.
        privacy: _No description given by bungie._
    """

    data: dict[int, "DestinyItemPlugObjectivesComponent"] = custom_field(
        metadata={"type": """dict[int, DestinyItemPlugObjectivesComponent]"""}
    )
    disabled: bool = custom_field()
    privacy: Union["ComponentPrivacySetting", int] = custom_field(converter=enum_converter("ComponentPrivacySetting"))


@custom_define()
class DictionaryComponentResponseOfint64AndDestinyItemTalentGridComponent(BaseModel):
    """
    _No description given by bungie._

    None
    Attributes:
        data: _No description given by bungie._
        disabled: If true, this component is disabled.
        privacy: _No description given by bungie._
    """

    data: dict[int, "DestinyItemTalentGridComponent"] = custom_field(
        metadata={"type": """dict[int, DestinyItemTalentGridComponent]"""}
    )
    disabled: bool = custom_field()
    privacy: Union["ComponentPrivacySetting", int] = custom_field(converter=enum_converter("ComponentPrivacySetting"))


@custom_define()
class DictionaryComponentResponseOfuint32AndDestinyItemPlugComponent(BaseModel):
    """
    _No description given by bungie._

    None
    Attributes:
        data: _No description given by bungie._
        disabled: If true, this component is disabled.
        privacy: _No description given by bungie._
    """

    data: dict[int, "DestinyItemPlugComponent"] = custom_field(
        metadata={"type": """dict[int, DestinyItemPlugComponent]"""}
    )
    disabled: bool = custom_field()
    privacy: Union["ComponentPrivacySetting", int] = custom_field(converter=enum_converter("ComponentPrivacySetting"))


@custom_define()
class DictionaryComponentResponseOfint64AndDestinyCurrenciesComponent(BaseModel):
    """
    _No description given by bungie._

    None
    Attributes:
        data: _No description given by bungie._
        disabled: If true, this component is disabled.
        privacy: _No description given by bungie._
    """

    data: dict[int, "DestinyCurrenciesComponent"] = custom_field(
        metadata={"type": """dict[int, DestinyCurrenciesComponent]"""}
    )
    disabled: bool = custom_field()
    privacy: Union["ComponentPrivacySetting", int] = custom_field(converter=enum_converter("ComponentPrivacySetting"))


@custom_define()
class SingleComponentResponseOfDestinyCharacterComponent(BaseModel):
    """
    _No description given by bungie._

    None
    Attributes:
        data: _No description given by bungie._
        disabled: If true, this component is disabled.
        privacy: _No description given by bungie._
    """

    data: "DestinyCharacterComponent" = custom_field()
    disabled: bool = custom_field()
    privacy: Union["ComponentPrivacySetting", int] = custom_field(converter=enum_converter("ComponentPrivacySetting"))


@custom_define()
class SingleComponentResponseOfDestinyCharacterProgressionComponent(BaseModel):
    """
    _No description given by bungie._

    None
    Attributes:
        data: _No description given by bungie._
        disabled: If true, this component is disabled.
        privacy: _No description given by bungie._
    """

    data: "DestinyCharacterProgressionComponent" = custom_field()
    disabled: bool = custom_field()
    privacy: Union["ComponentPrivacySetting", int] = custom_field(converter=enum_converter("ComponentPrivacySetting"))


@custom_define()
class SingleComponentResponseOfDestinyCharacterRenderComponent(BaseModel):
    """
    _No description given by bungie._

    None
    Attributes:
        data: _No description given by bungie._
        disabled: If true, this component is disabled.
        privacy: _No description given by bungie._
    """

    data: "DestinyCharacterRenderComponent" = custom_field()
    disabled: bool = custom_field()
    privacy: Union["ComponentPrivacySetting", int] = custom_field(converter=enum_converter("ComponentPrivacySetting"))


@custom_define()
class SingleComponentResponseOfDestinyCharacterActivitiesComponent(BaseModel):
    """
    _No description given by bungie._

    None
    Attributes:
        data: _No description given by bungie._
        disabled: If true, this component is disabled.
        privacy: _No description given by bungie._
    """

    data: "DestinyCharacterActivitiesComponent" = custom_field()
    disabled: bool = custom_field()
    privacy: Union["ComponentPrivacySetting", int] = custom_field(converter=enum_converter("ComponentPrivacySetting"))


@custom_define()
class SingleComponentResponseOfDestinyLoadoutsComponent(BaseModel):
    """
    _No description given by bungie._

    None
    Attributes:
        data: _No description given by bungie._
        disabled: If true, this component is disabled.
        privacy: _No description given by bungie._
    """

    data: "DestinyLoadoutsComponent" = custom_field()
    disabled: bool = custom_field()
    privacy: Union["ComponentPrivacySetting", int] = custom_field(converter=enum_converter("ComponentPrivacySetting"))


@custom_define()
class SingleComponentResponseOfDestinyCharacterRecordsComponent(BaseModel):
    """
    _No description given by bungie._

    None
    Attributes:
        data: _No description given by bungie._
        disabled: If true, this component is disabled.
        privacy: _No description given by bungie._
    """

    data: "DestinyCharacterRecordsComponent" = custom_field()
    disabled: bool = custom_field()
    privacy: Union["ComponentPrivacySetting", int] = custom_field(converter=enum_converter("ComponentPrivacySetting"))


@custom_define()
class SingleComponentResponseOfDestinyCollectiblesComponent(BaseModel):
    """
    _No description given by bungie._

    None
    Attributes:
        data: _No description given by bungie._
        disabled: If true, this component is disabled.
        privacy: _No description given by bungie._
    """

    data: "DestinyCollectiblesComponent" = custom_field()
    disabled: bool = custom_field()
    privacy: Union["ComponentPrivacySetting", int] = custom_field(converter=enum_converter("ComponentPrivacySetting"))


@custom_define()
class SingleComponentResponseOfDestinyCurrenciesComponent(BaseModel):
    """
    _No description given by bungie._

    None
    Attributes:
        data: _No description given by bungie._
        disabled: If true, this component is disabled.
        privacy: _No description given by bungie._
    """

    data: "DestinyCurrenciesComponent" = custom_field()
    disabled: bool = custom_field()
    privacy: Union["ComponentPrivacySetting", int] = custom_field(converter=enum_converter("ComponentPrivacySetting"))


@custom_define()
class SingleComponentResponseOfDestinyItemComponent(BaseModel):
    """
    _No description given by bungie._

    None
    Attributes:
        data: _No description given by bungie._
        disabled: If true, this component is disabled.
        privacy: _No description given by bungie._
    """

    data: "DestinyItemComponent" = custom_field()
    disabled: bool = custom_field()
    privacy: Union["ComponentPrivacySetting", int] = custom_field(converter=enum_converter("ComponentPrivacySetting"))


@custom_define()
class SingleComponentResponseOfDestinyItemInstanceComponent(BaseModel):
    """
    _No description given by bungie._

    None
    Attributes:
        data: _No description given by bungie._
        disabled: If true, this component is disabled.
        privacy: _No description given by bungie._
    """

    data: "DestinyItemInstanceComponent" = custom_field()
    disabled: bool = custom_field()
    privacy: Union["ComponentPrivacySetting", int] = custom_field(converter=enum_converter("ComponentPrivacySetting"))


@custom_define()
class SingleComponentResponseOfDestinyItemObjectivesComponent(BaseModel):
    """
    _No description given by bungie._

    None
    Attributes:
        data: _No description given by bungie._
        disabled: If true, this component is disabled.
        privacy: _No description given by bungie._
    """

    data: "DestinyItemObjectivesComponent" = custom_field()
    disabled: bool = custom_field()
    privacy: Union["ComponentPrivacySetting", int] = custom_field(converter=enum_converter("ComponentPrivacySetting"))


@custom_define()
class SingleComponentResponseOfDestinyItemPerksComponent(BaseModel):
    """
    _No description given by bungie._

    None
    Attributes:
        data: _No description given by bungie._
        disabled: If true, this component is disabled.
        privacy: _No description given by bungie._
    """

    data: "DestinyItemPerksComponent" = custom_field()
    disabled: bool = custom_field()
    privacy: Union["ComponentPrivacySetting", int] = custom_field(converter=enum_converter("ComponentPrivacySetting"))


@custom_define()
class SingleComponentResponseOfDestinyItemRenderComponent(BaseModel):
    """
    _No description given by bungie._

    None
    Attributes:
        data: _No description given by bungie._
        disabled: If true, this component is disabled.
        privacy: _No description given by bungie._
    """

    data: "DestinyItemRenderComponent" = custom_field()
    disabled: bool = custom_field()
    privacy: Union["ComponentPrivacySetting", int] = custom_field(converter=enum_converter("ComponentPrivacySetting"))


@custom_define()
class SingleComponentResponseOfDestinyItemStatsComponent(BaseModel):
    """
    _No description given by bungie._

    None
    Attributes:
        data: _No description given by bungie._
        disabled: If true, this component is disabled.
        privacy: _No description given by bungie._
    """

    data: "DestinyItemStatsComponent" = custom_field()
    disabled: bool = custom_field()
    privacy: Union["ComponentPrivacySetting", int] = custom_field(converter=enum_converter("ComponentPrivacySetting"))


@custom_define()
class SingleComponentResponseOfDestinyItemTalentGridComponent(BaseModel):
    """
    _No description given by bungie._

    None
    Attributes:
        data: _No description given by bungie._
        disabled: If true, this component is disabled.
        privacy: _No description given by bungie._
    """

    data: "DestinyItemTalentGridComponent" = custom_field()
    disabled: bool = custom_field()
    privacy: Union["ComponentPrivacySetting", int] = custom_field(converter=enum_converter("ComponentPrivacySetting"))


@custom_define()
class SingleComponentResponseOfDestinyItemSocketsComponent(BaseModel):
    """
    _No description given by bungie._

    None
    Attributes:
        data: _No description given by bungie._
        disabled: If true, this component is disabled.
        privacy: _No description given by bungie._
    """

    data: "DestinyItemSocketsComponent" = custom_field()
    disabled: bool = custom_field()
    privacy: Union["ComponentPrivacySetting", int] = custom_field(converter=enum_converter("ComponentPrivacySetting"))


@custom_define()
class SingleComponentResponseOfDestinyItemReusablePlugsComponent(BaseModel):
    """
    _No description given by bungie._

    None
    Attributes:
        data: _No description given by bungie._
        disabled: If true, this component is disabled.
        privacy: _No description given by bungie._
    """

    data: "DestinyItemReusablePlugsComponent" = custom_field()
    disabled: bool = custom_field()
    privacy: Union["ComponentPrivacySetting", int] = custom_field(converter=enum_converter("ComponentPrivacySetting"))


@custom_define()
class SingleComponentResponseOfDestinyItemPlugObjectivesComponent(BaseModel):
    """
    _No description given by bungie._

    None
    Attributes:
        data: _No description given by bungie._
        disabled: If true, this component is disabled.
        privacy: _No description given by bungie._
    """

    data: "DestinyItemPlugObjectivesComponent" = custom_field()
    disabled: bool = custom_field()
    privacy: Union["ComponentPrivacySetting", int] = custom_field(converter=enum_converter("ComponentPrivacySetting"))


@custom_define()
class SingleComponentResponseOfDestinyVendorGroupComponent(BaseModel):
    """
    _No description given by bungie._

    None
    Attributes:
        data: _No description given by bungie._
        disabled: If true, this component is disabled.
        privacy: _No description given by bungie._
    """

    data: "DestinyVendorGroupComponent" = custom_field()
    disabled: bool = custom_field()
    privacy: Union["ComponentPrivacySetting", int] = custom_field(converter=enum_converter("ComponentPrivacySetting"))


@custom_define()
class DictionaryComponentResponseOfuint32AndDestinyVendorComponent(BaseModel):
    """
    _No description given by bungie._

    None
    Attributes:
        data: _No description given by bungie._
        disabled: If true, this component is disabled.
        privacy: _No description given by bungie._
    """

    data: dict[int, "DestinyVendorComponent"] = custom_field(metadata={"type": """dict[int, DestinyVendorComponent]"""})
    disabled: bool = custom_field()
    privacy: Union["ComponentPrivacySetting", int] = custom_field(converter=enum_converter("ComponentPrivacySetting"))


@custom_define()
class DictionaryComponentResponseOfuint32AndDestinyVendorCategoriesComponent(BaseModel):
    """
    _No description given by bungie._

    None
    Attributes:
        data: _No description given by bungie._
        disabled: If true, this component is disabled.
        privacy: _No description given by bungie._
    """

    data: dict[int, "DestinyVendorCategoriesComponent"] = custom_field(
        metadata={"type": """dict[int, DestinyVendorCategoriesComponent]"""}
    )
    disabled: bool = custom_field()
    privacy: Union["ComponentPrivacySetting", int] = custom_field(converter=enum_converter("ComponentPrivacySetting"))


@custom_define()
class DestinyVendorSaleItemSetComponentOfDestinyVendorSaleItemComponent(BaseModel):
    """
    _No description given by bungie._

    None
    Attributes:
        sale_items: _No description given by bungie._
    """

    sale_items: dict[int, "DestinyVendorSaleItemComponent"] = custom_field(
        metadata={"type": """dict[int, DestinyVendorSaleItemComponent]"""}
    )


@custom_define()
class DictionaryComponentResponseOfuint32AndPersonalDestinyVendorSaleItemSetComponent(BaseModel):
    """
    _No description given by bungie._

    None
    Attributes:
        data: _No description given by bungie._
        disabled: If true, this component is disabled.
        privacy: _No description given by bungie._
    """

    data: dict[int, "PersonalDestinyVendorSaleItemSetComponent"] = custom_field(
        metadata={"type": """dict[int, PersonalDestinyVendorSaleItemSetComponent]"""}
    )
    disabled: bool = custom_field()
    privacy: Union["ComponentPrivacySetting", int] = custom_field(converter=enum_converter("ComponentPrivacySetting"))


@custom_define()
class DestinyBaseItemComponentSetOfint32(BaseModel):
    """
    _No description given by bungie._

    None
    Attributes:
        objectives: _No description given by bungie._
        perks: _No description given by bungie._
    """

    objectives: "DictionaryComponentResponseOfint32AndDestinyItemObjectivesComponent" = custom_field()
    perks: "DictionaryComponentResponseOfint32AndDestinyItemPerksComponent" = custom_field()


@custom_define()
class DictionaryComponentResponseOfint32AndDestinyItemObjectivesComponent(BaseModel):
    """
    _No description given by bungie._

    None
    Attributes:
        data: _No description given by bungie._
        disabled: If true, this component is disabled.
        privacy: _No description given by bungie._
    """

    data: dict[int, "DestinyItemObjectivesComponent"] = custom_field(
        metadata={"type": """dict[int, DestinyItemObjectivesComponent]"""}
    )
    disabled: bool = custom_field()
    privacy: Union["ComponentPrivacySetting", int] = custom_field(converter=enum_converter("ComponentPrivacySetting"))


@custom_define()
class DictionaryComponentResponseOfint32AndDestinyItemPerksComponent(BaseModel):
    """
    _No description given by bungie._

    None
    Attributes:
        data: _No description given by bungie._
        disabled: If true, this component is disabled.
        privacy: _No description given by bungie._
    """

    data: dict[int, "DestinyItemPerksComponent"] = custom_field(
        metadata={"type": """dict[int, DestinyItemPerksComponent]"""}
    )
    disabled: bool = custom_field()
    privacy: Union["ComponentPrivacySetting", int] = custom_field(converter=enum_converter("ComponentPrivacySetting"))


@custom_define()
class DestinyItemComponentSetOfint32(BaseModel):
    """
    _No description given by bungie._

    None
    Attributes:
        instances: _No description given by bungie._
        objectives: _No description given by bungie._
        perks: _No description given by bungie._
        plug_objectives: _No description given by bungie._
        plug_states: _No description given by bungie._
        render_data: _No description given by bungie._
        reusable_plugs: _No description given by bungie._
        sockets: _No description given by bungie._
        stats: _No description given by bungie._
        talent_grids: _No description given by bungie._
    """

    instances: "DictionaryComponentResponseOfint32AndDestinyItemInstanceComponent" = custom_field()
    objectives: "DictionaryComponentResponseOfint32AndDestinyItemObjectivesComponent" = custom_field()
    perks: "DictionaryComponentResponseOfint32AndDestinyItemPerksComponent" = custom_field()
    plug_objectives: "DictionaryComponentResponseOfint32AndDestinyItemPlugObjectivesComponent" = custom_field()
    plug_states: "DictionaryComponentResponseOfuint32AndDestinyItemPlugComponent" = custom_field()
    render_data: "DictionaryComponentResponseOfint32AndDestinyItemRenderComponent" = custom_field()
    reusable_plugs: "DictionaryComponentResponseOfint32AndDestinyItemReusablePlugsComponent" = custom_field()
    sockets: "DictionaryComponentResponseOfint32AndDestinyItemSocketsComponent" = custom_field()
    stats: "DictionaryComponentResponseOfint32AndDestinyItemStatsComponent" = custom_field()
    talent_grids: "DictionaryComponentResponseOfint32AndDestinyItemTalentGridComponent" = custom_field()


@custom_define()
class DictionaryComponentResponseOfint32AndDestinyItemInstanceComponent(BaseModel):
    """
    _No description given by bungie._

    None
    Attributes:
        data: _No description given by bungie._
        disabled: If true, this component is disabled.
        privacy: _No description given by bungie._
    """

    data: dict[int, "DestinyItemInstanceComponent"] = custom_field(
        metadata={"type": """dict[int, DestinyItemInstanceComponent]"""}
    )
    disabled: bool = custom_field()
    privacy: Union["ComponentPrivacySetting", int] = custom_field(converter=enum_converter("ComponentPrivacySetting"))


@custom_define()
class DictionaryComponentResponseOfint32AndDestinyItemRenderComponent(BaseModel):
    """
    _No description given by bungie._

    None
    Attributes:
        data: _No description given by bungie._
        disabled: If true, this component is disabled.
        privacy: _No description given by bungie._
    """

    data: dict[int, "DestinyItemRenderComponent"] = custom_field(
        metadata={"type": """dict[int, DestinyItemRenderComponent]"""}
    )
    disabled: bool = custom_field()
    privacy: Union["ComponentPrivacySetting", int] = custom_field(converter=enum_converter("ComponentPrivacySetting"))


@custom_define()
class DictionaryComponentResponseOfint32AndDestinyItemStatsComponent(BaseModel):
    """
    _No description given by bungie._

    None
    Attributes:
        data: _No description given by bungie._
        disabled: If true, this component is disabled.
        privacy: _No description given by bungie._
    """

    data: dict[int, "DestinyItemStatsComponent"] = custom_field(
        metadata={"type": """dict[int, DestinyItemStatsComponent]"""}
    )
    disabled: bool = custom_field()
    privacy: Union["ComponentPrivacySetting", int] = custom_field(converter=enum_converter("ComponentPrivacySetting"))


@custom_define()
class DictionaryComponentResponseOfint32AndDestinyItemSocketsComponent(BaseModel):
    """
    _No description given by bungie._

    None
    Attributes:
        data: _No description given by bungie._
        disabled: If true, this component is disabled.
        privacy: _No description given by bungie._
    """

    data: dict[int, "DestinyItemSocketsComponent"] = custom_field(
        metadata={"type": """dict[int, DestinyItemSocketsComponent]"""}
    )
    disabled: bool = custom_field()
    privacy: Union["ComponentPrivacySetting", int] = custom_field(converter=enum_converter("ComponentPrivacySetting"))


@custom_define()
class DictionaryComponentResponseOfint32AndDestinyItemReusablePlugsComponent(BaseModel):
    """
    _No description given by bungie._

    None
    Attributes:
        data: _No description given by bungie._
        disabled: If true, this component is disabled.
        privacy: _No description given by bungie._
    """

    data: dict[int, "DestinyItemReusablePlugsComponent"] = custom_field(
        metadata={"type": """dict[int, DestinyItemReusablePlugsComponent]"""}
    )
    disabled: bool = custom_field()
    privacy: Union["ComponentPrivacySetting", int] = custom_field(converter=enum_converter("ComponentPrivacySetting"))


@custom_define()
class DictionaryComponentResponseOfint32AndDestinyItemPlugObjectivesComponent(BaseModel):
    """
    _No description given by bungie._

    None
    Attributes:
        data: _No description given by bungie._
        disabled: If true, this component is disabled.
        privacy: _No description given by bungie._
    """

    data: dict[int, "DestinyItemPlugObjectivesComponent"] = custom_field(
        metadata={"type": """dict[int, DestinyItemPlugObjectivesComponent]"""}
    )
    disabled: bool = custom_field()
    privacy: Union["ComponentPrivacySetting", int] = custom_field(converter=enum_converter("ComponentPrivacySetting"))


@custom_define()
class DictionaryComponentResponseOfint32AndDestinyItemTalentGridComponent(BaseModel):
    """
    _No description given by bungie._

    None
    Attributes:
        data: _No description given by bungie._
        disabled: If true, this component is disabled.
        privacy: _No description given by bungie._
    """

    data: dict[int, "DestinyItemTalentGridComponent"] = custom_field(
        metadata={"type": """dict[int, DestinyItemTalentGridComponent]"""}
    )
    disabled: bool = custom_field()
    privacy: Union["ComponentPrivacySetting", int] = custom_field(converter=enum_converter("ComponentPrivacySetting"))


@custom_define()
class DestinyVendorItemComponentSetOfint32(BaseModel):
    """
    _No description given by bungie._

    None
    Attributes:
        instances: _No description given by bungie._
        item_components: _No description given by bungie._
        objectives: _No description given by bungie._
        perks: _No description given by bungie._
        plug_objectives: _No description given by bungie._
        plug_states: _No description given by bungie._
        render_data: _No description given by bungie._
        reusable_plugs: _No description given by bungie._
        sockets: _No description given by bungie._
        stats: _No description given by bungie._
        talent_grids: _No description given by bungie._
    """

    instances: "DictionaryComponentResponseOfint32AndDestinyItemInstanceComponent" = custom_field()
    item_components: dict = custom_field(metadata={"type": """dict"""})
    objectives: "DictionaryComponentResponseOfint32AndDestinyItemObjectivesComponent" = custom_field()
    perks: "DictionaryComponentResponseOfint32AndDestinyItemPerksComponent" = custom_field()
    plug_objectives: "DictionaryComponentResponseOfint32AndDestinyItemPlugObjectivesComponent" = custom_field()
    plug_states: "DictionaryComponentResponseOfuint32AndDestinyItemPlugComponent" = custom_field()
    render_data: "DictionaryComponentResponseOfint32AndDestinyItemRenderComponent" = custom_field()
    reusable_plugs: "DictionaryComponentResponseOfint32AndDestinyItemReusablePlugsComponent" = custom_field()
    sockets: "DictionaryComponentResponseOfint32AndDestinyItemSocketsComponent" = custom_field()
    stats: "DictionaryComponentResponseOfint32AndDestinyItemStatsComponent" = custom_field()
    talent_grids: "DictionaryComponentResponseOfint32AndDestinyItemTalentGridComponent" = custom_field()


@custom_define()
class DictionaryComponentResponseOfint32AndDestinyItemComponent(BaseModel):
    """
    _No description given by bungie._

    None
    Attributes:
        data: _No description given by bungie._
        disabled: If true, this component is disabled.
        privacy: _No description given by bungie._
    """

    data: dict[int, "DestinyItemComponent"] = custom_field(metadata={"type": """dict[int, DestinyItemComponent]"""})
    disabled: bool = custom_field()
    privacy: Union["ComponentPrivacySetting", int] = custom_field(converter=enum_converter("ComponentPrivacySetting"))


@custom_define()
class SingleComponentResponseOfDestinyVendorComponent(BaseModel):
    """
    _No description given by bungie._

    None
    Attributes:
        data: _No description given by bungie._
        disabled: If true, this component is disabled.
        privacy: _No description given by bungie._
    """

    data: "DestinyVendorComponent" = custom_field()
    disabled: bool = custom_field()
    privacy: Union["ComponentPrivacySetting", int] = custom_field(converter=enum_converter("ComponentPrivacySetting"))


@custom_define()
class SingleComponentResponseOfDestinyVendorCategoriesComponent(BaseModel):
    """
    _No description given by bungie._

    None
    Attributes:
        data: _No description given by bungie._
        disabled: If true, this component is disabled.
        privacy: _No description given by bungie._
    """

    data: "DestinyVendorCategoriesComponent" = custom_field()
    disabled: bool = custom_field()
    privacy: Union["ComponentPrivacySetting", int] = custom_field(converter=enum_converter("ComponentPrivacySetting"))


@custom_define()
class DictionaryComponentResponseOfint32AndDestinyVendorSaleItemComponent(BaseModel):
    """
    _No description given by bungie._

    None
    Attributes:
        data: _No description given by bungie._
        disabled: If true, this component is disabled.
        privacy: _No description given by bungie._
    """

    data: dict[int, "DestinyVendorSaleItemComponent"] = custom_field(
        metadata={"type": """dict[int, DestinyVendorSaleItemComponent]"""}
    )
    disabled: bool = custom_field()
    privacy: Union["ComponentPrivacySetting", int] = custom_field(converter=enum_converter("ComponentPrivacySetting"))


@custom_define()
class DictionaryComponentResponseOfuint32AndDestinyPublicVendorComponent(BaseModel):
    """
    _No description given by bungie._

    None
    Attributes:
        data: _No description given by bungie._
        disabled: If true, this component is disabled.
        privacy: _No description given by bungie._
    """

    data: dict[int, "DestinyPublicVendorComponent"] = custom_field(
        metadata={"type": """dict[int, DestinyPublicVendorComponent]"""}
    )
    disabled: bool = custom_field()
    privacy: Union["ComponentPrivacySetting", int] = custom_field(converter=enum_converter("ComponentPrivacySetting"))


@custom_define()
class DestinyVendorSaleItemSetComponentOfDestinyPublicVendorSaleItemComponent(BaseModel):
    """
    _No description given by bungie._

    None
    Attributes:
        sale_items: _No description given by bungie._
    """

    sale_items: dict[int, "DestinyPublicVendorSaleItemComponent"] = custom_field(
        metadata={"type": """dict[int, DestinyPublicVendorSaleItemComponent]"""}
    )


@custom_define()
class DictionaryComponentResponseOfuint32AndPublicDestinyVendorSaleItemSetComponent(BaseModel):
    """
    _No description given by bungie._

    None
    Attributes:
        data: _No description given by bungie._
        disabled: If true, this component is disabled.
        privacy: _No description given by bungie._
    """

    data: dict[int, "PublicDestinyVendorSaleItemSetComponent"] = custom_field(
        metadata={"type": """dict[int, PublicDestinyVendorSaleItemSetComponent]"""}
    )
    disabled: bool = custom_field()
    privacy: Union["ComponentPrivacySetting", int] = custom_field(converter=enum_converter("ComponentPrivacySetting"))


@custom_define()
class DestinyItemComponentSetOfuint32(BaseModel):
    """
    _No description given by bungie._

    None
    Attributes:
        instances: _No description given by bungie._
        objectives: _No description given by bungie._
        perks: _No description given by bungie._
        plug_objectives: _No description given by bungie._
        plug_states: _No description given by bungie._
        render_data: _No description given by bungie._
        reusable_plugs: _No description given by bungie._
        sockets: _No description given by bungie._
        stats: _No description given by bungie._
        talent_grids: _No description given by bungie._
    """

    instances: "DictionaryComponentResponseOfuint32AndDestinyItemInstanceComponent" = custom_field()
    objectives: "DictionaryComponentResponseOfuint32AndDestinyItemObjectivesComponent" = custom_field()
    perks: "DictionaryComponentResponseOfuint32AndDestinyItemPerksComponent" = custom_field()
    plug_objectives: "DictionaryComponentResponseOfuint32AndDestinyItemPlugObjectivesComponent" = custom_field()
    plug_states: "DictionaryComponentResponseOfuint32AndDestinyItemPlugComponent" = custom_field()
    render_data: "DictionaryComponentResponseOfuint32AndDestinyItemRenderComponent" = custom_field()
    reusable_plugs: "DictionaryComponentResponseOfuint32AndDestinyItemReusablePlugsComponent" = custom_field()
    sockets: "DictionaryComponentResponseOfuint32AndDestinyItemSocketsComponent" = custom_field()
    stats: "DictionaryComponentResponseOfuint32AndDestinyItemStatsComponent" = custom_field()
    talent_grids: "DictionaryComponentResponseOfuint32AndDestinyItemTalentGridComponent" = custom_field()


@custom_define()
class DictionaryComponentResponseOfuint32AndDestinyItemInstanceComponent(BaseModel):
    """
    _No description given by bungie._

    None
    Attributes:
        data: _No description given by bungie._
        disabled: If true, this component is disabled.
        privacy: _No description given by bungie._
    """

    data: dict[int, "DestinyItemInstanceComponent"] = custom_field(
        metadata={"type": """dict[int, DestinyItemInstanceComponent]"""}
    )
    disabled: bool = custom_field()
    privacy: Union["ComponentPrivacySetting", int] = custom_field(converter=enum_converter("ComponentPrivacySetting"))


@custom_define()
class DictionaryComponentResponseOfuint32AndDestinyItemRenderComponent(BaseModel):
    """
    _No description given by bungie._

    None
    Attributes:
        data: _No description given by bungie._
        disabled: If true, this component is disabled.
        privacy: _No description given by bungie._
    """

    data: dict[int, "DestinyItemRenderComponent"] = custom_field(
        metadata={"type": """dict[int, DestinyItemRenderComponent]"""}
    )
    disabled: bool = custom_field()
    privacy: Union["ComponentPrivacySetting", int] = custom_field(converter=enum_converter("ComponentPrivacySetting"))


@custom_define()
class DictionaryComponentResponseOfuint32AndDestinyItemStatsComponent(BaseModel):
    """
    _No description given by bungie._

    None
    Attributes:
        data: _No description given by bungie._
        disabled: If true, this component is disabled.
        privacy: _No description given by bungie._
    """

    data: dict[int, "DestinyItemStatsComponent"] = custom_field(
        metadata={"type": """dict[int, DestinyItemStatsComponent]"""}
    )
    disabled: bool = custom_field()
    privacy: Union["ComponentPrivacySetting", int] = custom_field(converter=enum_converter("ComponentPrivacySetting"))


@custom_define()
class DictionaryComponentResponseOfuint32AndDestinyItemSocketsComponent(BaseModel):
    """
    _No description given by bungie._

    None
    Attributes:
        data: _No description given by bungie._
        disabled: If true, this component is disabled.
        privacy: _No description given by bungie._
    """

    data: dict[int, "DestinyItemSocketsComponent"] = custom_field(
        metadata={"type": """dict[int, DestinyItemSocketsComponent]"""}
    )
    disabled: bool = custom_field()
    privacy: Union["ComponentPrivacySetting", int] = custom_field(converter=enum_converter("ComponentPrivacySetting"))


@custom_define()
class DictionaryComponentResponseOfuint32AndDestinyItemReusablePlugsComponent(BaseModel):
    """
    _No description given by bungie._

    None
    Attributes:
        data: _No description given by bungie._
        disabled: If true, this component is disabled.
        privacy: _No description given by bungie._
    """

    data: dict[int, "DestinyItemReusablePlugsComponent"] = custom_field(
        metadata={"type": """dict[int, DestinyItemReusablePlugsComponent]"""}
    )
    disabled: bool = custom_field()
    privacy: Union["ComponentPrivacySetting", int] = custom_field(converter=enum_converter("ComponentPrivacySetting"))


@custom_define()
class DictionaryComponentResponseOfuint32AndDestinyItemPlugObjectivesComponent(BaseModel):
    """
    _No description given by bungie._

    None
    Attributes:
        data: _No description given by bungie._
        disabled: If true, this component is disabled.
        privacy: _No description given by bungie._
    """

    data: dict[int, "DestinyItemPlugObjectivesComponent"] = custom_field(
        metadata={"type": """dict[int, DestinyItemPlugObjectivesComponent]"""}
    )
    disabled: bool = custom_field()
    privacy: Union["ComponentPrivacySetting", int] = custom_field(converter=enum_converter("ComponentPrivacySetting"))


@custom_define()
class DictionaryComponentResponseOfuint32AndDestinyItemTalentGridComponent(BaseModel):
    """
    _No description given by bungie._

    None
    Attributes:
        data: _No description given by bungie._
        disabled: If true, this component is disabled.
        privacy: _No description given by bungie._
    """

    data: dict[int, "DestinyItemTalentGridComponent"] = custom_field(
        metadata={"type": """dict[int, DestinyItemTalentGridComponent]"""}
    )
    disabled: bool = custom_field()
    privacy: Union["ComponentPrivacySetting", int] = custom_field(converter=enum_converter("ComponentPrivacySetting"))


@custom_define()
class SearchResultOfDestinyEntitySearchResultItem(BaseModel):
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
    results: list["DestinyEntitySearchResultItem"] = custom_field(
        metadata={"type": """list[DestinyEntitySearchResultItem]"""}
    )
    total_results: int = custom_field()
    use_total_results: bool = custom_field()


@custom_define()
class SearchResultOfTrendingEntry(BaseModel):
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
    results: list["TrendingEntry"] = custom_field(metadata={"type": """list[TrendingEntry]"""})
    total_results: int = custom_field()
    use_total_results: bool = custom_field()


@custom_define()
class SearchResultOfFireteamSummary(BaseModel):
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
    results: list["FireteamSummary"] = custom_field(metadata={"type": """list[FireteamSummary]"""})
    total_results: int = custom_field()
    use_total_results: bool = custom_field()


@custom_define()
class SearchResultOfFireteamResponse(BaseModel):
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
    results: list["FireteamResponse"] = custom_field(metadata={"type": """list[FireteamResponse]"""})
    total_results: int = custom_field()
    use_total_results: bool = custom_field()


@custom_define()
class GlobalAlert(BaseModel):
    """
    _No description given by bungie._

    None
    Attributes:
        alert_html: _No description given by bungie._
        alert_key: _No description given by bungie._
        alert_level: _No description given by bungie._
        alert_link: _No description given by bungie._
        alert_timestamp: _No description given by bungie._
        alert_type: _No description given by bungie._
        stream_info: _No description given by bungie._
    """

    alert_html: str = custom_field()
    alert_key: str = custom_field()
    alert_level: Union["GlobalAlertLevel", int] = custom_field(converter=enum_converter("GlobalAlertLevel"))
    alert_link: str = custom_field()
    alert_timestamp: datetime = custom_field()
    alert_type: Union["GlobalAlertType", int] = custom_field(converter=enum_converter("GlobalAlertType"))
    stream_info: "StreamInfo" = custom_field()


class GlobalAlertLevel(BaseEnum):
    """
    _No description given by bungie._
    """

    UNKNOWN = 0
    """_No description given by bungie._ """
    BLUE = 1
    """_No description given by bungie._ """
    YELLOW = 2
    """_No description given by bungie._ """
    RED = 3
    """_No description given by bungie._ """


class GlobalAlertType(BaseEnum):
    """
    _No description given by bungie._
    """

    GLOBAL_ALERT = 0
    """_No description given by bungie._ """
    STREAMING_ALERT = 1
    """_No description given by bungie._ """


@custom_define()
class StreamInfo(BaseModel):
    """
    _No description given by bungie._

    None
    Attributes:
        channel_name: _No description given by bungie._
    """

    channel_name: str = custom_field()
