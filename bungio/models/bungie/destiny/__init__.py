import datetime
from typing import TYPE_CHECKING, Any, Optional, Union

import attr

from bungio.models.base import BaseEnum, BaseModel

if TYPE_CHECKING:
    from bungio.models import (
        DestinyActivityDefinition,
        DestinyActivityModifierDefinition,
        DestinyChallengeStatus,
        DestinyInventoryItemDefinition,
        DestinyMaterialRequirement,
        DestinyProgressionDefinition,
        DestinyStatDefinition,
        DestinyUnlockDefinition,
        PlatformErrorCodes,
    )


@attr.define
class DestinyProgression(BaseModel):
    """
    Information about a current character's status with a Progression. A progression is a value that can increase with activity and has levels. Think Character Level and Reputation Levels. Combine this "live" data with the related DestinyProgressionDefinition for a full picture of the Progression.

    Attributes:
        progression_hash: The hash identifier of the Progression in question. Use it to look up the DestinyProgressionDefinition in static data.
        daily_progress: The amount of progress earned today for this progression.
        daily_limit: If this progression has a daily limit, this is that limit.
        weekly_progress: The amount of progress earned toward this progression in the current week.
        weekly_limit: If this progression has a weekly limit, this is that limit.
        current_progress: This is the total amount of progress obtained overall for this progression (for instance, the total amount of Character Level experience earned)
        level: This is the level of the progression (for instance, the Character Level).
        level_cap: This is the maximum possible level you can achieve for this progression (for example, the maximum character level obtainable)
        step_index: Progressions define their levels in "steps". Since the last step may be repeatable, the user may be at a higher level than the actual Step achieved in the progression. Not necessarily useful, but potentially interesting for those cruising the API. Relate this to the "steps" property of the DestinyProgression to see which step the user is on, if you care about that. (Note that this is Content Version dependent since it refers to indexes.)
        progress_to_next_level: The amount of progression (i.e. "Experience") needed to reach the next level of this Progression. Jeez, progression is such an overloaded word.
        next_level_at: The total amount of progression (i.e. "Experience") needed in order to reach the next level.
        current_reset_count: The number of resets of this progression you've executed this season, if applicable to this progression.
        season_resets: Information about historical resets of this progression, if there is any data for it.
        reward_item_states: Information about historical rewards for this progression, if there is any data for it.
    """

    progression_hash: "DestinyProgressionDefinition" = attr.field()
    daily_progress: int = attr.field()
    daily_limit: int = attr.field()
    weekly_progress: int = attr.field()
    weekly_limit: int = attr.field()
    current_progress: int = attr.field()
    level: int = attr.field()
    level_cap: int = attr.field()
    step_index: int = attr.field()
    progress_to_next_level: int = attr.field()
    next_level_at: int = attr.field()
    current_reset_count: int = attr.field()
    season_resets: list["DestinyProgressionResetEntry"] = attr.field()
    reward_item_states: list["DestinyProgressionRewardItemState"] = attr.field()


@attr.define
class DestinyProgressionResetEntry(BaseModel):
    """
    Represents a season and the number of resets you had in that season.  We do not necessarily - even for progressions with resets - track it over all seasons. So be careful and check the season numbers being returned.

    Attributes:
        season: _No description given by bungie_
        resets: _No description given by bungie_
    """

    season: int = attr.field()
    resets: int = attr.field()


class DestinyProgressionRewardItemState(BaseEnum):
    """
    Represents the different states a progression reward item can be in.
    """

    NONE = 0
    """_No description given by bungie_ """
    INVISIBLE = 1
    """If this is set, the reward should be hidden. """
    EARNED = 2
    """If this is set, the reward has been earned. """
    CLAIMED = 4
    """If this is set, the reward has been claimed. """
    CLAIM_ALLOWED = 8
    """If this is set, the reward is allowed to be claimed by this Character. An item can be earned but still can't be claimed in certain circumstances, like if it's only allowed for certain subclasses. It also might not be able to be claimed if you already claimed it! """


class DestinyProgressionScope(BaseEnum):
    """
    There are many Progressions in Destiny (think Character Level, or Reputation). These are the various "Scopes" of Progressions, which affect many things: * Where/if they are stored * How they are calculated * Where they can be used in other game logic
    """

    ACCOUNT = 0
    """_No description given by bungie_ """
    CHARACTER = 1
    """_No description given by bungie_ """
    CLAN = 2
    """_No description given by bungie_ """
    ITEM = 3
    """_No description given by bungie_ """
    IMPLICIT_FROM_EQUIPMENT = 4
    """_No description given by bungie_ """
    MAPPED = 5
    """_No description given by bungie_ """
    MAPPED_AGGREGATE = 6
    """_No description given by bungie_ """
    MAPPED_STAT = 7
    """_No description given by bungie_ """
    MAPPED_UNLOCK_VALUE = 8
    """_No description given by bungie_ """


class DestinyProgressionStepDisplayEffect(BaseEnum):
    """
    If progression is earned, this determines whether the progression shows visual effects on the character or its item - or neither.
    """

    NONE = 0
    """_No description given by bungie_ """
    CHARACTER = 1
    """_No description given by bungie_ """
    ITEM = 2
    """_No description given by bungie_ """


@attr.define
class DestinyItemQuantity(BaseModel):
    """
    Used in a number of Destiny contracts to return data about an item stack and its quantity. Can optionally return an itemInstanceId if the item is instanced - in which case, the quantity returned will be 1. If it's not... uh, let me know okay? Thanks.

    Attributes:
        item_hash: The hash identifier for the item in question. Use it to look up the item's DestinyInventoryItemDefinition.
        item_instance_id: If this quantity is referring to a specific instance of an item, this will have the item's instance ID. Normally, this will be null.
        quantity: The amount of the item needed/available depending on the context of where DestinyItemQuantity is being used.
        has_conditional_visibility: Indicates that this item quantity may be conditionally shown or hidden, based on various sources of state. For example: server flags, account state, or character progress.
    """

    item_hash: "DestinyInventoryItemDefinition" = attr.field()
    item_instance_id: int = attr.field()
    quantity: int = attr.field()
    has_conditional_visibility: bool = attr.field()


class SocketTypeActionType(BaseEnum):
    """
    Indicates the type of actions that can be performed
    """

    INSERT_PLUG = 0
    """_No description given by bungie_ """
    INFUSE_ITEM = 1
    """_No description given by bungie_ """
    REINITIALIZE_SOCKET = 2
    """_No description given by bungie_ """


class DestinySocketVisibility(BaseEnum):
    """
    _No description given by bungie_
    """

    VISIBLE = 0
    """_No description given by bungie_ """
    HIDDEN = 1
    """_No description given by bungie_ """
    HIDDEN_WHEN_EMPTY = 2
    """_No description given by bungie_ """
    HIDDEN_IF_NO_PLUGS_AVAILABLE = 3
    """_No description given by bungie_ """


class DestinySocketCategoryStyle(BaseEnum):
    """
    Represents the possible and known UI styles used by the game for rendering Socket Categories.
    """

    UNKNOWN = 0
    """_No description given by bungie_ """
    REUSABLE = 1
    """_No description given by bungie_ """
    CONSUMABLE = 2
    """_No description given by bungie_ """
    UNLOCKABLE = 3
    """_No description given by bungie_ """
    INTRINSIC = 4
    """_No description given by bungie_ """
    ENERGY_METER = 5
    """_No description given by bungie_ """
    LARGE_PERK = 6
    """_No description given by bungie_ """
    ABILITIES = 7
    """_No description given by bungie_ """
    SUPERS = 8
    """_No description given by bungie_ """


class TierType(BaseEnum):
    """
    _No description given by bungie_
    """

    UNKNOWN = 0
    """_No description given by bungie_ """
    CURRENCY = 1
    """_No description given by bungie_ """
    BASIC = 2
    """_No description given by bungie_ """
    COMMON = 3
    """_No description given by bungie_ """
    RARE = 4
    """_No description given by bungie_ """
    SUPERIOR = 5
    """_No description given by bungie_ """
    EXOTIC = 6
    """_No description given by bungie_ """


class BucketScope(BaseEnum):
    """
    _No description given by bungie_
    """

    CHARACTER = 0
    """_No description given by bungie_ """
    ACCOUNT = 1
    """_No description given by bungie_ """


class BucketCategory(BaseEnum):
    """
    _No description given by bungie_
    """

    INVISIBLE = 0
    """_No description given by bungie_ """
    ITEM = 1
    """_No description given by bungie_ """
    CURRENCY = 2
    """_No description given by bungie_ """
    EQUIPPABLE = 3
    """_No description given by bungie_ """
    IGNORED = 4
    """_No description given by bungie_ """


