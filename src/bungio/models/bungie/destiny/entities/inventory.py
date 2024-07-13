# DO NOT CHANGE ANY CODE BELOW
# This file is generated automatically by `generate_api_schema.py` and will be overwritten
# Instead, change functions / models by subclassing them in the `./overwrites/` folder. They will be used instead.

from typing import TYPE_CHECKING

from bungio.models.base import BaseModel, custom_define, custom_field

if TYPE_CHECKING:
    from bungio.models import DestinyItemComponent


@custom_define()
class DestinyInventoryComponent(BaseModel):
    """
    A list of minimal information for items in an inventory: be it a character's inventory, or a Profile's inventory. (Note that the Vault is a collection of inventory buckets in the Profile's inventory) Inventory Items returned here are in a flat list, but importantly they have a bucketHash property that indicates the specific inventory bucket that is holding them. These buckets constitute things like the separate sections of the Vault, the user's inventory slots, etc. See DestinyInventoryBucketDefinition for more info.

    None
    Attributes:
        items: The items in this inventory. If you care to bucket them, use the item's bucketHash property to group them.
    """

    items: list["DestinyItemComponent"] = custom_field(metadata={"type": """list[DestinyItemComponent]"""})
