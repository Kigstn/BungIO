import pytest
from bungio.client import Client
from bungio.models import GroupNameSearchRequest, GroupQuery, GroupType
from bungio.models.base import BaseModel
from bungio.models.basic.user import DestinyUser


@pytest.mark.asyncio
async def test_get_available_avatars(client: Client, user: DestinyUser):
    """
    Test for `Client.api.get_available_avatars()`
    """

    # data = await client.api.get_available_avatars()
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
async def test_get_user_clan_invite_setting(client: Client, user: DestinyUser):
    """
    Test for `Client.api.get_user_clan_invite_setting()`
    """

    # data = await client.api.get_user_clan_invite_setting()
    # assert data
    # assert isinstance(data, BaseModel)

    raise NotImplementedError


@pytest.mark.asyncio
async def test_get_recommended_groups(client: Client, user: DestinyUser):
    """
    Test for `Client.api.get_recommended_groups()`
    """

    # data = await client.api.get_recommended_groups()
    # assert data
    # assert isinstance(data, BaseModel)

    raise NotImplementedError


@pytest.mark.asyncio
async def test_group_search(client: Client, user: DestinyUser):
    """
    Test for `Client.api.group_search()`
    """

    data = await client.api.group_search(data=GroupQuery(name="Descend"))
    assert data
    assert isinstance(data, BaseModel)


@pytest.mark.asyncio
async def test_get_group(client: Client, user: DestinyUser):
    """
    Test for `Client.api.get_group()`
    """

    data = await client.api.get_group(group_id=4107840)
    assert data
    assert isinstance(data, BaseModel)


@pytest.mark.asyncio
async def test_get_group_by_name(client: Client, user: DestinyUser):
    """
    Test for `Client.api.get_group_by_name()`
    """

    # data = await client.api.get_group_by_name()
    # assert data
    # assert isinstance(data, BaseModel)

    raise NotImplementedError


@pytest.mark.asyncio
async def test_get_group_by_name_v2(client: Client, user: DestinyUser):
    """
    Test for `Client.api.get_group_by_name_v2()`
    """

    data = await client.api.get_group_by_name_v2(
        data=GroupNameSearchRequest(group_name="Descend", group_type=GroupType.CLAN)
    )
    assert data
    assert isinstance(data, BaseModel)


@pytest.mark.asyncio
async def test_get_group_optional_conversations(client: Client, user: DestinyUser):
    """
    Test for `Client.api.get_group_optional_conversations()`
    """

    data = await client.api.get_group_optional_conversations(group_id=4107840)
    assert data is not None
    assert isinstance(data, list)
    for entry in data:
        assert isinstance(entry, BaseModel)


@pytest.mark.asyncio
async def test_edit_group(client: Client, user: DestinyUser):
    """
    Test for `Client.api.edit_group()`
    """

    # data = await client.api.edit_group()
    # assert data
    # assert isinstance(data, BaseModel)

    raise NotImplementedError


@pytest.mark.asyncio
async def test_edit_clan_banner(client: Client, user: DestinyUser):
    """
    Test for `Client.api.edit_clan_banner()`
    """

    # data = await client.api.edit_clan_banner()
    # assert data
    # assert isinstance(data, BaseModel)

    raise NotImplementedError


@pytest.mark.asyncio
async def test_edit_founder_options(client: Client, user: DestinyUser):
    """
    Test for `Client.api.edit_founder_options()`
    """

    # data = await client.api.edit_founder_options()
    # assert data
    # assert isinstance(data, BaseModel)

    raise NotImplementedError


@pytest.mark.asyncio
async def test_add_optional_conversation(client: Client, user: DestinyUser):
    """
    Test for `Client.api.add_optional_conversation()`
    """

    # data = await client.api.add_optional_conversation()
    # assert data
    # assert isinstance(data, BaseModel)

    raise NotImplementedError


@pytest.mark.asyncio
async def test_edit_optional_conversation(client: Client, user: DestinyUser):
    """
    Test for `Client.api.edit_optional_conversation()`
    """

    # data = await client.api.edit_optional_conversation()
    # assert data
    # assert isinstance(data, BaseModel)

    raise NotImplementedError


@pytest.mark.asyncio
async def test_get_members_of_group(client: Client, user: DestinyUser):
    """
    Test for `Client.api.get_members_of_group()`
    """

    data = await client.api.get_members_of_group(currentpage=1, group_id=4107840)
    assert data
    assert isinstance(data, BaseModel)


@pytest.mark.asyncio
async def test_get_admins_and_founder_of_group(client: Client, user: DestinyUser):
    """
    Test for `Client.api.get_admins_and_founder_of_group()`
    """

    data = await client.api.get_admins_and_founder_of_group(
        currentpage=1, group_id=4107840
    )
    assert data
    assert isinstance(data, BaseModel)


@pytest.mark.asyncio
async def test_edit_group_membership(client: Client, user: DestinyUser):
    """
    Test for `Client.api.edit_group_membership()`
    """

    # data = await client.api.edit_group_membership()
    # assert data
    # assert isinstance(data, BaseModel)

    raise NotImplementedError


