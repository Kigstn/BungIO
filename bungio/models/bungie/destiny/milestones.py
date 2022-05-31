import datetime
from typing import TYPE_CHECKING, Any

import attr

from bungio.models.base import BaseModel

if TYPE_CHECKING:
    from bungio.models import (
        DestinyChallengeStatus,
        DestinyMilestoneActivity,
        DestinyMilestoneActivityCompletionStatus,
        DestinyMilestoneActivityPhase,
        DestinyMilestoneActivityVariant,
        DestinyMilestoneChallengeActivity,
        DestinyMilestoneContentItemCategory,
        DestinyMilestoneQuest,
        DestinyMilestoneRewardCategory,
        DestinyMilestoneRewardEntry,
        DestinyMilestoneVendor,
        DestinyPublicMilestoneActivity,
        DestinyPublicMilestoneActivityVariant,
        DestinyPublicMilestoneChallenge,
        DestinyPublicMilestoneChallengeActivity,
        DestinyPublicMilestoneQuest,
        DestinyPublicMilestoneVendor,
        DestinyQuestStatus,
    )


@attr.define
class DestinyMilestone(BaseModel):
    """
    Represents a runtime instance of a user's milestone status. Live Milestone data should be combined with DestinyMilestoneDefinition data to show the user a picture of what is available for them to do in the game, and their status in regards to said "things to do." Consider it a big, wonky to-do list, or Advisors 3.0 for those who remember the Destiny 1 API.

    Attributes:
        milestone_hash: The unique identifier for the Milestone. Use it to look up the DestinyMilestoneDefinition, so you can combine the other data in this contract with static definition data.
        available_quests: Indicates what quests are available for this Milestone. Usually this will be only a single Quest, but some quests have multiple available that you can choose from at any given time. All possible quests for a milestone can be found in the DestinyMilestoneDefinition, but they must be combined with this Live data to determine which one(s) are actually active right now. It is possible for Milestones to not have any quests.
        activities: The currently active Activities in this milestone, when the Milestone is driven by Challenges. Not all Milestones have Challenges, but when they do this will indicate the Activities and Challenges under those Activities related to this Milestone.
        values: Milestones may have arbitrary key/value pairs associated with them, for data that users will want to know about but that doesn't fit neatly into any of the common components such as Quests. A good example of this would be - if this existed in Destiny 1 - the number of wins you currently have on your Trials of Osiris ticket. Looking in the DestinyMilestoneDefinition, you can use the string identifier of this dictionary to look up more info about the value, including localized string content for displaying the value. The value in the dictionary is the floating point number. The definition will tell you how to format this number.
        vendor_hashes: A milestone may have one or more active vendors that are "related" to it (that provide rewards, or that are the initiators of the Milestone). I already regret this, even as I'm typing it. [I told you I'd regret this] You see, sometimes a milestone may be directly correlated with a set of vendors that provide varying tiers of rewards. The player may not be able to interact with one or more of those vendors. This will return the hashes of the Vendors that the player *can* interact with, allowing you to show their current inventory as rewards or related items to the Milestone or its activities. Before we even use it, it's already deprecated! How much of a bummer is that? We need more data.
        vendors: Replaces vendorHashes, which I knew was going to be trouble the day it walked in the door. This will return not only what Vendors are active and relevant to the activity (in an implied order that you can choose to ignore), but also other data - for example, if the Vendor is featuring a specific item relevant to this event that you should show with them.
        rewards: If the entity to which this component is attached has known active Rewards for the player, this will detail information about those rewards, keyed by the RewardEntry Hash. (See DestinyMilestoneDefinition for more information about Reward Entries) Note that these rewards are not for the Quests related to the Milestone. Think of these as "overview/checklist" rewards that may be provided for Milestones that may provide rewards for performing a variety of tasks that aren't under a specific Quest.
        start_date: If known, this is the date when the event last began or refreshed. It will only be populated for events with fixed and repeating start and end dates.
        end_date: If known, this is the date when the event will next end or repeat. It will only be populated for events with fixed and repeating start and end dates.
        order: Used for ordering milestones in a display to match how we order them in BNet. May pull from static data, or possibly in the future from dynamic information.
    """

    milestone_hash: int = attr.field()
    available_quests: list["DestinyMilestoneQuest"] = attr.field()
    activities: list["DestinyMilestoneChallengeActivity"] = attr.field()
    values: Any = attr.field()
    vendor_hashes: list[int] = attr.field()
    vendors: list["DestinyMilestoneVendor"] = attr.field()
    rewards: list["DestinyMilestoneRewardCategory"] = attr.field()
    start_date: datetime.datetime = attr.field()
    end_date: datetime.datetime = attr.field()
    order: int = attr.field()