class ItemLocation(BaseEnum):
    """
    _No description given by bungie_
    """

    UNKNOWN = 0
    """_No description given by bungie_ """
    INVENTORY = 1
    """_No description given by bungie_ """
    VAULT = 2
    """_No description given by bungie_ """
    VENDOR = 3
    """_No description given by bungie_ """
    POSTMASTER = 4
    """_No description given by bungie_ """


class DestinyStatAggregationType(BaseEnum):
    """
    When a Stat (DestinyStatDefinition) is aggregated, this is the rules used for determining the level and formula used for aggregation. * CharacterAverage = apply a weighted average using the related DestinyStatGroupDefinition on the DestinyInventoryItemDefinition across the character's equipped items. See both of those definitions for details. * Character = don't aggregate: the stat should be located and used directly on the character. * Item = don't aggregate: the stat should be located and used directly on the item.
    """

    CHARACTER_AVERAGE = 0
    """_No description given by bungie_ """
    CHARACTER = 1
    """_No description given by bungie_ """
    ITEM = 2
    """_No description given by bungie_ """


class DestinyStatCategory(BaseEnum):
    """
    At last, stats have categories. Use this for whatever purpose you might wish.
    """

    GAMEPLAY = 0
    """_No description given by bungie_ """
    WEAPON = 1
    """_No description given by bungie_ """
    DEFENSE = 2
    """_No description given by bungie_ """
    PRIMARY = 3
    """_No description given by bungie_ """


class EquippingItemBlockAttributes(BaseEnum):
    """
    _No description given by bungie_
    """

    NONE = 0
    """_No description given by bungie_ """
    EQUIP_ON_ACQUIRE = 1
    """_No description given by bungie_ """


class DestinyAmmunitionType(BaseEnum):
    """
    _No description given by bungie_
    """

    NONE = 0
    """_No description given by bungie_ """
    PRIMARY = 1
    """_No description given by bungie_ """
    SPECIAL = 2
    """_No description given by bungie_ """
    HEAVY = 3
    """_No description given by bungie_ """
    UNKNOWN = 4
    """_No description given by bungie_ """


@attr.define
class DyeReference(BaseModel):
    """
    _No description given by bungie_

    Attributes:
        channel_hash: _No description given by bungie_
        dye_hash: _No description given by bungie_
    """

    channel_hash: int = attr.field()
    dye_hash: int = attr.field()


class DestinyClass(BaseEnum):
    """
    _No description given by bungie_
    """

    TITAN = 0
    """_No description given by bungie_ """
    HUNTER = 1
    """_No description given by bungie_ """
    WARLOCK = 2
    """_No description given by bungie_ """
    UNKNOWN = 3
    """_No description given by bungie_ """


class DestinyGender(BaseEnum):
    """
    _No description given by bungie_
    """

    MALE = 0
    """_No description given by bungie_ """
    FEMALE = 1
    """_No description given by bungie_ """
    UNKNOWN = 2
    """_No description given by bungie_ """


class DestinyVendorProgressionType(BaseEnum):
    """
    Describes the type of progression that a vendor has.
    """

    DEFAULT = 0
    """The original rank progression from token redemption. """
    RITUAL = 1
    """Progression from ranks in ritual content. For example: Crucible (Shaxx), Gambit (Drifter), and Season 13 Battlegrounds (War Table). """
    NO_SEASONAL_REFRESH = 2
    """A vendor progression with no seasonal refresh. For example: Xur in the Eternity destination for the 30th Anniversary. """


class VendorDisplayCategorySortOrder(BaseEnum):
    """
    Display categories can have custom sort orders. These are the possible options.
    """

    DEFAULT = 0
    """_No description given by bungie_ """
    SORT_BY_TIER = 1
    """_No description given by bungie_ """


class DestinyVendorInteractionRewardSelection(BaseEnum):
    """
    When a Vendor Interaction provides rewards, they'll either let you choose one or let you have all of them. This determines which it will be.
    """

    NONE = 0
    """_No description given by bungie_ """
    ONE = 1
    """_No description given by bungie_ """
    ALL = 2
    """_No description given by bungie_ """


class DestinyVendorReplyType(BaseEnum):
    """
    This determines the type of reply that a Vendor will have during an Interaction.
    """

    ACCEPT = 0
    """_No description given by bungie_ """
    DECLINE = 1
    """_No description given by bungie_ """
    COMPLETE = 2
    """_No description given by bungie_ """


class VendorInteractionType(BaseEnum):
    """
    An enumeration of the known UI interactions for Vendors.
    """

    UNKNOWN = 0
    """_No description given by bungie_ """
    UNDEFINED = 1
    """An empty interaction. If this ends up in content, it is probably a game bug. """
    QUEST_COMPLETE = 2
    """An interaction shown when you complete a quest and receive a reward. """
    QUEST_CONTINUE = 3
    """An interaction shown when you talk to a Vendor as an intermediary step of a quest. """
    REPUTATION_PREVIEW = 4
    """An interaction shown when you are previewing the vendor's reputation rewards. """
    RANK_UP_REWARD = 5
    """An interaction shown when you rank up with the vendor. """
    TOKEN_TURN_IN = 6
    """An interaction shown when you have tokens to turn in for the vendor. """
    QUEST_ACCEPT = 7
    """An interaction shown when you're accepting a new quest. """
    PROGRESS_TAB = 8
    """Honestly, this doesn't seem consistent to me. It is used to give you choices in the Cryptarch as well as some reward prompts by the Eververse vendor. I'll have to look into that further at some point. """
    END = 9
    """These seem even less consistent. I don't know what these are. """
    START = 10
    """Also seem inconsistent. I also don't know what these are offhand. """


class DestinyItemSortType(BaseEnum):
    """
    Determines how items are sorted in an inventory bucket.
    """

    ITEM_ID = 0
    """_No description given by bungie_ """
    TIMESTAMP = 1
    """_No description given by bungie_ """
    STACK_SIZE = 2
    """_No description given by bungie_ """


class DestinyVendorItemRefundPolicy(BaseEnum):
    """
    The action that happens when the user attempts to refund an item.
    """

    NOT_REFUNDABLE = 0
    """_No description given by bungie_ """
    DELETES_ITEM = 1
    """_No description given by bungie_ """
    REVOKES_LICENSE = 2
    """_No description given by bungie_ """


class DestinyGatingScope(BaseEnum):
    """
    This enumeration represents the most restrictive type of gating that is being performed by an entity. This is useful as a shortcut to avoid a lot of lookups when determining whether the gating on an Entity applies to everyone equally, or to their specific Profile or Character states. None = There is no gating on this item. Global = The gating on this item is based entirely on global game state. It will be gated the same for everyone. Clan = The gating on this item is at the Clan level. For instance, if you're gated by Clan level this will be the case. Profile = The gating includes Profile-specific checks, but not on the Profile's characters. An example of this might be when you acquire an Emblem: the Emblem will be available in your Kiosk for all characters in your Profile from that point onward. Character = The gating includes Character-specific checks, including character level restrictions. An example of this might be an item that you can't purchase from a Vendor until you reach a specific Character Level. Item = The gating includes item-specific checks. For BNet, this generally implies that we'll show this data only on a character level or deeper. AssumedWorstCase = The unlocks and checks being used for this calculation are of an unknown type and are used for unknown purposes. For instance, if some great person decided that an unlock value should be globally scoped, but then the game changes it using character-specific data in a way that BNet doesn't know about. Because of the open-ended potential for this to occur, many unlock checks for "globally" scoped unlock data may be assumed as the worst case unless it has been specifically whitelisted as otherwise. That sucks, but them's the breaks.
    """

    NONE = 0
    """_No description given by bungie_ """
    GLOBAL = 1
    """_No description given by bungie_ """
    CLAN = 2
    """_No description given by bungie_ """
    PROFILE = 3
    """_No description given by bungie_ """
    CHARACTER = 4
    """_No description given by bungie_ """
    ITEM = 5
    """_No description given by bungie_ """
    ASSUMED_WORST_CASE = 6
    """_No description given by bungie_ """


class ActivityGraphNodeHighlightType(BaseEnum):
    """
    The various known UI styles in which an item can be highlighted. It'll be up to you to determine what you want to show based on this highlighting, BNet doesn't have any assets that correspond to these states. And yeah, RiseOfIron and Comet have their own special highlight states. Don't ask me, I can't imagine they're still used.
    """

    NONE = 0
    """_No description given by bungie_ """
    NORMAL = 1
    """_No description given by bungie_ """
    HYPER = 2
    """_No description given by bungie_ """
    COMET = 3
    """_No description given by bungie_ """
    RISE_OF_IRON = 4
    """_No description given by bungie_ """


