from bungio.http.route import Route
from bungio.http.routes import AllRequests
from bungio.singleton import SingletonMetaclass

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


class HttpClient(AllRequests, metaclass=SingletonMetaclass):
    """
    The singleton http client doing all communication with bungie
    """

    json_dumps = json_dumps
    json_loads = json_loads

    async def request(self, route: Route) -> dict:
        """
        Handle all web requests.

        Args:
            route: The route / method / params the request should have

        Returns:
            The json response
        """

        ...
