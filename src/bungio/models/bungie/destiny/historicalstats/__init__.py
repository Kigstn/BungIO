# DO NOT CHANGE ANY CODE BELOW
# This file is generated automatically by `generate_api_schema.py` and will be overwritten
# Instead, change functions / models by subclassing them in the `./overwrites/` folder. They will be used instead.

from datetime import datetime
from typing import Optional, Any, Union, TYPE_CHECKING

from bungio.utils import enum_converter
from bungio.models.base import BaseModel, BaseEnum, BaseFlagEnum, HashObject, ManifestModel, custom_define, custom_field


if TYPE_CHECKING:
    from bungio.models import DestinyActivityModeType
    from bungio.models import UserInfoCard
    from bungio.models import BungieMembershipType
    from bungio.models import DestinyHistoricalStatsPeriodGroup
    from bungio.models import DestinyClassDefinition
    from bungio.models import DestinyRaceDefinition
    from bungio.models import DestinyGenderDefinition
    from bungio.models import DestinyInventoryItemDefinition
    from bungio.models import DestinyActivityDefinition


@custom_define()
class DestinyPostGameCarnageReportData(BaseModel):
    """
    _No description given by bungie._

    None
    Attributes:
        activity_details: Details about the activity.
        activity_was_started_from_beginning: True if the activity was started from the beginning, if that information is available and the activity was played post Witch Queen release.
        entries: Collection of players and their data for this activity.
        period: Date and time for the activity.
        starting_phase_index: If this activity has "phases", this is the phase at which the activity was started. This value is only valid for activities before the Beyond Light expansion shipped. Subsequent activities will not have a valid value here.
        teams: Collection of stats for the player in this activity.
    """

    activity_details: "DestinyHistoricalStatsActivity" = custom_field()
    activity_was_started_from_beginning: bool = custom_field()
    entries: list["DestinyPostGameCarnageReportEntry"] = custom_field(
        metadata={"type": """list[DestinyPostGameCarnageReportEntry]"""}
    )
    period: datetime = custom_field()
    starting_phase_index: int = custom_field()
    teams: list["DestinyPostGameCarnageReportTeamEntry"] = custom_field(
        metadata={"type": """list[DestinyPostGameCarnageReportTeamEntry]"""}
    )


@custom_define()
class DestinyHistoricalStatsActivity(BaseModel):
    """
    Summary information about the activity that was played.

    Tip: Manifest Information
        This model has some attributes which can be filled with additional information found in the manifest (`manifest_...`).
        Without additional work, these attributes will be `None`, since they require additional requests and database lookups.

        To fill the manifest dependent attributes, either:

        - Run `await ThisClass.fetch_manifest_information()`, see [here](/API Reference/Models/base)
        - Set `Client.always_return_manifest_information` to `True`, see [here](/API Reference/client)

    Attributes:
        director_activity_hash: The unique hash identifier of the DestinyActivityDefinition that was played.
        instance_id: The unique identifier for this *specific* match that was played. This value can be used to get additional data about this activity such as who else was playing via the GetPostGameCarnageReport endpoint.
        is_private: Whether or not the match was a private match.
        membership_type: The Membership Type indicating the platform on which this match was played.
        mode: Indicates the most specific game mode of the activity that we could find.
        modes: The list of all Activity Modes to which this activity applies, including aggregates. This will let you see, for example, whether the activity was both Clash and part of the Trials of the Nine event.
        reference_id: The unique hash identifier of the DestinyActivityDefinition that was played. If I had this to do over, it'd be named activityHash. Too late now.
        manifest_director_activity_hash: Manifest information for `director_activity_hash`
        manifest_reference_id: Manifest information for `reference_id`
    """

    director_activity_hash: int = custom_field()
    instance_id: int = custom_field(metadata={"int64": True})
    is_private: bool = custom_field()
    membership_type: Union["BungieMembershipType", int] = custom_field(converter=enum_converter("BungieMembershipType"))
    mode: Union["DestinyActivityModeType", int] = custom_field(converter=enum_converter("DestinyActivityModeType"))
    modes: list[Union["DestinyActivityModeType", int]] = custom_field(
        converter=enum_converter("DestinyActivityModeType")
    )
    reference_id: int = custom_field()
    manifest_director_activity_hash: Optional["DestinyActivityDefinition"] = custom_field(default=None)
    manifest_reference_id: Optional["DestinyActivityDefinition"] = custom_field(default=None)


