# DO NOT CHANGE ANY CODE BELOW
# This file is generated automatically by `generate_api_schema.py` and will be overwritten
# Instead, change functions / models by subclassing them in the `./overwrites/` folder. They will be used instead.

from datetime import datetime
from typing import TYPE_CHECKING, Union

import attr

from bungio.models.base import BaseEnum, BaseModel
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
        DestinyStringVariablesComponent,
        DestinyVendorCategoriesComponent,
        DestinyVendorComponent,
        DestinyVendorGroupComponent,
        DestinyVendorReceiptsComponent,
        DestinyVendorSaleItemComponent,
        FireteamResponse,
        FireteamSummary,
        GroupBan,
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


@attr.define
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

    has_more: bool = attr.field()
    query: "PagedQuery" = attr.field()
    replacement_continuation_token: str = attr.field()
    results: list["ContentItemPublicContract"] = attr.field(metadata={"type": """list[ContentItemPublicContract]"""})
    total_results: int = attr.field()
    use_total_results: bool = attr.field()


@attr.define
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

    has_more: bool = attr.field()
    query: "PagedQuery" = attr.field()
    replacement_continuation_token: str = attr.field()
    results: list["PostResponse"] = attr.field(metadata={"type": """list[PostResponse]"""})
    total_results: int = attr.field()
    use_total_results: bool = attr.field()


@attr.define
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

    has_more: bool = attr.field()
    query: "PagedQuery" = attr.field()
    replacement_continuation_token: str = attr.field()
    results: list["GroupV2Card"] = attr.field(metadata={"type": """list[GroupV2Card]"""})
    total_results: int = attr.field()
    use_total_results: bool = attr.field()


@attr.define
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

    has_more: bool = attr.field()
    query: "PagedQuery" = attr.field()
    replacement_continuation_token: str = attr.field()
    results: list["GroupMember"] = attr.field(metadata={"type": """list[GroupMember]"""})
    total_results: int = attr.field()
    use_total_results: bool = attr.field()


@attr.define
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

    has_more: bool = attr.field()
    query: "PagedQuery" = attr.field()
    replacement_continuation_token: str = attr.field()
    results: list["GroupBan"] = attr.field(metadata={"type": """list[GroupBan]"""})
    total_results: int = attr.field()
    use_total_results: bool = attr.field()


@attr.define
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

    has_more: bool = attr.field()
    query: "PagedQuery" = attr.field()
    replacement_continuation_token: str = attr.field()
    results: list["GroupMemberApplication"] = attr.field(metadata={"type": """list[GroupMemberApplication]"""})
    total_results: int = attr.field()
    use_total_results: bool = attr.field()


@attr.define
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

    has_more: bool = attr.field()
    query: "PagedQuery" = attr.field()
    replacement_continuation_token: str = attr.field()
    results: list["GroupMembership"] = attr.field(metadata={"type": """list[GroupMembership]"""})
    total_results: int = attr.field()
    use_total_results: bool = attr.field()


@attr.define
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

    has_more: bool = attr.field()
    query: "PagedQuery" = attr.field()
    replacement_continuation_token: str = attr.field()
    results: list["GroupPotentialMembership"] = attr.field(metadata={"type": """list[GroupPotentialMembership]"""})
    total_results: int = attr.field()
    use_total_results: bool = attr.field()


@attr.define
class SingleComponentResponseOfDestinyVendorReceiptsComponent(BaseModel):
    """
    _No description given by bungie._

    None
    Attributes:
        data: _No description given by bungie._
        disabled: If true, this component is disabled.
        privacy: _No description given by bungie._
    """

    data: "DestinyVendorReceiptsComponent" = attr.field()
    disabled: bool = attr.field()
    privacy: Union["ComponentPrivacySetting", int] = attr.field(converter=enum_converter("ComponentPrivacySetting"))


@attr.define
class SingleComponentResponseOfDestinyInventoryComponent(BaseModel):
    """
    _No description given by bungie._

    None
    Attributes:
        data: _No description given by bungie._
        disabled: If true, this component is disabled.
        privacy: _No description given by bungie._
    """

    data: "DestinyInventoryComponent" = attr.field()
    disabled: bool = attr.field()
    privacy: Union["ComponentPrivacySetting", int] = attr.field(converter=enum_converter("ComponentPrivacySetting"))


@attr.define
class SingleComponentResponseOfDestinyProfileComponent(BaseModel):
    """
    _No description given by bungie._

    None
    Attributes:
        data: _No description given by bungie._
        disabled: If true, this component is disabled.
        privacy: _No description given by bungie._
    """

    data: "DestinyProfileComponent" = attr.field()
    disabled: bool = attr.field()
    privacy: Union["ComponentPrivacySetting", int] = attr.field(converter=enum_converter("ComponentPrivacySetting"))


@attr.define
class SingleComponentResponseOfDestinyPlatformSilverComponent(BaseModel):
    """
    _No description given by bungie._

    None
    Attributes:
        data: _No description given by bungie._
        disabled: If true, this component is disabled.
        privacy: _No description given by bungie._
    """

    data: "DestinyPlatformSilverComponent" = attr.field()
    disabled: bool = attr.field()
    privacy: Union["ComponentPrivacySetting", int] = attr.field(converter=enum_converter("ComponentPrivacySetting"))


@attr.define
class SingleComponentResponseOfDestinyKiosksComponent(BaseModel):
    """
    _No description given by bungie._

    None
    Attributes:
        data: _No description given by bungie._
        disabled: If true, this component is disabled.
        privacy: _No description given by bungie._
    """

    data: "DestinyKiosksComponent" = attr.field()
    disabled: bool = attr.field()
    privacy: Union["ComponentPrivacySetting", int] = attr.field(converter=enum_converter("ComponentPrivacySetting"))


@attr.define
class SingleComponentResponseOfDestinyPlugSetsComponent(BaseModel):
    """
    _No description given by bungie._

    None
    Attributes:
        data: _No description given by bungie._
        disabled: If true, this component is disabled.
        privacy: _No description given by bungie._
    """

    data: "DestinyPlugSetsComponent" = attr.field()
    disabled: bool = attr.field()
    privacy: Union["ComponentPrivacySetting", int] = attr.field(converter=enum_converter("ComponentPrivacySetting"))


@attr.define
class SingleComponentResponseOfDestinyProfileProgressionComponent(BaseModel):
    """
    _No description given by bungie._

    None
    Attributes:
        data: _No description given by bungie._
        disabled: If true, this component is disabled.
        privacy: _No description given by bungie._
    """

    data: "DestinyProfileProgressionComponent" = attr.field()
    disabled: bool = attr.field()
    privacy: Union["ComponentPrivacySetting", int] = attr.field(converter=enum_converter("ComponentPrivacySetting"))


@attr.define
class SingleComponentResponseOfDestinyPresentationNodesComponent(BaseModel):
    """
    _No description given by bungie._

    None
    Attributes:
        data: _No description given by bungie._
        disabled: If true, this component is disabled.
        privacy: _No description given by bungie._
    """

    data: "DestinyPresentationNodesComponent" = attr.field()
    disabled: bool = attr.field()
    privacy: Union["ComponentPrivacySetting", int] = attr.field(converter=enum_converter("ComponentPrivacySetting"))


