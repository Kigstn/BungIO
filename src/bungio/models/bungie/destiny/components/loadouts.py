# DO NOT CHANGE ANY CODE BELOW
# This file is generated automatically by `generate_api_schema.py` and will be overwritten
# Instead, change functions / models by subclassing them in the `./overwrites/` folder. They will be used instead.

from typing import Optional, TYPE_CHECKING

from bungio.models.base import BaseModel, custom_define, custom_field


if TYPE_CHECKING:
    from bungio.models import DestinyLoadoutColorDefinition
    from bungio.models import DestinyLoadoutIconDefinition
    from bungio.models import DestinyLoadoutNameDefinition


@custom_define()
class DestinyLoadoutsComponent(BaseModel):
    """
    _No description given by bungie._

    None
    Attributes:
        loadouts: _No description given by bungie._
    """

    loadouts: list["DestinyLoadoutComponent"] = custom_field(metadata={"type": """list[DestinyLoadoutComponent]"""})


@custom_define()
class DestinyLoadoutComponent(BaseModel):
    """
    _No description given by bungie._

    Tip: Manifest Information
        This model has some attributes which can be filled with additional information found in the manifest (`manifest_...`).
        Without additional work, these attributes will be `None`, since they require additional requests and database lookups.

        To fill the manifest dependent attributes, either:

        - Run `await ThisClass.fetch_manifest_information()`, see [here](/API Reference/Models/base)
        - Set `Client.always_return_manifest_information` to `True`, see [here](/API Reference/client)

    Attributes:
        color_hash: _No description given by bungie._
        icon_hash: _No description given by bungie._
        items: _No description given by bungie._
        name_hash: _No description given by bungie._
        manifest_color_hash: Manifest information for `color_hash`
        manifest_icon_hash: Manifest information for `icon_hash`
        manifest_name_hash: Manifest information for `name_hash`
    """

    color_hash: int = custom_field()
    icon_hash: int = custom_field()
    items: list["DestinyLoadoutItemComponent"] = custom_field(
        metadata={"type": """list[DestinyLoadoutItemComponent]"""}
    )
    name_hash: int = custom_field()
    manifest_color_hash: Optional["DestinyLoadoutColorDefinition"] = custom_field(default=None)
    manifest_icon_hash: Optional["DestinyLoadoutIconDefinition"] = custom_field(default=None)
    manifest_name_hash: Optional["DestinyLoadoutNameDefinition"] = custom_field(default=None)


@custom_define()
class DestinyLoadoutItemComponent(BaseModel):
    """
    _No description given by bungie._

    None
    Attributes:
        item_instance_id: _No description given by bungie._
        plug_item_hashes: _No description given by bungie._
    """

    item_instance_id: int = custom_field(metadata={"int64": True})
    plug_item_hashes: list[int] = custom_field(metadata={"type": """list[int]"""})
