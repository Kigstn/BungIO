import datetime
from typing import TYPE_CHECKING, Any

import attr

from bungio.models.base import BaseEnum, BaseModel

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
        DestinyCurrenciesComponent,
        DestinyEntitySearchResultItem,
        DestinyInventoryComponent,
        DestinyItemComponent,
        DestinyItemInstanceComponent,
        DestinyItemObjectivesComponent,
        DestinyItemPerksComponent,
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
        DestinyStringVariablesComponent,
        DestinyVendorCategoriesComponent,
        DestinyVendorComponent,
        DestinyVendorGroupComponent,
        DestinyVendorReceiptsComponent,
        FireteamResponse,
        FireteamSummary,
        GroupBan,
        GroupMember,
        GroupMemberApplication,
        GroupMembership,
        GroupPotentialMembership,
        GroupV2Card,
        PagedQuery,
        PostResponse,
        TrendingEntry,
    )


class BungieMembershipType(BaseEnum):
    """
    The types of membership the Accounts system supports. This is the external facing enum used in place of the internal-only Bungie.SharedDefinitions.MembershipType.
    """

    NONE = 0
    """_No description given by bungie_ """
    TIGER_XBOX = 1
    """_No description given by bungie_ """
    TIGER_PSN = 2
    """_No description given by bungie_ """
    TIGER_STEAM = 3
    """_No description given by bungie_ """
    TIGER_BLIZZARD = 4
    """_No description given by bungie_ """
    TIGER_STADIA = 5
    """_No description given by bungie_ """
    TIGER_DEMON = 10
    """_No description given by bungie_ """
    BUNGIE_NEXT = 254
    """_No description given by bungie_ """
    ALL = -1
    """"All" is only valid for searching capabilities: you need to pass the actual matching BungieMembershipType for any query where you pass a known membershipId. """


class BungieCredentialType(BaseEnum):
    """
    The types of credentials the Accounts system supports. This is the external facing enum used in place of the internal-only Bungie.SharedDefinitions.CredentialType.
    """

    NONE = 0
    """_No description given by bungie_ """
    XUID = 1
    """_No description given by bungie_ """
    PSNID = 2
    """_No description given by bungie_ """
    WLID = 3
    """_No description given by bungie_ """
    FAKE = 4
    """_No description given by bungie_ """
    FACEBOOK = 5
    """_No description given by bungie_ """
    GOOGLE = 8
    """_No description given by bungie_ """
    WINDOWS = 9
    """_No description given by bungie_ """
    DEMON_ID = 10
    """_No description given by bungie_ """
    STEAM_ID = 12
    """_No description given by bungie_ """
    BATTLE_NET_ID = 14
    """_No description given by bungie_ """
    STADIA_ID = 16
    """_No description given by bungie_ """
    TWITCH_ID = 18
    """_No description given by bungie_ """


@attr.define
class SearchResultOfContentItemPublicContract(BaseModel):
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

    results: list["ContentItemPublicContract"] = attr.field()
    total_results: int = attr.field()
    has_more: bool = attr.field()
    query: "PagedQuery" = attr.field()
    replacement_continuation_token: str = attr.field()
    use_total_results: bool = attr.field()


@attr.define
class SearchResultOfPostResponse(BaseModel):
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

    results: list["PostResponse"] = attr.field()
    total_results: int = attr.field()
    has_more: bool = attr.field()
    query: "PagedQuery" = attr.field()
    replacement_continuation_token: str = attr.field()
    use_total_results: bool = attr.field()


@attr.define
class SearchResultOfGroupV2Card(BaseModel):
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
class SearchResultOfGroupMember(BaseModel):
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

    results: list["GroupMember"] = attr.field()
    total_results: int = attr.field()
    has_more: bool = attr.field()
    query: "PagedQuery" = attr.field()
    replacement_continuation_token: str = attr.field()
    use_total_results: bool = attr.field()


@attr.define
class SearchResultOfGroupBan(BaseModel):
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

    results: list["GroupBan"] = attr.field()
    total_results: int = attr.field()
    has_more: bool = attr.field()
    query: "PagedQuery" = attr.field()
    replacement_continuation_token: str = attr.field()
    use_total_results: bool = attr.field()


@attr.define
class SearchResultOfGroupMemberApplication(BaseModel):
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

    results: list["GroupMemberApplication"] = attr.field()
    total_results: int = attr.field()
    has_more: bool = attr.field()
    query: "PagedQuery" = attr.field()
    replacement_continuation_token: str = attr.field()
    use_total_results: bool = attr.field()


@attr.define
class SearchResultOfGroupMembership(BaseModel):
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
class SearchResultOfGroupPotentialMembership(BaseModel):
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
class SingleComponentResponseOfDestinyVendorReceiptsComponent(BaseModel):
    """
    _No description given by bungie_

    Attributes:
        data: _No description given by bungie_
        privacy: _No description given by bungie_
        disabled: If true, this component is disabled.
    """

    data: "DestinyVendorReceiptsComponent" = attr.field()
    privacy: "ComponentPrivacySetting" = attr.field()
    disabled: bool = attr.field()


@attr.define
class SingleComponentResponseOfDestinyInventoryComponent(BaseModel):
    """
    _No description given by bungie_

    Attributes:
        data: _No description given by bungie_
        privacy: _No description given by bungie_
        disabled: If true, this component is disabled.
    """

    data: "DestinyInventoryComponent" = attr.field()
    privacy: "ComponentPrivacySetting" = attr.field()
    disabled: bool = attr.field()


@attr.define
class SingleComponentResponseOfDestinyProfileComponent(BaseModel):
    """
    _No description given by bungie_

    Attributes:
        data: _No description given by bungie_
        privacy: _No description given by bungie_
        disabled: If true, this component is disabled.
    """

    data: "DestinyProfileComponent" = attr.field()
    privacy: "ComponentPrivacySetting" = attr.field()
    disabled: bool = attr.field()


