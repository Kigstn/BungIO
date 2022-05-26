import datetime
from typing import TYPE_CHECKING, Any, Optional

import attr

from bungio.models.base import BaseEnum, BaseModel


class BungieMembershipType(BaseEnum):
    """
    The types of membership the Accounts system supports. This is the external facing enum used in place of the internal-only Bungie.SharedDefinitions.MembershipType.
    """

    NONE = 0
    """Not specified. """
    TIGER_XBOX = 1
    """Not specified. """
    TIGER_PSN = 2
    """Not specified. """
    TIGER_STEAM = 3
    """Not specified. """
    TIGER_BLIZZARD = 4
    """Not specified. """
    TIGER_STADIA = 5
    """Not specified. """
    TIGER_DEMON = 10
    """Not specified. """
    BUNGIE_NEXT = 254
    """Not specified. """
    ALL = -1
    """"All" is only valid for searching capabilities: you need to pass the actual matching BungieMembershipType for any query where you pass a known membershipId. """


class BungieCredentialType(BaseEnum):
    """
    The types of credentials the Accounts system supports. This is the external facing enum used in place of the internal-only Bungie.SharedDefinitions.CredentialType.
    """

    NONE = 0
    """Not specified. """
    XUID = 1
    """Not specified. """
    PSNID = 2
    """Not specified. """
    WLID = 3
    """Not specified. """
    FAKE = 4
    """Not specified. """
    FACEBOOK = 5
    """Not specified. """
    GOOGLE = 8
    """Not specified. """
    WINDOWS = 9
    """Not specified. """
    DEMON_ID = 10
    """Not specified. """
    STEAM_ID = 12
    """Not specified. """
    BATTLE_NET_ID = 14
    """Not specified. """
    STADIA_ID = 16
    """Not specified. """
    TWITCH_ID = 18
    """Not specified. """


@attr.define
class SearchResultOfContentItemPublicContract(BaseModel):
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

    results: list["ContentItemPublicContract"] = attr.field()
    total_results: int = attr.field()
    has_more: bool = attr.field()
    query: "PagedQuery" = attr.field()
    replacement_continuation_token: str = attr.field()
    use_total_results: bool = attr.field()


@attr.define
class SearchResultOfPostResponse(BaseModel):
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

    results: list["PostResponse"] = attr.field()
    total_results: int = attr.field()
    has_more: bool = attr.field()
    query: "PagedQuery" = attr.field()
    replacement_continuation_token: str = attr.field()
    use_total_results: bool = attr.field()


@attr.define
class SearchResultOfGroupV2Card(BaseModel):
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
class SearchResultOfGroupMember(BaseModel):
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

    results: list["GroupMember"] = attr.field()
    total_results: int = attr.field()
    has_more: bool = attr.field()
    query: "PagedQuery" = attr.field()
    replacement_continuation_token: str = attr.field()
    use_total_results: bool = attr.field()


@attr.define
class SearchResultOfGroupBan(BaseModel):
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

    results: list["GroupBan"] = attr.field()
    total_results: int = attr.field()
    has_more: bool = attr.field()
    query: "PagedQuery" = attr.field()
    replacement_continuation_token: str = attr.field()
    use_total_results: bool = attr.field()


@attr.define
class SearchResultOfGroupMemberApplication(BaseModel):
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

    results: list["GroupMemberApplication"] = attr.field()
    total_results: int = attr.field()
    has_more: bool = attr.field()
    query: "PagedQuery" = attr.field()
    replacement_continuation_token: str = attr.field()
    use_total_results: bool = attr.field()


@attr.define
class SearchResultOfGroupMembership(BaseModel):
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
class SearchResultOfGroupPotentialMembership(BaseModel):
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
class SingleComponentResponseOfDestinyVendorReceiptsComponent(BaseModel):
    """
    Not specified.

    Attributes:
        data: Not specified.
        privacy: Not specified.
        disabled: If true, this component is disabled.
    """

    data: "DestinyVendorReceiptsComponent" = attr.field()
    privacy: int = attr.field()
    disabled: bool = attr.field()


@attr.define
class SingleComponentResponseOfDestinyInventoryComponent(BaseModel):
    """
    Not specified.

    Attributes:
        data: Not specified.
        privacy: Not specified.
        disabled: If true, this component is disabled.
    """

    data: "DestinyInventoryComponent" = attr.field()
    privacy: int = attr.field()
    disabled: bool = attr.field()


@attr.define
class SingleComponentResponseOfDestinyProfileComponent(BaseModel):
    """
    Not specified.

    Attributes:
        data: Not specified.
        privacy: Not specified.
        disabled: If true, this component is disabled.
    """

    data: "DestinyProfileComponent" = attr.field()
    privacy: int = attr.field()
    disabled: bool = attr.field()


