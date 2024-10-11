# DO NOT CHANGE ANY CODE BELOW
# This file is generated automatically by `generate_api_schema.py` and will be overwritten
# Instead, change functions / models by subclassing them in the `./overwrites/` folder. They will be used instead.

from typing import TYPE_CHECKING, Optional, Union

from bungio.models.base import BaseEnum, ManifestModel, custom_define, custom_field
from bungio.utils import enum_converter

if TYPE_CHECKING:
    from bungio.models import DestinyMedalTierDefinition


class DestinyActivityModeType(BaseEnum):
    """
    For historical reasons, this list will have both D1 and D2-relevant Activity Modes in it. Please don't take this to mean that some D1-only feature is coming back!
    """

    NONE = 0
    """_No description given by bungie._ """
    STORY = 2
    """_No description given by bungie._ """
    STRIKE = 3
    """_No description given by bungie._ """
    RAID = 4
    """_No description given by bungie._ """
    ALL_PV_P = 5
    """_No description given by bungie._ """
    PATROL = 6
    """_No description given by bungie._ """
    ALL_PV_E = 7
    """_No description given by bungie._ """
    RESERVED9 = 9
    """_No description given by bungie._ """
    CONTROL = 10
    """_No description given by bungie._ """
    RESERVED11 = 11
    """_No description given by bungie._ """
    CLASH = 12
    """Clash -> Destiny's name for Team Deathmatch. 4v4 combat, the team with the highest kills at the end of time wins. """
    RESERVED13 = 13
    """_No description given by bungie._ """
    CRIMSON_DOUBLES = 15
    """_No description given by bungie._ """
    NIGHTFALL = 16
    """_No description given by bungie._ """
    HEROIC_NIGHTFALL = 17
    """_No description given by bungie._ """
    ALL_STRIKES = 18
    """_No description given by bungie._ """
    IRON_BANNER = 19
    """_No description given by bungie._ """
    RESERVED20 = 20
    """_No description given by bungie._ """
    RESERVED21 = 21
    """_No description given by bungie._ """
    RESERVED22 = 22
    """_No description given by bungie._ """
    RESERVED24 = 24
    """_No description given by bungie._ """
    ALL_MAYHEM = 25
    """_No description given by bungie._ """
    RESERVED26 = 26
    """_No description given by bungie._ """
    RESERVED27 = 27
    """_No description given by bungie._ """
    RESERVED28 = 28
    """_No description given by bungie._ """
    RESERVED29 = 29
    """_No description given by bungie._ """
    RESERVED30 = 30
    """_No description given by bungie._ """
    SUPREMACY = 31
    """_No description given by bungie._ """
    PRIVATE_MATCHES_ALL = 32
    """_No description given by bungie._ """
    SURVIVAL = 37
    """_No description given by bungie._ """
    COUNTDOWN = 38
    """_No description given by bungie._ """
    TRIALS_OF_THE_NINE = 39
    """_No description given by bungie._ """
    SOCIAL = 40
    """_No description given by bungie._ """
    TRIALS_COUNTDOWN = 41
    """_No description given by bungie._ """
    TRIALS_SURVIVAL = 42
    """_No description given by bungie._ """
    IRON_BANNER_CONTROL = 43
    """_No description given by bungie._ """
    IRON_BANNER_CLASH = 44
    """_No description given by bungie._ """
    IRON_BANNER_SUPREMACY = 45
    """_No description given by bungie._ """
    SCORED_NIGHTFALL = 46
    """_No description given by bungie._ """
    SCORED_HEROIC_NIGHTFALL = 47
    """_No description given by bungie._ """
    RUMBLE = 48
    """_No description given by bungie._ """
    ALL_DOUBLES = 49
    """_No description given by bungie._ """
    DOUBLES = 50
    """_No description given by bungie._ """
    PRIVATE_MATCHES_CLASH = 51
    """_No description given by bungie._ """
    PRIVATE_MATCHES_CONTROL = 52
    """_No description given by bungie._ """
    PRIVATE_MATCHES_SUPREMACY = 53
    """_No description given by bungie._ """
    PRIVATE_MATCHES_COUNTDOWN = 54
    """_No description given by bungie._ """
    PRIVATE_MATCHES_SURVIVAL = 55
    """_No description given by bungie._ """
    PRIVATE_MATCHES_MAYHEM = 56
    """_No description given by bungie._ """
    PRIVATE_MATCHES_RUMBLE = 57
    """_No description given by bungie._ """
    HEROIC_ADVENTURE = 58
    """_No description given by bungie._ """
    SHOWDOWN = 59
    """_No description given by bungie._ """
    LOCKDOWN = 60
    """_No description given by bungie._ """
    SCORCHED = 61
    """_No description given by bungie._ """
    SCORCHED_TEAM = 62
    """_No description given by bungie._ """
    GAMBIT = 63
    """_No description given by bungie._ """
    ALL_PV_E_COMPETITIVE = 64
    """_No description given by bungie._ """
    BREAKTHROUGH = 65
    """_No description given by bungie._ """
    BLACK_ARMORY_RUN = 66
    """_No description given by bungie._ """
    SALVAGE = 67
    """_No description given by bungie._ """
    IRON_BANNER_SALVAGE = 68
    """_No description given by bungie._ """
    PV_P_COMPETITIVE = 69
    """_No description given by bungie._ """
    PV_P_QUICKPLAY = 70
    """_No description given by bungie._ """
    CLASH_QUICKPLAY = 71
    """_No description given by bungie._ """
    CLASH_COMPETITIVE = 72
    """_No description given by bungie._ """
    CONTROL_QUICKPLAY = 73
    """_No description given by bungie._ """
    CONTROL_COMPETITIVE = 74
    """_No description given by bungie._ """
    GAMBIT_PRIME = 75
    """_No description given by bungie._ """
    RECKONING = 76
    """_No description given by bungie._ """
    MENAGERIE = 77
    """_No description given by bungie._ """
    VEX_OFFENSIVE = 78
    """_No description given by bungie._ """
    NIGHTMARE_HUNT = 79
    """_No description given by bungie._ """
    ELIMINATION = 80
    """_No description given by bungie._ """
    MOMENTUM = 81
    """_No description given by bungie._ """
    DUNGEON = 82
    """_No description given by bungie._ """
    SUNDIAL = 83
    """_No description given by bungie._ """
    TRIALS_OF_OSIRIS = 84
    """_No description given by bungie._ """
    DARES = 85
    """_No description given by bungie._ """
    OFFENSIVE = 86
    """_No description given by bungie._ """
    LOST_SECTOR = 87
    """_No description given by bungie._ """
    RIFT = 88
    """_No description given by bungie._ """
    ZONE_CONTROL = 89
    """_No description given by bungie._ """
    IRON_BANNER_RIFT = 90
    """_No description given by bungie._ """
    IRON_BANNER_ZONE_CONTROL = 91
    """_No description given by bungie._ """
    RELIC = 92
    """_No description given by bungie._ """


