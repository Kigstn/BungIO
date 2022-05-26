import datetime
from typing import TYPE_CHECKING, Any, Optional

import attr

from bungio.models.base import BaseEnum, BaseModel


@attr.define
class DestinyPublicActivityStatus(BaseModel):
    """
        Represents the public-facing status of an activity: any data about what is currently active in the Activity, regardless of an individual character's progress in it.

        Attributes:
            challenge_objective_hashes: Active Challenges for the activity, if any - represented as hashes for DestinyObjectiveDefinitions.
            modifier_hashes: The active modifiers on this activity, if any - represented as hashes for DestinyActivityModifierDefinitions.
            reward_tooltip_items: If the activity itself provides any specific "mock" rewards, this will be the items and their quantity.

    Why "mock", you ask? Because these are the rewards as they are represented in the tooltip of the Activity.

    These are often pointers to fake items that look good in a tooltip, but represent an abstract concept of what you will get for a reward rather than the specific items you may obtain.
    """

    challenge_objective_hashes: list[int] = attr.field()
    modifier_hashes: list[int] = attr.field()
    reward_tooltip_items: list["DestinyItemQuantity"] = attr.field()
