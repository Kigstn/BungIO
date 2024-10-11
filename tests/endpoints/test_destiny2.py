import pytest

from bungio.client import Client
from bungio.models import (
    DestinyComponentType,
    DestinyInventoryItemDefinition,
    ExactSearchRequest,
)
from bungio.models.base import BaseModel
from bungio.models.basic.user import DestinyUser


@pytest.mark.asyncio
async def test_get_destiny_manifest(client: Client, user: DestinyUser):
    """
    Test for `Client.api.get_destiny_manifest()`
    """

    data = await client.api.get_destiny_manifest()
    assert data
    assert isinstance(data, BaseModel)


@pytest.mark.asyncio
async def test_get_destiny_entity_definition(client: Client, user: DestinyUser):
    """
    Test for `Client.api.get_destiny_entity_definition()`
    """

    data = await client.api.get_destiny_entity_definition(
        entity_type=DestinyInventoryItemDefinition, hash_identifier=14194600
    )
    assert data
    assert isinstance(data, BaseModel)


@pytest.mark.asyncio
async def test_search_destiny_player_by_bungie_name(client: Client, user: DestinyUser):
    """
    Test for `Client.api.search_destiny_player_by_bungie_name()`
    """

    data = await client.api.search_destiny_player_by_bungie_name(
        data=ExactSearchRequest(display_name="Kigstn", display_name_code=4459),
        membership_type=user.membership_type,
    )
    assert data is not None
    assert isinstance(data, list)
    for entry in data:
        assert isinstance(entry, BaseModel)


@pytest.mark.asyncio
async def test_get_linked_profiles(client: Client, user: DestinyUser):
    """
    Test for `Client.api.get_linked_profiles()`
    """

    # data = await client.api.get_linked_profiles()
    # assert data
    # assert isinstance(data, BaseModel)

    raise NotImplementedError


@pytest.mark.asyncio
async def test_get_profile(client: Client, user: DestinyUser):
    """
    Test for `Client.api.get_profile()`
    """

    data = await client.api.get_profile(
        destiny_membership_id=user.membership_id,
        membership_type=user.membership_type,
        components=[DestinyComponentType.METRICS],
    )
    assert data
    assert isinstance(data, BaseModel)


@pytest.mark.asyncio
async def test_get_character(client: Client, user: DestinyUser):
    """
    Test for `Client.api.get_character()`
    """

    data = await client.api.get_character(
        character_id=2305843009300285667,
        destiny_membership_id=user.membership_id,
        membership_type=user.membership_type,
        components=[DestinyComponentType.METRICS],
    )
    assert data
    assert isinstance(data, BaseModel)


@pytest.mark.asyncio
async def test_get_clan_weekly_reward_state(client: Client, user: DestinyUser):
    """
    Test for `Client.api.get_clan_weekly_reward_state()`
    """

    data = await client.api.get_clan_weekly_reward_state(group_id=4107840)
    assert data
    assert isinstance(data, BaseModel)


@pytest.mark.asyncio
async def test_get_clan_banner_source(client: Client, user: DestinyUser):
    """
    Test for `Client.api.get_clan_banner_source()`
    """

    data = await client.api.get_clan_banner_source()
    assert data
    assert isinstance(data, dict)


@pytest.mark.asyncio
async def test_get_item(client: Client, user: DestinyUser):
    """
    Test for `Client.api.get_item()`
    """

    # data = await client.api.get_item()
    # assert data
    # assert isinstance(data, BaseModel)

    raise NotImplementedError


@pytest.mark.asyncio
async def test_get_vendors(client: Client, user: DestinyUser):
    """
    Test for `Client.api.get_vendors()`
    """

    # data = await client.api.get_vendors()
    # assert data
    # assert isinstance(data, BaseModel)

    raise NotImplementedError


@pytest.mark.asyncio
async def test_get_vendor(client: Client, user: DestinyUser):
    """
    Test for `Client.api.get_vendor()`
    """

    # data = await client.api.get_vendor()
    # assert data
    # assert isinstance(data, BaseModel)

    raise NotImplementedError


@pytest.mark.asyncio
async def test_get_public_vendors(client: Client, user: DestinyUser):
    """
    Test for `Client.api.get_public_vendors()`
    """

    data = await client.api.get_public_vendors(
        components=[
            DestinyComponentType.VENDORS,
            DestinyComponentType.VENDOR_SALES,
            DestinyComponentType.VENDOR_CATEGORIES,
        ]
    )
    assert data
    assert isinstance(data, BaseModel)


