import datetime
from typing import TYPE_CHECKING, Any, Optional

import attr

from bungio.models.base import BaseEnum, BaseModel


@attr.define
class DestinyPostGameCarnageReportData(BaseModel):
    """
    Not specified.

    Attributes:
        period: Date and time for the activity.
        starting_phase_index: If this activity has "phases", this is the phase at which the activity was started. This value is only valid for activities before the Beyond Light expansion shipped. Subsequent activities will not have a valid value here.
        activity_was_started_from_beginning: True if the activity was started from the beginning, if that information is available and the activity was played post Witch Queen release.
        activity_details: Details about the activity.
        entries: Collection of players and their data for this activity.
        teams: Collection of stats for the player in this activity.
    """

    period: datetime.datetime = attr.field()
    starting_phase_index: int = attr.field()
    activity_was_started_from_beginning: bool = attr.field()
    activity_details: Any = attr.field()
    entries: list["DestinyPostGameCarnageReportEntry"] = attr.field()
    teams: list["DestinyPostGameCarnageReportTeamEntry"] = attr.field()


@attr.define
class DestinyHistoricalStatsActivity(BaseModel):
    """
        Summary information about the activity that was played.

        Attributes:
            reference_id: The unique hash identifier of the DestinyActivityDefinition that was played. If I had this to do over, it'd be named activityHash. Too late now.
            director_activity_hash: The unique hash identifier of the DestinyActivityDefinition that was played.
            instance_id: The unique identifier for this *specific* match that was played.

    This value can be used to get additional data about this activity such as who else was playing via the GetPostGameCarnageReport endpoint.
            mode: Indicates the most specific game mode of the activity that we could find.
            modes: The list of all Activity Modes to which this activity applies, including aggregates. This will let you see, for example, whether the activity was both Clash and part of the Trials of the Nine event.
            is_private: Whether or not the match was a private match.
            membership_type: The Membership Type indicating the platform on which this match was played.
    """

    reference_id: int = attr.field()
    director_activity_hash: int = attr.field()
    instance_id: int = attr.field()
    mode: int = attr.field()
    modes: list[int] = attr.field()
    is_private: bool = attr.field()
    membership_type: int = attr.field()


@attr.define
class DestinyPostGameCarnageReportEntry(BaseModel):
    """
    Not specified.

    Attributes:
        standing: Standing of the player
        score: Score of the player if available
        player: Identity details of the player
        character_id: ID of the player's character used in the activity.
        values: Collection of stats for the player in this activity.
        extended: Extended data extracted from the activity blob.
    """

    standing: int = attr.field()
    score: Any = attr.field()
    player: Any = attr.field()
    character_id: int = attr.field()
    values: Any = attr.field()
    extended: Any = attr.field()


@attr.define
class DestinyHistoricalStatsValue(BaseModel):
    """
    Not specified.

    Attributes:
        stat_id: Unique ID for this stat
        basic: Basic stat value.
        pga: Per game average for the statistic, if applicable
        weighted: Weighted value of the stat if a weight greater than 1 has been assigned.
        activity_id: When a stat represents the best, most, longest, fastest or some other personal best, the actual activity ID where that personal best was established is available on this property.
    """

    stat_id: str = attr.field()
    basic: Any = attr.field()
    pga: Any = attr.field()
    weighted: Any = attr.field()
    activity_id: int = attr.field()


@attr.define
class DestinyHistoricalStatsValuePair(BaseModel):
    """
    Not specified.

    Attributes:
        value: Raw value of the statistic
        display_value: Localized formated version of the value.
    """

    value: float = attr.field()
    display_value: str = attr.field()


@attr.define
class DestinyPlayer(BaseModel):
    """
    Not specified.

    Attributes:
        destiny_user_info: Details about the player as they are known in game (platform display name, Destiny emblem)
        character_class: Class of the character if applicable and available.
        class_hash: Not specified.
        race_hash: Not specified.
        gender_hash: Not specified.
        character_level: Level of the character if available. Zero if it is not available.
        light_level: Light Level of the character if available. Zero if it is not available.
        bungie_net_user_info: Details about the player as they are known on BungieNet. This will be undefined if the player has marked their credential private, or does not have a BungieNet account.
        clan_name: Current clan name for the player. This value may be null or an empty string if the user does not have a clan.
        clan_tag: Current clan tag for the player. This value may be null or an empty string if the user does not have a clan.
        emblem_hash: If we know the emblem's hash, this can be used to look up the player's emblem at the time of a match when receiving PGCR data, or otherwise their currently equipped emblem (if we are able to obtain it).
    """

    destiny_user_info: Any = attr.field()
    character_class: str = attr.field()
    class_hash: int = attr.field()
    race_hash: int = attr.field()
    gender_hash: int = attr.field()
    character_level: int = attr.field()
    light_level: int = attr.field()
    bungie_net_user_info: Any = attr.field()
    clan_name: str = attr.field()
    clan_tag: str = attr.field()
    emblem_hash: int = attr.field()


@attr.define
class DestinyPostGameCarnageReportExtendedData(BaseModel):
    """
    Not specified.

    Attributes:
        weapons: List of weapons and their perspective values.
        values: Collection of stats for the player in this activity.
    """

    weapons: list["DestinyHistoricalWeaponStats"] = attr.field()
    values: Any = attr.field()


@attr.define
class DestinyHistoricalWeaponStats(BaseModel):
    """
    Not specified.

    Attributes:
        reference_id: The hash ID of the item definition that describes the weapon.
        values: Collection of stats for the period.
    """

    reference_id: int = attr.field()
    values: Any = attr.field()


