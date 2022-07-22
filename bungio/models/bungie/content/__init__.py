# DO NOT CHANGE ANY CODE BELOW
# This file is generated automatically by `generate_api_schema.py` and will be overwritten
# Instead, change functions / models by subclassing them in the `./overwrites/` folder. They will be used instead.

from datetime import datetime
from typing import TYPE_CHECKING, Any, Optional, Union

import attr

from bungio.models.base import BaseEnum, BaseFlagEnum, BaseModel, ManifestModel
from bungio.utils import enum_converter

if TYPE_CHECKING:
    from bungio.models import GeneralUser


@attr.define
class ContentItemPublicContract(BaseModel):
    """
    _No description given by bungie._

    None
    Attributes:
        allow_comments: _No description given by bungie._
        author: _No description given by bungie._
        auto_english_property_fallback: _No description given by bungie._
        c_type: _No description given by bungie._
        cms_path: _No description given by bungie._
        comment_summary: _No description given by bungie._
        content_id: _No description given by bungie._
        creation_date: _No description given by bungie._
        has_age_gate: _No description given by bungie._
        minimum_age: _No description given by bungie._
        modify_date: _No description given by bungie._
        properties: Firehose content is really a collection of metadata and "properties", which are the potentially-but-not-strictly localizable data that comprises the meat of whatever content is being shown. As Cole Porter would have crooned, "Anything Goes" with Firehose properties. They are most often strings, but they can theoretically be anything. They are JSON encoded, and could be JSON structures, simple strings, numbers etc... The Content Type of the item (cType) will describe the properties, and thus how they ought to be deserialized.
        rating_image_path: _No description given by bungie._
        representations: _No description given by bungie._
        tags: NOTE: Tags will always be lower case.
    """

    allow_comments: bool = attr.field()
    author: "GeneralUser" = attr.field()
    auto_english_property_fallback: bool = attr.field()
    c_type: str = attr.field()
    cms_path: str = attr.field()
    comment_summary: "CommentSummary" = attr.field()
    content_id: int = attr.field()
    creation_date: datetime = attr.field()
    has_age_gate: bool = attr.field()
    minimum_age: int = attr.field()
    modify_date: datetime = attr.field()
    properties: dict[str, Any] = attr.field(metadata={"type": """dict[str, Any]"""})
    rating_image_path: str = attr.field()
    representations: list["ContentRepresentation"] = attr.field(metadata={"type": """list[ContentRepresentation]"""})
    tags: list[str] = attr.field(metadata={"type": """list[str]"""})


@attr.define
class ContentRepresentation(BaseModel):
    """
    _No description given by bungie._

    None
    Attributes:
        name: _No description given by bungie._
        path: _No description given by bungie._
        validation_string: _No description given by bungie._
    """

    name: str = attr.field()
    path: str = attr.field()
    validation_string: str = attr.field()


@attr.define
class CommentSummary(BaseModel):
    """
    _No description given by bungie._

    None
    Attributes:
        comment_count: _No description given by bungie._
        topic_id: _No description given by bungie._
    """

    comment_count: int = attr.field()
    topic_id: int = attr.field()


@attr.define
class NewsArticleRssResponse(BaseModel):
    """
    _No description given by bungie._

    None
    Attributes:
        current_pagination_token: _No description given by bungie._
        news_articles: _No description given by bungie._
        next_pagination_token: _No description given by bungie._
        result_count_this_page: _No description given by bungie._
    """

    current_pagination_token: int = attr.field()
    news_articles: list["NewsArticleRssItem"] = attr.field(metadata={"type": """list[NewsArticleRssItem]"""})
    next_pagination_token: int = attr.field()
    result_count_this_page: int = attr.field()


@attr.define
class NewsArticleRssItem(BaseModel):
    """
    _No description given by bungie._

    None
    Attributes:
        description: _No description given by bungie._
        link: _No description given by bungie._
        pub_date: _No description given by bungie._
        title: _No description given by bungie._
        unique_identifier: _No description given by bungie._
    """

    description: str = attr.field()
    link: str = attr.field()
    pub_date: datetime = attr.field()
    title: str = attr.field()
    unique_identifier: str = attr.field()
