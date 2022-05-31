import datetime
from typing import TYPE_CHECKING, Any, Optional

import attr

from bungio.models.base import BaseEnum, BaseModel

if TYPE_CHECKING:
    from bungio.models import (
        DateRange,
        DestinyActivityChallengeDefinition,
        DestinyActivityGraphListEntryDefinition,
        DestinyActivityGuidedBlockDefinition,
        DestinyActivityInsertionPointDefinition,
        DestinyActivityLoadoutRequirement,
        DestinyActivityLoadoutRequirementSet,
        DestinyActivityMatchmakingBlockDefinition,
        DestinyActivityModifierReferenceDefinition,
        DestinyActivityPlaylistItemDefinition,
        DestinyActivityRewardDefinition,
        DestinyActivityUnlockStringDefinition,
        DestinyAnimationReference,
        DestinyArrangementRegionFilterDefinition,
        DestinyArtDyeReference,
        DestinyBubbleDefinition,
        DestinyColor,
        DestinyDerivedItemCategoryDefinition,
        DestinyDestinationBubbleSettingDefinition,
        DestinyDisplayCategoryDefinition,
        DestinyDisplayPropertiesDefinition,
        DestinyEnvironmentLocationMapping,
        DestinyEquippingBlockDefinition,
        DestinyFactionVendorDefinition,
        DestinyGearArtArrangementReference,
        DestinyIconSequenceDefinition,
        DestinyItemActionBlockDefinition,
        DestinyItemActionRequiredItemDefinition,
        DestinyItemCraftingBlockBonusPlugDefinition,
        DestinyItemCraftingBlockDefinition,
        DestinyItemCreationEntryLevelDefinition,
        DestinyItemGearsetBlockDefinition,
        DestinyItemIntrinsicSocketEntryDefinition,
        DestinyItemInventoryBlockDefinition,
        DestinyItemInvestmentStatDefinition,
        DestinyItemMetricBlockDefinition,
        DestinyItemObjectiveBlockDefinition,
        DestinyItemPerkEntryDefinition,
        DestinyItemPlugDefinition,
        DestinyItemPreviewBlockDefinition,
        DestinyItemQualityBlockDefinition,
        DestinyItemQuantity,
        DestinyItemSackBlockDefinition,
        DestinyItemSetBlockDefinition,
        DestinyItemSetBlockEntryDefinition,
        DestinyItemSocketBlockDefinition,
        DestinyItemSocketCategoryDefinition,
        DestinyItemSocketEntryDefinition,
        DestinyItemSocketEntryPlugItemDefinition,
        DestinyItemSourceBlockDefinition,
        DestinyItemSourceDefinition,
        DestinyItemStatBlockDefinition,
        DestinyItemSummaryBlockDefinition,
        DestinyItemTalentGridBlockDefinition,
        DestinyItemTooltipNotification,
        DestinyItemTranslationBlockDefinition,
        DestinyItemValueBlockDefinition,
        DestinyItemVendorSourceReference,
        DestinyItemVersionDefinition,
        DestinyLocationReleaseDefinition,
        DestinyMaterialRequirement,
        DestinyNodeActivationRequirement,
        DestinyNodeSocketReplaceResponse,
        DestinyNodeStepDefinition,
        DestinyObjectiveDisplayProperties,
        DestinyObjectivePerkEntryDefinition,
        DestinyObjectiveStatEntryDefinition,
        DestinyPlugItemCraftingRequirements,
        DestinyPlugItemCraftingUnlockRequirement,
        DestinyProgressionDisplayPropertiesDefinition,
        DestinyProgressionRewardDefinition,
        DestinyProgressionRewardItemQuantity,
        DestinyProgressionStepDefinition,
        DestinyStatDisplayDefinition,
        DestinyTalentNodeCategory,
        DestinyTalentNodeDefinition,
        DestinyTalentNodeExclusiveSetDefinition,
        DestinyTalentNodeStepGroups,
        DestinyVendorAcceptedItemDefinition,
        DestinyVendorActionDefinition,
        DestinyVendorCategoryEntryDefinition,
        DestinyVendorCategoryOverlayDefinition,
        DestinyVendorDisplayPropertiesDefinition,
        DestinyVendorGroupReference,
        DestinyVendorInteractionDefinition,
        DestinyVendorInteractionReplyDefinition,
        DestinyVendorInteractionSackEntryDefinition,
        DestinyVendorInventoryFlyoutBucketDefinition,
        DestinyVendorInventoryFlyoutDefinition,
        DestinyVendorItemDefinition,
        DestinyVendorItemQuantity,
        DestinyVendorItemSocketOverride,
        DestinyVendorLocationDefinition,
        DestinyVendorRequirementDisplayEntryDefinition,
        DestinyVendorSaleItemActionBlockDefinition,
        DestinyVendorServiceDefinition,
        DyeReference,
        HyperlinkReference,
        InterpolationPoint,
        SearchResultOfDestinyEntitySearchResultItem,
    )


@attr.define
class DestinyDefinition(BaseModel):
    """
    Provides common properties for destiny definitions.

    Attributes:
        hash: The unique identifier for this entity. Guaranteed to be unique for the type of entity, but not globally. When entities refer to each other in Destiny content, it is this hash that they are referring to.
        index: The index of the entity as it was found in the investment tables.
        redacted: If this is true, then there is an entity with this identifier/type combination, but BNet is not yet allowed to show it. Sorry!
    """

    hash: int = attr.field()
    index: int = attr.field()
    redacted: bool = attr.field()


@attr.define
class DestinyProgressionDefinition(BaseModel):
    """
    A "Progression" in Destiny is best explained by an example. A Character's "Level" is a progression: it has Experience that can be earned, levels that can be gained, and is evaluated and displayed at various points in the game. A Character's "Faction Reputation" is also a progression for much the same reason. Progression is used by a variety of systems, and the definition of a Progression will generally only be useful if combining with live data (such as a character's DestinyCharacterProgressionComponent.progressions property, which holds that character's live Progression states). Fundamentally, a Progression measures your "Level" by evaluating the thresholds in its Steps (one step per level, except for the last step which can be repeated indefinitely for "Levels" that have no ceiling) against the total earned "progression points"/experience. (for simplicity purposes, we will henceforth refer to earned progression points as experience, though it need not be a mechanic that in any way resembles Experience in a traditional sense). Earned experience is calculated in a variety of ways, determined by the Progression's scope. These go from looking up a stored value to performing exceedingly obtuse calculations. This is why we provide live data in DestinyCharacterProgressionComponent.progressions, so you don't have to worry about those.

    Attributes:
        display_properties: _No description given by bungie_
        scope: The "Scope" of the progression indicates the source of the progression's live data. See the DestinyProgressionScope enum for more info: but essentially, a Progression can either be backed by a stored value, or it can be a calculated derivative of other values.
        repeat_last_step: If this is True, then the progression doesn't have a maximum level.
        source: If there's a description of how to earn this progression in the local config, this will be that localized description.
        steps: Progressions are divided into Steps, which roughly equate to "Levels" in the traditional sense of a Progression. Notably, the last step can be repeated indefinitely if repeatLastStep is true, meaning that the calculation for your level is not as simple as comparing your current progress to the max progress of the steps.  These and more calculations are done for you if you grab live character progression data, such as in the DestinyCharacterProgressionComponent.
        visible: If true, the Progression is something worth showing to users. If false, BNet isn't going to show it. But that doesn't mean you can't. We're all friends here.
        faction_hash: If the value exists, this is the hash identifier for the Faction that owns this Progression. This is purely for convenience, if you're looking at a progression and want to know if and who it's related to in terms of Faction Reputation.
        color: The #RGB string value for the color related to this progression, if there is one.
        rank_icon: For progressions that have it, this is the rank icon we use in the Companion, displayed above the progressions' rank value.
        reward_items: _No description given by bungie_
        hash: The unique identifier for this entity. Guaranteed to be unique for the type of entity, but not globally. When entities refer to each other in Destiny content, it is this hash that they are referring to.
        index: The index of the entity as it was found in the investment tables.
        redacted: If this is true, then there is an entity with this identifier/type combination, but BNet is not yet allowed to show it. Sorry!
    """

    display_properties: "DestinyProgressionDisplayPropertiesDefinition" = attr.field()
    scope: int = attr.field()
    repeat_last_step: bool = attr.field()
    source: str = attr.field()
    steps: list["DestinyProgressionStepDefinition"] = attr.field()
    visible: bool = attr.field()
    faction_hash: int = attr.field()
    color: "DestinyColor" = attr.field()
    rank_icon: str = attr.field()
    reward_items: list["DestinyProgressionRewardItemQuantity"] = attr.field()
    hash: int = attr.field()
    index: int = attr.field()
    redacted: bool = attr.field()


@attr.define
class DestinyProgressionDisplayPropertiesDefinition(BaseModel):
    """
    _No description given by bungie_

    Attributes:
        display_units_name: When progressions show your "experience" gained, that bar has units (i.e. "Experience", "Bad Dudes Snuffed Out", whatever). This is the localized string for that unit of measurement.
        description: _No description given by bungie_
        name: _No description given by bungie_
        icon: Note that "icon" is sometimes misleading, and should be interpreted in the context of the entity. For instance, in Destiny 1 the DestinyRecordBookDefinition's icon was a big picture of a book. But usually, it will be a small square image that you can use as... well, an icon. They are currently represented as 96px x 96px images.
        icon_sequences: _No description given by bungie_
        high_res_icon: If this item has a high-res icon (at least for now, many things won't), then the path to that icon will be here.
        has_icon: _No description given by bungie_
    """

    display_units_name: str = attr.field()
    description: str = attr.field()
    name: str = attr.field()
    icon: str = attr.field()
    icon_sequences: list["DestinyIconSequenceDefinition"] = attr.field()
    high_res_icon: str = attr.field()
    has_icon: bool = attr.field()


@attr.define
class DestinyProgressionStepDefinition(BaseModel):
    """
    This defines a single Step in a progression (which roughly equates to a level. See DestinyProgressionDefinition for caveats).

    Attributes:
        step_name: Very rarely, Progressions will have localized text describing the Level of the progression. This will be that localized text, if it exists. Otherwise, the standard appears to be to simply show the level numerically.
        display_effect_type: This appears to be, when you "level up", whether a visual effect will display and on what entity. See DestinyProgressionStepDisplayEffect for slightly more info.
        progress_total: The total amount of progression points/"experience" you will need to initially reach this step. If this is the last step and the progression is repeating indefinitely (DestinyProgressionDefinition.repeatLastStep), this will also be the progress needed to level it up further by repeating this step again.
        reward_items: A listing of items rewarded as a result of reaching this level.
        icon: If this progression step has a specific icon related to it, this is the icon to show.
    """

    step_name: str = attr.field()
    display_effect_type: int = attr.field()
    progress_total: int = attr.field()
    reward_items: list["DestinyItemQuantity"] = attr.field()
    icon: str = attr.field()


@attr.define
class DestinyInventoryItemDefinition(BaseModel):
    """
    So much of what you see in Destiny is actually an Item used in a new and creative way. This is the definition for Items in Destiny, which started off as just entities that could exist in your Inventory but ended up being the backing data for so much more: quests, reward previews, slots, and subclasses. In practice, you will want to associate this data with "live" item data from a Bungie.Net Platform call: these definitions describe the item in generic, non-instanced terms: but an actual instance of an item can vary widely from these generic definitions.

    Attributes:
        display_properties: _No description given by bungie_
        tooltip_notifications: Tooltips that only come up conditionally for the item. Check the live data DestinyItemComponent.tooltipNotificationIndexes property for which of these should be shown at runtime.
        collectible_hash: If this item has a collectible related to it, this is the hash identifier of that collectible entry.
        icon_watermark: If available, this is the original 'active' release watermark overlay for the icon. If the item has different versions, this can be overridden by the 'display version watermark icon' from the 'quality' block. Alternatively, if there is no watermark for the version, and the item version has a power cap below the current season power cap, this can be overridden by the iconWatermarkShelved property.
        icon_watermark_shelved: If available, this is the 'shelved' release watermark overlay for the icon. If the item version has a power cap below the current season power cap, it can be treated as 'shelved', and should be shown with this 'shelved' watermark overlay.
        secondary_icon: A secondary icon associated with the item. Currently this is used in very context specific applications, such as Emblem Nameplates.
        secondary_overlay: Pulled from the secondary icon, this is the "secondary background" of the secondary icon. Confusing? Sure, that's why I call it "overlay" here: because as far as it's been used thus far, it has been for an optional overlay image. We'll see if that holds up, but at least for now it explains what this image is a bit better.
        secondary_special: Pulled from the Secondary Icon, this is the "special" background for the item. For Emblems, this is the background image used on the Details view: but it need not be limited to that for other types of items.
        background_color: Sometimes, an item will have a background color. Most notably this occurs with Emblems, who use the Background Color for small character nameplates such as the "friends" view you see in-game. There are almost certainly other items that have background color as well, though I have not bothered to investigate what items have it nor what purposes they serve: use it as you will.
        screenshot: If we were able to acquire an in-game screenshot for the item, the path to that screenshot will be returned here. Note that not all items have screenshots: particularly not any non-equippable items.
        item_type_display_name: The localized title/name of the item's type. This can be whatever the designers want, and has no guarantee of consistency between items.
        flavor_text: _No description given by bungie_
        ui_item_display_style: A string identifier that the game's UI uses to determine how the item should be rendered in inventory screens and the like. This could really be anything - at the moment, we don't have the time to really breakdown and maintain all the possible strings this could be, partly because new ones could be added ad hoc. But if you want to use it to dictate your own UI, or look for items with a certain display style, go for it!
        item_type_and_tier_display_name: It became a common enough pattern in our UI to show Item Type and Tier combined into a single localized string that I'm just going to go ahead and start pre-creating these for items.
        display_source: In theory, it is a localized string telling you about how you can find the item. I really wish this was more consistent. Many times, it has nothing. Sometimes, it's instead a more narrative-forward description of the item. Which is cool, and I wish all properties had that data, but it should really be its own property.
        tooltip_style: An identifier that the game UI uses to determine what type of tooltip to show for the item. These have no corresponding definitions that BNet can link to: so it'll be up to you to interpret and display your UI differently according to these styles (or ignore it).
        action: If the item can be "used", this block will be non-null, and will have data related to the action performed when using the item. (Guess what? 99% of the time, this action is "dismantle". Shocker)
        crafting: Recipe items will have relevant crafting information available here.
        inventory: If this item can exist in an inventory, this block will be non-null. In practice, every item that currently exists has one of these blocks. But note that it is not necessarily guaranteed.
        set_data: If this item is a quest, this block will be non-null. In practice, I wish I had called this the Quest block, but at the time it wasn't clear to me whether it would end up being used for purposes other than quests. It will contain data about the steps in the quest, and mechanics we can use for displaying and tracking the quest.
        stats: If this item can have stats (such as a weapon, armor, or vehicle), this block will be non-null and populated with the stats found on the item.
        emblem_objective_hash: If the item is an emblem that has a special Objective attached to it - for instance, if the emblem tracks PVP Kills, or what-have-you. This is a bit different from, for example, the Vanguard Kill Tracker mod, which pipes data into the "art channel". When I get some time, I would like to standardize these so you can get at the values they expose without having to care about what they're being used for and how they are wired up, but for now here's the raw data.
        equipping_block: If this item can be equipped, this block will be non-null and will be populated with the conditions under which it can be equipped.
        translation_block: If this item can be rendered, this block will be non-null and will be populated with rendering information.
        preview: If this item can be Used or Acquired to gain other items (for instance, how Eververse Boxes can be consumed to get items from the box), this block will be non-null and will give summary information for the items that can be acquired.
        quality: If this item can have a level or stats, this block will be non-null and will be populated with default quality (item level, "quality", and infusion) data. See the block for more details, there's often less upfront information in D2 so you'll want to be aware of how you use quality and item level on the definition level now.
        value: The conceptual "Value" of an item, if any was defined. See the DestinyItemValueBlockDefinition for more details.
        source_data: If this item has a known source, this block will be non-null and populated with source information. Unfortunately, at this time we are not generating sources: that is some aggressively manual work which we didn't have time for, and I'm hoping to get back to at some point in the future.
        objectives: If this item has Objectives (extra tasks that can be accomplished related to the item... most frequently when the item is a Quest Step and the Objectives need to be completed to move on to the next Quest Step), this block will be non-null and the objectives defined herein.
        metrics: If this item has available metrics to be shown, this block will be non-null have the appropriate hashes defined.
        plug: If this item *is* a Plug, this will be non-null and the info defined herein. See DestinyItemPlugDefinition for more information.
        gearset: If this item has related items in a "Gear Set", this will be non-null and the relationships defined herein.
        sack: If this item is a "reward sack" that can be opened to provide other items, this will be non-null and the properties of the sack contained herein.
        sockets: If this item has any Sockets, this will be non-null and the individual sockets on the item will be defined herein.
        summary: Summary data about the item.
        talent_grid: If the item has a Talent Grid, this will be non-null and the properties of the grid defined herein. Note that, while many items still have talent grids, the only ones with meaningful Nodes still on them will be Subclass/"Build" items.
        investment_stats: If the item has stats, this block will be defined. It has the "raw" investment stats for the item. These investment stats don't take into account the ways that the items can spawn, nor do they take into account any Stat Group transformations. I have retained them for debugging purposes, but I do not know how useful people will find them.
        perks: If the item has any *intrinsic* Perks (Perks that it will provide regardless of Sockets, Talent Grid, and other transitory state), they will be defined here.
        lore_hash: If the item has any related Lore (DestinyLoreDefinition), this will be the hash identifier you can use to look up the lore definition.
        summary_item_hash: There are times when the game will show you a "summary/vague" version of an item - such as a description of its type represented as a DestinyInventoryItemDefinition - rather than display the item itself. This happens sometimes when summarizing possible rewards in a tooltip. This is the item displayed instead, if it exists.
        animations: If any animations were extracted from game content for this item, these will be the definitions of those animations.
        allow_actions: BNet may forbid the execution of actions on this item via the API. If that is occurring, allowActions will be set to false.
        links: If we added any help or informational URLs about this item, these will be those links.
        does_postmaster_pull_have_side_effects: The boolean will indicate to us (and you!) whether something *could* happen when you transfer this item from the Postmaster that might be considered a "destructive" action. It is not feasible currently to tell you (or ourelves!) in a consistent way whether this *will* actually cause a destructive action, so we are playing it safe: if it has the potential to do so, we will not allow it to be transferred from the Postmaster by default. You will need to check for this flag before transferring an item from the Postmaster, or else you'll end up receiving an error.
        non_transferrable: The intrinsic transferability of an item. I hate that this boolean is negative - but there's a reason. Just because an item is intrinsically transferrable doesn't mean that it can be transferred, and we don't want to imply that this is the only source of that transferability.
        item_category_hashes: BNet attempts to make a more formal definition of item "Categories", as defined by DestinyItemCategoryDefinition. This is a list of all Categories that we were able to algorithmically determine that this item is a member of. (for instance, that it's a "Weapon", that it's an "Auto Rifle", etc...) The algorithm for these is, unfortunately, volatile. If you believe you see a miscategorized item, please let us know on the Bungie API forums.
        special_item_type: In Destiny 1, we identified some items as having particular categories that we'd like to know about for various internal logic purposes. These are defined in SpecialItemType, and while these days the itemCategoryHashes are the preferred way of identifying types, we have retained this enum for its convenience.
        item_type: A value indicating the "base" the of the item. This enum is a useful but dramatic oversimplification of what it means for an item to have a "Type". Still, it's handy in many situations. itemCategoryHashes are the preferred way of identifying types, we have retained this enum for its convenience.
        item_sub_type: A value indicating the "sub-type" of the item. For instance, where an item might have an itemType value "Weapon", this will be something more specific like "Auto Rifle". itemCategoryHashes are the preferred way of identifying types, we have retained this enum for its convenience.
        class_type: We run a similarly weak-sauce algorithm to try and determine whether an item is restricted to a specific class. If we find it to be restricted in such a way, we set this classType property to match the class' enumeration value so that users can easily identify class restricted items. If you see a mis-classed item, please inform the developers in the Bungie API forum.
        breaker_type: Some weapons and plugs can have a "Breaker Type": a special ability that works sort of like damage type vulnerabilities. This is (almost?) always set on items by plugs.
        breaker_type_hash: Since we also have a breaker type definition, this is the hash for that breaker type for your convenience. Whether you use the enum or hash and look up the definition depends on what's cleanest for your code.
        equippable: If true, then you will be allowed to equip the item if you pass its other requirements. This being false means that you cannot equip the item under any circumstances.
        damage_type_hashes: Theoretically, an item can have many possible damage types. In *practice*, this is not true, but just in case weapons start being made that have multiple (for instance, an item where a socket has reusable plugs for every possible damage type that you can choose from freely), this field will return all of the possible damage types that are available to the weapon by default.
        damage_types: This is the list of all damage types that we know ahead of time the item can take on. Unfortunately, this does not preclude the possibility of something funky happening to give the item a damage type that cannot be predicted beforehand: for example, if some designer decides to create arbitrary non-reusable plugs that cause damage type to change. This damage type prediction will only use the following to determine potential damage types: - Intrinsic perks - Talent Node perks - Known, reusable plugs for sockets
        default_damage_type: If the item has a damage type that could be considered to be default, it will be populated here. For various upsetting reasons, it's surprisingly cumbersome to figure this out. I hope you're happy.
        default_damage_type_hash: Similar to defaultDamageType, but represented as the hash identifier for a DestinyDamageTypeDefinition. I will likely regret leaving in the enumeration versions of these properties, but for now they're very convenient.
        season_hash: If this item is related directly to a Season of Destiny, this is the hash identifier for that season.
        is_wrapper: If true, this is a dummy vendor-wrapped item template. Items purchased from Eververse will be "wrapped" by one of these items so that we can safely provide refund capabilities before the item is "unwrapped".
        trait_ids: Traits are metadata tags applied to this item. For example: armor slot, weapon type, foundry, faction, etc. These IDs come from the game and don't map to any content, but should still be useful.
        trait_hashes: These are the corresponding trait definition hashes for the entries in traitIds.
        hash: The unique identifier for this entity. Guaranteed to be unique for the type of entity, but not globally. When entities refer to each other in Destiny content, it is this hash that they are referring to.
        index: The index of the entity as it was found in the investment tables.
        redacted: If this is true, then there is an entity with this identifier/type combination, but BNet is not yet allowed to show it. Sorry!
    """

    display_properties: "DestinyDisplayPropertiesDefinition" = attr.field()
    tooltip_notifications: list["DestinyItemTooltipNotification"] = attr.field()
    collectible_hash: int = attr.field()
    icon_watermark: str = attr.field()
    icon_watermark_shelved: str = attr.field()
    secondary_icon: str = attr.field()
    secondary_overlay: str = attr.field()
    secondary_special: str = attr.field()
    background_color: "DestinyColor" = attr.field()
    screenshot: str = attr.field()
    item_type_display_name: str = attr.field()
    flavor_text: str = attr.field()
    ui_item_display_style: str = attr.field()
    item_type_and_tier_display_name: str = attr.field()
    display_source: str = attr.field()
    tooltip_style: str = attr.field()
    action: "DestinyItemActionBlockDefinition" = attr.field()
    crafting: "DestinyItemCraftingBlockDefinition" = attr.field()
    inventory: "DestinyItemInventoryBlockDefinition" = attr.field()
    set_data: "DestinyItemSetBlockDefinition" = attr.field()
    stats: "DestinyItemStatBlockDefinition" = attr.field()
    emblem_objective_hash: int = attr.field()
    equipping_block: "DestinyEquippingBlockDefinition" = attr.field()
    translation_block: "DestinyItemTranslationBlockDefinition" = attr.field()
    preview: "DestinyItemPreviewBlockDefinition" = attr.field()
    quality: "DestinyItemQualityBlockDefinition" = attr.field()
    value: "DestinyItemValueBlockDefinition" = attr.field()
    source_data: "DestinyItemSourceBlockDefinition" = attr.field()
    objectives: "DestinyItemObjectiveBlockDefinition" = attr.field()
    metrics: "DestinyItemMetricBlockDefinition" = attr.field()
    plug: "DestinyItemPlugDefinition" = attr.field()
    gearset: "DestinyItemGearsetBlockDefinition" = attr.field()
    sack: "DestinyItemSackBlockDefinition" = attr.field()
    sockets: "DestinyItemSocketBlockDefinition" = attr.field()
    summary: "DestinyItemSummaryBlockDefinition" = attr.field()
    talent_grid: "DestinyItemTalentGridBlockDefinition" = attr.field()
    investment_stats: list["DestinyItemInvestmentStatDefinition"] = attr.field()
    perks: list["DestinyItemPerkEntryDefinition"] = attr.field()
    lore_hash: int = attr.field()
    summary_item_hash: int = attr.field()
    animations: list["DestinyAnimationReference"] = attr.field()
    allow_actions: bool = attr.field()
    links: list["HyperlinkReference"] = attr.field()
    does_postmaster_pull_have_side_effects: bool = attr.field()
    non_transferrable: bool = attr.field()
    item_category_hashes: list[int] = attr.field()
    special_item_type: int = attr.field()
    item_type: int = attr.field()
    item_sub_type: int = attr.field()
    class_type: int = attr.field()
    breaker_type: int = attr.field()
    breaker_type_hash: int = attr.field()
    equippable: bool = attr.field()
    damage_type_hashes: list[int] = attr.field()
    damage_types: list[int] = attr.field()
    default_damage_type: int = attr.field()
    default_damage_type_hash: int = attr.field()
    season_hash: int = attr.field()
    is_wrapper: bool = attr.field()
    trait_ids: list[str] = attr.field()
    trait_hashes: list[int] = attr.field()
    hash: int = attr.field()
    index: int = attr.field()
    redacted: bool = attr.field()