@attr.define
class SingleComponentResponseOfDestinyPlatformSilverComponent(BaseModel):
    """
    Not specified.

    Attributes:
        data: Not specified.
        privacy: Not specified.
        disabled: If true, this component is disabled.
    """

    data: "DestinyPlatformSilverComponent" = attr.field()
    privacy: int = attr.field()
    disabled: bool = attr.field()


@attr.define
class SingleComponentResponseOfDestinyKiosksComponent(BaseModel):
    """
    Not specified.

    Attributes:
        data: Not specified.
        privacy: Not specified.
        disabled: If true, this component is disabled.
    """

    data: "DestinyKiosksComponent" = attr.field()
    privacy: int = attr.field()
    disabled: bool = attr.field()


@attr.define
class SingleComponentResponseOfDestinyPlugSetsComponent(BaseModel):
    """
    Not specified.

    Attributes:
        data: Not specified.
        privacy: Not specified.
        disabled: If true, this component is disabled.
    """

    data: "DestinyPlugSetsComponent" = attr.field()
    privacy: int = attr.field()
    disabled: bool = attr.field()


@attr.define
class SingleComponentResponseOfDestinyProfileProgressionComponent(BaseModel):
    """
    Not specified.

    Attributes:
        data: Not specified.
        privacy: Not specified.
        disabled: If true, this component is disabled.
    """

    data: "DestinyProfileProgressionComponent" = attr.field()
    privacy: int = attr.field()
    disabled: bool = attr.field()


@attr.define
class SingleComponentResponseOfDestinyPresentationNodesComponent(BaseModel):
    """
    Not specified.

    Attributes:
        data: Not specified.
        privacy: Not specified.
        disabled: If true, this component is disabled.
    """

    data: "DestinyPresentationNodesComponent" = attr.field()
    privacy: int = attr.field()
    disabled: bool = attr.field()


@attr.define
class SingleComponentResponseOfDestinyProfileRecordsComponent(BaseModel):
    """
    Not specified.

    Attributes:
        data: Not specified.
        privacy: Not specified.
        disabled: If true, this component is disabled.
    """

    data: "DestinyProfileRecordsComponent" = attr.field()
    privacy: int = attr.field()
    disabled: bool = attr.field()


@attr.define
class SingleComponentResponseOfDestinyProfileCollectiblesComponent(BaseModel):
    """
    Not specified.

    Attributes:
        data: Not specified.
        privacy: Not specified.
        disabled: If true, this component is disabled.
    """

    data: "DestinyProfileCollectiblesComponent" = attr.field()
    privacy: int = attr.field()
    disabled: bool = attr.field()


@attr.define
class SingleComponentResponseOfDestinyProfileTransitoryComponent(BaseModel):
    """
    Not specified.

    Attributes:
        data: Not specified.
        privacy: Not specified.
        disabled: If true, this component is disabled.
    """

    data: "DestinyProfileTransitoryComponent" = attr.field()
    privacy: int = attr.field()
    disabled: bool = attr.field()


@attr.define
class SingleComponentResponseOfDestinyMetricsComponent(BaseModel):
    """
    Not specified.

    Attributes:
        data: Not specified.
        privacy: Not specified.
        disabled: If true, this component is disabled.
    """

    data: "DestinyMetricsComponent" = attr.field()
    privacy: int = attr.field()
    disabled: bool = attr.field()


@attr.define
class SingleComponentResponseOfDestinyStringVariablesComponent(BaseModel):
    """
    Not specified.

    Attributes:
        data: Not specified.
        privacy: Not specified.
        disabled: If true, this component is disabled.
    """

    data: "DestinyStringVariablesComponent" = attr.field()
    privacy: int = attr.field()
    disabled: bool = attr.field()


@attr.define
class DictionaryComponentResponseOfint64AndDestinyCharacterComponent(BaseModel):
    """
    Not specified.

    Attributes:
        data: Not specified.
        privacy: Not specified.
        disabled: If true, this component is disabled.
    """

    data: Any = attr.field()
    privacy: int = attr.field()
    disabled: bool = attr.field()


@attr.define
class DictionaryComponentResponseOfint64AndDestinyInventoryComponent(BaseModel):
    """
    Not specified.

    Attributes:
        data: Not specified.
        privacy: Not specified.
        disabled: If true, this component is disabled.
    """

    data: Any = attr.field()
    privacy: int = attr.field()
    disabled: bool = attr.field()


@attr.define
class DictionaryComponentResponseOfint64AndDestinyCharacterProgressionComponent(BaseModel):
    """
    Not specified.

    Attributes:
        data: Not specified.
        privacy: Not specified.
        disabled: If true, this component is disabled.
    """

    data: Any = attr.field()
    privacy: int = attr.field()
    disabled: bool = attr.field()


