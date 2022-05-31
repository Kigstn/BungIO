import datetime
from typing import TYPE_CHECKING, Any, Optional

import attr

from bungio.models.base import BaseEnum, BaseModel

if TYPE_CHECKING:
    from bungio.models import CommentSummary, ContentRepresentation, GeneralUser


@attr.define
class ContentItemPublicContract(BaseModel):
    """
    _No description given_

    Attributes:
        content_id: _No description given_
        c_type: _No description given_
        cms_path: _No description given_
        creation_date: _No description given_
        modify_date: _No description given_
        allow_comments: _No description given_
        has_age_gate: _No description given_
        minimum_age: _No description given_
        rating_image_path: _No description given_
        author: _No description given_
        auto_english_property_fallback: _No description given_
        properties: Firehose content is really a collection of metadata and "properties", which are the potentially-but-not-strictly localizable data that comprises the meat of whatever content is being shown. As Cole Porter would have crooned, "Anything Goes" with Firehose properties. They are most often strings, but they can theoretically be anything. They are JSON encoded, and could be JSON structures, simple strings, numbers etc... The Content Type of the item (cType) will describe the properties, and thus how they ought to be deserialized.
        representations: _No description given_
        tags: NOTE: Tags will always be lower case.
        comment_summary: _No description given_
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
    _No description given_

    Attributes:
        name: _No description given_
        path: _No description given_
        validation_string: _No description given_
    """

    name: str = attr.field()
    path: str = attr.field()
    validation_string: str = attr.field()


@attr.define
class CommentSummary(BaseModel):
    """
    _No description given_

    Attributes:
        topic_id: _No description given_
        comment_count: _No description given_
    """

    topic_id: int = attr.field()
    comment_count: int = attr.field()
