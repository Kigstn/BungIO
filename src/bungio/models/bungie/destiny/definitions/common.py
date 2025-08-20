# DO NOT CHANGE ANY CODE BELOW
# This file is generated automatically by `generate_api_schema.py` and will be overwritten
# Instead, change functions / models by subclassing them in the `./overwrites/` folder. They will be used instead.

from typing import Optional

from bungio.models.base import BaseModel, custom_define, custom_field


@custom_define()
class DestinyDisplayPropertiesDefinition(BaseModel):
    """
    Many Destiny*Definition contracts - the "first order" entities of Destiny that have their own tables in the Manifest Database - also have displayable information. This is the base class for that display information.

    Tip: Manifest Information
        This model has some attributes which can be filled with additional information found in the manifest (`manifest_...`).
        Without additional work, these attributes will be `None`, since they require additional requests and database lookups.

        To fill the manifest dependent attributes, either:

        - Run `await ThisClass.fetch_manifest_information()`, see [here](/API Reference/Models/base)
        - Set `Client.always_return_manifest_information` to `True`, see [here](/API Reference/client)

    Attributes:
        description: _No description given by bungie._
        has_icon: _No description given by bungie._
        high_res_icon: If this item has a high-res icon (at least for now, many things won't), then the path to that icon will be here.
        icon: Note that "icon" is sometimes misleading, and should be interpreted in the context of the entity. For instance, in Destiny 1 the DestinyRecordBookDefinition's icon was a big picture of a book. But usually, it will be a small square image that you can use as... well, an icon. They are currently represented as 96px x 96px images.
        icon_hash: _No description given by bungie._
        icon_sequences: _No description given by bungie._
        name: _No description given by bungie._
        manifest_icon_hash: Manifest information for `icon_hash`
    """

    description: str = custom_field()
    has_icon: bool = custom_field()
    high_res_icon: str = custom_field()
    icon: str = custom_field()
    icon_hash: int = custom_field()
    icon_sequences: list["DestinyIconSequenceDefinition"] = custom_field(
        metadata={"type": """list[DestinyIconSequenceDefinition]"""}
    )
    name: str = custom_field()
    manifest_icon_hash: Optional[dict] = custom_field(metadata={"type": """Optional[dict]"""}, default=None)


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
