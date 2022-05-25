import datetime
from typing import Callable, Coroutine, Optional

from bungio.http.route import Route
from bungio.models.auth import AuthData


class GetAvailableLocalesRequests:
    request: Callable[..., Coroutine]

    async def get_available_locales(self, auth: Optional[AuthData] = None) -> dict:
        """
        List of available localization cultures

        Args:
            auth: Authentication information. Required when users with a private profile are queried.

        Returns:
            The json response
        """

        return await self.request(Route(path=f"/GetAvailableLocales/", method="GET", auth=auth))
