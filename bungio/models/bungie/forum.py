import datetime
from typing import TYPE_CHECKING

import attr

from bungio.models.base import BaseEnum, BaseModel

if TYPE_CHECKING:
    from bungio.models import (
        GeneralUser,
        GroupResponse,
        IgnoreResponse,
        PagedQuery,
        TagResponse,
    )


class ForumTopicsCategoryFiltersEnum(BaseEnum):
    """
    _No description given by bungie_
    """

    NONE = 0
    """_No description given by bungie_ """
    LINKS = 1
    """_No description given by bungie_ """
    QUESTIONS = 2
    """_No description given by bungie_ """
    ANSWERED_QUESTIONS = 4
    """_No description given by bungie_ """
    MEDIA = 8
    """_No description given by bungie_ """
    TEXT_ONLY = 16
    """_No description given by bungie_ """
    ANNOUNCEMENT = 32
    """_No description given by bungie_ """
    BUNGIE_OFFICIAL = 64
    """_No description given by bungie_ """
    POLLS = 128
    """_No description given by bungie_ """


class ForumTopicsQuickDateEnum(BaseEnum):
    """
    _No description given by bungie_
    """

    ALL = 0
    """_No description given by bungie_ """
    LAST_YEAR = 1
    """_No description given by bungie_ """
    LAST_MONTH = 2
    """_No description given by bungie_ """
    LAST_WEEK = 3
    """_No description given by bungie_ """
    LAST_DAY = 4
    """_No description given by bungie_ """


class ForumTopicsSortEnum(BaseEnum):
    """
    _No description given by bungie_
    """

    DEFAULT = 0
    """_No description given by bungie_ """
    LAST_REPLIED = 1
    """_No description given by bungie_ """
    MOST_REPLIED = 2
    """_No description given by bungie_ """
    POPULARITY = 3
    """_No description given by bungie_ """
    CONTROVERSIALITY = 4
    """_No description given by bungie_ """
    LIKED = 5
    """_No description given by bungie_ """
    HIGHEST_RATED = 6
    """_No description given by bungie_ """
    MOST_UPVOTED = 7
    """_No description given by bungie_ """


@attr.define
class PostResponse(BaseModel):
    """
    _No description given by bungie_

    Attributes:
        last_reply_timestamp: _No description given by bungie_
        is_pinned: _No description given by bungie_
        url_media_type: _No description given by bungie_
        thumbnail: _No description given by bungie_
        popularity: _No description given by bungie_
        is_active: _No description given by bungie_
        is_announcement: _No description given by bungie_
        user_rating: _No description given by bungie_
        user_has_rated: _No description given by bungie_
        user_has_muted_post: _No description given by bungie_
        latest_reply_post_id: _No description given by bungie_
        latest_reply_author_id: _No description given by bungie_
        ignore_status: _No description given by bungie_
        locale: _No description given by bungie_
    """

    last_reply_timestamp: datetime.datetime = attr.field()
    is_pinned: bool = attr.field()
    url_media_type: "ForumMediaType" = attr.field()
    thumbnail: str = attr.field()
    popularity: "ForumPostPopularity" = attr.field()
    is_active: bool = attr.field()
    is_announcement: bool = attr.field()
    user_rating: int = attr.field()
    user_has_rated: bool = attr.field()
    user_has_muted_post: bool = attr.field()
    latest_reply_post_id: int = attr.field()
    latest_reply_author_id: int = attr.field()
    ignore_status: "IgnoreResponse" = attr.field()
    locale: str = attr.field()


class ForumMediaType(BaseEnum):
    """
    _No description given by bungie_
    """

    NONE = 0
    """_No description given by bungie_ """
    IMAGE = 1
    """_No description given by bungie_ """
    VIDEO = 2
    """_No description given by bungie_ """
    YOUTUBE = 3
    """_No description given by bungie_ """


class ForumPostPopularity(BaseEnum):
    """
    _No description given by bungie_
    """

    EMPTY = 0
    """_No description given by bungie_ """
    DEFAULT = 1
    """_No description given by bungie_ """
    DISCUSSED = 2
    """_No description given by bungie_ """
    COOL_STORY = 3
    """_No description given by bungie_ """
    HEATING_UP = 4
    """_No description given by bungie_ """
    HOT = 5
    """_No description given by bungie_ """


