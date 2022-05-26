import datetime
from typing import TYPE_CHECKING, Any, Optional

import attr

from bungio.models.base import BaseEnum, BaseModel


class ForumTopicsCategoryFiltersEnum(BaseEnum):
    """
    Not specified.
    """

    NONE = 0
    """Not specified. """
    LINKS = 1
    """Not specified. """
    QUESTIONS = 2
    """Not specified. """
    ANSWERED_QUESTIONS = 4
    """Not specified. """
    MEDIA = 8
    """Not specified. """
    TEXT_ONLY = 16
    """Not specified. """
    ANNOUNCEMENT = 32
    """Not specified. """
    BUNGIE_OFFICIAL = 64
    """Not specified. """
    POLLS = 128
    """Not specified. """


class ForumTopicsQuickDateEnum(BaseEnum):
    """
    Not specified.
    """

    ALL = 0
    """Not specified. """
    LAST_YEAR = 1
    """Not specified. """
    LAST_MONTH = 2
    """Not specified. """
    LAST_WEEK = 3
    """Not specified. """
    LAST_DAY = 4
    """Not specified. """


class ForumTopicsSortEnum(BaseEnum):
    """
    Not specified.
    """

    DEFAULT = 0
    """Not specified. """
    LAST_REPLIED = 1
    """Not specified. """
    MOST_REPLIED = 2
    """Not specified. """
    POPULARITY = 3
    """Not specified. """
    CONTROVERSIALITY = 4
    """Not specified. """
    LIKED = 5
    """Not specified. """
    HIGHEST_RATED = 6
    """Not specified. """
    MOST_UPVOTED = 7
    """Not specified. """


@attr.define
class PostResponse(BaseModel):
    """
    Not specified.

    Attributes:
        last_reply_timestamp: Not specified.
        is_pinned: Not specified.
        url_media_type: Not specified.
        thumbnail: Not specified.
        popularity: Not specified.
        is_active: Not specified.
        is_announcement: Not specified.
        user_rating: Not specified.
        user_has_rated: Not specified.
        user_has_muted_post: Not specified.
        latest_reply_post_id: Not specified.
        latest_reply_author_id: Not specified.
        ignore_status: Not specified.
        locale: Not specified.
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
    Not specified.
    """

    NONE = 0
    """Not specified. """
    IMAGE = 1
    """Not specified. """
    VIDEO = 2
    """Not specified. """
    YOUTUBE = 3
    """Not specified. """


class ForumPostPopularity(BaseEnum):
    """
    Not specified.
    """

    EMPTY = 0
    """Not specified. """
    DEFAULT = 1
    """Not specified. """
    DISCUSSED = 2
    """Not specified. """
    COOL_STORY = 3
    """Not specified. """
    HEATING_UP = 4
    """Not specified. """
    HOT = 5
    """Not specified. """


@attr.define
class PostSearchResponse(BaseModel):
    """
        Not specified.

        Attributes:
            related_posts: Not specified.
            authors: Not specified.
            groups: Not specified.
            searched_tags: Not specified.
            polls: Not specified.
            recruitment_details: Not specified.
            available_pages: Not specified.
            results: Not specified.
            total_results: Not specified.
            has_more: Not specified.
            query: Not specified.
            replacement_continuation_token: Not specified.
            use_total_results: If useTotalResults is true, then totalResults represents an accurate count.

    If False, it does not, and may be estimated/only the size of the current page.

    Either way, you should probably always only trust hasMore.

    This is a long-held historical throwback to when we used to do paging with known total results. Those queries toasted our database, and we were left to hastily alter our endpoints and create backward- compatible shims, of which useTotalResults is one.
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
    Not specified.

    Attributes:
        topic_id: Not specified.
        results: Not specified.
        total_votes: Not specified.
    """

    topic_id: int = attr.field()
    results: list["PollResult"] = attr.field()
    total_votes: int = attr.field()


@attr.define
class PollResult(BaseModel):
    """
    Not specified.

    Attributes:
        answer_text: Not specified.
        answer_slot: Not specified.
        last_vote_date: Not specified.
        votes: Not specified.
        requesting_user_voted: Not specified.
    """

    answer_text: str = attr.field()
    answer_slot: int = attr.field()
    last_vote_date: datetime.datetime = attr.field()
    votes: int = attr.field()
    requesting_user_voted: bool = attr.field()


@attr.define
class ForumRecruitmentDetail(BaseModel):
    """
    Not specified.

    Attributes:
        topic_id: Not specified.
        microphone_required: Not specified.
        intensity: Not specified.
        tone: Not specified.
        approved: Not specified.
        conversation_id: Not specified.
        player_slots_total: Not specified.
        player_slots_remaining: Not specified.
        fireteam: Not specified.
        kicked_player_ids: Not specified.
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
    Not specified.
    """

    NONE = 0
    """Not specified. """
    CASUAL = 1
    """Not specified. """
    PROFESSIONAL = 2
    """Not specified. """


class ForumRecruitmentToneLabel(BaseEnum):
    """
    Not specified.
    """

    NONE = 0
    """Not specified. """
    FAMILY_FRIENDLY = 1
    """Not specified. """
    ROWDY = 2
    """Not specified. """


class ForumPostSortEnum(BaseEnum):
    """
    Not specified.
    """

    DEFAULT = 0
    """Not specified. """
    OLDEST_FIRST = 1
    """Not specified. """


class CommunityContentSortMode(BaseEnum):
    """
    Not specified.
    """

    TRENDING = 0
    """Not specified. """
    LATEST = 1
    """Not specified. """
    HIGHEST_RATED = 2
    """Not specified. """
