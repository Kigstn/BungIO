# DO NOT CHANGE ANY CODE BELOW
# This file is generated automatically by `generate_api_schema.py` and will be overwritten
# Instead, change functions / models by subclassing them in the `./overwrites/` folder. They will be used instead.


from bungio.models.base import BaseModel, custom_define, custom_field


@custom_define()
class DestinyDisplayPropertiesDefinition(BaseModel):
    """
    Many Destiny*Definition contracts - the "first order" entities of Destiny that have their own tables in the Manifest Database - also have displayable information. This is the base class for that display information.

    None
    Attributes:
        description: _No description given by bungie._
        has_icon: _No description given by bungie._
        high_res_icon: If this item has a high-res icon (at least for now, many things won't), then the path to that icon will be here.
        icon: Note that "icon" is sometimes misleading, and should be interpreted in the context of the entity. For instance, in Destiny 1 the DestinyRecordBookDefinition's icon was a big picture of a book. But usually, it will be a small square image that you can use as... well, an icon. They are currently represented as 96px x 96px images.
        icon_sequences: _No description given by bungie._
        name: _No description given by bungie._
    """

    description: str = custom_field()
    has_icon: bool = custom_field()
    high_res_icon: str = custom_field()
    icon: str = custom_field()
    icon_sequences: list["DestinyIconSequenceDefinition"] = custom_field(
        metadata={"type": """list[DestinyIconSequenceDefinition]"""}
    )
    name: str = custom_field()


@custom_define()
class DestinyIconSequenceDefinition(BaseModel):
    """
    _No description given by bungie._

    None
    Attributes:
        frames: _No description given by bungie._
    """

    frames: list[str] = custom_field(metadata={"type": """list[str]"""})


@custom_define()
class DestinyPositionDefinition(BaseModel):
    """
    _No description given by bungie._

    None
    Attributes:
        x: _No description given by bungie._
        y: _No description given by bungie._
        z: _No description given by bungie._
    """

    x: int = custom_field()
    y: int = custom_field()
    z: int = custom_field()