@pytest.mark.asyncio
async def test_get_collectible_node_details(client: Client, user: DestinyUser):
    """
    Test for `Client.api.get_collectible_node_details()`
    """

    data = await client.api.get_collectible_node_details(
        character_id=2305843009300285667,
        destiny_membership_id=user.membership_id,
        membership_type=user.membership_type,
        collectible_presentation_node_hash=329619022,
        components=[DestinyComponentType.PRESENTATION_NODES],
    )
    assert data
    assert isinstance(data, BaseModel)


@pytest.mark.asyncio
async def test_transfer_item(client: Client, user: DestinyUser):
    """
    Test for `Client.api.transfer_item()`
    """

    # data = await client.api.transfer_item()
    # assert data
    # assert isinstance(data, BaseModel)

    raise NotImplementedError


@pytest.mark.asyncio
async def test_pull_from_postmaster(client: Client, user: DestinyUser):
    """
    Test for `Client.api.pull_from_postmaster()`
    """

    # data = await client.api.pull_from_postmaster()
    # assert data
    # assert isinstance(data, BaseModel)

    raise NotImplementedError


@pytest.mark.asyncio
async def test_equip_item(client: Client, user: DestinyUser):
    """
    Test for `Client.api.equip_item()`
    """

    # data = await client.api.equip_item()
    # assert data
    # assert isinstance(data, BaseModel)

    raise NotImplementedError


@pytest.mark.asyncio
async def test_equip_items(client: Client, user: DestinyUser):
    """
    Test for `Client.api.equip_items()`
    """

    # data = await client.api.equip_items()
    # assert data
    # assert isinstance(data, BaseModel)

    raise NotImplementedError


@pytest.mark.asyncio
async def test_set_item_lock_state(client: Client, user: DestinyUser):
    """
    Test for `Client.api.set_item_lock_state()`
    """

    # data = await client.api.set_item_lock_state()
    # assert data
    # assert isinstance(data, BaseModel)

    raise NotImplementedError


@pytest.mark.asyncio
async def test_set_quest_tracked_state(client: Client, user: DestinyUser):
    """
    Test for `Client.api.set_quest_tracked_state()`
    """

    # data = await client.api.set_quest_tracked_state()
    # assert data
    # assert isinstance(data, BaseModel)

    raise NotImplementedError


@pytest.mark.asyncio
async def test_insert_socket_plug(client: Client, user: DestinyUser):
    """
    Test for `Client.api.insert_socket_plug()`
    """

    # data = await client.api.insert_socket_plug()
    # assert data
    # assert isinstance(data, BaseModel)

    raise NotImplementedError


@pytest.mark.asyncio
async def test_insert_socket_plug_free(client: Client, user: DestinyUser):
    """
    Test for `Client.api.insert_socket_plug_free()`
    """

    # data = await client.api.insert_socket_plug_free()
    # assert data
    # assert isinstance(data, BaseModel)

    raise NotImplementedError


@pytest.mark.asyncio
async def test_get_post_game_carnage_report(client: Client, user: DestinyUser):
    """
    Test for `Client.api.get_post_game_carnage_report()`
    """

    data = await client.api.get_post_game_carnage_report(4625517138)
    assert data
    assert isinstance(data, BaseModel)


@pytest.mark.asyncio
async def test_report_offensive_post_game_carnage_report_player(client: Client, user: DestinyUser):
    """
    Test for `Client.api.report_offensive_post_game_carnage_report_player()`
    """

    # data = await client.api.report_offensive_post_game_carnage_report_player()
    # assert data
    # assert isinstance(data, BaseModel)

    raise NotImplementedError


@pytest.mark.asyncio
async def test_get_historical_stats_definition(client: Client, user: DestinyUser):
    """
    Test for `Client.api.get_historical_stats_definition()`
    """

    data = await client.api.get_historical_stats_definition()
    assert data
    assert isinstance(data, dict)
    for entry in data.values():
        assert isinstance(entry, BaseModel)


@pytest.mark.asyncio
async def test_get_clan_leaderboards(client: Client, user: DestinyUser):
    """
    Test for `Client.api.get_clan_leaderboards()`
    """

    # data = await client.api.get_clan_leaderboards()
    # assert data
    # assert isinstance(data, BaseModel)

    raise NotImplementedError


@pytest.mark.asyncio
async def test_get_clan_aggregate_stats(client: Client, user: DestinyUser):
    """
    Test for `Client.api.get_clan_aggregate_stats()`
    """

    data = await client.api.get_clan_aggregate_stats(group_id=4107840)
    assert data is not None
    assert isinstance(data, list)
    for entry in data:
        assert isinstance(entry, BaseModel)


@pytest.mark.asyncio
async def test_get_leaderboards(client: Client, user: DestinyUser):
    """
    Test for `Client.api.get_leaderboards()`
    """

    data = await client.api.get_leaderboards(
        destiny_membership_id=user.membership_id, membership_type=user.membership_type
    )
    assert data is not None
    assert isinstance(data, dict)
    for entry in data.values():
        assert isinstance(entry, dict)
        for entry2 in entry.values():
            assert isinstance(entry2, BaseModel)


