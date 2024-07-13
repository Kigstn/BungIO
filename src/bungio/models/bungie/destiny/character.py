# DO NOT CHANGE ANY CODE BELOW
# This file is generated automatically by `generate_api_schema.py` and will be overwritten
# Instead, change functions / models by subclassing them in the `./overwrites/` folder. They will be used instead.

from typing import Optional, TYPE_CHECKING

from bungio.models.base import BaseModel, custom_define, custom_field


if TYPE_CHECKING:
    from bungio.models import DyeReference
    from bungio.models import DestinyInventoryItemDefinition


@custom_define()
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

    decal_color: int = custom_field()
    decal_index: int = custom_field()
    eye_color: int = custom_field()
    face: int = custom_field()
    feature_colors: list[int] = custom_field(metadata={"type": """list[int]"""})
    feature_index: int = custom_field()
    hair_colors: list[int] = custom_field(metadata={"type": """list[int]"""})
    hair_index: int = custom_field()
    lip_color: int = custom_field()
    personality: int = custom_field()
    skin_color: int = custom_field()
    wear_helmet: bool = custom_field()


@custom_define()
class DestinyCharacterPeerView(BaseModel):
    """
    A minimal view of a character's equipped items, for the purpose of rendering a summary screen or showing the character in 3D.

    None
    Attributes:
        equipment: _No description given by bungie._
    """

    equipment: list["DestinyItemPeerView"] = custom_field(metadata={"type": """list[DestinyItemPeerView]"""})


@custom_define()
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

    dyes: list["DyeReference"] = custom_field(metadata={"type": """list[DyeReference]"""})
    item_hash: int = custom_field()
    manifest_item_hash: Optional["DestinyInventoryItemDefinition"] = custom_field(default=None)