@attr.define
class DestinyItemTooltipNotification(BaseModel):
    """
    _No description given by bungie_

    Attributes:
        display_string: _No description given by bungie_
        display_style: _No description given by bungie_
    """

    display_string: str = attr.field()
    display_style: str = attr.field()


@attr.define
class DestinyItemActionBlockDefinition(BaseModel):
    """
    If an item can have an action performed on it (like "Dismantle"), it will be defined here if you care.

    Attributes:
        verb_name: Localized text for the verb of the action being performed.
        verb_description: Localized text describing the action being performed.
        is_positive: The content has this property, however it's not entirely clear how it is used.
        overlay_screen_name: If the action has an overlay screen associated with it, this is the name of that screen. Unfortunately, we cannot return the screen's data itself.
        overlay_icon: The icon associated with the overlay screen for the action, if any.
        required_cooldown_seconds: The number of seconds to delay before allowing this action to be performed again.
        required_items: If the action requires other items to exist or be destroyed, this is the list of those items and requirements.
        progression_rewards: If performing this action earns you Progression, this is the list of progressions and values granted for those progressions by performing this action.
        action_type_label: The internal identifier for the action.
        required_location: Theoretically, an item could have a localized string for a hint about the location in which the action should be performed. In practice, no items yet have this property.
        required_cooldown_hash: The identifier hash for the Cooldown associated with this action. We have not pulled this data yet for you to have more data to use for cooldowns.
        delete_on_action: If true, the item is deleted when the action completes.
        consume_entire_stack: If true, the entire stack is deleted when the action completes.
        use_on_acquire: If true, this action will be performed as soon as you earn this item. Some rewards work this way, providing you a single item to pick up from a reward-granting vendor in-game and then immediately consuming itself to provide you multiple items.
    """

    verb_name: str = attr.field()
    verb_description: str = attr.field()
    is_positive: bool = attr.field()
    overlay_screen_name: str = attr.field()
    overlay_icon: str = attr.field()
    required_cooldown_seconds: int = attr.field()
    required_items: list["DestinyItemActionRequiredItemDefinition"] = attr.field()
    progression_rewards: list["DestinyProgressionRewardDefinition"] = attr.field()
    action_type_label: str = attr.field()
    required_location: str = attr.field()
    required_cooldown_hash: int = attr.field()
    delete_on_action: bool = attr.field()
    consume_entire_stack: bool = attr.field()
    use_on_acquire: bool = attr.field()


@attr.define
class DestinyItemActionRequiredItemDefinition(BaseModel):
    """
    The definition of an item and quantity required in a character's inventory in order to perform an action.

    Attributes:
        count: The minimum quantity of the item you have to have.
        item_hash: The hash identifier of the item you need to have. Use it to look up the DestinyInventoryItemDefinition for more info.
        delete_on_action: If true, the item/quantity will be deleted from your inventory when the action is performed. Otherwise, you'll retain these required items after the action is complete.
    """

    count: int = attr.field()
    item_hash: int = attr.field()
    delete_on_action: bool = attr.field()


@attr.define
class DestinyProgressionRewardDefinition(BaseModel):
    """
    Inventory Items can reward progression when actions are performed on them. A common example of this in Destiny 1 was Bounties, which would reward Experience on your Character and the like when you completed the bounty. Note that this maps to a DestinyProgressionMappingDefinition, and *not* a DestinyProgressionDefinition directly. This is apparently so that multiple progressions can be granted progression points/experience at the same time.

    Attributes:
        progression_mapping_hash: The hash identifier of the DestinyProgressionMappingDefinition that contains the progressions for which experience should be applied.
        amount: The amount of experience to give to each of the mapped progressions.
        apply_throttles: If true, the game's internal mechanisms to throttle progression should be applied.
    """

    progression_mapping_hash: int = attr.field()
    amount: int = attr.field()
    apply_throttles: bool = attr.field()


@attr.define
class DestinyProgressionMappingDefinition(BaseModel):
    """
    Aggregations of multiple progressions. These are used to apply rewards to multiple progressions at once. They can sometimes have human readable data as well, but only extremely sporadically.

    Attributes:
        display_properties: Infrequently defined in practice. Defer to the individual progressions' display properties.
        display_units: The localized unit of measurement for progression across the progressions defined in this mapping. Unfortunately, this is very infrequently defined. Defer to the individual progressions' display units.
        hash: The unique identifier for this entity. Guaranteed to be unique for the type of entity, but not globally. When entities refer to each other in Destiny content, it is this hash that they are referring to.
        index: The index of the entity as it was found in the investment tables.
        redacted: If this is true, then there is an entity with this identifier/type combination, but BNet is not yet allowed to show it. Sorry!
    """

    display_properties: "DestinyDisplayPropertiesDefinition" = attr.field()
    display_units: str = attr.field()
    hash: int = attr.field()
    index: int = attr.field()
    redacted: bool = attr.field()


@attr.define
class DestinyItemCraftingBlockDefinition(BaseModel):
    """
    If an item can have an action performed on it (like "Dismantle"), it will be defined here if you care.

    Attributes:
        output_item_hash: A reference to the item definition that is created when crafting with this 'recipe' item.
        required_socket_type_hashes: A list of socket type hashes that describes which sockets are required for crafting with this recipe.
        failed_requirement_strings: _No description given by bungie_
        base_material_requirements: A reference to the base material requirements for crafting with this recipe.
        bonus_plugs: A list of 'bonus' socket plugs that may be available if certain requirements are met.
    """

    output_item_hash: int = attr.field()
    required_socket_type_hashes: list[int] = attr.field()
    failed_requirement_strings: list[str] = attr.field()
    base_material_requirements: int = attr.field()
    bonus_plugs: list["DestinyItemCraftingBlockBonusPlugDefinition"] = attr.field()


@attr.define
class DestinyItemCraftingBlockBonusPlugDefinition(BaseModel):
    """
    _No description given by bungie_

    Attributes:
        socket_type_hash: _No description given by bungie_
        plug_item_hash: _No description given by bungie_
    """

    socket_type_hash: int = attr.field()
    plug_item_hash: int = attr.field()


@attr.define
class DestinyMaterialRequirementSetDefinition(BaseModel):
    """
    Represent a set of material requirements: Items that either need to be owned or need to be consumed in order to perform an action. A variety of other entities refer to these as gatekeepers and payments for actions that can be performed in game.

    Attributes:
        materials: The list of all materials that are required.
        hash: The unique identifier for this entity. Guaranteed to be unique for the type of entity, but not globally. When entities refer to each other in Destiny content, it is this hash that they are referring to.
        index: The index of the entity as it was found in the investment tables.
        redacted: If this is true, then there is an entity with this identifier/type combination, but BNet is not yet allowed to show it. Sorry!
    """

    materials: list["DestinyMaterialRequirement"] = attr.field()
    hash: int = attr.field()
    index: int = attr.field()
    redacted: bool = attr.field()


@attr.define
class DestinyMaterialRequirement(BaseModel):
    """
    Many actions relating to items require you to expend materials: - Activating a talent node - Inserting a plug into a socket The items will refer to material requirements by a materialRequirementsHash in these cases, and this is the definition for those requirements in terms of the item required, how much of it is required and other interesting info. This is one of the rare/strange times where a single contract class is used both in definitions *and* in live data response contracts. I'm not sure yet whether I regret that.

    Attributes:
        item_hash: The hash identifier of the material required. Use it to look up the material's DestinyInventoryItemDefinition.
        delete_on_action: If True, the material will be removed from the character's inventory when the action is performed.
        count: The amount of the material required.
        count_is_constant: If true, the material requirement count value is constant. Since The Witch Queen expansion, some material requirement counts can be dynamic and will need to be returned with an API call.
        omit_from_requirements: If True, this requirement is "silent": don't bother showing it in a material requirements display. I mean, I'm not your mom: I'm not going to tell you you *can't* show it. But we won't show it in our UI.
    """

    item_hash: int = attr.field()
    delete_on_action: bool = attr.field()
    count: int = attr.field()
    count_is_constant: bool = attr.field()
    omit_from_requirements: bool = attr.field()


@attr.define
class DestinyItemInventoryBlockDefinition(BaseModel):
    """
    If the item can exist in an inventory - the overwhelming majority of them can and do - then this is the basic properties regarding the item's relationship with the inventory.

    Attributes:
        stack_unique_label: If this string is populated, you can't have more than one stack with this label in a given inventory. Note that this is different from the equipping block's unique label, which is used for equipping uniqueness.
        max_stack_size: The maximum quantity of this item that can exist in a stack.
        bucket_type_hash: The hash identifier for the DestinyInventoryBucketDefinition to which this item belongs. I should have named this "bucketHash", but too many things refer to it now. Sigh.
        recovery_bucket_type_hash: If the item is picked up by the lost loot queue, this is the hash identifier for the DestinyInventoryBucketDefinition into which it will be placed. Again, I should have named this recoveryBucketHash instead.
        tier_type_hash: The hash identifier for the Tier Type of the item, use to look up its DestinyItemTierTypeDefinition if you need to show localized data for the item's tier.
        is_instance_item: If TRUE, this item is instanced. Otherwise, it is a generic item that merely has a quantity in a stack (like Glimmer).
        tier_type_name: The localized name of the tier type, which is a useful shortcut so you don't have to look up the definition every time. However, it's mostly a holdover from days before we had a DestinyItemTierTypeDefinition to refer to.
        tier_type: The enumeration matching the tier type of the item to known values, again for convenience sake.
        expiration_tooltip: The tooltip message to show, if any, when the item expires.
        expired_in_activity_message: If the item expires while playing in an activity, we show a different message.
        expired_in_orbit_message: If the item expires in orbit, we show a... more different message. ("Consummate V's, consummate!")
        suppress_expiration_when_objectives_complete: _No description given by bungie_
        recipe_item_hash: A reference to the associated crafting 'recipe' item definition, if this item can be crafted.
    """

    stack_unique_label: str = attr.field()
    max_stack_size: int = attr.field()
    bucket_type_hash: int = attr.field()
    recovery_bucket_type_hash: int = attr.field()
    tier_type_hash: int = attr.field()
    is_instance_item: bool = attr.field()
    tier_type_name: str = attr.field()
    tier_type: int = attr.field()
    expiration_tooltip: str = attr.field()
    expired_in_activity_message: str = attr.field()
    expired_in_orbit_message: str = attr.field()
    suppress_expiration_when_objectives_complete: bool = attr.field()
    recipe_item_hash: int = attr.field()


@attr.define
class DestinyInventoryBucketDefinition(BaseModel):
    """
    An Inventory (be it Character or Profile level) is comprised of many Buckets. An example of a bucket is "Primary Weapons", where all of the primary weapons on a character are gathered together into a single visual element in the UI: a subset of the inventory that has a limited number of slots, and in this case also has an associated Equipment Slot for equipping an item in the bucket. Item definitions declare what their "default" bucket is (DestinyInventoryItemDefinition.inventory.bucketTypeHash), and Item instances will tell you which bucket they are currently residing in (DestinyItemComponent.bucketHash). You can use this information along with the DestinyInventoryBucketDefinition to show these items grouped by bucket. You cannot transfer an item to a bucket that is not its Default without going through a Vendor's "accepted items" (DestinyVendorDefinition.acceptedItems). This is how transfer functionality like the Vault is implemented, as a feature of a Vendor. See the vendor's acceptedItems property for more details.

    Attributes:
        display_properties: _No description given by bungie_
        scope: Where the bucket is found. 0 = Character, 1 = Account
        category: An enum value for what items can be found in the bucket. See the BucketCategory enum for more details.
        bucket_order: Use this property to provide a quick-and-dirty recommended ordering for buckets in the UI. Most UIs will likely want to forsake this for something more custom and manual.
        item_count: The maximum # of item "slots" in a bucket. A slot is a given combination of item + quantity. For instance, a Weapon will always take up a single slot, and always have a quantity of 1. But a material could take up only a single slot with hundreds of quantity.
        location: Sometimes, inventory buckets represent conceptual "locations" in the game that might not be expected. This value indicates the conceptual location of the bucket, regardless of where it is actually contained on the character/account.  See ItemLocation for details.  Note that location includes the Vault and the Postmaster (both of whom being just inventory buckets with additional actions that can be performed on them through a Vendor)
        has_transfer_destination: If TRUE, there is at least one Vendor that can transfer items to/from this bucket. See the DestinyVendorDefinition's acceptedItems property for more information on how transferring works.
        enabled: If True, this bucket is enabled. Disabled buckets may include buckets that were included for test purposes, or that were going to be used but then were abandoned but never removed from content *cough*.
        fifo: if a FIFO bucket fills up, it will delete the oldest item from said bucket when a new item tries to be added to it. If this is FALSE, the bucket will not allow new items to be placed in it until room is made by the user manually deleting items from it. You can see an example of this with the Postmaster's bucket.
        hash: The unique identifier for this entity. Guaranteed to be unique for the type of entity, but not globally. When entities refer to each other in Destiny content, it is this hash that they are referring to.
        index: The index of the entity as it was found in the investment tables.
        redacted: If this is true, then there is an entity with this identifier/type combination, but BNet is not yet allowed to show it. Sorry!
    """

    display_properties: "DestinyDisplayPropertiesDefinition" = attr.field()
    scope: int = attr.field()
    category: int = attr.field()
    bucket_order: int = attr.field()
    item_count: int = attr.field()
    location: int = attr.field()
    has_transfer_destination: bool = attr.field()
    enabled: bool = attr.field()
    fifo: bool = attr.field()
    hash: int = attr.field()
    index: int = attr.field()
    redacted: bool = attr.field()


@attr.define
class DestinyItemSetBlockDefinition(BaseModel):
    """
    Primarily for Quests, this is the definition of properties related to the item if it is a quest and its various quest steps.

    Attributes:
        item_list: A collection of hashes of set items, for items such as Quest Metadata items that possess this data.
        require_ordered_set_item_add: If true, items in the set can only be added in increasing order, and adding an item will remove any previous item. For Quests, this is by necessity true. Only one quest step is present at a time, and previous steps are removed as you advance in the quest.
        set_is_featured: If true, the UI should treat this quest as "featured"
        set_type: A string identifier we can use to attempt to identify the category of the Quest.
        quest_line_name: The name of the quest line that this quest step is a part of.
        quest_line_description: The description of the quest line that this quest step is a part of.
        quest_step_summary: An additional summary of this step in the quest line.
    """

    item_list: list["DestinyItemSetBlockEntryDefinition"] = attr.field()
    require_ordered_set_item_add: bool = attr.field()
    set_is_featured: bool = attr.field()
    set_type: str = attr.field()
    quest_line_name: str = attr.field()
    quest_line_description: str = attr.field()
    quest_step_summary: str = attr.field()


@attr.define
class DestinyItemSetBlockEntryDefinition(BaseModel):
    """
    Defines a particular entry in an ItemSet (AKA a particular Quest Step in a Quest)

    Attributes:
        tracking_value: Used for tracking which step a user reached. These values will be populated in the user's internal state, which we expose externally as a more usable DestinyQuestStatus object. If this item has been obtained, this value will be set in trackingUnlockValueHash.
        item_hash: This is the hash identifier for a DestinyInventoryItemDefinition representing this quest step.
    """

    tracking_value: int = attr.field()
    item_hash: int = attr.field()


@attr.define
class DestinyItemStatBlockDefinition(BaseModel):
    """
    Information about the item's calculated stats, with as much data as we can find for the stats without having an actual instance of the item. Note that this means the entire concept of providing these stats is fundamentally insufficient: we cannot predict with 100% accuracy the conditions under which an item can spawn, so we use various heuristics to attempt to simulate the conditions as accurately as possible. Actual stats for items in-game can and will vary, but these should at least be useful base points for comparison and display. It is also worth noting that some stats, like Magazine size, have further calculations performed on them by scripts in-game and on the game servers that BNet does not have access to. We cannot know how those stats are further transformed, and thus some stats will be inaccurate even on instances of items in BNet vs. how they appear in-game. This is a known limitation of our item statistics, without any planned fix.

    Attributes:
        disable_primary_stat_display: If true, the game won't show the "primary" stat on this item when you inspect it. NOTE: This is being manually mapped, because I happen to want it in a block that isn't going to directly create this derivative block.
        stat_group_hash: If the item's stats are meant to be modified by a DestinyStatGroupDefinition, this will be the identifier for that definition. If you are using live data or precomputed stats data on the DestinyInventoryItemDefinition.stats.stats property, you don't have to worry about statGroupHash and how it alters stats: the already altered stats are provided to you. But if you want to see how the sausage gets made, or perform computations yourself, this is valuable information.
        stats: If you are looking for precomputed values for the stats on a weapon, this is where they are stored. Technically these are the "Display" stat values. Please see DestinyStatsDefinition for what Display Stat Values means, it's a very long story... but essentially these are the closest values BNet can get to the item stats that you see in-game. These stats are keyed by the DestinyStatDefinition's hash identifier for the stat that's found on the item.
        has_displayable_stats: A quick and lazy way to determine whether any stat other than the "primary" stat is actually visible on the item. Items often have stats that we return in case people find them useful, but they're not part of the "Stat Group" and thus we wouldn't display them in our UI. If this is False, then we're not going to display any of these stats other than the primary one.
        primary_base_stat_hash: This stat is determined to be the "primary" stat, and can be looked up in the stats or any other stat collection related to the item. Use this hash to look up the stat's value using DestinyInventoryItemDefinition.stats.stats, and the renderable data for the primary stat in the related DestinyStatDefinition.
    """

    disable_primary_stat_display: bool = attr.field()
    stat_group_hash: int = attr.field()
    stats: Any = attr.field()
    has_displayable_stats: bool = attr.field()
    primary_base_stat_hash: int = attr.field()


@attr.define
class DestinyInventoryItemStatDefinition(BaseModel):
    """
    Defines a specific stat value on an item, and the minimum/maximum range that we could compute for the item based on our heuristics for how the item might be generated. Not guaranteed to match real-world instances of the item, but should hopefully at least be close. If it's not close, let us know on the Bungie API forums.

    Attributes:
        stat_hash: The hash for the DestinyStatDefinition representing this stat.
        value: This value represents the stat value assuming the minimum possible roll but accounting for any mandatory bonuses that should be applied to the stat on item creation. In Destiny 1, this was different from the "minimum" value because there were certain conditions where an item could be theoretically lower level/value than the initial roll.  In Destiny 2, this is not possible unless Talent Grids begin to be used again for these purposes or some other system change occurs... thus in practice, value and minimum should be the same in Destiny 2. Good riddance.
        minimum: The minimum possible value for this stat that we think the item can roll.
        maximum: The maximum possible value for this stat that we think the item can roll. WARNING: In Destiny 1, this field was calculated using the potential stat rolls on the item's talent grid. In Destiny 2, items no longer have meaningful talent grids and instead have sockets: but the calculation of this field was never altered to adapt to this change. As such, this field should be considered deprecated until we can address this oversight.
        display_maximum: The maximum possible value for the stat as shown in the UI, if it is being shown somewhere that reveals maximum in the UI (such as a bar chart-style view). This is pulled directly from the item's DestinyStatGroupDefinition, and placed here for convenience. If not returned, there is no maximum to use (and thus the stat should not be shown in a way that assumes there is a limit to the stat)
    """

    stat_hash: int = attr.field()
    value: int = attr.field()
    minimum: int = attr.field()
    maximum: int = attr.field()
    display_maximum: int = attr.field()