@custom_define()
class DestinyHistoricalStatsDefinition(ManifestModel):
    """
    _No description given by bungie._

    Tip: Manifest Information
        This model has some attributes which can be filled with additional information found in the manifest (`manifest_...`).
        Without additional work, these attributes will be `None`, since they require additional requests and database lookups.

        To fill the manifest dependent attributes, either:

        - Run `await ThisClass.fetch_manifest_information()`, see [here](/API Reference/Models/base)
        - Set `Client.always_return_manifest_information` to `True`, see [here](/API Reference/client)

    Attributes:
        category: Category for the stat.
        group: Statistic group
        icon_image: Optional URI to an icon for the statistic
        medal_tier_hash: The tier associated with this medal - be it implicitly or explicitly.
        merge_method: Optional icon for the statistic
        modes: Game modes where this statistic can be reported.
        period_types: Time periods the statistic covers
        stat_description: Description of a stat if applicable.
        stat_id: Unique programmer friendly ID for this stat
        stat_name: Display name
        stat_name_abbr: Display name abbreviated
        unit_label: Localized Unit Name for the stat.
        unit_type: Unit, if any, for the statistic
        weight: Weight assigned to this stat indicating its relative impressiveness.
        manifest_medal_tier_hash: Manifest information for `medal_tier_hash`
    """

    category: Union["DestinyStatsCategoryType", int] = custom_field(
        converter=enum_converter("DestinyStatsCategoryType")
    )
    group: Union["DestinyStatsGroupType", int] = custom_field(converter=enum_converter("DestinyStatsGroupType"))
    icon_image: str = custom_field()
    medal_tier_hash: int = custom_field()
    merge_method: int = custom_field()
    modes: list[Union["DestinyActivityModeType", int]] = custom_field(
        converter=enum_converter("DestinyActivityModeType")
    )
    period_types: list[Union["PeriodType", int]] = custom_field(converter=enum_converter("PeriodType"))
    stat_description: str = custom_field()
    stat_id: str = custom_field()
    stat_name: str = custom_field()
    stat_name_abbr: str = custom_field()
    unit_label: str = custom_field()
    unit_type: Union["UnitType", int] = custom_field(converter=enum_converter("UnitType"))
    weight: int = custom_field()
    manifest_medal_tier_hash: Optional["DestinyMedalTierDefinition"] = custom_field(default=None)


