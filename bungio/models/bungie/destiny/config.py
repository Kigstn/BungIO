from typing import TYPE_CHECKING, Any

import attr

from bungio.models.base import BaseModel

if TYPE_CHECKING:
    from bungio.models import GearAssetDataBaseDefinition, ImagePyramidEntry


@attr.define
class DestinyManifest(BaseModel):
    """
    DestinyManifest is the external-facing contract for just the properties needed by those calling the Destiny Platform.

    Attributes:
        version: _No description given by bungie_
        mobile_asset_content_path: _No description given by bungie_
        mobile_gear_asset_data_bases: _No description given by bungie_
        mobile_world_content_paths: _No description given by bungie_
        json_world_content_paths: This points to the generated JSON that contains all the Definitions. Each key is a locale. The value is a path to the aggregated world definitions (warning: large file!)
        json_world_component_content_paths: This points to the generated JSON that contains all the Definitions. Each key is a locale. The value is a dictionary, where the key is a definition type by name, and the value is the path to the file for that definition. WARNING: This is unsafe and subject to change - do not depend on data in these files staying around long-term.
        mobile_clan_banner_database_path: _No description given by bungie_
        mobile_gear_c_d_n: _No description given by bungie_
        icon_image_pyramid_info: Information about the "Image Pyramid" for Destiny icons. Where possible, we create smaller versions of Destiny icons. These are found as subfolders under the location of the "original/full size" Destiny images, with the same file name and extension as the original image itself. (this lets us avoid sending largely redundant path info with every entity, at the expense of the smaller versions of the image being less discoverable)
    """

    version: str = attr.field()
    mobile_asset_content_path: str = attr.field()
    mobile_gear_asset_data_bases: list["GearAssetDataBaseDefinition"] = attr.field()
    mobile_world_content_paths: Any = attr.field()
    json_world_content_paths: Any = attr.field()
    json_world_component_content_paths: Any = attr.field()
    mobile_clan_banner_database_path: str = attr.field()
    mobile_gear_c_d_n: Any = attr.field()
    icon_image_pyramid_info: list["ImagePyramidEntry"] = attr.field()


@attr.define
class GearAssetDataBaseDefinition(BaseModel):
    """
    _No description given by bungie_

    Attributes:
        version: _No description given by bungie_
        path: _No description given by bungie_
    """

    version: int = attr.field()
    path: str = attr.field()


@attr.define
class ImagePyramidEntry(BaseModel):
    """
    _No description given by bungie_

    Attributes:
        name: The name of the subfolder where these images are located.
        factor: The factor by which the original image size has been reduced.
    """

    name: str = attr.field()
    factor: float = attr.field()