@attr.define
class DestinyMilestoneQuest(BaseModel):
    """
    If a Milestone has one or more Quests, this will contain the live information for the character's status with one of those quests.

    Attributes:
        quest_item_hash: Quests are defined as Items in content. As such, this is the hash identifier of the DestinyInventoryItemDefinition that represents this quest. It will have pointers to all of the steps in the quest, and display information for the quest (title, description, icon etc) Individual steps will be referred to in the Quest item's DestinyInventoryItemDefinition.setData property, and themselves are Items with their own renderable data.
        status: The current status of the quest for the character making the request.
        activity: *IF* the Milestone has an active Activity that can give you greater details about what you need to do, it will be returned here. Remember to associate this with the DestinyMilestoneDefinition's activities to get details about the activity, including what specific quest it is related to if you have multiple quests to choose from.
        challenges: The activities referred to by this quest can have many associated challenges. They are all contained here, with activityHashes so that you can associate them with the specific activity variants in which they can be found. In retrospect, I probably should have put these under the specific Activity Variants, but it's too late to change it now. Theoretically, a quest without Activities can still have Challenges, which is why this is on a higher level than activity/variants, but it probably should have been in both places. That may come as a later revision.
    """

    quest_item_hash: int = attr.field()
    status: "DestinyQuestStatus" = attr.field()
    activity: "DestinyMilestoneActivity" = attr.field()
    challenges: list["DestinyChallengeStatus"] = attr.field()


@attr.define
class DestinyMilestoneActivity(BaseModel):
    """
    Sometimes, we know the specific activity that the Milestone wants you to play. This entity provides additional information about that Activity and all of its variants. (sometimes there's only one variant, but I think you get the point)

    Attributes:
        activity_hash: The hash of an arbitrarily chosen variant of this activity. We'll go ahead and call that the "canonical" activity, because if you're using this value you should only use it for properties that are common across the variants: things like the name of the activity, it's location, etc... Use this hash to look up the DestinyActivityDefinition of this activity for rendering data.
        activity_mode_hash: The hash identifier of the most specific Activity Mode under which this activity is played. This is useful for situations where the activity in question is - for instance - a PVP map, but it's not clear what mode the PVP map is being played under. If it's a playlist, this will be less specific: but hopefully useful in some way.
        activity_mode_type: The enumeration equivalent of the most specific Activity Mode under which this activity is played.
        modifier_hashes: If the activity has modifiers, this will be the list of modifiers that all variants have in common. Perform lookups against DestinyActivityModifierDefinition which defines the modifier being applied to get at the modifier data. Note that, in the DestiyActivityDefinition, you will see many more modifiers than this being referred to: those are all *possible* modifiers for the activity, not the active ones. Use only the active ones to match what's really live.
        variants: If you want more than just name/location/etc... you're going to have to dig into and show the variants of the conceptual activity. These will differ in seemingly arbitrary ways, like difficulty level and modifiers applied. Show it in whatever way tickles your fancy.
    """

    activity_hash: int = attr.field()
    activity_mode_hash: int = attr.field()
    activity_mode_type: int = attr.field()
    modifier_hashes: list[int] = attr.field()
    variants: list["DestinyMilestoneActivityVariant"] = attr.field()