class DestinyUnlockValueUIStyle(BaseEnum):
    """
    If you're showing an unlock value in the UI, this is the format in which it should be shown. You'll have to build your own algorithms on the client side to determine how best to render these options.
    """

    AUTOMATIC = 0
    """Generally, Automatic means "Just show the number" """
    FRACTION = 1
    """Show the number as a fractional value. For this to make sense, the value being displayed should have a comparable upper bound, like the progress to the next level of a Progression. """
    CHECKBOX = 2
    """Show the number as a checkbox. 0 Will mean unchecked, any other value will mean checked. """
    PERCENTAGE = 3
    """Show the number as a percentage. For this to make sense, the value being displayed should have a comparable upper bound, like the progress to the next level of a Progression. """
    DATE_TIME = 4
    """Show the number as a date and time. The number will be the number of seconds since the Unix Epoch (January 1st, 1970 at midnight UTC). It'll be up to you to convert this into a date and time format understandable to the user in their time zone. """
    FRACTION_FLOAT = 5
    """Show the number as a floating point value that represents a fraction, where 0 is min and 1 is max. For this to make sense, the value being displayed should have a comparable upper bound, like the progress to the next level of a Progression. """
    INTEGER = 6
    """Show the number as a straight-up integer. """
    TIME_DURATION = 7
    """Show the number as a time duration. The value will be returned as seconds. """
    HIDDEN = 8
    """Don't bother showing the value at all, it's not easily human-interpretable, and used for some internal purpose. """
    MULTIPLIER = 9
    """Example: "1.5x" """
    GREEN_PIPS = 10
    """Show the value as a series of green pips, like the wins in a Trials of Osiris score card. """
    RED_PIPS = 11
    """Show the value as a series of red pips, like the losses in a Trials of Osiris score card. """
    EXPLICIT_PERCENTAGE = 12
    """Show the value as a percentage. For example: "51%" - Does no division, only appends '%' """
    RAW_FLOAT = 13
    """Show the value as a floating-point number. For example: "4.52" NOTE: Passed along from Investment as whole number with last two digits as decimal values (452 -> 4.52) """
    LEVEL_AND_REWARD = 14
    """Show the value as a level and a reward. """


class DestinyObjectiveGrantStyle(BaseEnum):
    """
    Some Objectives provide perks, generally as part of providing some kind of interesting modifier for a Challenge or Quest. This indicates when the Perk is granted.
    """

    WHEN_INCOMPLETE = 0
    """_No description given by bungie_ """
    WHEN_COMPLETE = 1
    """_No description given by bungie_ """
    ALWAYS = 2
    """_No description given by bungie_ """


class DamageType(BaseEnum):
    """
    _No description given by bungie_
    """

    NONE = 0
    """_No description given by bungie_ """
    KINETIC = 1
    """_No description given by bungie_ """
    ARC = 2
    """_No description given by bungie_ """
    THERMAL = 3
    """_No description given by bungie_ """
    VOID = 4
    """_No description given by bungie_ """
    RAID = 5
    """_No description given by bungie_ """
    STASIS = 6
    """_No description given by bungie_ """


class DestinyObjectiveUiStyle(BaseEnum):
    """
    If the objective has a known UI label, this enumeration will represent it.
    """

    NONE = 0
    """_No description given by bungie_ """
    HIGHLIGHTED = 1
    """_No description given by bungie_ """
    CRAFTING_WEAPON_LEVEL = 2
    """_No description given by bungie_ """
    CRAFTING_WEAPON_LEVEL_PROGRESS = 3
    """_No description given by bungie_ """
    CRAFTING_WEAPON_TIMESTAMP = 4
    """_No description given by bungie_ """
    CRAFTING_MEMENTOS = 5
    """_No description given by bungie_ """
    CRAFTING_MEMENTO_TITLE = 6
    """_No description given by bungie_ """


class DestinyActivityNavPointType(BaseEnum):
    """
    _No description given by bungie_
    """

    INACTIVE = 0
    """_No description given by bungie_ """
    PRIMARY_OBJECTIVE = 1
    """_No description given by bungie_ """
    SECONDARY_OBJECTIVE = 2
    """_No description given by bungie_ """
    TRAVEL_OBJECTIVE = 3
    """_No description given by bungie_ """
    PUBLIC_EVENT_OBJECTIVE = 4
    """_No description given by bungie_ """
    AMMO_CACHE = 5
    """_No description given by bungie_ """
    POINT_TYPE_FLAG = 6
    """_No description given by bungie_ """
    CAPTURE_POINT = 7
    """_No description given by bungie_ """
    DEFENSIVE_ENCOUNTER = 8
    """_No description given by bungie_ """
    GHOST_INTERACTION = 9
    """_No description given by bungie_ """
    KILL_AI = 10
    """_No description given by bungie_ """
    QUEST_ITEM = 11
    """_No description given by bungie_ """
    PATROL_MISSION = 12
    """_No description given by bungie_ """
    INCOMING = 13
    """_No description given by bungie_ """
    ARENA_OBJECTIVE = 14
    """_No description given by bungie_ """
    AUTOMATION_HINT = 15
    """_No description given by bungie_ """
    TRACKED_QUEST = 16
    """_No description given by bungie_ """


class DestinyActivityModeCategory(BaseEnum):
    """
    Activity Modes are grouped into a few possible broad categories.
    """

    NONE = 0
    """Activities that are neither PVP nor PVE, such as social activities. """
    PV_E = 1
    """PvE activities, where you shoot aliens in the face. """
    PV_P = 2
    """PvP activities, where you shoot your "friends". """
    PV_E_COMPETITIVE = 3
    """PVE competitive activities, where you shoot whoever you want whenever you want. Or run around collecting small glowing triangles. """


class DestinyItemSubType(BaseEnum):
    """
    This Enumeration further classifies items by more specific categorizations than DestinyItemType. The "Sub-Type" is where we classify and categorize items one step further in specificity: "Auto Rifle" instead of just "Weapon" for example, or "Vanguard Bounty" instead of merely "Bounty". These sub-types are provided for historical compatibility with Destiny 1, but an ideal alternative is to use DestinyItemCategoryDefinitions and the DestinyItemDefinition.itemCategories property instead. Item Categories allow for arbitrary hierarchies of specificity, and for items to belong to multiple categories across multiple hierarchies simultaneously. For this enum, we pick a single type as a "best guess" fit. NOTE: This is not all of the item types available, and some of these are holdovers from Destiny 1 that may or may not still exist.
    """

    NONE = 0
    """_No description given by bungie_ """
    CRUCIBLE = 1
    """DEPRECATED. Items can be both "Crucible" and something else interesting. """
    VANGUARD = 2
    """DEPRECATED. An item can both be "Vanguard" and something else. """
    EXOTIC = 5
    """DEPRECATED. An item can both be Exotic and something else. """
    AUTO_RIFLE = 6
    """_No description given by bungie_ """
    SHOTGUN = 7
    """_No description given by bungie_ """
    MACHINEGUN = 8
    """_No description given by bungie_ """
    HAND_CANNON = 9
    """_No description given by bungie_ """
    ROCKET_LAUNCHER = 10
    """_No description given by bungie_ """
    FUSION_RIFLE = 11
    """_No description given by bungie_ """
    SNIPER_RIFLE = 12
    """_No description given by bungie_ """
    PULSE_RIFLE = 13
    """_No description given by bungie_ """
    SCOUT_RIFLE = 14
    """_No description given by bungie_ """
    CRM = 16
    """DEPRECATED. An item can both be CRM and something else. """
    SIDEARM = 17
    """_No description given by bungie_ """
    SWORD = 18
    """_No description given by bungie_ """
    MASK = 19
    """_No description given by bungie_ """
    SHADER = 20
    """_No description given by bungie_ """
    ORNAMENT = 21
    """_No description given by bungie_ """
    FUSION_RIFLE_LINE = 22
    """_No description given by bungie_ """
    GRENADE_LAUNCHER = 23
    """_No description given by bungie_ """
    SUBMACHINE_GUN = 24
    """_No description given by bungie_ """
    TRACE_RIFLE = 25
    """_No description given by bungie_ """
    HELMET_ARMOR = 26
    """_No description given by bungie_ """
    GAUNTLETS_ARMOR = 27
    """_No description given by bungie_ """
    CHEST_ARMOR = 28
    """_No description given by bungie_ """
    LEG_ARMOR = 29
    """_No description given by bungie_ """
    CLASS_ARMOR = 30
    """_No description given by bungie_ """
    BOW = 31
    """_No description given by bungie_ """
    DUMMY_REPEATABLE_BOUNTY = 32
    """_No description given by bungie_ """
    GLAIVE = 33
    """_No description given by bungie_ """


class DestinyGraphNodeState(BaseEnum):
    """
    Represents a potential state of an Activity Graph node.
    """

    HIDDEN = 0
    """_No description given by bungie_ """
    VISIBLE = 1
    """_No description given by bungie_ """
    TEASER = 2
    """_No description given by bungie_ """
    INCOMPLETE = 3
    """_No description given by bungie_ """
    COMPLETED = 4
    """_No description given by bungie_ """


