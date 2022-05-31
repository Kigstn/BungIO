from bungio.models.base import BaseEnum


class ForumPostCategoryEnums(BaseEnum):
    """
    _No description given_
    """

    NONE = 0
    """_No description given_ """
    TEXT_ONLY = 1
    """_No description given_ """
    MEDIA = 2
    """_No description given_ """
    LINK = 4
    """_No description given_ """
    POLL = 8
    """_No description given_ """
    QUESTION = 16
    """_No description given_ """
    ANSWERED = 32
    """_No description given_ """
    ANNOUNCEMENT = 64
    """_No description given_ """
    CONTENT_COMMENT = 128
    """_No description given_ """
    BUNGIE_OFFICIAL = 256
    """_No description given_ """
    NINJA_OFFICIAL = 512
    """_No description given_ """
    RECRUITMENT = 1024
    """_No description given_ """


class ForumFlagsEnum(BaseEnum):
    """
    _No description given_
    """

    NONE = 0
    """_No description given_ """
    BUNGIE_STAFF_POST = 1
    """_No description given_ """
    FORUM_NINJA_POST = 2
    """_No description given_ """
    FORUM_MENTOR_POST = 4
    """_No description given_ """
    TOPIC_BUNGIE_STAFF_POSTED = 8
    """_No description given_ """
    TOPIC_BUNGIE_VOLUNTEER_POSTED = 16
    """_No description given_ """
    QUESTION_ANSWERED_BY_BUNGIE = 32
    """_No description given_ """
    QUESTION_ANSWERED_BY_NINJA = 64
    """_No description given_ """
    COMMUNITY_CONTENT = 128
    """_No description given_ """
