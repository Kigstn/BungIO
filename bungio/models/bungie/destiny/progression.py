from typing import TYPE_CHECKING

import attr

from bungio.models.base import BaseModel

if TYPE_CHECKING:
    from bungio.models import DestinyProgressionResetEntry


@attr.define
class DestinyFactionProgression(BaseModel):
    """
    Mostly for historical purposes, we segregate Faction progressions from other progressions. This is just a DestinyProgression with a shortcut for finding the DestinyFactionDefinition of the faction related to the progression.

    Attributes:
        faction_hash: The hash identifier of the Faction related to this progression. Use it to look up the DestinyFactionDefinition for more rendering info.
        faction_vendor_index: The index of the Faction vendor that is currently available. Will be set to -1 if no vendors are available.
        progression_hash: The hash identifier of the Progression in question. Use it to look up the DestinyProgressionDefinition in static data.
        daily_progress: The amount of progress earned today for this progression.
        daily_limit: If this progression has a daily limit, this is that limit.
        weekly_progress: The amount of progress earned toward this progression in the current week.
        weekly_limit: If this progression has a weekly limit, this is that limit.
        current_progress: This is the total amount of progress obtained overall for this progression (for instance, the total amount of Character Level experience earned)
        level: This is the level of the progression (for instance, the Character Level).
        level_cap: This is the maximum possible level you can achieve for this progression (for example, the maximum character level obtainable)
        step_index: Progressions define their levels in "steps". Since the last step may be repeatable, the user may be at a higher level than the actual Step achieved in the progression. Not necessarily useful, but potentially interesting for those cruising the API. Relate this to the "steps" property of the DestinyProgression to see which step the user is on, if you care about that. (Note that this is Content Version dependent since it refers to indexes.)
        progress_to_next_level: The amount of progression (i.e. "Experience") needed to reach the next level of this Progression. Jeez, progression is such an overloaded word.
        next_level_at: The total amount of progression (i.e. "Experience") needed in order to reach the next level.
        current_reset_count: The number of resets of this progression you've executed this season, if applicable to this progression.
        season_resets: Information about historical resets of this progression, if there is any data for it.
        reward_item_states: Information about historical rewards for this progression, if there is any data for it.
    """

    faction_hash: int = attr.field()
    faction_vendor_index: int = attr.field()
    progression_hash: int = attr.field()
    daily_progress: int = attr.field()
    daily_limit: int = attr.field()
    weekly_progress: int = attr.field()
    weekly_limit: int = attr.field()
    current_progress: int = attr.field()
    level: int = attr.field()
    level_cap: int = attr.field()
    step_index: int = attr.field()
    progress_to_next_level: int = attr.field()
    next_level_at: int = attr.field()
    current_reset_count: int = attr.field()
    season_resets: list["DestinyProgressionResetEntry"] = attr.field()
    reward_item_states: list[int] = attr.field()
