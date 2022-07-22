# DO NOT CHANGE ANY CODE BELOW
# This file is generated automatically by `generate_api_schema.py` and will be overwritten
# Instead, change functions / models by subclassing them in the `./overwrites/` folder. They will be used instead.

from datetime import datetime
from typing import TYPE_CHECKING, Union

import attr

from bungio.models.base import BaseEnum, BaseModel
from bungio.utils import enum_converter

if TYPE_CHECKING:
    from bungio.models import (
        ContentItemPublicContract,
        DestinyMilestoneContent,
        DestinyPublicActivityStatus,
        DestinyPublicMilestone,
        SearchResultOfTrendingEntry,
    )


@attr.define
class TrendingCategories(BaseModel):
    """
    _No description given by bungie._

    None
    Attributes:
        categories: _No description given by bungie._
    """

    categories: list["TrendingCategory"] = attr.field(metadata={"type": """list[TrendingCategory]"""})


@attr.define
class TrendingCategory(BaseModel):
    """
    _No description given by bungie._

    None
    Attributes:
        category_id: _No description given by bungie._
        category_name: _No description given by bungie._
        entries: _No description given by bungie._
    """

    category_id: str = attr.field()
    category_name: str = attr.field()
    entries: "SearchResultOfTrendingEntry" = attr.field()


@attr.define
class TrendingEntry(BaseModel):
    """
    The list entry view for trending items. Returns just enough to show the item on the trending page.

    None
    Attributes:
        creation_date: If the entry has a date at which it was created, this is that date.
        display_name: The localized "display name/article title/'primary localized identifier'" of the entity.
        end_date: _No description given by bungie._
        entity_type: An enum - unfortunately - dictating all of the possible kinds of trending items that you might get in your result set, in case you want to do custom rendering or call to get the details of the item.
        feature_image: If isFeatured, this image will be populated with whatever the featured image is. Note that this will likely be a very large image, so don't use it all the time.
        identifier: We don't know whether the identifier will be a string, a uint, or a long... so we're going to cast it all to a string. But either way, we need any trending item created to have a single unique identifier for its type.
        image: _No description given by bungie._
        is_featured: _No description given by bungie._
        items: If the item is of entityType TrendingEntryType.Container, it may have items - also Trending Entries - contained within it. This is the ordered list of those to display under the Container's header.
        link: _No description given by bungie._
        mp4_video: If this is populated, the entry has a related MP4 video to show. I am 100% certain I am going to regret putting this directly on TrendingEntry, but it will work so yolo
        start_date: _No description given by bungie._
        tagline: If the entity has a localized tagline/subtitle/motto/whatever, that is found here.
        webm_video: If this is populated, the entry has a related WebM video to show. I am 100% certain I am going to regret putting this directly on TrendingEntry, but it will work so yolo
        weight: The weighted score of this trending item.
    """

    creation_date: datetime = attr.field()
    display_name: str = attr.field()
    end_date: datetime = attr.field()
    entity_type: Union["TrendingEntryType", int] = attr.field(converter=enum_converter("TrendingEntryType"))
    feature_image: str = attr.field()
    identifier: str = attr.field()
    image: str = attr.field()
    is_featured: bool = attr.field()
    items: list["TrendingEntry"] = attr.field(metadata={"type": """list[TrendingEntry]"""})
    link: str = attr.field()
    mp4_video: str = attr.field()
    start_date: datetime = attr.field()
    tagline: str = attr.field()
    webm_video: str = attr.field()
    weight: float = attr.field()


