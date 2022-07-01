import pytest
from bungio.client import Client
from bungio.models.base import BaseModel
from bungio.models.basic.user import DestinyUser


@pytest.mark.asyncio
async def test_get_active_private_clan_fireteam_count(client: Client, user: DestinyUser):
    """
    Test for `Client.api.get_active_private_clan_fireteam_count()`
    """

    # data = await client.api.get_active_private_clan_fireteam_count()
    # assert data
    # assert isinstance(data, BaseModel)

    raise NotImplementedError


@pytest.mark.asyncio
async def test_get_available_clan_fireteams(client: Client, user: DestinyUser):
    """
    Test for `Client.api.get_available_clan_fireteams()`
    """

    # data = await client.api.get_available_clan_fireteams()
    # assert data
    # assert isinstance(data, BaseModel)

    raise NotImplementedError


@pytest.mark.asyncio
async def test_search_public_available_clan_fireteams(client: Client, user: DestinyUser):
    """
    Test for `Client.api.search_public_available_clan_fireteams()`
    """

    # data = await client.api.search_public_available_clan_fireteams()
    # assert data
    # assert isinstance(data, BaseModel)

    raise NotImplementedError


@pytest.mark.asyncio
async def test_get_my_clan_fireteams(client: Client, user: DestinyUser):
    """
    Test for `Client.api.get_my_clan_fireteams()`
    """

    # data = await client.api.get_my_clan_fireteams()
    # assert data
    # assert isinstance(data, BaseModel)

    raise NotImplementedError


@pytest.mark.asyncio
async def test_get_clan_fireteam(client: Client, user: DestinyUser):
    """
    Test for `Client.api.get_clan_fireteam()`
    """

    # data = await client.api.get_clan_fireteam()
    # assert data
    # assert isinstance(data, BaseModel)

    raise NotImplementedError
