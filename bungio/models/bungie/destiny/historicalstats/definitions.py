import attr

from bungio.models.base import BaseEnum, BaseModel


class DestinyActivityModeType(BaseEnum):
    """
    For historical reasons, this list will have both D1 and D2-relevant Activity Modes in it. Please don't take this to mean that some D1-only feature is coming back!
    """

    NONE = 0
    """_No description given_ """
    STORY = 2
    """_No description given_ """
    STRIKE = 3
    """_No description given_ """
    RAID = 4
    """_No description given_ """
    ALL_PV_P = 5
    """_No description given_ """
    PATROL = 6
    """_No description given_ """
    ALL_PV_E = 7
    """_No description given_ """
    RESERVED9 = 9
    """_No description given_ """
    CONTROL = 10
    """_No description given_ """
    RESERVED11 = 11
    """_No description given_ """
    CLASH = 12
    """Clash -> Destiny's name for Team Deathmatch. 4v4 combat, the team with the highest kills at the end of time wins. """
    RESERVED13 = 13
    """_No description given_ """
    CRIMSON_DOUBLES = 15
    """_No description given_ """
    NIGHTFALL = 16
    """_No description given_ """
    HEROIC_NIGHTFALL = 17
    """_No description given_ """
    ALL_STRIKES = 18
    """_No description given_ """
    IRON_BANNER = 19
    """_No description given_ """
    RESERVED20 = 20
    """_No description given_ """
    RESERVED21 = 21
    """_No description given_ """
    RESERVED22 = 22
    """_No description given_ """
    RESERVED24 = 24
    """_No description given_ """
    ALL_MAYHEM = 25
    """_No description given_ """
    RESERVED26 = 26
    """_No description given_ """
    RESERVED27 = 27
    """_No description given_ """
    RESERVED28 = 28
    """_No description given_ """
    RESERVED29 = 29
    """_No description given_ """
    RESERVED30 = 30
    """_No description given_ """
    SUPREMACY = 31
    """_No description given_ """
    PRIVATE_MATCHES_ALL = 32
    """_No description given_ """
    SURVIVAL = 37
    """_No description given_ """
    COUNTDOWN = 38
    """_No description given_ """
    TRIALS_OF_THE_NINE = 39
    """_No description given_ """
    SOCIAL = 40
    """_No description given_ """
    TRIALS_COUNTDOWN = 41
    """_No description given_ """
    TRIALS_SURVIVAL = 42
    """_No description given_ """
    IRON_BANNER_CONTROL = 43
    """_No description given_ """
    IRON_BANNER_CLASH = 44
    """_No description given_ """
    IRON_BANNER_SUPREMACY = 45
    """_No description given_ """
    SCORED_NIGHTFALL = 46
    """_No description given_ """
    SCORED_HEROIC_NIGHTFALL = 47
    """_No description given_ """
    RUMBLE = 48
    """_No description given_ """
    ALL_DOUBLES = 49
    """_No description given_ """
    DOUBLES = 50
    """_No description given_ """
    PRIVATE_MATCHES_CLASH = 51
    """_No description given_ """
    PRIVATE_MATCHES_CONTROL = 52
    """_No description given_ """
    PRIVATE_MATCHES_SUPREMACY = 53
    """_No description given_ """
    PRIVATE_MATCHES_COUNTDOWN = 54
    """_No description given_ """
    PRIVATE_MATCHES_SURVIVAL = 55
    """_No description given_ """
    PRIVATE_MATCHES_MAYHEM = 56
    """_No description given_ """
    PRIVATE_MATCHES_RUMBLE = 57
    """_No description given_ """
    HEROIC_ADVENTURE = 58
    """_No description given_ """
    SHOWDOWN = 59
    """_No description given_ """
    LOCKDOWN = 60
    """_No description given_ """
    SCORCHED = 61
    """_No description given_ """
    SCORCHED_TEAM = 62
    """_No description given_ """
    GAMBIT = 63
    """_No description given_ """
    ALL_PV_E_COMPETITIVE = 64
    """_No description given_ """
    BREAKTHROUGH = 65
    """_No description given_ """
    BLACK_ARMORY_RUN = 66
    """_No description given_ """
    SALVAGE = 67
    """_No description given_ """
    IRON_BANNER_SALVAGE = 68
    """_No description given_ """
    PV_P_COMPETITIVE = 69
    """_No description given_ """
    PV_P_QUICKPLAY = 70
    """_No description given_ """
    CLASH_QUICKPLAY = 71
    """_No description given_ """
    CLASH_COMPETITIVE = 72
    """_No description given_ """
    CONTROL_QUICKPLAY = 73
    """_No description given_ """
    CONTROL_COMPETITIVE = 74
    """_No description given_ """
    GAMBIT_PRIME = 75
    """_No description given_ """
    RECKONING = 76
    """_No description given_ """
    MENAGERIE = 77
    """_No description given_ """
    VEX_OFFENSIVE = 78
    """_No description given_ """
    NIGHTMARE_HUNT = 79
    """_No description given_ """
    ELIMINATION = 80
    """_No description given_ """
    MOMENTUM = 81
    """_No description given_ """
    DUNGEON = 82
    """_No description given_ """
    SUNDIAL = 83
    """_No description given_ """
    TRIALS_OF_OSIRIS = 84
    """_No description given_ """
    DARES = 85
    """_No description given_ """
    OFFENSIVE = 86
    """_No description given_ """
    LOST_SECTOR = 87
    """_No description given_ """
    RIFT = 88
    """_No description given_ """
    ZONE_CONTROL = 89
    """_No description given_ """
    IRON_BANNER_RIFT = 90
    """_No description given_ """