@attr.define
class PostSearchResponse(BaseModel):
    """
    _No description given by bungie_

    Attributes:
        related_posts: _No description given by bungie_
        authors: _No description given by bungie_
        groups: _No description given by bungie_
        searched_tags: _No description given by bungie_
        polls: _No description given by bungie_
        recruitment_details: _No description given by bungie_
        available_pages: _No description given by bungie_
        results: _No description given by bungie_
        total_results: _No description given by bungie_
        has_more: _No description given by bungie_
        query: _No description given by bungie_
        replacement_continuation_token: _No description given by bungie_
        use_total_results: If useTotalResults is true, then totalResults represents an accurate count. If False, it does not, and may be estimated/only the size of the current page. Either way, you should probably always only trust hasMore. This is a long-held historical throwback to when we used to do paging with known total results. Those queries toasted our database, and we were left to hastily alter our endpoints and create backward- compatible shims, of which useTotalResults is one.
    """

    related_posts: list["PostResponse"] = attr.field()
    authors: list["GeneralUser"] = attr.field()
    groups: list["GroupResponse"] = attr.field()
    searched_tags: list["TagResponse"] = attr.field()
    polls: list["PollResponse"] = attr.field()
    recruitment_details: list["ForumRecruitmentDetail"] = attr.field()
    available_pages: int = attr.field()
    results: list["PostResponse"] = attr.field()
    total_results: int = attr.field()
    has_more: bool = attr.field()
    query: "PagedQuery" = attr.field()
    replacement_continuation_token: str = attr.field()
    use_total_results: bool = attr.field()


@attr.define
class PollResponse(BaseModel):
    """
    _No description given by bungie_

    Attributes:
        topic_id: _No description given by bungie_
        results: _No description given by bungie_
        total_votes: _No description given by bungie_
    """

    topic_id: int = attr.field()
    results: list["PollResult"] = attr.field()
    total_votes: int = attr.field()


@attr.define
class PollResult(BaseModel):
    """
    _No description given by bungie_

    Attributes:
        answer_text: _No description given by bungie_
        answer_slot: _No description given by bungie_
        last_vote_date: _No description given by bungie_
        votes: _No description given by bungie_
        requesting_user_voted: _No description given by bungie_
    """

    answer_text: str = attr.field()
    answer_slot: int = attr.field()
    last_vote_date: datetime.datetime = attr.field()
    votes: int = attr.field()
    requesting_user_voted: bool = attr.field()


@attr.define
class ForumRecruitmentDetail(BaseModel):
    """
    _No description given by bungie_

    Attributes:
        topic_id: _No description given by bungie_
        microphone_required: _No description given by bungie_
        intensity: _No description given by bungie_
        tone: _No description given by bungie_
        approved: _No description given by bungie_
        conversation_id: _No description given by bungie_
        player_slots_total: _No description given by bungie_
        player_slots_remaining: _No description given by bungie_
        fireteam: _No description given by bungie_
        kicked_player_ids: _No description given by bungie_
    """

    topic_id: int = attr.field()
    microphone_required: bool = attr.field()
    intensity: "ForumRecruitmentIntensityLabel" = attr.field()
    tone: "ForumRecruitmentToneLabel" = attr.field()
    approved: bool = attr.field()
    conversation_id: int = attr.field()
    player_slots_total: int = attr.field()
    player_slots_remaining: int = attr.field()
    fireteam: list["GeneralUser"] = attr.field()
    kicked_player_ids: list[int] = attr.field()


class ForumRecruitmentIntensityLabel(BaseEnum):
    """
    _No description given by bungie_
    """

    NONE = 0
    """_No description given by bungie_ """
    CASUAL = 1
    """_No description given by bungie_ """
    PROFESSIONAL = 2
    """_No description given by bungie_ """


class ForumRecruitmentToneLabel(BaseEnum):
    """
    _No description given by bungie_
    """

    NONE = 0
    """_No description given by bungie_ """
    FAMILY_FRIENDLY = 1
    """_No description given by bungie_ """
    ROWDY = 2
    """_No description given by bungie_ """


class ForumPostSortEnum(BaseEnum):
    """
    _No description given by bungie_
    """

    DEFAULT = 0
    """_No description given by bungie_ """
    OLDEST_FIRST = 1
    """_No description given by bungie_ """


class CommunityContentSortMode(BaseEnum):
    """
    _No description given by bungie_
    """

    TRENDING = 0
    """_No description given by bungie_ """
    LATEST = 1
    """_No description given by bungie_ """
    HIGHEST_RATED = 2
    """_No description given by bungie_ """
