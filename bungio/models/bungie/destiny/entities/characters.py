import datetime
from typing import TYPE_CHECKING, Any

import attr

from bungio.models.base import BaseModel

if TYPE_CHECKING:
    from bungio.models import (
        DestinyActivity,
        DestinyArtifactCharacterScoped,
        DestinyCharacterCustomization,
        DestinyCharacterPeerView,
        DestinyColor,
        DestinyProgression,
        DestinyQuestStatus,
        DyeReference,
    )


@attr.define
class DestinyCharacterComponent(BaseModel):
    """
    This component contains base properties of the character. You'll probably want to always request this component, but hey you do you.

    Attributes:
        membership_id: Every Destiny Profile has a membershipId. This is provided on the character as well for convenience.
        membership_type: membershipType tells you the platform on which the character plays. Examine the BungieMembershipType enumeration for possible values.
        character_id: The unique identifier for the character.
        date_last_played: The last date that the user played Destiny.
        minutes_played_this_session: If the user is currently playing, this is how long they've been playing.
        minutes_played_total: If this value is 525,600, then they played Destiny for a year. Or they're a very dedicated Rent fan. Note that this includes idle time, not just time spent actually in activities shooting things.
        light: The user's calculated "Light Level". Light level is an indicator of your power that mostly matters in the end game, once you've reached the maximum character level: it's a level that's dependent on the average Attack/Defense power of your items.
        stats: Your character's stats, such as Agility, Resilience, etc... *not* historical stats. You'll have to call a different endpoint for those.
        race_hash: Use this hash to look up the character's DestinyRaceDefinition.
        gender_hash: Use this hash to look up the character's DestinyGenderDefinition.
        class_hash: Use this hash to look up the character's DestinyClassDefinition.
        race_type: Mostly for historical purposes at this point, this is an enumeration for the character's race. It'll be preferable in the general case to look up the related definition: but for some people this was too convenient to remove.
        class_type: Mostly for historical purposes at this point, this is an enumeration for the character's class. It'll be preferable in the general case to look up the related definition: but for some people this was too convenient to remove.
        gender_type: Mostly for historical purposes at this point, this is an enumeration for the character's Gender. It'll be preferable in the general case to look up the related definition: but for some people this was too convenient to remove. And yeah, it's an enumeration and not a boolean. Fight me.
        emblem_path: A shortcut path to the user's currently equipped emblem image. If you're just showing summary info for a user, this is more convenient than examining their equipped emblem and looking up the definition.
        emblem_background_path: A shortcut path to the user's currently equipped emblem background image. If you're just showing summary info for a user, this is more convenient than examining their equipped emblem and looking up the definition.
        emblem_hash: The hash of the currently equipped emblem for the user. Can be used to look up the DestinyInventoryItemDefinition.
        emblem_color: A shortcut for getting the background color of the user's currently equipped emblem without having to do a DestinyInventoryItemDefinition lookup.
        level_progression: The progression that indicates your character's level. Not their light level, but their character level: you know, the thing you max out a couple hours in and then ignore for the sake of light level.
        base_character_level: The "base" level of your character, not accounting for any light level.
        percent_to_next_level: A number between 0 and 100, indicating the whole and fractional % remaining to get to the next character level.
        title_record_hash: If this Character has a title assigned to it, this is the identifier of the DestinyRecordDefinition that has that title information.
    """

    membership_id: int = attr.field()
    membership_type: int = attr.field()
    character_id: int = attr.field()
    date_last_played: datetime.datetime = attr.field()
    minutes_played_this_session: int = attr.field()
    minutes_played_total: int = attr.field()
    light: int = attr.field()
    stats: Any = attr.field()
    race_hash: int = attr.field()
    gender_hash: int = attr.field()
    class_hash: int = attr.field()
    race_type: int = attr.field()
    class_type: int = attr.field()
    gender_type: int = attr.field()
    emblem_path: str = attr.field()
    emblem_background_path: str = attr.field()
    emblem_hash: int = attr.field()
    emblem_color: "DestinyColor" = attr.field()
    level_progression: "DestinyProgression" = attr.field()
    base_character_level: int = attr.field()
    percent_to_next_level: float = attr.field()
    title_record_hash: int = attr.field()