@attr.define
class DestinyStatDefinition(BaseModel):
    """
    This represents a stat that's applied to a character or an item (such as a weapon, piece of armor, or a vehicle). An example of a stat might be Attack Power on a weapon. Stats go through a complex set of transformations before they end up being shown to the user as a number or a progress bar, and those transformations are fundamentally intertwined with the concept of a "Stat Group" (DestinyStatGroupDefinition). Items have both Stats and a reference to a Stat Group, and it is the Stat Group that takes the raw stat information and gives it both rendering metadata (such as whether to show it as a number or a progress bar) and the final transformation data (interpolation tables to turn the raw investment stat into a display stat). Please see DestinyStatGroupDefinition for more information on that transformational process. Stats are segregated from Stat Groups because different items and types of items can refer to the same stat, but have different "scales" for the stat while still having the same underlying value. For example, both a Shotgun and an Auto Rifle may have a "raw" impact stat of 50, but the Auto Rifle's Stat Group will scale that 50 down so that, when it is displayed, it is a smaller value relative to the shotgun. (this is a totally made up example, don't assume shotguns have naturally higher impact than auto rifles because of this) A final caveat is that some stats, even after this "final" transformation, go through yet another set of transformations directly in the game as a result of dynamic, stateful scripts that get run. BNet has no access to these scripts, nor any way to know which scripts get executed. As a result, the stats for an item that you see in-game - particularly for stats that are often impacted by Perks, like Magazine Size - can change dramatically from what we return on Bungie.Net. This is a known issue with no fix coming down the pipeline. Take these stats with a grain of salt. Stats actually go through four transformations, for those interested: 1) "Sandbox" stat, the "most raw" form. These are pretty much useless without transformations applied, and thus are not currently returned in the API. If you really want these, we can provide them. Maybe someone could do something cool with it? 2) "Investment" stat (the stat's value after DestinyStatDefinition's interpolation tables and aggregation logic is applied to the "Sandbox" stat value) 3) "Display" stat (the stat's base UI-visible value after DestinyStatGroupDefinition's interpolation tables are applied to the Investment Stat value. For most stats, this is what is displayed.) 4) Underlying in-game stat (the stat's actual value according to the game, after the game runs dynamic scripts based on the game and character's state. This is the final transformation that BNet does not have access to. For most stats, this is not actually displayed to the user, with the exception of Magazine Size which is then piped back to the UI for display in-game, but not to BNet.)

    Attributes:
        display_properties: _No description given by bungie_
        aggregation_type: Stats can exist on a character or an item, and they may potentially be aggregated in different ways. The DestinyStatAggregationType enum value indicates the way that this stat is being aggregated.
        has_computed_block: True if the stat is computed rather than being delivered as a raw value on items. For instance, the Light stat in Destiny 1 was a computed stat.
        stat_category: The category of the stat, according to the game.
        hash: The unique identifier for this entity. Guaranteed to be unique for the type of entity, but not globally. When entities refer to each other in Destiny content, it is this hash that they are referring to.
        index: The index of the entity as it was found in the investment tables.
        redacted: If this is true, then there is an entity with this identifier/type combination, but BNet is not yet allowed to show it. Sorry!
    """

    display_properties: "DestinyDisplayPropertiesDefinition" = attr.field()
    aggregation_type: int = attr.field()
    has_computed_block: bool = attr.field()
    stat_category: int = attr.field()
    hash: int = attr.field()
    index: int = attr.field()
    redacted: bool = attr.field()


@attr.define
class DestinyStatGroupDefinition(BaseModel):
    """
    When an inventory item (DestinyInventoryItemDefinition) has Stats (such as Attack Power), the item will refer to a Stat Group. This definition enumerates the properties used to transform the item's "Investment" stats into "Display" stats. See DestinyStatDefinition's documentation for information about the transformation of Stats, and the meaning of an Investment vs. a Display stat. If you don't want to do these calculations on your own, fear not: pulling live data from the BNet endpoints will return display stat values pre-computed and ready for you to use. I highly recommend this approach, saves a lot of time and also accounts for certain stat modifiers that can't easily be accounted for without live data (such as stat modifiers on Talent Grids and Socket Plugs)

    Attributes:
        maximum_value: The maximum possible value that any stat in this group can be transformed into. This is used by stats that *don't* have scaledStats entries below, but that still need to be displayed as a progress bar, in which case this is used as the upper bound for said progress bar. (the lower bound is always 0)
        ui_position: This apparently indicates the position of the stats in the UI? I've returned it in case anyone can use it, but it's not of any use to us on BNet. Something's being lost in translation with this value.
        scaled_stats: Any stat that requires scaling to be transformed from an "Investment" stat to a "Display" stat will have an entry in this list. For more information on what those types of stats mean and the transformation process, see DestinyStatDefinition. In retrospect, I wouldn't mind if this was a dictionary keyed by the stat hash instead. But I'm going to leave it be because [[After Apple Picking]].
        overrides: The game has the ability to override, based on the stat group, what the localized text is that is displayed for Stats being shown on the item. Mercifully, no Stat Groups use this feature currently. If they start using them, we'll all need to start using them (and those of you who are more prudent than I am can go ahead and start pre-checking for this.)
        hash: The unique identifier for this entity. Guaranteed to be unique for the type of entity, but not globally. When entities refer to each other in Destiny content, it is this hash that they are referring to.
        index: The index of the entity as it was found in the investment tables.
        redacted: If this is true, then there is an entity with this identifier/type combination, but BNet is not yet allowed to show it. Sorry!
    """

    maximum_value: int = attr.field()
    ui_position: int = attr.field()
    scaled_stats: list["DestinyStatDisplayDefinition"] = attr.field()
    overrides: Any = attr.field()
    hash: int = attr.field()
    index: int = attr.field()
    redacted: bool = attr.field()


@attr.define
class DestinyStatDisplayDefinition(BaseModel):
    """
    Describes the way that an Item Stat (see DestinyStatDefinition) is transformed using the DestinyStatGroupDefinition related to that item. See both of the aforementioned definitions for more information about the stages of stat transformation. This represents the transformation of a stat into a "Display" stat (the closest value that BNet can get to the in-game display value of the stat)

    Attributes:
        stat_hash: The hash identifier for the stat being transformed into a Display stat. Use it to look up the DestinyStatDefinition, or key into a DestinyInventoryItemDefinition's stats property.
        maximum_value: Regardless of the output of interpolation, this is the maximum possible value that the stat can be. It should also be used as the upper bound for displaying the stat as a progress bar (the minimum always being 0)
        display_as_numeric: If this is true, the stat should be displayed as a number. Otherwise, display it as a progress bar. Or, you know, do whatever you want. There's no displayAsNumeric police.
        display_interpolation: The interpolation table representing how the Investment Stat is transformed into a Display Stat.  See DestinyStatDefinition for a description of the stages of stat transformation.
    """

    stat_hash: int = attr.field()
    maximum_value: int = attr.field()
    display_as_numeric: bool = attr.field()
    display_interpolation: list["InterpolationPoint"] = attr.field()


@attr.define
class DestinyStatOverrideDefinition(BaseModel):
    """
    Stat Groups (DestinyStatGroupDefinition) has the ability to override the localized text associated with stats that are to be shown on the items with which they are associated. This defines a specific overridden stat. You could theoretically check these before rendering your stat UI, and for each stat that has an override show these displayProperties instead of those on the DestinyStatDefinition. Or you could be like us, and skip that for now because the game has yet to actually use this feature. But know that it's here, waiting for a resilliant young designer to take up the mantle and make us all look foolish by showing the wrong name for stats. Note that, if this gets used, the override will apply only to items using the overriding Stat Group. Other items will still show the default stat's name/description.

    Attributes:
        stat_hash: The hash identifier of the stat whose display properties are being overridden.
        display_properties: The display properties to show instead of the base DestinyStatDefinition display properties.
    """

    stat_hash: int = attr.field()
    display_properties: "DestinyDisplayPropertiesDefinition" = attr.field()


@attr.define
class DestinyEquippingBlockDefinition(BaseModel):
    """
    Items that can be equipped define this block. It contains information we need to understand how and when the item can be equipped.

    Attributes:
        gearset_item_hash: If the item is part of a gearset, this is a reference to that gearset item.
        unique_label: If defined, this is the label used to check if the item has other items of matching types already equipped.  For instance, when you aren't allowed to equip more than one Exotic Weapon, that's because all exotic weapons have identical uniqueLabels and the game checks the to-be-equipped item's uniqueLabel vs. all other already equipped items (other than the item in the slot that's about to be occupied).
        unique_label_hash: The hash of that unique label. Does not point to a specific definition.
        equipment_slot_type_hash: An equipped item *must* be equipped in an Equipment Slot. This is the hash identifier of the DestinyEquipmentSlotDefinition into which it must be equipped.
        attributes: These are custom attributes on the equippability of the item. For now, this can only be "equip on acquire", which would mean that the item will be automatically equipped as soon as you pick it up.
        ammo_type: Ammo type used by a weapon is no longer determined by the bucket in which it is contained. If the item has an ammo type - i.e. if it is a weapon - this will be the type of ammunition expected.
        display_strings: These are strings that represent the possible Game/Account/Character state failure conditions that can occur when trying to equip the item. They match up one-to-one with requiredUnlockExpressions.
    """

    gearset_item_hash: int = attr.field()
    unique_label: str = attr.field()
    unique_label_hash: int = attr.field()
    equipment_slot_type_hash: int = attr.field()
    attributes: int = attr.field()
    ammo_type: int = attr.field()
    display_strings: list[str] = attr.field()


@attr.define
class DestinyEquipmentSlotDefinition(BaseModel):
    """
    Characters can not only have Inventory buckets (containers of items that are generally matched by their type or functionality), they can also have Equipment Slots. The Equipment Slot is an indicator that the related bucket can have instanced items equipped on the character. For instance, the Primary Weapon bucket has an Equipment Slot that determines whether you can equip primary weapons, and holds the association between its slot and the inventory bucket from which it can have items equipped. An Equipment Slot must have a related Inventory Bucket, but not all inventory buckets must have Equipment Slots.

    Attributes:
        display_properties: _No description given by bungie_
        equipment_category_hash: These technically point to "Equipment Category Definitions". But don't get excited. There's nothing of significant value in those definitions, so I didn't bother to expose them. You can use the hash here to group equipment slots by common functionality, which serves the same purpose as if we had the Equipment Category definitions exposed.
        bucket_type_hash: The inventory bucket that owns this equipment slot.
        apply_custom_art_dyes: If True, equipped items should have their custom art dyes applied when rendering the item. Otherwise, custom art dyes on an item should be ignored if the item is equipped in this slot.
        art_dye_channels: The Art Dye Channels that apply to this equipment slot.
        hash: The unique identifier for this entity. Guaranteed to be unique for the type of entity, but not globally. When entities refer to each other in Destiny content, it is this hash that they are referring to.
        index: The index of the entity as it was found in the investment tables.
        redacted: If this is true, then there is an entity with this identifier/type combination, but BNet is not yet allowed to show it. Sorry!
    """

    display_properties: "DestinyDisplayPropertiesDefinition" = attr.field()
    equipment_category_hash: int = attr.field()
    bucket_type_hash: int = attr.field()
    apply_custom_art_dyes: bool = attr.field()
    art_dye_channels: list["DestinyArtDyeReference"] = attr.field()
    hash: int = attr.field()
    index: int = attr.field()
    redacted: bool = attr.field()


@attr.define
class DestinyArtDyeReference(BaseModel):
    """
    _No description given by bungie_

    Attributes:
        art_dye_channel_hash: _No description given by bungie_
    """

    art_dye_channel_hash: int = attr.field()


@attr.define
class DestinyItemTranslationBlockDefinition(BaseModel):
    """
    This Block defines the rendering data associated with the item, if any.

    Attributes:
        weapon_pattern_identifier: _No description given by bungie_
        weapon_pattern_hash: _No description given by bungie_
        default_dyes: _No description given by bungie_
        locked_dyes: _No description given by bungie_
        custom_dyes: _No description given by bungie_
        arrangements: _No description given by bungie_
        has_geometry: _No description given by bungie_
    """

    weapon_pattern_identifier: str = attr.field()
    weapon_pattern_hash: int = attr.field()
    default_dyes: list["DyeReference"] = attr.field()
    locked_dyes: list["DyeReference"] = attr.field()
    custom_dyes: list["DyeReference"] = attr.field()
    arrangements: list["DestinyGearArtArrangementReference"] = attr.field()
    has_geometry: bool = attr.field()


@attr.define
class DestinyGearArtArrangementReference(BaseModel):
    """
    _No description given by bungie_

    Attributes:
        class_hash: _No description given by bungie_
        art_arrangement_hash: _No description given by bungie_
    """

    class_hash: int = attr.field()
    art_arrangement_hash: int = attr.field()


@attr.define
class DestinyClassDefinition(BaseModel):
    """
    Defines a Character Class in Destiny 2. These are types of characters you can play, like Titan, Warlock, and Hunter.

    Attributes:
        class_type: In Destiny 1, we added a convenience Enumeration for referring to classes. We've kept it, though mostly for posterity. This is the enum value for this definition's class.
        display_properties: _No description given by bungie_
        gendered_class_names: A localized string referring to the singular form of the Class's name when referred to in gendered form. Keyed by the DestinyGender.
        gendered_class_names_by_gender_hash: _No description given by bungie_
        mentor_vendor_hash: Mentors don't really mean anything anymore. Don't expect this to be populated.
        hash: The unique identifier for this entity. Guaranteed to be unique for the type of entity, but not globally. When entities refer to each other in Destiny content, it is this hash that they are referring to.
        index: The index of the entity as it was found in the investment tables.
        redacted: If this is true, then there is an entity with this identifier/type combination, but BNet is not yet allowed to show it. Sorry!
    """

    class_type: int = attr.field()
    display_properties: "DestinyDisplayPropertiesDefinition" = attr.field()
    gendered_class_names: Any = attr.field()
    gendered_class_names_by_gender_hash: Any = attr.field()
    mentor_vendor_hash: int = attr.field()
    hash: int = attr.field()
    index: int = attr.field()
    redacted: bool = attr.field()


@attr.define
class DestinyGenderDefinition(BaseModel):
    """
    Gender is a social construct, and as such we have definitions for Genders. Right now there happens to only be two, but we'll see what the future holds.

    Attributes:
        gender_type: This is a quick reference enumeration for all of the currently defined Genders. We use the enumeration for quicker lookups in related data, like DestinyClassDefinition.genderedClassNames.
        display_properties: _No description given by bungie_
        hash: The unique identifier for this entity. Guaranteed to be unique for the type of entity, but not globally. When entities refer to each other in Destiny content, it is this hash that they are referring to.
        index: The index of the entity as it was found in the investment tables.
        redacted: If this is true, then there is an entity with this identifier/type combination, but BNet is not yet allowed to show it. Sorry!
    """

    gender_type: int = attr.field()
    display_properties: "DestinyDisplayPropertiesDefinition" = attr.field()
    hash: int = attr.field()
    index: int = attr.field()
    redacted: bool = attr.field()


@attr.define
class DestinyVendorDefinition(BaseModel):
    """
    These are the definitions for Vendors. In Destiny, a Vendor can be a lot of things - some things that you wouldn't expect, and some things that you don't even see directly in the game. Vendors are the Dolly Levi of the Destiny universe. - Traditional Vendors as you see in game: people who you come up to and who give you quests, rewards, or who you can buy things from. - Kiosks/Collections, which are really just Vendors that don't charge currency (or charge some pittance of a currency) and whose gating for purchases revolves more around your character's state. - Previews for rewards or the contents of sacks. These are implemented as Vendors, where you can't actually purchase from them but the items that they have for sale and the categories of sale items reflect the rewards or contents of the sack. This is so that the game could reuse the existing Vendor display UI for rewards and save a bunch of wheel reinvention. - Item Transfer capabilities, like the Vault and Postmaster. Vendors can have "acceptedItem" buckets that determine the source and destination buckets for transfers. When you interact with such a vendor, these buckets are what gets shown in the UI instead of any items that the Vendor would have for sale. Yep, the Vault is a vendor. It is pretty much guaranteed that they'll be used for even more features in the future. They have come to be seen more as generic categorized containers for items than "vendors" in a traditional sense, for better or worse. Where possible and time allows, we'll attempt to split those out into their own more digestible derived "Definitions": but often time does not allow that, as you can see from the above ways that vendors are used which we never split off from Vendor Definitions externally. Since Vendors are so many things to so many parts of the game, the definition is understandably complex. You will want to combine this data with live Vendor information from the API when it is available.

    Attributes:
        display_properties: _No description given by bungie_
        vendor_progression_type: The type of reward progression that this vendor has. Default - The original rank progression from token redemption. Ritual - Progression from ranks in ritual content. For example: Crucible (Shaxx), Gambit (Drifter), and Battlegrounds (War Table).
        buy_string: If the vendor has a custom localized string describing the "buy" action, that is returned here.
        sell_string: Ditto for selling. Not that you can sell items to a vendor anymore. Will it come back? Who knows. The string's still there.
        display_item_hash: If the vendor has an item that should be displayed as the "featured" item, this is the hash identifier for that DestinyVendorItemDefinition. Apparently this is usually a related currency, like a reputation token. But it need not be restricted to that.
        inhibit_buying: If this is true, you aren't allowed to buy whatever the vendor is selling.
        inhibit_selling: If this is true, you're not allowed to sell whatever the vendor is buying.
        faction_hash: If the Vendor has a faction, this hash will be valid and point to a DestinyFactionDefinition. The game UI and BNet often mine the faction definition for additional elements and details to place on the screen, such as the faction's Progression status (aka "Reputation").
        reset_interval_minutes: A number used for calculating the frequency of a vendor's inventory resetting/refreshing. Don't worry about calculating this - we do it on the server side and send you the next refresh date with the live data.
        reset_offset_minutes: Again, used for reset/refreshing of inventory. Don't worry too much about it. Unless you want to.
        failure_strings: If an item can't be purchased from the vendor, there may be many "custom"/game state specific reasons why not. This is a list of localized strings with messages for those custom failures. The live BNet data will return a failureIndexes property for items that can't be purchased: using those values to index into this array, you can show the user the appropriate failure message for the item that can't be bought.
        unlock_ranges: If we were able to predict the dates when this Vendor will be visible/available, this will be the list of those date ranges. Sadly, we're not able to predict this very frequently, so this will often be useless data.
        vendor_identifier: The internal identifier for the Vendor. A holdover from the old days of Vendors, but we don't have time to refactor it away.
        vendor_portrait: A portrait of the Vendor's smiling mug. Or frothing tentacles.
        vendor_banner: If the vendor has a custom banner image, that can be found here.
        enabled: If a vendor is not enabled, we won't even save the vendor's definition, and we won't return any items or info about them. It's as if they don't exist.
        visible: If a vendor is not visible, we still have and will give vendor definition info, but we won't use them for things like Advisors or UI.
        vendor_subcategory_identifier: The identifier of the VendorCategoryDefinition for this vendor's subcategory.
        consolidate_categories: If TRUE, consolidate categories that only differ by trivial properties (such as having minor differences in name)
        actions: Describes "actions" that can be performed on a vendor. Currently, none of these exist. But theoretically a Vendor could let you interact with it by performing actions. We'll see what these end up looking like if they ever get used.
        categories: These are the headers for sections of items that the vendor is selling. When you see items organized by category in the header, it is these categories that it is showing. Well, technically not *exactly* these. On BNet, it doesn't make sense to have categories be "paged" as we do in Destiny, so we run some heuristics to attempt to aggregate pages of categories together.  These are the categories post-concatenation, if the vendor had concatenation applied. If you want the pre-aggregated category data, use originalCategories.
        original_categories: See the categories property for a description of categories and why originalCategories exists.
        display_categories: Display Categories are different from "categories" in that these are specifically for visual grouping and display of categories in Vendor UI.  The "categories" structure is for validation of the contained items, and can be categorized entirely separately from "Display Categories", there need be and often will be no meaningful relationship between the two.
        interactions: In addition to selling items, vendors can have "interactions": UI where you "talk" with the vendor and they offer you a reward, some item, or merely acknowledge via dialog that you did something cool.
        inventory_flyouts: If the vendor shows you items from your own inventory - such as the Vault vendor does - this data describes the UI around showing those inventory buckets and which ones get shown.
        item_list: If the vendor sells items (or merely has a list of items to show like the "Sack" vendors do), this is the list of those items that the vendor can sell. From this list, only a subset will be available from the vendor at any given time, selected randomly and reset on the vendor's refresh interval. Note that a vendor can sell the same item multiple ways: for instance, nothing stops a vendor from selling you some specific weapon but using two different currencies, or the same weapon at multiple "item levels".
        services: BNet doesn't use this data yet, but it appears to be an optional list of flavor text about services that the Vendor can provide.
        accepted_items: If the Vendor is actually a vehicle for the transferring of items (like the Vault and Postmaster vendors), this defines the list of source->destination buckets for transferring.
        return_with_vendor_request: As many of you know, Vendor data has historically been pretty brutal on the BNet servers. In an effort to reduce this workload, only Vendors with this flag set will be returned on Vendor requests. This allows us to filter out Vendors that don't dynamic data that's particularly useful: things like "Preview/Sack" vendors, for example, that you can usually suss out the details for using just the definitions themselves.
        locations: A vendor can be at different places in the world depending on the game/character/account state. This is the list of possible locations for the vendor, along with conditions we use to determine which one is currently active.
        groups: A vendor can be a part of 0 or 1 "groups" at a time: a group being a collection of Vendors related by either location or function/purpose. It's used for our our Companion Vendor UI. Only one of these can be active for a Vendor at a time.
        ignore_sale_item_hashes: Some items don't make sense to return in the API, for example because they represent an action to be performed rather than an item being sold. I'd rather we not do this, but at least in the short term this is a workable workaround.
        hash: The unique identifier for this entity. Guaranteed to be unique for the type of entity, but not globally. When entities refer to each other in Destiny content, it is this hash that they are referring to.
        index: The index of the entity as it was found in the investment tables.
        redacted: If this is true, then there is an entity with this identifier/type combination, but BNet is not yet allowed to show it. Sorry!
    """

    display_properties: "DestinyVendorDisplayPropertiesDefinition" = attr.field()
    vendor_progression_type: int = attr.field()
    buy_string: str = attr.field()
    sell_string: str = attr.field()
    display_item_hash: int = attr.field()
    inhibit_buying: bool = attr.field()
    inhibit_selling: bool = attr.field()
    faction_hash: int = attr.field()
    reset_interval_minutes: int = attr.field()
    reset_offset_minutes: int = attr.field()
    failure_strings: list[str] = attr.field()
    unlock_ranges: list["DateRange"] = attr.field()
    vendor_identifier: str = attr.field()
    vendor_portrait: str = attr.field()
    vendor_banner: str = attr.field()
    enabled: bool = attr.field()
    visible: bool = attr.field()
    vendor_subcategory_identifier: str = attr.field()
    consolidate_categories: bool = attr.field()
    actions: list["DestinyVendorActionDefinition"] = attr.field()
    categories: list["DestinyVendorCategoryEntryDefinition"] = attr.field()
    original_categories: list["DestinyVendorCategoryEntryDefinition"] = attr.field()
    display_categories: list["DestinyDisplayCategoryDefinition"] = attr.field()
    interactions: list["DestinyVendorInteractionDefinition"] = attr.field()
    inventory_flyouts: list["DestinyVendorInventoryFlyoutDefinition"] = attr.field()
    item_list: list["DestinyVendorItemDefinition"] = attr.field()
    services: list["DestinyVendorServiceDefinition"] = attr.field()
    accepted_items: list["DestinyVendorAcceptedItemDefinition"] = attr.field()
    return_with_vendor_request: bool = attr.field()
    locations: list["DestinyVendorLocationDefinition"] = attr.field()
    groups: list["DestinyVendorGroupReference"] = attr.field()
    ignore_sale_item_hashes: list[int] = attr.field()
    hash: int = attr.field()
    index: int = attr.field()
    redacted: bool = attr.field()


@attr.define
class DestinyVendorDisplayPropertiesDefinition(BaseModel):
    """
    _No description given by bungie_

    Attributes:
        large_icon: I regret calling this a "large icon". It's more like a medium-sized image with a picture of the vendor's mug on it, trying their best to look cool. Not what one would call an icon.
        subtitle: _No description given by bungie_
        original_icon: If we replaced the icon with something more glitzy, this is the original icon that the vendor had according to the game's content. It may be more lame and/or have less razzle-dazzle. But who am I to tell you which icon to use.
        requirements_display: Vendors, in addition to expected display property data, may also show some "common requirements" as statically defined definition data. This might be when a vendor accepts a single type of currency, or when the currency is unique to the vendor and the designers wanted to show that currency when you interact with the vendor.
        small_transparent_icon: This is the icon used in parts of the game UI such as the vendor's waypoint.
        map_icon: This is the icon used in the map overview, when the vendor is located on the map.
        large_transparent_icon: This is apparently the "Watermark". I am not certain offhand where this is actually used in the Game UI, but some people may find it useful.
        description: _No description given by bungie_
        name: _No description given by bungie_
        icon: Note that "icon" is sometimes misleading, and should be interpreted in the context of the entity. For instance, in Destiny 1 the DestinyRecordBookDefinition's icon was a big picture of a book. But usually, it will be a small square image that you can use as... well, an icon. They are currently represented as 96px x 96px images.
        icon_sequences: _No description given by bungie_
        high_res_icon: If this item has a high-res icon (at least for now, many things won't), then the path to that icon will be here.
        has_icon: _No description given by bungie_
    """

    large_icon: str = attr.field()
    subtitle: str = attr.field()
    original_icon: str = attr.field()
    requirements_display: list["DestinyVendorRequirementDisplayEntryDefinition"] = attr.field()
    small_transparent_icon: str = attr.field()
    map_icon: str = attr.field()
    large_transparent_icon: str = attr.field()
    description: str = attr.field()
    name: str = attr.field()
    icon: str = attr.field()
    icon_sequences: list["DestinyIconSequenceDefinition"] = attr.field()
    high_res_icon: str = attr.field()
    has_icon: bool = attr.field()


