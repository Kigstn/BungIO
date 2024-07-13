from datetime import datetime
from typing import Callable, Coroutine, Optional

from bungio.http.route import Route
from bungio.models.auth import AuthData


class AppRouteHttpRequests:
    request: Callable[..., Coroutine]

    async def get_application_api_usage(
        self,
        application_id: int,
        auth: AuthData,
        end: Optional[datetime] = None,
        start: Optional[datetime] = None,
        *args,
        **kwargs,
    ) -> dict:
        """
        Get API usage by application for time frame specified. You can go as far back as 30 days ago, and can ask for up to a 48 hour window of time in a single request. You must be authenticated with at least the ReadUserData permission to access this endpoint.

        Warning: Requires Authentication.
            Required oauth2 scopes: ReadUserData

        Args:
            application_id: ID of the application to get usage statistics.
            auth: Authentication information.
            end: End time for query. Goes to now if not specified.
            start: Start time for query. Goes to 24 hours ago if not specified.

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
            Route(path=f"/App/ApiUsage/{application_id}/", method="GET", auth=auth, end=end, start=start)
        )

    async def get_bungie_applications(self, auth: Optional[AuthData] = None, *args, **kwargs) -> dict:
        """
        Get list of applications created by Bungie.

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

        return await self.request(Route(path="/App/FirstParty/", method="GET", auth=auth))