@attr.define
class SingleComponentResponseOfDestinyProfileRecordsComponent(BaseModel):
    """
    _No description given by bungie._

    None
    Attributes:
        data: _No description given by bungie._
        disabled: If true, this component is disabled.
        privacy: _No description given by bungie._
    """

    data: "DestinyProfileRecordsComponent" = attr.field()
    disabled: bool = attr.field()
    privacy: Union["ComponentPrivacySetting", int] = attr.field(converter=enum_converter("ComponentPrivacySetting"))


@attr.define
class SingleComponentResponseOfDestinyProfileCollectiblesComponent(BaseModel):
    """
    _No description given by bungie._

    None
    Attributes:
        data: _No description given by bungie._
        disabled: If true, this component is disabled.
        privacy: _No description given by bungie._
    """

    data: "DestinyProfileCollectiblesComponent" = attr.field()
    disabled: bool = attr.field()
    privacy: Union["ComponentPrivacySetting", int] = attr.field(converter=enum_converter("ComponentPrivacySetting"))


@attr.define
class SingleComponentResponseOfDestinyProfileTransitoryComponent(BaseModel):
    """
    _No description given by bungie._

    None
    Attributes:
        data: _No description given by bungie._
        disabled: If true, this component is disabled.
        privacy: _No description given by bungie._
    """

    data: "DestinyProfileTransitoryComponent" = attr.field()
    disabled: bool = attr.field()
    privacy: Union["ComponentPrivacySetting", int] = attr.field(converter=enum_converter("ComponentPrivacySetting"))


@attr.define
class SingleComponentResponseOfDestinyMetricsComponent(BaseModel):
    """
    _No description given by bungie._

    None
    Attributes:
        data: _No description given by bungie._
        disabled: If true, this component is disabled.
        privacy: _No description given by bungie._
    """

    data: "DestinyMetricsComponent" = attr.field()
    disabled: bool = attr.field()
    privacy: Union["ComponentPrivacySetting", int] = attr.field(converter=enum_converter("ComponentPrivacySetting"))


@attr.define
class SingleComponentResponseOfDestinyStringVariablesComponent(BaseModel):
    """
    _No description given by bungie._

    None
    Attributes:
        data: _No description given by bungie._
        disabled: If true, this component is disabled.
        privacy: _No description given by bungie._
    """

    data: "DestinyStringVariablesComponent" = attr.field()
    disabled: bool = attr.field()
    privacy: Union["ComponentPrivacySetting", int] = attr.field(converter=enum_converter("ComponentPrivacySetting"))


@attr.define
class DictionaryComponentResponseOfint64AndDestinyCharacterComponent(BaseModel):
    """
    _No description given by bungie._

    None
    Attributes:
        data: _No description given by bungie._
        disabled: If true, this component is disabled.
        privacy: _No description given by bungie._
    """

    data: dict[int, "DestinyCharacterComponent"] = attr.field(
        metadata={"type": """dict[int, DestinyCharacterComponent]"""}
    )
    disabled: bool = attr.field()
    privacy: Union["ComponentPrivacySetting", int] = attr.field(converter=enum_converter("ComponentPrivacySetting"))


@attr.define
class DictionaryComponentResponseOfint64AndDestinyInventoryComponent(BaseModel):
    """
    _No description given by bungie._

    None
    Attributes:
        data: _No description given by bungie._
        disabled: If true, this component is disabled.
        privacy: _No description given by bungie._
    """

    data: dict[int, "DestinyInventoryComponent"] = attr.field(
        metadata={"type": """dict[int, DestinyInventoryComponent]"""}
    )
    disabled: bool = attr.field()
    privacy: Union["ComponentPrivacySetting", int] = attr.field(converter=enum_converter("ComponentPrivacySetting"))


@attr.define
class DictionaryComponentResponseOfint64AndDestinyCharacterProgressionComponent(BaseModel):
    """
    _No description given by bungie._

    None
    Attributes:
        data: _No description given by bungie._
        disabled: If true, this component is disabled.
        privacy: _No description given by bungie._
    """

    data: dict[int, "DestinyCharacterProgressionComponent"] = attr.field(
        metadata={"type": """dict[int, DestinyCharacterProgressionComponent]"""}
    )
    disabled: bool = attr.field()
    privacy: Union["ComponentPrivacySetting", int] = attr.field(converter=enum_converter("ComponentPrivacySetting"))


@attr.define
class DictionaryComponentResponseOfint64AndDestinyCharacterRenderComponent(BaseModel):
    """
    _No description given by bungie._

    None
    Attributes:
        data: _No description given by bungie._
        disabled: If true, this component is disabled.
        privacy: _No description given by bungie._
    """

    data: dict[int, "DestinyCharacterRenderComponent"] = attr.field(
        metadata={"type": """dict[int, DestinyCharacterRenderComponent]"""}
    )
    disabled: bool = attr.field()
    privacy: Union["ComponentPrivacySetting", int] = attr.field(converter=enum_converter("ComponentPrivacySetting"))


@attr.define
class DictionaryComponentResponseOfint64AndDestinyCharacterActivitiesComponent(BaseModel):
    """
    _No description given by bungie._

    None
    Attributes:
        data: _No description given by bungie._
        disabled: If true, this component is disabled.
        privacy: _No description given by bungie._
    """

    data: dict[int, "DestinyCharacterActivitiesComponent"] = attr.field(
        metadata={"type": """dict[int, DestinyCharacterActivitiesComponent]"""}
    )
    disabled: bool = attr.field()
    privacy: Union["ComponentPrivacySetting", int] = attr.field(converter=enum_converter("ComponentPrivacySetting"))


@attr.define
class DictionaryComponentResponseOfint64AndDestinyKiosksComponent(BaseModel):
    """
    _No description given by bungie._

    None
    Attributes:
        data: _No description given by bungie._
        disabled: If true, this component is disabled.
        privacy: _No description given by bungie._
    """

    data: dict[int, "DestinyKiosksComponent"] = attr.field(metadata={"type": """dict[int, DestinyKiosksComponent]"""})
    disabled: bool = attr.field()
    privacy: Union["ComponentPrivacySetting", int] = attr.field(converter=enum_converter("ComponentPrivacySetting"))


@attr.define
class DictionaryComponentResponseOfint64AndDestinyPlugSetsComponent(BaseModel):
    """
    _No description given by bungie._

    None
    Attributes:
        data: _No description given by bungie._
        disabled: If true, this component is disabled.
        privacy: _No description given by bungie._
    """

    data: dict[int, "DestinyPlugSetsComponent"] = attr.field(
        metadata={"type": """dict[int, DestinyPlugSetsComponent]"""}
    )
    disabled: bool = attr.field()
    privacy: Union["ComponentPrivacySetting", int] = attr.field(converter=enum_converter("ComponentPrivacySetting"))


