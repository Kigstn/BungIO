# DO NOT CHANGE ANY CODE BELOW
# This file is generated automatically by `generate_api_schema.py` and will be overwritten
# Instead, change functions / models by subclassing them in the `./overwrites/` folder. They will be used instead.

from datetime import datetime
from typing import TYPE_CHECKING, Optional

from bungio.models.base import BaseModel, custom_define, custom_field

if TYPE_CHECKING:
    from bungio.models import (
        DestinyInventoryItemDefinition,
        DestinyItemQuantity,
        DestinyVendorDefinition,
        DestinyVendorGroupDefinition,
    )


@custom_define()
class DestinyVendorGroupComponent(BaseModel):
    """
    This component returns references to all of the Vendors in the response, grouped by categorizations that Bungie has deemed to be interesting, in the order in which both the groups and the vendors within that group should be rendered.

    None
    Attributes:
        groups: The ordered list of groups being returned.
    """

    groups: list["DestinyVendorGroup"] = custom_field(metadata={"type": """list[DestinyVendorGroup]"""})


@custom_define()
class DestinyVendorGroup(BaseModel):
    """
    Represents a specific group of vendors that can be rendered in the recommended order. How do we figure out this order? It's a long story, and will likely get more complicated over time.

    Tip: Manifest Information
        This model has some attributes which can be filled with additional information found in the manifest (`manifest_...`).
        Without additional work, these attributes will be `None`, since they require additional requests and database lookups.

        To fill the manifest dependent attributes, either:

        - Run `await ThisClass.fetch_manifest_information()`, see [here](/API Reference/Models/base)
        - Set `Client.always_return_manifest_information` to `True`, see [here](/API Reference/client)

    Attributes:
        vendor_group_hash: _No description given by bungie._
        vendor_hashes: The ordered list of vendors within a particular group.
        manifest_vendor_group_hash: Manifest information for `vendor_group_hash`
    """

    vendor_group_hash: int = custom_field()
    vendor_hashes: list[int] = custom_field(metadata={"type": """list[int]"""})
    manifest_vendor_group_hash: Optional["DestinyVendorGroupDefinition"] = custom_field(default=None)


@custom_define()
class DestinyVendorBaseComponent(BaseModel):
    """
    This component contains essential/summary information about the vendor.

    Tip: Manifest Information
        This model has some attributes which can be filled with additional information found in the manifest (`manifest_...`).
        Without additional work, these attributes will be `None`, since they require additional requests and database lookups.

        To fill the manifest dependent attributes, either:

        - Run `await ThisClass.fetch_manifest_information()`, see [here](/API Reference/Models/base)
        - Set `Client.always_return_manifest_information` to `True`, see [here](/API Reference/client)

    Attributes:
        enabled: If True, the Vendor is currently accessible.  If False, they may not actually be visible in the world at the moment.
        next_refresh_date: The date when this vendor's inventory will next rotate/refresh. Note that this is distinct from the date ranges that the vendor is visible/available in-game: this field indicates the specific time when the vendor's available items refresh and rotate, regardless of whether the vendor is actually available at that time. Unfortunately, these two values may be (and are, for the case of important vendors like Xur) different. Issue https://github.com/Bungie-net/api/issues/353 is tracking a fix to start providing visibility date ranges where possible in addition to this refresh date, so that all important dates for vendors are available for use.
        vendor_hash: The unique identifier for the vendor. Use it to look up their DestinyVendorDefinition.
        manifest_vendor_hash: Manifest information for `vendor_hash`
    """

    enabled: bool = custom_field()
    next_refresh_date: datetime = custom_field()
    vendor_hash: int = custom_field()
    manifest_vendor_hash: Optional["DestinyVendorDefinition"] = custom_field(default=None)


@custom_define()
class DestinyVendorSaleItemBaseComponent(BaseModel):
    """
    The base class for Vendor Sale Item data. Has a bunch of character-agnostic state about the item being sold. Note that if you want instance, stats, etc... data for the item, you'll have to request additional components such as ItemInstances, ItemPerks etc... and acquire them from the DestinyVendorResponse's "items" property.

    Tip: Manifest Information
        This model has some attributes which can be filled with additional information found in the manifest (`manifest_...`).
        Without additional work, these attributes will be `None`, since they require additional requests and database lookups.

        To fill the manifest dependent attributes, either:

        - Run `await ThisClass.fetch_manifest_information()`, see [here](/API Reference/Models/base)
        - Set `Client.always_return_manifest_information` to `True`, see [here](/API Reference/client)

    Attributes:
        api_purchasable: If true, this item can be purchased through the Bungie.net API.
        costs: A summary of the current costs of the item.
        item_hash: The hash of the item being sold, as a quick shortcut for looking up the DestinyInventoryItemDefinition of the sale item.
        override_next_refresh_date: If this item has its own custom date where it may be removed from the Vendor's rotation, this is that date. Note that there's not actually any guarantee that it will go away: it could be chosen again and end up still being in the Vendor's sale items! But this is the next date where that test will occur, and is also the date that the game shows for availability on things like Bounties being sold. So it's the best we can give.
        override_style_item_hash: If populated, this is the hash of the item whose icon (and other secondary styles, but *not* the human readable strings) should override whatever icons/styles are on the item being sold. If you don't do this, certain items whose styles are being overridden by socketed items - such as the "Recycle Shader" item - would show whatever their default icon/style is, and it wouldn't be pretty or look accurate.
        quantity: How much of the item you'll be getting.
        vendor_item_index: The index into the DestinyVendorDefinition.itemList property. Note that this means Vendor data *is* Content Version dependent: make sure you have the latest content before you use Vendor data, or these indexes may mismatch.  Most systems avoid this problem, but Vendors is one area where we are unable to reasonably avoid content dependency at the moment.
        manifest_item_hash: Manifest information for `item_hash`
        manifest_override_style_item_hash: Manifest information for `override_style_item_hash`
    """

    api_purchasable: bool = custom_field()
    costs: list["DestinyItemQuantity"] = custom_field(metadata={"type": """list[DestinyItemQuantity]"""})
    item_hash: int = custom_field()
    override_next_refresh_date: datetime = custom_field()
    override_style_item_hash: int = custom_field()
    quantity: int = custom_field()
    vendor_item_index: int = custom_field()
    manifest_item_hash: Optional["DestinyInventoryItemDefinition"] = custom_field(default=None)
    manifest_override_style_item_hash: Optional["DestinyInventoryItemDefinition"] = custom_field(default=None)


