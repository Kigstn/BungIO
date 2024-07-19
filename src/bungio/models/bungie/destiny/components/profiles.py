# DO NOT CHANGE ANY CODE BELOW
# This file is generated automatically by `generate_api_schema.py` and will be overwritten
# Instead, change functions / models by subclassing them in the `./overwrites/` folder. They will be used instead.

from datetime import datetime
from typing import Optional, Union, TYPE_CHECKING

from bungio.utils import enum_converter
from bungio.models.base import BaseModel, custom_define, custom_field


if TYPE_CHECKING:
    from bungio.models import DestinyObjectiveDefinition
    from bungio.models import DestinyDestinationDefinition
    from bungio.models import DestinyLocationDefinition
    from bungio.models import DestinyGamePrivacySetting
    from bungio.models import DestinyArtifactProfileScoped
    from bungio.models import DestinyPartyMemberStates
    from bungio.models import DestinyJoinClosedReasons
    from bungio.models import DestinyInventoryItemDefinition
    from bungio.models import DestinyActivityDefinition


@custom_define()
class DestinyProfileProgressionComponent(BaseModel):
    """
    The set of progression-related information that applies at a Profile-wide level for your Destiny experience. This differs from the Jimi Hendrix Experience because there's less guitars on fire. Yet. #spoileralert? This will include information such as Checklist info.

    None
    Attributes:
        checklists: The set of checklists that can be examined on a profile-wide basis, keyed by the hash identifier of the Checklist (DestinyChecklistDefinition) For each checklist returned, its value is itself a Dictionary keyed by the checklist's hash identifier with the value being a boolean indicating if it's been discovered yet.
        seasonal_artifact: Data related to your progress on the current season's artifact that is the same across characters.
    """

    checklists: dict[int, dict[int, bool]] = custom_field(metadata={"type": """dict[int, dict[int, bool]]"""})
    seasonal_artifact: "DestinyArtifactProfileScoped" = custom_field()


@custom_define()
class DestinyProfileTransitoryComponent(BaseModel):
    """
    This is an experimental set of data that Bungie considers to be "transitory" - information that may be useful for API users, but that is coming from a non-authoritative data source about information that could potentially change at a more frequent pace than Bungie.net will receive updates about it. This information is provided exclusively for convenience should any of it be useful to users: we provide no guarantees to the accuracy or timeliness of data that comes from this source. Know that this data can potentially be out-of-date or even wrong entirely if the user disconnected from the game or suddenly changed their status before we can receive refreshed data.

    Tip: Manifest Information
        This model has some attributes which can be filled with additional information found in the manifest (`manifest_...`).
        Without additional work, these attributes will be `None`, since they require additional requests and database lookups.

        To fill the manifest dependent attributes, either:

        - Run `await ThisClass.fetch_manifest_information()`, see [here](/API Reference/Models/base)
        - Set `Client.always_return_manifest_information` to `True`, see [here](/API Reference/client)

    Attributes:
        current_activity: If you are in an activity, this is some transitory info about the activity currently being played.
        joinability: Information about whether and what might prevent you from joining this person on a fireteam.
        last_orbited_destination_hash: The hash identifier for the DestinyDestinationDefinition of the last location you were orbiting when in orbit.
        party_members: If you have any members currently in your party, this is some (very) bare-bones information about those members.
        tracking: Information about tracked entities.
        manifest_last_orbited_destination_hash: Manifest information for `last_orbited_destination_hash`
    """

    current_activity: "DestinyProfileTransitoryCurrentActivity" = custom_field()
    joinability: "DestinyProfileTransitoryJoinability" = custom_field()
    last_orbited_destination_hash: int = custom_field()
    party_members: list["DestinyProfileTransitoryPartyMember"] = custom_field(
        metadata={"type": """list[DestinyProfileTransitoryPartyMember]"""}
    )
    tracking: list["DestinyProfileTransitoryTrackingEntry"] = custom_field(
        metadata={"type": """list[DestinyProfileTransitoryTrackingEntry]"""}
    )
    manifest_last_orbited_destination_hash: Optional["DestinyDestinationDefinition"] = custom_field(default=None)


@custom_define()
class DestinyProfileTransitoryPartyMember(BaseModel):
    """
    This is some bare minimum information about a party member in a Fireteam. Unfortunately, without great computational expense on our side we can only get at the data contained here. I'd like to give you a character ID for example, but we don't have it. But we do have these three pieces of information. May they help you on your quest to show meaningful data about current Fireteams. Notably, we don't and can't feasibly return info on characters. If you can, try to use just the data below for your UI and purposes. Only hit us with further queries if you absolutely must know the character ID of the currently playing character. Pretty please with sugar on top.

    Tip: Manifest Information
        This model has some attributes which can be filled with additional information found in the manifest (`manifest_...`).
        Without additional work, these attributes will be `None`, since they require additional requests and database lookups.

        To fill the manifest dependent attributes, either:

        - Run `await ThisClass.fetch_manifest_information()`, see [here](/API Reference/Models/base)
        - Set `Client.always_return_manifest_information` to `True`, see [here](/API Reference/client)

    Attributes:
        display_name: The player's last known display name.
        emblem_hash: The identifier for the DestinyInventoryItemDefinition of the player's emblem.
        membership_id: The Membership ID that matches the party member.
        status: A Flags Enumeration value indicating the states that the player is in relevant to being on a fireteam.
        manifest_emblem_hash: Manifest information for `emblem_hash`
    """

    display_name: str = custom_field()
    emblem_hash: int = custom_field()
    membership_id: int = custom_field(metadata={"int64": True})
    status: Union["DestinyPartyMemberStates", int] = custom_field(converter=enum_converter("DestinyPartyMemberStates"))
    manifest_emblem_hash: Optional["DestinyInventoryItemDefinition"] = custom_field(default=None)