@custom_define()
class DestinyPostGameCarnageReportEntry(BaseModel):
    """
    _No description given by bungie._

    None
    Attributes:
        character_id: ID of the player's character used in the activity.
        extended: Extended data extracted from the activity blob.
        player: Identity details of the player
        score: Score of the player if available
        standing: Standing of the player
        values: Collection of stats for the player in this activity.
    """

    character_id: int = custom_field(metadata={"int64": True})
    extended: "DestinyPostGameCarnageReportExtendedData" = custom_field()
    player: "DestinyPlayer" = custom_field()
    score: "DestinyHistoricalStatsValue" = custom_field()
    standing: int = custom_field()
    values: dict[str, "DestinyHistoricalStatsValue"] = custom_field(
        metadata={"type": """dict[str, DestinyHistoricalStatsValue]"""}
    )


@custom_define()
class DestinyHistoricalStatsValue(BaseModel):
    """
    _No description given by bungie._

    None
    Attributes:
        activity_id: When a stat represents the best, most, longest, fastest or some other personal best, the actual activity ID where that personal best was established is available on this property.
        basic: Basic stat value.
        pga: Per game average for the statistic, if applicable
        stat_id: Unique ID for this stat
        weighted: Weighted value of the stat if a weight greater than 1 has been assigned.
    """

    activity_id: int = custom_field(metadata={"int64": True})
    basic: "DestinyHistoricalStatsValuePair" = custom_field()
    pga: "DestinyHistoricalStatsValuePair" = custom_field()
    stat_id: str = custom_field()
    weighted: "DestinyHistoricalStatsValuePair" = custom_field()


@custom_define()
class DestinyHistoricalStatsValuePair(BaseModel):
    """
    _No description given by bungie._

    None
    Attributes:
        display_value: Localized formated version of the value.
        value: Raw value of the statistic
    """

    display_value: str = custom_field()
    value: float = custom_field()


@custom_define()
class DestinyPlayer(BaseModel):
    """
    _No description given by bungie._

    Tip: Manifest Information
        This model has some attributes which can be filled with additional information found in the manifest (`manifest_...`).
        Without additional work, these attributes will be `None`, since they require additional requests and database lookups.

        To fill the manifest dependent attributes, either:

        - Run `await ThisClass.fetch_manifest_information()`, see [here](/API Reference/Models/base)
        - Set `Client.always_return_manifest_information` to `True`, see [here](/API Reference/client)

    Attributes:
        bungie_net_user_info: Details about the player as they are known on BungieNet. This will be undefined if the player has marked their credential private, or does not have a BungieNet account.
        character_class: Class of the character if applicable and available.
        character_level: Level of the character if available. Zero if it is not available.
        clan_name: Current clan name for the player. This value may be null or an empty string if the user does not have a clan.
        clan_tag: Current clan tag for the player. This value may be null or an empty string if the user does not have a clan.
        class_hash: _No description given by bungie._
        destiny_user_info: Details about the player as they are known in game (platform display name, Destiny emblem)
        emblem_hash: If we know the emblem's hash, this can be used to look up the player's emblem at the time of a match when receiving PGCR data, or otherwise their currently equipped emblem (if we are able to obtain it).
        gender_hash: _No description given by bungie._
        light_level: Light Level of the character if available. Zero if it is not available.
        race_hash: _No description given by bungie._
        manifest_class_hash: Manifest information for `class_hash`
        manifest_emblem_hash: Manifest information for `emblem_hash`
        manifest_gender_hash: Manifest information for `gender_hash`
        manifest_race_hash: Manifest information for `race_hash`
    """

    bungie_net_user_info: "UserInfoCard" = custom_field()
    character_class: str = custom_field()
    character_level: int = custom_field()
    clan_name: str = custom_field()
    clan_tag: str = custom_field()
    class_hash: int = custom_field()
    destiny_user_info: "UserInfoCard" = custom_field()
    emblem_hash: int = custom_field()
    gender_hash: int = custom_field()
    light_level: int = custom_field()
    race_hash: int = custom_field()
    manifest_class_hash: Optional["DestinyClassDefinition"] = custom_field(default=None)
    manifest_emblem_hash: Optional["DestinyInventoryItemDefinition"] = custom_field(default=None)
    manifest_gender_hash: Optional["DestinyGenderDefinition"] = custom_field(default=None)
    manifest_race_hash: Optional["DestinyRaceDefinition"] = custom_field(default=None)


@custom_define()
class DestinyPostGameCarnageReportExtendedData(BaseModel):
    """
    _No description given by bungie._

    None
    Attributes:
        values: Collection of stats for the player in this activity.
        weapons: List of weapons and their perspective values.
    """

    values: dict[str, "DestinyHistoricalStatsValue"] = custom_field(
        metadata={"type": """dict[str, DestinyHistoricalStatsValue]"""}
    )
    weapons: list["DestinyHistoricalWeaponStats"] = custom_field(
        metadata={"type": """list[DestinyHistoricalWeaponStats]"""}
    )


