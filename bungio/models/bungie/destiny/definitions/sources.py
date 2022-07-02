# DO NOT CHANGE ANY CODE BELOW
# This file is generated automatically by `generate_api_schema.py` and will be overwritten
# Instead, change functions / models by subclassing them in the `./overwrites/` folder. They will be used instead.

from typing import TYPE_CHECKING

import attr

from bungio.models.base import BaseModel

if TYPE_CHECKING:
    from bungio.models import DestinyInventoryItemStatDefinition


@attr.define
class DestinyItemSourceDefinition(BaseModel):
    """
    Properties of a DestinyInventoryItemDefinition that store all of the information we were able to discern about how the item spawns, and where you can find the item. Items will have many of these sources, one per level at which it spawns, to try and give more granular data about where items spawn for specific level ranges.

    None
    Attributes:
        computed_stats: The stats computed for this level/quality range.
        level: The level at which the item spawns. Essentially the Primary Key for this source data: there will be multiple of these source entries per item that has source data, grouped by the level at which the item spawns.
        max_level_required: The maximum Character Level required for equipping the item when the item spawns at the item level defined on this DestinyItemSourceDefinition, as far as we saw in our processing.
        max_quality: The maximum quality at which the item spawns for this level.
        min_level_required: The minimum Character Level required for equipping the item when the item spawns at the item level defined on this DestinyItemSourceDefinition, as far as we saw in our processing.
        min_quality: The minimum Quality at which the item spawns for this level. Examine DestinyInventoryItemDefinition for more information about what Quality means. Just don't ask Phaedrus about it, he'll never stop talking and you'll have to write a book about it.
        source_hashes: The DestinyRewardSourceDefinitions found that can spawn the item at this level.
    """

    computed_stats: dict[int, "DestinyInventoryItemStatDefinition"] = attr.field(
        metadata={"type": """dict[int, DestinyInventoryItemStatDefinition]"""}
    )
    level: int = attr.field()
    max_level_required: int = attr.field()
    max_quality: int = attr.field()
    min_level_required: int = attr.field()
    min_quality: int = attr.field()
    source_hashes: list[int] = attr.field(metadata={"type": """list[int]"""})