class DestinyPresentationNodeType(BaseEnum):
    """
    _No description given by bungie_
    """

    DEFAULT = 0
    """_No description given by bungie_ """
    CATEGORY = 1
    """_No description given by bungie_ """
    COLLECTIBLES = 2
    """_No description given by bungie_ """
    RECORDS = 3
    """_No description given by bungie_ """
    METRIC = 4
    """_No description given by bungie_ """
    CRAFTABLE = 5
    """_No description given by bungie_ """


class DestinyScope(BaseEnum):
    """
    There's a lot of places where we need to know scope on more than just a profile or character level. For everything else, there's this more generic sense of scope.
    """

    PROFILE = 0
    """_No description given by bungie_ """
    CHARACTER = 1
    """_No description given by bungie_ """


class DestinyPresentationDisplayStyle(BaseEnum):
    """
    A hint for how the presentation node should be displayed when shown in a list. How you use this is your UI is up to you.
    """

    CATEGORY = 0
    """Display the item as a category, through which sub-items are filtered. """
    BADGE = 1
    """_No description given by bungie_ """
    MEDALS = 2
    """_No description given by bungie_ """
    COLLECTIBLE = 3
    """_No description given by bungie_ """
    RECORD = 4
    """_No description given by bungie_ """


class DestinyRecordValueStyle(BaseEnum):
    """
    _No description given by bungie_
    """

    INTEGER = 0
    """_No description given by bungie_ """
    PERCENTAGE = 1
    """_No description given by bungie_ """
    MILLISECONDS = 2
    """_No description given by bungie_ """
    BOOLEAN = 3
    """_No description given by bungie_ """
    DECIMAL = 4
    """_No description given by bungie_ """


class DestinyRecordToastStyle(BaseEnum):
    """
    _No description given by bungie_
    """

    NONE = 0
    """_No description given by bungie_ """
    RECORD = 1
    """_No description given by bungie_ """
    LORE = 2
    """_No description given by bungie_ """
    BADGE = 3
    """_No description given by bungie_ """
    META_RECORD = 4
    """_No description given by bungie_ """
    MEDAL_COMPLETE = 5
    """_No description given by bungie_ """
    SEASON_CHALLENGE_COMPLETE = 6
    """_No description given by bungie_ """
    GILDED_TITLE_COMPLETE = 7
    """_No description given by bungie_ """
    CRAFTING_RECIPE_UNLOCKED = 8
    """_No description given by bungie_ """


class DestinyPresentationScreenStyle(BaseEnum):
    """
    A hint for what screen should be shown when this presentation node is clicked into. How you use this is your UI is up to you.
    """

    DEFAULT = 0
    """Use the "default" view for the presentation nodes. """
    CATEGORY_SETS = 1
    """Show sub-items as "category sets". In-game, you'd see these as a vertical list of child presentation nodes - armor sets for example - and the icons of items within those sets displayed horizontally. """
    BADGE = 2
    """Show sub-items as Badges. (I know, I know. We don't need no stinkin' badges har har har) """


class PlugUiStyles(BaseEnum):
    """
    If the plug has a specific custom style, this enumeration will represent that style/those styles.
    """

    NONE = 0
    """_No description given by bungie_ """
    MASTERWORK = 1
    """_No description given by bungie_ """


class PlugAvailabilityMode(BaseEnum):
    """
    This enum determines whether the plug is available to be inserted. - Normal means that all existing rules for plug insertion apply. - UnavailableIfSocketContainsMatchingPlugCategory means that the plug is only available if the socket does NOT match the plug category. - AvailableIfSocketContainsMatchingPlugCategory means that the plug is only available if the socket DOES match the plug category. For category matching, use the plug's "plugCategoryIdentifier" property, comparing it to
    """

    NORMAL = 0
    """_No description given by bungie_ """
    UNAVAILABLE_IF_SOCKET_CONTAINS_MATCHING_PLUG_CATEGORY = 1
    """_No description given by bungie_ """
    AVAILABLE_IF_SOCKET_CONTAINS_MATCHING_PLUG_CATEGORY = 2
    """_No description given by bungie_ """


class DestinyEnergyType(BaseEnum):
    """
    Represents the socket energy types for Armor 2.0, Ghosts 2.0, and Stasis subclasses.
    """

    ANY = 0
    """_No description given by bungie_ """
    ARC = 1
    """_No description given by bungie_ """
    THERMAL = 2
    """_No description given by bungie_ """
    VOID = 3
    """_No description given by bungie_ """
    GHOST = 4
    """_No description given by bungie_ """
    SUBCLASS = 5
    """_No description given by bungie_ """
    STASIS = 6
    """_No description given by bungie_ """


class SocketPlugSources(BaseEnum):
    """
    Indicates how a socket is populated, and where you should look for valid plug data.  This is a flags enumeration/bitmask field, as you may have to look in multiple sources across multiple components for valid plugs.  For instance, a socket could have plugs that are sourced from its own definition, as well as plugs that are sourced from Character-scoped AND profile-scoped Plug Sets. Only by combining plug data for every indicated source will you be able to know all of the plugs available for a socket.
    """

    NONE = 0
    """If there's no way we can detect to insert new plugs. """
    INVENTORY_SOURCED = 1
    """Use plugs found in the player's inventory, based on the socket type rules (see DestinySocketTypeDefinition for more info) Note that a socket - like Shaders - can have *both* reusable plugs and inventory items inserted theoretically. """
    REUSABLE_PLUG_ITEMS = 2
    """Use the DestinyItemSocketsComponent.sockets.reusablePlugs property to determine which plugs are valid for this socket. This may have to be combined with other sources, such as plug sets, if those flags are set.  Note that "Reusable" plugs may not necessarily come from a plug set, nor from the "reusablePlugItems" in the socket's Definition data. They can sometimes be "randomized" in which case the only source of truth at the moment is still the runtime DestinyItemSocketsComponent.sockets.reusablePlugs property. """
    PROFILE_PLUG_SET = 4
    """Use the ProfilePlugSets (DestinyProfileResponse.profilePlugSets) component data to determine which plugs are valid for this socket. """
    CHARACTER_PLUG_SET = 8
    """Use the CharacterPlugSets (DestinyProfileResponse.characterPlugSets) component data to determine which plugs are valid for this socket. """


class ItemPerkVisibility(BaseEnum):
    """
    Indicates how a perk should be shown, or if it should be, in the game UI. Maybe useful for those of you trying to filter out internal-use-only perks (or for those of you trying to figure out what they do!)
    """

    VISIBLE = 0
    """_No description given by bungie_ """
    DISABLED = 1
    """_No description given by bungie_ """
    HIDDEN = 2
    """_No description given by bungie_ """


class SpecialItemType(BaseEnum):
    """
    As you run into items that need to be classified for Milestone purposes in ways that we cannot infer via direct data, add a new classification here and use a string constant to represent it in the local item config file. NOTE: This is not all of the item types available, and some of these are holdovers from Destiny 1 that may or may not still exist.
    """

    NONE = 0
    """_No description given by bungie_ """
    SPECIAL_CURRENCY = 1
    """_No description given by bungie_ """
    ARMOR = 8
    """_No description given by bungie_ """
    WEAPON = 9
    """_No description given by bungie_ """
    ENGRAM = 23
    """_No description given by bungie_ """
    CONSUMABLE = 24
    """_No description given by bungie_ """
    EXCHANGE_MATERIAL = 25
    """_No description given by bungie_ """
    MISSION_REWARD = 27
    """_No description given by bungie_ """
    CURRENCY = 29
    """_No description given by bungie_ """


