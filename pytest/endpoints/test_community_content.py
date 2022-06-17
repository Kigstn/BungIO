import pytest
from bungio.client import Client
from bungio.models.auth import UserData
from bungio.models.base import BaseModel


@pytest.mark.asyncio
async def test_get_community_content(client: Client, user: UserData):
    """
    Test for `Client.api.get_community_content()`
    """

    # data = await client.api.get_community_content()
    # assert data
    # assert isinstance(data, BaseModel)

    raise NotImplementedError