@attr.define
class SingleComponentResponseOfDestinyPlatformSilverComponent(BaseModel):
    """
    _No description given by bungie_

    Attributes:
        data: _No description given by bungie_
        privacy: _No description given by bungie_
        disabled: If true, this component is disabled.
    """

    data: "DestinyPlatformSilverComponent" = attr.field()
    privacy: "ComponentPrivacySetting" = attr.field()
    disabled: bool = attr.field()


@attr.define
class SingleComponentResponseOfDestinyKiosksComponent(BaseModel):
    """
    _No description given by bungie_

    Attributes:
        data: _No description given by bungie_
        privacy: _No description given by bungie_
        disabled: If true, this component is disabled.
    """

    data: "DestinyKiosksComponent" = attr.field()
    privacy: "ComponentPrivacySetting" = attr.field()
    disabled: bool = attr.field()


@attr.define
class SingleComponentResponseOfDestinyPlugSetsComponent(BaseModel):
    """
    _No description given by bungie_

    Attributes:
        data: _No description given by bungie_
        privacy: _No description given by bungie_
        disabled: If true, this component is disabled.
    """

    data: "DestinyPlugSetsComponent" = attr.field()
    privacy: "ComponentPrivacySetting" = attr.field()
    disabled: bool = attr.field()


@attr.define
class SingleComponentResponseOfDestinyProfileProgressionComponent(BaseModel):
    """
    _No description given by bungie_

    Attributes:
        data: _No description given by bungie_
        privacy: _No description given by bungie_
        disabled: If true, this component is disabled.
    """

    data: "DestinyProfileProgressionComponent" = attr.field()
    privacy: "ComponentPrivacySetting" = attr.field()
    disabled: bool = attr.field()


@attr.define
class SingleComponentResponseOfDestinyPresentationNodesComponent(BaseModel):
    """
    _No description given by bungie_

    Attributes:
        data: _No description given by bungie_
        privacy: _No description given by bungie_
        disabled: If true, this component is disabled.
    """

    data: "DestinyPresentationNodesComponent" = attr.field()
    privacy: "ComponentPrivacySetting" = attr.field()
    disabled: bool = attr.field()


@attr.define
class SingleComponentResponseOfDestinyProfileRecordsComponent(BaseModel):
    """
    _No description given by bungie_

    Attributes:
        data: _No description given by bungie_
        privacy: _No description given by bungie_
        disabled: If true, this component is disabled.
    """

    data: "DestinyProfileRecordsComponent" = attr.field()
    privacy: "ComponentPrivacySetting" = attr.field()
    disabled: bool = attr.field()


@attr.define
class SingleComponentResponseOfDestinyProfileCollectiblesComponent(BaseModel):
    """
    _No description given by bungie_

    Attributes:
        data: _No description given by bungie_
        privacy: _No description given by bungie_
        disabled: If true, this component is disabled.
    """

    data: "DestinyProfileCollectiblesComponent" = attr.field()
    privacy: "ComponentPrivacySetting" = attr.field()
    disabled: bool = attr.field()


@attr.define
class SingleComponentResponseOfDestinyProfileTransitoryComponent(BaseModel):
    """
    _No description given by bungie_

    Attributes:
        data: _No description given by bungie_
        privacy: _No description given by bungie_
        disabled: If true, this component is disabled.
    """

    data: "DestinyProfileTransitoryComponent" = attr.field()
    privacy: "ComponentPrivacySetting" = attr.field()
    disabled: bool = attr.field()


@attr.define
class SingleComponentResponseOfDestinyMetricsComponent(BaseModel):
    """
    _No description given by bungie_

    Attributes:
        data: _No description given by bungie_
        privacy: _No description given by bungie_
        disabled: If true, this component is disabled.
    """

    data: "DestinyMetricsComponent" = attr.field()
    privacy: "ComponentPrivacySetting" = attr.field()
    disabled: bool = attr.field()


@attr.define
class SingleComponentResponseOfDestinyStringVariablesComponent(BaseModel):
    """
    _No description given by bungie_

    Attributes:
        data: _No description given by bungie_
        privacy: _No description given by bungie_
        disabled: If true, this component is disabled.
    """

    data: "DestinyStringVariablesComponent" = attr.field()
    privacy: "ComponentPrivacySetting" = attr.field()
    disabled: bool = attr.field()


@attr.define
class DictionaryComponentResponseOfint64AndDestinyCharacterComponent(BaseModel):
    """
    _No description given by bungie_

    Attributes:
        data: _No description given by bungie_
        privacy: _No description given by bungie_
        disabled: If true, this component is disabled.
    """

    data: Any = attr.field()
    privacy: "ComponentPrivacySetting" = attr.field()
    disabled: bool = attr.field()


@attr.define
class DictionaryComponentResponseOfint64AndDestinyInventoryComponent(BaseModel):
    """
    _No description given by bungie_

    Attributes:
        data: _No description given by bungie_
        privacy: _No description given by bungie_
        disabled: If true, this component is disabled.
    """

    data: Any = attr.field()
    privacy: "ComponentPrivacySetting" = attr.field()
    disabled: bool = attr.field()


@attr.define
class DictionaryComponentResponseOfint64AndDestinyCharacterProgressionComponent(BaseModel):
    """
    _No description given by bungie_

    Attributes:
        data: _No description given by bungie_
        privacy: _No description given by bungie_
        disabled: If true, this component is disabled.
    """

    data: Any = attr.field()
    privacy: "ComponentPrivacySetting" = attr.field()
    disabled: bool = attr.field()


@attr.define
class DictionaryComponentResponseOfint64AndDestinyCharacterRenderComponent(BaseModel):
    """
    _No description given by bungie_

    Attributes:
        data: _No description given by bungie_
        privacy: _No description given by bungie_
        disabled: If true, this component is disabled.
    """

    data: Any = attr.field()
    privacy: "ComponentPrivacySetting" = attr.field()
    disabled: bool = attr.field()