class DestinyItemType(BaseEnum):
    """
    An enumeration that indicates the high-level "type" of the item, attempting to iron out the context specific differences for specific instances of an entity. For instance, though a weapon may be of various weapon "Types", in DestinyItemType they are all classified as "Weapon". This allows for better filtering on a higher level of abstraction for the concept of types.  This enum is provided for historical compatibility with Destiny 1, but an ideal alternative is to use DestinyItemCategoryDefinitions and the DestinyItemDefinition.itemCategories property instead. Item Categories allow for arbitrary hierarchies of specificity, and for items to belong to multiple categories across multiple hierarchies simultaneously. For this enum, we pick a single type as a "best guess" fit.  NOTE: This is not all of the item types available, and some of these are holdovers from Destiny 1 that may or may not still exist.  I keep updating these because they're so damn convenient. I guess I shouldn't fight it.
    """

    NONE = 0
    """_No description given by bungie_ """
    CURRENCY = 1
    """_No description given by bungie_ """
    ARMOR = 2
    """_No description given by bungie_ """
    WEAPON = 3
    """_No description given by bungie_ """
    MESSAGE = 7
    """_No description given by bungie_ """
    ENGRAM = 8
    """_No description given by bungie_ """
    CONSUMABLE = 9
    """_No description given by bungie_ """
    EXCHANGE_MATERIAL = 10
    """_No description given by bungie_ """
    MISSION_REWARD = 11
    """_No description given by bungie_ """
    QUEST_STEP = 12
    """_No description given by bungie_ """
    QUEST_STEP_COMPLETE = 13
    """_No description given by bungie_ """
    EMBLEM = 14
    """_No description given by bungie_ """
    QUEST = 15
    """_No description given by bungie_ """
    SUBCLASS = 16
    """_No description given by bungie_ """
    CLAN_BANNER = 17
    """_No description given by bungie_ """
    AURA = 18
    """_No description given by bungie_ """
    MOD = 19
    """_No description given by bungie_ """
    DUMMY = 20
    """_No description given by bungie_ """
    SHIP = 21
    """_No description given by bungie_ """
    VEHICLE = 22
    """_No description given by bungie_ """
    EMOTE = 23
    """_No description given by bungie_ """
    GHOST = 24
    """_No description given by bungie_ """
    PACKAGE = 25
    """_No description given by bungie_ """
    BOUNTY = 26
    """_No description given by bungie_ """
    WRAPPER = 27
    """_No description given by bungie_ """
    SEASONAL_ARTIFACT = 28
    """_No description given by bungie_ """
    FINISHER = 29
    """_No description given by bungie_ """
    PATTERN = 30
    """_No description given by bungie_ """


class DestinyBreakerType(BaseEnum):
    """
    A plug can optionally have a "Breaker Type": a special ability that can affect units in unique ways. Activating this plug can grant one of these types.
    """

    NONE = 0
    """_No description given by bungie_ """
    SHIELD_PIERCING = 1
    """_No description given by bungie_ """
    DISRUPTION = 2
    """_No description given by bungie_ """
    STAGGER = 3
    """_No description given by bungie_ """


class DestinyProgressionRewardItemAcquisitionBehavior(BaseEnum):
    """
    Represents the different kinds of acquisition behavior for progression reward items.
    """

    INSTANT = 0
    """_No description given by bungie_ """
    PLAYER_CLAIM_REQUIRED = 1
    """_No description given by bungie_ """


class ItemBindStatus(BaseEnum):
    """
    _No description given by bungie_
    """

    NOT_BOUND = 0
    """_No description given by bungie_ """
    BOUND_TO_CHARACTER = 1
    """_No description given by bungie_ """
    BOUND_TO_ACCOUNT = 2
    """_No description given by bungie_ """
    BOUND_TO_GUILD = 3
    """_No description given by bungie_ """


class TransferStatuses(BaseEnum):
    """
    Whether you can transfer an item, and why not if you can't.
    """

    CAN_TRANSFER = 0
    """The item can be transferred. """
    ITEM_IS_EQUIPPED = 1
    """You can't transfer the item because it is equipped on a character. """
    NOT_TRANSFERRABLE = 2
    """The item is defined as not transferrable in its DestinyInventoryItemDefinition.nonTransferrable property. """
    NO_ROOM_IN_DESTINATION = 4
    """You could transfer the item, but the place you're trying to put it has run out of room! Check your remaining Vault and/or character space. """


class ItemState(BaseEnum):
    """
    A flags enumeration/bitmask where each bit represents a different possible state that the item can be in that may effect how the item is displayed to the user and what actions can be performed against it.
    """

    NONE = 0
    """_No description given by bungie_ """
    LOCKED = 1
    """If this bit is set, the item has been "locked" by the user and cannot be deleted. You may want to represent this visually with a "lock" icon. """
    TRACKED = 2
    """If this bit is set, the item is a quest that's being tracked by the user. You may want a visual indicator to show that this is a tracked quest. """
    MASTERWORK = 4
    """If this bit is set, the item has a Masterwork plug inserted. This usually coincides with having a special "glowing" effect applied to the item's icon. """
    CRAFTED = 8
    """If this bit is set, the item has been 'crafted' by the player. You may want to represent this visually with a "crafted" icon overlay. """
    HIGHLIGHTED_OBJECTIVE = 16
    """If this bit is set, the item has a 'highlighted' objective. You may want to represent this with an orange-red icon border color. """


class DestinyGameVersions(BaseEnum):
    """
    A flags enumeration/bitmask indicating the versions of the game that a given user has purchased.
    """

    NONE = 0
    """_No description given by bungie_ """
    DESTINY2 = 1
    """_No description given by bungie_ """
    D_L_C1 = 2
    """_No description given by bungie_ """
    D_L_C2 = 4
    """_No description given by bungie_ """
    FORSAKEN = 8
    """_No description given by bungie_ """
    YEAR_TWO_ANNUAL_PASS = 16
    """_No description given by bungie_ """
    SHADOWKEEP = 32
    """_No description given by bungie_ """
    BEYOND_LIGHT = 64
    """_No description given by bungie_ """
    ANNIVERSARY30TH = 128
    """_No description given by bungie_ """
    THE_WITCH_QUEEN = 256
    """_No description given by bungie_ """


