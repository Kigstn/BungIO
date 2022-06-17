from typing import Callable, Coroutine, Optional

from bungio.http.route import Route
from bungio.models.auth import AuthData


class UserSystemOverridesRouteHttpRequests:
    request: Callable[..., Coroutine]

    async def get_user_system_overrides(self, auth: Optional[AuthData] = None) -> dict:
        """
        Get the user-specific system overrides that should be respected alongside common systems.

        Args:
            auth: Authentication information. Required when users with a private profile are queried, or when Bungie feels like it

        Raises:
            NotFound: 404 request
            BadRequest: 400 request
            InvalidAuthentication: If authentication is invalid
            TimeoutException: If no connection could be made
            BungieDead: Servers are down
            AuthenticationTooSlow: The authentication key has expired
            BungieException: Relaying the bungie error

        Returns:
            The json response
        """

        return await self.request(Route(path=f"/UserSystemOverrides/", method="GET", auth=auth))
