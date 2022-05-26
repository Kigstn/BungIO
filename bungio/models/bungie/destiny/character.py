import datetime
from typing import TYPE_CHECKING, Any, Optional

import attr

from bungio.models.base import BaseEnum, BaseModel


@attr.define
class DestinyCharacterCustomization(BaseModel):
    """
        Raw data about the customization options chosen for a character's face and appearance.

    You can look up the relevant class/race/gender combo in DestinyCharacterCustomizationOptionDefinition for the character, and then look up these values within the CustomizationOptions found to pull some data about their choices. Warning: not all of that data is meaningful. Some data has useful icons. Others have nothing, and are only meant for 3D rendering purposes (which we sadly do not expose yet)

        Attributes:
            personality: Not specified.
            face: Not specified.
            skin_color: Not specified.
            lip_color: Not specified.
            eye_color: Not specified.
            hair_colors: Not specified.
            feature_colors: Not specified.
            decal_color: Not specified.
            wear_helmet: Not specified.
            hair_index: Not specified.
            feature_index: Not specified.
            decal_index: Not specified.
    """

    personality: int = attr.field()
    face: int = attr.field()
    skin_color: int = attr.field()
    lip_color: int = attr.field()
    eye_color: int = attr.field()
    hair_colors: list[int] = attr.field()
    feature_colors: list[int] = attr.field()
    decal_color: int = attr.field()
    wear_helmet: bool = attr.field()
    hair_index: int = attr.field()
    feature_index: int = attr.field()
    decal_index: int = attr.field()


@attr.define
class DestinyCharacterPeerView(BaseModel):
    """
    A minimal view of a character's equipped items, for the purpose of rendering a summary screen or showing the character in 3D.

    Attributes:
        equipment: Not specified.
    """

    equipment: list["DestinyItemPeerView"] = attr.field()


@attr.define
class DestinyItemPeerView(BaseModel):
    """
    Bare minimum summary information for an item, for the sake of 3D rendering the item.

    Attributes:
        item_hash: The hash identifier of the item in question. Use it to look up the DestinyInventoryItemDefinition of the item for static rendering data.
        dyes: The list of dyes that have been applied to this item.
    """

    item_hash: int = attr.field()
    dyes: list["DyeReference"] = attr.field()