class DestinyComponentType(BaseEnum):
    """
    Represents the possible components that can be returned from Destiny "Get" calls such as GetProfile, GetCharacter, GetVendor etc... When making one of these requests, you will pass one or more of these components as a comma separated list in the "?components=" querystring parameter. For instance, if you want baseline Profile data, Character Data, and character progressions, you would pass "?components=Profiles,Characters,CharacterProgressions" You may use either the numerical or string values.
    """

    NONE = 0
    """_No description given by bungie_ """
    PROFILES = 100
    """Profiles is the most basic component, only relevant when calling GetProfile. This returns basic information about the profile, which is almost nothing: a list of characterIds, some information about the last time you logged in, and that most sobering statistic: how long you've played. """
    VENDOR_RECEIPTS = 101
    """Only applicable for GetProfile, this will return information about receipts for refundable vendor items. """
    PROFILE_INVENTORIES = 102
    """Asking for this will get you the profile-level inventories, such as your Vault buckets (yeah, the Vault is really inventory buckets located on your Profile) """
    PROFILE_CURRENCIES = 103
    """This will get you a summary of items on your Profile that we consider to be "currencies", such as Glimmer. I mean, if there's Glimmer in Destiny 2. I didn't say there was Glimmer. """
    PROFILE_PROGRESSION = 104
    """This will get you any progression-related information that exists on a Profile-wide level, across all characters. """
    PLATFORM_SILVER = 105
    """This will get you information about the silver that this profile has on every platform on which it plays.  You may only request this component for the logged in user's Profile, and will not recieve it if you request it for another Profile. """
    CHARACTERS = 200
    """This will get you summary info about each of the characters in the profile. """
    CHARACTER_INVENTORIES = 201
    """This will get you information about any non-equipped items on the character or character(s) in question, if you're allowed to see it. You have to either be authenticated as that user, or that user must allow anonymous viewing of their non-equipped items in Bungie.Net settings to actually get results. """
    CHARACTER_PROGRESSIONS = 202
    """This will get you information about the progression (faction, experience, etc... "levels") relevant to each character, if you are the currently authenticated user or the user has elected to allow anonymous viewing of its progression info. """
    CHARACTER_RENDER_DATA = 203
    """This will get you just enough information to be able to render the character in 3D if you have written a 3D rendering library for Destiny Characters, or "borrowed" ours. It's okay, I won't tell anyone if you're using it. I'm no snitch. (actually, we don't care if you use it - go to town) """
    CHARACTER_ACTIVITIES = 204
    """This will return info about activities that a user can see and gating on it, if you are the currently authenticated user or the user has elected to allow anonymous viewing of its progression info. Note that the data returned by this can be unfortunately problematic and relatively unreliable in some cases. We'll eventually work on making it more consistently reliable. """
    CHARACTER_EQUIPMENT = 205
    """This will return info about the equipped items on the character(s). Everyone can see this. """
    ITEM_INSTANCES = 300
    """This will return basic info about instanced items - whether they can be equipped, their tracked status, and some info commonly needed in many places (current damage type, primary stat value, etc) """
    ITEM_OBJECTIVES = 301
    """Items can have Objectives (DestinyObjectiveDefinition) bound to them. If they do, this will return info for items that have such bound objectives. """
    ITEM_PERKS = 302
    """Items can have perks (DestinyPerkDefinition). If they do, this will return info for what perks are active on items. """
    ITEM_RENDER_DATA = 303
    """If you just want to render the weapon, this is just enough info to do that rendering. """
    ITEM_STATS = 304
    """Items can have stats, like rate of fire. Asking for this component will return requested item's stats if they have stats. """
    ITEM_SOCKETS = 305
    """Items can have sockets, where plugs can be inserted. Asking for this component will return all info relevant to the sockets on items that have them. """
    ITEM_TALENT_GRIDS = 306
    """Items can have talent grids, though that matters a lot less frequently than it used to. Asking for this component will return all relevant info about activated Nodes and Steps on this talent grid, like the good ol' days. """
    ITEM_COMMON_DATA = 307
    """Items that *aren't* instanced still have important information you need to know: how much of it you have, the itemHash so you can look up their DestinyInventoryItemDefinition, whether they're locked, etc... Both instanced and non-instanced items will have these properties. You will get this automatically with Inventory components - you only need to pass this when calling GetItem on a specific item. """
    ITEM_PLUG_STATES = 308
    """Items that are "Plugs" can be inserted into sockets. This returns statuses about those plugs and why they can/can't be inserted. I hear you giggling, there's nothing funny about inserting plugs. Get your head out of the gutter and pay attention! """
    ITEM_PLUG_OBJECTIVES = 309
    """Sometimes, plugs have objectives on them. This data can get really large, so we split it into its own component. Please, don't grab it unless you need it. """
    ITEM_REUSABLE_PLUGS = 310
    """Sometimes, designers create thousands of reusable plugs and suddenly your response sizes are almost 3MB, and something has to give.  Reusable Plugs were split off as their own component, away from ItemSockets, as a result of the Plug changes in Shadowkeep that made plug data infeasibly large for the most common use cases.  Request this component if and only if you need to know what plugs *could* be inserted into a socket, and need to know it before "drilling" into the details of an item in your application (for instance, if you're doing some sort of interesting sorting or aggregation based on available plugs.  When you get this, you will also need to combine it with "Plug Sets" data if you want a full picture of all of the available plugs: this component will only return plugs that have state data that is per-item. See Plug Sets for available plugs that have Character, Profile, or no state-specific restrictions. """
    VENDORS = 400
    """When obtaining vendor information, this will return summary information about the Vendor or Vendors being returned. """
    VENDOR_CATEGORIES = 401
    """When obtaining vendor information, this will return information about the categories of items provided by the Vendor. """
    VENDOR_SALES = 402
    """When obtaining vendor information, this will return the information about items being sold by the Vendor. """
    KIOSKS = 500
    """Asking for this component will return you the account's Kiosk statuses: that is, what items have been filled out/acquired. But only if you are the currently authenticated user or the user has elected to allow anonymous viewing of its progression info. """
    CURRENCY_LOOKUPS = 600
    """A "shortcut" component that will give you all of the item hashes/quantities of items that the requested character can use to determine if an action (purchasing, socket insertion) has the required currency. (recall that all currencies are just items, and that some vendor purchases require items that you might not traditionally consider to be a "currency", like plugs/mods!) """
    PRESENTATION_NODES = 700
    """Returns summary status information about all "Presentation Nodes". See DestinyPresentationNodeDefinition for more details, but the gist is that these are entities used by the game UI to bucket Collectibles and Records into a hierarchy of categories. You may ask for and use this data if you want to perform similar bucketing in your own UI: or you can skip it and roll your own. """
    COLLECTIBLES = 800
    """Returns summary status information about all "Collectibles". These are records of what items you've discovered while playing Destiny, and some other basic information. For detailed information, you will have to call a separate endpoint devoted to the purpose. """
    RECORDS = 900
    """Returns summary status information about all "Records" (also known in the game as "Triumphs". I know, it's confusing because there's also "Moments of Triumph" that will themselves be represented as "Triumphs.") """
    TRANSITORY = 1000
    """Returns information that Bungie considers to be "Transitory": data that may change too frequently or come from a non-authoritative source such that we don't consider the data to be fully trustworthy, but that might prove useful for some limited use cases. We can provide no guarantee of timeliness nor consistency for this data: buyer beware with the Transitory component. """
    METRICS = 1100
    """Returns summary status information about all "Metrics" (also known in the game as "Stat Trackers"). """
    STRING_VARIABLES = 1200
    """Returns a mapping of localized string variable hashes to values, on a per-account or per-character basis. """
    CRAFTABLES = 1300
    """Returns summary status information about all "Craftables" aka crafting recipe items. """


class DestinyPresentationNodeState(BaseEnum):
    """
    I know this doesn't look like a Flags Enumeration/bitmask right now, but I assure you it is. This is the possible states that a Presentation Node can be in, and it is almost certain that its potential states will increase in the future. So don't treat it like a straight up enumeration.
    """

    NONE = 0
    """_No description given by bungie_ """
    INVISIBLE = 1
    """If this is set, the game recommends that you not show this node. But you know your life, do what you've got to do. """
    OBSCURED = 2
    """Turns out Presentation Nodes can also be obscured. If they are, this is set. """


class DestinyRecordState(BaseEnum):
    """
    A Flags enumeration/bitmask where each bit represents a possible state that a Record/Triumph can be in.
    """

    NONE = 0
    """If there are no flags set, the record is in a state where it *could* be redeemed, but it has not been yet. """
    RECORD_REDEEMED = 1
    """If this is set, the completed record has been redeemed. """
    REWARD_UNAVAILABLE = 2
    """If this is set, there's a reward available from this Record but it's unavailable for redemption. """
    OBJECTIVE_NOT_COMPLETED = 4
    """If this is set, the objective for this Record has not yet been completed. """
    OBSCURED = 8
    """If this is set, the game recommends that you replace the display text of this Record with DestinyRecordDefinition.stateInfo.obscuredString. """
    INVISIBLE = 16
    """If this is set, the game recommends that you not show this record. Do what you will with this recommendation. """
    ENTITLEMENT_UNOWNED = 32
    """If this is set, you can't complete this record because you lack some permission that's required to complete it. """
    CAN_EQUIP_TITLE = 64
    """If this is set, the record has a title (check DestinyRecordDefinition for title info) and you can equip it. """


class DestinyCollectibleState(BaseEnum):
    """
    A Flags Enumeration/bitmask where each bit represents a different state that the Collectible can be in. A collectible can be in any number of these states, and you can choose to use or ignore any or all of them when making your own UI that shows Collectible info. Our displays are going to honor them, but we're also the kind of people who only pretend to inhale before quickly passing it to the left. So, you know, do what you got to do. (All joking aside, please note the caveat I mention around the Invisible flag: there are cases where it is in the best interest of your users to honor these flags even if you're a "show all the data" person. Collector-oriented compulsion is a very unfortunate and real thing, and I would hate to instill that compulsion in others through showing them items that they cannot earn. Please consider this when you are making your own apps/sites.)
    """

    NONE = 0
    """_No description given by bungie_ """
    NOT_ACQUIRED = 1
    """If this flag is set, you have not yet obtained this collectible. """
    OBSCURED = 2
    """If this flag is set, the item is "obscured" to you: you can/should use the alternate item hash found in DestinyCollectibleDefinition.stateInfo.obscuredOverrideItemHash when displaying this collectible instead of the default display info. """
    INVISIBLE = 4
    """If this flag is set, the collectible should not be shown to the user. Please do consider honoring this flag. It is used - for example - to hide items that a person didn't get from the Eververse. I can't prevent these from being returned in definitions, because some people may have acquired them and thus they should show up: but I would hate for people to start feeling some variant of a Collector's Remorse about these items, and thus increasing their purchasing based on that compulsion. That would be a very unfortunate outcome, and one that I wouldn't like to see happen. So please, whether or not I'm your mom, consider honoring this flag and don't show people invisible collectibles. """
    CANNOT_AFFORD_MATERIAL_REQUIREMENTS = 8
    """If this flag is set, the collectible requires payment for creating an instance of the item, and you are lacking in currency. Bring the benjamins next time. Or spinmetal. Whatever. """
    INVENTORY_SPACE_UNAVAILABLE = 16
    """If this flag is set, you can't pull this item out of your collection because there's no room left in your inventory. """
    UNIQUENESS_VIOLATION = 32
    """If this flag is set, you already have one of these items and can't have a second one. """
    PURCHASE_DISABLED = 64
    """If this flag is set, the ability to pull this item out of your collection has been disabled. """


class DestinyPartyMemberStates(BaseEnum):
    """
    A flags enumeration that represents a Fireteam Member's status.
    """

    NONE = 0
    """_No description given by bungie_ """
    FIRETEAM_MEMBER = 1
    """This one's pretty obvious - they're on your Fireteam. """
    POSSE_MEMBER = 2
    """I don't know what it means to be in a 'Posse', but apparently this is it. """
    GROUP_MEMBER = 4
    """Nor do I understand the difference between them being in a 'Group' vs. a 'Fireteam'. I'll update these docs once I get more info. If I get more info. If you're reading this, I never got more info. You're on your own, kid. """
    PARTY_LEADER = 8
    """This person is the party leader. """


