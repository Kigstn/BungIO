# DO NOT CHANGE ANY CODE BELOW
# This file is generated automatically by `generate_api_schema.py` and will be overwritten
# Instead, change functions / models by subclassing them in the `./overwrites/` folder. They will be used instead.

from typing import TYPE_CHECKING, Optional

from bungio.models.base import BaseModel, custom_define, custom_field

if TYPE_CHECKING:
    from bungio.models import (
        DestinyActivityDefinition,
        DestinyDestinationDefinition,
        DestinyInventoryItemDefinition,
        DestinyObjectiveDefinition,
    )


@custom_define()
class DestinyObjectiveProgress(BaseModel):
    """
    Returns data about a character's status with a given Objective. Combine with DestinyObjectiveDefinition static data for display purposes.

    Tip: Manifest Information
        This model has some attributes which can be filled with additional information found in the manifest (`manifest_...`).
        Without additional work, these attributes will be `None`, since they require additional requests and database lookups.

        To fill the manifest dependent attributes, either:

        - Run `await ThisClass.fetch_manifest_information()`, see [here](/API Reference/Models/base)
        - Set `Client.always_return_manifest_information` to `True`, see [here](/API Reference/client)

    Attributes:
        activity_hash: If the Objective has an Activity associated with it, this is the unique identifier of the Activity being referred to. Use to look up the DestinyActivityDefinition in static data. This will give localized data about *what* you should be playing for the objective to be achieved.
        complete: Whether or not the Objective is completed.
        completion_value: As of Forsaken, objectives' completion value is determined dynamically at runtime. This value represents the threshold of progress you need to surpass in order for this objective to be considered "complete". If you were using objective data, switch from using the DestinyObjectiveDefinition's "completionValue" to this value.
        destination_hash: If the Objective has a Destination associated with it, this is the unique identifier of the Destination being referred to. Use to look up the DestinyDestinationDefinition in static data. This will give localized data about *where* in the universe the objective should be achieved.
        objective_hash: The unique identifier of the Objective being referred to. Use to look up the DestinyObjectiveDefinition in static data.
        progress: If progress has been made, and the progress can be measured numerically, this will be the value of that progress. You can compare it to the DestinyObjectiveDefinition.completionValue property for current vs. upper bounds, and use DestinyObjectiveDefinition.inProgressValueStyle or completedValueStyle to determine how this should be rendered. Note that progress, in Destiny 2, need not be a literal numeric progression. It could be one of a number of possible values, even a Timestamp. Always examine DestinyObjectiveDefinition.inProgressValueStyle or completedValueStyle before rendering progress.
        visible: If this is true, the objective is visible in-game. Otherwise, it's not yet visible to the player. Up to you if you want to honor this property.
        manifest_activity_hash: Manifest information for `activity_hash`
        manifest_destination_hash: Manifest information for `destination_hash`
        manifest_objective_hash: Manifest information for `objective_hash`
    """

    activity_hash: int = custom_field()
    complete: bool = custom_field()
    completion_value: int = custom_field()
    destination_hash: int = custom_field()
    objective_hash: int = custom_field()
    progress: int = custom_field()
    visible: bool = custom_field()
    manifest_activity_hash: Optional["DestinyActivityDefinition"] = custom_field(default=None)
    manifest_destination_hash: Optional["DestinyDestinationDefinition"] = custom_field(default=None)
    manifest_objective_hash: Optional["DestinyObjectiveDefinition"] = custom_field(default=None)


@custom_define()
class DestinyQuestStatus(BaseModel):
    """
    Data regarding the progress of a Quest for a specific character. Quests are composed of multiple steps, each with potentially multiple objectives: this QuestStatus will return Objective data for the *currently active* step in this quest.

    Tip: Manifest Information
        This model has some attributes which can be filled with additional information found in the manifest (`manifest_...`).
        Without additional work, these attributes will be `None`, since they require additional requests and database lookups.

        To fill the manifest dependent attributes, either:

        - Run `await ThisClass.fetch_manifest_information()`, see [here](/API Reference/Models/base)
        - Set `Client.always_return_manifest_information` to `True`, see [here](/API Reference/client)

    Attributes:
        completed: Whether or not the whole quest has been completed, regardless of whether or not you have redeemed the rewards for the quest.
        item_instance_id: The current Quest Step will be an instanced item in the player's inventory. If you care about that, this is the instance ID of that item.
        quest_hash: The hash identifier for the Quest Item. (Note: Quests are defined as Items, and thus you would use this to look up the quest's DestinyInventoryItemDefinition). For information on all steps in the quest, you can then examine its DestinyInventoryItemDefinition.setData property for Quest Steps (which are *also* items). You can use the Item Definition to display human readable data about the overall quest.
        redeemed: Whether or not you have redeemed rewards for this quest.
        started: Whether or not you have started this quest.
        step_hash: The hash identifier of the current Quest Step, which is also a DestinyInventoryItemDefinition. You can use this to get human readable data about the current step and what to do in that step.
        step_objectives: A step can have multiple objectives. This will give you the progress for each objective in the current step, in the order in which they are rendered in-game.
        tracked: Whether or not the quest is tracked
        vendor_hash: If the quest has a related Vendor that you should talk to in order to initiate the quest/earn rewards/continue the quest, this will be the hash identifier of that Vendor. Look it up its DestinyVendorDefinition.
        manifest_quest_hash: Manifest information for `quest_hash`
        manifest_step_hash: Manifest information for `step_hash`
    """

    completed: bool = custom_field()
    item_instance_id: int = custom_field(metadata={"int64": True})
    quest_hash: int = custom_field()
    redeemed: bool = custom_field()
    started: bool = custom_field()
    step_hash: int = custom_field()
    step_objectives: list["DestinyObjectiveProgress"] = custom_field(
        metadata={"type": """list[DestinyObjectiveProgress]"""}
    )
    tracked: bool = custom_field()
    vendor_hash: int = custom_field()
    manifest_quest_hash: Optional["DestinyInventoryItemDefinition"] = custom_field(default=None)
    manifest_step_hash: Optional["DestinyInventoryItemDefinition"] = custom_field(default=None)
