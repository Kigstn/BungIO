from typing import TYPE_CHECKING

import attr

from bungio.models.base import BaseModel

if TYPE_CHECKING:
    from bungio.models import DestinyDisplayPropertiesDefinition


@attr.define
class DestinyTraitDefinition(BaseModel):
    """
    _No description given by bungie_

    Attributes:
        display_properties: _No description given by bungie_
        trait_category_id: _No description given by bungie_
        trait_category_hash: _No description given by bungie_
        display_hint: An identifier for how this trait can be displayed. For example: a 'keyword' hint to show an explanation for certain related terms.
        hash: The unique identifier for this entity. Guaranteed to be unique for the type of entity, but not globally. When entities refer to each other in Destiny content, it is this hash that they are referring to.
        index: The index of the entity as it was found in the investment tables.
        redacted: If this is true, then there is an entity with this identifier/type combination, but BNet is not yet allowed to show it. Sorry!
    """

    display_properties: "DestinyDisplayPropertiesDefinition" = attr.field()
    trait_category_id: str = attr.field()
    trait_category_hash: "DestinyTraitCategoryDefinition" = attr.field()
    display_hint: str = attr.field()
    hash: int = attr.field()
    index: int = attr.field()
    redacted: bool = attr.field()


@attr.define
class DestinyTraitCategoryDefinition(BaseModel):
    """
    _No description given by bungie_

    Attributes:
        trait_category_id: _No description given by bungie_
        trait_hashes: _No description given by bungie_
        trait_ids: _No description given by bungie_
        hash: The unique identifier for this entity. Guaranteed to be unique for the type of entity, but not globally. When entities refer to each other in Destiny content, it is this hash that they are referring to.
        index: The index of the entity as it was found in the investment tables.
        redacted: If this is true, then there is an entity with this identifier/type combination, but BNet is not yet allowed to show it. Sorry!
    """

    trait_category_id: str = attr.field()
    trait_hashes: list["DestinyTraitDefinition"] = attr.field()
    trait_ids: list[str] = attr.field()
    hash: int = attr.field()
    index: int = attr.field()
    redacted: bool = attr.field()
