import datetime
from typing import TYPE_CHECKING

import attr

from bungio.models.base import BaseEnum, BaseModel

if TYPE_CHECKING:
    from bungio.models import (
        ForumRecruitmentDetail,
        GeneralUser,
        GroupResponse,
        IgnoreResponse,
        PagedQuery,
        PollResponse,
        PollResult,
        PostResponse,
        TagResponse,
    )


class ForumTopicsCategoryFiltersEnum(BaseEnum):
    """
    _No description given_
    """

    NONE = 0
    """_No description given_ """
    LINKS = 1
    """_No description given_ """
    QUESTIONS = 2
    """_No description given_ """
    ANSWERED_QUESTIONS = 4
    """_No description given_ """
    MEDIA = 8
    """_No description given_ """
    TEXT_ONLY = 16
    """_No description given_ """
    ANNOUNCEMENT = 32
    """_No description given_ """
    BUNGIE_OFFICIAL = 64
    """_No description given_ """
    POLLS = 128
    """_No description given_ """


class ForumTopicsQuickDateEnum(BaseEnum):
    """
    _No description given_
    """

    ALL = 0
    """_No description given_ """
    LAST_YEAR = 1
    """_No description given_ """
    LAST_MONTH = 2
    """_No description given_ """
    LAST_WEEK = 3
    """_No description given_ """
    LAST_DAY = 4
    """_No description given_ """


class ForumTopicsSortEnum(BaseEnum):
    """
    _No description given_
    """

    DEFAULT = 0
    """_No description given_ """
    LAST_REPLIED = 1
    """_No description given_ """
    MOST_REPLIED = 2
    """_No description given_ """
    POPULARITY = 3
    """_No description given_ """
    CONTROVERSIALITY = 4
    """_No description given_ """
    LIKED = 5
    """_No description given_ """
    HIGHEST_RATED = 6
    """_No description given_ """
    MOST_UPVOTED = 7
    """_No description given_ """


@attr.define
class PostResponse(BaseModel):
    """
    _No description given_

    Attributes:
        last_reply_timestamp: _No description given_
        is_pinned: _No description given_
        url_media_type: _No description given_
        thumbnail: _No description given_
        popularity: _No description given_
        is_active: _No description given_
        is_announcement: _No description given_
        user_rating: _No description given_
        user_has_rated: _No description given_
        user_has_muted_post: _No description given_
        latest_reply_post_id: _No description given_
        latest_reply_author_id: _No description given_
        ignore_status: _No description given_
        locale: _No description given_
    """

    last_reply_timestamp: datetime.datetime = attr.field()
    is_pinned: bool = attr.field()
    url_media_type: int = attr.field()
    thumbnail: str = attr.field()
    popularity: int = attr.field()
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
    _No description given_
    """

    NONE = 0
    """_No description given_ """
    IMAGE = 1
    """_No description given_ """
    VIDEO = 2
    """_No description given_ """
    YOUTUBE = 3
    """_No description given_ """


class ForumPostPopularity(BaseEnum):
    """
    _No description given_
    """

    EMPTY = 0
    """_No description given_ """
    DEFAULT = 1
    """_No description given_ """
    DISCUSSED = 2
    """_No description given_ """
    COOL_STORY = 3
    """_No description given_ """
    HEATING_UP = 4
    """_No description given_ """
    HOT = 5
    """_No description given_ """


@attr.define
class PostSearchResponse(BaseModel):
    """
    _No description given_

    Attributes:
        related_posts: _No description given_
        authors: _No description given_
        groups: _No description given_
        searched_tags: _No description given_
        polls: _No description given_
        recruitment_details: _No description given_
        available_pages: _No description given_
        results: _No description given_
        total_results: _No description given_
        has_more: _No description given_
        query: _No description given_
        replacement_continuation_token: _No description given_
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
    _No description given_

    Attributes:
        topic_id: _No description given_
        results: _No description given_
        total_votes: _No description given_
    """

    topic_id: int = attr.field()
    results: list["PollResult"] = attr.field()
    total_votes: int = attr.field()


@attr.define
class PollResult(BaseModel):
    """
    _No description given_

    Attributes:
        answer_text: _No description given_
        answer_slot: _No description given_
        last_vote_date: _No description given_
        votes: _No description given_
        requesting_user_voted: _No description given_
    """

    answer_text: str = attr.field()
    answer_slot: int = attr.field()
    last_vote_date: datetime.datetime = attr.field()
    votes: int = attr.field()
    requesting_user_voted: bool = attr.field()


@attr.define
class ForumRecruitmentDetail(BaseModel):
    """
    _No description given_

    Attributes:
        topic_id: _No description given_
        microphone_required: _No description given_
        intensity: _No description given_
        tone: _No description given_
        approved: _No description given_
        conversation_id: _No description given_
        player_slots_total: _No description given_
        player_slots_remaining: _No description given_
        fireteam: _No description given_
        kicked_player_ids: _No description given_
    """

    topic_id: int = attr.field()
    microphone_required: bool = attr.field()
    intensity: int = attr.field()
    tone: int = attr.field()
    approved: bool = attr.field()
    conversation_id: int = attr.field()
    player_slots_total: int = attr.field()
    player_slots_remaining: int = attr.field()
    fireteam: list["GeneralUser"] = attr.field()
    kicked_player_ids: list[int] = attr.field()


class ForumRecruitmentIntensityLabel(BaseEnum):
    """
    _No description given_
    """

    NONE = 0
    """_No description given_ """
    CASUAL = 1
    """_No description given_ """
    PROFESSIONAL = 2
    """_No description given_ """


class ForumRecruitmentToneLabel(BaseEnum):
    """
    _No description given_
    """

    NONE = 0
    """_No description given_ """
    FAMILY_FRIENDLY = 1
    """_No description given_ """
    ROWDY = 2
    """_No description given_ """


class ForumPostSortEnum(BaseEnum):
    """
    _No description given_
    """

    DEFAULT = 0
    """_No description given_ """
    OLDEST_FIRST = 1
    """_No description given_ """


class CommunityContentSortMode(BaseEnum):
    """
    _No description given_
    """

    TRENDING = 0
    """_No description given_ """
    LATEST = 1
    """_No description given_ """
    HIGHEST_RATED = 2
    """_No description given_ """
