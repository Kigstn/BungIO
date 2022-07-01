import pytest
from bungio.client import Client
from bungio.models.base import BaseModel
from bungio.models.basic.user import DestinyUser


@pytest.mark.asyncio
async def test_get_friend_list(client: Client, user: DestinyUser):
    """
    Test for `Client.api.get_friend_list()`
    """

    # data = await client.api.get_friend_list()
    # assert data
    # assert isinstance(data, BaseModel)

    raise NotImplementedError


@pytest.mark.asyncio
async def test_get_friend_request_list(client: Client, user: DestinyUser):
    """
    Test for `Client.api.get_friend_request_list()`
    """

    # data = await client.api.get_friend_request_list()
    # assert data
    # assert isinstance(data, BaseModel)

    raise NotImplementedError


@pytest.mark.asyncio
async def test_issue_friend_request(client: Client, user: DestinyUser):
    """
    Test for `Client.api.issue_friend_request()`
    """

    # data = await client.api.issue_friend_request()
    # assert data
    # assert isinstance(data, BaseModel)

    raise NotImplementedError


@pytest.mark.asyncio
async def test_accept_friend_request(client: Client, user: DestinyUser):
    """
    Test for `Client.api.accept_friend_request()`
    """

    # data = await client.api.accept_friend_request()
    # assert data
    # assert isinstance(data, BaseModel)

    raise NotImplementedError


@pytest.mark.asyncio
async def test_decline_friend_request(client: Client, user: DestinyUser):
    """
    Test for `Client.api.decline_friend_request()`
    """

    # data = await client.api.decline_friend_request()
    # assert data
    # assert isinstance(data, BaseModel)

    raise NotImplementedError


@pytest.mark.asyncio
async def test_remove_friend(client: Client, user: DestinyUser):
    """
    Test for `Client.api.remove_friend()`
    """

    # data = await client.api.remove_friend()
    # assert data
    # assert isinstance(data, BaseModel)

    raise NotImplementedError


@pytest.mark.asyncio
async def test_remove_friend_request(client: Client, user: DestinyUser):
    """
    Test for `Client.api.remove_friend_request()`
    """

    # data = await client.api.remove_friend_request()
    # assert data
    # assert isinstance(data, BaseModel)

    raise NotImplementedError


@pytest.mark.asyncio
async def test_get_platform_friend_list(client: Client, user: DestinyUser):
    """
    Test for `Client.api.get_platform_friend_list()`
    """

    # data = await client.api.get_platform_friend_list()
    # assert data
    # assert isinstance(data, BaseModel)

    raise NotImplementedError