@custom_define()
class DestinyProfileTransitoryCurrentActivity(BaseModel):
    """
    If you are playing in an activity, this is some information about it. Note that we cannot guarantee any of this resembles what ends up in the PGCR in any way. They are sourced by two entirely separate systems with their own logic, and the one we source this data from should be considered non-authoritative in comparison.

    None
    Attributes:
        end_time: If you're still in it but it "ended" (like when folks are dancing around the loot after they beat a boss), this is when the activity ended.
        highest_opposing_faction_score: If you have human opponents, this is the highest opposing team's score.
        number_of_opponents: This is how many human or poorly crafted aimbot opponents you have.
        number_of_players: This is how many human or poorly crafted aimbots are on your team.
        score: This is what our non-authoritative source thought the score was.
        start_time: When the activity started.
    """

    end_time: datetime = custom_field()
    highest_opposing_faction_score: float = custom_field()
    number_of_opponents: int = custom_field()
    number_of_players: int = custom_field()
    score: float = custom_field()
    start_time: datetime = custom_field()


@custom_define()
class DestinyProfileTransitoryJoinability(BaseModel):
    """
    Some basic information about whether you can be joined, how many slots are left etc. Note that this can change quickly, so it may not actually be useful. But perhaps it will be in some use cases?

    None
    Attributes:
        closed_reasons: Reasons why a person can't join this person's fireteam.
        open_slots: The number of slots still available on this person's fireteam.
        privacy_setting: Who the person is currently allowing invites from.
    """

    closed_reasons: Union["DestinyJoinClosedReasons", int] = custom_field(
        converter=enum_converter("DestinyJoinClosedReasons")
    )
    open_slots: int = custom_field()
    privacy_setting: Union["DestinyGamePrivacySetting", int] = custom_field(
        converter=enum_converter("DestinyGamePrivacySetting")
    )


@custom_define()
class DestinyProfileTransitoryTrackingEntry(BaseModel):
    """
    This represents a single "thing" being tracked by the player. This can point to many types of entities, but only a subset of them will actually have a valid hash identifier for whatever it is being pointed to. It's up to you to interpret what it means when various combinations of these entries have values being tracked.

    Tip: Manifest Information
        This model has some attributes which can be filled with additional information found in the manifest (`manifest_...`).
        Without additional work, these attributes will be `None`, since they require additional requests and database lookups.

        To fill the manifest dependent attributes, either:

        - Run `await ThisClass.fetch_manifest_information()`, see [here](/API Reference/Models/base)
        - Set `Client.always_return_manifest_information` to `True`, see [here](/API Reference/client)

    Attributes:
        activity_hash: OPTIONAL - If this is tracking the status of a DestinyActivityDefinition, this is the identifier for that activity.
        item_hash: OPTIONAL - If this is tracking the status of a DestinyInventoryItemDefinition, this is the identifier for that item.
        location_hash: OPTIONAL - If this is tracking a DestinyLocationDefinition, this is the identifier for that location.
        objective_hash: OPTIONAL - If this is tracking the status of a DestinyObjectiveDefinition, this is the identifier for that objective.
        questline_item_hash: OPTIONAL - If this is tracking the status of a quest, this is the identifier for the DestinyInventoryItemDefinition that containst that questline data.
        tracked_date: OPTIONAL - I've got to level with you, I don't really know what this is. Is it when you started tracking it? Is it only populated for tracked items that have time limits? I don't know, but we can get at it - when I get time to actually test what it is, I'll update this. In the meantime, bask in the mysterious data.
        manifest_activity_hash: Manifest information for `activity_hash`
        manifest_item_hash: Manifest information for `item_hash`
        manifest_location_hash: Manifest information for `location_hash`
        manifest_objective_hash: Manifest information for `objective_hash`
        manifest_questline_item_hash: Manifest information for `questline_item_hash`
    """

    activity_hash: int = custom_field()
    item_hash: int = custom_field()
    location_hash: int = custom_field()
    objective_hash: int = custom_field()
    questline_item_hash: int = custom_field()
    tracked_date: datetime = custom_field()
    manifest_activity_hash: Optional["DestinyActivityDefinition"] = custom_field(default=None)
    manifest_item_hash: Optional["DestinyInventoryItemDefinition"] = custom_field(default=None)
    manifest_location_hash: Optional["DestinyLocationDefinition"] = custom_field(default=None)
    manifest_objective_hash: Optional["DestinyObjectiveDefinition"] = custom_field(default=None)
    manifest_questline_item_hash: Optional["DestinyInventoryItemDefinition"] = custom_field(default=None)
