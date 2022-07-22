# DO NOT CHANGE ANY CODE BELOW
# This file is generated automatically by `generate_api_schema.py` and will be overwritten
# Instead, change functions / models by subclassing them in the `./overwrites/` folder. They will be used instead.

from typing import TYPE_CHECKING, Optional

import attr

from bungio.models.base import BaseModel

if TYPE_CHECKING:
    from bungio.models import DestinyInventoryItemDefinition, DyeReference


@attr.define
class DestinyCharacterCustomization(BaseModel):
    """
    Raw data about the customization options chosen for a character's face and appearance. You can look up the relevant class/race/gender combo in DestinyCharacterCustomizationOptionDefinition for the character, and then look up these values within the CustomizationOptions found to pull some data about their choices. Warning: not all of that data is meaningful. Some data has useful icons. Others have nothing, and are only meant for 3D rendering purposes (which we sadly do not expose yet)

    None
    Attributes:
        decal_color: _No description given by bungie._
        decal_index: _No description given by bungie._
        eye_color: _No description given by bungie._
        face: _No description given by bungie._
        feature_colors: _No description given by bungie._
        feature_index: _No description given by bungie._
        hair_colors: _No description given by bungie._
        hair_index: _No description given by bungie._
        lip_color: _No description given by bungie._
        personality: _No description given by bungie._
        skin_color: _No description given by bungie._
        wear_helmet: _No description given by bungie._
    """

    decal_color: int = attr.field()
    decal_index: int = attr.field()
    eye_color: int = attr.field()
    face: int = attr.field()
    feature_colors: list[int] = attr.field(metadata={"type": """list[int]"""})
    feature_index: int = attr.field()
    hair_colors: list[int] = attr.field(metadata={"type": """list[int]"""})
    hair_index: int = attr.field()
    lip_color: int = attr.field()
    personality: int = attr.field()
    skin_color: int = attr.field()
    wear_helmet: bool = attr.field()


@attr.define
class DestinyCharacterPeerView(BaseModel):
    """
    A minimal view of a character's equipped items, for the purpose of rendering a summary screen or showing the character in 3D.

    None
    Attributes:
        equipment: _No description given by bungie._
    """

    equipment: list["DestinyItemPeerView"] = attr.field(metadata={"type": """list[DestinyItemPeerView]"""})


@attr.define
class DestinyItemPeerView(BaseModel):
    """
    Bare minimum summary information for an item, for the sake of 3D rendering the item.

    Tip: Manifest Information
        This model has some attributes which can be filled with additional information found in the manifest (`manifest_...`).
        Without additional work, these attributes will be `None`, since they require additional requests and database lookups.

        To fill the manifest dependent attributes, either:

        - Run `await ThisClass.fetch_manifest_information()`, see [here](/API Reference/Models/base)
        - Set `Client.always_return_manifest_information` to `True`, see [here](/API Reference/client)

    Attributes:
        dyes: The list of dyes that have been applied to this item.
        item_hash: The hash identifier of the item in question. Use it to look up the DestinyInventoryItemDefinition of the item for static rendering data.
        manifest_item_hash: Manifest information for `item_hash`
    """

    dyes: list["DyeReference"] = attr.field(metadata={"type": """list[DyeReference]"""})
    item_hash: int = attr.field()
    manifest_item_hash: Optional["DestinyInventoryItemDefinition"] = attr.field(default=None)