@attr.define
class DestinyBaseItemComponentSetOfuint32(BaseModel):
    """
    _No description given by bungie._

    None
    Attributes:
        objectives: _No description given by bungie._
        perks: _No description given by bungie._
    """

    objectives: "DictionaryComponentResponseOfuint32AndDestinyItemObjectivesComponent" = attr.field()
    perks: "DictionaryComponentResponseOfuint32AndDestinyItemPerksComponent" = attr.field()


@attr.define
class DictionaryComponentResponseOfuint32AndDestinyItemObjectivesComponent(BaseModel):
    """
    _No description given by bungie._

    None
    Attributes:
        data: _No description given by bungie._
        disabled: If true, this component is disabled.
        privacy: _No description given by bungie._
    """

    data: dict[int, "DestinyItemObjectivesComponent"] = attr.field(
        metadata={"type": """dict[int, DestinyItemObjectivesComponent]"""}
    )
    disabled: bool = attr.field()
    privacy: Union["ComponentPrivacySetting", int] = attr.field(converter=enum_converter("ComponentPrivacySetting"))


@attr.define
class DictionaryComponentResponseOfuint32AndDestinyItemPerksComponent(BaseModel):
    """
    _No description given by bungie._

    None
    Attributes:
        data: _No description given by bungie._
        disabled: If true, this component is disabled.
        privacy: _No description given by bungie._
    """

    data: dict[int, "DestinyItemPerksComponent"] = attr.field(
        metadata={"type": """dict[int, DestinyItemPerksComponent]"""}
    )
    disabled: bool = attr.field()
    privacy: Union["ComponentPrivacySetting", int] = attr.field(converter=enum_converter("ComponentPrivacySetting"))


@attr.define
class DictionaryComponentResponseOfint64AndDestinyPresentationNodesComponent(BaseModel):
    """
    _No description given by bungie._

    None
    Attributes:
        data: _No description given by bungie._
        disabled: If true, this component is disabled.
        privacy: _No description given by bungie._
    """

    data: dict[int, "DestinyPresentationNodesComponent"] = attr.field(
        metadata={"type": """dict[int, DestinyPresentationNodesComponent]"""}
    )
    disabled: bool = attr.field()
    privacy: Union["ComponentPrivacySetting", int] = attr.field(converter=enum_converter("ComponentPrivacySetting"))


@attr.define
class DictionaryComponentResponseOfint64AndDestinyCharacterRecordsComponent(BaseModel):
    """
    _No description given by bungie._

    None
    Attributes:
        data: _No description given by bungie._
        disabled: If true, this component is disabled.
        privacy: _No description given by bungie._
    """

    data: dict[int, "DestinyCharacterRecordsComponent"] = attr.field(
        metadata={"type": """dict[int, DestinyCharacterRecordsComponent]"""}
    )
    disabled: bool = attr.field()
    privacy: Union["ComponentPrivacySetting", int] = attr.field(converter=enum_converter("ComponentPrivacySetting"))


@attr.define
class DictionaryComponentResponseOfint64AndDestinyCollectiblesComponent(BaseModel):
    """
    _No description given by bungie._

    None
    Attributes:
        data: _No description given by bungie._
        disabled: If true, this component is disabled.
        privacy: _No description given by bungie._
    """

    data: dict[int, "DestinyCollectiblesComponent"] = attr.field(
        metadata={"type": """dict[int, DestinyCollectiblesComponent]"""}
    )
    disabled: bool = attr.field()
    privacy: Union["ComponentPrivacySetting", int] = attr.field(converter=enum_converter("ComponentPrivacySetting"))


@attr.define
class DictionaryComponentResponseOfint64AndDestinyStringVariablesComponent(BaseModel):
    """
    _No description given by bungie._

    None
    Attributes:
        data: _No description given by bungie._
        disabled: If true, this component is disabled.
        privacy: _No description given by bungie._
    """

    data: dict[int, "DestinyStringVariablesComponent"] = attr.field(
        metadata={"type": """dict[int, DestinyStringVariablesComponent]"""}
    )
    disabled: bool = attr.field()
    privacy: Union["ComponentPrivacySetting", int] = attr.field(converter=enum_converter("ComponentPrivacySetting"))


@attr.define
class DictionaryComponentResponseOfint64AndDestinyCraftablesComponent(BaseModel):
    """
    _No description given by bungie._

    None
    Attributes:
        data: _No description given by bungie._
        disabled: If true, this component is disabled.
        privacy: _No description given by bungie._
    """

    data: dict[int, "DestinyCraftablesComponent"] = attr.field(
        metadata={"type": """dict[int, DestinyCraftablesComponent]"""}
    )
    disabled: bool = attr.field()
    privacy: Union["ComponentPrivacySetting", int] = attr.field(converter=enum_converter("ComponentPrivacySetting"))


@attr.define
class DestinyBaseItemComponentSetOfint64(BaseModel):
    """
    _No description given by bungie._

    None
    Attributes:
        objectives: _No description given by bungie._
        perks: _No description given by bungie._
    """

    objectives: "DictionaryComponentResponseOfint64AndDestinyItemObjectivesComponent" = attr.field()
    perks: "DictionaryComponentResponseOfint64AndDestinyItemPerksComponent" = attr.field()


@attr.define
class DictionaryComponentResponseOfint64AndDestinyItemObjectivesComponent(BaseModel):
    """
    _No description given by bungie._

    None
    Attributes:
        data: _No description given by bungie._
        disabled: If true, this component is disabled.
        privacy: _No description given by bungie._
    """

    data: dict[int, "DestinyItemObjectivesComponent"] = attr.field(
        metadata={"type": """dict[int, DestinyItemObjectivesComponent]"""}
    )
    disabled: bool = attr.field()
    privacy: Union["ComponentPrivacySetting", int] = attr.field(converter=enum_converter("ComponentPrivacySetting"))


@attr.define
class DictionaryComponentResponseOfint64AndDestinyItemPerksComponent(BaseModel):
    """
    _No description given by bungie._

    None
    Attributes:
        data: _No description given by bungie._
        disabled: If true, this component is disabled.
        privacy: _No description given by bungie._
    """

    data: dict[int, "DestinyItemPerksComponent"] = attr.field(
        metadata={"type": """dict[int, DestinyItemPerksComponent]"""}
    )
    disabled: bool = attr.field()
    privacy: Union["ComponentPrivacySetting", int] = attr.field(converter=enum_converter("ComponentPrivacySetting"))


@attr.define
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

    instances: "DictionaryComponentResponseOfint64AndDestinyItemInstanceComponent" = attr.field()
    objectives: "DictionaryComponentResponseOfint64AndDestinyItemObjectivesComponent" = attr.field()
    perks: "DictionaryComponentResponseOfint64AndDestinyItemPerksComponent" = attr.field()
    plug_objectives: "DictionaryComponentResponseOfint64AndDestinyItemPlugObjectivesComponent" = attr.field()
    plug_states: "DictionaryComponentResponseOfuint32AndDestinyItemPlugComponent" = attr.field()
    render_data: "DictionaryComponentResponseOfint64AndDestinyItemRenderComponent" = attr.field()
    reusable_plugs: "DictionaryComponentResponseOfint64AndDestinyItemReusablePlugsComponent" = attr.field()
    sockets: "DictionaryComponentResponseOfint64AndDestinyItemSocketsComponent" = attr.field()
    stats: "DictionaryComponentResponseOfint64AndDestinyItemStatsComponent" = attr.field()
    talent_grids: "DictionaryComponentResponseOfint64AndDestinyItemTalentGridComponent" = attr.field()