@custom_define()
class DestinyPublicVendorComponent(BaseModel):
    """
    This component contains essential/summary information about the vendor from the perspective of a character-agnostic view.

    Tip: Manifest Information
        This model has some attributes which can be filled with additional information found in the manifest (`manifest_...`).
        Without additional work, these attributes will be `None`, since they require additional requests and database lookups.

        To fill the manifest dependent attributes, either:

        - Run `await ThisClass.fetch_manifest_information()`, see [here](/API Reference/Models/base)
        - Set `Client.always_return_manifest_information` to `True`, see [here](/API Reference/client)

    Attributes:
        enabled: If True, the Vendor is currently accessible.  If False, they may not actually be visible in the world at the moment.
        next_refresh_date: The date when this vendor's inventory will next rotate/refresh. Note that this is distinct from the date ranges that the vendor is visible/available in-game: this field indicates the specific time when the vendor's available items refresh and rotate, regardless of whether the vendor is actually available at that time. Unfortunately, these two values may be (and are, for the case of important vendors like Xur) different. Issue https://github.com/Bungie-net/api/issues/353 is tracking a fix to start providing visibility date ranges where possible in addition to this refresh date, so that all important dates for vendors are available for use.
        vendor_hash: The unique identifier for the vendor. Use it to look up their DestinyVendorDefinition.
        manifest_vendor_hash: Manifest information for `vendor_hash`
    """

    enabled: bool = custom_field()
    next_refresh_date: datetime = custom_field()
    vendor_hash: int = custom_field()
    manifest_vendor_hash: Optional["DestinyVendorDefinition"] = custom_field(default=None)


@custom_define()
class DestinyPublicVendorSaleItemComponent(BaseModel):
    """
    Has character-agnostic information about an item being sold by a vendor. Note that if you want instance, stats, etc... data for the item, you'll have to request additional components such as ItemInstances, ItemPerks etc... and acquire them from the DestinyVendorResponse's "items" property. For most of these, however, you'll have to ask for it in context of a specific character.

    Tip: Manifest Information
        This model has some attributes which can be filled with additional information found in the manifest (`manifest_...`).
        Without additional work, these attributes will be `None`, since they require additional requests and database lookups.

        To fill the manifest dependent attributes, either:

        - Run `await ThisClass.fetch_manifest_information()`, see [here](/API Reference/Models/base)
        - Set `Client.always_return_manifest_information` to `True`, see [here](/API Reference/client)

    Attributes:
        api_purchasable: If true, this item can be purchased through the Bungie.net API.
        costs: A summary of the current costs of the item.
        item_hash: The hash of the item being sold, as a quick shortcut for looking up the DestinyInventoryItemDefinition of the sale item.
        override_next_refresh_date: If this item has its own custom date where it may be removed from the Vendor's rotation, this is that date. Note that there's not actually any guarantee that it will go away: it could be chosen again and end up still being in the Vendor's sale items! But this is the next date where that test will occur, and is also the date that the game shows for availability on things like Bounties being sold. So it's the best we can give.
        override_style_item_hash: If populated, this is the hash of the item whose icon (and other secondary styles, but *not* the human readable strings) should override whatever icons/styles are on the item being sold. If you don't do this, certain items whose styles are being overridden by socketed items - such as the "Recycle Shader" item - would show whatever their default icon/style is, and it wouldn't be pretty or look accurate.
        quantity: How much of the item you'll be getting.
        vendor_item_index: The index into the DestinyVendorDefinition.itemList property. Note that this means Vendor data *is* Content Version dependent: make sure you have the latest content before you use Vendor data, or these indexes may mismatch.  Most systems avoid this problem, but Vendors is one area where we are unable to reasonably avoid content dependency at the moment.
        manifest_item_hash: Manifest information for `item_hash`
        manifest_override_style_item_hash: Manifest information for `override_style_item_hash`
    """

    api_purchasable: bool = custom_field()
    costs: list["DestinyItemQuantity"] = custom_field(metadata={"type": """list[DestinyItemQuantity]"""})
    item_hash: int = custom_field()
    override_next_refresh_date: datetime = custom_field()
    override_style_item_hash: int = custom_field()
    quantity: int = custom_field()
    vendor_item_index: int = custom_field()
    manifest_item_hash: Optional["DestinyInventoryItemDefinition"] = custom_field(default=None)
    manifest_override_style_item_hash: Optional["DestinyInventoryItemDefinition"] = custom_field(default=None)