class TrendingEntryType(BaseEnum):
    """
    The known entity types that you can have returned from Trending.
    """

    NEWS = 0
    """_No description given by bungie._ """
    DESTINY_ITEM = 1
    """_No description given by bungie._ """
    DESTINY_ACTIVITY = 2
    """_No description given by bungie._ """
    DESTINY_RITUAL = 3
    """_No description given by bungie._ """
    SUPPORT_ARTICLE = 4
    """_No description given by bungie._ """
    CREATION = 5
    """_No description given by bungie._ """
    STREAM = 6
    """_No description given by bungie._ """
    UPDATE = 7
    """_No description given by bungie._ """
    LINK = 8
    """_No description given by bungie._ """
    FORUM_TAG = 9
    """_No description given by bungie._ """
    CONTAINER = 10
    """_No description given by bungie._ """
    RELEASE = 11
    """_No description given by bungie._ """


@attr.define
class TrendingDetail(BaseModel):
    """
    _No description given by bungie._

    None
    Attributes:
        creation: _No description given by bungie._
        destiny_activity: _No description given by bungie._
        destiny_item: _No description given by bungie._
        destiny_ritual: _No description given by bungie._
        entity_type: _No description given by bungie._
        identifier: _No description given by bungie._
        news: _No description given by bungie._
        support: _No description given by bungie._
    """

    creation: "TrendingEntryCommunityCreation" = attr.field()
    destiny_activity: "TrendingEntryDestinyActivity" = attr.field()
    destiny_item: "TrendingEntryDestinyItem" = attr.field()
    destiny_ritual: "TrendingEntryDestinyRitual" = attr.field()
    entity_type: Union["TrendingEntryType", int] = attr.field(converter=enum_converter("TrendingEntryType"))
    identifier: str = attr.field()
    news: "TrendingEntryNews" = attr.field()
    support: "TrendingEntrySupportArticle" = attr.field()


@attr.define
class TrendingEntryNews(BaseModel):
    """
    _No description given by bungie._

    None
    Attributes:
        article: _No description given by bungie._
    """

    article: "ContentItemPublicContract" = attr.field()


@attr.define
class TrendingEntrySupportArticle(BaseModel):
    """
    _No description given by bungie._

    None
    Attributes:
        article: _No description given by bungie._
    """

    article: "ContentItemPublicContract" = attr.field()


@attr.define
class TrendingEntryDestinyItem(BaseModel):
    """
    _No description given by bungie._

    None
    Attributes:
        item_hash: _No description given by bungie._
    """

    item_hash: int = attr.field()


@attr.define
class TrendingEntryDestinyActivity(BaseModel):
    """
    _No description given by bungie._

    None
    Attributes:
        activity_hash: _No description given by bungie._
        status: _No description given by bungie._
    """

    activity_hash: int = attr.field()
    status: "DestinyPublicActivityStatus" = attr.field()


@attr.define
class TrendingEntryDestinyRitual(BaseModel):
    """
    _No description given by bungie._

    None
    Attributes:
        date_end: _No description given by bungie._
        date_start: _No description given by bungie._
        event_content: A destiny event will not necessarily have milestone "custom content", but if it does the details will be here.
        icon: _No description given by bungie._
        image: _No description given by bungie._
        milestone_details: A destiny event does not necessarily have a related Milestone, but if it does the details will be returned here.
        subtitle: _No description given by bungie._
        title: _No description given by bungie._
    """

    date_end: datetime = attr.field()
    date_start: datetime = attr.field()
    event_content: "DestinyMilestoneContent" = attr.field()
    icon: str = attr.field()
    image: str = attr.field()
    milestone_details: "DestinyPublicMilestone" = attr.field()
    subtitle: str = attr.field()
    title: str = attr.field()


@attr.define
class TrendingEntryCommunityCreation(BaseModel):
    """
    _No description given by bungie._

    None
    Attributes:
        author: _No description given by bungie._
        author_membership_id: _No description given by bungie._
        body: _No description given by bungie._
        media: _No description given by bungie._
        post_id: _No description given by bungie._
        title: _No description given by bungie._
        upvotes: _No description given by bungie._
    """

    author: str = attr.field()
    author_membership_id: int = attr.field()
    body: str = attr.field()
    media: str = attr.field()
    post_id: int = attr.field()
    title: str = attr.field()
    upvotes: int = attr.field()