@attr.define
class DictionaryComponentResponseOfint64AndDestinyCharacterActivitiesComponent(BaseModel):
    """
    _No description given by bungie_

    Attributes:
        data: _No description given by bungie_
        privacy: _No description given by bungie_
        disabled: If true, this component is disabled.
    """

    data: Any = attr.field()
    privacy: "ComponentPrivacySetting" = attr.field()
    disabled: bool = attr.field()


@attr.define
class DictionaryComponentResponseOfint64AndDestinyKiosksComponent(BaseModel):
    """
    _No description given by bungie_

    Attributes:
        data: _No description given by bungie_
        privacy: _No description given by bungie_
        disabled: If true, this component is disabled.
    """

    data: Any = attr.field()
    privacy: "ComponentPrivacySetting" = attr.field()
    disabled: bool = attr.field()


@attr.define
class DictionaryComponentResponseOfint64AndDestinyPlugSetsComponent(BaseModel):
    """
    _No description given by bungie_

    Attributes:
        data: _No description given by bungie_
        privacy: _No description given by bungie_
        disabled: If true, this component is disabled.
    """

    data: Any = attr.field()
    privacy: "ComponentPrivacySetting" = attr.field()
    disabled: bool = attr.field()


@attr.define
class DestinyBaseItemComponentSetOfuint32(BaseModel):
    """
    _No description given by bungie_

    Attributes:
        objectives: _No description given by bungie_
        perks: _No description given by bungie_
    """

    objectives: "DictionaryComponentResponseOfuint32AndDestinyItemObjectivesComponent" = attr.field()
    perks: "DictionaryComponentResponseOfuint32AndDestinyItemPerksComponent" = attr.field()


@attr.define
class DictionaryComponentResponseOfuint32AndDestinyItemObjectivesComponent(BaseModel):
    """
    _No description given by bungie_

    Attributes:
        data: _No description given by bungie_
        privacy: _No description given by bungie_
        disabled: If true, this component is disabled.
    """

    data: Any = attr.field()
    privacy: "ComponentPrivacySetting" = attr.field()
    disabled: bool = attr.field()


@attr.define
class DictionaryComponentResponseOfuint32AndDestinyItemPerksComponent(BaseModel):
    """
    _No description given by bungie_

    Attributes:
        data: _No description given by bungie_
        privacy: _No description given by bungie_
        disabled: If true, this component is disabled.
    """

    data: Any = attr.field()
    privacy: "ComponentPrivacySetting" = attr.field()
    disabled: bool = attr.field()


@attr.define
class DictionaryComponentResponseOfint64AndDestinyPresentationNodesComponent(BaseModel):
    """
    _No description given by bungie_

    Attributes:
        data: _No description given by bungie_
        privacy: _No description given by bungie_
        disabled: If true, this component is disabled.
    """

    data: Any = attr.field()
    privacy: "ComponentPrivacySetting" = attr.field()
    disabled: bool = attr.field()


@attr.define
class DictionaryComponentResponseOfint64AndDestinyCharacterRecordsComponent(BaseModel):
    """
    _No description given by bungie_

    Attributes:
        data: _No description given by bungie_
        privacy: _No description given by bungie_
        disabled: If true, this component is disabled.
    """

    data: Any = attr.field()
    privacy: "ComponentPrivacySetting" = attr.field()
    disabled: bool = attr.field()


@attr.define
class DictionaryComponentResponseOfint64AndDestinyCollectiblesComponent(BaseModel):
    """
    _No description given by bungie_

    Attributes:
        data: _No description given by bungie_
        privacy: _No description given by bungie_
        disabled: If true, this component is disabled.
    """

    data: Any = attr.field()
    privacy: "ComponentPrivacySetting" = attr.field()
    disabled: bool = attr.field()


@attr.define
class DictionaryComponentResponseOfint64AndDestinyStringVariablesComponent(BaseModel):
    """
    _No description given by bungie_

    Attributes:
        data: _No description given by bungie_
        privacy: _No description given by bungie_
        disabled: If true, this component is disabled.
    """

    data: Any = attr.field()
    privacy: "ComponentPrivacySetting" = attr.field()
    disabled: bool = attr.field()


@attr.define
class DictionaryComponentResponseOfint64AndDestinyCraftablesComponent(BaseModel):
    """
    _No description given by bungie_

    Attributes:
        data: _No description given by bungie_
        privacy: _No description given by bungie_
        disabled: If true, this component is disabled.
    """

    data: Any = attr.field()
    privacy: "ComponentPrivacySetting" = attr.field()
    disabled: bool = attr.field()


@attr.define
class DestinyBaseItemComponentSetOfint64(BaseModel):
    """
    _No description given by bungie_

    Attributes:
        objectives: _No description given by bungie_
        perks: _No description given by bungie_
    """

    objectives: "DictionaryComponentResponseOfint64AndDestinyItemObjectivesComponent" = attr.field()
    perks: "DictionaryComponentResponseOfint64AndDestinyItemPerksComponent" = attr.field()


@attr.define
class DictionaryComponentResponseOfint64AndDestinyItemObjectivesComponent(BaseModel):
    """
    _No description given by bungie_

    Attributes:
        data: _No description given by bungie_
        privacy: _No description given by bungie_
        disabled: If true, this component is disabled.
    """

    data: Any = attr.field()
    privacy: "ComponentPrivacySetting" = attr.field()
    disabled: bool = attr.field()


@attr.define
class DictionaryComponentResponseOfint64AndDestinyItemPerksComponent(BaseModel):
    """
    _No description given by bungie_

    Attributes:
        data: _No description given by bungie_
        privacy: _No description given by bungie_
        disabled: If true, this component is disabled.
    """

    data: Any = attr.field()
    privacy: "ComponentPrivacySetting" = attr.field()
    disabled: bool = attr.field()


