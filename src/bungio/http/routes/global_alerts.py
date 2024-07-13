from typing import Callable, Coroutine, Optional

from bungio.http.route import Route
from bungio.models.auth import AuthData


class GlobalAlertsRouteHttpRequests:
    request: Callable[..., Coroutine]

    async def get_global_alerts(
        self, includestreaming: Optional[bool] = None, auth: Optional[AuthData] = None, *args, **kwargs
    ) -> dict:
        """
        Gets any active global alert for display in the forum banners, help pages, etc. Usually used for DOC alerts.

        Args:
            includestreaming: Determines whether Streaming Alerts are included in results
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

        return await self.request(
            Route(path="/GlobalAlerts/", method="GET", includestreaming=includestreaming, auth=auth)
        )
