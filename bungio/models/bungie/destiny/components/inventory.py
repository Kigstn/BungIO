# DO NOT CHANGE ANY CODE BELOW
# This file is generated automatically by `generate_api_schema.py` and will be overwritten
# Instead, change functions / models by subclassing them in the `./overwrites/` folder. They will be used instead.

from typing import TYPE_CHECKING, Union

from bungio.models.base import BaseModel, custom_define, custom_field

if TYPE_CHECKING:
    from bungio.models import BungieMembershipType, DestinyItemComponent


@custom_define()
class DestinyPlatformSilverComponent(BaseModel):
    """
    _No description given by bungie._

    None
    Attributes:
        platform_silver: If a Profile is played on multiple platforms, this is the silver they have for each platform, keyed by Membership Type.
    """

    platform_silver: dict[Union["BungieMembershipType", int], "DestinyItemComponent"] = custom_field(
        metadata={"type": """dict[BungieMembershipType, DestinyItemComponent]"""}
    )


@custom_define()
class DestinyCurrenciesComponent(BaseModel):
    """
    This component provides a quick lookup of every item the requested character has and how much of that item they have. Requesting this component will allow you to circumvent manually putting together the list of which currencies you have for the purpose of testing currency requirements on an item being purchased, or operations that have costs. You *could* figure this out yourself by doing a GetCharacter or GetProfile request and forming your own lookup table, but that is inconvenient enough that this feels like a worthwhile (and optional) redundency. Don't bother requesting it if you have already created your own lookup from prior GetCharacter/GetProfile calls.

    None
    Attributes:
        item_quantities: A dictionary - keyed by the item's hash identifier (DestinyInventoryItemDefinition), and whose value is the amount of that item you have across all available inventory buckets for purchasing. This allows you to see whether the requesting character can afford any given purchase/action without having to re-create this list itself.
    """

    item_quantities: dict[int, int] = custom_field(metadata={"type": """dict[int, int]"""})