@attr.define
class DestinyCharacterProgressionComponent(BaseModel):
    """
    This component returns anything that could be considered "Progression" on a user: data where the user is gaining levels, reputation, completions, rewards, etc...

    Attributes:
        progressions: A Dictionary of all known progressions for the Character, keyed by the Progression's hash. Not all progressions have user-facing data, but those who do will have that data contained in the DestinyProgressionDefinition.
        factions: A dictionary of all known Factions, keyed by the Faction's hash. It contains data about this character's status with the faction.
        milestones: Milestones are related to the simple progressions shown in the game, but return additional and hopefully helpful information for users about the specifics of the Milestone's status.
        quests: If the user has any active quests, the quests' statuses will be returned here.  Note that quests have been largely supplanted by Milestones, but that doesn't mean that they won't make a comeback independent of milestones at some point.  (Fun fact: quests came back as I feared they would, but we never looped back to populate this... I'm going to put that in the backlog.)
        uninstanced_item_objectives: Sometimes, you have items in your inventory that don't have instances, but still have Objective information. This provides you that objective information for uninstanced items.  This dictionary is keyed by the item's hash: which you can use to look up the name and description for the overall task(s) implied by the objective. The value is the list of objectives for this item, and their statuses.
        uninstanced_item_perks: Sometimes, you have items in your inventory that don't have instances, but still have perks (for example: Trials passage cards). This gives you the perk information for uninstanced items. This dictionary is keyed by item hash, which you can use to look up the corresponding item definition. The value is the list of perks states for the item.
        checklists: The set of checklists that can be examined for this specific character, keyed by the hash identifier of the Checklist (DestinyChecklistDefinition) For each checklist returned, its value is itself a Dictionary keyed by the checklist's hash identifier with the value being a boolean indicating if it's been discovered yet.
        seasonal_artifact: Data related to your progress on the current season's artifact that can vary per character.
    """

    progressions: Any = attr.field()
    factions: Any = attr.field()
    milestones: Any = attr.field()
    quests: list["DestinyQuestStatus"] = attr.field()
    uninstanced_item_objectives: Any = attr.field()
    uninstanced_item_perks: Any = attr.field()
    checklists: Any = attr.field()
    seasonal_artifact: "DestinyArtifactCharacterScoped" = attr.field()


@attr.define
class DestinyCharacterRenderComponent(BaseModel):
    """
    Only really useful if you're attempting to render the character's current appearance in 3D, this returns a bare minimum of information, pre-aggregated, that you'll need to perform that rendering. Note that you need to combine this with other 3D assets and data from our servers. Examine the Javascript returned by https://bungie.net/sharedbundle/spasm to see how we use this data, but be warned: the rabbit hole goes pretty deep.

    Attributes:
        custom_dyes: Custom dyes, calculated by iterating over the character's equipped items. Useful for pre-fetching all of the dye data needed from our server.
        customization: This is actually something that Spasm.js *doesn't* do right now, and that we don't return assets for yet. This is the data about what character customization options you picked. You can combine this with DestinyCharacterCustomizationOptionDefinition to show some cool info, and hopefully someday to actually render a user's face in 3D. We'll see if we ever end up with time for that.
        peer_view: A minimal view of: - Equipped items - The rendering-related custom options on those equipped items Combined, that should be enough to render all of the items on the equipped character.
    """

    custom_dyes: list["DyeReference"] = attr.field()
    customization: "DestinyCharacterCustomization" = attr.field()
    peer_view: "DestinyCharacterPeerView" = attr.field()


@attr.define
class DestinyCharacterActivitiesComponent(BaseModel):
    """
    This component holds activity data for a character. It will tell you about the character's current activity status, as well as activities that are available to the user.

    Attributes:
        date_activity_started: The last date that the user started playing an activity.
        available_activities: The list of activities that the user can play.
        current_activity_hash: If the user is in an activity, this will be the hash of the Activity being played. Note that you must combine this info with currentActivityModeHash to get a real picture of what the user is doing right now. For instance, PVP "Activities" are just maps: it's the ActivityMode that determines what type of PVP game they're playing.
        current_activity_mode_hash: If the user is in an activity, this will be the hash of the activity mode being played. Combine with currentActivityHash to give a person a full picture of what they're doing right now.
        current_activity_mode_type: And the current activity's most specific mode type, if it can be found.
        current_activity_mode_hashes: If the user is in an activity, this will be the hashes of the DestinyActivityModeDefinition being played. Combine with currentActivityHash to give a person a full picture of what they're doing right now.
        current_activity_mode_types: All Activity Modes that apply to the current activity being played, in enum form.
        current_playlist_activity_hash: If the user is in a playlist, this is the hash identifier for the playlist that they chose.
        last_completed_story_hash: This will have the activity hash of the last completed story/campaign mission, in case you care about that.
    """

    date_activity_started: datetime.datetime = attr.field()
    available_activities: list["DestinyActivity"] = attr.field()
    current_activity_hash: int = attr.field()
    current_activity_mode_hash: int = attr.field()
    current_activity_mode_type: int = attr.field()
    current_activity_mode_hashes: list[int] = attr.field()
    current_activity_mode_types: list[int] = attr.field()
    current_playlist_activity_hash: int = attr.field()
    last_completed_story_hash: int = attr.field()
