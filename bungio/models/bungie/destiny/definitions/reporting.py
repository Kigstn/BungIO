import datetime
from typing import TYPE_CHECKING, Any, Optional

import attr

from bungio.models.base import BaseEnum, BaseModel


@attr.define
class DestinyReportReasonCategoryDefinition(BaseModel):
    """
        If you're going to report someone for a Terms of Service violation, you need to choose a category and reason for the report. This definition holds both the categories and the reasons within those categories, for simplicity and my own laziness' sake.

    Note tha this means that, to refer to a Reason by reasonHash, you need a combination of the reasonHash *and* the associated ReasonCategory's hash: there are some reasons defined under multiple categories.

        Attributes:
            display_properties: Not specified.
            reasons: The specific reasons for the report under this category.
            hash: The unique identifier for this entity. Guaranteed to be unique for the type of entity, but not globally.

    When entities refer to each other in Destiny content, it is this hash that they are referring to.
            index: The index of the entity as it was found in the investment tables.
            redacted: If this is true, then there is an entity with this identifier/type combination, but BNet is not yet allowed to show it. Sorry!
    """

    display_properties: "DestinyDisplayPropertiesDefinition" = attr.field()
    reasons: Any = attr.field()
    hash: int = attr.field()
    index: int = attr.field()
    redacted: bool = attr.field()


@attr.define
class DestinyReportReasonDefinition(BaseModel):
    """
    A specific reason for being banned. Only accessible under the related category (DestinyReportReasonCategoryDefinition) under which it is shown. Note that this means that report reasons' reasonHash are not globally unique: and indeed, entries like "Other" are defined under most categories for example.

    Attributes:
        reason_hash: The identifier for the reason: they are only guaranteed unique under the Category in which they are found.
        display_properties: Not specified.
    """

    reason_hash: int = attr.field()
    display_properties: "DestinyDisplayPropertiesDefinition" = attr.field()
