from typing import TYPE_CHECKING

import attr

from bungio.models.base import BaseModel

if TYPE_CHECKING:
    from bungio.models import DestinyInventoryItemDefinition, DestinyObjectiveProgress


@attr.define
class DestinyItemPlugBase(BaseModel):
    """
    _No description given by bungie_

    Attributes:
        plug_item_hash: The hash identifier of the DestinyInventoryItemDefinition that represents this plug.
        can_insert: If true, this plug has met all of its insertion requirements. Big if true.
        enabled: If true, this plug will provide its benefits while inserted.
        insert_fail_indexes: If the plug cannot be inserted for some reason, this will have the indexes into the plug item definition's plug.insertionRules property, so you can show the reasons why it can't be inserted. This list will be empty if the plug can be inserted.
        enable_fail_indexes: If a plug is not enabled, this will be populated with indexes into the plug item definition's plug.enabledRules property, so that you can show the reasons why it is not enabled. This list will be empty if the plug is enabled.
    """

    plug_item_hash: "DestinyInventoryItemDefinition" = attr.field()
    can_insert: bool = attr.field()
    enabled: bool = attr.field()
    insert_fail_indexes: list[int] = attr.field()
    enable_fail_indexes: list[int] = attr.field()


@attr.define
class DestinyItemPlug(BaseModel):
    """
    _No description given by bungie_

    Attributes:
        plug_objectives: Sometimes, Plugs may have objectives: these are often used for flavor and display purposes, but they can be used for any arbitrary purpose (both fortunately and unfortunately). Recently (with Season 2) they were expanded in use to be used as the "gating" for whether the plug can be inserted at all. For instance, a Plug might be tracking the number of PVP kills you have made. It will use the parent item's data about that tracking status to determine what to show, and will generally show it using the DestinyObjectiveDefinition's progressDescription property. Refer to the plug's itemHash and objective property for more information if you would like to display even more data.
        plug_item_hash: The hash identifier of the DestinyInventoryItemDefinition that represents this plug.
        can_insert: If true, this plug has met all of its insertion requirements. Big if true.
        enabled: If true, this plug will provide its benefits while inserted.
        insert_fail_indexes: If the plug cannot be inserted for some reason, this will have the indexes into the plug item definition's plug.insertionRules property, so you can show the reasons why it can't be inserted. This list will be empty if the plug can be inserted.
        enable_fail_indexes: If a plug is not enabled, this will be populated with indexes into the plug item definition's plug.enabledRules property, so that you can show the reasons why it is not enabled. This list will be empty if the plug is enabled.
    """

    plug_objectives: list["DestinyObjectiveProgress"] = attr.field()
    plug_item_hash: "DestinyInventoryItemDefinition" = attr.field()
    can_insert: bool = attr.field()
    enabled: bool = attr.field()
    insert_fail_indexes: list[int] = attr.field()
    enable_fail_indexes: list[int] = attr.field()
