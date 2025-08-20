# DO NOT CHANGE ANY CODE BELOW
# This file is generated automatically by `generate_api_schema.py` and will be overwritten
# Instead, change functions / models by subclassing them in the `./overwrites/` folder. They will be used instead.

from typing import TYPE_CHECKING

from bungio.models.base import HashObject, ManifestModel, custom_define, custom_field

if TYPE_CHECKING:
    from bungio.models import DestinyDisplayPropertiesDefinition


@custom_define()
class DestinyLoadoutColorDefinition(ManifestModel, HashObject):
    """
    _No description given by bungie._

    None
    Attributes:
        color_image_path: _No description given by bungie._
        hash: The unique identifier for this entity. Guaranteed to be unique for the type of entity, but not globally. When entities refer to each other in Destiny content, it is this hash that they are referring to.
        index: The index of the entity as it was found in the investment tables.
        redacted: If this is true, then there is an entity with this identifier/type combination, but BNet is not yet allowed to show it. Sorry!
    """

    color_image_path: str = custom_field()
    index: int = custom_field()
    redacted: bool = custom_field()


@custom_define()
class DestinyLoadoutIconDefinition(ManifestModel, HashObject):
    """
    _No description given by bungie._

    None
    Attributes:
        hash: The unique identifier for this entity. Guaranteed to be unique for the type of entity, but not globally. When entities refer to each other in Destiny content, it is this hash that they are referring to.
        icon_image_path: _No description given by bungie._
        index: The index of the entity as it was found in the investment tables.
        redacted: If this is true, then there is an entity with this identifier/type combination, but BNet is not yet allowed to show it. Sorry!
    """

    icon_image_path: str = custom_field()
    index: int = custom_field()
    redacted: bool = custom_field()


@custom_define()
class DestinyLoadoutNameDefinition(ManifestModel, HashObject):
    """
    _No description given by bungie._

    None
    Attributes:
        hash: The unique identifier for this entity. Guaranteed to be unique for the type of entity, but not globally. When entities refer to each other in Destiny content, it is this hash that they are referring to.
        index: The index of the entity as it was found in the investment tables.
        name: _No description given by bungie._
        redacted: If this is true, then there is an entity with this identifier/type combination, but BNet is not yet allowed to show it. Sorry!
    """

    index: int = custom_field()
    name: str = custom_field()
    redacted: bool = custom_field()


@custom_define()
class DestinyLoadoutConstantsDefinition(ManifestModel, HashObject):
    """
    _No description given by bungie._

    None
    Attributes:
        black_icon_image_path: This is a color-inverted version of the whiteIconImagePath.
        display_properties: _No description given by bungie._
        hash: The unique identifier for this entity. Guaranteed to be unique for the type of entity, but not globally. When entities refer to each other in Destiny content, it is this hash that they are referring to.
        index: The index of the entity as it was found in the investment tables.
        loadout_color_hashes: A list of the loadout color hashes in index order, for convenience.
        loadout_count_per_character: The maximum number of loadouts available to each character. The loadouts component API response can return fewer loadouts than this, as more loadouts are unlocked by reaching higher Guardian Ranks.
        loadout_icon_hashes: A list of the loadout icon hashes in index order, for convenience.
        loadout_name_hashes: A list of the loadout name hashes in index order, for convenience.
        loadout_preview_filter_out_socket_category_hashes: A list of the socket category hashes to be filtered out of loadout item preview displays.
        loadout_preview_filter_out_socket_type_hashes: A list of the socket type hashes to be filtered out of loadout item preview displays.
        redacted: If this is true, then there is an entity with this identifier/type combination, but BNet is not yet allowed to show it. Sorry!
        white_icon_image_path: This is the same icon as the one in the display properties, offered here as well with a more descriptive name.
    """

    black_icon_image_path: str = custom_field()
    display_properties: "DestinyDisplayPropertiesDefinition" = custom_field()
    index: int = custom_field()
    loadout_color_hashes: list[int] = custom_field(metadata={"type": """list[int]"""})
    loadout_count_per_character: int = custom_field()
    loadout_icon_hashes: list[int] = custom_field(metadata={"type": """list[int]"""})
    loadout_name_hashes: list[int] = custom_field(metadata={"type": """list[int]"""})
    loadout_preview_filter_out_socket_category_hashes: list[int] = custom_field(metadata={"type": """list[int]"""})
    loadout_preview_filter_out_socket_type_hashes: list[int] = custom_field(metadata={"type": """list[int]"""})
    redacted: bool = custom_field()
    white_icon_image_path: str = custom_field()
