import datetime
from typing import TYPE_CHECKING, Any, Optional

import attr

from bungio.models.base import BaseEnum, BaseModel


@attr.define
class DestinyCraftablesComponent(BaseModel):
    """
    Not specified.

    Attributes:
        craftables: A map of craftable item hashes to craftable item state components.
        crafting_root_node_hash: The hash for the root presentation node definition of craftable item categories.
    """

    craftables: Any = attr.field()
    crafting_root_node_hash: int = attr.field()


@attr.define
class DestinyCraftableComponent(BaseModel):
    """
    Not specified.

    Attributes:
        visible: Not specified.
        failed_requirement_indexes: If the requirements are not met for crafting this item, these will index into the list of failure strings.
        sockets: Plug item state for the crafting sockets.
    """

    visible: bool = attr.field()
    failed_requirement_indexes: list[int] = attr.field()
    sockets: list["DestinyCraftableSocketComponent"] = attr.field()


@attr.define
class DestinyCraftableSocketComponent(BaseModel):
    """
    Not specified.

    Attributes:
        plug_set_hash: Not specified.
        plugs: Unlock state for plugs in the socket plug set definition
    """

    plug_set_hash: int = attr.field()
    plugs: list["DestinyCraftableSocketPlugComponent"] = attr.field()


@attr.define
class DestinyCraftableSocketPlugComponent(BaseModel):
    """
    Not specified.

    Attributes:
        plug_item_hash: Not specified.
        failed_requirement_indexes: Index into the unlock requirements to display failure descriptions
    """

    plug_item_hash: int = attr.field()
    failed_requirement_indexes: list[int] = attr.field()