@attr.define
class DestinyMilestoneActivityVariant(BaseModel):
    """
    Represents custom data that we know about an individual variant of an activity.

    Attributes:
        activity_hash: The hash for the specific variant of the activity related to this milestone. You can pull more detailed static info from the DestinyActivityDefinition, such as difficulty level.
        completion_status: An OPTIONAL component: if it makes sense to talk about this activity variant in terms of whether or not it has been completed or what progress you have made in it, this will be returned. Otherwise, this will be NULL.
        activity_mode_hash: The hash identifier of the most specific Activity Mode under which this activity is played. This is useful for situations where the activity in question is - for instance - a PVP map, but it's not clear what mode the PVP map is being played under. If it's a playlist, this will be less specific: but hopefully useful in some way.
        activity_mode_type: The enumeration equivalent of the most specific Activity Mode under which this activity is played.
    """

    activity_hash: int = attr.field()
    completion_status: "DestinyMilestoneActivityCompletionStatus" = attr.field()
    activity_mode_hash: int = attr.field()
    activity_mode_type: int = attr.field()


@attr.define
class DestinyMilestoneActivityCompletionStatus(BaseModel):
    """
    Represents this player's personal completion status for the Activity under a Milestone, if the activity has trackable completion and progress information. (most activities won't, or the concept won't apply. For instance, it makes sense to talk about a tier of a raid as being Completed or having progress, but it doesn't make sense to talk about a Crucible Playlist in those terms.

    Attributes:
        completed: If the activity has been "completed", that information will be returned here.
        phases: If the Activity has discrete "phases" that we can track, that info will be here. Otherwise, this value will be NULL. Note that this is a list and not a dictionary: the order implies the ascending order of phases or progression in this activity.
    """

    completed: bool = attr.field()
    phases: list["DestinyMilestoneActivityPhase"] = attr.field()


@attr.define
class DestinyMilestoneActivityPhase(BaseModel):
    """
    Represents whatever information we can return about an explicit phase in an activity. In the future, I hope we'll have more than just "guh, you done gone and did something," but for the forseeable future that's all we've got. I'm making it more than just a list of booleans out of that overly-optimistic hope.

    Attributes:
        complete: Indicates if the phase has been completed.
        phase_hash: In DestinyActivityDefinition, if the activity has phases, there will be a set of phases defined in the "insertionPoints" property. This is the hash that maps to that phase.
    """

    complete: bool = attr.field()
    phase_hash: int = attr.field()


@attr.define
class DestinyMilestoneChallengeActivity(BaseModel):
    """
    _No description given by bungie_

    Attributes:
        activity_hash: _No description given by bungie_
        challenges: _No description given by bungie_
        modifier_hashes: If the activity has modifiers, this will be the list of modifiers that all variants have in common. Perform lookups against DestinyActivityModifierDefinition which defines the modifier being applied to get at the modifier data. Note that, in the DestiyActivityDefinition, you will see many more modifiers than this being referred to: those are all *possible* modifiers for the activity, not the active ones. Use only the active ones to match what's really live.
        boolean_activity_options: The set of activity options for this activity, keyed by an identifier that's unique for this activity (not guaranteed to be unique between or across all activities, though should be unique for every *variant* of a given *conceptual* activity: for instance, the original D2 Raid has many variant DestinyActivityDefinitions. While other activities could potentially have the same option hashes, for any given D2 base Raid variant the hash will be unique). As a concrete example of this data, the hashes you get for Raids will correspond to the currently active "Challenge Mode". We don't have any human readable information for these, but saavy 3rd party app users could manually associate the key (a hash identifier for the "option" that is enabled/disabled) and the value (whether it's enabled or disabled presently) On our side, we don't necessarily even know what these are used for (the game designers know, but we don't), and we have no human readable data for them. In order to use them, you will have to do some experimentation.
        loadout_requirement_index: If returned, this is the index into the DestinyActivityDefinition's "loadouts" property, indicating the currently active loadout requirements.
        phases: If the Activity has discrete "phases" that we can track, that info will be here. Otherwise, this value will be NULL. Note that this is a list and not a dictionary: the order implies the ascending order of phases or progression in this activity.
    """

    activity_hash: int = attr.field()
    challenges: list["DestinyChallengeStatus"] = attr.field()
    modifier_hashes: list[int] = attr.field()
    boolean_activity_options: Any = attr.field()
    loadout_requirement_index: int = attr.field()
    phases: list["DestinyMilestoneActivityPhase"] = attr.field()


