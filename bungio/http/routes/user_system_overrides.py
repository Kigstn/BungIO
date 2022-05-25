import datetime
from typing import Callable, Coroutine, Optional

from bungio.http.route import Route
from bungio.models.auth import AuthData


class UserSystemOverridesRequests:
    request: Callable[..., Coroutine]

    async def get_user_system_overrides(self, auth: Optional[AuthData] = None) -> dict:
        """
        Get the user-specific system overrides that should be respected alongside common systems.

        Args:
            auth: Authentication information. Required when users with a private profile are queried.

        Returns:
            The json response
        """

        return await self.request(Route(path=f"/UserSystemOverrides/", method="GET", auth=auth))