@attr.define
class DestinyVendorRequirementDisplayEntryDefinition(BaseModel):
    """
    The localized properties of the requirementsDisplay, allowing information about the requirement or item being featured to be seen.

    Attributes:
        icon: _No description given by bungie_
        name: _No description given by bungie_
        source: _No description given by bungie_
        type: _No description given by bungie_
    """

    icon: str = attr.field()
    name: str = attr.field()
    source: str = attr.field()
    type: str = attr.field()


@attr.define
class DestinyVendorActionDefinition(BaseModel):
    """
    If a vendor can ever end up performing actions, these are the properties that will be related to those actions. I'm not going to bother documenting this yet, as it is unused and unclear if it will ever be used... but in case it is ever populated and someone finds it useful, it is defined here.

    Attributes:
        description: _No description given by bungie_
        execute_seconds: _No description given by bungie_
        icon: _No description given by bungie_
        name: _No description given by bungie_
        verb: _No description given by bungie_
        is_positive: _No description given by bungie_
        action_id: _No description given by bungie_
        action_hash: _No description given by bungie_
        auto_perform_action: _No description given by bungie_
    """

    description: str = attr.field()
    execute_seconds: int = attr.field()
    icon: str = attr.field()
    name: str = attr.field()
    verb: str = attr.field()
    is_positive: bool = attr.field()
    action_id: str = attr.field()
    action_hash: int = attr.field()
    auto_perform_action: bool = attr.field()


@attr.define
class DestinyVendorCategoryEntryDefinition(BaseModel):
    """
    This is the definition for a single Vendor Category, into which Sale Items are grouped.

    Attributes:
        category_index: The index of the category in the original category definitions for the vendor.
        sort_value: Used in sorting items in vendors... but there's a lot more to it. Just go with the order provided in the itemIndexes property on the DestinyVendorCategoryComponent instead, it should be more reliable than trying to recalculate it yourself.
        category_hash: The hashed identifier for the category.
        quantity_available: The amount of items that will be available when this category is shown.
        show_unavailable_items: If items aren't up for sale in this category, should we still show them (greyed out)?
        hide_if_no_currency: If you don't have the currency required to buy items from this category, should the items be hidden?
        hide_from_regular_purchase: True if this category doesn't allow purchases.
        buy_string_override: The localized string for making purchases from this category, if it is different from the vendor's string for purchasing.
        disabled_description: If the category is disabled, this is the localized description to show.
        display_title: The localized title of the category.
        overlay: If this category has an overlay prompt that should appear, this contains the details of that prompt.
        vendor_item_indexes: A shortcut for the vendor item indexes sold under this category. Saves us from some expensive reorganization at runtime.
        is_preview: Sometimes a category isn't actually used to sell items, but rather to preview them. This implies different UI (and manual placement of the category in the UI) in the game, and special treatment.
        is_display_only: If true, this category only displays items: you can't purchase anything in them.
        reset_interval_minutes_override: _No description given by bungie_
        reset_offset_minutes_override: _No description given by bungie_
    """

    category_index: int = attr.field()
    sort_value: int = attr.field()
    category_hash: int = attr.field()
    quantity_available: int = attr.field()
    show_unavailable_items: bool = attr.field()
    hide_if_no_currency: bool = attr.field()
    hide_from_regular_purchase: bool = attr.field()
    buy_string_override: str = attr.field()
    disabled_description: str = attr.field()
    display_title: str = attr.field()
    overlay: "DestinyVendorCategoryOverlayDefinition" = attr.field()
    vendor_item_indexes: list[int] = attr.field()
    is_preview: bool = attr.field()
    is_display_only: bool = attr.field()
    reset_interval_minutes_override: int = attr.field()
    reset_offset_minutes_override: int = attr.field()


@attr.define
class DestinyVendorCategoryOverlayDefinition(BaseModel):
    """
    The details of an overlay prompt to show to a user. They are all fairly self-explanatory localized strings that can be shown.

    Attributes:
        choice_description: _No description given by bungie_
        description: _No description given by bungie_
        icon: _No description given by bungie_
        title: _No description given by bungie_
        currency_item_hash: If this overlay has a currency item that it features, this is said featured item.
    """

    choice_description: str = attr.field()
    description: str = attr.field()
    icon: str = attr.field()
    title: str = attr.field()
    currency_item_hash: int = attr.field()


@attr.define
class DestinyDisplayCategoryDefinition(BaseModel):
    """
    Display Categories are different from "categories" in that these are specifically for visual grouping and display of categories in Vendor UI. The "categories" structure is for validation of the contained items, and can be categorized entirely separately from "Display Categories", there need be and often will be no meaningful relationship between the two.

    Attributes:
        index: _No description given by bungie_
        identifier: A string identifier for the display category.
        display_category_hash: _No description given by bungie_
        display_properties: _No description given by bungie_
        display_in_banner: If true, this category should be displayed in the "Banner" section of the vendor's UI.
        progression_hash: If it exists, this is the hash identifier of a DestinyProgressionDefinition that represents the progression to show on this display category. Specific categories can now have thier own distinct progression, apparently. So that's cool.
        sort_order: If this category sorts items in a nonstandard way, this will be the way we sort.
        display_style_hash: An indicator of how the category will be displayed in the UI. It's up to you to do something cool or interesting in response to this, or just to treat it as a normal category.
        display_style_identifier: An indicator of how the category will be displayed in the UI. It's up to you to do something cool or interesting in response to this, or just to treat it as a normal category.
    """

    index: int = attr.field()
    identifier: str = attr.field()
    display_category_hash: int = attr.field()
    display_properties: "DestinyDisplayPropertiesDefinition" = attr.field()
    display_in_banner: bool = attr.field()
    progression_hash: int = attr.field()
    sort_order: int = attr.field()
    display_style_hash: int = attr.field()
    display_style_identifier: str = attr.field()


@attr.define
class DestinyVendorInteractionDefinition(BaseModel):
    """
    A Vendor Interaction is a dialog shown by the vendor other than sale items or transfer screens. The vendor is showing you something, and asking you to reply to it by choosing an option or reward.

    Attributes:
        interaction_index: The position of this interaction in its parent array. Note that this is NOT content agnostic, and should not be used as such.
        replies: The potential replies that the user can make to the interaction.
        vendor_category_index: If >= 0, this is the category of sale items to show along with this interaction dialog.
        questline_item_hash: If this interaction dialog is about a quest, this is the questline related to the interaction. You can use this to show the quest overview, or even the character's status with the quest if you use it to find the character's current Quest Step by checking their inventory against this questlineItemHash's DestinyInventoryItemDefinition.setData.
        sack_interaction_list: If this interaction is meant to show you sacks, this is the list of types of sacks to be shown. If empty, the interaction is not meant to show sacks.
        ui_interaction_type: A UI hint for the behavior of the interaction screen. This is useful to determine what type of interaction is occurring, such as a prompt to receive a rank up reward or a prompt to choose a reward for completing a quest. The hash isn't as useful as the Enum in retrospect, well what can you do. Try using interactionType instead.
        interaction_type: The enumerated version of the possible UI hints for vendor interactions, which is a little easier to grok than the hash found in uiInteractionType.
        reward_block_label: If this interaction is displaying rewards, this is the text to use for the header of the reward-displaying section of the interaction.
        reward_vendor_category_index: If the vendor's reward list is sourced from one of his categories, this is the index into the category array of items to show.
        flavor_line_one: If the vendor interaction has flavor text, this is some of it.
        flavor_line_two: If the vendor interaction has flavor text, this is the rest of it.
        header_display_properties: The header for the interaction dialog.
        instructions: The localized text telling the player what to do when they see this dialog.
    """

    interaction_index: int = attr.field()
    replies: list["DestinyVendorInteractionReplyDefinition"] = attr.field()
    vendor_category_index: int = attr.field()
    questline_item_hash: int = attr.field()
    sack_interaction_list: list["DestinyVendorInteractionSackEntryDefinition"] = attr.field()
    ui_interaction_type: int = attr.field()
    interaction_type: int = attr.field()
    reward_block_label: str = attr.field()
    reward_vendor_category_index: int = attr.field()
    flavor_line_one: str = attr.field()
    flavor_line_two: str = attr.field()
    header_display_properties: "DestinyDisplayPropertiesDefinition" = attr.field()
    instructions: str = attr.field()


@attr.define
class DestinyVendorInteractionReplyDefinition(BaseModel):
    """
    When the interaction is replied to, Reward sites will fire and items potentially selected based on whether the given unlock expression is TRUE. You can potentially choose one from multiple replies when replying to an interaction: this is how you get either/or rewards from vendors.

    Attributes:
        item_rewards_selection: The rewards granted upon responding to the vendor.
        reply: The localized text for the reply.
        reply_type: An enum indicating the type of reply being made.
    """

    item_rewards_selection: int = attr.field()
    reply: str = attr.field()
    reply_type: int = attr.field()


@attr.define
class DestinyVendorInteractionSackEntryDefinition(BaseModel):
    """
    Compare this sackType to the sack identifier in the DestinyInventoryItemDefinition.vendorSackType property of items. If they match, show this sack with this interaction.

    Attributes:
        sack_type: _No description given by bungie_
    """

    sack_type: int = attr.field()


@attr.define
class DestinyVendorInventoryFlyoutDefinition(BaseModel):
    """
    The definition for an "inventory flyout": a UI screen where we show you part of an otherwise hidden vendor inventory: like the Vault inventory buckets.

    Attributes:
        locked_description: If the flyout is locked, this is the reason why.
        display_properties: The title and other common properties of the flyout.
        buckets: A list of inventory buckets and other metadata to show on the screen.
        flyout_id: An identifier for the flyout, in case anything else needs to refer to them.
        suppress_newness: If this is true, don't show any of the glistening "this is a new item" UI elements, like we show on the inventory items themselves in in-game UI.
        equipment_slot_hash: If this flyout is meant to show you the contents of the player's equipment slot, this is the slot to show.
    """

    locked_description: str = attr.field()
    display_properties: "DestinyDisplayPropertiesDefinition" = attr.field()
    buckets: list["DestinyVendorInventoryFlyoutBucketDefinition"] = attr.field()
    flyout_id: int = attr.field()
    suppress_newness: bool = attr.field()
    equipment_slot_hash: int = attr.field()


@attr.define
class DestinyVendorInventoryFlyoutBucketDefinition(BaseModel):
    """
    Information about a single inventory bucket in a vendor flyout UI and how it is shown.

    Attributes:
        collapsible: If true, the inventory bucket should be able to be collapsed visually.
        inventory_bucket_hash: The inventory bucket whose contents should be shown.
        sort_items_by: The methodology to use for sorting items from the flyout.
    """

    collapsible: bool = attr.field()
    inventory_bucket_hash: int = attr.field()
    sort_items_by: int = attr.field()


@attr.define
class DestinyVendorItemDefinition(BaseModel):
    """
    This represents an item being sold by the vendor.

    Attributes:
        vendor_item_index: The index into the DestinyVendorDefinition.saleList. This is what we use to refer to items being sold throughout live and definition data.
        item_hash: The hash identifier of the item being sold (DestinyInventoryItemDefinition). Note that a vendor can sell the same item in multiple ways, so don't assume that itemHash is a unique identifier for this entity.
        quantity: The amount you will recieve of the item described in itemHash if you make the purchase.
        failure_indexes: An list of indexes into the DestinyVendorDefinition.failureStrings array, indicating the possible failure strings that can be relevant for this item.
        currencies: This is a pre-compiled aggregation of item value and priceOverrideList, so that we have one place to check for what the purchaser must pay for the item. Use this instead of trying to piece together the price separately. The somewhat crappy part about this is that, now that item quantity overrides have dynamic modifiers, this will not necessarily be statically true. If you were using this instead of live data, switch to using live data.
        refund_policy: If this item can be refunded, this is the policy for what will be refundd, how, and in what time period.
        refund_time_limit: The amount of time before refundability of the newly purchased item will expire.
        creation_levels: The Default level at which the item will spawn. Almost always driven by an adjusto these days. Ideally should be singular. It's a long story how this ended up as a list, but there is always either going to be 0:1 of these entities.
        display_category_index: This is an index specifically into the display category, as opposed to the server-side Categories (which do not need to match or pair with each other in any way: server side categories are really just structures for common validation. Display Category will let us more easily categorize items visually)
        category_index: The index into the DestinyVendorDefinition.categories array, so you can find the category associated with this item.
        original_category_index: Same as above, but for the original category indexes.
        minimum_level: The minimum character level at which this item is available for sale.
        maximum_level: The maximum character level at which this item is available for sale.
        action: The action to be performed when purchasing the item, if it's not just "buy".
        display_category: The string identifier for the category selling this item.
        inventory_bucket_hash: The inventory bucket into which this item will be placed upon purchase.
        visibility_scope: The most restrictive scope that determines whether the item is available in the Vendor's inventory. See DestinyGatingScope's documentation for more information. This can be determined by Unlock gating, or by whether or not the item has purchase level requirements (minimumLevel and maximumLevel properties).
        purchasable_scope: Similar to visibilityScope, it represents the most restrictive scope that determines whether the item can be purchased. It will at least be as restrictive as visibilityScope, but could be more restrictive if the item has additional purchase requirements beyond whether it is merely visible or not. See DestinyGatingScope's documentation for more information.
        exclusivity: If this item can only be purchased by a given platform, this indicates the platform to which it is restricted.
        is_offer: If this sale can only be performed as the result of an offer check, this is true.
        is_crm: If this sale can only be performed as the result of receiving a CRM offer, this is true.
        sort_value: *if* the category this item is in supports non-default sorting, this value should represent the sorting value to use, pre-processed and ready to go.
        expiration_tooltip: If this item can expire, this is the tooltip message to show with its expiration info.
        redirect_to_sale_indexes: If this is populated, the purchase of this item should redirect to purchasing these other items instead.
        socket_overrides: _No description given by bungie_
        unpurchasable: If true, this item is some sort of dummy sale item that cannot actually be purchased. It may be a display only item, or some fluff left by a content designer for testing purposes, or something that got disabled because it was a terrible idea. You get the picture. We won't know *why* it can't be purchased, only that it can't be. Sorry. This is also only whether it's unpurchasable as a static property according to game content. There are other reasons why an item may or may not be purchasable at runtime, so even if this isn't set to True you should trust the runtime value for this sale item over the static definition if this is unset.
    """

    vendor_item_index: int = attr.field()
    item_hash: int = attr.field()
    quantity: int = attr.field()
    failure_indexes: list[int] = attr.field()
    currencies: list["DestinyVendorItemQuantity"] = attr.field()
    refund_policy: int = attr.field()
    refund_time_limit: int = attr.field()
    creation_levels: list["DestinyItemCreationEntryLevelDefinition"] = attr.field()
    display_category_index: int = attr.field()
    category_index: int = attr.field()
    original_category_index: int = attr.field()
    minimum_level: int = attr.field()
    maximum_level: int = attr.field()
    action: "DestinyVendorSaleItemActionBlockDefinition" = attr.field()
    display_category: str = attr.field()
    inventory_bucket_hash: int = attr.field()
    visibility_scope: int = attr.field()
    purchasable_scope: int = attr.field()
    exclusivity: int = attr.field()
    is_offer: bool = attr.field()
    is_crm: bool = attr.field()
    sort_value: int = attr.field()
    expiration_tooltip: str = attr.field()
    redirect_to_sale_indexes: list[int] = attr.field()
    socket_overrides: list["DestinyVendorItemSocketOverride"] = attr.field()
    unpurchasable: bool = attr.field()


@attr.define
class DestinyVendorItemQuantity(BaseModel):
    """
    In addition to item quantity information for vendor prices, this also has any optional information that may exist about how the item's quantity can be modified. (unfortunately not information that is able to be read outside of the BNet servers, but it's there)

    Attributes:
        item_hash: The hash identifier for the item in question. Use it to look up the item's DestinyInventoryItemDefinition.
        item_instance_id: If this quantity is referring to a specific instance of an item, this will have the item's instance ID. Normally, this will be null.
        quantity: The amount of the item needed/available depending on the context of where DestinyItemQuantity is being used.
        has_conditional_visibility: Indicates that this item quantity may be conditionally shown or hidden, based on various sources of state. For example: server flags, account state, or character progress.
    """

    item_hash: int = attr.field()
    item_instance_id: int = attr.field()
    quantity: int = attr.field()
    has_conditional_visibility: bool = attr.field()


@attr.define
class DestinyItemCreationEntryLevelDefinition(BaseModel):
    """
    An overly complicated wrapper for the item level at which the item should spawn.

    Attributes:
        level: _No description given by bungie_
    """

    level: int = attr.field()


@attr.define
class DestinyVendorSaleItemActionBlockDefinition(BaseModel):
    """
    Not terribly useful, some basic cooldown interaction info.

    Attributes:
        execute_seconds: _No description given by bungie_
        is_positive: _No description given by bungie_
    """

    execute_seconds: float = attr.field()
    is_positive: bool = attr.field()


@attr.define
class DestinyVendorItemSocketOverride(BaseModel):
    """
    The information for how the vendor purchase should override a given socket with custom plug data.

    Attributes:
        single_item_hash: If this is populated, the socket will be overridden with a specific plug. If this isn't populated, it's being overridden by something more complicated that is only known by the Game Server and God, which means we can't tell you in advance what it'll be.
        randomized_options_count: If this is greater than -1, the number of randomized plugs on this socket will be set to this quantity instead of whatever it's set to by default.
        socket_type_hash: This appears to be used to select which socket ultimately gets the override defined here.
    """

    single_item_hash: int = attr.field()
    randomized_options_count: int = attr.field()
    socket_type_hash: int = attr.field()


@attr.define
class DestinyVendorServiceDefinition(BaseModel):
    """
    When a vendor provides services, this is the localized name of those services.

    Attributes:
        name: The localized name of a service provided.
    """

    name: str = attr.field()


@attr.define
class DestinyVendorAcceptedItemDefinition(BaseModel):
    """
    If you ever wondered how the Vault works, here it is. The Vault is merely a set of inventory buckets that exist on your Profile/Account level. When you transfer items in the Vault, the game is using the Vault Vendor's DestinyVendorAcceptedItemDefinitions to see where the appropriate destination bucket is for the source bucket from whence your item is moving. If it finds such an entry, it transfers the item to the other bucket. The mechanics for Postmaster works similarly, which is also a vendor. All driven by Accepted Items.

    Attributes:
        accepted_inventory_bucket_hash: The "source" bucket for a transfer. When a user wants to transfer an item, the appropriate DestinyVendorDefinition's acceptedItems property is evaluated, looking for an entry where acceptedInventoryBucketHash matches the bucket that the item being transferred is currently located. If it exists, the item will be transferred into whatever bucket is defined by destinationInventoryBucketHash.
        destination_inventory_bucket_hash: This is the bucket where the item being transferred will be put, given that it was being transferred *from* the bucket defined in acceptedInventoryBucketHash.
    """

    accepted_inventory_bucket_hash: int = attr.field()
    destination_inventory_bucket_hash: int = attr.field()


@attr.define
class DestinyDestinationDefinition(BaseModel):
    """
    On to one of the more confusing subjects of the API. What is a Destination, and what is the relationship between it, Activities, Locations, and Places? A "Destination" is a specific region/city/area of a larger "Place". For instance, a Place might be Earth where a Destination might be Bellevue, Washington. (Please, pick a more interesting destination if you come to visit Earth).

    Attributes:
        display_properties: _No description given by bungie_
        place_hash: The place that "owns" this Destination. Use this hash to look up the DestinyPlaceDefinition.
        default_freeroam_activity_hash: If this Destination has a default Free-Roam activity, this is the hash for that Activity. Use it to look up the DestinyActivityDefintion.
        activity_graph_entries: If the Destination has default Activity Graphs (i.e. "Map") that should be shown in the director, this is the list of those Graphs. At most, only one should be active at any given time for a Destination: these would represent, for example, different variants on a Map if the Destination is changing on a macro level based on game state.
        bubble_settings: A Destination may have many "Bubbles" zones with human readable properties. We don't get as much info as I'd like about them - I'd love to return info like where on the map they are located - but at least this gives you the name of those bubbles. bubbleSettings and bubbles both have the identical number of entries, and you should match up their indexes to provide matching bubble and bubbleSettings data. DEPRECATED - Just use bubbles, it now has this data.
        bubbles: This provides the unique identifiers for every bubble in the destination (only guaranteed unique within the destination), and any intrinsic properties of the bubble. bubbleSettings and bubbles both have the identical number of entries, and you should match up their indexes to provide matching bubble and bubbleSettings data.
        hash: The unique identifier for this entity. Guaranteed to be unique for the type of entity, but not globally. When entities refer to each other in Destiny content, it is this hash that they are referring to.
        index: The index of the entity as it was found in the investment tables.
        redacted: If this is true, then there is an entity with this identifier/type combination, but BNet is not yet allowed to show it. Sorry!
    """

    display_properties: "DestinyDisplayPropertiesDefinition" = attr.field()
    place_hash: int = attr.field()
    default_freeroam_activity_hash: int = attr.field()
    activity_graph_entries: list["DestinyActivityGraphListEntryDefinition"] = attr.field()
    bubble_settings: list["DestinyDestinationBubbleSettingDefinition"] = attr.field()
    bubbles: list["DestinyBubbleDefinition"] = attr.field()
    hash: int = attr.field()
    index: int = attr.field()
    redacted: bool = attr.field()


@attr.define
class DestinyActivityGraphListEntryDefinition(BaseModel):
    """
    Destinations and Activities may have default Activity Graphs that should be shown when you bring up the Director and are playing in either. This contract defines the graph referred to and the gating for when it is relevant.

    Attributes:
        activity_graph_hash: The hash identifier of the DestinyActivityGraphDefinition that should be shown when opening the director.
    """

    activity_graph_hash: int = attr.field()


