# DO NOT CHANGE ANY CODE BELOW
# This file is generated automatically by `generate_api_schema.py` and will be overwritten
# Instead, change functions / models by subclassing them in the `./overwrites/` folder. They will be used instead.

from typing import TYPE_CHECKING

from bungio.models.base import BaseModel, custom_define, custom_field

if TYPE_CHECKING:
    from bungio.models import DestinyObjectiveProgress


@custom_define()
class DestinyKiosksComponent(BaseModel):
    """
    A Kiosk is a Vendor (DestinyVendorDefinition) that sells items based on whether you have already acquired that item before. This component returns information about what Kiosk items are available to you on a *Profile* level. It is theoretically possible for Kiosks to have items gated by specific Character as well. If you ever have those, you will find them on the individual character's DestinyCharacterKiosksComponent. Note that, because this component returns vendorItemIndexes (that is to say, indexes into the Kiosk Vendor's itemList property), these results are necessarily content version dependent. Make sure that you have the latest version of the content manifest databases before using this data.

    None
    Attributes:
        kiosk_items: A dictionary keyed by the Kiosk Vendor's hash identifier (use it to look up the DestinyVendorDefinition for the relevant kiosk vendor), and whose value is a list of all the items that the user can "see" in the Kiosk, and any other interesting metadata.
    """

    kiosk_items: dict[int, list["DestinyKioskItem"]] = custom_field(
        metadata={"type": """dict[int, list[DestinyKioskItem]]"""}
    )


@custom_define()
class DestinyKioskItem(BaseModel):
    """
    _No description given by bungie._

    None
    Attributes:
        can_acquire: If true, the user can not only see the item, but they can acquire it. It is possible that a user can see a kiosk item and not be able to acquire it.
        failure_indexes: Indexes into failureStrings for the Vendor, indicating the reasons why it failed if any.
        flavor_objective: I may regret naming it this way - but this represents when an item has an objective that doesn't serve a beneficial purpose, but rather is used for "flavor" or additional information. For instance, when Emblems track specific stats, those stats are represented as Objectives on the item.
        index: The index of the item in the related DestinyVendorDefintion's itemList property, representing the sale.
    """

    can_acquire: bool = custom_field()
    failure_indexes: list[int] = custom_field(metadata={"type": """list[int]"""})
    flavor_objective: "DestinyObjectiveProgress" = custom_field()
    index: int = custom_field()
