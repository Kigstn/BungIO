# DO NOT CHANGE ANY CODE BELOW
# This file is generated automatically by `generate_api_schema.py` and will be overwritten
# Instead, change functions / models by subclassing them in the `./overwrites/` folder. They will be used instead.

from datetime import datetime
from typing import TYPE_CHECKING, Union

import attr

from bungio.models.base import BaseEnum, BaseFlagEnum, BaseModel
from bungio.utils import enum_converter

if TYPE_CHECKING:
    from bungio.models import (
        GeneralUser,
        GroupResponse,
        IgnoreResponse,
        PagedQuery,
        TagResponse,
    )


class ForumTopicsCategoryFiltersEnum(BaseFlagEnum):
    """
    _No description given by bungie._
    """

    NONE = 0
    """_No description given by bungie._ """
    LINKS = 1
    """_No description given by bungie._ """
    QUESTIONS = 2
    """_No description given by bungie._ """
    ANSWERED_QUESTIONS = 4
    """_No description given by bungie._ """
    MEDIA = 8
    """_No description given by bungie._ """
    TEXT_ONLY = 16
    """_No description given by bungie._ """
    ANNOUNCEMENT = 32
    """_No description given by bungie._ """
    BUNGIE_OFFICIAL = 64
    """_No description given by bungie._ """
    POLLS = 128
    """_No description given by bungie._ """


class ForumTopicsQuickDateEnum(BaseEnum):
    """
    _No description given by bungie._
    """

    ALL = 0
    """_No description given by bungie._ """
    LAST_YEAR = 1
    """_No description given by bungie._ """
    LAST_MONTH = 2
    """_No description given by bungie._ """
    LAST_WEEK = 3
    """_No description given by bungie._ """
    LAST_DAY = 4
    """_No description given by bungie._ """


class ForumTopicsSortEnum(BaseEnum):
    """
    _No description given by bungie._
    """

    DEFAULT = 0
    """_No description given by bungie._ """
    LAST_REPLIED = 1
    """_No description given by bungie._ """
    MOST_REPLIED = 2
    """_No description given by bungie._ """
    POPULARITY = 3
    """_No description given by bungie._ """
    CONTROVERSIALITY = 4
    """_No description given by bungie._ """
    LIKED = 5
    """_No description given by bungie._ """
    HIGHEST_RATED = 6
    """_No description given by bungie._ """
    MOST_UPVOTED = 7
    """_No description given by bungie._ """


@attr.define
class PostResponse(BaseModel):
    """
    _No description given by bungie._

    None
    Attributes:
        ignore_status: _No description given by bungie._
        is_active: _No description given by bungie._
        is_announcement: _No description given by bungie._
        is_pinned: _No description given by bungie._
        last_reply_timestamp: _No description given by bungie._
        latest_reply_author_id: _No description given by bungie._
        latest_reply_post_id: _No description given by bungie._
        locale: _No description given by bungie._
        popularity: _No description given by bungie._
        thumbnail: _No description given by bungie._
        url_media_type: _No description given by bungie._
        user_has_muted_post: _No description given by bungie._
        user_has_rated: _No description given by bungie._
        user_rating: _No description given by bungie._
    """

    ignore_status: "IgnoreResponse" = attr.field()
    is_active: bool = attr.field()
    is_announcement: bool = attr.field()
    is_pinned: bool = attr.field()
    last_reply_timestamp: datetime = attr.field()
    latest_reply_author_id: int = attr.field()
    latest_reply_post_id: int = attr.field()
    locale: str = attr.field()
    popularity: Union["ForumPostPopularity", int] = attr.field(converter=enum_converter("ForumPostPopularity"))
    thumbnail: str = attr.field()
    url_media_type: Union["ForumMediaType", int] = attr.field(converter=enum_converter("ForumMediaType"))
    user_has_muted_post: bool = attr.field()
    user_has_rated: bool = attr.field()
    user_rating: int = attr.field()


class ForumMediaType(BaseEnum):
    """
    _No description given by bungie._
    """

    NONE = 0
    """_No description given by bungie._ """
    IMAGE = 1
    """_No description given by bungie._ """
    VIDEO = 2
    """_No description given by bungie._ """
    YOUTUBE = 3
    """_No description given by bungie._ """


class ForumPostPopularity(BaseEnum):
    """
    _No description given by bungie._
    """

    EMPTY = 0
    """_No description given by bungie._ """
    DEFAULT = 1
    """_No description given by bungie._ """
    DISCUSSED = 2
    """_No description given by bungie._ """
    COOL_STORY = 3
    """_No description given by bungie._ """
    HEATING_UP = 4
    """_No description given by bungie._ """
    HOT = 5
    """_No description given by bungie._ """


