# DO NOT CHANGE ANY CODE BELOW
# This file is generated automatically by `generate_api_schema.py` and will be overwritten
# Instead, change functions / models by subclassing them in the `./overwrites/` folder. They will be used instead.

from typing import TYPE_CHECKING, Optional

import attr

from bungio.models.base import ManifestModel

if TYPE_CHECKING:
    from bungio.models import DestinyDisplayPropertiesDefinition


@attr.define
class DestinyTraitDefinition(ManifestModel):
    """
    _No description given by bungie._

    Tip: Manifest Information
        This model has some attributes which can be filled with additional information found in the manifest (`manifest_...`).
        Without additional work, these attributes will be `None`, since they require additional requests and database lookups.

        To fill the manifest dependent attributes, either:

        - Run `await ThisClass.fetch_manifest_information()`, see [here](/API Reference/Models/base)
        - Set `Client.always_return_manifest_information` to `True`, see [here](/API Reference/client)

    Attributes:
        display_hint: An identifier for how this trait can be displayed. For example: a 'keyword' hint to show an explanation for certain related terms.
        display_properties: _No description given by bungie._
        hash: The unique identifier for this entity. Guaranteed to be unique for the type of entity, but not globally. When entities refer to each other in Destiny content, it is this hash that they are referring to.
        index: The index of the entity as it was found in the investment tables.
        redacted: If this is true, then there is an entity with this identifier/type combination, but BNet is not yet allowed to show it. Sorry!
        trait_category_hash: _No description given by bungie._
        trait_category_id: _No description given by bungie._
        manifest_trait_category_hash: Manifest information for `trait_category_hash`
    """

    display_hint: str = attr.field()
    display_properties: "DestinyDisplayPropertiesDefinition" = attr.field()
    hash: int = attr.field()
    index: int = attr.field()
    redacted: bool = attr.field()
    trait_category_hash: int = attr.field()
    trait_category_id: str = attr.field()
    manifest_trait_category_hash: Optional["DestinyTraitCategoryDefinition"] = attr.field(default=None)


@attr.define
class DestinyTraitCategoryDefinition(ManifestModel):
    """
    _No description given by bungie._

    None
    Attributes:
        hash: The unique identifier for this entity. Guaranteed to be unique for the type of entity, but not globally. When entities refer to each other in Destiny content, it is this hash that they are referring to.
        index: The index of the entity as it was found in the investment tables.
        redacted: If this is true, then there is an entity with this identifier/type combination, but BNet is not yet allowed to show it. Sorry!
        trait_category_id: _No description given by bungie._
        trait_hashes: _No description given by bungie._
        trait_ids: _No description given by bungie._
    """

    hash: int = attr.field()
    index: int = attr.field()
    redacted: bool = attr.field()
    trait_category_id: str = attr.field()
    trait_hashes: list[int] = attr.field(metadata={"type": """list[int]"""})
    trait_ids: list[str] = attr.field(metadata={"type": """list[str]"""})
