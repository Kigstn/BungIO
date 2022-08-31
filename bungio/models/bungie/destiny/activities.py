# DO NOT CHANGE ANY CODE BELOW
# This file is generated automatically by `generate_api_schema.py` and will be overwritten
# Instead, change functions / models by subclassing them in the `./overwrites/` folder. They will be used instead.

from typing import TYPE_CHECKING

from bungio.models.base import BaseModel, custom_define, custom_field

if TYPE_CHECKING:
    from bungio.models import DestinyItemQuantity


@custom_define()
class DestinyPublicActivityStatus(BaseModel):
    """
    Represents the public-facing status of an activity: any data about what is currently active in the Activity, regardless of an individual character's progress in it.

    None
    Attributes:
        challenge_objective_hashes: Active Challenges for the activity, if any - represented as hashes for DestinyObjectiveDefinitions.
        modifier_hashes: The active modifiers on this activity, if any - represented as hashes for DestinyActivityModifierDefinitions.
        reward_tooltip_items: If the activity itself provides any specific "mock" rewards, this will be the items and their quantity. Why "mock", you ask? Because these are the rewards as they are represented in the tooltip of the Activity. These are often pointers to fake items that look good in a tooltip, but represent an abstract concept of what you will get for a reward rather than the specific items you may obtain.
    """

    challenge_objective_hashes: list[int] = custom_field(metadata={"type": """list[int]"""})
    modifier_hashes: list[int] = custom_field(metadata={"type": """list[int]"""})
    reward_tooltip_items: list["DestinyItemQuantity"] = custom_field(metadata={"type": """list[DestinyItemQuantity]"""})
