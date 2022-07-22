# DO NOT CHANGE ANY CODE BELOW
# This file is generated automatically by `generate_api_schema.py` and will be overwritten
# Instead, change functions / models by subclassing them in the `./overwrites/` folder. They will be used instead.

from datetime import datetime
from typing import TYPE_CHECKING, Optional, Union

import attr

from bungio.models.base import BaseModel
from bungio.models.mixins import DestinyCharacterMixin
from bungio.utils import enum_converter

if TYPE_CHECKING:
    from bungio.models import (
        BungieMembershipType,
        DestinyActivity,
        DestinyActivityDefinition,
        DestinyActivityModeDefinition,
        DestinyActivityModeType,
        DestinyArtifactCharacterScoped,
        DestinyCharacterCustomization,
        DestinyCharacterPeerView,
        DestinyClass,
        DestinyClassDefinition,
        DestinyColor,
        DestinyFactionProgression,
        DestinyGender,
        DestinyGenderDefinition,
        DestinyInventoryItemDefinition,
        DestinyItemPerksComponent,
        DestinyMilestone,
        DestinyObjectiveProgress,
        DestinyProgression,
        DestinyQuestStatus,
        DestinyRace,
        DestinyRaceDefinition,
        DestinyRecordDefinition,
        DyeReference,
    )


@attr.define
class DestinyCharacterComponent(BaseModel, DestinyCharacterMixin):
    """
    This component contains base properties of the character. You'll probably want to always request this component, but hey you do you.

    Tip: Manifest Information
        This model has some attributes which can be filled with additional information found in the manifest (`manifest_...`).
        Without additional work, these attributes will be `None`, since they require additional requests and database lookups.

        To fill the manifest dependent attributes, either:

        - Run `await ThisClass.fetch_manifest_information()`, see [here](/API Reference/Models/base)
        - Set `Client.always_return_manifest_information` to `True`, see [here](/API Reference/client)

    Attributes:
        base_character_level: The "base" level of your character, not accounting for any light level.
        character_id: The unique identifier for the character.
        class_hash: Use this hash to look up the character's DestinyClassDefinition.
        class_type: Mostly for historical purposes at this point, this is an enumeration for the character's class. It'll be preferable in the general case to look up the related definition: but for some people this was too convenient to remove.
        date_last_played: The last date that the user played Destiny.
        emblem_background_path: A shortcut path to the user's currently equipped emblem background image. If you're just showing summary info for a user, this is more convenient than examining their equipped emblem and looking up the definition.
        emblem_color: A shortcut for getting the background color of the user's currently equipped emblem without having to do a DestinyInventoryItemDefinition lookup.
        emblem_hash: The hash of the currently equipped emblem for the user. Can be used to look up the DestinyInventoryItemDefinition.
        emblem_path: A shortcut path to the user's currently equipped emblem image. If you're just showing summary info for a user, this is more convenient than examining their equipped emblem and looking up the definition.
        gender_hash: Use this hash to look up the character's DestinyGenderDefinition.
        gender_type: Mostly for historical purposes at this point, this is an enumeration for the character's Gender. It'll be preferable in the general case to look up the related definition: but for some people this was too convenient to remove. And yeah, it's an enumeration and not a boolean. Fight me.
        level_progression: The progression that indicates your character's level. Not their light level, but their character level: you know, the thing you max out a couple hours in and then ignore for the sake of light level.
        light: The user's calculated "Light Level". Light level is an indicator of your power that mostly matters in the end game, once you've reached the maximum character level: it's a level that's dependent on the average Attack/Defense power of your items.
        membership_id: Every Destiny Profile has a membershipId. This is provided on the character as well for convenience.
        membership_type: membershipType tells you the platform on which the character plays. Examine the BungieMembershipType enumeration for possible values.
        minutes_played_this_session: If the user is currently playing, this is how long they've been playing.
        minutes_played_total: If this value is 525,600, then they played Destiny for a year. Or they're a very dedicated Rent fan. Note that this includes idle time, not just time spent actually in activities shooting things.
        percent_to_next_level: A number between 0 and 100, indicating the whole and fractional % remaining to get to the next character level.
        race_hash: Use this hash to look up the character's DestinyRaceDefinition.
        race_type: Mostly for historical purposes at this point, this is an enumeration for the character's race. It'll be preferable in the general case to look up the related definition: but for some people this was too convenient to remove.
        stats: Your character's stats, such as Agility, Resilience, etc... *not* historical stats. You'll have to call a different endpoint for those.
        title_record_hash: If this Character has a title assigned to it, this is the identifier of the DestinyRecordDefinition that has that title information.
        manifest_class_hash: Manifest information for `class_hash`
        manifest_emblem_hash: Manifest information for `emblem_hash`
        manifest_gender_hash: Manifest information for `gender_hash`
        manifest_race_hash: Manifest information for `race_hash`
        manifest_title_record_hash: Manifest information for `title_record_hash`
    """

    base_character_level: int = attr.field()
    character_id: int = attr.field()
    class_hash: int = attr.field()
    class_type: Union["DestinyClass", int] = attr.field(converter=enum_converter("DestinyClass"))
    date_last_played: datetime = attr.field()
    emblem_background_path: str = attr.field()
    emblem_color: "DestinyColor" = attr.field()
    emblem_hash: int = attr.field()
    emblem_path: str = attr.field()
    gender_hash: int = attr.field()
    gender_type: Union["DestinyGender", int] = attr.field(converter=enum_converter("DestinyGender"))
    level_progression: "DestinyProgression" = attr.field()
    light: int = attr.field()
    membership_id: int = attr.field()
    membership_type: Union["BungieMembershipType", int] = attr.field(converter=enum_converter("BungieMembershipType"))
    minutes_played_this_session: int = attr.field()
    minutes_played_total: int = attr.field()
    percent_to_next_level: float = attr.field()
    race_hash: int = attr.field()
    race_type: Union["DestinyRace", int] = attr.field(converter=enum_converter("DestinyRace"))
    stats: dict[int, int] = attr.field(metadata={"type": """dict[int, int]"""})
    title_record_hash: int = attr.field()
    manifest_class_hash: Optional["DestinyClassDefinition"] = attr.field(default=None)
    manifest_emblem_hash: Optional["DestinyInventoryItemDefinition"] = attr.field(default=None)
    manifest_gender_hash: Optional["DestinyGenderDefinition"] = attr.field(default=None)
    manifest_race_hash: Optional["DestinyRaceDefinition"] = attr.field(default=None)
    manifest_title_record_hash: Optional["DestinyRecordDefinition"] = attr.field(default=None)


