import datetime
from typing import Callable, Coroutine, Optional

from bungio.http.route import Route
from bungio.models.auth import AuthData


class SettingsRequests:
    request: Callable[..., Coroutine]

    async def get_common_settings(self, auth: Optional[AuthData] = None) -> dict:
        """
        Get the common settings used by the Bungie.Net environment.

        Args:
            auth: Authentication information. Required when users with a private profile are queried.

        Returns:
            The json response
        """

        return await self.request(Route(path=f"/Settings/", method="GET", auth=auth))
