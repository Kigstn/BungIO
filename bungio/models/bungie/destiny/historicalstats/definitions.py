import datetime
from typing import TYPE_CHECKING, Any, Optional

import attr

from bungio.models.base import BaseEnum, BaseModel


class DestinyActivityModeType(BaseEnum):
    """
    For historical reasons, this list will have both D1 and D2-relevant Activity Modes in it. Please don't take this to mean that some D1-only feature is coming back!
    """

    NONE = 0
    """Not specified. """
    STORY = 2
    """Not specified. """
    STRIKE = 3
    """Not specified. """
    RAID = 4
    """Not specified. """
    ALL_PV_P = 5
    """Not specified. """
    PATROL = 6
    """Not specified. """
    ALL_PV_E = 7
    """Not specified. """
    RESERVED9 = 9
    """Not specified. """
    CONTROL = 10
    """Not specified. """
    RESERVED11 = 11
    """Not specified. """
    CLASH = 12
    """Clash -> Destiny's name for Team Deathmatch. 4v4 combat, the team with the highest kills at the end of time wins. """
    RESERVED13 = 13
    """Not specified. """
    CRIMSON_DOUBLES = 15
    """Not specified. """
    NIGHTFALL = 16
    """Not specified. """
    HEROIC_NIGHTFALL = 17
    """Not specified. """
    ALL_STRIKES = 18
    """Not specified. """
    IRON_BANNER = 19
    """Not specified. """
    RESERVED20 = 20
    """Not specified. """
    RESERVED21 = 21
    """Not specified. """
    RESERVED22 = 22
    """Not specified. """
    RESERVED24 = 24
    """Not specified. """
    ALL_MAYHEM = 25
    """Not specified. """
    RESERVED26 = 26
    """Not specified. """
    RESERVED27 = 27
    """Not specified. """
    RESERVED28 = 28
    """Not specified. """
    RESERVED29 = 29
    """Not specified. """
    RESERVED30 = 30
    """Not specified. """
    SUPREMACY = 31
    """Not specified. """
    PRIVATE_MATCHES_ALL = 32
    """Not specified. """
    SURVIVAL = 37
    """Not specified. """
    COUNTDOWN = 38
    """Not specified. """
    TRIALS_OF_THE_NINE = 39
    """Not specified. """
    SOCIAL = 40
    """Not specified. """
    TRIALS_COUNTDOWN = 41
    """Not specified. """
    TRIALS_SURVIVAL = 42
    """Not specified. """
    IRON_BANNER_CONTROL = 43
    """Not specified. """
    IRON_BANNER_CLASH = 44
    """Not specified. """
    IRON_BANNER_SUPREMACY = 45
    """Not specified. """
    SCORED_NIGHTFALL = 46
    """Not specified. """
    SCORED_HEROIC_NIGHTFALL = 47
    """Not specified. """
    RUMBLE = 48
    """Not specified. """
    ALL_DOUBLES = 49
    """Not specified. """
    DOUBLES = 50
    """Not specified. """
    PRIVATE_MATCHES_CLASH = 51
    """Not specified. """
    PRIVATE_MATCHES_CONTROL = 52
    """Not specified. """
    PRIVATE_MATCHES_SUPREMACY = 53
    """Not specified. """
    PRIVATE_MATCHES_COUNTDOWN = 54
    """Not specified. """
    PRIVATE_MATCHES_SURVIVAL = 55
    """Not specified. """
    PRIVATE_MATCHES_MAYHEM = 56
    """Not specified. """
    PRIVATE_MATCHES_RUMBLE = 57
    """Not specified. """
    HEROIC_ADVENTURE = 58
    """Not specified. """
    SHOWDOWN = 59
    """Not specified. """
    LOCKDOWN = 60
    """Not specified. """
    SCORCHED = 61
    """Not specified. """
    SCORCHED_TEAM = 62
    """Not specified. """
    GAMBIT = 63
    """Not specified. """
    ALL_PV_E_COMPETITIVE = 64
    """Not specified. """
    BREAKTHROUGH = 65
    """Not specified. """
    BLACK_ARMORY_RUN = 66
    """Not specified. """
    SALVAGE = 67
    """Not specified. """
    IRON_BANNER_SALVAGE = 68
    """Not specified. """
    PV_P_COMPETITIVE = 69
    """Not specified. """
    PV_P_QUICKPLAY = 70
    """Not specified. """
    CLASH_QUICKPLAY = 71
    """Not specified. """
    CLASH_COMPETITIVE = 72
    """Not specified. """
    CONTROL_QUICKPLAY = 73
    """Not specified. """
    CONTROL_COMPETITIVE = 74
    """Not specified. """
    GAMBIT_PRIME = 75
    """Not specified. """
    RECKONING = 76
    """Not specified. """
    MENAGERIE = 77
    """Not specified. """
    VEX_OFFENSIVE = 78
    """Not specified. """
    NIGHTMARE_HUNT = 79
    """Not specified. """
    ELIMINATION = 80
    """Not specified. """
    MOMENTUM = 81
    """Not specified. """
    DUNGEON = 82
    """Not specified. """
    SUNDIAL = 83
    """Not specified. """
    TRIALS_OF_OSIRIS = 84
    """Not specified. """
    DARES = 85
    """Not specified. """
    OFFENSIVE = 86
    """Not specified. """
    LOST_SECTOR = 87
    """Not specified. """
    RIFT = 88
    """Not specified. """
    ZONE_CONTROL = 89
    """Not specified. """
    IRON_BANNER_RIFT = 90
    """Not specified. """


