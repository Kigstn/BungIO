from typing import Optional

from bungio.definitions import BASE_ROUTE
from bungio.models.auth import AuthData


class Route:
    """
    Bungie http route

    Attributes:
        path: The bungie path addition
        method: The http method
        auth: Authentication information
        data: Body data to send
        **params: All query parameters
    """

    def __init__(self, path: str, method: str, data: Optional[dict] = None, auth: Optional[AuthData] = None, **params):
        self.params = params or {}
        self.data = data
        self.auth = auth
        self.method = method
        self.path = BASE_ROUTE + path

        if "PostGameCarnageReport" in self.path:
            self.path = self.path.replace("www", "stats")