class DestinyGamePrivacySetting(BaseEnum):
    """
    A player can choose to restrict requests to join their Fireteam to specific states. These are the possible states a user can choose.
    """

    OPEN = 0
    """_No description given by bungie_ """
    CLAN_AND_FRIENDS_ONLY = 1
    """_No description given by bungie_ """
    FRIENDS_ONLY = 2
    """_No description given by bungie_ """
    INVITATION_ONLY = 3
    """_No description given by bungie_ """
    CLOSED = 4
    """_No description given by bungie_ """


class DestinyJoinClosedReasons(BaseEnum):
    """
    A Flags enumeration representing the reasons why a person can't join this user's fireteam.
    """

    NONE = 0
    """_No description given by bungie_ """
    IN_MATCHMAKING = 1
    """The user is currently in matchmaking. """
    LOADING = 2
    """The user is currently in a loading screen. """
    SOLO_MODE = 4
    """The user is in an activity that requires solo play. """
    INTERNAL_REASONS = 8
    """The user can't be joined for one of a variety of internal reasons. Basically, the game can't let you join at this time, but for reasons that aren't under the control of this user. """
    DISALLOWED_BY_GAME_STATE = 16
    """The user's current activity/quest/other transitory game state is preventing joining. """
    OFFLINE = 32768
    """The user appears to be offline. """


class DestinyRace(BaseEnum):
    """
    _No description given by bungie_
    """

    HUMAN = 0
    """_No description given by bungie_ """
    AWOKEN = 1
    """_No description given by bungie_ """
    EXO = 2
    """_No description given by bungie_ """
    UNKNOWN = 3
    """_No description given by bungie_ """


@attr.define
class DestinyActivity(BaseModel):
    """
    Represents the "Live" data that we can obtain about a Character's status with a specific Activity. This will tell you whether the character can participate in the activity, as well as some other basic mutable information.  Meant to be combined with static DestinyActivityDefinition data for a full picture of the Activity.

    Attributes:
        activity_hash: The hash identifier of the Activity. Use this to look up the DestinyActivityDefinition of the activity.
        is_new: If true, then the activity should have a "new" indicator in the Director UI.
        can_lead: If true, the user is allowed to lead a Fireteam into this activity.
        can_join: If true, the user is allowed to join with another Fireteam in this activity.
        is_completed: If true, we both have the ability to know that the user has completed this activity and they have completed it. Unfortunately, we can't necessarily know this for all activities. As such, this should probably only be used if you already know in advance which specific activities you wish to check.
        is_visible: If true, the user should be able to see this activity.
        display_level: The difficulty level of the activity, if applicable.
        recommended_light: The recommended light level for the activity, if applicable.
        difficulty_tier: A DestinyActivityDifficultyTier enum value indicating the difficulty of the activity.
        challenges: _No description given by bungie_
        modifier_hashes: If the activity has modifiers, this will be the list of modifiers that all variants have in common. Perform lookups against DestinyActivityModifierDefinition which defines the modifier being applied to get at the modifier data. Note that, in the DestiyActivityDefinition, you will see many more modifiers than this being referred to: those are all *possible* modifiers for the activity, not the active ones. Use only the active ones to match what's really live.
        boolean_activity_options: The set of activity options for this activity, keyed by an identifier that's unique for this activity (not guaranteed to be unique between or across all activities, though should be unique for every *variant* of a given *conceptual* activity: for instance, the original D2 Raid has many variant DestinyActivityDefinitions. While other activities could potentially have the same option hashes, for any given D2 base Raid variant the hash will be unique). As a concrete example of this data, the hashes you get for Raids will correspond to the currently active "Challenge Mode". We don't have any human readable information for these, but saavy 3rd party app users could manually associate the key (a hash identifier for the "option" that is enabled/disabled) and the value (whether it's enabled or disabled presently) On our side, we don't necessarily even know what these are used for (the game designers know, but we don't), and we have no human readable data for them. In order to use them, you will have to do some experimentation.
        loadout_requirement_index: If returned, this is the index into the DestinyActivityDefinition's "loadouts" property, indicating the currently active loadout requirements.
    """

    activity_hash: "DestinyActivityDefinition" = attr.field()
    is_new: bool = attr.field()
    can_lead: bool = attr.field()
    can_join: bool = attr.field()
    is_completed: bool = attr.field()
    is_visible: bool = attr.field()
    display_level: int = attr.field()
    recommended_light: int = attr.field()
    difficulty_tier: "DestinyActivityDifficultyTier" = attr.field()
    challenges: list["DestinyChallengeStatus"] = attr.field()
    modifier_hashes: list["DestinyActivityModifierDefinition"] = attr.field()
    boolean_activity_options: Any = attr.field()
    loadout_requirement_index: int = attr.field()


class DestinyActivityDifficultyTier(BaseEnum):
    """
    An enumeration representing the potential difficulty levels of an activity. Their names are... more qualitative than quantitative.
    """

    TRIVIAL = 0
    """_No description given by bungie_ """
    EASY = 1
    """_No description given by bungie_ """
    NORMAL = 2
    """_No description given by bungie_ """
    CHALLENGING = 3
    """_No description given by bungie_ """
    HARD = 4
    """_No description given by bungie_ """
    BRAVE = 5
    """_No description given by bungie_ """
    ALMOST_IMPOSSIBLE = 6
    """_No description given by bungie_ """
    IMPOSSIBLE = 7
    """_No description given by bungie_ """


@attr.define
class DestinyStat(BaseModel):
    """
    Represents a stat on an item *or* Character (NOT a Historical Stat, but a physical attribute stat like Attack, Defense etc...)

    Attributes:
        stat_hash: The hash identifier for the Stat. Use it to look up the DestinyStatDefinition for static data about the stat.
        value: The current value of the Stat.
    """

    stat_hash: "DestinyStatDefinition" = attr.field()
    value: int = attr.field()


class EquipFailureReason(BaseEnum):
    """
    The reasons why an item cannot be equipped, if any. Many flags can be set, or "None" if
    """

    NONE = 0
    """The item is/was able to be equipped. """
    ITEM_UNEQUIPPABLE = 1
    """This is not the kind of item that can be equipped. Did you try equipping Glimmer or something? """
    ITEM_UNIQUE_EQUIP_RESTRICTED = 2
    """This item is part of a "unique set", and you can't have more than one item of that same set type equipped at once. For instance, if you already have an Exotic Weapon equipped, you can't equip a second one in another weapon slot. """
    ITEM_FAILED_UNLOCK_CHECK = 4
    """This item has state-based gating that prevents it from being equipped in certain circumstances. For instance, an item might be for Warlocks only and you're a Titan, or it might require you to have beaten some special quest that you haven't beaten yet. Use the additional failure data passed on the item itself to get more information about what the specific failure case was (See DestinyInventoryItemDefinition and DestinyItemInstanceComponent) """
    ITEM_FAILED_LEVEL_CHECK = 8
    """This item requires you to have reached a specific character level in order to equip it, and you haven't reached that level yet. """
    ITEM_NOT_ON_CHARACTER = 16
    """This item can't be equipped on the character requested, because it must be in that character's inventory first. Transfer the item to the character you want to equip it before you attempt to equip it. """


