import pytest
from bungio.client import Client
from bungio.models.base import BaseModel
from bungio.models.basic.user import DestinyUser


@pytest.mark.asyncio
async def test_get_community_content(client: Client, user: DestinyUser):
    """
    Test for `Client.api.get_community_content()`
    """

    # data = await client.api.get_community_content()
    # assert data
    # assert isinstance(data, BaseModel)

    raise NotImplementedError
