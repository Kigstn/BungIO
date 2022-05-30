import datetime
from typing import TYPE_CHECKING, Any, Optional

import attr

from bungio.models.base import BaseEnum, BaseModel


@attr.define
class DestinyItemTransferRequest(BaseModel):
    """
    Not specified.

    Attributes:
        item_reference_hash: Not specified.
        stack_size: Not specified.
        transfer_to_vault: Not specified.
        item_id: The instance ID of the item for this action request.
        character_id: Not specified.
        membership_type: Not specified.
    """

    item_reference_hash: int = attr.field()
    stack_size: int = attr.field()
    transfer_to_vault: bool = attr.field()
    item_id: int = attr.field()
    character_id: int = attr.field()
    membership_type: int = attr.field()