@attr.define
class DestinyPostGameCarnageReportTeamEntry(BaseModel):
    """
    Not specified.

    Attributes:
        team_id: Integer ID for the team.
        standing: Team's standing relative to other teams.
        score: Score earned by the team
        team_name: Alpha or Bravo
    """

    team_id: int = attr.field()
    standing: Any = attr.field()
    score: Any = attr.field()
    team_name: str = attr.field()


@attr.define
class DestinyLeaderboard(BaseModel):
    """
    Not specified.

    Attributes:
        stat_id: Not specified.
        entries: Not specified.
    """

    stat_id: str = attr.field()
    entries: list["DestinyLeaderboardEntry"] = attr.field()


@attr.define
class DestinyLeaderboardEntry(BaseModel):
    """
    Not specified.

    Attributes:
        rank: Where this player ranks on the leaderboard. A value of 1 is the top rank.
        player: Identity details of the player
        character_id: ID of the player's best character for the reported stat.
        value: Value of the stat for this player
    """

    rank: int = attr.field()
    player: Any = attr.field()
    character_id: int = attr.field()
    value: Any = attr.field()


@attr.define
class DestinyLeaderboardResults(BaseModel):
    """
    Not specified.

    Attributes:
        focus_membership_id: Indicate the membership ID of the account that is the focal point of the provided leaderboards.
        focus_character_id: Indicate the character ID of the character that is the focal point of the provided leaderboards. May be null, in which case any character from the focus membership can appear in the provided leaderboards.
    """

    focus_membership_id: int = attr.field()
    focus_character_id: int = attr.field()


@attr.define
class DestinyClanAggregateStat(BaseModel):
    """
    Not specified.

    Attributes:
        mode: The id of the mode of stats (allPvp, allPvE, etc)
        stat_id: The id of the stat
        value: Value of the stat for this player
    """

    mode: int = attr.field()
    stat_id: str = attr.field()
    value: Any = attr.field()


@attr.define
class DestinyHistoricalStatsByPeriod(BaseModel):
    """
    Not specified.

    Attributes:
        all_time: Not specified.
        all_time_tier1: Not specified.
        all_time_tier2: Not specified.
        all_time_tier3: Not specified.
        daily: Not specified.
        monthly: Not specified.
    """

    all_time: Any = attr.field()
    all_time_tier1: Any = attr.field()
    all_time_tier2: Any = attr.field()
    all_time_tier3: Any = attr.field()
    daily: list["DestinyHistoricalStatsPeriodGroup"] = attr.field()
    monthly: list["DestinyHistoricalStatsPeriodGroup"] = attr.field()


@attr.define
class DestinyHistoricalStatsPeriodGroup(BaseModel):
    """
    Not specified.

    Attributes:
        period: Period for the group. If the stat periodType is day, then this will have a specific day. If the type is monthly, then this value will be the first day of the applicable month. This value is not set when the periodType is 'all time'.
        activity_details: If the period group is for a specific activity, this property will be set.
        values: Collection of stats for the period.
    """

    period: datetime.datetime = attr.field()
    activity_details: Any = attr.field()
    values: Any = attr.field()


@attr.define
class DestinyHistoricalStatsAccountResult(BaseModel):
    """
    Not specified.

    Attributes:
        merged_deleted_characters: Not specified.
        merged_all_characters: Not specified.
        characters: Not specified.
    """

    merged_deleted_characters: "DestinyHistoricalStatsWithMerged" = attr.field()
    merged_all_characters: "DestinyHistoricalStatsWithMerged" = attr.field()
    characters: list["DestinyHistoricalStatsPerCharacter"] = attr.field()


@attr.define
class DestinyHistoricalStatsWithMerged(BaseModel):
    """
    Not specified.

    Attributes:
        results: Not specified.
        merged: Not specified.
    """

    results: Any = attr.field()
    merged: "DestinyHistoricalStatsByPeriod" = attr.field()


@attr.define
class DestinyHistoricalStatsPerCharacter(BaseModel):
    """
    Not specified.

    Attributes:
        character_id: Not specified.
        deleted: Not specified.
        results: Not specified.
        merged: Not specified.
    """

    character_id: int = attr.field()
    deleted: bool = attr.field()
    results: Any = attr.field()
    merged: "DestinyHistoricalStatsByPeriod" = attr.field()


@attr.define
class DestinyActivityHistoryResults(BaseModel):
    """
    Not specified.

    Attributes:
        activities: List of activities, the most recent activity first.
    """

    activities: list["DestinyHistoricalStatsPeriodGroup"] = attr.field()


@attr.define
class DestinyHistoricalWeaponStatsData(BaseModel):
    """
    Not specified.

    Attributes:
        weapons: List of weapons and their perspective values.
    """

    weapons: list["DestinyHistoricalWeaponStats"] = attr.field()


@attr.define
class DestinyAggregateActivityResults(BaseModel):
    """
    Not specified.

    Attributes:
        activities: List of all activities the player has participated in.
    """

    activities: list["DestinyAggregateActivityStats"] = attr.field()


@attr.define
class DestinyAggregateActivityStats(BaseModel):
    """
    Not specified.

    Attributes:
        activity_hash: Hash ID that can be looked up in the DestinyActivityTable.
        values: Collection of stats for the player in this activity.
    """

    activity_hash: int = attr.field()
    values: Any = attr.field()