@pytest.mark.asyncio
async def test_kick_member(client: Client, user: DestinyUser):
    """
    Test for `Client.api.kick_member()`
    """

    # data = await client.api.kick_member()
    # assert data
    # assert isinstance(data, BaseModel)

    raise NotImplementedError


@pytest.mark.asyncio
async def test_ban_member(client: Client, user: DestinyUser):
    """
    Test for `Client.api.ban_member()`
    """

    # data = await client.api.ban_member()
    # assert data
    # assert isinstance(data, BaseModel)

    raise NotImplementedError


@pytest.mark.asyncio
async def test_unban_member(client: Client, user: DestinyUser):
    """
    Test for `Client.api.unban_member()`
    """

    # data = await client.api.unban_member()
    # assert data
    # assert isinstance(data, BaseModel)

    raise NotImplementedError


@pytest.mark.asyncio
async def test_get_banned_members_of_group(client: Client, user: DestinyUser):
    """
    Test for `Client.api.get_banned_members_of_group()`
    """

    # data = await client.api.get_banned_members_of_group()
    # assert data
    # assert isinstance(data, BaseModel)

    raise NotImplementedError


@pytest.mark.asyncio
async def test_abdicate_foundership(client: Client, user: DestinyUser):
    """
    Test for `Client.api.abdicate_foundership()`
    """

    # data = await client.api.abdicate_foundership()
    # assert data
    # assert isinstance(data, BaseModel)

    raise NotImplementedError


@pytest.mark.asyncio
async def test_get_pending_memberships(client: Client, user: DestinyUser):
    """
    Test for `Client.api.get_pending_memberships()`
    """

    # data = await client.api.get_pending_memberships()
    # assert data
    # assert isinstance(data, BaseModel)

    raise NotImplementedError


@pytest.mark.asyncio
async def test_get_invited_individuals(client: Client, user: DestinyUser):
    """
    Test for `Client.api.get_invited_individuals()`
    """

    # data = await client.api.get_invited_individuals()
    # assert data
    # assert isinstance(data, BaseModel)

    raise NotImplementedError


@pytest.mark.asyncio
async def test_approve_all_pending(client: Client, user: DestinyUser):
    """
    Test for `Client.api.approve_all_pending()`
    """

    # data = await client.api.approve_all_pending()
    # assert data
    # assert isinstance(data, BaseModel)

    raise NotImplementedError


@pytest.mark.asyncio
async def test_deny_all_pending(client: Client, user: DestinyUser):
    """
    Test for `Client.api.deny_all_pending()`
    """

    # data = await client.api.deny_all_pending()
    # assert data
    # assert isinstance(data, BaseModel)

    raise NotImplementedError


@pytest.mark.asyncio
async def test_approve_pending_for_list(client: Client, user: DestinyUser):
    """
    Test for `Client.api.approve_pending_for_list()`
    """

    # data = await client.api.approve_pending_for_list()
    # assert data
    # assert isinstance(data, BaseModel)

    raise NotImplementedError


@pytest.mark.asyncio
async def test_approve_pending(client: Client, user: DestinyUser):
    """
    Test for `Client.api.approve_pending()`
    """

    # data = await client.api.approve_pending()
    # assert data
    # assert isinstance(data, BaseModel)

    raise NotImplementedError


@pytest.mark.asyncio
async def test_deny_pending_for_list(client: Client, user: DestinyUser):
    """
    Test for `Client.api.deny_pending_for_list()`
    """

    # data = await client.api.deny_pending_for_list()
    # assert data
    # assert isinstance(data, BaseModel)

    raise NotImplementedError


@pytest.mark.asyncio
async def test_get_groups_for_member(client: Client, user: DestinyUser):
    """
    Test for `Client.api.get_groups_for_member()`
    """

    # data = await client.api.get_groups_for_member()
    # assert data
    # assert isinstance(data, BaseModel)

    raise NotImplementedError


@pytest.mark.asyncio
async def test_recover_group_for_founder(client: Client, user: DestinyUser):
    """
    Test for `Client.api.recover_group_for_founder()`
    """

    # data = await client.api.recover_group_for_founder()
    # assert data
    # assert isinstance(data, BaseModel)

    raise NotImplementedError


@pytest.mark.asyncio
async def test_get_potential_groups_for_member(client: Client, user: DestinyUser):
    """
    Test for `Client.api.get_potential_groups_for_member()`
    """

    # data = await client.api.get_potential_groups_for_member()
    # assert data
    # assert isinstance(data, BaseModel)

    raise NotImplementedError


@pytest.mark.asyncio
async def test_individual_group_invite(client: Client, user: DestinyUser):
    """
    Test for `Client.api.individual_group_invite()`
    """

    # data = await client.api.individual_group_invite()
    # assert data
    # assert isinstance(data, BaseModel)

    raise NotImplementedError


@pytest.mark.asyncio
async def test_individual_group_invite_cancel(client: Client, user: DestinyUser):
    """
    Test for `Client.api.individual_group_invite_cancel()`
    """

    # data = await client.api.individual_group_invite_cancel()
    # assert data
    # assert isinstance(data, BaseModel)

    raise NotImplementedError