@attr.define
class DictionaryComponentResponseOfint64AndDestinyCharacterRenderComponent(BaseModel):
    """
    Not specified.

    Attributes:
        data: Not specified.
        privacy: Not specified.
        disabled: If true, this component is disabled.
    """

    data: Any = attr.field()
    privacy: int = attr.field()
    disabled: bool = attr.field()


@attr.define
class DictionaryComponentResponseOfint64AndDestinyCharacterActivitiesComponent(BaseModel):
    """
    Not specified.

    Attributes:
        data: Not specified.
        privacy: Not specified.
        disabled: If true, this component is disabled.
    """

    data: Any = attr.field()
    privacy: int = attr.field()
    disabled: bool = attr.field()


@attr.define
class DictionaryComponentResponseOfint64AndDestinyKiosksComponent(BaseModel):
    """
    Not specified.

    Attributes:
        data: Not specified.
        privacy: Not specified.
        disabled: If true, this component is disabled.
    """

    data: Any = attr.field()
    privacy: int = attr.field()
    disabled: bool = attr.field()


@attr.define
class DictionaryComponentResponseOfint64AndDestinyPlugSetsComponent(BaseModel):
    """
    Not specified.

    Attributes:
        data: Not specified.
        privacy: Not specified.
        disabled: If true, this component is disabled.
    """

    data: Any = attr.field()
    privacy: int = attr.field()
    disabled: bool = attr.field()


@attr.define
class DestinyBaseItemComponentSetOfuint32(BaseModel):
    """
    Not specified.

    Attributes:
        objectives: Not specified.
        perks: Not specified.
    """

    objectives: "DictionaryComponentResponseOfuint32AndDestinyItemObjectivesComponent" = attr.field()
    perks: "DictionaryComponentResponseOfuint32AndDestinyItemPerksComponent" = attr.field()


@attr.define
class DictionaryComponentResponseOfuint32AndDestinyItemObjectivesComponent(BaseModel):
    """
    Not specified.

    Attributes:
        data: Not specified.
        privacy: Not specified.
        disabled: If true, this component is disabled.
    """

    data: Any = attr.field()
    privacy: int = attr.field()
    disabled: bool = attr.field()


@attr.define
class DictionaryComponentResponseOfuint32AndDestinyItemPerksComponent(BaseModel):
    """
    Not specified.

    Attributes:
        data: Not specified.
        privacy: Not specified.
        disabled: If true, this component is disabled.
    """

    data: Any = attr.field()
    privacy: int = attr.field()
    disabled: bool = attr.field()


@attr.define
class DictionaryComponentResponseOfint64AndDestinyPresentationNodesComponent(BaseModel):
    """
    Not specified.

    Attributes:
        data: Not specified.
        privacy: Not specified.
        disabled: If true, this component is disabled.
    """

    data: Any = attr.field()
    privacy: int = attr.field()
    disabled: bool = attr.field()


@attr.define
class DictionaryComponentResponseOfint64AndDestinyCharacterRecordsComponent(BaseModel):
    """
    Not specified.

    Attributes:
        data: Not specified.
        privacy: Not specified.
        disabled: If true, this component is disabled.
    """

    data: Any = attr.field()
    privacy: int = attr.field()
    disabled: bool = attr.field()


@attr.define
class DictionaryComponentResponseOfint64AndDestinyCollectiblesComponent(BaseModel):
    """
    Not specified.

    Attributes:
        data: Not specified.
        privacy: Not specified.
        disabled: If true, this component is disabled.
    """

    data: Any = attr.field()
    privacy: int = attr.field()
    disabled: bool = attr.field()


@attr.define
class DictionaryComponentResponseOfint64AndDestinyStringVariablesComponent(BaseModel):
    """
    Not specified.

    Attributes:
        data: Not specified.
        privacy: Not specified.
        disabled: If true, this component is disabled.
    """

    data: Any = attr.field()
    privacy: int = attr.field()
    disabled: bool = attr.field()


@attr.define
class DictionaryComponentResponseOfint64AndDestinyCraftablesComponent(BaseModel):
    """
    Not specified.

    Attributes:
        data: Not specified.
        privacy: Not specified.
        disabled: If true, this component is disabled.
    """

    data: Any = attr.field()
    privacy: int = attr.field()
    disabled: bool = attr.field()


@attr.define
class DestinyBaseItemComponentSetOfint64(BaseModel):
    """
    Not specified.

    Attributes:
        objectives: Not specified.
        perks: Not specified.
    """

    objectives: "DictionaryComponentResponseOfint64AndDestinyItemObjectivesComponent" = attr.field()
    perks: "DictionaryComponentResponseOfint64AndDestinyItemPerksComponent" = attr.field()


