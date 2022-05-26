import datetime
from typing import TYPE_CHECKING, Any, Optional

import attr

from bungio.models.base import BaseEnum, BaseModel


@attr.define
class DestinyDisplayPropertiesDefinition(BaseModel):
    """
        Many Destiny*Definition contracts - the "first order" entities of Destiny that have their own tables in the Manifest Database - also have displayable information. This is the base class for that display information.

        Attributes:
            description: Not specified.
            name: Not specified.
            icon: Note that "icon" is sometimes misleading, and should be interpreted in the context of the entity. For instance, in Destiny 1 the DestinyRecordBookDefinition's icon was a big picture of a book.

    But usually, it will be a small square image that you can use as... well, an icon.

    They are currently represented as 96px x 96px images.
            icon_sequences: Not specified.
            high_res_icon: If this item has a high-res icon (at least for now, many things won't), then the path to that icon will be here.
            has_icon: Not specified.
    """

    description: str = attr.field()
    name: str = attr.field()
    icon: str = attr.field()
    icon_sequences: list["DestinyIconSequenceDefinition"] = attr.field()
    high_res_icon: str = attr.field()
    has_icon: bool = attr.field()


@attr.define
class DestinyIconSequenceDefinition(BaseModel):
    """
    Not specified.

    Attributes:
        frames: Not specified.
    """

    frames: list[str] = attr.field()


@attr.define
class DestinyPositionDefinition(BaseModel):
    """
    Not specified.

    Attributes:
        x: Not specified.
        y: Not specified.
        z: Not specified.
    """

    x: int = attr.field()
    y: int = attr.field()
    z: int = attr.field()
