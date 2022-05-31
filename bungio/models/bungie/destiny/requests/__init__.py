import datetime
from typing import TYPE_CHECKING, Any, Optional

import attr

from bungio.models.base import BaseEnum, BaseModel


@attr.define
class DestinyItemTransferRequest(BaseModel):
    """
    _No description given by bungie_

    Attributes:
        item_reference_hash: _No description given by bungie_
        stack_size: _No description given by bungie_
        transfer_to_vault: _No description given by bungie_
        item_id: The instance ID of the item for this action request.
        character_id: _No description given by bungie_
        membership_type: _No description given by bungie_
    """

    item_reference_hash: int = attr.field()
    stack_size: int = attr.field()
    transfer_to_vault: bool = attr.field()
    item_id: int = attr.field()
    character_id: int = attr.field()
    membership_type: int = attr.field()
