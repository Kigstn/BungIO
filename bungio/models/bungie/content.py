import datetime
from typing import TYPE_CHECKING, Any, Optional

import attr

from bungio.models.base import BaseEnum, BaseModel


@attr.define
class ContentItemPublicContract(BaseModel):
    """
        Not specified.

        Attributes:
            content_id: Not specified.
            c_type: Not specified.
            cms_path: Not specified.
            creation_date: Not specified.
            modify_date: Not specified.
            allow_comments: Not specified.
            has_age_gate: Not specified.
            minimum_age: Not specified.
            rating_image_path: Not specified.
            author: Not specified.
            auto_english_property_fallback: Not specified.
            properties: Firehose content is really a collection of metadata and "properties", which are the potentially-but-not-strictly localizable data that comprises the meat of whatever content is being shown.

    As Cole Porter would have crooned, "Anything Goes" with Firehose properties. They are most often strings, but they can theoretically be anything. They are JSON encoded, and could be JSON structures, simple strings, numbers etc... The Content Type of the item (cType) will describe the properties, and thus how they ought to be deserialized.
            representations: Not specified.
            tags: NOTE: Tags will always be lower case.
            comment_summary: Not specified.
    """

    content_id: int = attr.field()
    c_type: str = attr.field()
    cms_path: str = attr.field()
    creation_date: datetime.datetime = attr.field()
    modify_date: datetime.datetime = attr.field()
    allow_comments: bool = attr.field()
    has_age_gate: bool = attr.field()
    minimum_age: int = attr.field()
    rating_image_path: str = attr.field()
    author: "GeneralUser" = attr.field()
    auto_english_property_fallback: bool = attr.field()
    properties: Any = attr.field()
    representations: list["ContentRepresentation"] = attr.field()
    tags: list[str] = attr.field()
    comment_summary: "CommentSummary" = attr.field()


@attr.define
class ContentRepresentation(BaseModel):
    """
    Not specified.

    Attributes:
        name: Not specified.
        path: Not specified.
        validation_string: Not specified.
    """

    name: str = attr.field()
    path: str = attr.field()
    validation_string: str = attr.field()


@attr.define
class CommentSummary(BaseModel):
    """
    Not specified.

    Attributes:
        topic_id: Not specified.
        comment_count: Not specified.
    """

    topic_id: int = attr.field()
    comment_count: int = attr.field()