@attr.define
class DictionaryComponentResponseOfint64AndDestinyItemObjectivesComponent(BaseModel):
    """
    Not specified.

    Attributes:
        data: Not specified.
        privacy: Not specified.
        disabled: If true, this component is disabled.
    """

    data: Any = attr.field()
    privacy: int = attr.field()
    disabled: bool = attr.field()


@attr.define
class DictionaryComponentResponseOfint64AndDestinyItemPerksComponent(BaseModel):
    """
    Not specified.

    Attributes:
        data: Not specified.
        privacy: Not specified.
        disabled: If true, this component is disabled.
    """

    data: Any = attr.field()
    privacy: int = attr.field()
    disabled: bool = attr.field()


@attr.define
class DestinyItemComponentSetOfint64(BaseModel):
    """
    Not specified.

    Attributes:
        instances: Not specified.
        render_data: Not specified.
        stats: Not specified.
        sockets: Not specified.
        reusable_plugs: Not specified.
        plug_objectives: Not specified.
        talent_grids: Not specified.
        plug_states: Not specified.
        objectives: Not specified.
        perks: Not specified.
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
    Not specified.

    Attributes:
        data: Not specified.
        privacy: Not specified.
        disabled: If true, this component is disabled.
    """

    data: Any = attr.field()
    privacy: int = attr.field()
    disabled: bool = attr.field()


@attr.define
class DictionaryComponentResponseOfint64AndDestinyItemRenderComponent(BaseModel):
    """
    Not specified.

    Attributes:
        data: Not specified.
        privacy: Not specified.
        disabled: If true, this component is disabled.
    """

    data: Any = attr.field()
    privacy: int = attr.field()
    disabled: bool = attr.field()


@attr.define
class DictionaryComponentResponseOfint64AndDestinyItemStatsComponent(BaseModel):
    """
    Not specified.

    Attributes:
        data: Not specified.
        privacy: Not specified.
        disabled: If true, this component is disabled.
    """

    data: Any = attr.field()
    privacy: int = attr.field()
    disabled: bool = attr.field()


@attr.define
class DictionaryComponentResponseOfint64AndDestinyItemSocketsComponent(BaseModel):
    """
    Not specified.

    Attributes:
        data: Not specified.
        privacy: Not specified.
        disabled: If true, this component is disabled.
    """

    data: Any = attr.field()
    privacy: int = attr.field()
    disabled: bool = attr.field()


@attr.define
class DictionaryComponentResponseOfint64AndDestinyItemReusablePlugsComponent(BaseModel):
    """
    Not specified.

    Attributes:
        data: Not specified.
        privacy: Not specified.
        disabled: If true, this component is disabled.
    """

    data: Any = attr.field()
    privacy: int = attr.field()
    disabled: bool = attr.field()


@attr.define
class DictionaryComponentResponseOfint64AndDestinyItemPlugObjectivesComponent(BaseModel):
    """
    Not specified.

    Attributes:
        data: Not specified.
        privacy: Not specified.
        disabled: If true, this component is disabled.
    """

    data: Any = attr.field()
    privacy: int = attr.field()
    disabled: bool = attr.field()


@attr.define
class DictionaryComponentResponseOfint64AndDestinyItemTalentGridComponent(BaseModel):
    """
    Not specified.

    Attributes:
        data: Not specified.
        privacy: Not specified.
        disabled: If true, this component is disabled.
    """

    data: Any = attr.field()
    privacy: int = attr.field()
    disabled: bool = attr.field()


@attr.define
class DictionaryComponentResponseOfuint32AndDestinyItemPlugComponent(BaseModel):
    """
    Not specified.

    Attributes:
        data: Not specified.
        privacy: Not specified.
        disabled: If true, this component is disabled.
    """

    data: Any = attr.field()
    privacy: int = attr.field()
    disabled: bool = attr.field()


@attr.define
class DictionaryComponentResponseOfint64AndDestinyCurrenciesComponent(BaseModel):
    """
    Not specified.

    Attributes:
        data: Not specified.
        privacy: Not specified.
        disabled: If true, this component is disabled.
    """

    data: Any = attr.field()
    privacy: int = attr.field()
    disabled: bool = attr.field()


@attr.define
class SingleComponentResponseOfDestinyCharacterComponent(BaseModel):
    """
    Not specified.

    Attributes:
        data: Not specified.
        privacy: Not specified.
        disabled: If true, this component is disabled.
    """

    data: "DestinyCharacterComponent" = attr.field()
    privacy: int = attr.field()
    disabled: bool = attr.field()


