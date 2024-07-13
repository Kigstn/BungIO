# DO NOT CHANGE ANY CODE BELOW
# This file is generated automatically by `generate_api_schema.py` and will be overwritten
# Instead, change functions / models by subclassing them in the `./overwrites/` folder. They will be used instead.

from datetime import datetime
from typing import Union, TYPE_CHECKING

from bungio.utils import enum_converter
from bungio.models.base import BaseModel, custom_define, custom_field


if TYPE_CHECKING:
    from bungio.models import DestinyVendorItemRefundPolicy
    from bungio.models import DestinyItemQuantity


@custom_define()
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

    currency_paid: list["DestinyItemQuantity"] = custom_field(metadata={"type": """list[DestinyItemQuantity]"""})
    expires_on: datetime = custom_field()
    item_received: "DestinyItemQuantity" = custom_field()
    license_unlock_hash: int = custom_field()
    purchased_by_character_id: int = custom_field(metadata={"int64": True})
    refund_policy: Union["DestinyVendorItemRefundPolicy", int] = custom_field(
        converter=enum_converter("DestinyVendorItemRefundPolicy")
    )
    sequence_number: int = custom_field()
    time_to_expiration: int = custom_field(metadata={"int64": True})