@attr.define
class DestinyItemComponentSetOfint64(BaseModel):
    """
    _No description given by bungie_

    Attributes:
        instances: _No description given by bungie_
        render_data: _No description given by bungie_
        stats: _No description given by bungie_
        sockets: _No description given by bungie_
        reusable_plugs: _No description given by bungie_
        plug_objectives: _No description given by bungie_
        talent_grids: _No description given by bungie_
        plug_states: _No description given by bungie_
        objectives: _No description given by bungie_
        perks: _No description given by bungie_
    """

    instances: "DictionaryComponentResponseOfint64AndDestinyItemInstanceComponent" = attr.field()
    render_data: "DictionaryComponentResponseOfint64AndDestinyItemRenderComponent" = attr.field()
    stats: "DictionaryComponentResponseOfint64AndDestinyItemStatsComponent" = attr.field()
    sockets: "DictionaryComponentResponseOfint64AndDestinyItemSocketsComponent" = attr.field()
    reusable_plugs: "DictionaryComponentResponseOfint64AndDestinyItemReusablePlugsComponent" = attr.field()
    plug_objectives: "DictionaryComponentResponseOfint64AndDestinyItemPlugObjectivesComponent" = attr.field()
    talent_grids: "DictionaryComponentResponseOfint64AndDestinyItemTalentGridComponent" = attr.field()
    plug_states: "DictionaryComponentResponseOfuint32AndDestinyItemPlugComponent" = attr.field()
    objectives: "DictionaryComponentResponseOfint64AndDestinyItemObjectivesComponent" = attr.field()
    perks: "DictionaryComponentResponseOfint64AndDestinyItemPerksComponent" = attr.field()


@attr.define
class DictionaryComponentResponseOfint64AndDestinyItemInstanceComponent(BaseModel):
    """
    _No description given by bungie_

    Attributes:
        data: _No description given by bungie_
        privacy: _No description given by bungie_
        disabled: If true, this component is disabled.
    """

    data: Any = attr.field()
    privacy: "ComponentPrivacySetting" = attr.field()
    disabled: bool = attr.field()


@attr.define
class DictionaryComponentResponseOfint64AndDestinyItemRenderComponent(BaseModel):
    """
    _No description given by bungie_

    Attributes:
        data: _No description given by bungie_
        privacy: _No description given by bungie_
        disabled: If true, this component is disabled.
    """

    data: Any = attr.field()
    privacy: "ComponentPrivacySetting" = attr.field()
    disabled: bool = attr.field()


@attr.define
class DictionaryComponentResponseOfint64AndDestinyItemStatsComponent(BaseModel):
    """
    _No description given by bungie_

    Attributes:
        data: _No description given by bungie_
        privacy: _No description given by bungie_
        disabled: If true, this component is disabled.
    """

    data: Any = attr.field()
    privacy: "ComponentPrivacySetting" = attr.field()
    disabled: bool = attr.field()


@attr.define
class DictionaryComponentResponseOfint64AndDestinyItemSocketsComponent(BaseModel):
    """
    _No description given by bungie_

    Attributes:
        data: _No description given by bungie_
        privacy: _No description given by bungie_
        disabled: If true, this component is disabled.
    """

    data: Any = attr.field()
    privacy: "ComponentPrivacySetting" = attr.field()
    disabled: bool = attr.field()


@attr.define
class DictionaryComponentResponseOfint64AndDestinyItemReusablePlugsComponent(BaseModel):
    """
    _No description given by bungie_

    Attributes:
        data: _No description given by bungie_
        privacy: _No description given by bungie_
        disabled: If true, this component is disabled.
    """

    data: Any = attr.field()
    privacy: "ComponentPrivacySetting" = attr.field()
    disabled: bool = attr.field()


@attr.define
class DictionaryComponentResponseOfint64AndDestinyItemPlugObjectivesComponent(BaseModel):
    """
    _No description given by bungie_

    Attributes:
        data: _No description given by bungie_
        privacy: _No description given by bungie_
        disabled: If true, this component is disabled.
    """

    data: Any = attr.field()
    privacy: "ComponentPrivacySetting" = attr.field()
    disabled: bool = attr.field()


@attr.define
class DictionaryComponentResponseOfint64AndDestinyItemTalentGridComponent(BaseModel):
    """
    _No description given by bungie_

    Attributes:
        data: _No description given by bungie_
        privacy: _No description given by bungie_
        disabled: If true, this component is disabled.
    """

    data: Any = attr.field()
    privacy: "ComponentPrivacySetting" = attr.field()
    disabled: bool = attr.field()


@attr.define
class DictionaryComponentResponseOfuint32AndDestinyItemPlugComponent(BaseModel):
    """
    _No description given by bungie_

    Attributes:
        data: _No description given by bungie_
        privacy: _No description given by bungie_
        disabled: If true, this component is disabled.
    """

    data: Any = attr.field()
    privacy: "ComponentPrivacySetting" = attr.field()
    disabled: bool = attr.field()


@attr.define
class DictionaryComponentResponseOfint64AndDestinyCurrenciesComponent(BaseModel):
    """
    _No description given by bungie_

    Attributes:
        data: _No description given by bungie_
        privacy: _No description given by bungie_
        disabled: If true, this component is disabled.
    """

    data: Any = attr.field()
    privacy: "ComponentPrivacySetting" = attr.field()
    disabled: bool = attr.field()


@attr.define
class SingleComponentResponseOfDestinyCharacterComponent(BaseModel):
    """
    _No description given by bungie_

    Attributes:
        data: _No description given by bungie_
        privacy: _No description given by bungie_
        disabled: If true, this component is disabled.
    """

    data: "DestinyCharacterComponent" = attr.field()
    privacy: "ComponentPrivacySetting" = attr.field()
    disabled: bool = attr.field()


@attr.define
class SingleComponentResponseOfDestinyCharacterProgressionComponent(BaseModel):
    """
    _No description given by bungie_

    Attributes:
        data: _No description given by bungie_
        privacy: _No description given by bungie_
        disabled: If true, this component is disabled.
    """

    data: "DestinyCharacterProgressionComponent" = attr.field()
    privacy: "ComponentPrivacySetting" = attr.field()
    disabled: bool = attr.field()