@attr.define
class DestinyCharacterProgressionComponent(BaseModel):
    """
    This component returns anything that could be considered "Progression" on a user: data where the user is gaining levels, reputation, completions, rewards, etc...

    None
    Attributes:
        checklists: The set of checklists that can be examined for this specific character, keyed by the hash identifier of the Checklist (DestinyChecklistDefinition) For each checklist returned, its value is itself a Dictionary keyed by the checklist's hash identifier with the value being a boolean indicating if it's been discovered yet.
        factions: A dictionary of all known Factions, keyed by the Faction's hash. It contains data about this character's status with the faction.
        milestones: Milestones are related to the simple progressions shown in the game, but return additional and hopefully helpful information for users about the specifics of the Milestone's status.
        progressions: A Dictionary of all known progressions for the Character, keyed by the Progression's hash. Not all progressions have user-facing data, but those who do will have that data contained in the DestinyProgressionDefinition.
        quests: If the user has any active quests, the quests' statuses will be returned here.  Note that quests have been largely supplanted by Milestones, but that doesn't mean that they won't make a comeback independent of milestones at some point.  (Fun fact: quests came back as I feared they would, but we never looped back to populate this... I'm going to put that in the backlog.)
        seasonal_artifact: Data related to your progress on the current season's artifact that can vary per character.
        uninstanced_item_objectives: Sometimes, you have items in your inventory that don't have instances, but still have Objective information. This provides you that objective information for uninstanced items.  This dictionary is keyed by the item's hash: which you can use to look up the name and description for the overall task(s) implied by the objective. The value is the list of objectives for this item, and their statuses.
        uninstanced_item_perks: Sometimes, you have items in your inventory that don't have instances, but still have perks (for example: Trials passage cards). This gives you the perk information for uninstanced items. This dictionary is keyed by item hash, which you can use to look up the corresponding item definition. The value is the list of perks states for the item.
    """

    checklists: dict[int, dict[int, bool]] = attr.field(metadata={"type": """dict[int, dict[int, bool]]"""})
    factions: dict[int, "DestinyFactionProgression"] = attr.field(
        metadata={"type": """dict[int, DestinyFactionProgression]"""}
    )
    milestones: dict[int, "DestinyMilestone"] = attr.field(metadata={"type": """dict[int, DestinyMilestone]"""})
    progressions: dict[int, "DestinyProgression"] = attr.field(metadata={"type": """dict[int, DestinyProgression]"""})
    quests: list["DestinyQuestStatus"] = attr.field(metadata={"type": """list[DestinyQuestStatus]"""})
    seasonal_artifact: "DestinyArtifactCharacterScoped" = attr.field()
    uninstanced_item_objectives: dict[int, list["DestinyObjectiveProgress"]] = attr.field(
        metadata={"type": """dict[int, list[DestinyObjectiveProgress]]"""}
    )
    uninstanced_item_perks: dict[int, "DestinyItemPerksComponent"] = attr.field(
        metadata={"type": """dict[int, DestinyItemPerksComponent]"""}
    )


