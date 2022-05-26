import datetime
from typing import TYPE_CHECKING, Any, Optional

import attr

from bungio.models.base import BaseEnum, BaseModel


@attr.define
class DestinyVendorLocationDefinition(BaseModel):
    """
    These definitions represent vendors' locations and relevant display information at different times in the game.

    Attributes:
        destination_hash: The hash identifier for a Destination at which this vendor may be located. Each destination where a Vendor may exist will only ever have a single entry.
        background_image_path: The relative path to the background image representing this Vendor at this location, for use in a banner.
    """

    destination_hash: int = attr.field()
    background_image_path: str = attr.field()