@attr.define
class DestinyHistoricalStatsDefinition(BaseModel):
    """
    Not specified.

    Attributes:
        stat_id: Unique programmer friendly ID for this stat
        group: Statistic group
        period_types: Time periods the statistic covers
        modes: Game modes where this statistic can be reported.
        category: Category for the stat.
        stat_name: Display name
        stat_name_abbr: Display name abbreviated
        stat_description: Description of a stat if applicable.
        unit_type: Unit, if any, for the statistic
        icon_image: Optional URI to an icon for the statistic
        merge_method: Optional icon for the statistic
        unit_label: Localized Unit Name for the stat.
        weight: Weight assigned to this stat indicating its relative impressiveness.
        medal_tier_hash: The tier associated with this medal - be it implicitly or explicitly.
    """

    stat_id: str = attr.field()
    group: int = attr.field()
    period_types: list[int] = attr.field()
    modes: list[int] = attr.field()
    category: int = attr.field()
    stat_name: str = attr.field()
    stat_name_abbr: str = attr.field()
    stat_description: str = attr.field()
    unit_type: int = attr.field()
    icon_image: str = attr.field()
    merge_method: int = attr.field()
    unit_label: str = attr.field()
    weight: int = attr.field()
    medal_tier_hash: int = attr.field()


class DestinyStatsGroupType(BaseEnum):
    """
    If the enum value is > 100, it is a "special" group that cannot be queried for directly (special cases apply to when they are returned, and are not relevant in general cases)
    """

    NONE = 0
    """Not specified. """
    GENERAL = 1
    """Not specified. """
    WEAPONS = 2
    """Not specified. """
    MEDALS = 3
    """Not specified. """
    RESERVED_GROUPS = 100
    """This is purely to serve as the dividing line between filterable and un-filterable groups. Below this number is a group you can pass as a filter. Above it are groups used in very specific circumstances and not relevant for filtering. """
    LEADERBOARD = 101
    """Only applicable while generating leaderboards. """
    ACTIVITY = 102
    """These will *only* be consumed by GetAggregateStatsByActivity """
    UNIQUE_WEAPON = 103
    """These are only consumed and returned by GetUniqueWeaponHistory """
    INTERNAL = 104
    """Not specified. """


class DestinyStatsCategoryType(BaseEnum):
    """
    Not specified.
    """

    NONE = 0
    """Not specified. """
    KILLS = 1
    """Not specified. """
    ASSISTS = 2
    """Not specified. """
    DEATHS = 3
    """Not specified. """
    CRITICALS = 4
    """Not specified. """
    K_DA = 5
    """Not specified. """
    K_D = 6
    """Not specified. """
    SCORE = 7
    """Not specified. """
    ENTERED = 8
    """Not specified. """
    TIME_PLAYED = 9
    """Not specified. """
    MEDAL_WINS = 10
    """Not specified. """
    MEDAL_GAME = 11
    """Not specified. """
    MEDAL_SPECIAL_KILLS = 12
    """Not specified. """
    MEDAL_SPREES = 13
    """Not specified. """
    MEDAL_MULTI_KILLS = 14
    """Not specified. """
    MEDAL_ABILITIES = 15
    """Not specified. """


class UnitType(BaseEnum):
    """
    Not specified.
    """

    NONE = 0
    """Not specified. """
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
    Not specified.
    """

    ADD = 0
    """When collapsing multiple instances of the stat together, add the values. """
    MIN = 1
    """When collapsing multiple instances of the stat together, take the lower value. """
    MAX = 2
    """When collapsing multiple instances of the stat together, take the higher value. """


class PeriodType(BaseEnum):
    """
    Not specified.
    """

    NONE = 0
    """Not specified. """
    DAILY = 1
    """Not specified. """
    ALL_TIME = 2
    """Not specified. """
    ACTIVITY = 3
    """Not specified. """
