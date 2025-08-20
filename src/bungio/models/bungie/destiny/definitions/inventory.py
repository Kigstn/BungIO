# DO NOT CHANGE ANY CODE BELOW
# This file is generated automatically by `generate_api_schema.py` and will be overwritten
# Instead, change functions / models by subclassing them in the `./overwrites/` folder. They will be used instead.

from typing import TYPE_CHECKING

from bungio.models.base import HashObject, ManifestModel, custom_define, custom_field

if TYPE_CHECKING:
    pass


@custom_define()
class DestinyIconDefinition(ManifestModel, HashObject):
    """
    Lists of icons that can be used for a variety of purposes

    None
    Attributes:
        background: _No description given by bungie._
        foreground: _No description given by bungie._
        hash: The unique identifier for this entity. Guaranteed to be unique for the type of entity, but not globally. When entities refer to each other in Destiny content, it is this hash that they are referring to.
        high_res_foreground: _No description given by bungie._
        index: The index of the entity as it was found in the investment tables.
        redacted: If this is true, then there is an entity with this identifier/type combination, but BNet is not yet allowed to show it. Sorry!
        secondary_background: _No description given by bungie._
        special_background: _No description given by bungie._
    """

    background: str = custom_field()
    foreground: str = custom_field()
    high_res_foreground: str = custom_field()
    index: int = custom_field()
    redacted: bool = custom_field()
    secondary_background: str = custom_field()
    special_background: str = custom_field()


@custom_define()
class DestinyItemFilterDefinition(ManifestModel, HashObject):
    """
    Lists of items that can be used for a variety of purposes, including featuring them as new gear

    None
    Attributes:
        allowed_items: The items in this set
        hash: The unique identifier for this entity. Guaranteed to be unique for the type of entity, but not globally. When entities refer to each other in Destiny content, it is this hash that they are referring to.
        index: The index of the entity as it was found in the investment tables.
        redacted: If this is true, then there is an entity with this identifier/type combination, but BNet is not yet allowed to show it. Sorry!
    """

    allowed_items: list[int] = custom_field(metadata={"type": """list[int]"""})
    index: int = custom_field()
    redacted: bool = custom_field()
