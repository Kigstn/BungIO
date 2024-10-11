# DO NOT CHANGE ANY CODE BELOW
# This file is generated automatically by `generate_api_schema.py` and will be overwritten
# Instead, change functions / models by subclassing them in the `./overwrites/` folder. They will be used instead.

from datetime import datetime
from typing import TYPE_CHECKING, Union

from bungio.models.base import BaseModel, custom_define, custom_field
from bungio.models.mixins import DestinyUserMixin
from bungio.utils import enum_converter

if TYPE_CHECKING:
    from bungio.models import (
        BungieMembershipType,
        DestinyBaseItemComponentSetOfuint32,
        DestinyItemComponent,
        DestinyItemComponentSetOfint64,
        DestinyItemComponentSetOfuint32,
        DestinyPlatformSilverComponent,
        DestinyPublicVendorSaleItemComponent,
        DestinyVendorSaleItemComponent,
        DictionaryComponentResponseOfint32AndDestinyVendorSaleItemComponent,
        DictionaryComponentResponseOfint64AndDestinyCharacterActivitiesComponent,
        DictionaryComponentResponseOfint64AndDestinyCharacterComponent,
        DictionaryComponentResponseOfint64AndDestinyCharacterProgressionComponent,
        DictionaryComponentResponseOfint64AndDestinyCharacterRecordsComponent,
        DictionaryComponentResponseOfint64AndDestinyCharacterRenderComponent,
        DictionaryComponentResponseOfint64AndDestinyCollectiblesComponent,
        DictionaryComponentResponseOfint64AndDestinyCraftablesComponent,
        DictionaryComponentResponseOfint64AndDestinyCurrenciesComponent,
        DictionaryComponentResponseOfint64AndDestinyInventoryComponent,
        DictionaryComponentResponseOfint64AndDestinyKiosksComponent,
        DictionaryComponentResponseOfint64AndDestinyLoadoutsComponent,
        DictionaryComponentResponseOfint64AndDestinyPlugSetsComponent,
        DictionaryComponentResponseOfint64AndDestinyPresentationNodesComponent,
        DictionaryComponentResponseOfint64AndDestinyStringVariablesComponent,
        DictionaryComponentResponseOfuint32AndDestinyPublicVendorComponent,
        DictionaryComponentResponseOfuint32AndDestinyVendorCategoriesComponent,
        DictionaryComponentResponseOfuint32AndDestinyVendorComponent,
        DictionaryComponentResponseOfuint32AndPersonalDestinyVendorSaleItemSetComponent,
        DictionaryComponentResponseOfuint32AndPublicDestinyVendorSaleItemSetComponent,
        PlatformErrorCodes,
        SingleComponentResponseOfDestinyCharacterActivitiesComponent,
        SingleComponentResponseOfDestinyCharacterComponent,
        SingleComponentResponseOfDestinyCharacterProgressionComponent,
        SingleComponentResponseOfDestinyCharacterRecordsComponent,
        SingleComponentResponseOfDestinyCharacterRenderComponent,
        SingleComponentResponseOfDestinyCollectiblesComponent,
        SingleComponentResponseOfDestinyCurrenciesComponent,
        SingleComponentResponseOfDestinyInventoryComponent,
        SingleComponentResponseOfDestinyItemComponent,
        SingleComponentResponseOfDestinyItemInstanceComponent,
        SingleComponentResponseOfDestinyItemObjectivesComponent,
        SingleComponentResponseOfDestinyItemPerksComponent,
        SingleComponentResponseOfDestinyItemPlugObjectivesComponent,
        SingleComponentResponseOfDestinyItemRenderComponent,
        SingleComponentResponseOfDestinyItemReusablePlugsComponent,
        SingleComponentResponseOfDestinyItemSocketsComponent,
        SingleComponentResponseOfDestinyItemStatsComponent,
        SingleComponentResponseOfDestinyItemTalentGridComponent,
        SingleComponentResponseOfDestinyKiosksComponent,
        SingleComponentResponseOfDestinyLoadoutsComponent,
        SingleComponentResponseOfDestinyMetricsComponent,
        SingleComponentResponseOfDestinyPlatformSilverComponent,
        SingleComponentResponseOfDestinyPlugSetsComponent,
        SingleComponentResponseOfDestinyPresentationNodesComponent,
        SingleComponentResponseOfDestinyProfileCollectiblesComponent,
        SingleComponentResponseOfDestinyProfileComponent,
        SingleComponentResponseOfDestinyProfileProgressionComponent,
        SingleComponentResponseOfDestinyProfileRecordsComponent,
        SingleComponentResponseOfDestinyProfileTransitoryComponent,
        SingleComponentResponseOfDestinySocialCommendationsComponent,
        SingleComponentResponseOfDestinyStringVariablesComponent,
        SingleComponentResponseOfDestinyVendorCategoriesComponent,
        SingleComponentResponseOfDestinyVendorComponent,
        SingleComponentResponseOfDestinyVendorGroupComponent,
        SingleComponentResponseOfDestinyVendorReceiptsComponent,
        UserInfoCard,
    )