@attr.define
class DestinyActivityDefinition(BaseModel):
    """
    The static data about Activities in Destiny 2. Note that an Activity must be combined with an ActivityMode to know - from a Gameplay perspective - what the user is "Playing". In most PvE activities, this is fairly straightforward. A Story Activity can only be played in the Story Activity Mode. However, in PvP activities, the Activity alone only tells you the map being played, or the Playlist that the user chose to enter. You'll need to know the Activity Mode they're playing to know that they're playing Mode X on Map Y. Activity Definitions tell a great deal of information about what *could* be relevant to a user: what rewards they can earn, what challenges could be performed, what modifiers could be applied. To figure out which of these properties is actually live, you'll need to combine the definition with "Live" data from one of the Destiny endpoints. Activities also have Activity Types, but unfortunately in Destiny 2 these are even less reliable of a source of information than they were in Destiny 1. I will be looking into ways to provide more reliable sources for type information as time goes on, but for now we're going to have to deal with the limitations. See DestinyActivityTypeDefinition for more information.

    Attributes:
        display_properties: The title, subtitle, and icon for the activity. We do a little post-processing on this to try and account for Activities where the designers have left this data too minimal to determine what activity is actually being played.
        original_display_properties: The unadulterated form of the display properties, as they ought to be shown in the Director (if the activity appears in the director).
        selection_screen_display_properties: The title, subtitle, and icon for the activity as determined by Selection Screen data, if there is any for this activity. There won't be data in this field if the activity is never shown in a selection/options screen.
        release_icon: If the activity has an icon associated with a specific release (such as a DLC), this is the path to that release's icon.
        release_time: If the activity will not be visible until a specific and known time, this will be the seconds since the Epoch when it will become visible.
        activity_light_level: The recommended light level for this activity.
        destination_hash: The hash identifier for the Destination on which this Activity is played. Use it to look up the DestinyDestinationDefinition for human readable info about the destination. A Destination can be thought of as a more specific location than a "Place". For instance, if the "Place" is Earth, the "Destination" would be a specific city or region on Earth.
        place_hash: The hash identifier for the "Place" on which this Activity is played. Use it to look up the DestinyPlaceDefinition for human readable info about the Place. A Place is the largest-scoped concept for location information. For instance, if the "Place" is Earth, the "Destination" would be a specific city or region on Earth.
        activity_type_hash: The hash identifier for the Activity Type of this Activity. You may use it to look up the DestinyActivityTypeDefinition for human readable info, but be forewarned: Playlists and many PVP Map Activities will map to generic Activity Types. You'll have to use your knowledge of the Activity Mode being played to get more specific information about what the user is playing.
        tier: The difficulty tier of the activity.
        pgcr_image: When Activities are completed, we generate a "Post-Game Carnage Report", or PGCR, with details about what happened in that activity (how many kills someone got, which team won, etc...) We use this image as the background when displaying PGCR information, and often use it when we refer to the Activity in general.
        rewards: The expected possible rewards for the activity. These rewards may or may not be accessible for an individual player based on their character state, the account state, and even the game's state overall. But it is a useful reference for possible rewards you can earn in the activity. These match up to rewards displayed when you hover over the Activity in the in-game Director, and often refer to Placeholder or "Dummy" items: items that tell you what you can earn in vague terms rather than what you'll specifically be earning (partly because the game doesn't even know what you'll earn specifically until you roll for it at the end)
        modifiers: Activities can have Modifiers, as defined in DestinyActivityModifierDefinition. These are references to the modifiers that *can* be applied to that activity, along with data that we use to determine if that modifier is actually active at any given point in time.
        is_playlist: If True, this Activity is actually a Playlist that refers to multiple possible specific Activities and Activity Modes. For instance, a Crucible Playlist may have references to multiple Activities (Maps) with multiple Activity Modes (specific PvP gameplay modes). If this is true, refer to the playlistItems property for the specific entries in the playlist.
        challenges: An activity can have many Challenges, of which any subset of them may be active for play at any given period of time. This gives the information about the challenges and data that we use to understand when they're active and what rewards they provide. Sadly, at the moment there's no central definition for challenges: much like "Skulls" were in Destiny 1, these are defined on individual activities and there can be many duplicates/near duplicates across the Destiny 2 ecosystem. I have it in mind to centralize these in a future revision of the API, but we are out of time.
        optional_unlock_strings: If there are status strings related to the activity and based on internal state of the game, account, or character, then this will be the definition of those strings and the states needed in order for the strings to be shown.
        playlist_items: Represents all of the possible activities that could be played in the Playlist, along with information that we can use to determine if they are active at the present time.
        activity_graph_list: Unfortunately, in practice this is almost never populated. In theory, this is supposed to tell which Activity Graph to show if you bring up the director while in this activity.
        matchmaking: This block of data provides information about the Activity's matchmaking attributes: how many people can join and such.
        guided_game: This block of data, if it exists, provides information about the guided game experience and restrictions for this activity. If it doesn't exist, the game is not able to be played as a guided game.
        direct_activity_mode_hash: If this activity had an activity mode directly defined on it, this will be the hash of that mode.
        direct_activity_mode_type: If the activity had an activity mode directly defined on it, this will be the enum value of that mode.
        loadouts: The set of all possible loadout requirements that could be active for this activity. Only one will be active at any given time, and you can discover which one through activity-associated data such as Milestones that have activity info on them.
        activity_mode_hashes: The hash identifiers for Activity Modes relevant to this activity.  Note that if this is a playlist, the specific playlist entry chosen will determine the actual activity modes that end up being relevant.
        activity_mode_types: The activity modes - if any - in enum form. Because we can't seem to escape the enums.
        is_pv_p: If true, this activity is a PVP activity or playlist.
        insertion_points: The list of phases or points of entry into an activity, along with information we can use to determine their gating and availability.
        activity_location_mappings: A list of location mappings that are affected by this activity. Pulled out of DestinyLocationDefinitions for our/your lookup convenience.
        hash: The unique identifier for this entity. Guaranteed to be unique for the type of entity, but not globally. When entities refer to each other in Destiny content, it is this hash that they are referring to.
        index: The index of the entity as it was found in the investment tables.
        redacted: If this is true, then there is an entity with this identifier/type combination, but BNet is not yet allowed to show it. Sorry!
    """

    display_properties: "DestinyDisplayPropertiesDefinition" = attr.field()
    original_display_properties: "DestinyDisplayPropertiesDefinition" = attr.field()
    selection_screen_display_properties: "DestinyDisplayPropertiesDefinition" = attr.field()
    release_icon: str = attr.field()
    release_time: int = attr.field()
    activity_light_level: int = attr.field()
    destination_hash: int = attr.field()
    place_hash: int = attr.field()
    activity_type_hash: int = attr.field()
    tier: int = attr.field()
    pgcr_image: str = attr.field()
    rewards: list["DestinyActivityRewardDefinition"] = attr.field()
    modifiers: list["DestinyActivityModifierReferenceDefinition"] = attr.field()
    is_playlist: bool = attr.field()
    challenges: list["DestinyActivityChallengeDefinition"] = attr.field()
    optional_unlock_strings: list["DestinyActivityUnlockStringDefinition"] = attr.field()
    playlist_items: list["DestinyActivityPlaylistItemDefinition"] = attr.field()
    activity_graph_list: list["DestinyActivityGraphListEntryDefinition"] = attr.field()
    matchmaking: "DestinyActivityMatchmakingBlockDefinition" = attr.field()
    guided_game: "DestinyActivityGuidedBlockDefinition" = attr.field()
    direct_activity_mode_hash: int = attr.field()
    direct_activity_mode_type: int = attr.field()
    loadouts: list["DestinyActivityLoadoutRequirementSet"] = attr.field()
    activity_mode_hashes: list[int] = attr.field()
    activity_mode_types: list[int] = attr.field()
    is_pv_p: bool = attr.field()
    insertion_points: list["DestinyActivityInsertionPointDefinition"] = attr.field()
    activity_location_mappings: list["DestinyEnvironmentLocationMapping"] = attr.field()
    hash: int = attr.field()
    index: int = attr.field()
    redacted: bool = attr.field()


@attr.define
class DestinyActivityRewardDefinition(BaseModel):
    """
    Activities can refer to one or more sets of tooltip-friendly reward data. These are the definitions for those tooltip friendly rewards.

    Attributes:
        reward_text: The header for the reward set, if any.
        reward_items: The "Items provided" in the reward. This is almost always a pointer to a DestinyInventoryItemDefintion for an item that you can't actually earn in-game, but that has name/description/icon information for the vague concept of the rewards you will receive. This is because the actual reward generation is non-deterministic and extremely complicated, so the best the game can do is tell you what you'll get in vague terms. And so too shall we. Interesting trivia: you actually *do* earn these items when you complete the activity. They go into a single-slot bucket on your profile, which is how you see the pop-ups of these rewards when you complete an activity that match these "dummy" items. You can even see them if you look at the last one you earned in your profile-level inventory through the BNet API! Who said reading documentation is a waste of time?
    """

    reward_text: str = attr.field()
    reward_items: list["DestinyItemQuantity"] = attr.field()


@attr.define
class DestinyActivityModifierReferenceDefinition(BaseModel):
    """
    A reference to an Activity Modifier from another entity, such as an Activity (for now, just Activities). This defines some

    Attributes:
        activity_modifier_hash: The hash identifier for the DestinyActivityModifierDefinition referenced by this activity.
    """

    activity_modifier_hash: int = attr.field()


@attr.define
class DestinyActivityChallengeDefinition(BaseModel):
    """
    Represents a reference to a Challenge, which for now is just an Objective.

    Attributes:
        objective_hash: The hash for the Objective that matches this challenge. Use it to look up the DestinyObjectiveDefinition.
        dummy_rewards: The rewards as they're represented in the UI. Note that they generally link to "dummy" items that give a summary of rewards rather than direct, real items themselves. If the quantity is 0, don't show the quantity.
    """

    objective_hash: int = attr.field()
    dummy_rewards: list["DestinyItemQuantity"] = attr.field()


@attr.define
class DestinyObjectiveDefinition(BaseModel):
    """
    Defines an "Objective". An objective is a specific task you should accomplish in the game. These are referred to by: - Quest Steps (which are DestinyInventoryItemDefinition entities with Objectives) - Challenges (which are Objectives defined on an DestinyActivityDefintion) - Milestones (which refer to Objectives that are defined on both Quest Steps and Activities) - Anything else that the designers decide to do later. Objectives have progress, a notion of having been Completed, human readable data describing the task to be accomplished, and a lot of optional tack-on data that can enhance the information provided about the task.

    Attributes:
        display_properties: Ideally, this should tell you what your task is. I'm not going to lie to you though. Sometimes this doesn't have useful information at all. Which sucks, but there's nothing either of us can do about it.
        completion_value: The value that the unlock value defined in unlockValueHash must reach in order for the objective to be considered Completed. Used in calculating progress and completion status.
        scope: A shortcut for determining the most restrictive gating that this Objective is set to use. This includes both the dynamic determination of progress and of completion values. See the DestinyGatingScope enum's documentation for more details.
        location_hash: OPTIONAL: a hash identifier for the location at which this objective must be accomplished, if there is a location defined. Look up the DestinyLocationDefinition for this hash for that additional location info.
        allow_negative_value: If true, the value is allowed to go negative.
        allow_value_change_when_completed: If true, you can effectively "un-complete" this objective if you lose progress after crossing the completion threshold.  If False, once you complete the task it will remain completed forever by locking the value.
        is_counting_downward: If true, completion means having an unlock value less than or equal to the completionValue. If False, completion means having an unlock value greater than or equal to the completionValue.
        value_style: The UI style applied to the objective. It's an enum, take a look at DestinyUnlockValueUIStyle for details of the possible styles. Use this info as you wish to customize your UI. DEPRECATED: This is no longer populated by Destiny 2 game content. Please use inProgressValueStyle and completedValueStyle instead.
        progress_description: Text to describe the progress bar.
        perks: If this objective enables Perks intrinsically, the conditions for that enabling are defined here.
        stats: If this objective enables modifications on a player's stats intrinsically, the conditions are defined here.
        minimum_visibility_threshold: If nonzero, this is the minimum value at which the objective's progression should be shown. Otherwise, don't show it yet.
        allow_overcompletion: If True, the progress will continue even beyond the point where the objective met its minimum completion requirements. Your UI will have to accommodate it.
        show_value_on_complete: If True, you should continue showing the progression value in the UI after it's complete. I mean, we already do that in BNet anyways, but if you want to be better behaved than us you could honor this flag.
        completed_value_style: The style to use when the objective is completed.
        in_progress_value_style: The style to use when the objective is still in progress.
        ui_label: Objectives can have arbitrary UI-defined identifiers that define the style applied to objectives. For convenience, known UI labels will be defined in the uiStyle enum value.
        ui_style: If the objective has a known UI label value, this property will represent it.
        hash: The unique identifier for this entity. Guaranteed to be unique for the type of entity, but not globally. When entities refer to each other in Destiny content, it is this hash that they are referring to.
        index: The index of the entity as it was found in the investment tables.
        redacted: If this is true, then there is an entity with this identifier/type combination, but BNet is not yet allowed to show it. Sorry!
    """

    display_properties: "DestinyDisplayPropertiesDefinition" = attr.field()
    completion_value: int = attr.field()
    scope: int = attr.field()
    location_hash: int = attr.field()
    allow_negative_value: bool = attr.field()
    allow_value_change_when_completed: bool = attr.field()
    is_counting_downward: bool = attr.field()
    value_style: int = attr.field()
    progress_description: str = attr.field()
    perks: "DestinyObjectivePerkEntryDefinition" = attr.field()
    stats: "DestinyObjectiveStatEntryDefinition" = attr.field()
    minimum_visibility_threshold: int = attr.field()
    allow_overcompletion: bool = attr.field()
    show_value_on_complete: bool = attr.field()
    completed_value_style: int = attr.field()
    in_progress_value_style: int = attr.field()
    ui_label: str = attr.field()
    ui_style: int = attr.field()
    hash: int = attr.field()
    index: int = attr.field()
    redacted: bool = attr.field()


@attr.define
class DestinyObjectivePerkEntryDefinition(BaseModel):
    """
    Defines the conditions under which an intrinsic perk is applied while participating in an Objective. These perks will generally not be benefit-granting perks, but rather a perk that modifies gameplay in some interesting way.

    Attributes:
        perk_hash: The hash identifier of the DestinySandboxPerkDefinition that will be applied to the character.
        style: An enumeration indicating whether it will be applied as long as the Objective is active, when it's completed, or until it's completed.
    """

    perk_hash: int = attr.field()
    style: int = attr.field()


@attr.define
class DestinySandboxPerkDefinition(BaseModel):
    """
    Perks are modifiers to a character or item that can be applied situationally. - Perks determine a weapons' damage type. - Perks put the Mods in Modifiers (they are literally the entity that bestows the Sandbox benefit for whatever fluff text about the modifier in the Socket, Plug or Talent Node) - Perks are applied for unique alterations of state in Objectives Anyways, I'm sure you can see why perks are so interesting. What Perks often don't have is human readable information, so we attempt to reverse engineer that by pulling that data from places that uniquely refer to these perks: namely, Talent Nodes and Plugs. That only gives us a subset of perks that are human readable, but those perks are the ones people generally care about anyways. The others are left as a mystery, their true purpose mostly unknown and undocumented.

    Attributes:
        display_properties: These display properties are by no means guaranteed to be populated. Usually when it is, it's only because we back-filled them with the displayProperties of some Talent Node or Plug item that happened to be uniquely providing that perk.
        perk_identifier: The string identifier for the perk.
        is_displayable: If true, you can actually show the perk in the UI. Otherwise, it doesn't have useful player-facing information.
        damage_type: If this perk grants a damage type to a weapon, the damage type will be defined here. Unless you have a compelling reason to use this enum value, use the damageTypeHash instead to look up the actual DestinyDamageTypeDefinition.
        damage_type_hash: The hash identifier for looking up the DestinyDamageTypeDefinition, if this perk has a damage type. This is preferred over using the damageType enumeration value, which has been left purely because it is occasionally convenient.
        perk_groups: An old holdover from the original Armory, this was an attempt to group perks by functionality. It is as yet unpopulated, and there will be quite a bit of work needed to restore it to its former working order.
        hash: The unique identifier for this entity. Guaranteed to be unique for the type of entity, but not globally. When entities refer to each other in Destiny content, it is this hash that they are referring to.
        index: The index of the entity as it was found in the investment tables.
        redacted: If this is true, then there is an entity with this identifier/type combination, but BNet is not yet allowed to show it. Sorry!
    """

    display_properties: "DestinyDisplayPropertiesDefinition" = attr.field()
    perk_identifier: str = attr.field()
    is_displayable: bool = attr.field()
    damage_type: int = attr.field()
    damage_type_hash: int = attr.field()
    perk_groups: "DestinyTalentNodeStepGroups" = attr.field()
    hash: int = attr.field()
    index: int = attr.field()
    redacted: bool = attr.field()


@attr.define
class DestinyTalentNodeStepGroups(BaseModel):
    """
    These properties are an attempt to categorize talent node steps by certain common properties. See the related enumerations for the type of properties being categorized.

    Attributes:
        weapon_performance: _No description given by bungie_
        impact_effects: _No description given by bungie_
        guardian_attributes: _No description given by bungie_
        light_abilities: _No description given by bungie_
        damage_types: _No description given by bungie_
    """

    weapon_performance: int = attr.field()
    impact_effects: int = attr.field()
    guardian_attributes: int = attr.field()
    light_abilities: int = attr.field()
    damage_types: int = attr.field()


class DestinyTalentNodeStepWeaponPerformances(BaseEnum):
    """
    _No description given by bungie_
    """

    NONE = 0
    """_No description given by bungie_ """
    RATE_OF_FIRE = 1
    """_No description given by bungie_ """
    DAMAGE = 2
    """_No description given by bungie_ """
    ACCURACY = 4
    """_No description given by bungie_ """
    RANGE = 8
    """_No description given by bungie_ """
    ZOOM = 16
    """_No description given by bungie_ """
    RECOIL = 32
    """_No description given by bungie_ """
    READY = 64
    """_No description given by bungie_ """
    RELOAD = 128
    """_No description given by bungie_ """
    HAIR_TRIGGER = 256
    """_No description given by bungie_ """
    AMMO_AND_MAGAZINE = 512
    """_No description given by bungie_ """
    TRACKING_AND_DETONATION = 1024
    """_No description given by bungie_ """
    SHOTGUN_SPREAD = 2048
    """_No description given by bungie_ """
    CHARGE_TIME = 4096
    """_No description given by bungie_ """
    ALL = 8191
    """_No description given by bungie_ """


class DestinyTalentNodeStepImpactEffects(BaseEnum):
    """
    _No description given by bungie_
    """

    NONE = 0
    """_No description given by bungie_ """
    ARMOR_PIERCING = 1
    """_No description given by bungie_ """
    RICOCHET = 2
    """_No description given by bungie_ """
    FLINCH = 4
    """_No description given by bungie_ """
    COLLATERAL_DAMAGE = 8
    """_No description given by bungie_ """
    DISORIENT = 16
    """_No description given by bungie_ """
    HIGHLIGHT_TARGET = 32
    """_No description given by bungie_ """
    ALL = 63
    """_No description given by bungie_ """


class DestinyTalentNodeStepGuardianAttributes(BaseEnum):
    """
    _No description given by bungie_
    """

    NONE = 0
    """_No description given by bungie_ """
    STATS = 1
    """_No description given by bungie_ """
    SHIELDS = 2
    """_No description given by bungie_ """
    HEALTH = 4
    """_No description given by bungie_ """
    REVIVE = 8
    """_No description given by bungie_ """
    AIM_UNDER_FIRE = 16
    """_No description given by bungie_ """
    RADAR = 32
    """_No description given by bungie_ """
    INVISIBILITY = 64
    """_No description given by bungie_ """
    REPUTATIONS = 128
    """_No description given by bungie_ """
    ALL = 255
    """_No description given by bungie_ """


class DestinyTalentNodeStepLightAbilities(BaseEnum):
    """
    _No description given by bungie_
    """

    NONE = 0
    """_No description given by bungie_ """
    GRENADES = 1
    """_No description given by bungie_ """
    MELEE = 2
    """_No description given by bungie_ """
    MOVEMENT_MODES = 4
    """_No description given by bungie_ """
    ORBS = 8
    """_No description given by bungie_ """
    SUPER_ENERGY = 16
    """_No description given by bungie_ """
    SUPER_MODS = 32
    """_No description given by bungie_ """
    ALL = 63
    """_No description given by bungie_ """


class DestinyTalentNodeStepDamageTypes(BaseEnum):
    """
    _No description given by bungie_
    """

    NONE = 0
    """_No description given by bungie_ """
    KINETIC = 1
    """_No description given by bungie_ """
    ARC = 2
    """_No description given by bungie_ """
    SOLAR = 4
    """_No description given by bungie_ """
    VOID = 8
    """_No description given by bungie_ """
    ALL = 15
    """_No description given by bungie_ """


@attr.define
class DestinyDamageTypeDefinition(BaseModel):
    """
    All damage types that are possible in the game are defined here, along with localized info and icons as needed.

    Attributes:
        display_properties: The description of the damage type, icon etc...
        transparent_icon_path: A variant of the icon that is transparent and colorless.
        show_icon: If TRUE, the game shows this damage type's icon. Otherwise, it doesn't. Whether you show it or not is up to you.
        enum_value: We have an enumeration for damage types for quick reference. This is the current definition's damage type enum value.
        hash: The unique identifier for this entity. Guaranteed to be unique for the type of entity, but not globally. When entities refer to each other in Destiny content, it is this hash that they are referring to.
        index: The index of the entity as it was found in the investment tables.
        redacted: If this is true, then there is an entity with this identifier/type combination, but BNet is not yet allowed to show it. Sorry!
    """

    display_properties: "DestinyDisplayPropertiesDefinition" = attr.field()
    transparent_icon_path: str = attr.field()
    show_icon: bool = attr.field()
    enum_value: int = attr.field()
    hash: int = attr.field()
    index: int = attr.field()
    redacted: bool = attr.field()


@attr.define
class DestinyObjectiveStatEntryDefinition(BaseModel):
    """
    Defines the conditions under which stat modifications will be applied to a Character while participating in an objective.

    Attributes:
        stat: The stat being modified, and the value used.
        style: Whether it will be applied as long as the objective is active, when it's completed, or until it's completed.
    """

    stat: "DestinyItemInvestmentStatDefinition" = attr.field()
    style: int = attr.field()


@attr.define
class DestinyItemInvestmentStatDefinition(BaseModel):
    """
    Represents a "raw" investment stat, before calculated stats are calculated and before any DestinyStatGroupDefinition is applied to transform the stat into something closer to what you see in-game. Because these won't match what you see in-game, consider carefully whether you really want to use these stats. I have left them in case someone can do something useful or interesting with the pre-processed statistics.

    Attributes:
        stat_type_hash: The hash identifier for the DestinyStatDefinition defining this stat.
        value: The raw "Investment" value for the stat, before transformations are performed to turn this raw stat into stats that are displayed in the game UI.
        is_conditionally_active: If this is true, the stat will only be applied on the item in certain game state conditions, and we can't know statically whether or not this stat will be applied. Check the "live" API data instead for whether this value is being applied on a specific instance of the item in question, and you can use this to decide whether you want to show the stat on the generic view of the item, or whether you want to show some kind of caveat or warning about the stat value being conditional on game state.
    """

    stat_type_hash: int = attr.field()
    value: int = attr.field()
    is_conditionally_active: bool = attr.field()


