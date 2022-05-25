from typing import Any, Optional

from bungio.models.auth import AuthData
from definitions import BASE_ROUTE


class Route:
    """
    Bungie http route

    Attributes:
        path: The bungie path addition
        method: The http method
        auth: Authentication information
        **params: All query parameters
    """

    def __init__(self, path: str, method: str, auth: Optional[AuthData] = None, **params):
        self.params = params or {}
        self.auth = auth
        self.method = method
        self.path = BASE_ROUTE + path

        if "PostGameCarnageReport" in self.path:
            self.path = self.path.replace("www", "stats")