@custom_define()
class DestinyLinkedProfilesResponse(BaseModel):
    """
    I know what you seek. You seek linked accounts. Found them, you have. This contract returns a minimal amount of data about Destiny Accounts that are linked through your Bungie.Net account. We will not return accounts in this response whose

    None
    Attributes:
        bnet_membership: If the requested membership had a linked Bungie.Net membership ID, this is the basic information about that BNet account. I know, Tetron; I know this is mixing UserServices concerns with DestinyServices concerns. But it's so damn convenient! https://www.youtube.com/watch?v=X5R-bB-gKVI
        profiles: Any Destiny account for whom we could successfully pull characters will be returned here, as the Platform-level summary of user data. (no character data, no Destiny account data other than the Membership ID and Type so you can make further queries)
        profiles_with_errors: This is brief summary info for profiles that we believe have valid Destiny info, but who failed to return data for some other reason and thus we know that subsequent calls for their info will also fail.
    """

    bnet_membership: "UserInfoCard" = custom_field()
    profiles: list["DestinyProfileUserInfoCard"] = custom_field(
        metadata={"type": """list[DestinyProfileUserInfoCard]"""}
    )
    profiles_with_errors: list["DestinyErrorProfile"] = custom_field(metadata={"type": """list[DestinyErrorProfile]"""})


@custom_define()
class DestinyProfileUserInfoCard(BaseModel, DestinyUserMixin):
    """
    _No description given by bungie._

    None
    Attributes:
        applicable_membership_types: The list of Membership Types indicating the platforms on which this Membership can be used.  Not in Cross Save = its original membership type. Cross Save Primary = Any membership types it is overridding, and its original membership type Cross Save Overridden = Empty list
        bungie_global_display_name: The bungie global display name, if set.
        bungie_global_display_name_code: The bungie global display name code, if set.
        cross_save_override: If there is a cross save override in effect, this value will tell you the type that is overridding this one.
        date_last_played: _No description given by bungie._
        display_name: Display Name the player has chosen for themselves. The display name is optional when the data type is used as input to a platform API.
        icon_path: URL the Icon if available.
        is_cross_save_primary: If true, this account is hooked up as the "Primary" cross save account for one or more platforms.
        is_overridden: If this profile is being overridden/obscured by Cross Save, this will be set to true. We will still return the profile for display purposes where users need to know the info: it is up to any given area of the app/site to determine if this profile should still be shown.
        is_public: If True, this is a public user membership.
        membership_id: Membership ID as they user is known in the Accounts service
        membership_type: Type of the membership. Not necessarily the native type.
        platform_silver: This is the silver available on this Profile across any platforms on which they have purchased silver.  This is only available if you are requesting yourself.
        supplemental_display_name: A platform specific additional display name - ex: psn Real Name, bnet Unique Name, etc.
        unpaired_game_versions: If this profile is not in a cross save pairing, this will return the game versions that we believe this profile has access to.  For the time being, we will not return this information for any membership that is in a cross save pairing. The gist is that, once the pairing occurs, we do not currently have a consistent way to get that information for the profile's original Platform, and thus gameVersions would be too inconsistent (based on the last platform they happened to play on) for the info to be useful.  If we ever can get this data, this field will be deprecated and replaced with data on the DestinyLinkedProfileResponse itself, with game versions per linked Platform. But since we can't get that, we have this as a stop-gap measure for getting the data in the only situation that we currently need it.
    """

    applicable_membership_types: list[Union["BungieMembershipType", int]] = custom_field(
        converter=enum_converter("BungieMembershipType")
    )
    bungie_global_display_name: str = custom_field()
    bungie_global_display_name_code: int = custom_field()
    cross_save_override: Union["BungieMembershipType", int] = custom_field(
        converter=enum_converter("BungieMembershipType")
    )
    date_last_played: datetime = custom_field()
    display_name: str = custom_field()
    icon_path: str = custom_field()
    is_cross_save_primary: bool = custom_field()
    is_overridden: bool = custom_field()
    is_public: bool = custom_field()
    membership_id: int = custom_field(metadata={"int64": True})
    membership_type: Union["BungieMembershipType", int] = custom_field(converter=enum_converter("BungieMembershipType"))
    platform_silver: "DestinyPlatformSilverComponent" = custom_field()
    supplemental_display_name: str = custom_field()
    unpaired_game_versions: int = custom_field()