@attr.define
class DictionaryComponentResponseOfint64AndDestinyItemInstanceComponent(BaseModel):
    """
    _No description given by bungie._

    None
    Attributes:
        data: _No description given by bungie._
        disabled: If true, this component is disabled.
        privacy: _No description given by bungie._
    """

    data: dict[int, "DestinyItemInstanceComponent"] = attr.field(
        metadata={"type": """dict[int, DestinyItemInstanceComponent]"""}
    )
    disabled: bool = attr.field()
    privacy: Union["ComponentPrivacySetting", int] = attr.field(converter=enum_converter("ComponentPrivacySetting"))


@attr.define
class DictionaryComponentResponseOfint64AndDestinyItemRenderComponent(BaseModel):
    """
    _No description given by bungie._

    None
    Attributes:
        data: _No description given by bungie._
        disabled: If true, this component is disabled.
        privacy: _No description given by bungie._
    """

    data: dict[int, "DestinyItemRenderComponent"] = attr.field(
        metadata={"type": """dict[int, DestinyItemRenderComponent]"""}
    )
    disabled: bool = attr.field()
    privacy: Union["ComponentPrivacySetting", int] = attr.field(converter=enum_converter("ComponentPrivacySetting"))


@attr.define
class DictionaryComponentResponseOfint64AndDestinyItemStatsComponent(BaseModel):
    """
    _No description given by bungie._

    None
    Attributes:
        data: _No description given by bungie._
        disabled: If true, this component is disabled.
        privacy: _No description given by bungie._
    """

    data: dict[int, "DestinyItemStatsComponent"] = attr.field(
        metadata={"type": """dict[int, DestinyItemStatsComponent]"""}
    )
    disabled: bool = attr.field()
    privacy: Union["ComponentPrivacySetting", int] = attr.field(converter=enum_converter("ComponentPrivacySetting"))


@attr.define
class DictionaryComponentResponseOfint64AndDestinyItemSocketsComponent(BaseModel):
    """
    _No description given by bungie._

    None
    Attributes:
        data: _No description given by bungie._
        disabled: If true, this component is disabled.
        privacy: _No description given by bungie._
    """

    data: dict[int, "DestinyItemSocketsComponent"] = attr.field(
        metadata={"type": """dict[int, DestinyItemSocketsComponent]"""}
    )
    disabled: bool = attr.field()
    privacy: Union["ComponentPrivacySetting", int] = attr.field(converter=enum_converter("ComponentPrivacySetting"))


@attr.define
class DictionaryComponentResponseOfint64AndDestinyItemReusablePlugsComponent(BaseModel):
    """
    _No description given by bungie._

    None
    Attributes:
        data: _No description given by bungie._
        disabled: If true, this component is disabled.
        privacy: _No description given by bungie._
    """

    data: dict[int, "DestinyItemReusablePlugsComponent"] = attr.field(
        metadata={"type": """dict[int, DestinyItemReusablePlugsComponent]"""}
    )
    disabled: bool = attr.field()
    privacy: Union["ComponentPrivacySetting", int] = attr.field(converter=enum_converter("ComponentPrivacySetting"))


@attr.define
class DictionaryComponentResponseOfint64AndDestinyItemPlugObjectivesComponent(BaseModel):
    """
    _No description given by bungie._

    None
    Attributes:
        data: _No description given by bungie._
        disabled: If true, this component is disabled.
        privacy: _No description given by bungie._
    """

    data: dict[int, "DestinyItemPlugObjectivesComponent"] = attr.field(
        metadata={"type": """dict[int, DestinyItemPlugObjectivesComponent]"""}
    )
    disabled: bool = attr.field()
    privacy: Union["ComponentPrivacySetting", int] = attr.field(converter=enum_converter("ComponentPrivacySetting"))


@attr.define
class DictionaryComponentResponseOfint64AndDestinyItemTalentGridComponent(BaseModel):
    """
    _No description given by bungie._

    None
    Attributes:
        data: _No description given by bungie._
        disabled: If true, this component is disabled.
        privacy: _No description given by bungie._
    """

    data: dict[int, "DestinyItemTalentGridComponent"] = attr.field(
        metadata={"type": """dict[int, DestinyItemTalentGridComponent]"""}
    )
    disabled: bool = attr.field()
    privacy: Union["ComponentPrivacySetting", int] = attr.field(converter=enum_converter("ComponentPrivacySetting"))


@attr.define
class DictionaryComponentResponseOfuint32AndDestinyItemPlugComponent(BaseModel):
    """
    _No description given by bungie._

    None
    Attributes:
        data: _No description given by bungie._
        disabled: If true, this component is disabled.
        privacy: _No description given by bungie._
    """

    data: dict[int, "DestinyItemPlugComponent"] = attr.field(
        metadata={"type": """dict[int, DestinyItemPlugComponent]"""}
    )
    disabled: bool = attr.field()
    privacy: Union["ComponentPrivacySetting", int] = attr.field(converter=enum_converter("ComponentPrivacySetting"))


@attr.define
class DictionaryComponentResponseOfint64AndDestinyCurrenciesComponent(BaseModel):
    """
    _No description given by bungie._

    None
    Attributes:
        data: _No description given by bungie._
        disabled: If true, this component is disabled.
        privacy: _No description given by bungie._
    """

    data: dict[int, "DestinyCurrenciesComponent"] = attr.field(
        metadata={"type": """dict[int, DestinyCurrenciesComponent]"""}
    )
    disabled: bool = attr.field()
    privacy: Union["ComponentPrivacySetting", int] = attr.field(converter=enum_converter("ComponentPrivacySetting"))


@attr.define
class SingleComponentResponseOfDestinyCharacterComponent(BaseModel):
    """
    _No description given by bungie._

    None
    Attributes:
        data: _No description given by bungie._
        disabled: If true, this component is disabled.
        privacy: _No description given by bungie._
    """

    data: "DestinyCharacterComponent" = attr.field()
    disabled: bool = attr.field()
    privacy: Union["ComponentPrivacySetting", int] = attr.field(converter=enum_converter("ComponentPrivacySetting"))


@attr.define
class SingleComponentResponseOfDestinyCharacterProgressionComponent(BaseModel):
    """
    _No description given by bungie._

    None
    Attributes:
        data: _No description given by bungie._
        disabled: If true, this component is disabled.
        privacy: _No description given by bungie._
    """

    data: "DestinyCharacterProgressionComponent" = attr.field()
    disabled: bool = attr.field()
    privacy: Union["ComponentPrivacySetting", int] = attr.field(converter=enum_converter("ComponentPrivacySetting"))