@attr.define
class SingleComponentResponseOfDestinyCharacterProgressionComponent(BaseModel):
    """
    Not specified.

    Attributes:
        data: Not specified.
        privacy: Not specified.
        disabled: If true, this component is disabled.
    """

    data: "DestinyCharacterProgressionComponent" = attr.field()
    privacy: int = attr.field()
    disabled: bool = attr.field()


@attr.define
class SingleComponentResponseOfDestinyCharacterRenderComponent(BaseModel):
    """
    Not specified.

    Attributes:
        data: Not specified.
        privacy: Not specified.
        disabled: If true, this component is disabled.
    """

    data: "DestinyCharacterRenderComponent" = attr.field()
    privacy: int = attr.field()
    disabled: bool = attr.field()


@attr.define
class SingleComponentResponseOfDestinyCharacterActivitiesComponent(BaseModel):
    """
    Not specified.

    Attributes:
        data: Not specified.
        privacy: Not specified.
        disabled: If true, this component is disabled.
    """

    data: "DestinyCharacterActivitiesComponent" = attr.field()
    privacy: int = attr.field()
    disabled: bool = attr.field()


@attr.define
class SingleComponentResponseOfDestinyCharacterRecordsComponent(BaseModel):
    """
    Not specified.

    Attributes:
        data: Not specified.
        privacy: Not specified.
        disabled: If true, this component is disabled.
    """

    data: "DestinyCharacterRecordsComponent" = attr.field()
    privacy: int = attr.field()
    disabled: bool = attr.field()


@attr.define
class SingleComponentResponseOfDestinyCollectiblesComponent(BaseModel):
    """
    Not specified.

    Attributes:
        data: Not specified.
        privacy: Not specified.
        disabled: If true, this component is disabled.
    """

    data: "DestinyCollectiblesComponent" = attr.field()
    privacy: int = attr.field()
    disabled: bool = attr.field()


@attr.define
class SingleComponentResponseOfDestinyCurrenciesComponent(BaseModel):
    """
    Not specified.

    Attributes:
        data: Not specified.
        privacy: Not specified.
        disabled: If true, this component is disabled.
    """

    data: "DestinyCurrenciesComponent" = attr.field()
    privacy: int = attr.field()
    disabled: bool = attr.field()


@attr.define
class SingleComponentResponseOfDestinyItemComponent(BaseModel):
    """
    Not specified.

    Attributes:
        data: Not specified.
        privacy: Not specified.
        disabled: If true, this component is disabled.
    """

    data: "DestinyItemComponent" = attr.field()
    privacy: int = attr.field()
    disabled: bool = attr.field()


@attr.define
class SingleComponentResponseOfDestinyItemInstanceComponent(BaseModel):
    """
    Not specified.

    Attributes:
        data: Not specified.
        privacy: Not specified.
        disabled: If true, this component is disabled.
    """

    data: "DestinyItemInstanceComponent" = attr.field()
    privacy: int = attr.field()
    disabled: bool = attr.field()


@attr.define
class SingleComponentResponseOfDestinyItemObjectivesComponent(BaseModel):
    """
    Not specified.

    Attributes:
        data: Not specified.
        privacy: Not specified.
        disabled: If true, this component is disabled.
    """

    data: "DestinyItemObjectivesComponent" = attr.field()
    privacy: int = attr.field()
    disabled: bool = attr.field()


@attr.define
class SingleComponentResponseOfDestinyItemPerksComponent(BaseModel):
    """
    Not specified.

    Attributes:
        data: Not specified.
        privacy: Not specified.
        disabled: If true, this component is disabled.
    """

    data: "DestinyItemPerksComponent" = attr.field()
    privacy: int = attr.field()
    disabled: bool = attr.field()


@attr.define
class SingleComponentResponseOfDestinyItemRenderComponent(BaseModel):
    """
    Not specified.

    Attributes:
        data: Not specified.
        privacy: Not specified.
        disabled: If true, this component is disabled.
    """

    data: "DestinyItemRenderComponent" = attr.field()
    privacy: int = attr.field()
    disabled: bool = attr.field()


@attr.define
class SingleComponentResponseOfDestinyItemStatsComponent(BaseModel):
    """
    Not specified.

    Attributes:
        data: Not specified.
        privacy: Not specified.
        disabled: If true, this component is disabled.
    """

    data: "DestinyItemStatsComponent" = attr.field()
    privacy: int = attr.field()
    disabled: bool = attr.field()


@attr.define
class SingleComponentResponseOfDestinyItemTalentGridComponent(BaseModel):
    """
    Not specified.

    Attributes:
        data: Not specified.
        privacy: Not specified.
        disabled: If true, this component is disabled.
    """

    data: "DestinyItemTalentGridComponent" = attr.field()
    privacy: int = attr.field()
    disabled: bool = attr.field()


