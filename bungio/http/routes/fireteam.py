from typing import Callable, Coroutine, Optional

from bungio.http.route import Route
from bungio.models.auth import AuthData


class FireteamRouteHttpRequests:
    request: Callable[..., Coroutine]

    async def get_active_private_clan_fireteam_count(self, group_id: int, auth: AuthData, *args, **kwargs) -> dict:
        """
        Gets a count of all active non-public fireteams for the specified clan. Maximum value returned is 25.

        Warning: Requires Authentication.
            Required oauth2 scopes: ReadGroups

        Args:
            group_id: The group id of the clan.
            auth: Authentication information.

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

        return await self.request(Route(path=f"/Fireteam/Clan/{group_id}/ActiveCount/", method="GET", auth=auth))

    async def get_available_clan_fireteams(
        self,
        activity_type: int,
        date_range: int,
        group_id: int,
        page: int,
        platform: int,
        public_only: int,
        slot_filter: int,
        auth: AuthData,
        exclude_immediate: Optional[bool] = None,
        lang_filter: Optional[str] = None,
        *args,
        **kwargs,
    ) -> dict:
        """
        Gets a listing of all of this clan's fireteams that are have available slots. Caller is not checked for join criteria so caching is maximized.

        Warning: Requires Authentication.
            Required oauth2 scopes: ReadGroups

        Args:
            activity_type: The activity type to filter by.
            date_range: The date range to grab available fireteams.
            group_id: The group id of the clan.
            page: Zero based page
            platform: The platform filter.
            public_only: Determines public/private filtering.
            slot_filter: Filters based on available slots
            auth: Authentication information.
            exclude_immediate: If you wish the result to exclude immediate fireteams, set this to true. Immediate-only can be forced using the dateRange enum.
            lang_filter: An optional language filter.

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
            Route(
                path=f"/Fireteam/Clan/{group_id}/Available/{platform}/{activity_type}/{date_range}/{slot_filter}/{public_only}/{page}/",
                method="GET",
                auth=auth,
                exclude_immediate=exclude_immediate,
                lang_filter=lang_filter,
            )
        )

    async def search_public_available_clan_fireteams(
        self,
        activity_type: int,
        date_range: int,
        page: int,
        platform: int,
        slot_filter: int,
        auth: AuthData,
        exclude_immediate: Optional[bool] = None,
        lang_filter: Optional[str] = None,
        *args,
        **kwargs,
    ) -> dict:
        """
        Gets a listing of all public fireteams starting now with open slots. Caller is not checked for join criteria so caching is maximized.

        Warning: Requires Authentication.
            Required oauth2 scopes: ReadGroups

        Args:
            activity_type: The activity type to filter by.
            date_range: The date range to grab available fireteams.
            page: Zero based page
            platform: The platform filter.
            slot_filter: Filters based on available slots
            auth: Authentication information.
            exclude_immediate: If you wish the result to exclude immediate fireteams, set this to true. Immediate-only can be forced using the dateRange enum.
            lang_filter: An optional language filter.

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
            Route(
                path=f"/Fireteam/Search/Available/{platform}/{activity_type}/{date_range}/{slot_filter}/{page}/",
                method="GET",
                auth=auth,
                exclude_immediate=exclude_immediate,
                lang_filter=lang_filter,
            )
        )

    async def get_my_clan_fireteams(
        self,
        group_id: int,
        include_closed: bool,
        page: int,
        platform: int,
        auth: AuthData,
        group_filter: Optional[bool] = None,
        lang_filter: Optional[str] = None,
        *args,
        **kwargs,
    ) -> dict:
        """
        Gets a listing of all fireteams that caller is an applicant, a member, or an alternate of.

        Warning: Requires Authentication.
            Required oauth2 scopes: ReadGroups

        Args:
            group_id: The group id of the clan. (This parameter is ignored unless the optional query parameter groupFilter is true).
            include_closed: If true, return fireteams that have been closed.
            page: Deprecated parameter, ignored.
            platform: The platform filter.
            auth: Authentication information.
            group_filter: If true, filter by clan. Otherwise, ignore the clan and show all of the user's fireteams.
            lang_filter: An optional language filter.

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
            Route(
                path=f"/Fireteam/Clan/{group_id}/My/{platform}/{include_closed}/{page}/",
                method="GET",
                auth=auth,
                group_filter=group_filter,
                lang_filter=lang_filter,
            )
        )

    async def get_clan_fireteam(self, fireteam_id: int, group_id: int, auth: AuthData, *args, **kwargs) -> dict:
        """
        Gets a specific fireteam.

        Warning: Requires Authentication.
            Required oauth2 scopes: ReadGroups

        Args:
            fireteam_id: The unique id of the fireteam.
            group_id: The group id of the clan.
            auth: Authentication information.

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
            Route(path=f"/Fireteam/Clan/{group_id}/Summary/{fireteam_id}/", method="GET", auth=auth)
        )
