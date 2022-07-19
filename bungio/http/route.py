from typing import Optional

import attr

from bungio.definitions import BASE_ROUTE
from bungio.models.auth import AuthData
from bungio.models.base import MISSING

__all__ = ("Route",)


@attr.define(init=False)
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

    path: str
    method: str
    data: Optional[dict | list]
    auth: Optional[AuthData]
    params: dict

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

        # clean the data
        if isinstance(data, dict):
            cleaned = {}
            for key, value in self.data.items():
                # skip None / MISSING entries
                if value is None or value is MISSING:
                    continue

                cleaned[key] = value
            self.data = cleaned

        # clean the params
        self.params = {}
        for key, value in params.items():
            # skip None / MISSING params
            if value is None or value is MISSING:
                continue

            # lists need to be comma seperated
            if isinstance(value, list):
                value = ",".join([str(v) for v in value])
            self.params[key] = value