@attr.define
class SingleComponentResponseOfDestinyItemSocketsComponent(BaseModel):
    """
    Not specified.

    Attributes:
        data: Not specified.
        privacy: Not specified.
        disabled: If true, this component is disabled.
    """

    data: "DestinyItemSocketsComponent" = attr.field()
    privacy: int = attr.field()
    disabled: bool = attr.field()


@attr.define
class SingleComponentResponseOfDestinyItemReusablePlugsComponent(BaseModel):
    """
    Not specified.

    Attributes:
        data: Not specified.
        privacy: Not specified.
        disabled: If true, this component is disabled.
    """

    data: "DestinyItemReusablePlugsComponent" = attr.field()
    privacy: int = attr.field()
    disabled: bool = attr.field()


@attr.define
class SingleComponentResponseOfDestinyItemPlugObjectivesComponent(BaseModel):
    """
    Not specified.

    Attributes:
        data: Not specified.
        privacy: Not specified.
        disabled: If true, this component is disabled.
    """

    data: "DestinyItemPlugObjectivesComponent" = attr.field()
    privacy: int = attr.field()
    disabled: bool = attr.field()


@attr.define
class SingleComponentResponseOfDestinyVendorGroupComponent(BaseModel):
    """
    Not specified.

    Attributes:
        data: Not specified.
        privacy: Not specified.
        disabled: If true, this component is disabled.
    """

    data: "DestinyVendorGroupComponent" = attr.field()
    privacy: int = attr.field()
    disabled: bool = attr.field()


@attr.define
class DictionaryComponentResponseOfuint32AndDestinyVendorComponent(BaseModel):
    """
    Not specified.

    Attributes:
        data: Not specified.
        privacy: Not specified.
        disabled: If true, this component is disabled.
    """

    data: Any = attr.field()
    privacy: int = attr.field()
    disabled: bool = attr.field()


@attr.define
class DictionaryComponentResponseOfuint32AndDestinyVendorCategoriesComponent(BaseModel):
    """
    Not specified.

    Attributes:
        data: Not specified.
        privacy: Not specified.
        disabled: If true, this component is disabled.
    """

    data: Any = attr.field()
    privacy: int = attr.field()
    disabled: bool = attr.field()


@attr.define
class DestinyVendorSaleItemSetComponentOfDestinyVendorSaleItemComponent(BaseModel):
    """
    Not specified.

    Attributes:
        sale_items: Not specified.
    """

    sale_items: Any = attr.field()


@attr.define
class DictionaryComponentResponseOfuint32AndPersonalDestinyVendorSaleItemSetComponent(BaseModel):
    """
    Not specified.

    Attributes:
        data: Not specified.
        privacy: Not specified.
        disabled: If true, this component is disabled.
    """

    data: Any = attr.field()
    privacy: int = attr.field()
    disabled: bool = attr.field()


@attr.define
class DestinyBaseItemComponentSetOfint32(BaseModel):
    """
    Not specified.

    Attributes:
        objectives: Not specified.
        perks: Not specified.
    """

    objectives: "DictionaryComponentResponseOfint32AndDestinyItemObjectivesComponent" = attr.field()
    perks: "DictionaryComponentResponseOfint32AndDestinyItemPerksComponent" = attr.field()


@attr.define
class DictionaryComponentResponseOfint32AndDestinyItemObjectivesComponent(BaseModel):
    """
    Not specified.

    Attributes:
        data: Not specified.
        privacy: Not specified.
        disabled: If true, this component is disabled.
    """

    data: Any = attr.field()
    privacy: int = attr.field()
    disabled: bool = attr.field()


@attr.define
class DictionaryComponentResponseOfint32AndDestinyItemPerksComponent(BaseModel):
    """
    Not specified.

    Attributes:
        data: Not specified.
        privacy: Not specified.
        disabled: If true, this component is disabled.
    """

    data: Any = attr.field()
    privacy: int = attr.field()
    disabled: bool = attr.field()


@attr.define
class DestinyItemComponentSetOfint32(BaseModel):
    """
    Not specified.

    Attributes:
        instances: Not specified.
        render_data: Not specified.
        stats: Not specified.
        sockets: Not specified.
        reusable_plugs: Not specified.
        plug_objectives: Not specified.
        talent_grids: Not specified.
        plug_states: Not specified.
        objectives: Not specified.
        perks: Not specified.
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
    Not specified.

    Attributes:
        data: Not specified.
        privacy: Not specified.
        disabled: If true, this component is disabled.
    """

    data: Any = attr.field()
    privacy: int = attr.field()
    disabled: bool = attr.field()