@custom_define()
class DestinyErrorProfile(BaseModel):
    """
    If a Destiny Profile can't be returned, but we're pretty certain it's a valid Destiny account, this will contain as much info as we can get about the profile for your use. Assume that the most you'll get is the Error Code, the Membership Type and the Membership ID.

    None
    Attributes:
        error_code: The error that we encountered. You should be able to look up localized text to show to the user for these failures.
        info_card: Basic info about the account that failed. Don't expect anything other than membership ID, Membership Type, and displayName to be populated.
    """

    error_code: Union["PlatformErrorCodes", int] = custom_field(converter=enum_converter("PlatformErrorCodes"))
    info_card: "UserInfoCard" = custom_field()


@custom_define()
class DestinyProfileResponse(BaseModel):
    """
    The response for GetDestinyProfile, with components for character and item-level data.

    None
    Attributes:
        character_activities: Character activity data - the activities available to this character and its status, keyed by the Character's Id. COMPONENT TYPE: CharacterActivities
        character_collectibles: COMPONENT TYPE: Collectibles
        character_craftables: COMPONENT TYPE: Craftables
        character_currency_lookups: A "lookup" convenience component that can be used to quickly check if the character has access to items that can be used for purchasing. COMPONENT TYPE: CurrencyLookups
        character_equipment: The character's equipped items, keyed by the Character's Id. COMPONENT TYPE: CharacterEquipment
        character_inventories: The character-level non-equipped inventory items, keyed by the Character's Id. COMPONENT TYPE: CharacterInventories
        character_kiosks: Items available from Kiosks that are available to a specific character as opposed to the account as a whole. It must be combined with data from the profileKiosks property to get a full picture of the character's available items to check out of a kiosk. This component returns information about what Kiosk items are available to you on a *Character* level. Usually, kiosk items will be earned for the entire Profile (all characters) at once. To find those, look in the profileKiosks property. COMPONENT TYPE: Kiosks
        character_loadouts: The character loadouts, keyed by the Character's Id. COMPONENT TYPE: CharacterLoadouts
        character_plug_sets: When sockets refer to reusable Plug Sets (see DestinyPlugSetDefinition for more info), this is the set of plugs and their states, per character, that are character-scoped. This comes back with ItemSockets, as it is needed for a complete picture of the sockets on requested items. COMPONENT TYPE: ItemSockets
        character_presentation_nodes: COMPONENT TYPE: PresentationNodes
        character_progressions: Character-level progression data, keyed by the Character's Id. COMPONENT TYPE: CharacterProgressions
        character_records: COMPONENT TYPE: Records
        character_render_data: Character rendering data - a minimal set of info needed to render a character in 3D - keyed by the Character's Id. COMPONENT TYPE: CharacterRenderData
        character_string_variables: COMPONENT TYPE: StringVariables
        character_uninstanced_item_components: Do you ever get the feeling that a system was designed *too* flexibly? That it can be used in so many different ways that you end up being unable to provide an easy to use abstraction for the mess that's happening under the surface? Let's talk about character-specific data that might be related to items without instances. These two statements are totally unrelated, I promise. At some point during D2, it was decided that items - such as Bounties - could be given to characters and *not* have instance data, but that *could* display and even use relevant state information on your account and character. Up to now, any item that had meaningful dependencies on character or account state had to be instanced, and thus "itemComponents" was all that you needed: it was keyed by item's instance IDs and provided the stateful information you needed inside. Unfortunately, we don't live in such a magical world anymore. This is information held on a per-character basis about non-instanced items that the characters have in their inventory - or that reference character-specific state information even if it's in Account-level inventory - and the values related to that item's state in relation to the given character. To give a concrete example, look at a Moments of Triumph bounty. They exist in a character's inventory, and show/care about a character's progression toward completing the bounty. But the bounty itself is a non-instanced item, like a mod or a currency. This returns that data for the characters who have the bounty in their inventory. I'm not crying, you're crying Okay we're both crying but it's going to be okay I promise Actually I shouldn't promise that, I don't know if it's going to be okay
        characters: Basic information about each character, keyed by the CharacterId. COMPONENT TYPE: Characters
        item_components: Information about instanced items across all returned characters, keyed by the item's instance ID. COMPONENT TYPE: [See inside the DestinyItemComponentSet contract for component types.]
        metrics: COMPONENT TYPE: Metrics
        platform_silver: Silver quantities for any platform on which this Profile plays destiny.  COMPONENT TYPE: PlatformSilver
        profile: The basic information about the Destiny Profile (formerly "Account"). COMPONENT TYPE: Profiles
        profile_collectibles: COMPONENT TYPE: Collectibles
        profile_commendations: COMPONENT TYPE: SocialCommendations
        profile_currencies: The profile-level currencies owned by the Destiny Profile. COMPONENT TYPE: ProfileCurrencies
        profile_inventory: The profile-level inventory of the Destiny Profile. COMPONENT TYPE: ProfileInventories
        profile_kiosks: Items available from Kiosks that are available Profile-wide (i.e. across all characters) This component returns information about what Kiosk items are available to you on a *Profile* level. It is theoretically possible for Kiosks to have items gated by specific Character as well. If you ever have those, you will find them on the characterKiosks property. COMPONENT TYPE: Kiosks
        profile_plug_sets: When sockets refer to reusable Plug Sets (see DestinyPlugSetDefinition for more info), this is the set of plugs and their states that are profile-scoped. This comes back with ItemSockets, as it is needed for a complete picture of the sockets on requested items. COMPONENT TYPE: ItemSockets
        profile_presentation_nodes: COMPONENT TYPE: PresentationNodes
        profile_progression: When we have progression information - such as Checklists - that may apply profile-wide, it will be returned here rather than in the per-character progression data. COMPONENT TYPE: ProfileProgression
        profile_records: COMPONENT TYPE: Records
        profile_string_variables: COMPONENT TYPE: StringVariables
        profile_transitory_data: COMPONENT TYPE: Transitory
        response_minted_timestamp: Records the timestamp of when most components were last generated from the world server source. Unless the component type is specified in the documentation for secondaryComponentsMintedTimestamp, this value is sufficient to do data freshness.
        secondary_components_minted_timestamp: Some secondary components are not tracked in the primary response timestamp and have their timestamp tracked here. If your component is any of the following, this field is where you will find your timestamp value:  PresentationNodes, Records, Collectibles, Metrics, StringVariables, Craftables, Transitory  All other component types may use the primary timestamp property.
        vendor_receipts: Recent, refundable purchases you have made from vendors. When will you use it? Couldn't say... COMPONENT TYPE: VendorReceipts
    """

    character_activities: "DictionaryComponentResponseOfint64AndDestinyCharacterActivitiesComponent" = custom_field()
    character_collectibles: "DictionaryComponentResponseOfint64AndDestinyCollectiblesComponent" = custom_field()
    character_craftables: "DictionaryComponentResponseOfint64AndDestinyCraftablesComponent" = custom_field()
    character_currency_lookups: "DictionaryComponentResponseOfint64AndDestinyCurrenciesComponent" = custom_field()
    character_equipment: "DictionaryComponentResponseOfint64AndDestinyInventoryComponent" = custom_field()
    character_inventories: "DictionaryComponentResponseOfint64AndDestinyInventoryComponent" = custom_field()
    character_kiosks: "DictionaryComponentResponseOfint64AndDestinyKiosksComponent" = custom_field()
    character_loadouts: "DictionaryComponentResponseOfint64AndDestinyLoadoutsComponent" = custom_field()
    character_plug_sets: "DictionaryComponentResponseOfint64AndDestinyPlugSetsComponent" = custom_field()
    character_presentation_nodes: "DictionaryComponentResponseOfint64AndDestinyPresentationNodesComponent" = (
        custom_field()
    )
    character_progressions: "DictionaryComponentResponseOfint64AndDestinyCharacterProgressionComponent" = custom_field()
    character_records: "DictionaryComponentResponseOfint64AndDestinyCharacterRecordsComponent" = custom_field()
    character_render_data: "DictionaryComponentResponseOfint64AndDestinyCharacterRenderComponent" = custom_field()
    character_string_variables: "DictionaryComponentResponseOfint64AndDestinyStringVariablesComponent" = custom_field()
    character_uninstanced_item_components: dict[int, "DestinyBaseItemComponentSetOfuint32"] = custom_field(
        metadata={"type": """dict[int, DestinyBaseItemComponentSetOfuint32]"""}
    )
    characters: "DictionaryComponentResponseOfint64AndDestinyCharacterComponent" = custom_field()
    item_components: "DestinyItemComponentSetOfint64" = custom_field()
    metrics: "SingleComponentResponseOfDestinyMetricsComponent" = custom_field()
    platform_silver: "SingleComponentResponseOfDestinyPlatformSilverComponent" = custom_field()
    profile: "SingleComponentResponseOfDestinyProfileComponent" = custom_field()
    profile_collectibles: "SingleComponentResponseOfDestinyProfileCollectiblesComponent" = custom_field()
    profile_commendations: "SingleComponentResponseOfDestinySocialCommendationsComponent" = custom_field()
    profile_currencies: "SingleComponentResponseOfDestinyInventoryComponent" = custom_field()
    profile_inventory: "SingleComponentResponseOfDestinyInventoryComponent" = custom_field()
    profile_kiosks: "SingleComponentResponseOfDestinyKiosksComponent" = custom_field()
    profile_plug_sets: "SingleComponentResponseOfDestinyPlugSetsComponent" = custom_field()
    profile_presentation_nodes: "SingleComponentResponseOfDestinyPresentationNodesComponent" = custom_field()
    profile_progression: "SingleComponentResponseOfDestinyProfileProgressionComponent" = custom_field()
    profile_records: "SingleComponentResponseOfDestinyProfileRecordsComponent" = custom_field()
    profile_string_variables: "SingleComponentResponseOfDestinyStringVariablesComponent" = custom_field()
    profile_transitory_data: "SingleComponentResponseOfDestinyProfileTransitoryComponent" = custom_field()
    response_minted_timestamp: datetime = custom_field()
    secondary_components_minted_timestamp: datetime = custom_field()
    vendor_receipts: "SingleComponentResponseOfDestinyVendorReceiptsComponent" = custom_field()


