# DO NOT CHANGE ANY CODE BELOW
# This file is generated automatically by `generate_api_schema.py` and will be overwritten
# Instead, change functions / models by subclassing them in the `./overwrites/` folder. They will be used instead.

from datetime import datetime
from typing import TYPE_CHECKING, Any, Optional, Union

from bungio.models.base import BaseEnum, BaseFlagEnum, BaseModel, HashObject, ManifestModel, custom_define, custom_field
from bungio.utils import enum_converter

if TYPE_CHECKING:
    from bungio.models import BungieMembershipType, DestinyInventoryItemDefinition


@custom_define()
class DestinyItemTransferRequest(BaseModel):
    """
    _No description given by bungie._

    Tip: Manifest Information
        This model has some attributes which can be filled with additional information found in the manifest (`manifest_...`).
        Without additional work, these attributes will be `None`, since they require additional requests and database lookups.

        To fill the manifest dependent attributes, either:

        - Run `await ThisClass.fetch_manifest_information()`, see [here](/API Reference/Models/base)
        - Set `Client.always_return_manifest_information` to `True`, see [here](/API Reference/client)

    Attributes:
        character_id: _No description given by bungie._
        item_id: The instance ID of the item for this action request.
        item_reference_hash: _No description given by bungie._
        membership_type: _No description given by bungie._
        stack_size: _No description given by bungie._
        transfer_to_vault: _No description given by bungie._
        manifest_item_reference_hash: Manifest information for `item_reference_hash`
    """

    character_id: int = custom_field(metadata={"int64": True})
    item_id: int = custom_field(metadata={"int64": True})
    item_reference_hash: int = custom_field()
    membership_type: Union["BungieMembershipType", int] = custom_field(converter=enum_converter("BungieMembershipType"))
    stack_size: int = custom_field()
    transfer_to_vault: bool = custom_field()
    manifest_item_reference_hash: Optional["DestinyInventoryItemDefinition"] = custom_field(default=None)