@attr.define
class DestinyTalentNode(BaseModel):
    """
    I see you've come to find out more about Talent Nodes. I'm so sorry. Talent Nodes are the conceptual, visual nodes that appear on Talent Grids. Talent Grids, in Destiny 1, were found on almost every instanced item: they had Nodes that could be activated to change the properties of the item. In Destiny 2, Talent Grids only exist for Builds/Subclasses, and while the basic concept is the same (Nodes can be activated once you've gained sufficient Experience on the Item, and provide effects), there are some new concepts from Destiny 1. Examine DestinyTalentGridDefinition and its subordinates for more information. This is the "Live" information for the current status of a Talent Node on a specific item. Talent Nodes have many Steps, but only one can be active at any one time: and it is the Step that determines both the visual and the game state-changing properties that the Node provides. Examine this and DestinyTalentNodeStepDefinition carefully. *IMPORTANT NOTE* Talent Nodes are, unfortunately, Content Version DEPENDENT. Though they refer to hashes for Nodes and Steps, those hashes are not guaranteed to be immutable across content versions. This is a source of great exasperation for me, but as a result anyone using Talent Grid data must ensure that the content version of their static content matches that of the server responses before showing or making decisions based on talent grid data.

    Attributes:
        node_index: The index of the Talent Node being referred to (an index into DestinyTalentGridDefinition.nodes[]). CONTENT VERSION DEPENDENT.
        node_hash: The hash of the Talent Node being referred to (in DestinyTalentGridDefinition.nodes). Deceptively CONTENT VERSION DEPENDENT. We have no guarantee of the hash's immutability between content versions.
        state: An DestinyTalentNodeState enum value indicating the node's state: whether it can be activated or swapped, and why not if neither can be performed.
        is_activated: If true, the node is activated: it's current step then provides its benefits.
        step_index: The currently relevant Step for the node. It is this step that has rendering data for the node and the benefits that are provided if the node is activated. (the actual rules for benefits provided are extremely complicated in theory, but with how Talent Grids are being used in Destiny 2 you don't have to worry about a lot of those old Destiny 1 rules.) This is an index into: DestinyTalentGridDefinition.nodes[nodeIndex].steps[stepIndex]
        materials_to_upgrade: If the node has material requirements to be activated, this is the list of those requirements.
        activation_grid_level: The progression level required on the Talent Grid in order to be able to activate this talent node. Talent Grids have their own Progression - similar to Character Level, but in this case it is experience related to the item itself.
        progress_percent: If you want to show a progress bar or circle for how close this talent node is to being activate-able, this is the percentage to show. It follows the node's underlying rules about when the progress bar should first show up, and when it should be filled.
        hidden: Whether or not the talent node is actually visible in the game's UI. Whether you want to show it in your own UI is up to you! I'm not gonna tell you who to sock it to.
        node_stats_block: This property has some history. A talent grid can provide stats on both the item it's related to and the character equipping the item. This returns data about those stat bonuses.
    """

    node_index: int = attr.field()
    node_hash: int = attr.field()
    state: "DestinyTalentNodeState" = attr.field()
    is_activated: bool = attr.field()
    step_index: int = attr.field()
    materials_to_upgrade: list["DestinyMaterialRequirement"] = attr.field()
    activation_grid_level: int = attr.field()
    progress_percent: float = attr.field()
    hidden: bool = attr.field()
    node_stats_block: "DestinyTalentNodeStatBlock" = attr.field()


class DestinyTalentNodeState(BaseEnum):
    """
    _No description given by bungie_
    """

    INVALID = 0
    """_No description given by bungie_ """
    CAN_UPGRADE = 1
    """_No description given by bungie_ """
    NO_POINTS = 2
    """_No description given by bungie_ """
    NO_PREREQUISITES = 3
    """_No description given by bungie_ """
    NO_STEPS = 4
    """_No description given by bungie_ """
    NO_UNLOCK = 5
    """_No description given by bungie_ """
    NO_MATERIAL = 6
    """_No description given by bungie_ """
    NO_GRID_LEVEL = 7
    """_No description given by bungie_ """
    SWAPPING_LOCKED = 8
    """_No description given by bungie_ """
    MUST_SWAP = 9
    """_No description given by bungie_ """
    COMPLETE = 10
    """_No description given by bungie_ """
    UNKNOWN = 11
    """_No description given by bungie_ """
    CREATION_ONLY = 12
    """_No description given by bungie_ """
    HIDDEN = 13
    """_No description given by bungie_ """


@attr.define
class DestinyTalentNodeStatBlock(BaseModel):
    """
    This property has some history. A talent grid can provide stats on both the item it's related to and the character equipping the item. This returns data about those stat bonuses.

    Attributes:
        current_step_stats: The stat benefits conferred when this talent node is activated for the current Step that is active on the node.
        next_step_stats: This is a holdover from the old days of Destiny 1, when a node could be activated multiple times, conferring multiple steps worth of benefits: you would use this property to show what activating the "next" step on the node would provide vs. what the current step is providing. While Nodes are currently not being used this way, the underlying system for this functionality still exists. I hesitate to remove this property while the ability for designers to make such a talent grid still exists. Whether you want to show it is up to you.
    """

    current_step_stats: list["DestinyStat"] = attr.field()
    next_step_stats: list["DestinyStat"] = attr.field()


class DestinyVendorFilter(BaseEnum):
    """
    Indicates the type of filter to apply to Vendor results.
    """

    NONE = 0
    """_No description given by bungie_ """
    API_PURCHASABLE = 1
    """_No description given by bungie_ """


class VendorItemStatus(BaseEnum):
    """
    _No description given by bungie_
    """

    SUCCESS = 0
    """_No description given by bungie_ """
    NO_INVENTORY_SPACE = 1
    """_No description given by bungie_ """
    NO_FUNDS = 2
    """_No description given by bungie_ """
    NO_PROGRESSION = 4
    """_No description given by bungie_ """
    NO_UNLOCK = 8
    """_No description given by bungie_ """
    NO_QUANTITY = 16
    """_No description given by bungie_ """
    OUTSIDE_PURCHASE_WINDOW = 32
    """_No description given by bungie_ """
    NOT_AVAILABLE = 64
    """_No description given by bungie_ """
    UNIQUENESS_VIOLATION = 128
    """_No description given by bungie_ """
    UNKNOWN_ERROR = 256
    """_No description given by bungie_ """
    ALREADY_SELLING = 512
    """_No description given by bungie_ """
    UNSELLABLE = 1024
    """_No description given by bungie_ """
    SELLING_INHIBITED = 2048
    """_No description given by bungie_ """
    ALREADY_OWNED = 4096
    """_No description given by bungie_ """
    DISPLAY_ONLY = 8192
    """_No description given by bungie_ """


@attr.define
class DestinyUnlockStatus(BaseModel):
    """
    Indicates the status of an "Unlock Flag" on a Character or Profile. These are individual bits of state that can be either set or not set, and sometimes provide interesting human-readable information in their related DestinyUnlockDefinition.

    Attributes:
        unlock_hash: The hash identifier for the Unlock Flag. Use to lookup DestinyUnlockDefinition for static data. Not all unlocks have human readable data - in fact, most don't. But when they do, it can be very useful to show. Even if they don't have human readable data, you might be able to infer the meaning of an unlock flag with a bit of experimentation...
        is_set: Whether the unlock flag is set.
    """

    unlock_hash: "DestinyUnlockDefinition" = attr.field()
    is_set: bool = attr.field()


class DestinyVendorItemState(BaseEnum):
    """
    The possible states of Destiny Profile Records. IMPORTANT: Any given item can theoretically have many of these states simultaneously: as a result, this was altered to be a flags enumeration/bitmask for v3.2.0.
    """

    NONE = 0
    """There are no augments on the item. """
    INCOMPLETE = 1
    """Deprecated forever (probably). There was a time when Records were going to be implemented through Vendors, and this field was relevant. Now they're implemented through Presentation Nodes, and this field doesn't matter anymore. """
    REWARD_AVAILABLE = 2
    """Deprecated forever (probably). See the description of the "Incomplete" value for the juicy scoop. """
    COMPLETE = 4
    """Deprecated forever (probably). See the description of the "Incomplete" value for the juicy scoop. """
    NEW = 8
    """This item is considered to be "newly available", and should have some UI showing how shiny it is. """
    FEATURED = 16
    """This item is being "featured", and should be shiny in a different way from items that are merely new. """
    ENDING = 32
    """This item is only available for a limited time, and that time is approaching. """
    ON_SALE = 64
    """This item is "on sale". Get it while it's hot. """
    OWNED = 128
    """This item is already owned. """
    WIDE_VIEW = 256
    """This item should be shown with a "wide view" instead of normal icon view. """
    NEXUS_ATTENTION = 512
    """This indicates that you should show some kind of attention-requesting indicator on the item, in a similar manner to items in the nexus that have such notifications. """
    SET_DISCOUNT = 1024
    """This indicates that the item has some sort of a 'set' discount. """
    PRICE_DROP = 2048
    """This indicates that the item has a price drop. """
    DAILY_OFFER = 4096
    """This indicates that the item is a daily offer. """
    CHARITY = 8192
    """This indicates that the item is for charity. """
    SEASONAL_REWARD_EXPIRATION = 16384
    """This indicates that the item has a seasonal reward expiration. """
    BEST_DEAL = 32768
    """This indicates that the sale item is the best deal among different choices. """
    POPULAR = 65536
    """This indicates that the sale item is popular. """
    FREE = 131072
    """This indicates that the sale item is free. """
    LOCKED = 262144
    """This indicates that the sale item is locked. """


@attr.define
class DestinyEquipItemResults(BaseModel):
    """
    The results of a bulk Equipping operation performed through the Destiny API.

    Attributes:
        equip_results: _No description given by bungie_
    """

    equip_results: list["DestinyEquipItemResult"] = attr.field()


@attr.define
class DestinyEquipItemResult(BaseModel):
    """
    The results of an Equipping operation performed through the Destiny API.

    Attributes:
        item_instance_id: The instance ID of the item in question (all items that can be equipped must, but definition, be Instanced and thus have an Instance ID that you can use to refer to them)
        equip_status: A PlatformErrorCodes enum indicating whether it succeeded, and if it failed why.
    """

    item_instance_id: int = attr.field()
    equip_status: "PlatformErrorCodes" = attr.field()
