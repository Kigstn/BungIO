# DO NOT CHANGE ANY CODE BELOW
# This file is generated automatically by `generate_api_schema.py` and will be overwritten
# Instead, change functions / models by subclassing them in the `./overwrites/` folder. They will be used instead.

from typing import TYPE_CHECKING

from bungio.models.base import BaseModel, HashObject, ManifestModel, custom_define, custom_field

if TYPE_CHECKING:
    from bungio.models import DestinyDisplayPropertiesDefinition


@custom_define()
class DestinyReportReasonCategoryDefinition(ManifestModel, HashObject):
    """
    If you're going to report someone for a Terms of Service violation, you need to choose a category and reason for the report. This definition holds both the categories and the reasons within those categories, for simplicity and my own laziness' sake. Note tha this means that, to refer to a Reason by reasonHash, you need a combination of the reasonHash *and* the associated ReasonCategory's hash: there are some reasons defined under multiple categories.

    None
    Attributes:
        display_properties: _No description given by bungie._
        hash: The unique identifier for this entity. Guaranteed to be unique for the type of entity, but not globally. When entities refer to each other in Destiny content, it is this hash that they are referring to.
        index: The index of the entity as it was found in the investment tables.
        reasons: The specific reasons for the report under this category.
        redacted: If this is true, then there is an entity with this identifier/type combination, but BNet is not yet allowed to show it. Sorry!
    """

    display_properties: "DestinyDisplayPropertiesDefinition" = custom_field()
    index: int = custom_field()
    reasons: dict[int, "DestinyReportReasonDefinition"] = custom_field(
        metadata={"type": """dict[int, DestinyReportReasonDefinition]"""}
    )
    redacted: bool = custom_field()


@custom_define()
class DestinyReportReasonDefinition(BaseModel):
    """
    A specific reason for being banned. Only accessible under the related category (DestinyReportReasonCategoryDefinition) under which it is shown. Note that this means that report reasons' reasonHash are not globally unique: and indeed, entries like "Other" are defined under most categories for example.

    None
    Attributes:
        display_properties: _No description given by bungie._
        reason_hash: The identifier for the reason: they are only guaranteed unique under the Category in which they are found.
    """

    display_properties: "DestinyDisplayPropertiesDefinition" = custom_field()
    reason_hash: int = custom_field()
