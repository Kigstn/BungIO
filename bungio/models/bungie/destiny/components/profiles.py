import datetime
from typing import TYPE_CHECKING

import attr

from bungio.models.base import BaseModel

if TYPE_CHECKING:
    from bungio.models import (
        DestinyActivityDefinition,
        DestinyArtifactProfileScoped,
        DestinyChecklistDefinition,
        DestinyDestinationDefinition,
        DestinyGamePrivacySetting,
        DestinyInventoryItemDefinition,
        DestinyJoinClosedReasons,
        DestinyLocationDefinition,
        DestinyObjectiveDefinition,
        DestinyPartyMemberStates,
    )


@attr.define
class DestinyProfileProgressionComponent(BaseModel):
    """
    The set of progression-related information that applies at a Profile-wide level for your Destiny experience. This differs from the Jimi Hendrix Experience because there's less guitars on fire. Yet. #spoileralert? This will include information such as Checklist info.

    Attributes:
        checklists: The set of checklists that can be examined on a profile-wide basis, keyed by the hash identifier of the Checklist (DestinyChecklistDefinition) For each checklist returned, its value is itself a Dictionary keyed by the checklist's hash identifier with the value being a boolean indicating if it's been discovered yet.
        seasonal_artifact: Data related to your progress on the current season's artifact that is the same across characters.
    """

    checklists: "DestinyChecklistDefinition" = attr.field()
    seasonal_artifact: "DestinyArtifactProfileScoped" = attr.field()


@attr.define
class DestinyProfileTransitoryComponent(BaseModel):
    """
    This is an experimental set of data that Bungie considers to be "transitory" - information that may be useful for API users, but that is coming from a non-authoritative data source about information that could potentially change at a more frequent pace than Bungie.net will receive updates about it. This information is provided exclusively for convenience should any of it be useful to users: we provide no guarantees to the accuracy or timeliness of data that comes from this source. Know that this data can potentially be out-of-date or even wrong entirely if the user disconnected from the game or suddenly changed their status before we can receive refreshed data.

    Attributes:
        party_members: If you have any members currently in your party, this is some (very) bare-bones information about those members.
        current_activity: If you are in an activity, this is some transitory info about the activity currently being played.
        joinability: Information about whether and what might prevent you from joining this person on a fireteam.
        tracking: Information about tracked entities.
        last_orbited_destination_hash: The hash identifier for the DestinyDestinationDefinition of the last location you were orbiting when in orbit.
    """

    party_members: list["DestinyProfileTransitoryPartyMember"] = attr.field()
    current_activity: "DestinyProfileTransitoryCurrentActivity" = attr.field()
    joinability: "DestinyProfileTransitoryJoinability" = attr.field()
    tracking: list["DestinyProfileTransitoryTrackingEntry"] = attr.field()
    last_orbited_destination_hash: "DestinyDestinationDefinition" = attr.field()


@attr.define
class DestinyProfileTransitoryPartyMember(BaseModel):
    """
    This is some bare minimum information about a party member in a Fireteam. Unfortunately, without great computational expense on our side we can only get at the data contained here. I'd like to give you a character ID for example, but we don't have it. But we do have these three pieces of information. May they help you on your quest to show meaningful data about current Fireteams. Notably, we don't and can't feasibly return info on characters. If you can, try to use just the data below for your UI and purposes. Only hit us with further queries if you absolutely must know the character ID of the currently playing character. Pretty please with sugar on top.

    Attributes:
        membership_id: The Membership ID that matches the party member.
        emblem_hash: The identifier for the DestinyInventoryItemDefinition of the player's emblem.
        display_name: The player's last known display name.
        status: A Flags Enumeration value indicating the states that the player is in relevant to being on a fireteam.
    """

    membership_id: int = attr.field()
    emblem_hash: "DestinyInventoryItemDefinition" = attr.field()
    display_name: str = attr.field()
    status: "DestinyPartyMemberStates" = attr.field()


@attr.define
class DestinyProfileTransitoryCurrentActivity(BaseModel):
    """
    If you are playing in an activity, this is some information about it. Note that we cannot guarantee any of this resembles what ends up in the PGCR in any way. They are sourced by two entirely separate systems with their own logic, and the one we source this data from should be considered non-authoritative in comparison.

    Attributes:
        start_time: When the activity started.
        end_time: If you're still in it but it "ended" (like when folks are dancing around the loot after they beat a boss), this is when the activity ended.
        score: This is what our non-authoritative source thought the score was.
        highest_opposing_faction_score: If you have human opponents, this is the highest opposing team's score.
        number_of_opponents: This is how many human or poorly crafted aimbot opponents you have.
        number_of_players: This is how many human or poorly crafted aimbots are on your team.
    """

    start_time: datetime.datetime = attr.field()
    end_time: datetime.datetime = attr.field()
    score: float = attr.field()
    highest_opposing_faction_score: float = attr.field()
    number_of_opponents: int = attr.field()
    number_of_players: int = attr.field()


@attr.define
class DestinyProfileTransitoryJoinability(BaseModel):
    """
    Some basic information about whether you can be joined, how many slots are left etc. Note that this can change quickly, so it may not actually be useful. But perhaps it will be in some use cases?

    Attributes:
        open_slots: The number of slots still available on this person's fireteam.
        privacy_setting: Who the person is currently allowing invites from.
        closed_reasons: Reasons why a person can't join this person's fireteam.
    """

    open_slots: int = attr.field()
    privacy_setting: "DestinyGamePrivacySetting" = attr.field()
    closed_reasons: "DestinyJoinClosedReasons" = attr.field()


@attr.define
class DestinyProfileTransitoryTrackingEntry(BaseModel):
    """
    This represents a single "thing" being tracked by the player. This can point to many types of entities, but only a subset of them will actually have a valid hash identifier for whatever it is being pointed to. It's up to you to interpret what it means when various combinations of these entries have values being tracked.

    Attributes:
        location_hash: OPTIONAL - If this is tracking a DestinyLocationDefinition, this is the identifier for that location.
        item_hash: OPTIONAL - If this is tracking the status of a DestinyInventoryItemDefinition, this is the identifier for that item.
        objective_hash: OPTIONAL - If this is tracking the status of a DestinyObjectiveDefinition, this is the identifier for that objective.
        activity_hash: OPTIONAL - If this is tracking the status of a DestinyActivityDefinition, this is the identifier for that activity.
        questline_item_hash: OPTIONAL - If this is tracking the status of a quest, this is the identifier for the DestinyInventoryItemDefinition that containst that questline data.
        tracked_date: OPTIONAL - I've got to level with you, I don't really know what this is. Is it when you started tracking it? Is it only populated for tracked items that have time limits? I don't know, but we can get at it - when I get time to actually test what it is, I'll update this. In the meantime, bask in the mysterious data.
    """

    location_hash: "DestinyLocationDefinition" = attr.field()
    item_hash: "DestinyInventoryItemDefinition" = attr.field()
    objective_hash: "DestinyObjectiveDefinition" = attr.field()
    activity_hash: "DestinyActivityDefinition" = attr.field()
    questline_item_hash: "DestinyInventoryItemDefinition" = attr.field()
    tracked_date: datetime.datetime = attr.field()
