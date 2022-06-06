from typing import TYPE_CHECKING

import attr

from bungio.models.base import BaseModel

if TYPE_CHECKING:
    from bungio.models import (
        DestinyInventoryItemDefinition,
        DestinyPlugSetDefinition,
        DestinyPresentationNodeDefinition,
    )


@attr.define
class DestinyCraftablesComponent(BaseModel):
    """
    _No description given by bungie_

    Attributes:
        craftables: A map of craftable item hashes to craftable item state components.
        crafting_root_node_hash: The hash for the root presentation node definition of craftable item categories.
    """

    craftables: "DestinyInventoryItemDefinition" = attr.field()
    crafting_root_node_hash: "DestinyPresentationNodeDefinition" = attr.field()


@attr.define
class DestinyCraftableComponent(BaseModel):
    """
    _No description given by bungie_

    Attributes:
        visible: _No description given by bungie_
        failed_requirement_indexes: If the requirements are not met for crafting this item, these will index into the list of failure strings.
        sockets: Plug item state for the crafting sockets.
    """

    visible: bool = attr.field()
    failed_requirement_indexes: list[int] = attr.field()
    sockets: list["DestinyCraftableSocketComponent"] = attr.field()


@attr.define
class DestinyCraftableSocketComponent(BaseModel):
    """
    _No description given by bungie_

    Attributes:
        plug_set_hash: _No description given by bungie_
        plugs: Unlock state for plugs in the socket plug set definition
    """

    plug_set_hash: "DestinyPlugSetDefinition" = attr.field()
    plugs: list["DestinyCraftableSocketPlugComponent"] = attr.field()


@attr.define
class DestinyCraftableSocketPlugComponent(BaseModel):
    """
    _No description given by bungie_

    Attributes:
        plug_item_hash: _No description given by bungie_
        failed_requirement_indexes: Index into the unlock requirements to display failure descriptions
    """

    plug_item_hash: "DestinyInventoryItemDefinition" = attr.field()
    failed_requirement_indexes: list[int] = attr.field()