@custom_define()
class DestinyCharacterResponse(BaseModel):
    """
    The response contract for GetDestinyCharacter, with components that can be returned for character and item-level data.

    None
    Attributes:
        activities: Activity data - info about current activities available to the player. COMPONENT TYPE: CharacterActivities
        character: Base information about the character in question. COMPONENT TYPE: Characters
        collectibles: COMPONENT TYPE: Collectibles
        currency_lookups: A "lookup" convenience component that can be used to quickly check if the character has access to items that can be used for purchasing. COMPONENT TYPE: CurrencyLookups
        equipment: Equipped items on the character. COMPONENT TYPE: CharacterEquipment
        inventory: The character-level non-equipped inventory items. COMPONENT TYPE: CharacterInventories
        item_components: The set of components belonging to the player's instanced items. COMPONENT TYPE: [See inside the DestinyItemComponentSet contract for component types.]
        kiosks: Items available from Kiosks that are available to this specific character.  COMPONENT TYPE: Kiosks
        loadouts: The loadouts available to the character. COMPONENT TYPE: CharacterLoadouts
        plug_sets: When sockets refer to reusable Plug Sets (see DestinyPlugSetDefinition for more info), this is the set of plugs and their states that are scoped to this character. This comes back with ItemSockets, as it is needed for a complete picture of the sockets on requested items. COMPONENT TYPE: ItemSockets
        presentation_nodes: COMPONENT TYPE: PresentationNodes
        progressions: Character progression data, including Milestones. COMPONENT TYPE: CharacterProgressions
        records: COMPONENT TYPE: Records
        render_data: Character rendering data - a minimal set of information about equipment and dyes used for rendering. COMPONENT TYPE: CharacterRenderData
        uninstanced_item_components: The set of components belonging to the player's UNinstanced items. Because apparently now those too can have information relevant to the character's state. COMPONENT TYPE: [See inside the DestinyItemComponentSet contract for component types.]
    """

    activities: "SingleComponentResponseOfDestinyCharacterActivitiesComponent" = custom_field()
    character: "SingleComponentResponseOfDestinyCharacterComponent" = custom_field()
    collectibles: "SingleComponentResponseOfDestinyCollectiblesComponent" = custom_field()
    currency_lookups: "SingleComponentResponseOfDestinyCurrenciesComponent" = custom_field()
    equipment: "SingleComponentResponseOfDestinyInventoryComponent" = custom_field()
    inventory: "SingleComponentResponseOfDestinyInventoryComponent" = custom_field()
    item_components: "DestinyItemComponentSetOfint64" = custom_field()
    kiosks: "SingleComponentResponseOfDestinyKiosksComponent" = custom_field()
    loadouts: "SingleComponentResponseOfDestinyLoadoutsComponent" = custom_field()
    plug_sets: "SingleComponentResponseOfDestinyPlugSetsComponent" = custom_field()
    presentation_nodes: "SingleComponentResponseOfDestinyPresentationNodesComponent" = custom_field()
    progressions: "SingleComponentResponseOfDestinyCharacterProgressionComponent" = custom_field()
    records: "SingleComponentResponseOfDestinyCharacterRecordsComponent" = custom_field()
    render_data: "SingleComponentResponseOfDestinyCharacterRenderComponent" = custom_field()
    uninstanced_item_components: "DestinyBaseItemComponentSetOfuint32" = custom_field()