@attr.define
class DictionaryComponentResponseOfint32AndDestinyItemRenderComponent(BaseModel):
    """
    Not specified.

    Attributes:
        data: Not specified.
        privacy: Not specified.
        disabled: If true, this component is disabled.
    """

    data: Any = attr.field()
    privacy: int = attr.field()
    disabled: bool = attr.field()


@attr.define
class DictionaryComponentResponseOfint32AndDestinyItemStatsComponent(BaseModel):
    """
    Not specified.

    Attributes:
        data: Not specified.
        privacy: Not specified.
        disabled: If true, this component is disabled.
    """

    data: Any = attr.field()
    privacy: int = attr.field()
    disabled: bool = attr.field()


@attr.define
class DictionaryComponentResponseOfint32AndDestinyItemSocketsComponent(BaseModel):
    """
    Not specified.

    Attributes:
        data: Not specified.
        privacy: Not specified.
        disabled: If true, this component is disabled.
    """

    data: Any = attr.field()
    privacy: int = attr.field()
    disabled: bool = attr.field()


@attr.define
class DictionaryComponentResponseOfint32AndDestinyItemReusablePlugsComponent(BaseModel):
    """
    Not specified.

    Attributes:
        data: Not specified.
        privacy: Not specified.
        disabled: If true, this component is disabled.
    """

    data: Any = attr.field()
    privacy: int = attr.field()
    disabled: bool = attr.field()


@attr.define
class DictionaryComponentResponseOfint32AndDestinyItemPlugObjectivesComponent(BaseModel):
    """
    Not specified.

    Attributes:
        data: Not specified.
        privacy: Not specified.
        disabled: If true, this component is disabled.
    """

    data: Any = attr.field()
    privacy: int = attr.field()
    disabled: bool = attr.field()


@attr.define
class DictionaryComponentResponseOfint32AndDestinyItemTalentGridComponent(BaseModel):
    """
    Not specified.

    Attributes:
        data: Not specified.
        privacy: Not specified.
        disabled: If true, this component is disabled.
    """

    data: Any = attr.field()
    privacy: int = attr.field()
    disabled: bool = attr.field()


@attr.define
class SingleComponentResponseOfDestinyVendorComponent(BaseModel):
    """
    Not specified.

    Attributes:
        data: Not specified.
        privacy: Not specified.
        disabled: If true, this component is disabled.
    """

    data: "DestinyVendorComponent" = attr.field()
    privacy: int = attr.field()
    disabled: bool = attr.field()


@attr.define
class SingleComponentResponseOfDestinyVendorCategoriesComponent(BaseModel):
    """
    Not specified.

    Attributes:
        data: Not specified.
        privacy: Not specified.
        disabled: If true, this component is disabled.
    """

    data: "DestinyVendorCategoriesComponent" = attr.field()
    privacy: int = attr.field()
    disabled: bool = attr.field()


@attr.define
class DictionaryComponentResponseOfint32AndDestinyVendorSaleItemComponent(BaseModel):
    """
    Not specified.

    Attributes:
        data: Not specified.
        privacy: Not specified.
        disabled: If true, this component is disabled.
    """

    data: Any = attr.field()
    privacy: int = attr.field()
    disabled: bool = attr.field()


@attr.define
class DictionaryComponentResponseOfuint32AndDestinyPublicVendorComponent(BaseModel):
    """
    Not specified.

    Attributes:
        data: Not specified.
        privacy: Not specified.
        disabled: If true, this component is disabled.
    """

    data: Any = attr.field()
    privacy: int = attr.field()
    disabled: bool = attr.field()


@attr.define
class DestinyVendorSaleItemSetComponentOfDestinyPublicVendorSaleItemComponent(BaseModel):
    """
    Not specified.

    Attributes:
        sale_items: Not specified.
    """

    sale_items: Any = attr.field()


@attr.define
class DictionaryComponentResponseOfuint32AndPublicDestinyVendorSaleItemSetComponent(BaseModel):
    """
    Not specified.

    Attributes:
        data: Not specified.
        privacy: Not specified.
        disabled: If true, this component is disabled.
    """

    data: Any = attr.field()
    privacy: int = attr.field()
    disabled: bool = attr.field()


@attr.define
class DestinyItemComponentSetOfuint32(BaseModel):
    """
    Not specified.

    Attributes:
        instances: Not specified.
        render_data: Not specified.
        stats: Not specified.
        sockets: Not specified.
        reusable_plugs: Not specified.
        plug_objectives: Not specified.
        talent_grids: Not specified.
        plug_states: Not specified.
        objectives: Not specified.
        perks: Not specified.
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
    Not specified.

    Attributes:
        data: Not specified.
        privacy: Not specified.
        disabled: If true, this component is disabled.
    """

    data: Any = attr.field()
    privacy: int = attr.field()
    disabled: bool = attr.field()


