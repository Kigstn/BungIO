# DO NOT CHANGE ANY CODE BELOW
# This file is generated automatically by `generate_api_schema.py` and will be overwritten
# Instead, change functions / models by subclassing them in the `./overwrites/` folder. They will be used instead.

from datetime import datetime
from typing import Optional, Any, Union, TYPE_CHECKING

from bungio.utils import enum_converter
from bungio.models.base import BaseModel, BaseEnum, BaseFlagEnum, HashObject, ManifestModel, custom_define, custom_field


if TYPE_CHECKING:
    from bungio.models import GeneralUser


@custom_define()
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

    allow_comments: bool = custom_field()
    author: "GeneralUser" = custom_field()
    auto_english_property_fallback: bool = custom_field()
    c_type: str = custom_field()
    cms_path: str = custom_field()
    comment_summary: "CommentSummary" = custom_field()
    content_id: int = custom_field(metadata={"int64": True})
    creation_date: datetime = custom_field()
    has_age_gate: bool = custom_field()
    minimum_age: int = custom_field()
    modify_date: datetime = custom_field()
    properties: dict[str, Any] = custom_field(metadata={"type": """dict[str, Any]"""})
    rating_image_path: str = custom_field()
    representations: list["ContentRepresentation"] = custom_field(metadata={"type": """list[ContentRepresentation]"""})
    tags: list[str] = custom_field(metadata={"type": """list[str]"""})


@custom_define()
class ContentRepresentation(BaseModel):
    """
    _No description given by bungie._

    None
    Attributes:
        name: _No description given by bungie._
        path: _No description given by bungie._
        validation_string: _No description given by bungie._
    """

    name: str = custom_field()
    path: str = custom_field()
    validation_string: str = custom_field()


@custom_define()
class CommentSummary(BaseModel):
    """
    _No description given by bungie._

    None
    Attributes:
        comment_count: _No description given by bungie._
        topic_id: _No description given by bungie._
    """

    comment_count: int = custom_field()
    topic_id: int = custom_field(metadata={"int64": True})


@custom_define()
class NewsArticleRssResponse(BaseModel):
    """
    _No description given by bungie._

    None
    Attributes:
        category_filter: _No description given by bungie._
        current_pagination_token: _No description given by bungie._
        news_articles: _No description given by bungie._
        next_pagination_token: _No description given by bungie._
        pager_action: _No description given by bungie._
        result_count_this_page: _No description given by bungie._
    """

    category_filter: str = custom_field()
    current_pagination_token: int = custom_field()
    news_articles: list["NewsArticleRssItem"] = custom_field(metadata={"type": """list[NewsArticleRssItem]"""})
    next_pagination_token: int = custom_field()
    pager_action: str = custom_field()
    result_count_this_page: int = custom_field()


@custom_define()
class NewsArticleRssItem(BaseModel):
    """
    _No description given by bungie._

    None
    Attributes:
        description: _No description given by bungie._
        html_content: _No description given by bungie._
        image_path: _No description given by bungie._
        link: _No description given by bungie._
        optional_mobile_image_path: _No description given by bungie._
        pub_date: _No description given by bungie._
        title: _No description given by bungie._
        unique_identifier: _No description given by bungie._
    """

    description: str = custom_field()
    html_content: str = custom_field()
    image_path: str = custom_field()
    link: str = custom_field()
    optional_mobile_image_path: str = custom_field()
    pub_date: datetime = custom_field()
    title: str = custom_field()
    unique_identifier: str = custom_field()