@custom_define()
class DestinyHistoricalWeaponStats(BaseModel):
    """
    _No description given by bungie._

    Tip: Manifest Information
        This model has some attributes which can be filled with additional information found in the manifest (`manifest_...`).
        Without additional work, these attributes will be `None`, since they require additional requests and database lookups.

        To fill the manifest dependent attributes, either:

        - Run `await ThisClass.fetch_manifest_information()`, see [here](/API Reference/Models/base)
        - Set `Client.always_return_manifest_information` to `True`, see [here](/API Reference/client)

    Attributes:
        reference_id: The hash ID of the item definition that describes the weapon.
        values: Collection of stats for the period.
        manifest_reference_id: Manifest information for `reference_id`
    """

    reference_id: int = custom_field()
    values: dict[str, "DestinyHistoricalStatsValue"] = custom_field(
        metadata={"type": """dict[str, DestinyHistoricalStatsValue]"""}
    )
    manifest_reference_id: Optional["DestinyInventoryItemDefinition"] = custom_field(default=None)


@custom_define()
class DestinyPostGameCarnageReportTeamEntry(BaseModel):
    """
    _No description given by bungie._

    None
    Attributes:
        score: Score earned by the team
        standing: Team's standing relative to other teams.
        team_id: Integer ID for the team.
        team_name: Alpha or Bravo
    """

    score: "DestinyHistoricalStatsValue" = custom_field()
    standing: "DestinyHistoricalStatsValue" = custom_field()
    team_id: int = custom_field()
    team_name: str = custom_field()


@custom_define()
class DestinyLeaderboard(BaseModel):
    """
    _No description given by bungie._

    None
    Attributes:
        entries: _No description given by bungie._
        stat_id: _No description given by bungie._
    """

    entries: list["DestinyLeaderboardEntry"] = custom_field(metadata={"type": """list[DestinyLeaderboardEntry]"""})
    stat_id: str = custom_field()


@custom_define()
class DestinyLeaderboardEntry(BaseModel):
    """
    _No description given by bungie._

    None
    Attributes:
        character_id: ID of the player's best character for the reported stat.
        player: Identity details of the player
        rank: Where this player ranks on the leaderboard. A value of 1 is the top rank.
        value: Value of the stat for this player
    """

    character_id: int = custom_field(metadata={"int64": True})
    player: "DestinyPlayer" = custom_field()
    rank: int = custom_field()
    value: "DestinyHistoricalStatsValue" = custom_field()


@custom_define()
class DestinyLeaderboardResults(BaseModel):
    """
    _No description given by bungie._

    None
    Attributes:
        focus_character_id: Indicate the character ID of the character that is the focal point of the provided leaderboards. May be null, in which case any character from the focus membership can appear in the provided leaderboards.
        focus_membership_id: Indicate the membership ID of the account that is the focal point of the provided leaderboards.
    """

    focus_character_id: int = custom_field(metadata={"int64": True})
    focus_membership_id: int = custom_field(metadata={"int64": True})


@custom_define()
class DestinyClanAggregateStat(BaseModel):
    """
    _No description given by bungie._

    None
    Attributes:
        mode: The id of the mode of stats (allPvp, allPvE, etc)
        stat_id: The id of the stat
        value: Value of the stat for this player
    """

    mode: Union["DestinyActivityModeType", int] = custom_field(converter=enum_converter("DestinyActivityModeType"))
    stat_id: str = custom_field()
    value: "DestinyHistoricalStatsValue" = custom_field()


@custom_define()
class DestinyHistoricalStatsByPeriod(BaseModel):
    """
    _No description given by bungie._

    None
    Attributes:
        all_time: _No description given by bungie._
        all_time_tier1: _No description given by bungie._
        all_time_tier2: _No description given by bungie._
        all_time_tier3: _No description given by bungie._
        daily: _No description given by bungie._
        monthly: _No description given by bungie._
    """

    all_time: dict[str, "DestinyHistoricalStatsValue"] = custom_field(
        metadata={"type": """dict[str, DestinyHistoricalStatsValue]"""}
    )
    all_time_tier1: dict[str, "DestinyHistoricalStatsValue"] = custom_field(
        metadata={"type": """dict[str, DestinyHistoricalStatsValue]"""}
    )
    all_time_tier2: dict[str, "DestinyHistoricalStatsValue"] = custom_field(
        metadata={"type": """dict[str, DestinyHistoricalStatsValue]"""}
    )
    all_time_tier3: dict[str, "DestinyHistoricalStatsValue"] = custom_field(
        metadata={"type": """dict[str, DestinyHistoricalStatsValue]"""}
    )
    daily: list["DestinyHistoricalStatsPeriodGroup"] = custom_field(
        metadata={"type": """list[DestinyHistoricalStatsPeriodGroup]"""}
    )
    monthly: list["DestinyHistoricalStatsPeriodGroup"] = custom_field(
        metadata={"type": """list[DestinyHistoricalStatsPeriodGroup]"""}
    )