@attr.define
class SingleComponentResponseOfDestinyCharacterRenderComponent(BaseModel):
    """
    _No description given by bungie_

    Attributes:
        data: _No description given by bungie_
        privacy: _No description given by bungie_
        disabled: If true, this component is disabled.
    """

    data: "DestinyCharacterRenderComponent" = attr.field()
    privacy: "ComponentPrivacySetting" = attr.field()
    disabled: bool = attr.field()


@attr.define
class SingleComponentResponseOfDestinyCharacterActivitiesComponent(BaseModel):
    """
    _No description given by bungie_

    Attributes:
        data: _No description given by bungie_
        privacy: _No description given by bungie_
        disabled: If true, this component is disabled.
    """

    data: "DestinyCharacterActivitiesComponent" = attr.field()
    privacy: "ComponentPrivacySetting" = attr.field()
    disabled: bool = attr.field()


@attr.define
class SingleComponentResponseOfDestinyCharacterRecordsComponent(BaseModel):
    """
    _No description given by bungie_

    Attributes:
        data: _No description given by bungie_
        privacy: _No description given by bungie_
        disabled: If true, this component is disabled.
    """

    data: "DestinyCharacterRecordsComponent" = attr.field()
    privacy: "ComponentPrivacySetting" = attr.field()
    disabled: bool = attr.field()


@attr.define
class SingleComponentResponseOfDestinyCollectiblesComponent(BaseModel):
    """
    _No description given by bungie_

    Attributes:
        data: _No description given by bungie_
        privacy: _No description given by bungie_
        disabled: If true, this component is disabled.
    """

    data: "DestinyCollectiblesComponent" = attr.field()
    privacy: "ComponentPrivacySetting" = attr.field()
    disabled: bool = attr.field()


@attr.define
class SingleComponentResponseOfDestinyCurrenciesComponent(BaseModel):
    """
    _No description given by bungie_

    Attributes:
        data: _No description given by bungie_
        privacy: _No description given by bungie_
        disabled: If true, this component is disabled.
    """

    data: "DestinyCurrenciesComponent" = attr.field()
    privacy: "ComponentPrivacySetting" = attr.field()
    disabled: bool = attr.field()


@attr.define
class SingleComponentResponseOfDestinyItemComponent(BaseModel):
    """
    _No description given by bungie_

    Attributes:
        data: _No description given by bungie_
        privacy: _No description given by bungie_
        disabled: If true, this component is disabled.
    """

    data: "DestinyItemComponent" = attr.field()
    privacy: "ComponentPrivacySetting" = attr.field()
    disabled: bool = attr.field()


@attr.define
class SingleComponentResponseOfDestinyItemInstanceComponent(BaseModel):
    """
    _No description given by bungie_

    Attributes:
        data: _No description given by bungie_
        privacy: _No description given by bungie_
        disabled: If true, this component is disabled.
    """

    data: "DestinyItemInstanceComponent" = attr.field()
    privacy: "ComponentPrivacySetting" = attr.field()
    disabled: bool = attr.field()


@attr.define
class SingleComponentResponseOfDestinyItemObjectivesComponent(BaseModel):
    """
    _No description given by bungie_

    Attributes:
        data: _No description given by bungie_
        privacy: _No description given by bungie_
        disabled: If true, this component is disabled.
    """

    data: "DestinyItemObjectivesComponent" = attr.field()
    privacy: "ComponentPrivacySetting" = attr.field()
    disabled: bool = attr.field()


@attr.define
class SingleComponentResponseOfDestinyItemPerksComponent(BaseModel):
    """
    _No description given by bungie_

    Attributes:
        data: _No description given by bungie_
        privacy: _No description given by bungie_
        disabled: If true, this component is disabled.
    """

    data: "DestinyItemPerksComponent" = attr.field()
    privacy: "ComponentPrivacySetting" = attr.field()
    disabled: bool = attr.field()


@attr.define
class SingleComponentResponseOfDestinyItemRenderComponent(BaseModel):
    """
    _No description given by bungie_

    Attributes:
        data: _No description given by bungie_
        privacy: _No description given by bungie_
        disabled: If true, this component is disabled.
    """

    data: "DestinyItemRenderComponent" = attr.field()
    privacy: "ComponentPrivacySetting" = attr.field()
    disabled: bool = attr.field()


@attr.define
class SingleComponentResponseOfDestinyItemStatsComponent(BaseModel):
    """
    _No description given by bungie_

    Attributes:
        data: _No description given by bungie_
        privacy: _No description given by bungie_
        disabled: If true, this component is disabled.
    """

    data: "DestinyItemStatsComponent" = attr.field()
    privacy: "ComponentPrivacySetting" = attr.field()
    disabled: bool = attr.field()


@attr.define
class SingleComponentResponseOfDestinyItemTalentGridComponent(BaseModel):
    """
    _No description given by bungie_

    Attributes:
        data: _No description given by bungie_
        privacy: _No description given by bungie_
        disabled: If true, this component is disabled.
    """

    data: "DestinyItemTalentGridComponent" = attr.field()
    privacy: "ComponentPrivacySetting" = attr.field()
    disabled: bool = attr.field()


@attr.define
class SingleComponentResponseOfDestinyItemSocketsComponent(BaseModel):
    """
    _No description given by bungie_

    Attributes:
        data: _No description given by bungie_
        privacy: _No description given by bungie_
        disabled: If true, this component is disabled.
    """

    data: "DestinyItemSocketsComponent" = attr.field()
    privacy: "ComponentPrivacySetting" = attr.field()
    disabled: bool = attr.field()


@attr.define
class SingleComponentResponseOfDestinyItemReusablePlugsComponent(BaseModel):
    """
    _No description given by bungie_

    Attributes:
        data: _No description given by bungie_
        privacy: _No description given by bungie_
        disabled: If true, this component is disabled.
    """

    data: "DestinyItemReusablePlugsComponent" = attr.field()
    privacy: "ComponentPrivacySetting" = attr.field()
    disabled: bool = attr.field()