@custom_define()
class DestinyItemResponse(BaseModel):
    """
    The response object for retrieving an individual instanced item. None of these components are relevant for an item that doesn't have an "itemInstanceId": for those, get your information from the DestinyInventoryDefinition.

    None
    Attributes:
        character_id: If the item is on a character, this will return the ID of the character that is holding the item.
        instance: Basic instance data for the item. COMPONENT TYPE: ItemInstances
        item: Common data for the item relevant to its non-instanced properties. COMPONENT TYPE: ItemCommonData
        objectives: Information specifically about the item's objectives. COMPONENT TYPE: ItemObjectives
        perks: Information specifically about the perks currently active on the item. COMPONENT TYPE: ItemPerks
        plug_objectives: Information about objectives on Plugs for a given item. See the component's documentation for more info. COMPONENT TYPE: ItemPlugObjectives
        render_data: Information about how to render the item in 3D. COMPONENT TYPE: ItemRenderData
        reusable_plugs: Information about the Reusable Plugs for sockets on an item. These are plugs that you can insert into the given socket regardless of if you actually own an instance of that plug: they are logic-driven plugs rather than inventory-driven.  These may need to be combined with Plug Set component data to get a full picture of available plugs on a given socket.  COMPONENT TYPE: ItemReusablePlugs
        sockets: Information about the sockets of the item: which are currently active, what potential sockets you could have and the stats/abilities/perks you can gain from them. COMPONENT TYPE: ItemSockets
        stats: Information about the computed stats of the item: power, defense, etc... COMPONENT TYPE: ItemStats
        talent_grid: Information about the talent grid attached to the item. Talent nodes can provide a variety of benefits and abilities, and in Destiny 2 are used almost exclusively for the character's "Builds". COMPONENT TYPE: ItemTalentGrids
    """

    character_id: int = custom_field(metadata={"int64": True})
    instance: "SingleComponentResponseOfDestinyItemInstanceComponent" = custom_field()
    item: "SingleComponentResponseOfDestinyItemComponent" = custom_field()
    objectives: "SingleComponentResponseOfDestinyItemObjectivesComponent" = custom_field()
    perks: "SingleComponentResponseOfDestinyItemPerksComponent" = custom_field()
    plug_objectives: "SingleComponentResponseOfDestinyItemPlugObjectivesComponent" = custom_field()
    render_data: "SingleComponentResponseOfDestinyItemRenderComponent" = custom_field()
    reusable_plugs: "SingleComponentResponseOfDestinyItemReusablePlugsComponent" = custom_field()
    sockets: "SingleComponentResponseOfDestinyItemSocketsComponent" = custom_field()
    stats: "SingleComponentResponseOfDestinyItemStatsComponent" = custom_field()
    talent_grid: "SingleComponentResponseOfDestinyItemTalentGridComponent" = custom_field()