@attr.define
class DestinyLocationDefinition(BaseModel):
    """
    A "Location" is a sort of shortcut for referring to a specific combination of Activity, Destination, Place, and even Bubble or NavPoint within a space. Most of this data isn't intrinsically useful to us, but Objectives refer to locations, and through that we can at least infer the Activity, Destination, and Place being referred to by the Objective.

    Attributes:
        vendor_hash: If the location has a Vendor on it, this is the hash identifier for that Vendor. Look them up with DestinyVendorDefinition.
        location_releases: A Location may refer to different specific spots in the world based on the world's current state. This is a list of those potential spots, and the data we can use at runtime to determine which one of the spots is the currently valid one.
        hash: The unique identifier for this entity. Guaranteed to be unique for the type of entity, but not globally. When entities refer to each other in Destiny content, it is this hash that they are referring to.
        index: The index of the entity as it was found in the investment tables.
        redacted: If this is true, then there is an entity with this identifier/type combination, but BNet is not yet allowed to show it. Sorry!
    """

    vendor_hash: int = attr.field()
    location_releases: list["DestinyLocationReleaseDefinition"] = attr.field()
    hash: int = attr.field()
    index: int = attr.field()
    redacted: bool = attr.field()


@attr.define
class DestinyLocationReleaseDefinition(BaseModel):
    """
    A specific "spot" referred to by a location. Only one of these can be active at a time for a given Location.

    Attributes:
        display_properties: Sadly, these don't appear to be populated anymore (ever?)
        small_transparent_icon: _No description given by bungie_
        map_icon: _No description given by bungie_
        large_transparent_icon: _No description given by bungie_
        spawn_point: If we had map information, this spawnPoint would be interesting. But sadly, we don't have that info.
        destination_hash: The Destination being pointed to by this location.
        activity_hash: The Activity being pointed to by this location.
        activity_graph_hash: The Activity Graph being pointed to by this location.
        activity_graph_node_hash: The Activity Graph Node being pointed to by this location. (Remember that Activity Graph Node hashes are only unique within an Activity Graph: so use the combination to find the node being spoken of)
        activity_bubble_name: The Activity Bubble within the Destination. Look this up in the DestinyDestinationDefinition's bubbles and bubbleSettings properties.
        activity_path_bundle: If we had map information, this would tell us something cool about the path this location wants you to take. I wish we had map information.
        activity_path_destination: If we had map information, this would tell us about path information related to destination on the map. Sad. Maybe you can do something cool with it. Go to town man.
        nav_point_type: The type of Nav Point that this represents. See the enumeration for more info.
        world_position: Looks like it should be the position on the map, but sadly it does not look populated... yet?
    """

    display_properties: "DestinyDisplayPropertiesDefinition" = attr.field()
    small_transparent_icon: str = attr.field()
    map_icon: str = attr.field()
    large_transparent_icon: str = attr.field()
    spawn_point: int = attr.field()
    destination_hash: int = attr.field()
    activity_hash: int = attr.field()
    activity_graph_hash: int = attr.field()
    activity_graph_node_hash: int = attr.field()
    activity_bubble_name: int = attr.field()
    activity_path_bundle: int = attr.field()
    activity_path_destination: int = attr.field()
    nav_point_type: int = attr.field()
    world_position: list[int] = attr.field()


@attr.define
class DestinyActivityUnlockStringDefinition(BaseModel):
    """
    Represents a status string that could be conditionally displayed about an activity. Note that externally, you can only see the strings themselves. Internally we combine this information with server state to determine which strings should be shown.

    Attributes:
        display_string: The string to be displayed if the conditions are met.
    """

    display_string: str = attr.field()


@attr.define
class DestinyActivityPlaylistItemDefinition(BaseModel):
    """
    If the activity is a playlist, this is the definition for a specific entry in the playlist: a single possible combination of Activity and Activity Mode that can be chosen.

    Attributes:
        activity_hash: The hash identifier of the Activity that can be played. Use it to look up the DestinyActivityDefinition.
        direct_activity_mode_hash: If this playlist entry had an activity mode directly defined on it, this will be the hash of that mode.
        direct_activity_mode_type: If the playlist entry had an activity mode directly defined on it, this will be the enum value of that mode.
        activity_mode_hashes: The hash identifiers for Activity Modes relevant to this entry.
        activity_mode_types: The activity modes - if any - in enum form. Because we can't seem to escape the enums.
    """

    activity_hash: int = attr.field()
    direct_activity_mode_hash: int = attr.field()
    direct_activity_mode_type: int = attr.field()
    activity_mode_hashes: list[int] = attr.field()
    activity_mode_types: list[int] = attr.field()


@attr.define
class DestinyActivityModeDefinition(BaseModel):
    """
    This definition represents an "Activity Mode" as it exists in the Historical Stats endpoints. An individual Activity Mode represents a collection of activities that are played in a certain way. For example, Nightfall Strikes are part of a "Nightfall" activity mode, and any activities played as the PVP mode "Clash" are part of the "Clash activity mode. Activity modes are nested under each other in a hierarchy, so that if you ask for - for example - "AllPvP", you will get any PVP activities that the user has played, regardless of what specific PVP mode was being played.

    Attributes:
        display_properties: _No description given by bungie_
        pgcr_image: If this activity mode has a related PGCR image, this will be the path to said image.
        mode_type: The Enumeration value for this Activity Mode. Pass this identifier into Stats endpoints to get aggregate stats for this mode.
        activity_mode_category: The type of play being performed in broad terms (PVP, PVE)
        is_team_based: If True, this mode has oppositional teams fighting against each other rather than "Free-For-All" or Co-operative modes of play. Note that Aggregate modes are never marked as team based, even if they happen to be team based at the moment. At any time, an aggregate whose subordinates are only team based could be changed so that one or more aren't team based, and then this boolean won't make much sense (the aggregation would become "sometimes team based"). Let's not deal with that right now.
        is_aggregate_mode: If true, this mode is an aggregation of other, more specific modes rather than being a mode in itself. This includes modes that group Features/Events rather than Gameplay, such as Trials of The Nine: Trials of the Nine being an Event that is interesting to see aggregate data for, but when you play the activities within Trials of the Nine they are more specific activity modes such as Clash.
        parent_hashes: The hash identifiers of the DestinyActivityModeDefinitions that represent all of the "parent" modes for this mode. For instance, the Nightfall Mode is also a member of AllStrikes and AllPvE.
        friendly_name: A Friendly identifier you can use for referring to this Activity Mode. We really only used this in our URLs, so... you know, take that for whatever it's worth.
        activity_mode_mappings: If this exists, the mode has specific Activities (referred to by the Key) that should instead map to other Activity Modes when they are played. This was useful in D1 for Private Matches, where we wanted to have Private Matches as an activity mode while still referring to the specific mode being played.
        display: If FALSE, we want to ignore this type when we're showing activity modes in BNet UI. It will still be returned in case 3rd parties want to use it for any purpose.
        order: The relative ordering of activity modes.
        hash: The unique identifier for this entity. Guaranteed to be unique for the type of entity, but not globally. When entities refer to each other in Destiny content, it is this hash that they are referring to.
        index: The index of the entity as it was found in the investment tables.
        redacted: If this is true, then there is an entity with this identifier/type combination, but BNet is not yet allowed to show it. Sorry!
    """

    display_properties: "DestinyDisplayPropertiesDefinition" = attr.field()
    pgcr_image: str = attr.field()
    mode_type: int = attr.field()
    activity_mode_category: int = attr.field()
    is_team_based: bool = attr.field()
    is_aggregate_mode: bool = attr.field()
    parent_hashes: list[int] = attr.field()
    friendly_name: str = attr.field()
    activity_mode_mappings: Any = attr.field()
    display: bool = attr.field()
    order: int = attr.field()
    hash: int = attr.field()
    index: int = attr.field()
    redacted: bool = attr.field()


@attr.define
class DestinyActivityMatchmakingBlockDefinition(BaseModel):
    """
    Information about matchmaking and party size for the activity.

    Attributes:
        is_matchmade: If TRUE, the activity is matchmade. Otherwise, it requires explicit forming of a party.
        min_party: The minimum # of people in the fireteam for the activity to launch.
        max_party: The maximum # of people allowed in a Fireteam.
        max_players: The maximum # of people allowed across all teams in the activity.
        requires_guardian_oath: If true, you have to Solemnly Swear to be up to Nothing But Good(tm) to play.
    """

    is_matchmade: bool = attr.field()
    min_party: int = attr.field()
    max_party: int = attr.field()
    max_players: int = attr.field()
    requires_guardian_oath: bool = attr.field()


@attr.define
class DestinyActivityGuidedBlockDefinition(BaseModel):
    """
    Guided Game information for this activity.

    Attributes:
        guided_max_lobby_size: The maximum amount of people that can be in the waiting lobby.
        guided_min_lobby_size: The minimum amount of people that can be in the waiting lobby.
        guided_disband_count: If -1, the guided group cannot be disbanded. Otherwise, take the total # of players in the activity and subtract this number: that is the total # of votes needed for the guided group to disband.
    """

    guided_max_lobby_size: int = attr.field()
    guided_min_lobby_size: int = attr.field()
    guided_disband_count: int = attr.field()


@attr.define
class DestinyActivityLoadoutRequirementSet(BaseModel):
    """
    _No description given by bungie_

    Attributes:
        requirements: The set of requirements that will be applied on the activity if this requirement set is active.
    """

    requirements: list["DestinyActivityLoadoutRequirement"] = attr.field()


@attr.define
class DestinyActivityLoadoutRequirement(BaseModel):
    """
    _No description given by bungie_

    Attributes:
        equipment_slot_hash: _No description given by bungie_
        allowed_equipped_item_hashes: _No description given by bungie_
        allowed_weapon_sub_types: _No description given by bungie_
    """

    equipment_slot_hash: int = attr.field()
    allowed_equipped_item_hashes: list[int] = attr.field()
    allowed_weapon_sub_types: list[int] = attr.field()


@attr.define
class DestinyActivityInsertionPointDefinition(BaseModel):
    """
    A point of entry into an activity, gated by an unlock flag and with some more-or-less useless (for our purposes) phase information. I'm including it in case we end up being able to bolt more useful information onto it in the future. UPDATE: Turns out this information isn't actually useless, and is in fact actually useful for people. Who would have thought? We still don't have localized info for it, but at least this will help people when they're looking at phase indexes in stats data, or when they want to know what phases have been completed on a weekly achievement.

    Attributes:
        phase_hash: A unique hash value representing the phase. This can be useful for, for example, comparing how different instances of Raids have phases in different orders!
    """

    phase_hash: int = attr.field()


@attr.define
class DestinyPlaceDefinition(BaseModel):
    """
    Okay, so Activities (DestinyActivityDefinition) take place in Destinations (DestinyDestinationDefinition). Destinations are part of larger locations known as Places (you're reading its documentation right now). Places are more on the planetary scale, like "Earth" and "Your Mom."

    Attributes:
        display_properties: _No description given by bungie_
        hash: The unique identifier for this entity. Guaranteed to be unique for the type of entity, but not globally. When entities refer to each other in Destiny content, it is this hash that they are referring to.
        index: The index of the entity as it was found in the investment tables.
        redacted: If this is true, then there is an entity with this identifier/type combination, but BNet is not yet allowed to show it. Sorry!
    """

    display_properties: "DestinyDisplayPropertiesDefinition" = attr.field()
    hash: int = attr.field()
    index: int = attr.field()
    redacted: bool = attr.field()


@attr.define
class DestinyActivityTypeDefinition(BaseModel):
    """
    The definition for an Activity Type. In Destiny 2, an Activity Type represents a conceptual categorization of Activities. These are most commonly used in the game for the subtitle under Activities, but BNet uses them extensively to identify and group activities by their common properties. Unfortunately, there has been a movement away from providing the richer data in Destiny 2 that we used to get in Destiny 1 for Activity Types. For instance, Nightfalls are grouped under the same Activity Type as regular Strikes.  For this reason, BNet will eventually migrate toward Activity Modes as a better indicator of activity category. But for the time being, it is still referred to in many places across our codebase.

    Attributes:
        display_properties: _No description given by bungie_
        hash: The unique identifier for this entity. Guaranteed to be unique for the type of entity, but not globally. When entities refer to each other in Destiny content, it is this hash that they are referring to.
        index: The index of the entity as it was found in the investment tables.
        redacted: If this is true, then there is an entity with this identifier/type combination, but BNet is not yet allowed to show it. Sorry!
    """

    display_properties: "DestinyDisplayPropertiesDefinition" = attr.field()
    hash: int = attr.field()
    index: int = attr.field()
    redacted: bool = attr.field()


@attr.define
class DestinyUnlockExpressionDefinition(BaseModel):
    """
    Where the sausage gets made. Unlock Expressions are the foundation of the game's gating mechanics and investment-related restrictions. They can test Unlock Flags and Unlock Values for certain states, using a sufficient amount of logical operators such that unlock expressions are effectively Turing complete. Use UnlockExpressionParser to evaluate expressions using an IUnlockContext parsed from Babel.

    Attributes:
        scope: A shortcut for determining the most restrictive gating that this expression performs. See the DestinyGatingScope enum's documentation for more details.
    """

    scope: int = attr.field()


@attr.define
class DestinyDestinationBubbleSettingDefinition(BaseModel):
    """
    Human readable data about the bubble. Combine with DestinyBubbleDefinition - see DestinyDestinationDefinition.bubbleSettings for more information. DEPRECATED - Just use bubbles.

    Attributes:
        display_properties: _No description given by bungie_
    """

    display_properties: "DestinyDisplayPropertiesDefinition" = attr.field()


@attr.define
class DestinyBubbleDefinition(BaseModel):
    """
    Basic identifying data about the bubble. Combine with DestinyDestinationBubbleSettingDefinition - see DestinyDestinationDefinition.bubbleSettings for more information.

    Attributes:
        hash: The identifier for the bubble: only guaranteed to be unique within the Destination.
        display_properties: The display properties of this bubble, so you don't have to look them up in a separate list anymore.
    """

    hash: int = attr.field()
    display_properties: "DestinyDisplayPropertiesDefinition" = attr.field()


@attr.define
class DestinyVendorGroupReference(BaseModel):
    """
    _No description given by bungie_

    Attributes:
        vendor_group_hash: The DestinyVendorGroupDefinition to which this Vendor can belong.
    """

    vendor_group_hash: int = attr.field()


@attr.define
class DestinyVendorGroupDefinition(BaseModel):
    """
    BNet attempts to group vendors into similar collections. These groups aren't technically game canonical, but they are helpful for filtering vendors or showing them organized into a clean view on a webpage or app. These definitions represent the groups we've built. Unlike in Destiny 1, a Vendors' group may change dynamically as the game state changes: thus, you will want to check DestinyVendorComponent responses to find a vendor's currently active Group (if you care). Using this will let you group your vendors in your UI in a similar manner to how we will do grouping in the Companion.

    Attributes:
        order: The recommended order in which to render the groups, Ascending order.
        category_name: For now, a group just has a name.
        hash: The unique identifier for this entity. Guaranteed to be unique for the type of entity, but not globally. When entities refer to each other in Destiny content, it is this hash that they are referring to.
        index: The index of the entity as it was found in the investment tables.
        redacted: If this is true, then there is an entity with this identifier/type combination, but BNet is not yet allowed to show it. Sorry!
    """

    order: int = attr.field()
    category_name: str = attr.field()
    hash: int = attr.field()
    index: int = attr.field()
    redacted: bool = attr.field()


@attr.define
class DestinyFactionDefinition(BaseModel):
    """
    These definitions represent Factions in the game. Factions have ended up unilaterally being related to Vendors that represent them, but that need not necessarily be the case. A Faction is really just an entity that has a related progression for which a character can gain experience. In Destiny 1, Dead Orbit was an example of a Faction: there happens to be a Vendor that represents Dead Orbit (and indeed, DestinyVendorDefinition.factionHash defines to this relationship), but Dead Orbit could theoretically exist without the Vendor that provides rewards.

    Attributes:
        display_properties: _No description given by bungie_
        progression_hash: The hash identifier for the DestinyProgressionDefinition that indicates the character's relationship with this faction in terms of experience and levels.
        token_values: The faction token item hashes, and their respective progression values.
        reward_item_hash: The faction reward item hash, usually an engram.
        reward_vendor_hash: The faction reward vendor hash, used for faction engram previews.
        vendors: List of vendors that are associated with this faction. The last vendor that passes the unlock flag checks is the one that should be shown.
        hash: The unique identifier for this entity. Guaranteed to be unique for the type of entity, but not globally. When entities refer to each other in Destiny content, it is this hash that they are referring to.
        index: The index of the entity as it was found in the investment tables.
        redacted: If this is true, then there is an entity with this identifier/type combination, but BNet is not yet allowed to show it. Sorry!
    """

    display_properties: "DestinyDisplayPropertiesDefinition" = attr.field()
    progression_hash: int = attr.field()
    token_values: Any = attr.field()
    reward_item_hash: int = attr.field()
    reward_vendor_hash: int = attr.field()
    vendors: list["DestinyFactionVendorDefinition"] = attr.field()
    hash: int = attr.field()
    index: int = attr.field()
    redacted: bool = attr.field()


@attr.define
class DestinyFactionVendorDefinition(BaseModel):
    """
    These definitions represent faction vendors at different points in the game. A single faction may contain multiple vendors, or the same vendor available at two different locations.

    Attributes:
        vendor_hash: The faction vendor hash.
        destination_hash: The hash identifier for a Destination at which this vendor may be located. Each destination where a Vendor may exist will only ever have a single entry.
        background_image_path: The relative path to the background image representing this Vendor at this location, for use in a banner.
    """

    vendor_hash: int = attr.field()
    destination_hash: int = attr.field()
    background_image_path: str = attr.field()


@attr.define
class DestinySandboxPatternDefinition(BaseModel):
    """
    _No description given by bungie_

    Attributes:
        pattern_hash: _No description given by bungie_
        pattern_global_tag_id_hash: _No description given by bungie_
        weapon_content_group_hash: _No description given by bungie_
        weapon_translation_group_hash: _No description given by bungie_
        weapon_type_hash: _No description given by bungie_
        weapon_type: _No description given by bungie_
        filters: _No description given by bungie_
        hash: The unique identifier for this entity. Guaranteed to be unique for the type of entity, but not globally. When entities refer to each other in Destiny content, it is this hash that they are referring to.
        index: The index of the entity as it was found in the investment tables.
        redacted: If this is true, then there is an entity with this identifier/type combination, but BNet is not yet allowed to show it. Sorry!
    """

    pattern_hash: int = attr.field()
    pattern_global_tag_id_hash: int = attr.field()
    weapon_content_group_hash: int = attr.field()
    weapon_translation_group_hash: int = attr.field()
    weapon_type_hash: int = attr.field()
    weapon_type: int = attr.field()
    filters: list["DestinyArrangementRegionFilterDefinition"] = attr.field()
    hash: int = attr.field()
    index: int = attr.field()
    redacted: bool = attr.field()


@attr.define
class DestinyArrangementRegionFilterDefinition(BaseModel):
    """
    _No description given by bungie_

    Attributes:
        art_arrangement_region_hash: _No description given by bungie_
        art_arrangement_region_index: _No description given by bungie_
        stat_hash: _No description given by bungie_
        arrangement_index_by_stat_value: _No description given by bungie_
    """

    art_arrangement_region_hash: int = attr.field()
    art_arrangement_region_index: int = attr.field()
    stat_hash: int = attr.field()
    arrangement_index_by_stat_value: Any = attr.field()


@attr.define
class DestinyItemPreviewBlockDefinition(BaseModel):
    """
    Items like Sacks or Boxes can have items that it shows in-game when you view details that represent the items you can obtain if you use or acquire the item. This defines those categories, and gives some insights into that data's source.

    Attributes:
        screen_style: A string that the game UI uses as a hint for which detail screen to show for the item. You, too, can leverage this for your own custom screen detail views. Note, however, that these are arbitrarily defined by designers: there's no guarantees of a fixed, known number of these - so fall back to something reasonable if you don't recognize it.
        preview_vendor_hash: If the preview data is derived from a fake "Preview" Vendor, this will be the hash identifier for the DestinyVendorDefinition of that fake vendor.
        artifact_hash: If this item should show you Artifact information when you preview it, this is the hash identifier of the DestinyArtifactDefinition for the artifact whose data should be shown.
        preview_action_string: If the preview has an associated action (like "Open"), this will be the localized string for that action.
        derived_item_categories: This is a list of the items being previewed, categorized in the same way as they are in the preview UI.
    """

    screen_style: str = attr.field()
    preview_vendor_hash: int = attr.field()
    artifact_hash: int = attr.field()
    preview_action_string: str = attr.field()
    derived_item_categories: list["DestinyDerivedItemCategoryDefinition"] = attr.field()


@attr.define
class DestinyItemQualityBlockDefinition(BaseModel):
    """
    An item's "Quality" determines its calculated stats. The Level at which the item spawns is combined with its "qualityLevel" along with some additional calculations to determine the value of those stats. In Destiny 2, most items don't have default item levels and quality, making this property less useful: these apparently are almost always determined by the complex mechanisms of the Reward system rather than statically. They are still provided here in case they are still useful for people. This also contains some information about Infusion.

    Attributes:
        item_levels: The "base" defined level of an item. This is a list because, in theory, each Expansion could define its own base level for an item. In practice, not only was that never done in Destiny 1, but now this isn't even populated at all. When it's not populated, the level at which it spawns has to be inferred by Reward information, of which BNet receives an imperfect view and will only be reliable on instanced data as a result.
        quality_level: qualityLevel is used in combination with the item's level to calculate stats like Attack and Defense. It plays a role in that calculation, but not nearly as large as itemLevel does.
        infusion_category_name: The string identifier for this item's "infusability", if any.  Items that match the same infusionCategoryName are allowed to infuse with each other. DEPRECATED: Items can now have multiple infusion categories. Please use infusionCategoryHashes instead.
        infusion_category_hash: The hash identifier for the infusion. It does not map to a Definition entity. DEPRECATED: Items can now have multiple infusion categories. Please use infusionCategoryHashes instead.
        infusion_category_hashes: If any one of these hashes matches any value in another item's infusionCategoryHashes, the two can infuse with each other.
        progression_level_requirement_hash: An item can refer to pre-set level requirements. They are defined in DestinyProgressionLevelRequirementDefinition, and you can use this hash to find the appropriate definition.
        current_version: The latest version available for this item.
        versions: The list of versions available for this item.
        display_version_watermark_icons: Icon overlays to denote the item version and power cap status.
    """

    item_levels: list[int] = attr.field()
    quality_level: int = attr.field()
    infusion_category_name: str = attr.field()
    infusion_category_hash: int = attr.field()
    infusion_category_hashes: list[int] = attr.field()
    progression_level_requirement_hash: int = attr.field()
    current_version: int = attr.field()
    versions: list["DestinyItemVersionDefinition"] = attr.field()
    display_version_watermark_icons: list[str] = attr.field()


@attr.define
class DestinyItemVersionDefinition(BaseModel):
    """
    The version definition currently just holds a reference to the power cap.

    Attributes:
        power_cap_hash: A reference to the power cap for this item version.
    """

    power_cap_hash: int = attr.field()


@attr.define
class DestinyItemValueBlockDefinition(BaseModel):
    """
    This defines an item's "Value". Unfortunately, this appears to be used in different ways depending on the way that the item itself is used. For items being sold at a Vendor, this is the default "sale price" of the item. These days, the vendor itself almost always sets the price, but it still possible for the price to fall back to this value. For quests, it is a preview of rewards you can gain by completing the quest. For dummy items, if the itemValue refers to an Emblem, it is the emblem that should be shown as the reward. (jeez louise) It will likely be used in a number of other ways in the future, it appears to be a bucket where they put arbitrary items and quantities into the item.

    Attributes:
        item_value: References to the items that make up this item's "value", and the quantity.
        value_description: If there's a localized text description of the value provided, this will be said description.
    """

    item_value: list["DestinyItemQuantity"] = attr.field()
    value_description: str = attr.field()


