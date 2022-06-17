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

    def __init__(
        self, path: str, method: str, data: Optional[dict | list] = None, auth: Optional[AuthData] = None, **params
    ):
        self.data = data
        self.auth = auth
        self.method = method
        self.path = BASE_ROUTE + path

        # pgcr need a different url
        if "PostGameCarnageReport" in self.path:
            self.path = self.path.replace("www", "stats")

        # manifest too
        if "destiny2_content" in self.path:
            self.path = self.path.replace("/Platform", "")

        self.params = {}
        for name, value in params.items():
            # skip None params
            if value is None:
                continue

            # lists need to be comma seperated
            if isinstance(value, list):
                value = ",".join([str(v) for v in value])
            self.params[name] = value
