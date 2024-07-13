from typing import Callable, Coroutine, Optional

from bungio.http.route import Route
from bungio.models.auth import AuthData


class SettingsRouteHttpRequests:
    request: Callable[..., Coroutine]

    async def get_common_settings(self, auth: Optional[AuthData] = None, *args, **kwargs) -> dict:
        """
        Get the common settings used by the Bungie.Net environment.

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

        return await self.request(Route(path="/Settings/", method="GET", auth=auth))
