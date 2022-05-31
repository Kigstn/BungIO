from bungio.models.base import BaseEnum


class ForumPostCategoryEnums(BaseEnum):
    """
    _No description given by bungie_
    """

    NONE = 0
    """_No description given by bungie_ """
    TEXT_ONLY = 1
    """_No description given by bungie_ """
    MEDIA = 2
    """_No description given by bungie_ """
    LINK = 4
    """_No description given by bungie_ """
    POLL = 8
    """_No description given by bungie_ """
    QUESTION = 16
    """_No description given by bungie_ """
    ANSWERED = 32
    """_No description given by bungie_ """
    ANNOUNCEMENT = 64
    """_No description given by bungie_ """
    CONTENT_COMMENT = 128
    """_No description given by bungie_ """
    BUNGIE_OFFICIAL = 256
    """_No description given by bungie_ """
    NINJA_OFFICIAL = 512
    """_No description given by bungie_ """
    RECRUITMENT = 1024
    """_No description given by bungie_ """


class ForumFlagsEnum(BaseEnum):
    """
    _No description given by bungie_
    """

    NONE = 0
    """_No description given by bungie_ """
    BUNGIE_STAFF_POST = 1
    """_No description given by bungie_ """
    FORUM_NINJA_POST = 2
    """_No description given by bungie_ """
    FORUM_MENTOR_POST = 4
    """_No description given by bungie_ """
    TOPIC_BUNGIE_STAFF_POSTED = 8
    """_No description given by bungie_ """
    TOPIC_BUNGIE_VOLUNTEER_POSTED = 16
    """_No description given by bungie_ """
    QUESTION_ANSWERED_BY_BUNGIE = 32
    """_No description given by bungie_ """
    QUESTION_ANSWERED_BY_NINJA = 64
    """_No description given by bungie_ """
    COMMUNITY_CONTENT = 128
    """_No description given by bungie_ """
