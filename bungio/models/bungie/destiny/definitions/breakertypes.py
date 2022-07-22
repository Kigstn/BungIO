# DO NOT CHANGE ANY CODE BELOW
# This file is generated automatically by `generate_api_schema.py` and will be overwritten
# Instead, change functions / models by subclassing them in the `./overwrites/` folder. They will be used instead.

from typing import TYPE_CHECKING, Union

import attr

from bungio.models.base import ManifestModel
from bungio.utils import enum_converter

if TYPE_CHECKING:
    from bungio.models import DestinyBreakerType, DestinyDisplayPropertiesDefinition


@attr.define
class DestinyBreakerTypeDefinition(ManifestModel):
    """
    _No description given by bungie._

    None
    Attributes:
        display_properties: _No description given by bungie._
        enum_value: We have an enumeration for Breaker types for quick reference. This is the current definition's breaker type enum value.
        hash: The unique identifier for this entity. Guaranteed to be unique for the type of entity, but not globally. When entities refer to each other in Destiny content, it is this hash that they are referring to.
        index: The index of the entity as it was found in the investment tables.
        redacted: If this is true, then there is an entity with this identifier/type combination, but BNet is not yet allowed to show it. Sorry!
    """

    display_properties: "DestinyDisplayPropertiesDefinition" = attr.field()
    enum_value: Union["DestinyBreakerType", int] = attr.field(converter=enum_converter("DestinyBreakerType"))
    hash: int = attr.field()
    index: int = attr.field()
    redacted: bool = attr.field()