@attr.define
class SingleComponentResponseOfDestinyCharacterRenderComponent(BaseModel):
    """
    _No description given by bungie._

    None
    Attributes:
        data: _No description given by bungie._
        disabled: If true, this component is disabled.
        privacy: _No description given by bungie._
    """

    data: "DestinyCharacterRenderComponent" = attr.field()
    disabled: bool = attr.field()
    privacy: Union["ComponentPrivacySetting", int] = attr.field(converter=enum_converter("ComponentPrivacySetting"))


@attr.define
class SingleComponentResponseOfDestinyCharacterActivitiesComponent(BaseModel):
    """
    _No description given by bungie._

    None
    Attributes:
        data: _No description given by bungie._
        disabled: If true, this component is disabled.
        privacy: _No description given by bungie._
    """

    data: "DestinyCharacterActivitiesComponent" = attr.field()
    disabled: bool = attr.field()
    privacy: Union["ComponentPrivacySetting", int] = attr.field(converter=enum_converter("ComponentPrivacySetting"))


@attr.define
class SingleComponentResponseOfDestinyCharacterRecordsComponent(BaseModel):
    """
    _No description given by bungie._

    None
    Attributes:
        data: _No description given by bungie._
        disabled: If true, this component is disabled.
        privacy: _No description given by bungie._
    """

    data: "DestinyCharacterRecordsComponent" = attr.field()
    disabled: bool = attr.field()
    privacy: Union["ComponentPrivacySetting", int] = attr.field(converter=enum_converter("ComponentPrivacySetting"))


@attr.define
class SingleComponentResponseOfDestinyCollectiblesComponent(BaseModel):
    """
    _No description given by bungie._

    None
    Attributes:
        data: _No description given by bungie._
        disabled: If true, this component is disabled.
        privacy: _No description given by bungie._
    """

    data: "DestinyCollectiblesComponent" = attr.field()
    disabled: bool = attr.field()
    privacy: Union["ComponentPrivacySetting", int] = attr.field(converter=enum_converter("ComponentPrivacySetting"))


@attr.define
class SingleComponentResponseOfDestinyCurrenciesComponent(BaseModel):
    """
    _No description given by bungie._

    None
    Attributes:
        data: _No description given by bungie._
        disabled: If true, this component is disabled.
        privacy: _No description given by bungie._
    """

    data: "DestinyCurrenciesComponent" = attr.field()
    disabled: bool = attr.field()
    privacy: Union["ComponentPrivacySetting", int] = attr.field(converter=enum_converter("ComponentPrivacySetting"))


@attr.define
class SingleComponentResponseOfDestinyItemComponent(BaseModel):
    """
    _No description given by bungie._

    None
    Attributes:
        data: _No description given by bungie._
        disabled: If true, this component is disabled.
        privacy: _No description given by bungie._
    """

    data: "DestinyItemComponent" = attr.field()
    disabled: bool = attr.field()
    privacy: Union["ComponentPrivacySetting", int] = attr.field(converter=enum_converter("ComponentPrivacySetting"))


@attr.define
class SingleComponentResponseOfDestinyItemInstanceComponent(BaseModel):
    """
    _No description given by bungie._

    None
    Attributes:
        data: _No description given by bungie._
        disabled: If true, this component is disabled.
        privacy: _No description given by bungie._
    """

    data: "DestinyItemInstanceComponent" = attr.field()
    disabled: bool = attr.field()
    privacy: Union["ComponentPrivacySetting", int] = attr.field(converter=enum_converter("ComponentPrivacySetting"))


@attr.define
class SingleComponentResponseOfDestinyItemObjectivesComponent(BaseModel):
    """
    _No description given by bungie._

    None
    Attributes:
        data: _No description given by bungie._
        disabled: If true, this component is disabled.
        privacy: _No description given by bungie._
    """

    data: "DestinyItemObjectivesComponent" = attr.field()
    disabled: bool = attr.field()
    privacy: Union["ComponentPrivacySetting", int] = attr.field(converter=enum_converter("ComponentPrivacySetting"))


@attr.define
class SingleComponentResponseOfDestinyItemPerksComponent(BaseModel):
    """
    _No description given by bungie._

    None
    Attributes:
        data: _No description given by bungie._
        disabled: If true, this component is disabled.
        privacy: _No description given by bungie._
    """

    data: "DestinyItemPerksComponent" = attr.field()
    disabled: bool = attr.field()
    privacy: Union["ComponentPrivacySetting", int] = attr.field(converter=enum_converter("ComponentPrivacySetting"))


@attr.define
class SingleComponentResponseOfDestinyItemRenderComponent(BaseModel):
    """
    _No description given by bungie._

    None
    Attributes:
        data: _No description given by bungie._
        disabled: If true, this component is disabled.
        privacy: _No description given by bungie._
    """

    data: "DestinyItemRenderComponent" = attr.field()
    disabled: bool = attr.field()
    privacy: Union["ComponentPrivacySetting", int] = attr.field(converter=enum_converter("ComponentPrivacySetting"))


@attr.define
class SingleComponentResponseOfDestinyItemStatsComponent(BaseModel):
    """
    _No description given by bungie._

    None
    Attributes:
        data: _No description given by bungie._
        disabled: If true, this component is disabled.
        privacy: _No description given by bungie._
    """

    data: "DestinyItemStatsComponent" = attr.field()
    disabled: bool = attr.field()
    privacy: Union["ComponentPrivacySetting", int] = attr.field(converter=enum_converter("ComponentPrivacySetting"))


@attr.define
class SingleComponentResponseOfDestinyItemTalentGridComponent(BaseModel):
    """
    _No description given by bungie._

    None
    Attributes:
        data: _No description given by bungie._
        disabled: If true, this component is disabled.
        privacy: _No description given by bungie._
    """

    data: "DestinyItemTalentGridComponent" = attr.field()
    disabled: bool = attr.field()
    privacy: Union["ComponentPrivacySetting", int] = attr.field(converter=enum_converter("ComponentPrivacySetting"))


@attr.define
class SingleComponentResponseOfDestinyItemSocketsComponent(BaseModel):
    """
    _No description given by bungie._

    None
    Attributes:
        data: _No description given by bungie._
        disabled: If true, this component is disabled.
        privacy: _No description given by bungie._
    """

    data: "DestinyItemSocketsComponent" = attr.field()
    disabled: bool = attr.field()
    privacy: Union["ComponentPrivacySetting", int] = attr.field(converter=enum_converter("ComponentPrivacySetting"))


@attr.define
class SingleComponentResponseOfDestinyItemReusablePlugsComponent(BaseModel):
    """
    _No description given by bungie._

    None
    Attributes:
        data: _No description given by bungie._
        disabled: If true, this component is disabled.
        privacy: _No description given by bungie._
    """

    data: "DestinyItemReusablePlugsComponent" = attr.field()
    disabled: bool = attr.field()
    privacy: Union["ComponentPrivacySetting", int] = attr.field(converter=enum_converter("ComponentPrivacySetting"))