@custom_define()
class DestinyVendorsResponse(BaseModel):
    """
    A response containing all of the components for all requested vendors.

    None
    Attributes:
        categories: Categories that the vendor has available, and references to the sales therein. These are keyed by the Vendor Hash, so you will get one Categories Component per vendor returned. COMPONENT TYPE: VendorCategories
        currency_lookups: A "lookup" convenience component that can be used to quickly check if the character has access to items that can be used for purchasing. COMPONENT TYPE: CurrencyLookups
        item_components: The set of item detail components, one set of item components per Vendor. These are keyed by the Vendor Hash, so you will get one Item Component Set per vendor returned. The components contained inside are themselves keyed by the vendorSaleIndex, and will have whatever item-level components you requested (Sockets, Stats, Instance data etc...) per item being sold by the vendor.
        sales: Sales, keyed by the vendorItemIndex of the item being sold. These are keyed by the Vendor Hash, so you will get one Sale Item Set Component per vendor returned. Note that within the Sale Item Set component, the sales are themselves keyed by the vendorSaleIndex, so you can relate it to the current sale item definition within the Vendor's definition. COMPONENT TYPE: VendorSales
        string_variables: A map of string variable values by hash for this character context. COMPONENT TYPE: StringVariables
        vendor_groups: For Vendors being returned, this will give you the information you need to group them and order them in the same way that the Bungie Companion app performs grouping. It will automatically be returned if you request the Vendors component. COMPONENT TYPE: Vendors
        vendors: The base properties of the vendor. These are keyed by the Vendor Hash, so you will get one Vendor Component per vendor returned. COMPONENT TYPE: Vendors
    """

    categories: "DictionaryComponentResponseOfuint32AndDestinyVendorCategoriesComponent" = custom_field()
    currency_lookups: "SingleComponentResponseOfDestinyCurrenciesComponent" = custom_field()
    item_components: dict[int, dict] = custom_field(metadata={"type": """dict[int, dict]"""})
    sales: "DictionaryComponentResponseOfuint32AndPersonalDestinyVendorSaleItemSetComponent" = custom_field()
    string_variables: "SingleComponentResponseOfDestinyStringVariablesComponent" = custom_field()
    vendor_groups: "SingleComponentResponseOfDestinyVendorGroupComponent" = custom_field()
    vendors: "DictionaryComponentResponseOfuint32AndDestinyVendorComponent" = custom_field()