@attr.define
class DestinyHistoricalStatsDefinition(BaseModel):
    """
    _No description given_

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
    """_No description given_ """
    GENERAL = 1
    """_No description given_ """
    WEAPONS = 2
    """_No description given_ """
    MEDALS = 3
    """_No description given_ """
    RESERVED_GROUPS = 100
    """This is purely to serve as the dividing line between filterable and un-filterable groups. Below this number is a group you can pass as a filter. Above it are groups used in very specific circumstances and not relevant for filtering. """
    LEADERBOARD = 101
    """Only applicable while generating leaderboards. """
    ACTIVITY = 102
    """These will *only* be consumed by GetAggregateStatsByActivity """
    UNIQUE_WEAPON = 103
    """These are only consumed and returned by GetUniqueWeaponHistory """
    INTERNAL = 104
    """_No description given_ """


class DestinyStatsCategoryType(BaseEnum):
    """
    _No description given_
    """

    NONE = 0
    """_No description given_ """
    KILLS = 1
    """_No description given_ """
    ASSISTS = 2
    """_No description given_ """
    DEATHS = 3
    """_No description given_ """
    CRITICALS = 4
    """_No description given_ """
    K_DA = 5
    """_No description given_ """
    K_D = 6
    """_No description given_ """
    SCORE = 7
    """_No description given_ """
    ENTERED = 8
    """_No description given_ """
    TIME_PLAYED = 9
    """_No description given_ """
    MEDAL_WINS = 10
    """_No description given_ """
    MEDAL_GAME = 11
    """_No description given_ """
    MEDAL_SPECIAL_KILLS = 12
    """_No description given_ """
    MEDAL_SPREES = 13
    """_No description given_ """
    MEDAL_MULTI_KILLS = 14
    """_No description given_ """
    MEDAL_ABILITIES = 15
    """_No description given_ """


class UnitType(BaseEnum):
    """
    _No description given_
    """

    NONE = 0
    """_No description given_ """
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
    _No description given_
    """

    ADD = 0
    """When collapsing multiple instances of the stat together, add the values. """
    MIN = 1
    """When collapsing multiple instances of the stat together, take the lower value. """
    MAX = 2
    """When collapsing multiple instances of the stat together, take the higher value. """


class PeriodType(BaseEnum):
    """
    _No description given_
    """

    NONE = 0
    """_No description given_ """
    DAILY = 1
    """_No description given_ """
    ALL_TIME = 2
    """_No description given_ """
    ACTIVITY = 3
    """_No description given_ """