@attr.define
class SingleComponentResponseOfDestinyItemPlugObjectivesComponent(BaseModel):
    """
    _No description given by bungie_

    Attributes:
        data: _No description given by bungie_
        privacy: _No description given by bungie_
        disabled: If true, this component is disabled.
    """

    data: "DestinyItemPlugObjectivesComponent" = attr.field()
    privacy: "ComponentPrivacySetting" = attr.field()
    disabled: bool = attr.field()


@attr.define
class SingleComponentResponseOfDestinyVendorGroupComponent(BaseModel):
    """
    _No description given by bungie_

    Attributes:
        data: _No description given by bungie_
        privacy: _No description given by bungie_
        disabled: If true, this component is disabled.
    """

    data: "DestinyVendorGroupComponent" = attr.field()
    privacy: "ComponentPrivacySetting" = attr.field()
    disabled: bool = attr.field()


@attr.define
class DictionaryComponentResponseOfuint32AndDestinyVendorComponent(BaseModel):
    """
    _No description given by bungie_

    Attributes:
        data: _No description given by bungie_
        privacy: _No description given by bungie_
        disabled: If true, this component is disabled.
    """

    data: Any = attr.field()
    privacy: "ComponentPrivacySetting" = attr.field()
    disabled: bool = attr.field()


@attr.define
class DictionaryComponentResponseOfuint32AndDestinyVendorCategoriesComponent(BaseModel):
    """
    _No description given by bungie_

    Attributes:
        data: _No description given by bungie_
        privacy: _No description given by bungie_
        disabled: If true, this component is disabled.
    """

    data: Any = attr.field()
    privacy: "ComponentPrivacySetting" = attr.field()
    disabled: bool = attr.field()


@attr.define
class DestinyVendorSaleItemSetComponentOfDestinyVendorSaleItemComponent(BaseModel):
    """
    _No description given by bungie_

    Attributes:
        sale_items: _No description given by bungie_
    """

    sale_items: Any = attr.field()


@attr.define
class DictionaryComponentResponseOfuint32AndPersonalDestinyVendorSaleItemSetComponent(BaseModel):
    """
    _No description given by bungie_

    Attributes:
        data: _No description given by bungie_
        privacy: _No description given by bungie_
        disabled: If true, this component is disabled.
    """

    data: Any = attr.field()
    privacy: "ComponentPrivacySetting" = attr.field()
    disabled: bool = attr.field()


@attr.define
class DestinyBaseItemComponentSetOfint32(BaseModel):
    """
    _No description given by bungie_

    Attributes:
        objectives: _No description given by bungie_
        perks: _No description given by bungie_
    """

    objectives: "DictionaryComponentResponseOfint32AndDestinyItemObjectivesComponent" = attr.field()
    perks: "DictionaryComponentResponseOfint32AndDestinyItemPerksComponent" = attr.field()


@attr.define
class DictionaryComponentResponseOfint32AndDestinyItemObjectivesComponent(BaseModel):
    """
    _No description given by bungie_

    Attributes:
        data: _No description given by bungie_
        privacy: _No description given by bungie_
        disabled: If true, this component is disabled.
    """

    data: Any = attr.field()
    privacy: "ComponentPrivacySetting" = attr.field()
    disabled: bool = attr.field()


@attr.define
class DictionaryComponentResponseOfint32AndDestinyItemPerksComponent(BaseModel):
    """
    _No description given by bungie_

    Attributes:
        data: _No description given by bungie_
        privacy: _No description given by bungie_
        disabled: If true, this component is disabled.
    """

    data: Any = attr.field()
    privacy: "ComponentPrivacySetting" = attr.field()
    disabled: bool = attr.field()


@attr.define
class DestinyItemComponentSetOfint32(BaseModel):
    """
    _No description given by bungie_

    Attributes:
        instances: _No description given by bungie_
        render_data: _No description given by bungie_
        stats: _No description given by bungie_
        sockets: _No description given by bungie_
        reusable_plugs: _No description given by bungie_
        plug_objectives: _No description given by bungie_
        talent_grids: _No description given by bungie_
        plug_states: _No description given by bungie_
        objectives: _No description given by bungie_
        perks: _No description given by bungie_
    """

    instances: "DictionaryComponentResponseOfint32AndDestinyItemInstanceComponent" = attr.field()
    render_data: "DictionaryComponentResponseOfint32AndDestinyItemRenderComponent" = attr.field()
    stats: "DictionaryComponentResponseOfint32AndDestinyItemStatsComponent" = attr.field()
    sockets: "DictionaryComponentResponseOfint32AndDestinyItemSocketsComponent" = attr.field()
    reusable_plugs: "DictionaryComponentResponseOfint32AndDestinyItemReusablePlugsComponent" = attr.field()
    plug_objectives: "DictionaryComponentResponseOfint32AndDestinyItemPlugObjectivesComponent" = attr.field()
    talent_grids: "DictionaryComponentResponseOfint32AndDestinyItemTalentGridComponent" = attr.field()
    plug_states: "DictionaryComponentResponseOfuint32AndDestinyItemPlugComponent" = attr.field()
    objectives: "DictionaryComponentResponseOfint32AndDestinyItemObjectivesComponent" = attr.field()
    perks: "DictionaryComponentResponseOfint32AndDestinyItemPerksComponent" = attr.field()


@attr.define
class DictionaryComponentResponseOfint32AndDestinyItemInstanceComponent(BaseModel):
    """
    _No description given by bungie_

    Attributes:
        data: _No description given by bungie_
        privacy: _No description given by bungie_
        disabled: If true, this component is disabled.
    """

    data: Any = attr.field()
    privacy: "ComponentPrivacySetting" = attr.field()
    disabled: bool = attr.field()


@attr.define
class DictionaryComponentResponseOfint32AndDestinyItemRenderComponent(BaseModel):
    """
    _No description given by bungie_

    Attributes:
        data: _No description given by bungie_
        privacy: _No description given by bungie_
        disabled: If true, this component is disabled.
    """

    data: Any = attr.field()
    privacy: "ComponentPrivacySetting" = attr.field()
    disabled: bool = attr.field()


