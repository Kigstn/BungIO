# DO NOT CHANGE ANY CODE BELOW
# This file is generated automatically by `generate_api_schema.py` and will be overwritten
# Instead, change functions / models by subclassing them in the `./overwrites/` folder. They will be used instead.

from typing import Optional, Union, TYPE_CHECKING

from bungio.utils import enum_converter
from bungio.models.base import BaseModel, custom_define, custom_field


if TYPE_CHECKING:
    from bungio.models import DestinyProgressionResetEntry
    from bungio.models import DestinyProgressionDefinition
    from bungio.models import DestinyProgressionRewardItemState
    from bungio.models import DestinyFactionDefinition


@custom_define()
class DestinyFactionProgression(BaseModel):
    """
    Mostly for historical purposes, we segregate Faction progressions from other progressions. This is just a DestinyProgression with a shortcut for finding the DestinyFactionDefinition of the faction related to the progression.

    Tip: Manifest Information
        This model has some attributes which can be filled with additional information found in the manifest (`manifest_...`).
        Without additional work, these attributes will be `None`, since they require additional requests and database lookups.

        To fill the manifest dependent attributes, either:

        - Run `await ThisClass.fetch_manifest_information()`, see [here](/API Reference/Models/base)
        - Set `Client.always_return_manifest_information` to `True`, see [here](/API Reference/client)

    Attributes:
        current_progress: This is the total amount of progress obtained overall for this progression (for instance, the total amount of Character Level experience earned)
        current_reset_count: The number of resets of this progression you've executed this season, if applicable to this progression.
        daily_limit: If this progression has a daily limit, this is that limit.
        daily_progress: The amount of progress earned today for this progression.
        faction_hash: The hash identifier of the Faction related to this progression. Use it to look up the DestinyFactionDefinition for more rendering info.
        faction_vendor_index: The index of the Faction vendor that is currently available. Will be set to -1 if no vendors are available.
        level: This is the level of the progression (for instance, the Character Level).
        level_cap: This is the maximum possible level you can achieve for this progression (for example, the maximum character level obtainable)
        next_level_at: The total amount of progression (i.e. "Experience") needed in order to reach the next level.
        progress_to_next_level: The amount of progression (i.e. "Experience") needed to reach the next level of this Progression. Jeez, progression is such an overloaded word.
        progression_hash: The hash identifier of the Progression in question. Use it to look up the DestinyProgressionDefinition in static data.
        reward_item_states: Information about historical rewards for this progression, if there is any data for it.
        season_resets: Information about historical resets of this progression, if there is any data for it.
        step_index: Progressions define their levels in "steps". Since the last step may be repeatable, the user may be at a higher level than the actual Step achieved in the progression. Not necessarily useful, but potentially interesting for those cruising the API. Relate this to the "steps" property of the DestinyProgression to see which step the user is on, if you care about that. (Note that this is Content Version dependent since it refers to indexes.)
        weekly_limit: If this progression has a weekly limit, this is that limit.
        weekly_progress: The amount of progress earned toward this progression in the current week.
        manifest_faction_hash: Manifest information for `faction_hash`
        manifest_progression_hash: Manifest information for `progression_hash`
    """

    current_progress: int = custom_field()
    current_reset_count: int = custom_field()
    daily_limit: int = custom_field()
    daily_progress: int = custom_field()
    faction_hash: int = custom_field()
    faction_vendor_index: int = custom_field()
    level: int = custom_field()
    level_cap: int = custom_field()
    next_level_at: int = custom_field()
    progress_to_next_level: int = custom_field()
    progression_hash: int = custom_field()
    reward_item_states: list[Union["DestinyProgressionRewardItemState", int]] = custom_field(
        converter=enum_converter("DestinyProgressionRewardItemState")
    )
    season_resets: list["DestinyProgressionResetEntry"] = custom_field(
        metadata={"type": """list[DestinyProgressionResetEntry]"""}
    )
    step_index: int = custom_field()
    weekly_limit: int = custom_field()
    weekly_progress: int = custom_field()
    manifest_faction_hash: Optional["DestinyFactionDefinition"] = custom_field(default=None)
    manifest_progression_hash: Optional["DestinyProgressionDefinition"] = custom_field(default=None)
