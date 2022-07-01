import pytest
from bungio.client import Client
from bungio.models.base import BaseModel
from bungio.models.basic.user import DestinyUser


@pytest.mark.asyncio
async def test_get_global_alerts(client: Client, user: DestinyUser):
    """
    Test for `Client.api.get_global_alerts()`
    """

    data = await client.api.get_global_alerts()
    assert data is not None
    assert isinstance(data, list)
    for entry in data:
        assert isinstance(entry, BaseModel)