@pytest.mark.asyncio
async def test_get_leaderboards_for_character(client: Client, user: DestinyUser):
    """
    Test for `Client.api.get_leaderboards_for_character()`
    """

    # data = await client.api.get_leaderboards_for_character(
    #     character_id=2305843009300285667,
    #     destiny_membership_id=user.membership_id,
    #     membership_type=user.membership_type,
    # )
    # assert data
    # assert isinstance(data, dict)
    # for entry in data.values():
    #     assert isinstance(entry, dict)
    #     for entry2 in entry.values():
    #         assert isinstance(entry2, BaseModel)

    raise NotImplementedError


@pytest.mark.asyncio
async def test_search_destiny_entities(client: Client, user: DestinyUser):
    """
    Test for `Client.api.search_destiny_entities()`
    """

    # data = await client.api.search_destiny_entities()
    # assert data
    # assert isinstance(data, BaseModel)

    raise NotImplementedError


@pytest.mark.asyncio
async def test_get_historical_stats(client: Client, user: DestinyUser):
    """
    Test for `Client.api.get_historical_stats()`
    """

    data = await client.api.get_historical_stats(
        character_id=2305843009300285667,
        destiny_membership_id=user.membership_id,
        membership_type=user.membership_type,
    )
    assert data
    assert isinstance(data, dict)
    for entry in data.values():
        assert isinstance(entry, BaseModel)


@pytest.mark.asyncio
async def test_get_historical_stats_for_account(client: Client, user: DestinyUser):
    """
    Test for `Client.api.get_historical_stats_for_account()`
    """

    data = await client.api.get_historical_stats_for_account(
        destiny_membership_id=user.membership_id,
        membership_type=user.membership_type,
    )
    assert data
    assert isinstance(data, BaseModel)


@pytest.mark.asyncio
async def test_get_activity_history(client: Client, user: DestinyUser):
    """
    Test for `Client.api.get_activity_history()`
    """

    data = await client.api.get_activity_history(
        character_id=2305843009300285667,
        destiny_membership_id=user.membership_id,
        membership_type=user.membership_type,
    )
    assert data
    assert isinstance(data, BaseModel)


@pytest.mark.asyncio
async def test_get_unique_weapon_history(client: Client, user: DestinyUser):
    """
    Test for `Client.api.get_unique_weapon_history()`
    """

    data = await client.api.get_unique_weapon_history(
        character_id=2305843009300285667,
        destiny_membership_id=user.membership_id,
        membership_type=user.membership_type,
    )
    assert data
    assert isinstance(data, BaseModel)


@pytest.mark.asyncio
async def test_get_destiny_aggregate_activity_stats(client: Client, user: DestinyUser):
    """
    Test for `Client.api.get_destiny_aggregate_activity_stats()`
    """

    data = await client.api.get_destiny_aggregate_activity_stats(
        character_id=2305843009300285667,
        destiny_membership_id=user.membership_id,
        membership_type=user.membership_type,
    )
    assert data
    assert isinstance(data, BaseModel)


@pytest.mark.asyncio
async def test_get_public_milestone_content(client: Client, user: DestinyUser):
    """
    Test for `Client.api.get_public_milestone_content()`
    """

    # data = await client.api.get_public_milestone_content()
    # assert data
    # assert isinstance(data, BaseModel)

    raise NotImplementedError


@pytest.mark.asyncio
async def test_get_public_milestones(client: Client, user: DestinyUser):
    """
    Test for `Client.api.get_public_milestones()`
    """

    data = await client.api.get_public_milestones()
    assert data
    assert isinstance(data, dict)
    for entry in data.values():
        assert isinstance(entry, BaseModel)


@pytest.mark.asyncio
async def test_awa_initialize_request(client: Client, user: DestinyUser):
    """
    Test for `Client.api.awa_initialize_request()`
    """

    # data = await client.api.awa_initialize_request()
    # assert data
    # assert isinstance(data, BaseModel)

    raise NotImplementedError


@pytest.mark.asyncio
async def test_awa_provide_authorization_result(client: Client, user: DestinyUser):
    """
    Test for `Client.api.awa_provide_authorization_result()`
    """

    # data = await client.api.awa_provide_authorization_result()
    # assert data
    # assert isinstance(data, BaseModel)

    raise NotImplementedError


@pytest.mark.asyncio
async def test_awa_get_action_token(client: Client, user: DestinyUser):
    """
    Test for `Client.api.awa_get_action_token()`
    """

    # data = await client.api.awa_get_action_token()
    # assert data
    # assert isinstance(data, BaseModel)

    raise NotImplementedError