@attr.define
class DestinyCharacterRenderComponent(BaseModel):
    """
    Only really useful if you're attempting to render the character's current appearance in 3D, this returns a bare minimum of information, pre-aggregated, that you'll need to perform that rendering. Note that you need to combine this with other 3D assets and data from our servers. Examine the Javascript returned by https://bungie.net/sharedbundle/spasm to see how we use this data, but be warned: the rabbit hole goes pretty deep.

    None
    Attributes:
        custom_dyes: Custom dyes, calculated by iterating over the character's equipped items. Useful for pre-fetching all of the dye data needed from our server.
        customization: This is actually something that Spasm.js *doesn't* do right now, and that we don't return assets for yet. This is the data about what character customization options you picked. You can combine this with DestinyCharacterCustomizationOptionDefinition to show some cool info, and hopefully someday to actually render a user's face in 3D. We'll see if we ever end up with time for that.
        peer_view: A minimal view of: - Equipped items - The rendering-related custom options on those equipped items Combined, that should be enough to render all of the items on the equipped character.
    """

    custom_dyes: list["DyeReference"] = attr.field(metadata={"type": """list[DyeReference]"""})
    customization: "DestinyCharacterCustomization" = attr.field()
    peer_view: "DestinyCharacterPeerView" = attr.field()


@attr.define
class DestinyCharacterActivitiesComponent(BaseModel):
    """
    This component holds activity data for a character. It will tell you about the character's current activity status, as well as activities that are available to the user.

    Tip: Manifest Information
        This model has some attributes which can be filled with additional information found in the manifest (`manifest_...`).
        Without additional work, these attributes will be `None`, since they require additional requests and database lookups.

        To fill the manifest dependent attributes, either:

        - Run `await ThisClass.fetch_manifest_information()`, see [here](/API Reference/Models/base)
        - Set `Client.always_return_manifest_information` to `True`, see [here](/API Reference/client)

    Attributes:
        available_activities: The list of activities that the user can play.
        current_activity_hash: If the user is in an activity, this will be the hash of the Activity being played. Note that you must combine this info with currentActivityModeHash to get a real picture of what the user is doing right now. For instance, PVP "Activities" are just maps: it's the ActivityMode that determines what type of PVP game they're playing.
        current_activity_mode_hash: If the user is in an activity, this will be the hash of the activity mode being played. Combine with currentActivityHash to give a person a full picture of what they're doing right now.
        current_activity_mode_hashes: If the user is in an activity, this will be the hashes of the DestinyActivityModeDefinition being played. Combine with currentActivityHash to give a person a full picture of what they're doing right now.
        current_activity_mode_type: And the current activity's most specific mode type, if it can be found.
        current_activity_mode_types: All Activity Modes that apply to the current activity being played, in enum form.
        current_playlist_activity_hash: If the user is in a playlist, this is the hash identifier for the playlist that they chose.
        date_activity_started: The last date that the user started playing an activity.
        last_completed_story_hash: This will have the activity hash of the last completed story/campaign mission, in case you care about that.
        manifest_current_activity_hash: Manifest information for `current_activity_hash`
        manifest_current_activity_mode_hash: Manifest information for `current_activity_mode_hash`
        manifest_current_playlist_activity_hash: Manifest information for `current_playlist_activity_hash`
        manifest_last_completed_story_hash: Manifest information for `last_completed_story_hash`
    """

    available_activities: list["DestinyActivity"] = attr.field(metadata={"type": """list[DestinyActivity]"""})
    current_activity_hash: int = attr.field()
    current_activity_mode_hash: int = attr.field()
    current_activity_mode_hashes: list[int] = attr.field(metadata={"type": """list[int]"""})
    current_activity_mode_type: int = attr.field()
    current_activity_mode_types: list[Union["DestinyActivityModeType", int]] = attr.field(
        converter=enum_converter("DestinyActivityModeType")
    )
    current_playlist_activity_hash: int = attr.field()
    date_activity_started: datetime = attr.field()
    last_completed_story_hash: int = attr.field()
    manifest_current_activity_hash: Optional["DestinyActivityDefinition"] = attr.field(default=None)
    manifest_current_activity_mode_hash: Optional["DestinyActivityModeDefinition"] = attr.field(default=None)
    manifest_current_playlist_activity_hash: Optional["DestinyActivityDefinition"] = attr.field(default=None)
    manifest_last_completed_story_hash: Optional["DestinyActivityDefinition"] = attr.field(default=None)
