import pytest

from bungio.client import Client
from bungio.models.base import BaseModel
from bungio.models.basic.user import DestinyUser


@pytest.mark.asyncio
async def test_get_application_api_usage(client: Client, user: DestinyUser):
    """
    Test for `Client.api.get_application_api_usage()`
    """

    # data = await client.api.get_application_api_usage()
    # assert data
    # assert isinstance(data, BaseModel)

    raise NotImplementedError


@pytest.mark.asyncio
async def test_get_bungie_applications(client: Client, user: DestinyUser):
    """
    Test for `Client.api.get_bungie_applications()`
    """

    data = await client.api.get_bungie_applications()
    assert data is not None
    assert isinstance(data, list)
    for entry in data:
        assert isinstance(entry, BaseModel)
