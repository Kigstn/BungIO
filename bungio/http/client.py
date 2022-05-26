from base64 import b64encode
from typing import TYPE_CHECKING, Callable, Optional

from bungio.http.auth import AuthRequests
from bungio.http.route import Route
from bungio.http.routes import AllRequests
from bungio.singleton import SingletonMetaclass

if TYPE_CHECKING:
    from bungio.client import Client

__all__ = ("HttpClient",)

# define json loading technique
try:
    import orjson

    def json_dumps(x):
        orjson.dumps(x).decode()

    json_loads = orjson.loads
except ModuleNotFoundError:
    import json

    json_dumps = json.dumps
    json_loads = json.loads


class HttpClient(AllRequests, AuthRequests, metaclass=SingletonMetaclass):
    """
    The singleton http client doing all communication with bungie
    """

    _client: "Client"

    _bungie_headers: dict[str, str]
    _bungie_auth_headers: dict[str, str]

    _json_dumps: Callable = json_dumps
    _json_loads: Callable = json_loads

    async def request(self, route: Route) -> dict:
        """
        Handle all web requests.

        Args:
            route: The route / method / params the request should have

        Returns:
            The json response
        """

        # make sure all is set up
        if not hasattr(self, "_client"):
            raise ValueError("You have to instantiate the `bungio.Client` before using this")

        ...

    async def _request(
        self, route: str, method: str, headers: dict, params: Optional[dict] = None, form_data: Optional[dict] = None
    ) -> dict:
        ...
