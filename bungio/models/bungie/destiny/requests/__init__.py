import datetime
from typing import TYPE_CHECKING, Any, Optional, Union

import attr

from bungio.models.base import BaseEnum, BaseModel

if TYPE_CHECKING:
    from bungio.models import BungieMembershipType, DestinyInventoryItemDefinition


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

    item_reference_hash: "DestinyInventoryItemDefinition" = attr.field()
    stack_size: int = attr.field()
    transfer_to_vault: bool = attr.field()
    item_id: int = attr.field()
    character_id: int = attr.field()
    membership_type: "BungieMembershipType" = attr.field()
