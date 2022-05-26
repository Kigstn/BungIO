import datetime
from typing import TYPE_CHECKING, Any, Optional

import attr

from bungio.models.base import BaseEnum, BaseModel


class ForumPostCategoryEnums(BaseEnum):
    """
    Not specified.
    """

    NONE = 0
    """Not specified. """
    TEXT_ONLY = 1
    """Not specified. """
    MEDIA = 2
    """Not specified. """
    LINK = 4
    """Not specified. """
    POLL = 8
    """Not specified. """
    QUESTION = 16
    """Not specified. """
    ANSWERED = 32
    """Not specified. """
    ANNOUNCEMENT = 64
    """Not specified. """
    CONTENT_COMMENT = 128
    """Not specified. """
    BUNGIE_OFFICIAL = 256
    """Not specified. """
    NINJA_OFFICIAL = 512
    """Not specified. """
    RECRUITMENT = 1024
    """Not specified. """


class ForumFlagsEnum(BaseEnum):
    """
    Not specified.
    """

    NONE = 0
    """Not specified. """
    BUNGIE_STAFF_POST = 1
    """Not specified. """
    FORUM_NINJA_POST = 2
    """Not specified. """
    FORUM_MENTOR_POST = 4
    """Not specified. """
    TOPIC_BUNGIE_STAFF_POSTED = 8
    """Not specified. """
    TOPIC_BUNGIE_VOLUNTEER_POSTED = 16
    """Not specified. """
    QUESTION_ANSWERED_BY_BUNGIE = 32
    """Not specified. """
    QUESTION_ANSWERED_BY_NINJA = 64
    """Not specified. """
    COMMUNITY_CONTENT = 128
    """Not specified. """
