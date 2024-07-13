import asyncio
import os

import pytest
from bungio.client import Client
from bungio.models.basic.user import DestinyUser


@pytest.fixture(scope="session")
def event_loop():
    """
    Need to override the event loop to not close
    """

    loop = asyncio.new_event_loop()
    yield loop
    loop.close()


@pytest.fixture(scope="session")
def client(event_loop) -> Client:
    """
    Set Up the Client
    """

    client = Client(
        bungie_client_id=os.environ.get("BUNGIE_CLIENT_ID"),
        bungie_client_secret=os.environ.get("BUNGIE_CLIENT_SECRET"),
        bungie_token=os.environ.get("BUNGIE_TOKEN"),
    )

    yield client


@pytest.fixture(scope="session")
def user(client) -> DestinyUser:
    """
    Get a user which can be used for queries
    """

    user = DestinyUser(membership_type=3, membership_id=4611686018467765462)

    yield user


def pytest_runtest_call(item):
    """
    Catch and Skip NotImplemented Errors
    """

    try:
        item.runtest()
    except NotImplementedError:
        pytest.skip("Not Implemented")
