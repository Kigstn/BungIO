# DO NOT CHANGE ANY CODE BELOW
# This file is generated automatically by `generate_api_schema.py` and will be overwritten
# Instead, change functions / models by subclassing them in the `./overwrites/` folder. They will be used instead.

from typing import TYPE_CHECKING

from bungio.models.base import HashObject, ManifestModel, custom_define, custom_field

if TYPE_CHECKING:
    pass


@custom_define()
class DestinyItemFilterDefinition(ManifestModel, HashObject):
    """
    Lists of items that can be used for a variety of purposes, including featuring them as new gear

    None
    Attributes:
        hash: The unique identifier for this entity. Guaranteed to be unique for the type of entity, but not globally. When entities refer to each other in Destiny content, it is this hash that they are referring to.
        index: The index of the entity as it was found in the investment tables.
        redacted: If this is true, then there is an entity with this identifier/type combination, but BNet is not yet allowed to show it. Sorry!
        set_items: The items in this set
    """

    index: int = custom_field()
    redacted: bool = custom_field()
    set_items: list[int] = custom_field(metadata={"type": """list[int]"""})
