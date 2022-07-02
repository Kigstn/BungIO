# DO NOT CHANGE ANY CODE BELOW
# This file is generated automatically by `generate_api_schema.py` and will be overwritten
# Instead, change functions / models by subclassing them in the `./overwrites/` folder. They will be used instead.

import attr

from bungio.models.base import BaseModel


@attr.define
class DestinyManifest(BaseModel):
    """
    DestinyManifest is the external-facing contract for just the properties needed by those calling the Destiny Platform.

    None
    Attributes:
        icon_image_pyramid_info: Information about the "Image Pyramid" for Destiny icons. Where possible, we create smaller versions of Destiny icons. These are found as subfolders under the location of the "original/full size" Destiny images, with the same file name and extension as the original image itself. (this lets us avoid sending largely redundant path info with every entity, at the expense of the smaller versions of the image being less discoverable)
        json_world_component_content_paths: This points to the generated JSON that contains all the Definitions. Each key is a locale. The value is a dictionary, where the key is a definition type by name, and the value is the path to the file for that definition. WARNING: This is unsafe and subject to change - do not depend on data in these files staying around long-term.
        json_world_content_paths: This points to the generated JSON that contains all the Definitions. Each key is a locale. The value is a path to the aggregated world definitions (warning: large file!)
        mobile_asset_content_path: _No description given by bungie._
        mobile_clan_banner_database_path: _No description given by bungie._
        mobile_gear_asset_data_bases: _No description given by bungie._
        mobile_gear_c_d_n: _No description given by bungie._
        mobile_world_content_paths: _No description given by bungie._
        version: _No description given by bungie._
    """

    icon_image_pyramid_info: list["ImagePyramidEntry"] = attr.field(metadata={"type": """list[ImagePyramidEntry]"""})
    json_world_component_content_paths: dict[str, dict[str, str]] = attr.field(
        metadata={"type": """dict[str, dict[str, str]]"""}
    )
    json_world_content_paths: dict[str, str] = attr.field(metadata={"type": """dict[str, str]"""})
    mobile_asset_content_path: str = attr.field()
    mobile_clan_banner_database_path: str = attr.field()
    mobile_gear_asset_data_bases: list["GearAssetDataBaseDefinition"] = attr.field(
        metadata={"type": """list[GearAssetDataBaseDefinition]"""}
    )
    mobile_gear_c_d_n: dict[str, str] = attr.field(metadata={"type": """dict[str, str]"""})
    mobile_world_content_paths: dict[str, str] = attr.field(metadata={"type": """dict[str, str]"""})
    version: str = attr.field()


@attr.define
class GearAssetDataBaseDefinition(BaseModel):
    """
    _No description given by bungie._

    None
    Attributes:
        path: _No description given by bungie._
        version: _No description given by bungie._
    """

    path: str = attr.field()
    version: int = attr.field()


@attr.define
class ImagePyramidEntry(BaseModel):
    """
    _No description given by bungie._

    None
    Attributes:
        factor: The factor by which the original image size has been reduced.
        name: The name of the subfolder where these images are located.
    """

    factor: float = attr.field()
    name: str = attr.field()
