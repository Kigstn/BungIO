import pytest

from bungio.client import Client
from bungio.models.basic.user import DestinyUser


@pytest.mark.asyncio
async def test_get_content_type(client: Client, user: DestinyUser):
    """
    Test for `Client.api.get_content_type()`
    """

    # data = await client.api.get_content_type()
    # assert data
    # assert isinstance(data, BaseModel)

    raise NotImplementedError


@pytest.mark.asyncio
async def test_get_content_by_id(client: Client, user: DestinyUser):
    """
    Test for `Client.api.get_content_by_id()`
    """

    # data = await client.api.get_content_by_id()
    # assert data
    # assert isinstance(data, BaseModel)

    raise NotImplementedError


@pytest.mark.asyncio
async def test_get_content_by_tag_and_type(client: Client, user: DestinyUser):
    """
    Test for `Client.api.get_content_by_tag_and_type()`
    """

    # data = await client.api.get_content_by_tag_and_type()
    # assert data
    # assert isinstance(data, BaseModel)

    raise NotImplementedError


@pytest.mark.asyncio
async def test_search_content_with_text(client: Client, user: DestinyUser):
    """
    Test for `Client.api.search_content_with_text()`
    """

    # data = await client.api.search_content_with_text()
    # assert data
    # assert isinstance(data, BaseModel)

    raise NotImplementedError


@pytest.mark.asyncio
async def test_search_content_by_tag_and_type(client: Client, user: DestinyUser):
    """
    Test for `Client.api.search_content_by_tag_and_type()`
    """

    # data = await client.api.search_content_by_tag_and_type()
    # assert data
    # assert isinstance(data, BaseModel)

    raise NotImplementedError


@pytest.mark.asyncio
async def test_search_help_articles(client: Client, user: DestinyUser):
    """
    Test for `Client.api.search_help_articles()`
    """

    # data = await client.api.search_help_articles()
    # assert data
    # assert isinstance(data, BaseModel)

    raise NotImplementedError
