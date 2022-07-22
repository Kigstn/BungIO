# DO NOT CHANGE ANY CODE BELOW
# This file is generated automatically by `generate_api_schema.py` and will be overwritten
# Instead, change functions / models by subclassing them in the `./overwrites/` folder. They will be used instead.

from datetime import datetime
from typing import TYPE_CHECKING, Union

import attr

from bungio.models.base import BaseModel
from bungio.utils import enum_converter

if TYPE_CHECKING:
    from bungio.models import DestinyItemQuantity, DestinyVendorItemRefundPolicy


@attr.define
class DestinyVendorReceipt(BaseModel):
    """
    If a character purchased an item that is refundable, a Vendor Receipt will be created on the user's Destiny Profile. These expire after a configurable period of time, but until then can be used to get refunds on items. BNet does not provide the ability to refund a purchase *yet*, but you know.

    None
    Attributes:
        currency_paid: The amount paid for the item, in terms of items that were consumed in the purchase and their quantity.
        expires_on: The date at which this receipt is rendered invalid.
        item_received: The item that was received, and its quantity.
        license_unlock_hash: The unlock flag used to determine whether you still have the purchased item.
        purchased_by_character_id: The ID of the character who made the purchase.
        refund_policy: Whether you can get a refund, and what happens in order for the refund to be received. See the DestinyVendorItemRefundPolicy enum for details.
        sequence_number: The identifier of this receipt.
        time_to_expiration: The seconds since epoch at which this receipt is rendered invalid.
    """

    currency_paid: list["DestinyItemQuantity"] = attr.field(metadata={"type": """list[DestinyItemQuantity]"""})
    expires_on: datetime = attr.field()
    item_received: "DestinyItemQuantity" = attr.field()
    license_unlock_hash: int = attr.field()
    purchased_by_character_id: int = attr.field()
    refund_policy: Union["DestinyVendorItemRefundPolicy", int] = attr.field(
        converter=enum_converter("DestinyVendorItemRefundPolicy")
    )
    sequence_number: int = attr.field()
    time_to_expiration: int = attr.field()
