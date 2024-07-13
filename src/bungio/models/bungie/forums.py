# DO NOT CHANGE ANY CODE BELOW
# This file is generated automatically by `generate_api_schema.py` and will be overwritten
# Instead, change functions / models by subclassing them in the `./overwrites/` folder. They will be used instead.


from bungio.models.base import BaseFlagEnum


class ForumPostCategoryEnums(BaseFlagEnum):
    """
    _No description given by bungie._
    """

    NONE = 0
    """_No description given by bungie._ """
    TEXT_ONLY = 1
    """_No description given by bungie._ """
    MEDIA = 2
    """_No description given by bungie._ """
    LINK = 4
    """_No description given by bungie._ """
    POLL = 8
    """_No description given by bungie._ """
    QUESTION = 16
    """_No description given by bungie._ """
    ANSWERED = 32
    """_No description given by bungie._ """
    ANNOUNCEMENT = 64
    """_No description given by bungie._ """
    CONTENT_COMMENT = 128
    """_No description given by bungie._ """
    BUNGIE_OFFICIAL = 256
    """_No description given by bungie._ """
    NINJA_OFFICIAL = 512
    """_No description given by bungie._ """
    RECRUITMENT = 1024
    """_No description given by bungie._ """


class ForumFlagsEnum(BaseFlagEnum):
    """
    _No description given by bungie._
    """

    NONE = 0
    """_No description given by bungie._ """
    BUNGIE_STAFF_POST = 1
    """_No description given by bungie._ """
    FORUM_NINJA_POST = 2
    """_No description given by bungie._ """
    FORUM_MENTOR_POST = 4
    """_No description given by bungie._ """
    TOPIC_BUNGIE_STAFF_POSTED = 8
    """_No description given by bungie._ """
    TOPIC_BUNGIE_VOLUNTEER_POSTED = 16
    """_No description given by bungie._ """
    QUESTION_ANSWERED_BY_BUNGIE = 32
    """_No description given by bungie._ """
    QUESTION_ANSWERED_BY_NINJA = 64
    """_No description given by bungie._ """
    COMMUNITY_CONTENT = 128
    """_No description given by bungie._ """
