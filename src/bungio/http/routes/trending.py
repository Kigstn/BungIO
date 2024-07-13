from typing import Callable, Coroutine, Optional

from bungio.http.route import Route
from bungio.models.auth import AuthData


class TrendingRouteHttpRequests:
    request: Callable[..., Coroutine]

    async def get_trending_categories(self, auth: Optional[AuthData] = None, *args, **kwargs) -> dict:
        """
        Returns trending items for Bungie.net, collapsed into the first page of items per category. For pagination within a category, call GetTrendingCategory.

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

        return await self.request(Route(path="/Trending/Categories/", method="GET", auth=auth))

    async def get_trending_category(
        self, category_id: str, page_number: int, auth: Optional[AuthData] = None, *args, **kwargs
    ) -> dict:
        """
        Returns paginated lists of trending items for a category.

        Args:
            category_id: The ID of the category for whom you want additional results.
            page_number: The page # of results to return.
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
            Route(path=f"/Trending/Categories/{category_id}/{page_number}/", method="GET", auth=auth)
        )

    async def get_trending_entry_detail(
        self, identifier: str, trending_entry_type: int, auth: Optional[AuthData] = None, *args, **kwargs
    ) -> dict:
        """
        Returns the detailed results for a specific trending entry. Note that trending entries are uniquely identified by a combination of *both* the TrendingEntryType *and* the identifier: the identifier alone is not guaranteed to be globally unique.

        Args:
            identifier: The identifier for the entity to be returned.
            trending_entry_type: The type of entity to be returned.
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
            Route(path=f"/Trending/Details/{trending_entry_type}/{identifier}/", method="GET", auth=auth)
        )
