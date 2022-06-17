import pytest
from bungio.client import Client
from bungio.models.auth import UserData
from bungio.models.base import BaseModel


@pytest.mark.asyncio
async def test_get_user_system_overrides(client: Client, user: UserData):
    """
    Test for `Client.api.get_user_system_overrides()`
    """

    # data = await client.api.get_user_system_overrides()
    # assert data
    # assert isinstance(data, BaseModel)

    raise NotImplementedError