@attr.define
class DictionaryComponentResponseOfint32AndDestinyItemStatsComponent(BaseModel):
    """
    _No description given by bungie_

    Attributes:
        data: _No description given by bungie_
        privacy: _No description given by bungie_
        disabled: If true, this component is disabled.
    """

    data: Any = attr.field()
    privacy: "ComponentPrivacySetting" = attr.field()
    disabled: bool = attr.field()


@attr.define
class DictionaryComponentResponseOfint32AndDestinyItemSocketsComponent(BaseModel):
    """
    _No description given by bungie_

    Attributes:
        data: _No description given by bungie_
        privacy: _No description given by bungie_
        disabled: If true, this component is disabled.
    """

    data: Any = attr.field()
    privacy: "ComponentPrivacySetting" = attr.field()
    disabled: bool = attr.field()


@attr.define
class DictionaryComponentResponseOfint32AndDestinyItemReusablePlugsComponent(BaseModel):
    """
    _No description given by bungie_

    Attributes:
        data: _No description given by bungie_
        privacy: _No description given by bungie_
        disabled: If true, this component is disabled.
    """

    data: Any = attr.field()
    privacy: "ComponentPrivacySetting" = attr.field()
    disabled: bool = attr.field()


@attr.define
class DictionaryComponentResponseOfint32AndDestinyItemPlugObjectivesComponent(BaseModel):
    """
    _No description given by bungie_

    Attributes:
        data: _No description given by bungie_
        privacy: _No description given by bungie_
        disabled: If true, this component is disabled.
    """

    data: Any = attr.field()
    privacy: "ComponentPrivacySetting" = attr.field()
    disabled: bool = attr.field()


@attr.define
class DictionaryComponentResponseOfint32AndDestinyItemTalentGridComponent(BaseModel):
    """
    _No description given by bungie_

    Attributes:
        data: _No description given by bungie_
        privacy: _No description given by bungie_
        disabled: If true, this component is disabled.
    """

    data: Any = attr.field()
    privacy: "ComponentPrivacySetting" = attr.field()
    disabled: bool = attr.field()


@attr.define
class SingleComponentResponseOfDestinyVendorComponent(BaseModel):
    """
    _No description given by bungie_

    Attributes:
        data: _No description given by bungie_
        privacy: _No description given by bungie_
        disabled: If true, this component is disabled.
    """

    data: "DestinyVendorComponent" = attr.field()
    privacy: "ComponentPrivacySetting" = attr.field()
    disabled: bool = attr.field()


@attr.define
class SingleComponentResponseOfDestinyVendorCategoriesComponent(BaseModel):
    """
    _No description given by bungie_

    Attributes:
        data: _No description given by bungie_
        privacy: _No description given by bungie_
        disabled: If true, this component is disabled.
    """

    data: "DestinyVendorCategoriesComponent" = attr.field()
    privacy: "ComponentPrivacySetting" = attr.field()
    disabled: bool = attr.field()


@attr.define
class DictionaryComponentResponseOfint32AndDestinyVendorSaleItemComponent(BaseModel):
    """
    _No description given by bungie_

    Attributes:
        data: _No description given by bungie_
        privacy: _No description given by bungie_
        disabled: If true, this component is disabled.
    """

    data: Any = attr.field()
    privacy: "ComponentPrivacySetting" = attr.field()
    disabled: bool = attr.field()


@attr.define
class DictionaryComponentResponseOfuint32AndDestinyPublicVendorComponent(BaseModel):
    """
    _No description given by bungie_

    Attributes:
        data: _No description given by bungie_
        privacy: _No description given by bungie_
        disabled: If true, this component is disabled.
    """

    data: Any = attr.field()
    privacy: "ComponentPrivacySetting" = attr.field()
    disabled: bool = attr.field()


@attr.define
class DestinyVendorSaleItemSetComponentOfDestinyPublicVendorSaleItemComponent(BaseModel):
    """
    _No description given by bungie_

    Attributes:
        sale_items: _No description given by bungie_
    """

    sale_items: Any = attr.field()


@attr.define
class DictionaryComponentResponseOfuint32AndPublicDestinyVendorSaleItemSetComponent(BaseModel):
    """
    _No description given by bungie_

    Attributes:
        data: _No description given by bungie_
        privacy: _No description given by bungie_
        disabled: If true, this component is disabled.
    """

    data: Any = attr.field()
    privacy: "ComponentPrivacySetting" = attr.field()
    disabled: bool = attr.field()


@attr.define
class DestinyItemComponentSetOfuint32(BaseModel):
    """
    _No description given by bungie_

    Attributes:
        instances: _No description given by bungie_
        render_data: _No description given by bungie_
        stats: _No description given by bungie_
        sockets: _No description given by bungie_
        reusable_plugs: _No description given by bungie_
        plug_objectives: _No description given by bungie_
        talent_grids: _No description given by bungie_
        plug_states: _No description given by bungie_
        objectives: _No description given by bungie_
        perks: _No description given by bungie_
    """

    instances: "DictionaryComponentResponseOfuint32AndDestinyItemInstanceComponent" = attr.field()
    render_data: "DictionaryComponentResponseOfuint32AndDestinyItemRenderComponent" = attr.field()
    stats: "DictionaryComponentResponseOfuint32AndDestinyItemStatsComponent" = attr.field()
    sockets: "DictionaryComponentResponseOfuint32AndDestinyItemSocketsComponent" = attr.field()
    reusable_plugs: "DictionaryComponentResponseOfuint32AndDestinyItemReusablePlugsComponent" = attr.field()
    plug_objectives: "DictionaryComponentResponseOfuint32AndDestinyItemPlugObjectivesComponent" = attr.field()
    talent_grids: "DictionaryComponentResponseOfuint32AndDestinyItemTalentGridComponent" = attr.field()
    plug_states: "DictionaryComponentResponseOfuint32AndDestinyItemPlugComponent" = attr.field()
    objectives: "DictionaryComponentResponseOfuint32AndDestinyItemObjectivesComponent" = attr.field()
    perks: "DictionaryComponentResponseOfuint32AndDestinyItemPerksComponent" = attr.field()


