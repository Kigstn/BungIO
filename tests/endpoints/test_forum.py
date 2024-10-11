import pytest

from bungio.client import Client
from bungio.models import (
    ForumTopicsCategoryFiltersEnum,
    ForumTopicsQuickDateEnum,
    ForumTopicsSortEnum,
)
from bungio.models.base import BaseModel
from bungio.models.basic.user import DestinyUser


@pytest.mark.asyncio
async def test_get_topics_paged(client: Client, user: DestinyUser):
    """
    Test for `Client.api.get_topics_paged()`
    """

    # data = await client.api.get_topics_paged()
    # assert data
    # assert isinstance(data, BaseModel)

    raise NotImplementedError


@pytest.mark.asyncio
async def test_get_core_topics_paged(client: Client, user: DestinyUser):
    """
    Test for `Client.api.get_core_topics_paged()`
    """

    data = await client.api.get_core_topics_paged(
        category_filter=ForumTopicsCategoryFiltersEnum.MEDIA,
        page=0,
        quick_date=ForumTopicsQuickDateEnum.LAST_DAY,
        sort=ForumTopicsSortEnum.HIGHEST_RATED,
    )
    assert data
    assert isinstance(data, BaseModel)


@pytest.mark.asyncio
async def test_get_posts_threaded_paged(client: Client, user: DestinyUser):
    """
    Test for `Client.api.get_posts_threaded_paged()`
    """

    # data = await client.api.get_posts_threaded_paged()
    # assert data
    # assert isinstance(data, BaseModel)

    raise NotImplementedError


@pytest.mark.asyncio
async def test_get_posts_threaded_paged_from_child(client: Client, user: DestinyUser):
    """
    Test for `Client.api.get_posts_threaded_paged_from_child()`
    """

    # data = await client.api.get_posts_threaded_paged_from_child()
    # assert data
    # assert isinstance(data, BaseModel)

    raise NotImplementedError


@pytest.mark.asyncio
async def test_get_post_and_parent(client: Client, user: DestinyUser):
    """
    Test for `Client.api.get_post_and_parent()`
    """

    # data = await client.api.get_post_and_parent()
    # assert data
    # assert isinstance(data, BaseModel)

    raise NotImplementedError


@pytest.mark.asyncio
async def test_get_post_and_parent_awaiting_approval(client: Client, user: DestinyUser):
    """
    Test for `Client.api.get_post_and_parent_awaiting_approval()`
    """

    # data = await client.api.get_post_and_parent_awaiting_approval()
    # assert data
    # assert isinstance(data, BaseModel)

    raise NotImplementedError


@pytest.mark.asyncio
async def test_get_topic_for_content(client: Client, user: DestinyUser):
    """
    Test for `Client.api.get_topic_for_content()`
    """

    # data = await client.api.get_topic_for_content()
    # assert data
    # assert isinstance(data, BaseModel)

    raise NotImplementedError


@pytest.mark.asyncio
async def test_get_forum_tag_suggestions(client: Client, user: DestinyUser):
    """
    Test for `Client.api.get_forum_tag_suggestions()`
    """

    # data = await client.api.get_forum_tag_suggestions()
    # assert data
    # assert isinstance(data, BaseModel)

    raise NotImplementedError


@pytest.mark.asyncio
async def test_get_poll(client: Client, user: DestinyUser):
    """
    Test for `Client.api.get_poll()`
    """

    # data = await client.api.get_poll()
    # assert data
    # assert isinstance(data, BaseModel)

    raise NotImplementedError


@pytest.mark.asyncio
async def test_get_recruitment_thread_summaries(client: Client, user: DestinyUser):
    """
    Test for `Client.api.get_recruitment_thread_summaries()`
    """

    # data = await client.api.get_recruitment_thread_summaries()
    # assert data
    # assert isinstance(data, BaseModel)

    raise NotImplementedError
