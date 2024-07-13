# DO NOT CHANGE ANY CODE BELOW
# This file is generated automatically by `generate_api_schema.py` and will be overwritten
# Instead, change functions / models by subclassing them in the `./overwrites/` folder. They will be used instead.

from typing import Optional, TYPE_CHECKING

from bungio.models.base import BaseModel, HashObject, ManifestModel, custom_define, custom_field


if TYPE_CHECKING:
    from bungio.models import DestinyDisplayPropertiesDefinition
    from bungio.models import DestinyPresentationNodeDefinition


@custom_define()
class DestinyGuardianRankDefinition(ManifestModel, HashObject):
    """
    _No description given by bungie._

    Tip: Manifest Information
        This model has some attributes which can be filled with additional information found in the manifest (`manifest_...`).
        Without additional work, these attributes will be `None`, since they require additional requests and database lookups.

        To fill the manifest dependent attributes, either:

        - Run `await ThisClass.fetch_manifest_information()`, see [here](/API Reference/Models/base)
        - Set `Client.always_return_manifest_information` to `True`, see [here](/API Reference/client)

    Attributes:
        display_properties: _No description given by bungie._
        foreground_image_path: _No description given by bungie._
        hash: The unique identifier for this entity. Guaranteed to be unique for the type of entity, but not globally. When entities refer to each other in Destiny content, it is this hash that they are referring to.
        index: The index of the entity as it was found in the investment tables.
        overlay_image_path: _No description given by bungie._
        overlay_mask_image_path: _No description given by bungie._
        presentation_node_hash: _No description given by bungie._
        rank_number: _No description given by bungie._
        redacted: If this is true, then there is an entity with this identifier/type combination, but BNet is not yet allowed to show it. Sorry!
        manifest_presentation_node_hash: Manifest information for `presentation_node_hash`
    """

    display_properties: "DestinyDisplayPropertiesDefinition" = custom_field()
    foreground_image_path: str = custom_field()
    index: int = custom_field()
    overlay_image_path: str = custom_field()
    overlay_mask_image_path: str = custom_field()
    presentation_node_hash: int = custom_field()
    rank_number: int = custom_field()
    redacted: bool = custom_field()
    manifest_presentation_node_hash: Optional["DestinyPresentationNodeDefinition"] = custom_field(default=None)


@custom_define()
class DestinyGuardianRankConstantsDefinition(ManifestModel, HashObject):
    """
    _No description given by bungie._

    Tip: Manifest Information
        This model has some attributes which can be filled with additional information found in the manifest (`manifest_...`).
        Without additional work, these attributes will be `None`, since they require additional requests and database lookups.

        To fill the manifest dependent attributes, either:

        - Run `await ThisClass.fetch_manifest_information()`, see [here](/API Reference/Models/base)
        - Set `Client.always_return_manifest_information` to `True`, see [here](/API Reference/client)

    Attributes:
        display_properties: _No description given by bungie._
        guardian_rank_hashes: _No description given by bungie._
        hash: The unique identifier for this entity. Guaranteed to be unique for the type of entity, but not globally. When entities refer to each other in Destiny content, it is this hash that they are referring to.
        icon_backgrounds: _No description given by bungie._
        index: The index of the entity as it was found in the investment tables.
        rank_count: _No description given by bungie._
        redacted: If this is true, then there is an entity with this identifier/type combination, but BNet is not yet allowed to show it. Sorry!
        root_node_hash: _No description given by bungie._
        manifest_root_node_hash: Manifest information for `root_node_hash`
    """

    display_properties: "DestinyDisplayPropertiesDefinition" = custom_field()
    guardian_rank_hashes: list[int] = custom_field(metadata={"type": """list[int]"""})
    icon_backgrounds: "DestinyGuardianRankIconBackgroundsDefinition" = custom_field()
    index: int = custom_field()
    rank_count: int = custom_field()
    redacted: bool = custom_field()
    root_node_hash: int = custom_field()
    manifest_root_node_hash: Optional["DestinyPresentationNodeDefinition"] = custom_field(default=None)


@custom_define()
class DestinyGuardianRankIconBackgroundsDefinition(BaseModel):
    """
    _No description given by bungie._

    None
    Attributes:
        background_empty_blue_gradient_bordered_image_path: _No description given by bungie._
        background_empty_bordered_image_path: _No description given by bungie._
        background_filled_blue_bordered_image_path: _No description given by bungie._
        background_filled_blue_gradient_bordered_image_path: _No description given by bungie._
        background_filled_blue_low_alpha_image_path: _No description given by bungie._
        background_filled_blue_medium_alpha_image_path: _No description given by bungie._
        background_filled_gray_heavy_alpha_bordered_image_path: _No description given by bungie._
        background_filled_gray_medium_alpha_bordered_image_path: _No description given by bungie._
        background_filled_white_image_path: _No description given by bungie._
        background_filled_white_medium_alpha_image_path: _No description given by bungie._
        background_plate_black_alpha_image_path: _No description given by bungie._
        background_plate_black_image_path: _No description given by bungie._
        background_plate_white_image_path: _No description given by bungie._
    """

    background_empty_blue_gradient_bordered_image_path: str = custom_field()
    background_empty_bordered_image_path: str = custom_field()
    background_filled_blue_bordered_image_path: str = custom_field()
    background_filled_blue_gradient_bordered_image_path: str = custom_field()
    background_filled_blue_low_alpha_image_path: str = custom_field()
    background_filled_blue_medium_alpha_image_path: str = custom_field()
    background_filled_gray_heavy_alpha_bordered_image_path: str = custom_field()
    background_filled_gray_medium_alpha_bordered_image_path: str = custom_field()
    background_filled_white_image_path: str = custom_field()
    background_filled_white_medium_alpha_image_path: str = custom_field()
    background_plate_black_alpha_image_path: str = custom_field()
    background_plate_black_image_path: str = custom_field()
    background_plate_white_image_path: str = custom_field()
