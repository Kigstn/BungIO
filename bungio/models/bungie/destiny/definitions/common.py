import attr

from bungio.models.base import BaseModel


@attr.define
class DestinyDisplayPropertiesDefinition(BaseModel):
    """
    Many Destiny*Definition contracts - the "first order" entities of Destiny that have their own tables in the Manifest Database - also have displayable information. This is the base class for that display information.

    Attributes:
        description: _No description given by bungie_
        name: _No description given by bungie_
        icon: Note that "icon" is sometimes misleading, and should be interpreted in the context of the entity. For instance, in Destiny 1 the DestinyRecordBookDefinition's icon was a big picture of a book. But usually, it will be a small square image that you can use as... well, an icon. They are currently represented as 96px x 96px images.
        icon_sequences: _No description given by bungie_
        high_res_icon: If this item has a high-res icon (at least for now, many things won't), then the path to that icon will be here.
        has_icon: _No description given by bungie_
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
    _No description given by bungie_

    Attributes:
        frames: _No description given by bungie_
    """

    frames: list[str] = attr.field()


@attr.define
class DestinyPositionDefinition(BaseModel):
    """
    _No description given by bungie_

    Attributes:
        x: _No description given by bungie_
        y: _No description given by bungie_
        z: _No description given by bungie_
    """

    x: int = attr.field()
    y: int = attr.field()
    z: int = attr.field()