class DestinyStatsGroupType(BaseEnum):
    """
    If the enum value is > 100, it is a "special" group that cannot be queried for directly (special cases apply to when they are returned, and are not relevant in general cases)
    """

    NONE = 0
    """_No description given by bungie._ """
    GENERAL = 1
    """_No description given by bungie._ """
    WEAPONS = 2
    """_No description given by bungie._ """
    MEDALS = 3
    """_No description given by bungie._ """
    RESERVED_GROUPS = 100
    """This is purely to serve as the dividing line between filterable and un-filterable groups. Below this number is a group you can pass as a filter. Above it are groups used in very specific circumstances and not relevant for filtering. """
    LEADERBOARD = 101
    """Only applicable while generating leaderboards. """
    ACTIVITY = 102
    """These will *only* be consumed by GetAggregateStatsByActivity """
    UNIQUE_WEAPON = 103
    """These are only consumed and returned by GetUniqueWeaponHistory """
    INTERNAL = 104
    """_No description given by bungie._ """


class DestinyStatsCategoryType(BaseEnum):
    """
    _No description given by bungie._
    """

    NONE = 0
    """_No description given by bungie._ """
    KILLS = 1
    """_No description given by bungie._ """
    ASSISTS = 2
    """_No description given by bungie._ """
    DEATHS = 3
    """_No description given by bungie._ """
    CRITICALS = 4
    """_No description given by bungie._ """
    K_DA = 5
    """_No description given by bungie._ """
    K_D = 6
    """_No description given by bungie._ """
    SCORE = 7
    """_No description given by bungie._ """
    ENTERED = 8
    """_No description given by bungie._ """
    TIME_PLAYED = 9
    """_No description given by bungie._ """
    MEDAL_WINS = 10
    """_No description given by bungie._ """
    MEDAL_GAME = 11
    """_No description given by bungie._ """
    MEDAL_SPECIAL_KILLS = 12
    """_No description given by bungie._ """
    MEDAL_SPREES = 13
    """_No description given by bungie._ """
    MEDAL_MULTI_KILLS = 14
    """_No description given by bungie._ """
    MEDAL_ABILITIES = 15
    """_No description given by bungie._ """


class UnitType(BaseEnum):
    """
    _No description given by bungie._
    """

    NONE = 0
    """_No description given by bungie._ """
    COUNT = 1
    """Indicates the statistic is a simple count of something. """
    PER_GAME = 2
    """Indicates the statistic is a per game average. """
    SECONDS = 3
    """Indicates the number of seconds """
    POINTS = 4
    """Indicates the number of points earned """
    TEAM = 5
    """Values represents a team ID """
    DISTANCE = 6
    """Values represents a distance (units to-be-determined) """
    PERCENT = 7
    """Ratio represented as a whole value from 0 to 100. """
    RATIO = 8
    """Ratio of something, shown with decimal places """
    BOOLEAN = 9
    """True or false """
    WEAPON_TYPE = 10
    """The stat is actually a weapon type. """
    STANDING = 11
    """Indicates victory, defeat, or something in between. """
    MILLISECONDS = 12
    """Number of milliseconds some event spanned. For example, race time, or lap time. """
    COMPLETION_REASON = 13
    """The value is a enumeration of the Completion Reason type. """


class DestinyStatsMergeMethod(BaseEnum):
    """
    _No description given by bungie._
    """

    ADD = 0
    """When collapsing multiple instances of the stat together, add the values. """
    MIN = 1
    """When collapsing multiple instances of the stat together, take the lower value. """
    MAX = 2
    """When collapsing multiple instances of the stat together, take the higher value. """


class PeriodType(BaseEnum):
    """
    _No description given by bungie._
    """

    NONE = 0
    """_No description given by bungie._ """
    DAILY = 1
    """_No description given by bungie._ """
    ALL_TIME = 2
    """_No description given by bungie._ """
    ACTIVITY = 3
    """_No description given by bungie._ """