@attr.define
class DictionaryComponentResponseOfuint32AndDestinyItemRenderComponent(BaseModel):
    """
    Not specified.

    Attributes:
        data: Not specified.
        privacy: Not specified.
        disabled: If true, this component is disabled.
    """

    data: Any = attr.field()
    privacy: int = attr.field()
    disabled: bool = attr.field()


@attr.define
class DictionaryComponentResponseOfuint32AndDestinyItemStatsComponent(BaseModel):
    """
    Not specified.

    Attributes:
        data: Not specified.
        privacy: Not specified.
        disabled: If true, this component is disabled.
    """

    data: Any = attr.field()
    privacy: int = attr.field()
    disabled: bool = attr.field()


@attr.define
class DictionaryComponentResponseOfuint32AndDestinyItemSocketsComponent(BaseModel):
    """
    Not specified.

    Attributes:
        data: Not specified.
        privacy: Not specified.
        disabled: If true, this component is disabled.
    """

    data: Any = attr.field()
    privacy: int = attr.field()
    disabled: bool = attr.field()


@attr.define
class DictionaryComponentResponseOfuint32AndDestinyItemReusablePlugsComponent(BaseModel):
    """
    Not specified.

    Attributes:
        data: Not specified.
        privacy: Not specified.
        disabled: If true, this component is disabled.
    """

    data: Any = attr.field()
    privacy: int = attr.field()
    disabled: bool = attr.field()


@attr.define
class DictionaryComponentResponseOfuint32AndDestinyItemPlugObjectivesComponent(BaseModel):
    """
    Not specified.

    Attributes:
        data: Not specified.
        privacy: Not specified.
        disabled: If true, this component is disabled.
    """

    data: Any = attr.field()
    privacy: int = attr.field()
    disabled: bool = attr.field()


@attr.define
class DictionaryComponentResponseOfuint32AndDestinyItemTalentGridComponent(BaseModel):
    """
    Not specified.

    Attributes:
        data: Not specified.
        privacy: Not specified.
        disabled: If true, this component is disabled.
    """

    data: Any = attr.field()
    privacy: int = attr.field()
    disabled: bool = attr.field()


@attr.define
class SearchResultOfDestinyEntitySearchResultItem(BaseModel):
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

    results: list["DestinyEntitySearchResultItem"] = attr.field()
    total_results: int = attr.field()
    has_more: bool = attr.field()
    query: "PagedQuery" = attr.field()
    replacement_continuation_token: str = attr.field()
    use_total_results: bool = attr.field()


@attr.define
class SearchResultOfTrendingEntry(BaseModel):
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

    results: list["TrendingEntry"] = attr.field()
    total_results: int = attr.field()
    has_more: bool = attr.field()
    query: "PagedQuery" = attr.field()
    replacement_continuation_token: str = attr.field()
    use_total_results: bool = attr.field()


@attr.define
class SearchResultOfFireteamSummary(BaseModel):
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

    results: list["FireteamSummary"] = attr.field()
    total_results: int = attr.field()
    has_more: bool = attr.field()
    query: "PagedQuery" = attr.field()
    replacement_continuation_token: str = attr.field()
    use_total_results: bool = attr.field()


@attr.define
class SearchResultOfFireteamResponse(BaseModel):
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

    results: list["FireteamResponse"] = attr.field()
    total_results: int = attr.field()
    has_more: bool = attr.field()
    query: "PagedQuery" = attr.field()
    replacement_continuation_token: str = attr.field()
    use_total_results: bool = attr.field()


@attr.define
class GlobalAlert(BaseModel):
    """
    Not specified.

    Attributes:
        alert_key: Not specified.
        alert_html: Not specified.
        alert_timestamp: Not specified.
        alert_link: Not specified.
        alert_level: Not specified.
        alert_type: Not specified.
        stream_info: Not specified.
    """

    alert_key: str = attr.field()
    alert_html: str = attr.field()
    alert_timestamp: datetime.datetime = attr.field()
    alert_link: str = attr.field()
    alert_level: int = attr.field()
    alert_type: int = attr.field()
    stream_info: "StreamInfo" = attr.field()


class GlobalAlertLevel(BaseEnum):
    """
    Not specified.
    """

    UNKNOWN = 0
    """Not specified. """
    BLUE = 1
    """Not specified. """
    YELLOW = 2
    """Not specified. """
    RED = 3
    """Not specified. """


class GlobalAlertType(BaseEnum):
    """
    Not specified.
    """

    GLOBAL_ALERT = 0
    """Not specified. """
    STREAMING_ALERT = 1
    """Not specified. """


@attr.define
class StreamInfo(BaseModel):
    """
    Not specified.

    Attributes:
        channel_name: Not specified.
    """

    channel_name: str = attr.field()