@attr.define
class DestinyMilestoneVendor(BaseModel):
    """
    If a Milestone has one or more Vendors that are relevant to it, this will contain information about that vendor that you can choose to show.

    Attributes:
        vendor_hash: The hash identifier of the Vendor related to this Milestone. You can show useful things from this, such as thier Faction icon or whatever you might care about.
        preview_item_hash: If this vendor is featuring a specific item for this event, this will be the hash identifier of that item. I'm taking bets now on how long we go before this needs to be a list or some other, more complex representation instead and I deprecate this too. I'm going to go with 5 months. Calling it now, 2017-09-14 at 9:46pm PST.
    """

    vendor_hash: int = attr.field()
    preview_item_hash: int = attr.field()


@attr.define
class DestinyMilestoneRewardCategory(BaseModel):
    """
    Represents a category of "summary" rewards that can be earned for the Milestone regardless of specific quest rewards that can be earned.

    Attributes:
        reward_category_hash: Look up the relevant DestinyMilestoneDefinition, and then use rewardCategoryHash to look up the category info in DestinyMilestoneDefinition.rewards.
        entries: The individual reward entries for this category, and their status.
    """

    reward_category_hash: int = attr.field()
    entries: list["DestinyMilestoneRewardEntry"] = attr.field()


@attr.define
class DestinyMilestoneRewardEntry(BaseModel):
    """
    The character-specific data for a milestone's reward entry. See DestinyMilestoneDefinition for more information about Reward Entries.

    Attributes:
        reward_entry_hash: The identifier for the reward entry in question. It is important to look up the related DestinyMilestoneRewardEntryDefinition to get the static details about the reward, which you can do by looking up the milestone's DestinyMilestoneDefinition and examining the DestinyMilestoneDefinition.rewards[rewardCategoryHash].rewardEntries[rewardEntryHash] data.
        earned: If TRUE, the player has earned this reward.
        redeemed: If TRUE, the player has redeemed/picked up/obtained this reward. Feel free to alias this to "gotTheShinyBauble" in your own codebase.
    """

    reward_entry_hash: int = attr.field()
    earned: bool = attr.field()
    redeemed: bool = attr.field()


@attr.define
class DestinyMilestoneContent(BaseModel):
    """
    Represents localized, extended content related to Milestones. This is intentionally returned by a separate endpoint and not with Character-level Milestone data because we do not put localized data into standard Destiny responses, both for brevity of response and for caching purposes. If you really need this data, hit the Milestone Content endpoint.

    Attributes:
        about: The "About this Milestone" text from the Firehose.
        status: The Current Status of the Milestone, as driven by the Firehose.
        tips: A list of tips, provided by the Firehose.
        item_categories: If DPS has defined items related to this Milestone, they can categorize those items in the Firehose. That data will then be returned as item categories here.
    """

    about: str = attr.field()
    status: str = attr.field()
    tips: list[str] = attr.field()
    item_categories: list["DestinyMilestoneContentItemCategory"] = attr.field()


@attr.define
class DestinyMilestoneContentItemCategory(BaseModel):
    """
    Part of our dynamic, localized Milestone content is arbitrary categories of items. These are built in our content management system, and thus aren't the same as programmatically generated rewards.

    Attributes:
        title: _No description given by bungie_
        item_hashes: _No description given by bungie_
    """

    title: str = attr.field()
    item_hashes: list[int] = attr.field()