@custom_define()
class OverwrittenDestinyHistoricalStatsPeriodGroup(BaseModel):
    """
    _No description given by bungie._

    None
    Attributes:
        activity_details: If the period group is for a specific activity, this property will be set.
        period: Period for the group. If the stat periodType is day, then this will have a specific day. If the type is monthly, then this value will be the first day of the applicable month. This value is not set when the periodType is 'all time'.
        values: Collection of stats for the period.
    """

    activity_details: "DestinyHistoricalStatsActivity" = custom_field()
    period: datetime = custom_field()
    values: dict[str, "DestinyHistoricalStatsValue"] = custom_field(
        metadata={"type": """dict[str, DestinyHistoricalStatsValue]"""}
    )


@custom_define()
class DestinyHistoricalStatsAccountResult(BaseModel):
    """
    _No description given by bungie._

    None
    Attributes:
        characters: _No description given by bungie._
        merged_all_characters: _No description given by bungie._
        merged_deleted_characters: _No description given by bungie._
    """

    characters: list["DestinyHistoricalStatsPerCharacter"] = custom_field(
        metadata={"type": """list[DestinyHistoricalStatsPerCharacter]"""}
    )
    merged_all_characters: "DestinyHistoricalStatsWithMerged" = custom_field()
    merged_deleted_characters: "DestinyHistoricalStatsWithMerged" = custom_field()


@custom_define()
class DestinyHistoricalStatsWithMerged(BaseModel):
    """
    _No description given by bungie._

    None
    Attributes:
        merged: _No description given by bungie._
        results: _No description given by bungie._
    """

    merged: "DestinyHistoricalStatsByPeriod" = custom_field()
    results: dict[str, "DestinyHistoricalStatsByPeriod"] = custom_field(
        metadata={"type": """dict[str, DestinyHistoricalStatsByPeriod]"""}
    )


@custom_define()
class DestinyHistoricalStatsPerCharacter(BaseModel):
    """
    _No description given by bungie._

    None
    Attributes:
        character_id: _No description given by bungie._
        deleted: _No description given by bungie._
        merged: _No description given by bungie._
        results: _No description given by bungie._
    """

    character_id: int = custom_field(metadata={"int64": True})
    deleted: bool = custom_field()
    merged: "DestinyHistoricalStatsByPeriod" = custom_field()
    results: dict[str, "DestinyHistoricalStatsByPeriod"] = custom_field(
        metadata={"type": """dict[str, DestinyHistoricalStatsByPeriod]"""}
    )


@custom_define()
class DestinyActivityHistoryResults(BaseModel):
    """
    _No description given by bungie._

    None
    Attributes:
        activities: List of activities, the most recent activity first.
    """

    activities: list["DestinyHistoricalStatsPeriodGroup"] = custom_field(
        metadata={"type": """list[DestinyHistoricalStatsPeriodGroup]"""}
    )


@custom_define()
class DestinyHistoricalWeaponStatsData(BaseModel):
    """
    _No description given by bungie._

    None
    Attributes:
        weapons: List of weapons and their perspective values.
    """

    weapons: list["DestinyHistoricalWeaponStats"] = custom_field(
        metadata={"type": """list[DestinyHistoricalWeaponStats]"""}
    )


@custom_define()
class DestinyAggregateActivityResults(BaseModel):
    """
    _No description given by bungie._

    None
    Attributes:
        activities: List of all activities the player has participated in.
    """

    activities: list["DestinyAggregateActivityStats"] = custom_field(
        metadata={"type": """list[DestinyAggregateActivityStats]"""}
    )


@custom_define()
class DestinyAggregateActivityStats(BaseModel):
    """
    _No description given by bungie._

    Tip: Manifest Information
        This model has some attributes which can be filled with additional information found in the manifest (`manifest_...`).
        Without additional work, these attributes will be `None`, since they require additional requests and database lookups.

        To fill the manifest dependent attributes, either:

        - Run `await ThisClass.fetch_manifest_information()`, see [here](/API Reference/Models/base)
        - Set `Client.always_return_manifest_information` to `True`, see [here](/API Reference/client)

    Attributes:
        activity_hash: Hash ID that can be looked up in the DestinyActivityTable.
        values: Collection of stats for the player in this activity.
        manifest_activity_hash: Manifest information for `activity_hash`
    """

    activity_hash: int = custom_field()
    values: dict[str, "DestinyHistoricalStatsValue"] = custom_field(
        metadata={"type": """dict[str, DestinyHistoricalStatsValue]"""}
    )
    manifest_activity_hash: Optional["DestinyActivityDefinition"] = custom_field(default=None)
