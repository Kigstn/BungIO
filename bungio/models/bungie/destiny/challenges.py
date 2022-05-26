import datetime
from typing import TYPE_CHECKING, Any, Optional

import attr

from bungio.models.base import BaseEnum, BaseModel


@attr.define
class DestinyChallengeStatus(BaseModel):
    """
        Represents the status and other related information for a challenge that is - or was - available to a player.

    A challenge is a bonus objective, generally tacked onto Quests or Activities, that provide additional variations on play.

        Attributes:
            objective: The progress - including completion status - of the active challenge.
    """

    objective: Any = attr.field()