@attr.define
class DestinyPublicMilestone(BaseModel):
    """
    Information about milestones, presented in a character state-agnostic manner. Combine this data with DestinyMilestoneDefinition to get a full picture of the milestone, which is basically a checklist of things to do in the game. Think of this as GetPublicAdvisors 3.0, for those who used the Destiny 1 API.

    Attributes:
        milestone_hash: The hash identifier for the milestone. Use it to look up the DestinyMilestoneDefinition for static data about the Milestone.
        available_quests: A milestone not need have even a single quest, but if there are active quests they will be returned here.
        activities: _No description given by bungie_
        vendor_hashes: Sometimes milestones - or activities active in milestones - will have relevant vendors. These are the vendors that are currently relevant. Deprecated, already, for the sake of the new "vendors" property that has more data. What was I thinking.
        vendors: This is why we can't have nice things. This is the ordered list of vendors to be shown that relate to this milestone, potentially along with other interesting data.
        start_date: If known, this is the date when the Milestone started/became active.
        end_date: If known, this is the date when the Milestone will expire/recycle/end.
        order: Used for ordering milestones in a display to match how we order them in BNet. May pull from static data, or possibly in the future from dynamic information.
    """

    milestone_hash: int = attr.field()
    available_quests: list["DestinyPublicMilestoneQuest"] = attr.field()
    activities: list["DestinyPublicMilestoneChallengeActivity"] = attr.field()
    vendor_hashes: list[int] = attr.field()
    vendors: list["DestinyPublicMilestoneVendor"] = attr.field()
    start_date: datetime.datetime = attr.field()
    end_date: datetime.datetime = attr.field()
    order: int = attr.field()


@attr.define
class DestinyPublicMilestoneQuest(BaseModel):
    """
    _No description given by bungie_

    Attributes:
        quest_item_hash: Quests are defined as Items in content. As such, this is the hash identifier of the DestinyInventoryItemDefinition that represents this quest. It will have pointers to all of the steps in the quest, and display information for the quest (title, description, icon etc) Individual steps will be referred to in the Quest item's DestinyInventoryItemDefinition.setData property, and themselves are Items with their own renderable data.
        activity: A milestone need not have an active activity, but if there is one it will be returned here, along with any variant and additional information.
        challenges: For the given quest there could be 0-to-Many challenges: mini quests that you can perform in the course of doing this quest, that may grant you rewards and benefits.
    """

    quest_item_hash: int = attr.field()
    activity: "DestinyPublicMilestoneActivity" = attr.field()
    challenges: list["DestinyPublicMilestoneChallenge"] = attr.field()


@attr.define
class DestinyPublicMilestoneActivity(BaseModel):
    """
    A milestone may have one or more conceptual Activities associated with it, and each of those conceptual activities could have a variety of variants, modes, tiers, what-have-you. Our attempts to determine what qualifies as a conceptual activity are, unfortunately, janky. So if you see missing modes or modes that don't seem appropriate to you, let us know and I'll buy you a beer if we ever meet up in person.

    Attributes:
        activity_hash: The hash identifier of the activity that's been chosen to be considered the canonical "conceptual" activity definition. This may have many variants, defined herein.
        modifier_hashes: The activity may have 0-to-many modifiers: if it does, this will contain the hashes to the DestinyActivityModifierDefinition that defines the modifier being applied.
        variants: Every relevant variation of this conceptual activity, including the conceptual activity itself, have variants defined here.
        activity_mode_hash: The hash identifier of the most specific Activity Mode under which this activity is played. This is useful for situations where the activity in question is - for instance - a PVP map, but it's not clear what mode the PVP map is being played under. If it's a playlist, this will be less specific: but hopefully useful in some way.
        activity_mode_type: The enumeration equivalent of the most specific Activity Mode under which this activity is played.
    """

    activity_hash: int = attr.field()
    modifier_hashes: list[int] = attr.field()
    variants: list["DestinyPublicMilestoneActivityVariant"] = attr.field()
    activity_mode_hash: int = attr.field()
    activity_mode_type: int = attr.field()


