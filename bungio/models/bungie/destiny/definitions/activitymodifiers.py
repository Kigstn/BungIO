# DO NOT CHANGE ANY CODE BELOW
# This file is generated automatically by `generate_api_schema.py` and will be overwritten
# Instead, change functions / models by subclassing them in the `./overwrites/` folder. They will be used instead.

from typing import TYPE_CHECKING

import attr

from bungio.models.base import ManifestModel

if TYPE_CHECKING:
    from bungio.models import DestinyDisplayPropertiesDefinition


@attr.define
class DestinyActivityModifierDefinition(ManifestModel):
    """
    Modifiers - in Destiny 1, these were referred to as "Skulls" - are changes that can be applied to an Activity.

    None
    Attributes:
        display_in_activity_selection: _No description given by bungie._
        display_in_nav_mode: _No description given by bungie._
        display_properties: _No description given by bungie._
        hash: The unique identifier for this entity. Guaranteed to be unique for the type of entity, but not globally. When entities refer to each other in Destiny content, it is this hash that they are referring to.
        index: The index of the entity as it was found in the investment tables.
        redacted: If this is true, then there is an entity with this identifier/type combination, but BNet is not yet allowed to show it. Sorry!
    """

    display_in_activity_selection: bool = attr.field()
    display_in_nav_mode: bool = attr.field()
    display_properties: "DestinyDisplayPropertiesDefinition" = attr.field()
    hash: int = attr.field()
    index: int = attr.field()
    redacted: bool = attr.field()