@attr.define
class PostSearchResponse(BaseModel):
    """
    _No description given by bungie._

    None
    Attributes:
        authors: _No description given by bungie._
        available_pages: _No description given by bungie._
        groups: _No description given by bungie._
        has_more: _No description given by bungie._
        polls: _No description given by bungie._
        query: _No description given by bungie._
        recruitment_details: _No description given by bungie._
        related_posts: _No description given by bungie._
        replacement_continuation_token: _No description given by bungie._
        results: _No description given by bungie._
        searched_tags: _No description given by bungie._
        total_results: _No description given by bungie._
        use_total_results: If useTotalResults is true, then totalResults represents an accurate count. If False, it does not, and may be estimated/only the size of the current page. Either way, you should probably always only trust hasMore. This is a long-held historical throwback to when we used to do paging with known total results. Those queries toasted our database, and we were left to hastily alter our endpoints and create backward- compatible shims, of which useTotalResults is one.
    """

    authors: list["GeneralUser"] = attr.field(metadata={"type": """list[GeneralUser]"""})
    available_pages: int = attr.field()
    groups: list["GroupResponse"] = attr.field(metadata={"type": """list[GroupResponse]"""})
    has_more: bool = attr.field()
    polls: list["PollResponse"] = attr.field(metadata={"type": """list[PollResponse]"""})
    query: "PagedQuery" = attr.field()
    recruitment_details: list["ForumRecruitmentDetail"] = attr.field(
        metadata={"type": """list[ForumRecruitmentDetail]"""}
    )
    related_posts: list["PostResponse"] = attr.field(metadata={"type": """list[PostResponse]"""})
    replacement_continuation_token: str = attr.field()
    results: list["PostResponse"] = attr.field(metadata={"type": """list[PostResponse]"""})
    searched_tags: list["TagResponse"] = attr.field(metadata={"type": """list[TagResponse]"""})
    total_results: int = attr.field()
    use_total_results: bool = attr.field()


@attr.define
class PollResponse(BaseModel):
    """
    _No description given by bungie._

    None
    Attributes:
        results: _No description given by bungie._
        topic_id: _No description given by bungie._
        total_votes: _No description given by bungie._
    """

    results: list["PollResult"] = attr.field(metadata={"type": """list[PollResult]"""})
    topic_id: int = attr.field()
    total_votes: int = attr.field()


@attr.define
class PollResult(BaseModel):
    """
    _No description given by bungie._

    None
    Attributes:
        answer_slot: _No description given by bungie._
        answer_text: _No description given by bungie._
        last_vote_date: _No description given by bungie._
        requesting_user_voted: _No description given by bungie._
        votes: _No description given by bungie._
    """

    answer_slot: int = attr.field()
    answer_text: str = attr.field()
    last_vote_date: datetime = attr.field()
    requesting_user_voted: bool = attr.field()
    votes: int = attr.field()


@attr.define
class ForumRecruitmentDetail(BaseModel):
    """
    _No description given by bungie._

    None
    Attributes:
        approved: _No description given by bungie._
        conversation_id: _No description given by bungie._
        fireteam: _No description given by bungie._
        intensity: _No description given by bungie._
        kicked_player_ids: _No description given by bungie._
        microphone_required: _No description given by bungie._
        player_slots_remaining: _No description given by bungie._
        player_slots_total: _No description given by bungie._
        tone: _No description given by bungie._
        topic_id: _No description given by bungie._
    """

    approved: bool = attr.field()
    conversation_id: int = attr.field()
    fireteam: list["GeneralUser"] = attr.field(metadata={"type": """list[GeneralUser]"""})
    intensity: Union["ForumRecruitmentIntensityLabel", int] = attr.field(
        converter=enum_converter("ForumRecruitmentIntensityLabel")
    )
    kicked_player_ids: list[int] = attr.field(metadata={"type": """list[int]"""})
    microphone_required: bool = attr.field()
    player_slots_remaining: int = attr.field()
    player_slots_total: int = attr.field()
    tone: Union["ForumRecruitmentToneLabel", int] = attr.field(converter=enum_converter("ForumRecruitmentToneLabel"))
    topic_id: int = attr.field()


class ForumRecruitmentIntensityLabel(BaseEnum):
    """
    _No description given by bungie._
    """

    NONE = 0
    """_No description given by bungie._ """
    CASUAL = 1
    """_No description given by bungie._ """
    PROFESSIONAL = 2
    """_No description given by bungie._ """


class ForumRecruitmentToneLabel(BaseEnum):
    """
    _No description given by bungie._
    """

    NONE = 0
    """_No description given by bungie._ """
    FAMILY_FRIENDLY = 1
    """_No description given by bungie._ """
    ROWDY = 2
    """_No description given by bungie._ """


class ForumPostSortEnum(BaseEnum):
    """
    _No description given by bungie._
    """

    DEFAULT = 0
    """_No description given by bungie._ """
    OLDEST_FIRST = 1
    """_No description given by bungie._ """


class CommunityContentSortMode(BaseEnum):
    """
    _No description given by bungie._
    """

    TRENDING = 0
    """_No description given by bungie._ """
    LATEST = 1
    """_No description given by bungie._ """
    HIGHEST_RATED = 2
    """_No description given by bungie._ """
