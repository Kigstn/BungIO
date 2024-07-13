# DO NOT CHANGE ANY CODE BELOW
# This file is generated automatically by `generate_api_schema.py` and will be overwritten
# Instead, change functions / models by subclassing them in the `./overwrites/` folder. They will be used instead.

from typing import TYPE_CHECKING

from bungio.models.base import BaseModel, custom_define, custom_field

if TYPE_CHECKING:
    from bungio.models import DestinyObjectiveProgress


@custom_define()
class DestinyChallengeStatus(BaseModel):
    """
    Represents the status and other related information for a challenge that is - or was - available to a player.  A challenge is a bonus objective, generally tacked onto Quests or Activities, that provide additional variations on play.

    None
    Attributes:
        objective: The progress - including completion status - of the active challenge.
    """

    objective: "DestinyObjectiveProgress" = custom_field()
