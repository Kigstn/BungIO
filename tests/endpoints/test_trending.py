import pytest

from bungio.client import Client
from bungio.models.base import BaseModel
from bungio.models.basic.user import DestinyUser


@pytest.mark.asyncio
async def test_get_trending_categories(client: Client, user: DestinyUser):
    """
    Test for `Client.api.get_trending_categories()`
    """

    data = await client.api.get_trending_categories()
    assert data
    assert isinstance(data, BaseModel)


@pytest.mark.asyncio
async def test_get_trending_category(client: Client, user: DestinyUser):
    """
    Test for `Client.api.get_trending_category()`
    """

    # data = await client.api.get_trending_category()
    # assert data
    # assert isinstance(data, BaseModel)

    raise NotImplementedError


@pytest.mark.asyncio
async def test_get_trending_entry_detail(client: Client, user: DestinyUser):
    """
    Test for `Client.api.get_trending_entry_detail()`
    """

    # data = await client.api.get_trending_entry_detail()
    # assert data
    # assert isinstance(data, BaseModel)

    raise NotImplementedError
