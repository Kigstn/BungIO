import datetime
from typing import TYPE_CHECKING, Any, Optional

import attr

from bungio.models.base import BaseEnum, BaseModel


@attr.define
class TrendingCategories(BaseModel):
    """
    Not specified.

    Attributes:
        categories: Not specified.
    """

    categories: list["TrendingCategory"] = attr.field()


@attr.define
class TrendingCategory(BaseModel):
    """
    Not specified.

    Attributes:
        category_name: Not specified.
        entries: Not specified.
        category_id: Not specified.
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
        is_featured: Not specified.
        identifier: We don't know whether the identifier will be a string, a uint, or a long... so we're going to cast it all to a string. But either way, we need any trending item created to have a single unique identifier for its type.
        entity_type: An enum - unfortunately - dictating all of the possible kinds of trending items that you might get in your result set, in case you want to do custom rendering or call to get the details of the item.
        display_name: The localized "display name/article title/'primary localized identifier'" of the entity.
        tagline: If the entity has a localized tagline/subtitle/motto/whatever, that is found here.
        image: Not specified.
        start_date: Not specified.
        end_date: Not specified.
        link: Not specified.
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
    """Not specified. """
    DESTINY_ITEM = 1
    """Not specified. """
    DESTINY_ACTIVITY = 2
    """Not specified. """
    DESTINY_RITUAL = 3
    """Not specified. """
    SUPPORT_ARTICLE = 4
    """Not specified. """
    CREATION = 5
    """Not specified. """
    STREAM = 6
    """Not specified. """
    UPDATE = 7
    """Not specified. """
    LINK = 8
    """Not specified. """
    FORUM_TAG = 9
    """Not specified. """
    CONTAINER = 10
    """Not specified. """
    RELEASE = 11
    """Not specified. """


@attr.define
class TrendingDetail(BaseModel):
    """
    Not specified.

    Attributes:
        identifier: Not specified.
        entity_type: Not specified.
        news: Not specified.
        support: Not specified.
        destiny_item: Not specified.
        destiny_activity: Not specified.
        destiny_ritual: Not specified.
        creation: Not specified.
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
    Not specified.

    Attributes:
        article: Not specified.
    """

    article: "ContentItemPublicContract" = attr.field()


@attr.define
class TrendingEntrySupportArticle(BaseModel):
    """
    Not specified.

    Attributes:
        article: Not specified.
    """

    article: "ContentItemPublicContract" = attr.field()


@attr.define
class TrendingEntryDestinyItem(BaseModel):
    """
    Not specified.

    Attributes:
        item_hash: Not specified.
    """

    item_hash: int = attr.field()


@attr.define
class TrendingEntryDestinyActivity(BaseModel):
    """
    Not specified.

    Attributes:
        activity_hash: Not specified.
        status: Not specified.
    """

    activity_hash: int = attr.field()
    status: "DestinyPublicActivityStatus" = attr.field()


@attr.define
class TrendingEntryDestinyRitual(BaseModel):
    """
    Not specified.

    Attributes:
        image: Not specified.
        icon: Not specified.
        title: Not specified.
        subtitle: Not specified.
        date_start: Not specified.
        date_end: Not specified.
        milestone_details: A destiny event does not necessarily have a related Milestone, but if it does the details will be returned here.
        event_content: A destiny event will not necessarily have milestone "custom content", but if it does the details will be here.
    """

    image: str = attr.field()
    icon: str = attr.field()
    title: str = attr.field()
    subtitle: str = attr.field()
    date_start: datetime.datetime = attr.field()
    date_end: datetime.datetime = attr.field()
    milestone_details: Any = attr.field()
    event_content: Any = attr.field()


@attr.define
class TrendingEntryCommunityCreation(BaseModel):
    """
    Not specified.

    Attributes:
        media: Not specified.
        title: Not specified.
        author: Not specified.
        author_membership_id: Not specified.
        post_id: Not specified.
        body: Not specified.
        upvotes: Not specified.
    """

    media: str = attr.field()
    title: str = attr.field()
    author: str = attr.field()
    author_membership_id: int = attr.field()
    post_id: int = attr.field()
    body: str = attr.field()
    upvotes: int = attr.field()