@custom_define()
class PersonalDestinyVendorSaleItemSetComponent(BaseModel):
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
class DestinyVendorResponse(BaseModel):
    """
    A response containing all of the components for a vendor.

    None
    Attributes:
        categories: Categories that the vendor has available, and references to the sales therein. COMPONENT TYPE: VendorCategories
        currency_lookups: A "lookup" convenience component that can be used to quickly check if the character has access to items that can be used for purchasing. COMPONENT TYPE: CurrencyLookups
        item_components: Item components, keyed by the vendorItemIndex of the active sale items. COMPONENT TYPE: [See inside the DestinyVendorItemComponentSet contract for component types.]
        sales: Sales, keyed by the vendorItemIndex of the item being sold. COMPONENT TYPE: VendorSales
        string_variables: A map of string variable values by hash for this character context. COMPONENT TYPE: StringVariables
        vendor: The base properties of the vendor. COMPONENT TYPE: Vendors
    """

    categories: "SingleComponentResponseOfDestinyVendorCategoriesComponent" = custom_field()
    currency_lookups: "SingleComponentResponseOfDestinyCurrenciesComponent" = custom_field()
    item_components: dict = custom_field(metadata={"type": """dict"""})
    sales: "DictionaryComponentResponseOfint32AndDestinyVendorSaleItemComponent" = custom_field()
    string_variables: "SingleComponentResponseOfDestinyStringVariablesComponent" = custom_field()
    vendor: "SingleComponentResponseOfDestinyVendorComponent" = custom_field()


