# DO NOT CHANGE ANY CODE BELOW
# This file is generated automatically by `generate_api_schema.py` and will be overwritten
# Instead, change functions / models by subclassing them in the `./overwrites/` folder. They will be used instead.

from typing import TYPE_CHECKING, Optional

from bungio.models.base import BaseModel, custom_define, custom_field

if TYPE_CHECKING:
    from bungio.models import DestinyDestinationDefinition


@custom_define()
class DestinyVendorLocationDefinition(BaseModel):
    """
    These definitions represent vendors' locations and relevant display information at different times in the game.

    Tip: Manifest Information
        This model has some attributes which can be filled with additional information found in the manifest (`manifest_...`).
        Without additional work, these attributes will be `None`, since they require additional requests and database lookups.

        To fill the manifest dependent attributes, either:

        - Run `await ThisClass.fetch_manifest_information()`, see [here](/API Reference/Models/base)
        - Set `Client.always_return_manifest_information` to `True`, see [here](/API Reference/client)

    Attributes:
        background_image_path: The relative path to the background image representing this Vendor at this location, for use in a banner.
        destination_hash: The hash identifier for a Destination at which this vendor may be located. Each destination where a Vendor may exist will only ever have a single entry.
        manifest_destination_hash: Manifest information for `destination_hash`
    """

    background_image_path: str = custom_field()
    destination_hash: int = custom_field()
    manifest_destination_hash: Optional["DestinyDestinationDefinition"] = custom_field(default=None)
