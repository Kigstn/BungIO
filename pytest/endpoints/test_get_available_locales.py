import pytest
from bungio.client import Client
from bungio.models.auth import UserData
from bungio.models.base import BaseModel


@pytest.mark.asyncio
async def test_get_available_locales(client: Client, user: UserData):
    """
    Test for `Client.api.get_available_locales()`
    """

    # data = await client.api.get_available_locales()
    # assert data
    # assert isinstance(data, BaseModel)

    raise NotImplementedError
