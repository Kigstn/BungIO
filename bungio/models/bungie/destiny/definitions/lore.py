# DO NOT CHANGE ANY CODE BELOW
# This file is generated automatically by `generate_api_schema.py` and will be overwritten
# Instead, change functions / models by subclassing them in the `./overwrites/` folder. They will be used instead.

from typing import TYPE_CHECKING

import attr

from bungio.models.base import ManifestModel

if TYPE_CHECKING:
    from bungio.models import DestinyDisplayPropertiesDefinition


@attr.define
class DestinyLoreDefinition(ManifestModel):
    """
    These are definitions for in-game "Lore," meant to be narrative enhancements of the game experience. DestinyInventoryItemDefinitions for interesting items point to these definitions, but nothing's stopping you from scraping all of these and doing something cool with them. If they end up having cool data.

    None
    Attributes:
        display_properties: _No description given by bungie._
        hash: The unique identifier for this entity. Guaranteed to be unique for the type of entity, but not globally. When entities refer to each other in Destiny content, it is this hash that they are referring to.
        index: The index of the entity as it was found in the investment tables.
        redacted: If this is true, then there is an entity with this identifier/type combination, but BNet is not yet allowed to show it. Sorry!
        subtitle: _No description given by bungie._
    """

    display_properties: "DestinyDisplayPropertiesDefinition" = attr.field()
    hash: int = attr.field()
    index: int = attr.field()
    redacted: bool = attr.field()
    subtitle: str = attr.field()