@attr.define
class DestinyItemSourceBlockDefinition(BaseModel):
    """
    Data about an item's "sources": ways that the item can be obtained.

    Attributes:
        source_hashes: The list of hash identifiers for Reward Sources that hint where the item can be found (DestinyRewardSourceDefinition).
        sources: A collection of details about the stats that were computed for the ways we found that the item could be spawned.
        exclusive: If we found that this item is exclusive to a specific platform, this will be set to the BungieMembershipType enumeration that matches that platform.
        vendor_sources: A denormalized reference back to vendors that potentially sell this item.
    """

    source_hashes: list[int] = attr.field()
    sources: list["DestinyItemSourceDefinition"] = attr.field()
    exclusive: int = attr.field()
    vendor_sources: list["DestinyItemVendorSourceReference"] = attr.field()


@attr.define
class DestinyRewardSourceDefinition(BaseModel):
    """
    Represents a heuristically-determined "item source" according to Bungie.net. These item sources are non-canonical: we apply a combination of special configuration and often-fragile heuristics to attempt to discern whether an item should be part of a given "source," but we have known cases of false positives and negatives due to our imperfect heuristics. Still, they provide a decent approximation for people trying to figure out how an item can be obtained. DestinyInventoryItemDefinition refers to sources in the sourceDatas.sourceHashes property for all sources we determined the item could spawn from. An example in Destiny 1 of a Source would be "Nightfall". If an item has the "Nightfall" source associated with it, it's extremely likely that you can earn that item while playing Nightfall, either during play or as an after-completion reward.

    Attributes:
        display_properties: _No description given by bungie_
        category: Sources are grouped into categories: common ways that items are provided. I hope to see this expand in Destiny 2 once we have time to generate accurate reward source data.
        hash: The unique identifier for this entity. Guaranteed to be unique for the type of entity, but not globally. When entities refer to each other in Destiny content, it is this hash that they are referring to.
        index: The index of the entity as it was found in the investment tables.
        redacted: If this is true, then there is an entity with this identifier/type combination, but BNet is not yet allowed to show it. Sorry!
    """

    display_properties: "DestinyDisplayPropertiesDefinition" = attr.field()
    category: int = attr.field()
    hash: int = attr.field()
    index: int = attr.field()
    redacted: bool = attr.field()


class DestinyRewardSourceCategory(BaseEnum):
    """
    BNet's custom categorization of reward sources. We took a look at the existing ways that items could be spawned, and tried to make high-level categorizations of them. This needs to be re-evaluated for Destiny 2.
    """

    NONE = 0
    """The source doesn't fit well into any of the other types. """
    ACTIVITY = 1
    """The source is directly related to the rewards gained by playing an activity or set of activities. This currently includes Quests and other action in-game. """
    VENDOR = 2
    """This source is directly related to items that Vendors sell. """
    AGGREGATE = 3
    """This source is a custom aggregation of items that can be earned in many ways, but that share some other property in common that is useful to share. For instance, in Destiny 1 we would make "Reward Sources" for every game expansion: that way, you could search reward sources to see what items became available with any given Expansion. """


@attr.define
class DestinyItemVendorSourceReference(BaseModel):
    """
    Represents that a vendor could sell this item, and provides a quick link to that vendor and sale item.  Note that we do not and cannot make a guarantee that the vendor will ever *actually* sell this item, only that the Vendor has a definition that indicates it *could* be sold.  Note also that a vendor may sell the same item in multiple "ways", which means there may be multiple vendorItemIndexes for a single Vendor hash.

    Attributes:
        vendor_hash: The identifier for the vendor that may sell this item.
        vendor_item_indexes: The Vendor sale item indexes that represent the sale information for this item. The same vendor may sell an item in multiple "ways", hence why this is a list. (for instance, a weapon may be "sold" as a reward in a quest, for Glimmer, and for Masterwork Cores: each of those ways would be represented by a different vendor sale item with a different index)
    """

    vendor_hash: int = attr.field()
    vendor_item_indexes: list[int] = attr.field()


@attr.define
class DestinyItemObjectiveBlockDefinition(BaseModel):
    """
    An item can have objectives on it. In practice, these are the exclusive purview of "Quest Step" items: DestinyInventoryItemDefinitions that represent a specific step in a Quest. Quest steps have 1:M objectives that we end up processing and returning in live data as DestinyQuestStatus data, and other useful information.

    Attributes:
        objective_hashes: The hashes to Objectives (DestinyObjectiveDefinition) that are part of this Quest Step, in the order that they should be rendered.
        display_activity_hashes: For every entry in objectiveHashes, there is a corresponding entry in this array at the same index. If the objective is meant to be associated with a specific DestinyActivityDefinition, there will be a valid hash at that index. Otherwise, it will be invalid (0). Rendered somewhat obsolete by perObjectiveDisplayProperties, which currently has much the same information but may end up with more info in the future.
        require_full_objective_completion: If True, all objectives must be completed for the step to be completed. If False, any one objective can be completed for the step to be completed.
        questline_item_hash: The hash for the DestinyInventoryItemDefinition representing the Quest to which this Quest Step belongs.
        narrative: The localized string for narrative text related to this quest step, if any.
        objective_verb_name: The localized string describing an action to be performed associated with the objectives, if any.
        quest_type_identifier: The identifier for the type of quest being performed, if any. Not associated with any fixed definition, yet.
        quest_type_hash: A hashed value for the questTypeIdentifier, because apparently I like to be redundant.
        per_objective_display_properties: One entry per Objective on the item, it will have related display information.
        display_as_stat_tracker: _No description given by bungie_
    """

    objective_hashes: list[int] = attr.field()
    display_activity_hashes: list[int] = attr.field()
    require_full_objective_completion: bool = attr.field()
    questline_item_hash: int = attr.field()
    narrative: str = attr.field()
    objective_verb_name: str = attr.field()
    quest_type_identifier: str = attr.field()
    quest_type_hash: int = attr.field()
    per_objective_display_properties: list["DestinyObjectiveDisplayProperties"] = attr.field()
    display_as_stat_tracker: bool = attr.field()


@attr.define
class DestinyObjectiveDisplayProperties(BaseModel):
    """
    _No description given by bungie_

    Attributes:
        activity_hash: The activity associated with this objective in the context of this item, if any.
        display_on_item_preview_screen: If true, the game shows this objective on item preview screens.
    """

    activity_hash: int = attr.field()
    display_on_item_preview_screen: bool = attr.field()


@attr.define
class DestinyItemMetricBlockDefinition(BaseModel):
    """
    The metrics available for display and selection on an item.

    Attributes:
        available_metric_category_node_hashes: Hash identifiers for any DestinyPresentationNodeDefinition entry that can be used to list available metrics. Any metric listed directly below these nodes, or in any of these nodes' children will be made available for selection.
    """

    available_metric_category_node_hashes: list[int] = attr.field()


@attr.define
class DestinyUnlockValueDefinition(BaseModel):
    """
    An Unlock Value is an internal integer value, stored on the server and used in a variety of ways, most frequently for the gating/requirement checks that the game performs across all of its main features. They can also be used as the storage data for mapped Progressions, Objectives, and other features that require storage of variable numeric values.

    Attributes:
        hash: The unique identifier for this entity. Guaranteed to be unique for the type of entity, but not globally. When entities refer to each other in Destiny content, it is this hash that they are referring to.
        index: The index of the entity as it was found in the investment tables.
        redacted: If this is true, then there is an entity with this identifier/type combination, but BNet is not yet allowed to show it. Sorry!
    """

    hash: int = attr.field()
    index: int = attr.field()
    redacted: bool = attr.field()


@attr.define
class DestinyItemGearsetBlockDefinition(BaseModel):
    """
    If an item has a related gearset, this is the list of items in that set, and an unlock expression that evaluates to a number representing the progress toward gearset completion (a very rare use for unlock expressions!)

    Attributes:
        tracking_value_max: The maximum possible number of items that can be collected.
        item_list: The list of hashes for items in the gearset. Use them to look up DestinyInventoryItemDefinition entries for the items in the set.
    """

    tracking_value_max: int = attr.field()
    item_list: list[int] = attr.field()


@attr.define
class DestinyItemSackBlockDefinition(BaseModel):
    """
    Some items are "sacks" - they can be "opened" to produce other items. This is information related to its sack status, mostly UI strings. Engrams are an example of items that are considered to be "Sacks".

    Attributes:
        detail_action: A description of what will happen when you open the sack. As far as I can tell, this is blank currently. Unknown whether it will eventually be populated with useful info.
        open_action: The localized name of the action being performed when you open the sack.
        select_item_count: _No description given by bungie_
        vendor_sack_type: _No description given by bungie_
        open_on_acquire: _No description given by bungie_
    """

    detail_action: str = attr.field()
    open_action: str = attr.field()
    select_item_count: int = attr.field()
    vendor_sack_type: str = attr.field()
    open_on_acquire: bool = attr.field()


@attr.define
class DestinyItemSocketBlockDefinition(BaseModel):
    """
    If defined, the item has at least one socket.

    Attributes:
        detail: This was supposed to be a string that would give per-item details about sockets. In practice, it turns out that all this ever has is the localized word "details". ... that's lame, but perhaps it will become something cool in the future.
        socket_entries: Each non-intrinsic (or mutable) socket on an item is defined here. Check inside for more info.
        intrinsic_sockets: Each intrinsic (or immutable/permanent) socket on an item is defined here, along with the plug that is permanently affixed to the socket.
        socket_categories: A convenience property, that refers to the sockets in the "sockets" property, pre-grouped by category and ordered in the manner that they should be grouped in the UI. You could form this yourself with the existing data, but why would you want to? Enjoy life man.
    """

    detail: str = attr.field()
    socket_entries: list["DestinyItemSocketEntryDefinition"] = attr.field()
    intrinsic_sockets: list["DestinyItemIntrinsicSocketEntryDefinition"] = attr.field()
    socket_categories: list["DestinyItemSocketCategoryDefinition"] = attr.field()


@attr.define
class DestinyItemSocketEntryDefinition(BaseModel):
    """
    The definition information for a specific socket on an item. This will determine how the socket behaves in-game.

    Attributes:
        socket_type_hash: All sockets have a type, and this is the hash identifier for this particular type. Use it to look up the DestinySocketTypeDefinition: read there for more information on how socket types affect the behavior of the socket.
        single_initial_item_hash: If a valid hash, this is the hash identifier for the DestinyInventoryItemDefinition representing the Plug that will be initially inserted into the item on item creation. Otherwise, this Socket will either start without a plug inserted, or will have one randomly inserted.
        reusable_plug_items: This is a list of pre-determined plugs that can *always* be plugged into this socket, without the character having the plug in their inventory. If this list is populated, you will not be allowed to plug an arbitrary item in the socket: you will only be able to choose from one of these reusable plugs.
        prevent_initialization_on_vendor_purchase: If this is true, then the socket will not be initialized with a plug if the item is purchased from a Vendor. Remember that Vendors are much more than conceptual vendors: they include "Collection Kiosks" and other entities. See DestinyVendorDefinition for more information.
        hide_perks_in_item_tooltip: If this is true, the perks provided by this socket shouldn't be shown in the item's tooltip. This might be useful if it's providing a hidden bonus, or if the bonus is less important than other benefits on the item.
        plug_sources: Indicates where you should go to get plugs for this socket. This will affect how you populate your UI, as well as what plugs are valid for this socket. It's an alternative to having to check for the existence of certain properties (reusablePlugItems for example) to infer where plugs should come from.
        reusable_plug_set_hash: If this socket's plugs come from a reusable DestinyPlugSetDefinition, this is the identifier for that set. We added this concept to reduce some major duplication that's going to come from sockets as replacements for what was once implemented as large sets of items and kiosks (like Emotes).  As of Shadowkeep, these will come up much more frequently and be driven by game content rather than custom curation.
        randomized_plug_set_hash: This field replaces "randomizedPlugItems" as of Shadowkeep launch. If a socket has randomized plugs, this is a pointer to the set of plugs that could be used, as defined in DestinyPlugSetDefinition.  If null, the item has no randomized plugs.
        default_visible: If true, then this socket is visible in the item's "default" state. If you have an instance, you should always check the runtime state, as that can override this visibility setting: but if you're looking at the item on a conceptual level, this property can be useful for hiding data such as legacy sockets - which remain defined on items for infrastructure purposes, but can be confusing for users to see.
    """

    socket_type_hash: int = attr.field()
    single_initial_item_hash: int = attr.field()
    reusable_plug_items: list["DestinyItemSocketEntryPlugItemDefinition"] = attr.field()
    prevent_initialization_on_vendor_purchase: bool = attr.field()
    hide_perks_in_item_tooltip: bool = attr.field()
    plug_sources: int = attr.field()
    reusable_plug_set_hash: int = attr.field()
    randomized_plug_set_hash: int = attr.field()
    default_visible: bool = attr.field()


@attr.define
class DestinyItemSocketEntryPlugItemDefinition(BaseModel):
    """
    The definition of a known, reusable plug that can be applied to a socket.

    Attributes:
        plug_item_hash: The hash identifier of a DestinyInventoryItemDefinition representing the plug that can be inserted.
    """

    plug_item_hash: int = attr.field()


@attr.define
class DestinyItemSocketEntryPlugItemRandomizedDefinition(BaseModel):
    """
    _No description given by bungie_

    Attributes:
        crafting_requirements: _No description given by bungie_
        currently_can_roll: Indicates if the plug can be rolled on the current version of the item. For example, older versions of weapons may have plug rolls that are no longer possible on the current versions.
        plug_item_hash: The hash identifier of a DestinyInventoryItemDefinition representing the plug that can be inserted.
    """

    crafting_requirements: "DestinyPlugItemCraftingRequirements" = attr.field()
    currently_can_roll: bool = attr.field()
    plug_item_hash: int = attr.field()


@attr.define
class DestinyPlugItemCraftingRequirements(BaseModel):
    """
    _No description given by bungie_

    Attributes:
        unlock_requirements: _No description given by bungie_
        required_level: If the plug has a known level requirement, it'll be available here.
        material_requirement_hashes: _No description given by bungie_
    """

    unlock_requirements: list["DestinyPlugItemCraftingUnlockRequirement"] = attr.field()
    required_level: int = attr.field()
    material_requirement_hashes: list[int] = attr.field()


@attr.define
class DestinyPlugItemCraftingUnlockRequirement(BaseModel):
    """
    _No description given by bungie_

    Attributes:
        failure_description: _No description given by bungie_
    """

    failure_description: str = attr.field()


@attr.define
class DestinyItemIntrinsicSocketEntryDefinition(BaseModel):
    """
    Represents a socket that has a plug associated with it intrinsically. This is useful for situations where the weapon needs to have a visual plug/Mod on it, but that plug/Mod should never change.

    Attributes:
        plug_item_hash: Indicates the plug that is intrinsically inserted into this socket.
        socket_type_hash: Indicates the type of this intrinsic socket.
        default_visible: If true, then this socket is visible in the item's "default" state. If you have an instance, you should always check the runtime state, as that can override this visibility setting: but if you're looking at the item on a conceptual level, this property can be useful for hiding data such as legacy sockets - which remain defined on items for infrastructure purposes, but can be confusing for users to see.
    """

    plug_item_hash: int = attr.field()
    socket_type_hash: int = attr.field()
    default_visible: bool = attr.field()


@attr.define
class DestinyItemSocketCategoryDefinition(BaseModel):
    """
    Sockets are grouped into categories in the UI. These define which category and which sockets are under that category.

    Attributes:
        socket_category_hash: The hash for the Socket Category: a quick way to go get the header display information for the category. Use it to look up DestinySocketCategoryDefinition info.
        socket_indexes: Use these indexes to look up the sockets in the "sockets.socketEntries" property on the item definition. These are the indexes under the category, in game-rendered order.
    """

    socket_category_hash: int = attr.field()
    socket_indexes: list[int] = attr.field()


@attr.define
class DestinyItemSummaryBlockDefinition(BaseModel):
    """
    This appears to be information used when rendering rewards. We don't currently use it on BNet.

    Attributes:
        sort_priority: Apparently when rendering an item in a reward, this should be used as a sort priority. We're not doing it presently.
    """

    sort_priority: int = attr.field()


@attr.define
class DestinyItemTalentGridBlockDefinition(BaseModel):
    """
    This defines information that can only come from a talent grid on an item. Items mostly have negligible talent grid data these days, but instanced items still retain grids as a source for some of this common information. Builds/Subclasses are the only items left that still have talent grids with meaningful Nodes.

    Attributes:
        talent_grid_hash: The hash identifier of the DestinyTalentGridDefinition attached to this item.
        item_detail_string: This is meant to be a subtitle for looking at the talent grid. In practice, somewhat frustratingly, this always merely says the localized word for "Details". Great. Maybe it'll have more if talent grids ever get used for more than builds and subclasses again.
        build_name: A shortcut string identifier for the "build" in question, if this talent grid has an associated build. Doesn't map to anything we can expose at the moment.
        hud_damage_type: If the talent grid implies a damage type, this is the enum value for that damage type.
        hud_icon: If the talent grid has a special icon that's shown in the game UI (like builds, funny that), this is the identifier for that icon. Sadly, we don't actually get that icon right now. I'll be looking to replace this with a path to the actual icon itself.
    """

    talent_grid_hash: int = attr.field()
    item_detail_string: str = attr.field()
    build_name: str = attr.field()
    hud_damage_type: int = attr.field()
    hud_icon: str = attr.field()


@attr.define
class DestinyTalentGridDefinition(BaseModel):
    """
    The time has unfortunately come to talk about Talent Grids. Talent Grids are the most complex and unintuitive part of the Destiny Definition data. Grab a cup of coffee before we begin, I can wait. Talent Grids were the primary way that items could be customized in Destiny 1. In Destiny 2, for now, talent grids have become exclusively used by Subclass/Build items: but the system is still in place for it to be used by items should the direction change back toward talent grids. Talent Grids have Nodes: the visual circles on the talent grid detail screen that have icons and can be activated if you meet certain requirements and pay costs. The actual visual data and effects, however, are driven by the "Steps" on Talent Nodes. Any given node will have 1:M of these steps, and the specific step that will be considered the "current" step (and thus the dictator of all benefits, visual state, and activation requirements on the Node) will almost always not be determined until an instance of the item is created. This is how, in Destiny 1, items were able to have such a wide variety of what users saw as "Perks": they were actually Talent Grids with nodes that had a wide variety of Steps, randomly chosen at the time of item creation. Now that Talent Grids are used exclusively by subclasses and builds, all of the properties within still apply: but there are additional visual elements on the Subclass/Build screens that are superimposed on top of the talent nodes. Unfortunately, BNet doesn't have this data: if you want to build a subclass screen, you will have to provide your own "decorative" assets, such as the visual connectors between nodes and the fancy colored-fire-bathed character standing behind the nodes. DestinyInventoryItem.talentGrid.talentGridHash defines an item's linked Talent Grid, which brings you to this definition that contains enough satic data about talent grids to make your head spin. These *must* be combined with instanced data - found when live data returns DestinyItemTalentGridComponent - in order to derive meaning. The instanced data will reference nodes and steps within these definitions, which you will then have to look up in the definition and combine with the instanced data to give the user the visual representation of their item's talent grid.

    Attributes:
        max_grid_level: The maximum possible level of the Talent Grid: at this level, any nodes are allowed to be activated.
        grid_level_per_column: The meaning of this has been lost in the sands of time: it still exists as a property, but appears to be unused in the modern UI of talent grids. It used to imply that each visual "column" of talent nodes required identical progression levels in order to be activated. Returning this value in case it is still useful to someone? Perhaps it's just a bit of interesting history.
        progression_hash: The hash identifier of the Progression (DestinyProgressionDefinition) that drives whether and when Talent Nodes can be activated on the Grid. Items will have instances of this Progression, and will gain experience that will eventually cause the grid to increase in level. As the grid's level increases, it will cross the threshold where nodes can be activated. See DestinyTalentGridStepDefinition's activation requirements for more information.
        nodes: The list of Talent Nodes on the Grid (recall that Nodes themselves are really just locations in the UI to show whatever their current Step is. You will only know the current step for a node by retrieving instanced data through platform calls to the API that return DestinyItemTalentGridComponent).
        exclusive_sets: Talent Nodes can exist in "exclusive sets": these are sets of nodes in which only a single node in the set can be activated at any given time. Activating a node in this set will automatically deactivate the other nodes in the set (referred to as a "Swap"). If a node in the exclusive set has already been activated, the game will not charge you materials to activate another node in the set, even if you have never activated it before, because you already paid the cost to activate one node in the set. Not to be confused with Exclusive Groups. (how the heck do we NOT get confused by that? Jeez) See the groups property for information about that only-tangentially-related concept.
        independent_node_indexes: This is a quick reference to the indexes of nodes that are not part of exclusive sets. Handy for knowing which talent nodes can only be activated directly, rather than via swapping.
        groups: Talent Nodes can have "Exclusive Groups". These are not to be confused with Exclusive Sets (see exclusiveSets property). Look at the definition of DestinyTalentExclusiveGroup for more information and how they work. These groups are keyed by the "groupHash" from DestinyTalentExclusiveGroup.
        node_categories: BNet wants to show talent nodes grouped by similar purpose with localized titles. This is the ordered list of those categories: if you want to show nodes by category, you can iterate over this list, render the displayProperties for the category as the title, and then iterate over the talent nodes referenced by the category to show the related nodes. Note that this is different from Exclusive Groups or Sets, because these categories also incorporate "Independent" nodes that belong to neither sets nor groups. These are purely for visual grouping of nodes rather than functional grouping.
        hash: The unique identifier for this entity. Guaranteed to be unique for the type of entity, but not globally. When entities refer to each other in Destiny content, it is this hash that they are referring to.
        index: The index of the entity as it was found in the investment tables.
        redacted: If this is true, then there is an entity with this identifier/type combination, but BNet is not yet allowed to show it. Sorry!
    """

    max_grid_level: int = attr.field()
    grid_level_per_column: int = attr.field()
    progression_hash: int = attr.field()
    nodes: list["DestinyTalentNodeDefinition"] = attr.field()
    exclusive_sets: list["DestinyTalentNodeExclusiveSetDefinition"] = attr.field()
    independent_node_indexes: list[int] = attr.field()
    groups: Any = attr.field()
    node_categories: list["DestinyTalentNodeCategory"] = attr.field()
    hash: int = attr.field()
    index: int = attr.field()
    redacted: bool = attr.field()


