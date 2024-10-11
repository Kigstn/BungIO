import pytest

from bungio.client import Client
from bungio.models.base import BaseModel
from bungio.models.basic.user import DestinyUser


@pytest.mark.asyncio
async def test_get_common_settings(client: Client, user: DestinyUser):
    """
    Test for `Client.api.get_common_settings()`
    """

    data = await client.api.get_common_settings()
    assert data
    assert isinstance(data, BaseModel)