@attr.define
class SingleComponentResponseOfDestinyItemPlugObjectivesComponent(BaseModel):
    """
    _No description given by bungie._

    None
    Attributes:
        data: _No description given by bungie._
        disabled: If true, this component is disabled.
        privacy: _No description given by bungie._
    """

    data: "DestinyItemPlugObjectivesComponent" = attr.field()
    disabled: bool = attr.field()
    privacy: Union["ComponentPrivacySetting", int] = attr.field(converter=enum_converter("ComponentPrivacySetting"))


@attr.define
class SingleComponentResponseOfDestinyVendorGroupComponent(BaseModel):
    """
    _No description given by bungie._

    None
    Attributes:
        data: _No description given by bungie._
        disabled: If true, this component is disabled.
        privacy: _No description given by bungie._
    """

    data: "DestinyVendorGroupComponent" = attr.field()
    disabled: bool = attr.field()
    privacy: Union["ComponentPrivacySetting", int] = attr.field(converter=enum_converter("ComponentPrivacySetting"))


@attr.define
class DictionaryComponentResponseOfuint32AndDestinyVendorComponent(BaseModel):
    """
    _No description given by bungie._

    None
    Attributes:
        data: _No description given by bungie._
        disabled: If true, this component is disabled.
        privacy: _No description given by bungie._
    """

    data: dict[int, "DestinyVendorComponent"] = attr.field(metadata={"type": """dict[int, DestinyVendorComponent]"""})
    disabled: bool = attr.field()
    privacy: Union["ComponentPrivacySetting", int] = attr.field(converter=enum_converter("ComponentPrivacySetting"))


@attr.define
class DictionaryComponentResponseOfuint32AndDestinyVendorCategoriesComponent(BaseModel):
    """
    _No description given by bungie._

    None
    Attributes:
        data: _No description given by bungie._
        disabled: If true, this component is disabled.
        privacy: _No description given by bungie._
    """

    data: dict[int, "DestinyVendorCategoriesComponent"] = attr.field(
        metadata={"type": """dict[int, DestinyVendorCategoriesComponent]"""}
    )
    disabled: bool = attr.field()
    privacy: Union["ComponentPrivacySetting", int] = attr.field(converter=enum_converter("ComponentPrivacySetting"))


@attr.define
class DestinyVendorSaleItemSetComponentOfDestinyVendorSaleItemComponent(BaseModel):
    """
    _No description given by bungie._

    None
    Attributes:
        sale_items: _No description given by bungie._
    """

    sale_items: dict[int, "DestinyVendorSaleItemComponent"] = attr.field(
        metadata={"type": """dict[int, DestinyVendorSaleItemComponent]"""}
    )


@attr.define
class DictionaryComponentResponseOfuint32AndPersonalDestinyVendorSaleItemSetComponent(BaseModel):
    """
    _No description given by bungie._

    None
    Attributes:
        data: _No description given by bungie._
        disabled: If true, this component is disabled.
        privacy: _No description given by bungie._
    """

    data: dict[int, "PersonalDestinyVendorSaleItemSetComponent"] = attr.field(
        metadata={"type": """dict[int, PersonalDestinyVendorSaleItemSetComponent]"""}
    )
    disabled: bool = attr.field()
    privacy: Union["ComponentPrivacySetting", int] = attr.field(converter=enum_converter("ComponentPrivacySetting"))


@attr.define
class DestinyBaseItemComponentSetOfint32(BaseModel):
    """
    _No description given by bungie._

    None
    Attributes:
        objectives: _No description given by bungie._
        perks: _No description given by bungie._
    """

    objectives: "DictionaryComponentResponseOfint32AndDestinyItemObjectivesComponent" = attr.field()
    perks: "DictionaryComponentResponseOfint32AndDestinyItemPerksComponent" = attr.field()


@attr.define
class DictionaryComponentResponseOfint32AndDestinyItemObjectivesComponent(BaseModel):
    """
    _No description given by bungie._

    None
    Attributes:
        data: _No description given by bungie._
        disabled: If true, this component is disabled.
        privacy: _No description given by bungie._
    """

    data: dict[int, "DestinyItemObjectivesComponent"] = attr.field(
        metadata={"type": """dict[int, DestinyItemObjectivesComponent]"""}
    )
    disabled: bool = attr.field()
    privacy: Union["ComponentPrivacySetting", int] = attr.field(converter=enum_converter("ComponentPrivacySetting"))


@attr.define
class DictionaryComponentResponseOfint32AndDestinyItemPerksComponent(BaseModel):
    """
    _No description given by bungie._

    None
    Attributes:
        data: _No description given by bungie._
        disabled: If true, this component is disabled.
        privacy: _No description given by bungie._
    """

    data: dict[int, "DestinyItemPerksComponent"] = attr.field(
        metadata={"type": """dict[int, DestinyItemPerksComponent]"""}
    )
    disabled: bool = attr.field()
    privacy: Union["ComponentPrivacySetting", int] = attr.field(converter=enum_converter("ComponentPrivacySetting"))


@attr.define
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

    instances: "DictionaryComponentResponseOfint32AndDestinyItemInstanceComponent" = attr.field()
    objectives: "DictionaryComponentResponseOfint32AndDestinyItemObjectivesComponent" = attr.field()
    perks: "DictionaryComponentResponseOfint32AndDestinyItemPerksComponent" = attr.field()
    plug_objectives: "DictionaryComponentResponseOfint32AndDestinyItemPlugObjectivesComponent" = attr.field()
    plug_states: "DictionaryComponentResponseOfuint32AndDestinyItemPlugComponent" = attr.field()
    render_data: "DictionaryComponentResponseOfint32AndDestinyItemRenderComponent" = attr.field()
    reusable_plugs: "DictionaryComponentResponseOfint32AndDestinyItemReusablePlugsComponent" = attr.field()
    sockets: "DictionaryComponentResponseOfint32AndDestinyItemSocketsComponent" = attr.field()
    stats: "DictionaryComponentResponseOfint32AndDestinyItemStatsComponent" = attr.field()
    talent_grids: "DictionaryComponentResponseOfint32AndDestinyItemTalentGridComponent" = attr.field()


@attr.define
class DictionaryComponentResponseOfint32AndDestinyItemInstanceComponent(BaseModel):
    """
    _No description given by bungie._

    None
    Attributes:
        data: _No description given by bungie._
        disabled: If true, this component is disabled.
        privacy: _No description given by bungie._
    """

    data: dict[int, "DestinyItemInstanceComponent"] = attr.field(
        metadata={"type": """dict[int, DestinyItemInstanceComponent]"""}
    )
    disabled: bool = attr.field()
    privacy: Union["ComponentPrivacySetting", int] = attr.field(converter=enum_converter("ComponentPrivacySetting"))


@attr.define
class DictionaryComponentResponseOfint32AndDestinyItemRenderComponent(BaseModel):
    """
    _No description given by bungie._

    None
    Attributes:
        data: _No description given by bungie._
        disabled: If true, this component is disabled.
        privacy: _No description given by bungie._
    """

    data: dict[int, "DestinyItemRenderComponent"] = attr.field(
        metadata={"type": """dict[int, DestinyItemRenderComponent]"""}
    )
    disabled: bool = attr.field()
    privacy: Union["ComponentPrivacySetting", int] = attr.field(converter=enum_converter("ComponentPrivacySetting"))


