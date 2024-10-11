import pytest

from bungio.client import Client
from bungio.models.base import BaseModel
from bungio.models.basic.user import DestinyUser


@pytest.mark.asyncio
async def test_claim_partner_offer(client: Client, user: DestinyUser):
    """
    Test for `Client.api.claim_partner_offer()`
    """

    # data = await client.api.claim_partner_offer()
    # assert data
    # assert isinstance(data, BaseModel)

    raise NotImplementedError


@pytest.mark.asyncio
async def test_apply_missing_partner_offers_without_claim(client: Client, user: DestinyUser):
    """
    Test for `Client.api.apply_missing_partner_offers_without_claim()`
    """

    # data = await client.api.apply_missing_partner_offers_without_claim()
    # assert data
    # assert isinstance(data, BaseModel)

    raise NotImplementedError


@pytest.mark.asyncio
async def test_get_partner_offer_sku_history(client: Client, user: DestinyUser):
    """
    Test for `Client.api.get_partner_offer_sku_history()`
    """

    # data = await client.api.get_partner_offer_sku_history()
    # assert data
    # assert isinstance(data, BaseModel)

    raise NotImplementedError


@pytest.mark.asyncio
async def test_get_bungie_rewards_for_user(client: Client, user: DestinyUser):
    """
    Test for `Client.api.get_bungie_rewards_for_user()`
    """

    # data = await client.api.get_bungie_rewards_for_user()
    # assert data
    # assert isinstance(data, BaseModel)

    raise NotImplementedError


@pytest.mark.asyncio
async def test_get_bungie_rewards_list(client: Client, user: DestinyUser):
    """
    Test for `Client.api.get_bungie_rewards_list()`
    """

    data = await client.api.get_bungie_rewards_list()
    assert data
    assert isinstance(data, dict)
    for entry in data.values():
        assert isinstance(entry, BaseModel)
