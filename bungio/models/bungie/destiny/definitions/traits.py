import datetime
from typing import TYPE_CHECKING, Any, Optional

import attr

from bungio.models.base import BaseEnum, BaseModel


@attr.define
class DestinyTraitDefinition(BaseModel):
    """
        Not specified.

        Attributes:
            display_properties: Not specified.
            trait_category_id: Not specified.
            trait_category_hash: Not specified.
            display_hint: An identifier for how this trait can be displayed. For example: a 'keyword' hint to show an explanation for certain related terms.
            hash: The unique identifier for this entity. Guaranteed to be unique for the type of entity, but not globally.

    When entities refer to each other in Destiny content, it is this hash that they are referring to.
            index: The index of the entity as it was found in the investment tables.
            redacted: If this is true, then there is an entity with this identifier/type combination, but BNet is not yet allowed to show it. Sorry!
    """

    display_properties: "DestinyDisplayPropertiesDefinition" = attr.field()
    trait_category_id: str = attr.field()
    trait_category_hash: int = attr.field()
    display_hint: str = attr.field()
    hash: int = attr.field()
    index: int = attr.field()
    redacted: bool = attr.field()


@attr.define
class DestinyTraitCategoryDefinition(BaseModel):
    """
        Not specified.

        Attributes:
            trait_category_id: Not specified.
            trait_hashes: Not specified.
            trait_ids: Not specified.
            hash: The unique identifier for this entity. Guaranteed to be unique for the type of entity, but not globally.

    When entities refer to each other in Destiny content, it is this hash that they are referring to.
            index: The index of the entity as it was found in the investment tables.
            redacted: If this is true, then there is an entity with this identifier/type combination, but BNet is not yet allowed to show it. Sorry!
    """

    trait_category_id: str = attr.field()
    trait_hashes: list[int] = attr.field()
    trait_ids: list[str] = attr.field()
    hash: int = attr.field()
    index: int = attr.field()
    redacted: bool = attr.field()
