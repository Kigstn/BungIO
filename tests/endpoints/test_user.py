import pytest

from bungio.client import Client
from bungio.models import UserSearchPrefixRequest
from bungio.models.base import BaseModel
from bungio.models.basic.user import DestinyUser


@pytest.mark.asyncio
async def test_get_bungie_net_user_by_id(client: Client, user: DestinyUser):
    """
    Test for `Client.api.get_bungie_net_user_by_id()`
    """

    # data = await client.api.get_bungie_net_user_by_id()
    # assert data
    # assert isinstance(data, BaseModel)

    raise NotImplementedError


@pytest.mark.asyncio
async def test_get_sanitized_platform_display_names(client: Client, user: DestinyUser):
    """
    Test for `Client.api.get_sanitized_platform_display_names()`
    """

    # data = await client.api.get_sanitized_platform_display_names()
    # assert data
    # assert isinstance(data, BaseModel)

    raise NotImplementedError


@pytest.mark.asyncio
async def test_get_credential_types_for_target_account(client: Client, user: DestinyUser):
    """
    Test for `Client.api.get_credential_types_for_target_account()`
    """

    # data = await client.api.get_credential_types_for_target_account()
    # assert data
    # assert isinstance(data, BaseModel)

    raise NotImplementedError


@pytest.mark.asyncio
async def test_get_available_themes(client: Client, user: DestinyUser):
    """
    Test for `Client.api.get_available_themes()`
    """

    data = await client.api.get_available_themes()
    assert data is not None
    assert isinstance(data, list)
    for entry in data:
        assert isinstance(entry, BaseModel)


@pytest.mark.asyncio
async def test_get_membership_data_by_id(client: Client, user: DestinyUser):
    """
    Test for `Client.api.get_membership_data_by_id()`
    """

    data = await client.api.get_membership_data_by_id(
        membership_id=user.membership_id, membership_type=user.membership_type
    )
    assert data
    assert isinstance(data, BaseModel)


@pytest.mark.asyncio
async def test_get_membership_data_for_current_user(client: Client, user: DestinyUser):
    """
    Test for `Client.api.get_membership_data_for_current_user()`
    """

    # data = await client.api.get_membership_data_for_current_user()
    # assert data
    # assert isinstance(data, BaseModel)

    raise NotImplementedError


@pytest.mark.asyncio
async def test_get_membership_from_hard_linked_credential(client: Client, user: DestinyUser):
    """
    Test for `Client.api.get_membership_from_hard_linked_credential()`
    """

    # data = await client.api.get_membership_from_hard_linked_credential()
    # assert data
    # assert isinstance(data, BaseModel)

    raise NotImplementedError


@pytest.mark.asyncio
async def test_search_by_global_name_prefix(client: Client, user: DestinyUser):
    """
    Test for `Client.api.search_by_global_name_prefix()`
    """

    # data = await client.api.search_by_global_name_prefix()
    # assert data
    # assert isinstance(data, BaseModel)

    raise NotImplementedError


@pytest.mark.asyncio
async def test_search_by_global_name_post(client: Client, user: DestinyUser):
    """
    Test for `Client.api.search_by_global_name_post()`
    """

    data = await client.api.search_by_global_name_post(
        page=0, data=UserSearchPrefixRequest(display_name_prefix="Kigstn")
    )
    assert data
    assert isinstance(data, BaseModel)