@attr.define
class DictionaryComponentResponseOfuint32AndDestinyItemInstanceComponent(BaseModel):
    """
    _No description given by bungie_

    Attributes:
        data: _No description given by bungie_
        privacy: _No description given by bungie_
        disabled: If true, this component is disabled.
    """

    data: Any = attr.field()
    privacy: "ComponentPrivacySetting" = attr.field()
    disabled: bool = attr.field()


@attr.define
class DictionaryComponentResponseOfuint32AndDestinyItemRenderComponent(BaseModel):
    """
    _No description given by bungie_

    Attributes:
        data: _No description given by bungie_
        privacy: _No description given by bungie_
        disabled: If true, this component is disabled.
    """

    data: Any = attr.field()
    privacy: "ComponentPrivacySetting" = attr.field()
    disabled: bool = attr.field()


@attr.define
class DictionaryComponentResponseOfuint32AndDestinyItemStatsComponent(BaseModel):
    """
    _No description given by bungie_

    Attributes:
        data: _No description given by bungie_
        privacy: _No description given by bungie_
        disabled: If true, this component is disabled.
    """

    data: Any = attr.field()
    privacy: "ComponentPrivacySetting" = attr.field()
    disabled: bool = attr.field()


@attr.define
class DictionaryComponentResponseOfuint32AndDestinyItemSocketsComponent(BaseModel):
    """
    _No description given by bungie_

    Attributes:
        data: _No description given by bungie_
        privacy: _No description given by bungie_
        disabled: If true, this component is disabled.
    """

    data: Any = attr.field()
    privacy: "ComponentPrivacySetting" = attr.field()
    disabled: bool = attr.field()


@attr.define
class DictionaryComponentResponseOfuint32AndDestinyItemReusablePlugsComponent(BaseModel):
    """
    _No description given by bungie_

    Attributes:
        data: _No description given by bungie_
        privacy: _No description given by bungie_
        disabled: If true, this component is disabled.
    """

    data: Any = attr.field()
    privacy: "ComponentPrivacySetting" = attr.field()
    disabled: bool = attr.field()


@attr.define
class DictionaryComponentResponseOfuint32AndDestinyItemPlugObjectivesComponent(BaseModel):
    """
    _No description given by bungie_

    Attributes:
        data: _No description given by bungie_
        privacy: _No description given by bungie_
        disabled: If true, this component is disabled.
    """

    data: Any = attr.field()
    privacy: "ComponentPrivacySetting" = attr.field()
    disabled: bool = attr.field()


@attr.define
class DictionaryComponentResponseOfuint32AndDestinyItemTalentGridComponent(BaseModel):
    """
    _No description given by bungie_

    Attributes:
        data: _No description given by bungie_
        privacy: _No description given by bungie_
        disabled: If true, this component is disabled.
    """

    data: Any = attr.field()
    privacy: "ComponentPrivacySetting" = attr.field()
    disabled: bool = attr.field()


@attr.define
class SearchResultOfDestinyEntitySearchResultItem(BaseModel):
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

    results: list["DestinyEntitySearchResultItem"] = attr.field()
    total_results: int = attr.field()
    has_more: bool = attr.field()
    query: "PagedQuery" = attr.field()
    replacement_continuation_token: str = attr.field()
    use_total_results: bool = attr.field()


@attr.define
class SearchResultOfTrendingEntry(BaseModel):
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

    results: list["TrendingEntry"] = attr.field()
    total_results: int = attr.field()
    has_more: bool = attr.field()
    query: "PagedQuery" = attr.field()
    replacement_continuation_token: str = attr.field()
    use_total_results: bool = attr.field()


@attr.define
class SearchResultOfFireteamSummary(BaseModel):
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

    results: list["FireteamSummary"] = attr.field()
    total_results: int = attr.field()
    has_more: bool = attr.field()
    query: "PagedQuery" = attr.field()
    replacement_continuation_token: str = attr.field()
    use_total_results: bool = attr.field()


@attr.define
class SearchResultOfFireteamResponse(BaseModel):
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

    results: list["FireteamResponse"] = attr.field()
    total_results: int = attr.field()
    has_more: bool = attr.field()
    query: "PagedQuery" = attr.field()
    replacement_continuation_token: str = attr.field()
    use_total_results: bool = attr.field()


@attr.define
class GlobalAlert(BaseModel):
    """
    _No description given by bungie_

    Attributes:
        alert_key: _No description given by bungie_
        alert_html: _No description given by bungie_
        alert_timestamp: _No description given by bungie_
        alert_link: _No description given by bungie_
        alert_level: _No description given by bungie_
        alert_type: _No description given by bungie_
        stream_info: _No description given by bungie_
    """

    alert_key: str = attr.field()
    alert_html: str = attr.field()
    alert_timestamp: datetime.datetime = attr.field()
    alert_link: str = attr.field()
    alert_level: "GlobalAlertLevel" = attr.field()
    alert_type: "GlobalAlertType" = attr.field()
    stream_info: "StreamInfo" = attr.field()


class GlobalAlertLevel(BaseEnum):
    """
    _No description given by bungie_
    """

    UNKNOWN = 0
    """_No description given by bungie_ """
    BLUE = 1
    """_No description given by bungie_ """
    YELLOW = 2
    """_No description given by bungie_ """
    RED = 3
    """_No description given by bungie_ """


class GlobalAlertType(BaseEnum):
    """
    _No description given by bungie_
    """

    GLOBAL_ALERT = 0
    """_No description given by bungie_ """
    STREAMING_ALERT = 1
    """_No description given by bungie_ """


@attr.define
class StreamInfo(BaseModel):
    """
    _No description given by bungie_

    Attributes:
        channel_name: _No description given by bungie_
    """

    channel_name: str = attr.field()