@custom_define()
class DestinyPublicVendorsResponse(BaseModel):
    """
    A response containing all valid components for the public Vendors endpoint.  It is a decisively smaller subset of data compared to what we can get when we know the specific user making the request.  If you want any of the other data - item details, whether or not you can buy it, etc... you'll have to call in the context of a character. I know, sad but true.

    None
    Attributes:
        categories: Categories that the vendor has available, and references to the sales therein. These are keyed by the Vendor Hash, so you will get one Categories Component per vendor returned. COMPONENT TYPE: VendorCategories
        sales: Sales, keyed by the vendorItemIndex of the item being sold. These are keyed by the Vendor Hash, so you will get one Sale Item Set Component per vendor returned. Note that within the Sale Item Set component, the sales are themselves keyed by the vendorSaleIndex, so you can relate it to the corrent sale item definition within the Vendor's definition. COMPONENT TYPE: VendorSales
        string_variables: A set of string variable values by hash for a public vendors context. COMPONENT TYPE: StringVariables
        vendor_groups: For Vendors being returned, this will give you the information you need to group them and order them in the same way that the Bungie Companion app performs grouping. It will automatically be returned if you request the Vendors component. COMPONENT TYPE: Vendors
        vendors: The base properties of the vendor. These are keyed by the Vendor Hash, so you will get one Vendor Component per vendor returned. COMPONENT TYPE: Vendors
    """

    categories: "DictionaryComponentResponseOfuint32AndDestinyVendorCategoriesComponent" = custom_field()
    sales: "DictionaryComponentResponseOfuint32AndPublicDestinyVendorSaleItemSetComponent" = custom_field()
    string_variables: "SingleComponentResponseOfDestinyStringVariablesComponent" = custom_field()
    vendor_groups: "SingleComponentResponseOfDestinyVendorGroupComponent" = custom_field()
    vendors: "DictionaryComponentResponseOfuint32AndDestinyPublicVendorComponent" = custom_field()


@custom_define()
class PublicDestinyVendorSaleItemSetComponent(BaseModel):
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
class DestinyCollectibleNodeDetailResponse(BaseModel):
    """
    Returns the detailed information about a Collectible Presentation Node and any Collectibles that are direct descendants.

    None
    Attributes:
        collectible_item_components: Item components, keyed by the item hash of the items pointed at collectibles found under the requested Presentation Node. NOTE: I had a lot of hemming and hawing about whether these should be keyed by collectible hash or item hash... but ultimately having it be keyed by item hash meant that UI that already uses DestinyItemComponentSet data wouldn't have to have a special override to do the collectible -> item lookup once you delve into an item's details, and it also meant that you didn't have to remember that the Hash being used as the key for plugSets was different from the Hash being used for the other Dictionaries. As a result, using the Item Hash felt like the least crappy solution. We may all come to regret this decision. We will see. COMPONENT TYPE: [See inside the DestinyItemComponentSet contract for component types.]
        collectibles: COMPONENT TYPE: Collectibles
    """

    collectible_item_components: "DestinyItemComponentSetOfuint32" = custom_field()
    collectibles: "SingleComponentResponseOfDestinyCollectiblesComponent" = custom_field()


@custom_define()
class InventoryChangedResponse(BaseModel):
    """
    A response containing all of the components for all requested vendors.

    None
    Attributes:
        added_inventory_items: Items that appeared in the inventory possibly as a result of an action.
        removed_inventory_items: Items that disappeared from the inventory possibly as a result of an action.
    """

    added_inventory_items: list["DestinyItemComponent"] = custom_field(
        metadata={"type": """list[DestinyItemComponent]"""}
    )
    removed_inventory_items: list["DestinyItemComponent"] = custom_field(
        metadata={"type": """list[DestinyItemComponent]"""}
    )


@custom_define()
class DestinyItemChangeResponse(BaseModel):
    """
    _No description given by bungie._

    None
    Attributes:
        added_inventory_items: Items that appeared in the inventory possibly as a result of an action.
        item: _No description given by bungie._
        removed_inventory_items: Items that disappeared from the inventory possibly as a result of an action.
    """

    added_inventory_items: list["DestinyItemComponent"] = custom_field(
        metadata={"type": """list[DestinyItemComponent]"""}
    )
    item: "DestinyItemResponse" = custom_field()
    removed_inventory_items: list["DestinyItemComponent"] = custom_field(
        metadata={"type": """list[DestinyItemComponent]"""}
    )