@attr.define
class DictionaryComponentResponseOfint32AndDestinyItemStatsComponent(BaseModel):
    """
    _No description given by bungie._

    None
    Attributes:
        data: _No description given by bungie._
        disabled: If true, this component is disabled.
        privacy: _No description given by bungie._
    """

    data: dict[int, "DestinyItemStatsComponent"] = attr.field(
        metadata={"type": """dict[int, DestinyItemStatsComponent]"""}
    )
    disabled: bool = attr.field()
    privacy: Union["ComponentPrivacySetting", int] = attr.field(converter=enum_converter("ComponentPrivacySetting"))


@attr.define
class DictionaryComponentResponseOfint32AndDestinyItemSocketsComponent(BaseModel):
    """
    _No description given by bungie._

    None
    Attributes:
        data: _No description given by bungie._
        disabled: If true, this component is disabled.
        privacy: _No description given by bungie._
    """

    data: dict[int, "DestinyItemSocketsComponent"] = attr.field(
        metadata={"type": """dict[int, DestinyItemSocketsComponent]"""}
    )
    disabled: bool = attr.field()
    privacy: Union["ComponentPrivacySetting", int] = attr.field(converter=enum_converter("ComponentPrivacySetting"))


@attr.define
class DictionaryComponentResponseOfint32AndDestinyItemReusablePlugsComponent(BaseModel):
    """
    _No description given by bungie._

    None
    Attributes:
        data: _No description given by bungie._
        disabled: If true, this component is disabled.
        privacy: _No description given by bungie._
    """

    data: dict[int, "DestinyItemReusablePlugsComponent"] = attr.field(
        metadata={"type": """dict[int, DestinyItemReusablePlugsComponent]"""}
    )
    disabled: bool = attr.field()
    privacy: Union["ComponentPrivacySetting", int] = attr.field(converter=enum_converter("ComponentPrivacySetting"))


@attr.define
class DictionaryComponentResponseOfint32AndDestinyItemPlugObjectivesComponent(BaseModel):
    """
    _No description given by bungie._

    None
    Attributes:
        data: _No description given by bungie._
        disabled: If true, this component is disabled.
        privacy: _No description given by bungie._
    """

    data: dict[int, "DestinyItemPlugObjectivesComponent"] = attr.field(
        metadata={"type": """dict[int, DestinyItemPlugObjectivesComponent]"""}
    )
    disabled: bool = attr.field()
    privacy: Union["ComponentPrivacySetting", int] = attr.field(converter=enum_converter("ComponentPrivacySetting"))


@attr.define
class DictionaryComponentResponseOfint32AndDestinyItemTalentGridComponent(BaseModel):
    """
    _No description given by bungie._

    None
    Attributes:
        data: _No description given by bungie._
        disabled: If true, this component is disabled.
        privacy: _No description given by bungie._
    """

    data: dict[int, "DestinyItemTalentGridComponent"] = attr.field(
        metadata={"type": """dict[int, DestinyItemTalentGridComponent]"""}
    )
    disabled: bool = attr.field()
    privacy: Union["ComponentPrivacySetting", int] = attr.field(converter=enum_converter("ComponentPrivacySetting"))


@attr.define
class SingleComponentResponseOfDestinyVendorComponent(BaseModel):
    """
    _No description given by bungie._

    None
    Attributes:
        data: _No description given by bungie._
        disabled: If true, this component is disabled.
        privacy: _No description given by bungie._
    """

    data: "DestinyVendorComponent" = attr.field()
    disabled: bool = attr.field()
    privacy: Union["ComponentPrivacySetting", int] = attr.field(converter=enum_converter("ComponentPrivacySetting"))


@attr.define
class SingleComponentResponseOfDestinyVendorCategoriesComponent(BaseModel):
    """
    _No description given by bungie._

    None
    Attributes:
        data: _No description given by bungie._
        disabled: If true, this component is disabled.
        privacy: _No description given by bungie._
    """

    data: "DestinyVendorCategoriesComponent" = attr.field()
    disabled: bool = attr.field()
    privacy: Union["ComponentPrivacySetting", int] = attr.field(converter=enum_converter("ComponentPrivacySetting"))


@attr.define
class DictionaryComponentResponseOfint32AndDestinyVendorSaleItemComponent(BaseModel):
    """
    _No description given by bungie._

    None
    Attributes:
        data: _No description given by bungie._
        disabled: If true, this component is disabled.
        privacy: _No description given by bungie._
    """

    data: dict[int, "DestinyVendorSaleItemComponent"] = attr.field(
        metadata={"type": """dict[int, DestinyVendorSaleItemComponent]"""}
    )
    disabled: bool = attr.field()
    privacy: Union["ComponentPrivacySetting", int] = attr.field(converter=enum_converter("ComponentPrivacySetting"))


@attr.define
class DictionaryComponentResponseOfuint32AndDestinyPublicVendorComponent(BaseModel):
    """
    _No description given by bungie._

    None
    Attributes:
        data: _No description given by bungie._
        disabled: If true, this component is disabled.
        privacy: _No description given by bungie._
    """

    data: dict[int, "DestinyPublicVendorComponent"] = attr.field(
        metadata={"type": """dict[int, DestinyPublicVendorComponent]"""}
    )
    disabled: bool = attr.field()
    privacy: Union["ComponentPrivacySetting", int] = attr.field(converter=enum_converter("ComponentPrivacySetting"))


@attr.define
class DestinyVendorSaleItemSetComponentOfDestinyPublicVendorSaleItemComponent(BaseModel):
    """
    _No description given by bungie._

    None
    Attributes:
        sale_items: _No description given by bungie._
    """

    sale_items: dict[int, "DestinyPublicVendorSaleItemComponent"] = attr.field(
        metadata={"type": """dict[int, DestinyPublicVendorSaleItemComponent]"""}
    )


@attr.define
class DictionaryComponentResponseOfuint32AndPublicDestinyVendorSaleItemSetComponent(BaseModel):
    """
    _No description given by bungie._

    None
    Attributes:
        data: _No description given by bungie._
        disabled: If true, this component is disabled.
        privacy: _No description given by bungie._
    """

    data: dict[int, "PublicDestinyVendorSaleItemSetComponent"] = attr.field(
        metadata={"type": """dict[int, PublicDestinyVendorSaleItemSetComponent]"""}
    )
    disabled: bool = attr.field()
    privacy: Union["ComponentPrivacySetting", int] = attr.field(converter=enum_converter("ComponentPrivacySetting"))


