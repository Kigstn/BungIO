# DO NOT CHANGE ANY CODE BELOW
# This file is generated automatically by `generate_api_schema.py` and will be overwritten
# Instead, change functions / models by subclassing them in the `./overwrites/` folder. They will be used instead.

from datetime import datetime
from typing import Union, TYPE_CHECKING

from bungio.utils import enum_converter
from bungio.models.base import BaseModel, BaseEnum, custom_define, custom_field


if TYPE_CHECKING:
    from bungio.models import DestinyPublicMilestone
    from bungio.models import DestinyPublicActivityStatus
    from bungio.models import SearchResultOfTrendingEntry
    from bungio.models import ContentItemPublicContract
    from bungio.models import DestinyMilestoneContent


@custom_define()
class TrendingCategories(BaseModel):
    """
    _No description given by bungie._

    None
    Attributes:
        categories: _No description given by bungie._
    """

    categories: list["TrendingCategory"] = custom_field(metadata={"type": """list[TrendingCategory]"""})


@custom_define()
class TrendingCategory(BaseModel):
    """
    _No description given by bungie._

    None
    Attributes:
        category_id: _No description given by bungie._
        category_name: _No description given by bungie._
        entries: _No description given by bungie._
    """

    category_id: str = custom_field()
    category_name: str = custom_field()
    entries: "SearchResultOfTrendingEntry" = custom_field()


@custom_define()
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

    creation_date: datetime = custom_field()
    display_name: str = custom_field()
    end_date: datetime = custom_field()
    entity_type: Union["TrendingEntryType", int] = custom_field(converter=enum_converter("TrendingEntryType"))
    feature_image: str = custom_field()
    identifier: str = custom_field()
    image: str = custom_field()
    is_featured: bool = custom_field()
    items: list["TrendingEntry"] = custom_field(metadata={"type": """list[TrendingEntry]"""})
    link: str = custom_field()
    mp4_video: str = custom_field()
    start_date: datetime = custom_field()
    tagline: str = custom_field()
    webm_video: str = custom_field()
    weight: float = custom_field()


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


@custom_define()
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

    creation: "TrendingEntryCommunityCreation" = custom_field()
    destiny_activity: "TrendingEntryDestinyActivity" = custom_field()
    destiny_item: "TrendingEntryDestinyItem" = custom_field()
    destiny_ritual: "TrendingEntryDestinyRitual" = custom_field()
    entity_type: Union["TrendingEntryType", int] = custom_field(converter=enum_converter("TrendingEntryType"))
    identifier: str = custom_field()
    news: "TrendingEntryNews" = custom_field()
    support: "TrendingEntrySupportArticle" = custom_field()


@custom_define()
class TrendingEntryNews(BaseModel):
    """
    _No description given by bungie._

    None
    Attributes:
        article: _No description given by bungie._
    """

    article: "ContentItemPublicContract" = custom_field()


@custom_define()
class TrendingEntrySupportArticle(BaseModel):
    """
    _No description given by bungie._

    None
    Attributes:
        article: _No description given by bungie._
    """

    article: "ContentItemPublicContract" = custom_field()


@custom_define()
class TrendingEntryDestinyItem(BaseModel):
    """
    _No description given by bungie._

    None
    Attributes:
        item_hash: _No description given by bungie._
    """

    item_hash: int = custom_field()


@custom_define()
class TrendingEntryDestinyActivity(BaseModel):
    """
    _No description given by bungie._

    None
    Attributes:
        activity_hash: _No description given by bungie._
        status: _No description given by bungie._
    """

    activity_hash: int = custom_field()
    status: "DestinyPublicActivityStatus" = custom_field()


@custom_define()
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

    date_end: datetime = custom_field()
    date_start: datetime = custom_field()
    event_content: "DestinyMilestoneContent" = custom_field()
    icon: str = custom_field()
    image: str = custom_field()
    milestone_details: "DestinyPublicMilestone" = custom_field()
    subtitle: str = custom_field()
    title: str = custom_field()


@custom_define()
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

    author: str = custom_field()
    author_membership_id: int = custom_field(metadata={"int64": True})
    body: str = custom_field()
    media: str = custom_field()
    post_id: int = custom_field(metadata={"int64": True})
    title: str = custom_field()
    upvotes: int = custom_field()
