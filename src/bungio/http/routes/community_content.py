from typing import Callable, Coroutine, Optional

from bungio.http.route import Route
from bungio.models.auth import AuthData


class CommunityContentRouteHttpRequests:
    request: Callable[..., Coroutine]

    async def get_community_content(
        self, media_filter: int, page: int, sort: int, auth: Optional[AuthData] = None, *args, **kwargs
    ) -> dict:
        """
        Returns community content.

        Args:
            media_filter: The type of media to get
            page: Zero based page
            sort: The sort mode.
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
            Route(path=f"/CommunityContent/Get/{sort}/{media_filter}/{page}/", method="GET", auth=auth)
        )