@attr.define
class DestinyTalentNodeDefinition(BaseModel):
    """
    Talent Grids on items have Nodes. These nodes have positions in the talent grid's UI, and contain "Steps" (DestinyTalentNodeStepDefinition), one of whom will be the "Current" step. The Current Step determines the visual properties of the node, as well as what the node grants when it is activated. See DestinyTalentGridDefinition for a more complete overview of how Talent Grids work, and how they are used in Destiny 2 (and how they were used in Destiny 1).

    Attributes:
        node_index: The index into the DestinyTalentGridDefinition's "nodes" property where this node is located. Used to uniquely identify the node within the Talent Grid. Note that this is content version dependent: make sure you have the latest version of content before trying to use these properties.
        node_hash: The hash identifier for the node, which unfortunately is also content version dependent but can be (and ideally, should be) used instead of the nodeIndex to uniquely identify the node. The two exist side-by-side for backcompat reasons due to the Great Talent Node Restructuring of Destiny 1, and I ran out of time to remove one of them and standardize on the other. Sorry!
        row: The visual "row" where the node should be shown in the UI. If negative, then the node is hidden.
        column: The visual "column" where the node should be shown in the UI. If negative, the node is hidden.
        prerequisite_node_indexes: Indexes into the DestinyTalentGridDefinition.nodes property for any nodes that must be activated before this one is allowed to be activated. I would have liked to change this to hashes for Destiny 2, but we have run out of time.
        binary_pair_node_index: At one point, Talent Nodes supported the idea of "Binary Pairs": nodes that overlapped each other visually, and where activating one deactivated the other. They ended up not being used, mostly because Exclusive Sets are *almost* a superset of this concept, but the potential for it to be used still exists in theory. If this is ever used, this will be the index into the DestinyTalentGridDefinition.nodes property for the node that is the binary pair match to this node. Activating one deactivates the other.
        auto_unlocks: If true, this node will automatically unlock when the Talent Grid's level reaches the required level of the current step of this node.
        last_step_repeats: At one point, Nodes were going to be able to be activated multiple times, changing the current step and potentially piling on multiple effects from the previously activated steps. This property would indicate if the last step could be activated multiple times.  This is not currently used, but it isn't out of the question that this could end up being used again in a theoretical future.
        is_random: If this is true, the node's step is determined randomly rather than the first step being chosen.
        random_activation_requirement: At one point, you were going to be able to repurchase talent nodes that had random steps, to "re-roll" the current step of the node (and thus change the properties of your item). This was to be the activation requirement for performing that re-roll. The system still exists to do this, as far as I know, so it may yet come back around!
        is_random_repurchasable: If this is true, the node can be "re-rolled" to acquire a different random current step. This is not used, but still exists for a theoretical future of talent grids.
        steps: At this point, "steps" have been obfuscated into conceptual entities, aggregating the underlying notions of "properties" and "true steps". If you need to know a step as it truly exists - such as when recreating Node logic when processing Vendor data - you'll have to use the "realSteps" property below.
        exclusive_with_node_hashes: The nodeHash values for nodes that are in an Exclusive Set with this node. See DestinyTalentGridDefinition.exclusiveSets for more info about exclusive sets. Again, note that these are nodeHashes and *not* nodeIndexes.
        random_start_progression_bar_at_progression: If the node's step is randomly selected, this is the amount of the Talent Grid's progression experience at which the progression bar for the node should be shown.
        layout_identifier: A string identifier for a custom visual layout to apply to this talent node. Unfortunately, we do not have any data for rendering these custom layouts. It will be up to you to interpret these strings and change your UI if you want to have custom UI matching these layouts.
        group_hash: As of Destiny 2, nodes can exist as part of "Exclusive Groups". These differ from exclusive sets in that, within the group, many nodes can be activated. But the act of activating any node in the group will cause "opposing" nodes (nodes in groups that are not allowed to be activated at the same time as this group) to deactivate. See DestinyTalentExclusiveGroup for more information on the details. This is an identifier for this node's group, if it is part of one.
        lore_hash: Talent nodes can be associated with a piece of Lore, generally rendered in a tooltip. This is the hash identifier of the lore element to show, if there is one to be show.
        node_style_identifier: Comes from the talent grid node style: this identifier should be used to determine how to render the node in the UI.
        ignore_for_completion: Comes from the talent grid node style: if true, then this node should be ignored for determining whether the grid is complete.
    """

    node_index: int = attr.field()
    node_hash: int = attr.field()
    row: int = attr.field()
    column: int = attr.field()
    prerequisite_node_indexes: list[int] = attr.field()
    binary_pair_node_index: int = attr.field()
    auto_unlocks: bool = attr.field()
    last_step_repeats: bool = attr.field()
    is_random: bool = attr.field()
    random_activation_requirement: "DestinyNodeActivationRequirement" = attr.field()
    is_random_repurchasable: bool = attr.field()
    steps: list["DestinyNodeStepDefinition"] = attr.field()
    exclusive_with_node_hashes: list[int] = attr.field()
    random_start_progression_bar_at_progression: int = attr.field()
    layout_identifier: str = attr.field()
    group_hash: int = attr.field()
    lore_hash: int = attr.field()
    node_style_identifier: str = attr.field()
    ignore_for_completion: bool = attr.field()


@attr.define
class DestinyNodeActivationRequirement(BaseModel):
    """
    Talent nodes have requirements that must be met before they can be activated. This describes the material costs, the Level of the Talent Grid's progression required, and other conditional information that limits whether a talent node can be activated.

    Attributes:
        grid_level: The Progression level on the Talent Grid required to activate this node. See DestinyTalentGridDefinition.progressionHash for the related Progression, and read DestinyProgressionDefinition's documentation to learn more about Progressions.
        material_requirement_hashes: The list of hash identifiers for material requirement sets: materials that are required for the node to be activated. See DestinyMaterialRequirementSetDefinition for more information about material requirements. In this case, only a single DestinyMaterialRequirementSetDefinition will be chosen from this list, and we won't know which one will be chosen until an instance of the item is created.
    """

    grid_level: int = attr.field()
    material_requirement_hashes: list[int] = attr.field()


@attr.define
class DestinyNodeStepDefinition(BaseModel):
    """
    This defines the properties of a "Talent Node Step". When you see a talent node in game, the actual visible properties that you see (its icon, description, the perks and stats it provides) are not provided by the Node itself, but rather by the currently active Step on the node. When a Talent Node is activated, the currently active step's benefits are conferred upon the item and character. The currently active step on talent nodes are determined when an item is first instantiated. Sometimes it is random, sometimes it is more deterministic (particularly when a node has only a single step). Note that, when dealing with Talent Node Steps, you must ensure that you have the latest version of content. stepIndex and nodeStepHash - two ways of identifying the step within a node - are both content version dependent, and thus are subject to change between content updates.

    Attributes:
        display_properties: These are the display properties actually used to render the Talent Node. The currently active step's displayProperties are shown.
        step_index: The index of this step in the list of Steps on the Talent Node. Unfortunately, this is the closest thing we have to an identifier for the Step: steps are not provided a content version agnostic identifier. This means that, when you are dealing with talent nodes, you will need to first ensure that you have the latest version of content.
        node_step_hash: The hash of this node step. Unfortunately, while it can be used to uniquely identify the step within a node, it is also content version dependent and should not be relied on without ensuring you have the latest vesion of content.
        interaction_description: If you can interact with this node in some way, this is the localized description of that interaction.
        damage_type: An enum representing a damage type granted by activating this step, if any.
        damage_type_hash: If the step provides a damage type, this will be the hash identifier used to look up the damage type's DestinyDamageTypeDefinition.
        activation_requirement: If the step has requirements for activation (they almost always do, if nothing else than for the Talent Grid's Progression to have reached a certain level), they will be defined here.
        can_activate_next_step: There was a time when talent nodes could be activated multiple times, and the effects of subsequent Steps would be compounded on each other, essentially "upgrading" the node. We have moved away from this, but theoretically the capability still exists. I continue to return this in case it is used in the future: if true and this step is the current step in the node, you are allowed to activate the node a second time to receive the benefits of the next step in the node, which will then become the active step.
        next_step_index: The stepIndex of the next step in the talent node, or -1 if this is the last step or if the next step to be chosen is random. This doesn't really matter anymore unless canActivateNextStep begins to be used again.
        is_next_step_random: If true, the next step to be chosen is random, and if you're allowed to activate the next step. (if canActivateNextStep = true)
        perk_hashes: The list of hash identifiers for Perks (DestinySandboxPerkDefinition) that are applied when this step is active. Perks provide a variety of benefits and modifications - examine DestinySandboxPerkDefinition to learn more.
        start_progression_bar_at_progress: When the Talent Grid's progression reaches this value, the circular "progress bar" that surrounds the talent node should be shown. This also indicates the lower bound of said progress bar, with the upper bound being the progress required to reach activationRequirement.gridLevel. (at some point I should precalculate the upper bound and put it in the definition to save people time)
        stat_hashes: When the step provides stat benefits on the item or character, this is the list of hash identifiers for stats (DestinyStatDefinition) that are provided.
        affects_quality: If this is true, the step affects the item's Quality in some way. See DestinyInventoryItemDefinition for more information about the meaning of Quality. I already made a joke about Zen and the Art of Motorcycle Maintenance elsewhere in the documentation, so I will avoid doing it again. Oops too late
        step_groups: In Destiny 1, the Armory's Perk Filtering was driven by a concept of TalentNodeStepGroups: categorizations of talent nodes based on their functionality. While the Armory isn't a BNet-facing thing for now, and the new Armory will need to account for Sockets rather than Talent Nodes, this categorization capability feels useful enough to still keep around.
        affects_level: If true, this step can affect the level of the item. See DestinyInventoryItemDefintion for more information about item levels and their effect on stats.
        socket_replacements: If this step is activated, this will be a list of information used to replace socket items with new Plugs. See DestinyInventoryItemDefinition for more information about sockets and plugs.
    """

    display_properties: "DestinyDisplayPropertiesDefinition" = attr.field()
    step_index: int = attr.field()
    node_step_hash: int = attr.field()
    interaction_description: str = attr.field()
    damage_type: int = attr.field()
    damage_type_hash: int = attr.field()
    activation_requirement: "DestinyNodeActivationRequirement" = attr.field()
    can_activate_next_step: bool = attr.field()
    next_step_index: int = attr.field()
    is_next_step_random: bool = attr.field()
    perk_hashes: list[int] = attr.field()
    start_progression_bar_at_progress: int = attr.field()
    stat_hashes: list[int] = attr.field()
    affects_quality: bool = attr.field()
    step_groups: "DestinyTalentNodeStepGroups" = attr.field()
    affects_level: bool = attr.field()
    socket_replacements: list["DestinyNodeSocketReplaceResponse"] = attr.field()


@attr.define
class DestinyNodeSocketReplaceResponse(BaseModel):
    """
    This is a bit of an odd duck. Apparently, if talent nodes steps have this data, the game will go through on step activation and alter the first Socket it finds on the item that has a type matching the given socket type, inserting the indicated plug item.

    Attributes:
        socket_type_hash: The hash identifier of the socket type to find amidst the item's sockets (the item to which this talent grid is attached). See DestinyInventoryItemDefinition.sockets.socketEntries to find the socket type of sockets on the item in question.
        plug_item_hash: The hash identifier of the plug item that will be inserted into the socket found.
    """

    socket_type_hash: int = attr.field()
    plug_item_hash: int = attr.field()


@attr.define
class DestinyTalentNodeExclusiveSetDefinition(BaseModel):
    """
    The list of indexes into the Talent Grid's "nodes" property for nodes in this exclusive set. (See DestinyTalentNodeDefinition.nodeIndex)

    Attributes:
        node_indexes: The list of node indexes for the exclusive set. Historically, these were indexes. I would have liked to replace this with nodeHashes for consistency, but it's way too late for that. (9:09 PM, he's right!)
    """

    node_indexes: list[int] = attr.field()


@attr.define
class DestinyTalentExclusiveGroup(BaseModel):
    """
    As of Destiny 2, nodes can exist as part of "Exclusive Groups". These differ from exclusive sets in that, within the group, many nodes can be activated. But the act of activating any node in the group will cause "opposing" nodes (nodes in groups that are not allowed to be activated at the same time as this group) to deactivate.

    Attributes:
        group_hash: The identifier for this exclusive group. Only guaranteed unique within the talent grid, not globally.
        lore_hash: If this group has an associated piece of lore to show next to it, this will be the identifier for that DestinyLoreDefinition.
        node_hashes: A quick reference of the talent nodes that are part of this group, by their Talent Node hashes. (See DestinyTalentNodeDefinition.nodeHash)
        opposing_group_hashes: A quick reference of Groups whose nodes will be deactivated if any node in this group is activated.
        opposing_node_hashes: A quick reference of Nodes that will be deactivated if any node in this group is activated, by their Talent Node hashes. (See DestinyTalentNodeDefinition.nodeHash)
    """

    group_hash: int = attr.field()
    lore_hash: int = attr.field()
    node_hashes: list[int] = attr.field()
    opposing_group_hashes: list[int] = attr.field()
    opposing_node_hashes: list[int] = attr.field()


@attr.define
class DestinyTalentNodeCategory(BaseModel):
    """
    An artificial construct provided by Bungie.Net, where we attempt to group talent nodes by functionality. This is a single set of references to Talent Nodes that share a common trait or purpose.

    Attributes:
        identifier: Mostly just for debug purposes, but if you find it useful you can have it. This is BNet's manually created identifier for this category.
        is_lore_driven: If true, we found the localized content in a related DestinyLoreDefinition instead of local BNet localization files. This is mostly for ease of my own future investigations.
        display_properties: Will contain at least the "name", which will be the title of the category. We will likely not have description and an icon yet, but I'm going to keep my options open.
        node_hashes: The set of all hash identifiers for Talent Nodes (DestinyTalentNodeDefinition) in this Talent Grid that are part of this Category.
    """

    identifier: str = attr.field()
    is_lore_driven: bool = attr.field()
    display_properties: "DestinyDisplayPropertiesDefinition" = attr.field()
    node_hashes: list[int] = attr.field()


@attr.define
class DestinyItemPerkEntryDefinition(BaseModel):
    """
    An intrinsic perk on an item, and the requirements for it to be activated.

    Attributes:
        requirement_display_string: If this perk is not active, this is the string to show for why it's not providing its benefits.
        perk_hash: A hash identifier for the DestinySandboxPerkDefinition being provided on the item.
        perk_visibility: Indicates whether this perk should be shown, or if it should be shown disabled.
    """

    requirement_display_string: str = attr.field()
    perk_hash: int = attr.field()
    perk_visibility: int = attr.field()


@attr.define
class DestinyItemCategoryDefinition(BaseModel):
    """
    In an attempt to categorize items by type, usage, and other interesting properties, we created DestinyItemCategoryDefinition: information about types that is assembled using a set of heuristics that examine the properties of an item such as what inventory bucket it's in, its item type name, and whether it has or is missing certain blocks of data. This heuristic is imperfect, however. If you find an item miscategorized, let us know on the Bungie API forums! We then populate all of the categories that we think an item belongs to in its DestinyInventoryItemDefinition.itemCategoryHashes property. You can use that to provide your own custom item filtering, sorting, aggregating... go nuts on it! And let us know if you see more categories that you wish would be added!

    Attributes:
        display_properties: _No description given by bungie_
        visible: If True, this category should be visible in UI. Sometimes we make categories that we don't think are interesting externally. It's up to you if you want to skip on showing them.
        deprecated: If True, this category has been deprecated: it may have no items left, or there may be only legacy items that remain in it which are no longer relevant to the game.
        short_title: A shortened version of the title. The reason why we have this is because the Armory in German had titles that were too long to display in our UI, so these were localized abbreviated versions of those categories. The property still exists today, even though the Armory doesn't exist for D2... yet.
        item_type_regex: The janky regular expression we used against the item type to try and discern whether the item belongs to this category.
        grant_destiny_breaker_type: If the item in question has this category, it also should have this breaker type.
        plug_category_identifier: If the item is a plug, this is the identifier we expect to find associated with it if it is in this category.
        item_type_regex_not: If the item type matches this janky regex, it does *not* belong to this category.
        origin_bucket_identifier: If the item belongs to this bucket, it does belong to this category.
        grant_destiny_item_type: If an item belongs to this category, it will also receive this item type. This is now how DestinyItemType is populated for items: it used to be an even jankier process, but that's a story that requires more alcohol.
        grant_destiny_sub_type: If an item belongs to this category, it will also receive this subtype enum value. I know what you're thinking - what if it belongs to multiple categories that provide sub-types? The last one processed wins, as is the case with all of these "grant" enums. Now you can see one reason why we moved away from these enums... but they're so convenient when they work, aren't they?
        grant_destiny_class: If an item belongs to this category, it will also get this class restriction enum value. See the other "grant"-prefixed properties on this definition for my color commentary.
        trait_id: The traitId that can be found on items that belong to this category.
        grouped_category_hashes: If this category is a "parent" category of other categories, those children will have their hashes listed in rendering order here, and can be looked up using these hashes against DestinyItemCategoryDefinition. In this way, you can build up a visual hierarchy of item categories. That's what we did, and you can do it too. I believe in you. Yes, you, Carl. (I hope someone named Carl reads this someday)
        parent_category_hashes: All item category hashes of "parent" categories: categories that contain this as a child through the hierarchy of groupedCategoryHashes. It's a bit redundant, but having this child-centric list speeds up some calculations.
        group_category_only: If true, this category is only used for grouping, and should not be evaluated with its own checks. Rather, the item only has this category if it has one of its child categories.
        hash: The unique identifier for this entity. Guaranteed to be unique for the type of entity, but not globally. When entities refer to each other in Destiny content, it is this hash that they are referring to.
        index: The index of the entity as it was found in the investment tables.
        redacted: If this is true, then there is an entity with this identifier/type combination, but BNet is not yet allowed to show it. Sorry!
    """

    display_properties: "DestinyDisplayPropertiesDefinition" = attr.field()
    visible: bool = attr.field()
    deprecated: bool = attr.field()
    short_title: str = attr.field()
    item_type_regex: str = attr.field()
    grant_destiny_breaker_type: int = attr.field()
    plug_category_identifier: str = attr.field()
    item_type_regex_not: str = attr.field()
    origin_bucket_identifier: str = attr.field()
    grant_destiny_item_type: int = attr.field()
    grant_destiny_sub_type: int = attr.field()
    grant_destiny_class: int = attr.field()
    trait_id: str = attr.field()
    grouped_category_hashes: list[int] = attr.field()
    parent_category_hashes: list[int] = attr.field()
    group_category_only: bool = attr.field()
    hash: int = attr.field()
    index: int = attr.field()
    redacted: bool = attr.field()


@attr.define
class DestinyProgressionRewardItemQuantity(BaseModel):
    """
    _No description given by bungie_

    Attributes:
        rewarded_at_progression_level: _No description given by bungie_
        acquisition_behavior: _No description given by bungie_
        ui_display_style: _No description given by bungie_
        claim_unlock_display_strings: _No description given by bungie_
        item_hash: The hash identifier for the item in question. Use it to look up the item's DestinyInventoryItemDefinition.
        item_instance_id: If this quantity is referring to a specific instance of an item, this will have the item's instance ID. Normally, this will be null.
        quantity: The amount of the item needed/available depending on the context of where DestinyItemQuantity is being used.
        has_conditional_visibility: Indicates that this item quantity may be conditionally shown or hidden, based on various sources of state. For example: server flags, account state, or character progress.
    """

    rewarded_at_progression_level: int = attr.field()
    acquisition_behavior: int = attr.field()
    ui_display_style: str = attr.field()
    claim_unlock_display_strings: list[str] = attr.field()
    item_hash: int = attr.field()
    item_instance_id: int = attr.field()
    quantity: int = attr.field()
    has_conditional_visibility: bool = attr.field()


@attr.define
class DestinyRaceDefinition(BaseModel):
    """
    In Destiny, "Races" are really more like "Species". Sort of. I mean, are the Awoken a separate species from humans? I'm not sure. But either way, they're defined here. You'll see Exo, Awoken, and Human as examples of these Species. Players will choose one for their character.

    Attributes:
        display_properties: _No description given by bungie_
        race_type: An enumeration defining the existing, known Races/Species for player characters. This value will be the enum value matching this definition.
        gendered_race_names: A localized string referring to the singular form of the Race's name when referred to in gendered form. Keyed by the DestinyGender.
        gendered_race_names_by_gender_hash: _No description given by bungie_
        hash: The unique identifier for this entity. Guaranteed to be unique for the type of entity, but not globally. When entities refer to each other in Destiny content, it is this hash that they are referring to.
        index: The index of the entity as it was found in the investment tables.
        redacted: If this is true, then there is an entity with this identifier/type combination, but BNet is not yet allowed to show it. Sorry!
    """

    display_properties: "DestinyDisplayPropertiesDefinition" = attr.field()
    race_type: int = attr.field()
    gendered_race_names: Any = attr.field()
    gendered_race_names_by_gender_hash: Any = attr.field()
    hash: int = attr.field()
    index: int = attr.field()
    redacted: bool = attr.field()


@attr.define
class DestinyUnlockDefinition(BaseModel):
    """
    Unlock Flags are small bits (literally, a bit, as in a boolean value) that the game server uses for an extremely wide range of state checks, progress storage, and other interesting tidbits of information.

    Attributes:
        display_properties: Sometimes, but not frequently, these unlock flags also have human readable information: usually when they are being directly tested for some requirement, in which case the string is a localized description of why the requirement check failed.
        hash: The unique identifier for this entity. Guaranteed to be unique for the type of entity, but not globally. When entities refer to each other in Destiny content, it is this hash that they are referring to.
        index: The index of the entity as it was found in the investment tables.
        redacted: If this is true, then there is an entity with this identifier/type combination, but BNet is not yet allowed to show it. Sorry!
    """

    display_properties: "DestinyDisplayPropertiesDefinition" = attr.field()
    hash: int = attr.field()
    index: int = attr.field()
    redacted: bool = attr.field()


@attr.define
class DestinyMedalTierDefinition(BaseModel):
    """
    An artificial construct of our own creation, to try and put some order on top of Medals and keep them from being one giant, unmanageable and unsorted blob of stats. Unfortunately, we haven't had time to do this evaluation yet in Destiny 2, so we're short on Medal Tiers. This will hopefully be updated over time, if Medals continue to exist.

    Attributes:
        tier_name: The name of the tier.
        order: If you're rendering medals by tier, render them in this order (ascending)
        hash: The unique identifier for this entity. Guaranteed to be unique for the type of entity, but not globally. When entities refer to each other in Destiny content, it is this hash that they are referring to.
        index: The index of the entity as it was found in the investment tables.
        redacted: If this is true, then there is an entity with this identifier/type combination, but BNet is not yet allowed to show it. Sorry!
    """

    tier_name: str = attr.field()
    order: int = attr.field()
    hash: int = attr.field()
    index: int = attr.field()
    redacted: bool = attr.field()


@attr.define
class DestinyEntitySearchResult(BaseModel):
    """
    The results of a search for Destiny content. This will be improved on over time, I've been doing some experimenting to see what might be useful.

    Attributes:
        suggested_words: A list of suggested words that might make for better search results, based on the text searched for.
        results: The items found that are matches/near matches for the searched-for term, sorted by something vaguely resembling "relevance". Hopefully this will get better in the future.
    """

    suggested_words: list[str] = attr.field()
    results: "SearchResultOfDestinyEntitySearchResultItem" = attr.field()


@attr.define
class DestinyEntitySearchResultItem(BaseModel):
    """
    An individual Destiny Entity returned from the entity search.

    Attributes:
        hash: The hash identifier of the entity. You will use this to look up the DestinyDefinition relevant for the entity found.
        entity_type: The type of entity, returned as a string matching the DestinyDefinition's contract class name. You'll have to have your own mapping from class names to actually looking up those definitions in the manifest databases.
        display_properties: Basic display properties on the entity, so you don't have to look up the definition to show basic results for the item.
        weight: The ranking value for sorting that we calculated using our relevance formula. This will hopefully get better with time and iteration.
    """

    hash: int = attr.field()
    entity_type: str = attr.field()
    display_properties: "DestinyDisplayPropertiesDefinition" = attr.field()
    weight: float = attr.field()