@attr.define
class DestinyPublicMilestoneActivityVariant(BaseModel):
    """
    Represents a variant of an activity that's relevant to a milestone.

    Attributes:
        activity_hash: The hash identifier of this activity variant. Examine the activity's definition in the Manifest database to determine what makes it a distinct variant. Usually it will be difficulty level or whether or not it is a guided game variant of the activity, but theoretically it could be distinguished in any arbitrary way.
        activity_mode_hash: The hash identifier of the most specific Activity Mode under which this activity is played. This is useful for situations where the activity in question is - for instance - a PVP map, but it's not clear what mode the PVP map is being played under. If it's a playlist, this will be less specific: but hopefully useful in some way.
        activity_mode_type: The enumeration equivalent of the most specific Activity Mode under which this activity is played.
    """

    activity_hash: int = attr.field()
    activity_mode_hash: int = attr.field()
    activity_mode_type: int = attr.field()


@attr.define
class DestinyPublicMilestoneChallenge(BaseModel):
    """
    A Milestone can have many Challenges. Challenges are just extra Objectives that provide a fun way to mix-up play and provide extra rewards.

    Attributes:
        objective_hash: The objective for the Challenge, which should have human-readable data about what needs to be done to accomplish the objective. Use this hash to look up the DestinyObjectiveDefinition.
        activity_hash: IF the Objective is related to a specific Activity, this will be that activity's hash. Use it to look up the DestinyActivityDefinition for additional data to show.
    """

    objective_hash: int = attr.field()
    activity_hash: int = attr.field()


@attr.define
class DestinyPublicMilestoneChallengeActivity(BaseModel):
    """
    _No description given by bungie_

    Attributes:
        activity_hash: _No description given by bungie_
        challenge_objective_hashes: _No description given by bungie_
        modifier_hashes: If the activity has modifiers, this will be the list of modifiers that all variants have in common. Perform lookups against DestinyActivityModifierDefinition which defines the modifier being applied to get at the modifier data. Note that, in the DestiyActivityDefinition, you will see many more modifiers than this being referred to: those are all *possible* modifiers for the activity, not the active ones. Use only the active ones to match what's really live.
        loadout_requirement_index: If returned, this is the index into the DestinyActivityDefinition's "loadouts" property, indicating the currently active loadout requirements.
        phase_hashes: The ordered list of phases for this activity, if any. Note that we have no human readable info for phases, nor any entities to relate them to: relating these hashes to something human readable is up to you unfortunately.
        boolean_activity_options: The set of activity options for this activity, keyed by an identifier that's unique for this activity (not guaranteed to be unique between or across all activities, though should be unique for every *variant* of a given *conceptual* activity: for instance, the original D2 Raid has many variant DestinyActivityDefinitions. While other activities could potentially have the same option hashes, for any given D2 base Raid variant the hash will be unique). As a concrete example of this data, the hashes you get for Raids will correspond to the currently active "Challenge Mode". We have no human readable information for this data, so it's up to you if you want to associate it with such info to show it.
    """

    activity_hash: int = attr.field()
    challenge_objective_hashes: list[int] = attr.field()
    modifier_hashes: list[int] = attr.field()
    loadout_requirement_index: int = attr.field()
    phase_hashes: list[int] = attr.field()
    boolean_activity_options: Any = attr.field()


@attr.define
class DestinyPublicMilestoneVendor(BaseModel):
    """
    _No description given by bungie_

    Attributes:
        vendor_hash: The hash identifier of the Vendor related to this Milestone. You can show useful things from this, such as thier Faction icon or whatever you might care about.
        preview_item_hash: If this vendor is featuring a specific item for this event, this will be the hash identifier of that item. I'm taking bets now on how long we go before this needs to be a list or some other, more complex representation instead and I deprecate this too. I'm going to go with 5 months. Calling it now, 2017-09-14 at 9:46pm PST.
    """

    vendor_hash: int = attr.field()
    preview_item_hash: int = attr.field()