@attr.define
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

    instances: "DictionaryComponentResponseOfuint32AndDestinyItemInstanceComponent" = attr.field()
    objectives: "DictionaryComponentResponseOfuint32AndDestinyItemObjectivesComponent" = attr.field()
    perks: "DictionaryComponentResponseOfuint32AndDestinyItemPerksComponent" = attr.field()
    plug_objectives: "DictionaryComponentResponseOfuint32AndDestinyItemPlugObjectivesComponent" = attr.field()
    plug_states: "DictionaryComponentResponseOfuint32AndDestinyItemPlugComponent" = attr.field()
    render_data: "DictionaryComponentResponseOfuint32AndDestinyItemRenderComponent" = attr.field()
    reusable_plugs: "DictionaryComponentResponseOfuint32AndDestinyItemReusablePlugsComponent" = attr.field()
    sockets: "DictionaryComponentResponseOfuint32AndDestinyItemSocketsComponent" = attr.field()
    stats: "DictionaryComponentResponseOfuint32AndDestinyItemStatsComponent" = attr.field()
    talent_grids: "DictionaryComponentResponseOfuint32AndDestinyItemTalentGridComponent" = attr.field()


@attr.define
class DictionaryComponentResponseOfuint32AndDestinyItemInstanceComponent(BaseModel):
    """
    _No description given by bungie._

    None
    Attributes:
        data: _No description given by bungie._
        disabled: If true, this component is disabled.
        privacy: _No description given by bungie._
    """

    data: dict[int, "DestinyItemInstanceComponent"] = attr.field(
        metadata={"type": """dict[int, DestinyItemInstanceComponent]"""}
    )
    disabled: bool = attr.field()
    privacy: Union["ComponentPrivacySetting", int] = attr.field(converter=enum_converter("ComponentPrivacySetting"))


@attr.define
class DictionaryComponentResponseOfuint32AndDestinyItemRenderComponent(BaseModel):
    """
    _No description given by bungie._

    None
    Attributes:
        data: _No description given by bungie._
        disabled: If true, this component is disabled.
        privacy: _No description given by bungie._
    """

    data: dict[int, "DestinyItemRenderComponent"] = attr.field(
        metadata={"type": """dict[int, DestinyItemRenderComponent]"""}
    )
    disabled: bool = attr.field()
    privacy: Union["ComponentPrivacySetting", int] = attr.field(converter=enum_converter("ComponentPrivacySetting"))


@attr.define
class DictionaryComponentResponseOfuint32AndDestinyItemStatsComponent(BaseModel):
    """
    _No description given by bungie._

    None
    Attributes:
        data: _No description given by bungie._
        disabled: If true, this component is disabled.
        privacy: _No description given by bungie._
    """

    data: dict[int, "DestinyItemStatsComponent"] = attr.field(
        metadata={"type": """dict[int, DestinyItemStatsComponent]"""}
    )
    disabled: bool = attr.field()
    privacy: Union["ComponentPrivacySetting", int] = attr.field(converter=enum_converter("ComponentPrivacySetting"))


@attr.define
class DictionaryComponentResponseOfuint32AndDestinyItemSocketsComponent(BaseModel):
    """
    _No description given by bungie._

    None
    Attributes:
        data: _No description given by bungie._
        disabled: If true, this component is disabled.
        privacy: _No description given by bungie._
    """

    data: dict[int, "DestinyItemSocketsComponent"] = attr.field(
        metadata={"type": """dict[int, DestinyItemSocketsComponent]"""}
    )
    disabled: bool = attr.field()
    privacy: Union["ComponentPrivacySetting", int] = attr.field(converter=enum_converter("ComponentPrivacySetting"))


@attr.define
class DictionaryComponentResponseOfuint32AndDestinyItemReusablePlugsComponent(BaseModel):
    """
    _No description given by bungie._

    None
    Attributes:
        data: _No description given by bungie._
        disabled: If true, this component is disabled.
        privacy: _No description given by bungie._
    """

    data: dict[int, "DestinyItemReusablePlugsComponent"] = attr.field(
        metadata={"type": """dict[int, DestinyItemReusablePlugsComponent]"""}
    )
    disabled: bool = attr.field()
    privacy: Union["ComponentPrivacySetting", int] = attr.field(converter=enum_converter("ComponentPrivacySetting"))


@attr.define
class DictionaryComponentResponseOfuint32AndDestinyItemPlugObjectivesComponent(BaseModel):
    """
    _No description given by bungie._

    None
    Attributes:
        data: _No description given by bungie._
        disabled: If true, this component is disabled.
        privacy: _No description given by bungie._
    """

    data: dict[int, "DestinyItemPlugObjectivesComponent"] = attr.field(
        metadata={"type": """dict[int, DestinyItemPlugObjectivesComponent]"""}
    )
    disabled: bool = attr.field()
    privacy: Union["ComponentPrivacySetting", int] = attr.field(converter=enum_converter("ComponentPrivacySetting"))


@attr.define
class DictionaryComponentResponseOfuint32AndDestinyItemTalentGridComponent(BaseModel):
    """
    _No description given by bungie._

    None
    Attributes:
        data: _No description given by bungie._
        disabled: If true, this component is disabled.
        privacy: _No description given by bungie._
    """

    data: dict[int, "DestinyItemTalentGridComponent"] = attr.field(
        metadata={"type": """dict[int, DestinyItemTalentGridComponent]"""}
    )
    disabled: bool = attr.field()
    privacy: Union["ComponentPrivacySetting", int] = attr.field(converter=enum_converter("ComponentPrivacySetting"))


@attr.define
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

    has_more: bool = attr.field()
    query: "PagedQuery" = attr.field()
    replacement_continuation_token: str = attr.field()
    results: list["DestinyEntitySearchResultItem"] = attr.field(
        metadata={"type": """list[DestinyEntitySearchResultItem]"""}
    )
    total_results: int = attr.field()
    use_total_results: bool = attr.field()


@attr.define
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

    has_more: bool = attr.field()
    query: "PagedQuery" = attr.field()
    replacement_continuation_token: str = attr.field()
    results: list["TrendingEntry"] = attr.field(metadata={"type": """list[TrendingEntry]"""})
    total_results: int = attr.field()
    use_total_results: bool = attr.field()


@attr.define
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

    has_more: bool = attr.field()
    query: "PagedQuery" = attr.field()
    replacement_continuation_token: str = attr.field()
    results: list["FireteamSummary"] = attr.field(metadata={"type": """list[FireteamSummary]"""})
    total_results: int = attr.field()
    use_total_results: bool = attr.field()


@attr.define
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

    has_more: bool = attr.field()
    query: "PagedQuery" = attr.field()
    replacement_continuation_token: str = attr.field()
    results: list["FireteamResponse"] = attr.field(metadata={"type": """list[FireteamResponse]"""})
    total_results: int = attr.field()
    use_total_results: bool = attr.field()


@attr.define
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

    alert_html: str = attr.field()
    alert_key: str = attr.field()
    alert_level: Union["GlobalAlertLevel", int] = attr.field(converter=enum_converter("GlobalAlertLevel"))
    alert_link: str = attr.field()
    alert_timestamp: datetime = attr.field()
    alert_type: Union["GlobalAlertType", int] = attr.field(converter=enum_converter("GlobalAlertType"))
    stream_info: "StreamInfo" = attr.field()


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


@attr.define
class StreamInfo(BaseModel):
    """
    _No description given by bungie._

    None
    Attributes:
        channel_name: _No description given by bungie._
    """

    channel_name: str = attr.field()
