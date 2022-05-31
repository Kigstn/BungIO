import datetime
from typing import TYPE_CHECKING

import attr

from bungio.models.base import BaseEnum, BaseModel

if TYPE_CHECKING:
    from bungio.models import (
        ContentItemPublicContract,
        DestinyMilestoneContent,
        DestinyPublicActivityStatus,
        DestinyPublicMilestone,
        SearchResultOfTrendingEntry,
        TrendingCategory,
        TrendingEntry,
        TrendingEntryCommunityCreation,
        TrendingEntryDestinyActivity,
        TrendingEntryDestinyItem,
        TrendingEntryDestinyRitual,
        TrendingEntryNews,
        TrendingEntrySupportArticle,
    )


@attr.define
class TrendingCategories(BaseModel):
    """
    _No description given by bungie_

    Attributes:
        categories: _No description given by bungie_
    """

    categories: list["TrendingCategory"] = attr.field()


@attr.define
class TrendingCategory(BaseModel):
    """
    _No description given by bungie_

    Attributes:
        category_name: _No description given by bungie_
        entries: _No description given by bungie_
        category_id: _No description given by bungie_
    """

    category_name: str = attr.field()
    entries: "SearchResultOfTrendingEntry" = attr.field()
    category_id: str = attr.field()


@attr.define
class TrendingEntry(BaseModel):
    """
    The list entry view for trending items. Returns just enough to show the item on the trending page.

    Attributes:
        weight: The weighted score of this trending item.
        is_featured: _No description given by bungie_
        identifier: We don't know whether the identifier will be a string, a uint, or a long... so we're going to cast it all to a string. But either way, we need any trending item created to have a single unique identifier for its type.
        entity_type: An enum - unfortunately - dictating all of the possible kinds of trending items that you might get in your result set, in case you want to do custom rendering or call to get the details of the item.
        display_name: The localized "display name/article title/'primary localized identifier'" of the entity.
        tagline: If the entity has a localized tagline/subtitle/motto/whatever, that is found here.
        image: _No description given by bungie_
        start_date: _No description given by bungie_
        end_date: _No description given by bungie_
        link: _No description given by bungie_
        webm_video: If this is populated, the entry has a related WebM video to show. I am 100% certain I am going to regret putting this directly on TrendingEntry, but it will work so yolo
        mp4_video: If this is populated, the entry has a related MP4 video to show. I am 100% certain I am going to regret putting this directly on TrendingEntry, but it will work so yolo
        feature_image: If isFeatured, this image will be populated with whatever the featured image is. Note that this will likely be a very large image, so don't use it all the time.
        items: If the item is of entityType TrendingEntryType.Container, it may have items - also Trending Entries - contained within it. This is the ordered list of those to display under the Container's header.
        creation_date: If the entry has a date at which it was created, this is that date.
    """

    weight: float = attr.field()
    is_featured: bool = attr.field()
    identifier: str = attr.field()
    entity_type: int = attr.field()
    display_name: str = attr.field()
    tagline: str = attr.field()
    image: str = attr.field()
    start_date: datetime.datetime = attr.field()
    end_date: datetime.datetime = attr.field()
    link: str = attr.field()
    webm_video: str = attr.field()
    mp4_video: str = attr.field()
    feature_image: str = attr.field()
    items: list["TrendingEntry"] = attr.field()
    creation_date: datetime.datetime = attr.field()


class TrendingEntryType(BaseEnum):
    """
    The known entity types that you can have returned from Trending.
    """

    NEWS = 0
    """_No description given by bungie_ """
    DESTINY_ITEM = 1
    """_No description given by bungie_ """
    DESTINY_ACTIVITY = 2
    """_No description given by bungie_ """
    DESTINY_RITUAL = 3
    """_No description given by bungie_ """
    SUPPORT_ARTICLE = 4
    """_No description given by bungie_ """
    CREATION = 5
    """_No description given by bungie_ """
    STREAM = 6
    """_No description given by bungie_ """
    UPDATE = 7
    """_No description given by bungie_ """
    LINK = 8
    """_No description given by bungie_ """
    FORUM_TAG = 9
    """_No description given by bungie_ """
    CONTAINER = 10
    """_No description given by bungie_ """
    RELEASE = 11
    """_No description given by bungie_ """


@attr.define
class TrendingDetail(BaseModel):
    """
    _No description given by bungie_

    Attributes:
        identifier: _No description given by bungie_
        entity_type: _No description given by bungie_
        news: _No description given by bungie_
        support: _No description given by bungie_
        destiny_item: _No description given by bungie_
        destiny_activity: _No description given by bungie_
        destiny_ritual: _No description given by bungie_
        creation: _No description given by bungie_
    """

    identifier: str = attr.field()
    entity_type: int = attr.field()
    news: "TrendingEntryNews" = attr.field()
    support: "TrendingEntrySupportArticle" = attr.field()
    destiny_item: "TrendingEntryDestinyItem" = attr.field()
    destiny_activity: "TrendingEntryDestinyActivity" = attr.field()
    destiny_ritual: "TrendingEntryDestinyRitual" = attr.field()
    creation: "TrendingEntryCommunityCreation" = attr.field()


@attr.define
class TrendingEntryNews(BaseModel):
    """
    _No description given by bungie_

    Attributes:
        article: _No description given by bungie_
    """

    article: "ContentItemPublicContract" = attr.field()


@attr.define
class TrendingEntrySupportArticle(BaseModel):
    """
    _No description given by bungie_

    Attributes:
        article: _No description given by bungie_
    """

    article: "ContentItemPublicContract" = attr.field()


@attr.define
class TrendingEntryDestinyItem(BaseModel):
    """
    _No description given by bungie_

    Attributes:
        item_hash: _No description given by bungie_
    """

    item_hash: int = attr.field()


@attr.define
class TrendingEntryDestinyActivity(BaseModel):
    """
    _No description given by bungie_

    Attributes:
        activity_hash: _No description given by bungie_
        status: _No description given by bungie_
    """

    activity_hash: int = attr.field()
    status: "DestinyPublicActivityStatus" = attr.field()


@attr.define
class TrendingEntryDestinyRitual(BaseModel):
    """
    _No description given by bungie_

    Attributes:
        image: _No description given by bungie_
        icon: _No description given by bungie_
        title: _No description given by bungie_
        subtitle: _No description given by bungie_
        date_start: _No description given by bungie_
        date_end: _No description given by bungie_
        milestone_details: A destiny event does not necessarily have a related Milestone, but if it does the details will be returned here.
        event_content: A destiny event will not necessarily have milestone "custom content", but if it does the details will be here.
    """

    image: str = attr.field()
    icon: str = attr.field()
    title: str = attr.field()
    subtitle: str = attr.field()
    date_start: datetime.datetime = attr.field()
    date_end: datetime.datetime = attr.field()
    milestone_details: "DestinyPublicMilestone" = attr.field()
    event_content: "DestinyMilestoneContent" = attr.field()


@attr.define
class TrendingEntryCommunityCreation(BaseModel):
    """
    _No description given by bungie_

    Attributes:
        media: _No description given by bungie_
        title: _No description given by bungie_
        author: _No description given by bungie_
        author_membership_id: _No description given by bungie_
        post_id: _No description given by bungie_
        body: _No description given by bungie_
        upvotes: _No description given by bungie_
    """

    media: str = attr.field()
    title: str = attr.field()
    author: str = attr.field()
    author_membership_id: int = attr.field()
    post_id: int = attr.field()
    body: str = attr.field()
    upvotes: int = attr.field()
