from typing import Any

import attr

from bungio.models.base import BaseModel


@attr.define
class DestinyPlatformSilverComponent(BaseModel):
    """
    _No description given by bungie_

    Attributes:
        platform_silver: If a Profile is played on multiple platforms, this is the silver they have for each platform, keyed by Membership Type.
    """

    platform_silver: Any = attr.field()


@attr.define
class DestinyCurrenciesComponent(BaseModel):
    """
    This component provides a quick lookup of every item the requested character has and how much of that item they have. Requesting this component will allow you to circumvent manually putting together the list of which currencies you have for the purpose of testing currency requirements on an item being purchased, or operations that have costs. You *could* figure this out yourself by doing a GetCharacter or GetProfile request and forming your own lookup table, but that is inconvenient enough that this feels like a worthwhile (and optional) redundency. Don't bother requesting it if you have already created your own lookup from prior GetCharacter/GetProfile calls.

    Attributes:
        item_quantities: A dictionary - keyed by the item's hash identifier (DestinyInventoryItemDefinition), and whose value is the amount of that item you have across all available inventory buckets for purchasing. This allows you to see whether the requesting character can afford any given purchase/action without having to re-create this list itself.
    """

    item_quantities: Any = attr.field()
