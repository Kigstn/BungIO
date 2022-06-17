from typing import Optional

import attr

from bungio.models import (
    FireteamDateRange,
    FireteamPlatform,
    FireteamPublicSearchOption,
    FireteamResponse,
    FireteamSlotSearch,
    SearchResultOfFireteamResponse,
    SearchResultOfFireteamSummary,
)
from bungio.models.auth import AuthData
from bungio.models.base import ClientMixin


@attr.define
class FireteamRouteInterface(ClientMixin):
    async def get_active_private_clan_fireteam_count(self, group_id: int, auth: AuthData) -> int:
        """
        Gets a count of all active non-public fireteams for the specified clan. Maximum value returned is 25.

        Warning: Requires Authentication.
            Required oauth2 scopes: ReadGroups

        Args:
            group_id: The group id of the clan.
            auth: Authentication information.

        Returns:
            The model which is returned by bungie. [General endpoint information.](https://bungie-net.github.io/multi/index.html)
        """

        response = await self._client.http.get_active_private_clan_fireteam_count(group_id=group_id, auth=auth)
        return response["Response"]

    async def get_available_clan_fireteams(
        self,
        activity_type: int,
        date_range: FireteamDateRange,
        group_id: int,
        page: int,
        platform: FireteamPlatform,
        public_only: FireteamPublicSearchOption,
        slot_filter: FireteamSlotSearch,
        auth: AuthData,
        lang_filter: Optional[str] = None,
    ) -> SearchResultOfFireteamSummary:
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
            lang_filter: An optional language filter.

        Returns:
            The model which is returned by bungie. [General endpoint information.](https://bungie-net.github.io/multi/index.html)
        """

        response = await self._client.http.get_available_clan_fireteams(
            activity_type=activity_type,
            date_range=date_range.value,
            group_id=group_id,
            page=page,
            platform=platform.value,
            public_only=public_only.value,
            slot_filter=slot_filter.value,
            auth=auth,
            lang_filter=lang_filter,
        )
        return await SearchResultOfFireteamSummary.from_dict(data=response, client=self._client)

    async def search_public_available_clan_fireteams(
        self,
        activity_type: int,
        date_range: FireteamDateRange,
        page: int,
        platform: FireteamPlatform,
        slot_filter: FireteamSlotSearch,
        auth: AuthData,
        lang_filter: Optional[str] = None,
    ) -> SearchResultOfFireteamSummary:
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
            lang_filter: An optional language filter.

        Returns:
            The model which is returned by bungie. [General endpoint information.](https://bungie-net.github.io/multi/index.html)
        """

        response = await self._client.http.search_public_available_clan_fireteams(
            activity_type=activity_type,
            date_range=date_range.value,
            page=page,
            platform=platform.value,
            slot_filter=slot_filter.value,
            auth=auth,
            lang_filter=lang_filter,
        )
        return await SearchResultOfFireteamSummary.from_dict(data=response, client=self._client)

    async def get_my_clan_fireteams(
        self,
        group_id: int,
        include_closed: bool,
        page: int,
        platform: FireteamPlatform,
        auth: AuthData,
        group_filter: Optional[bool] = None,
        lang_filter: Optional[str] = None,
    ) -> SearchResultOfFireteamResponse:
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

        Returns:
            The model which is returned by bungie. [General endpoint information.](https://bungie-net.github.io/multi/index.html)
        """

        response = await self._client.http.get_my_clan_fireteams(
            group_id=group_id,
            include_closed=include_closed,
            page=page,
            platform=platform.value,
            auth=auth,
            group_filter=group_filter,
            lang_filter=lang_filter,
        )
        return await SearchResultOfFireteamResponse.from_dict(data=response, client=self._client)

    async def get_clan_fireteam(self, fireteam_id: int, group_id: int, auth: AuthData) -> FireteamResponse:
        """
        Gets a specific fireteam.

        Warning: Requires Authentication.
            Required oauth2 scopes: ReadGroups

        Args:
            fireteam_id: The unique id of the fireteam.
            group_id: The group id of the clan.
            auth: Authentication information.

        Returns:
            The model which is returned by bungie. [General endpoint information.](https://bungie-net.github.io/multi/index.html)
        """

        response = await self._client.http.get_clan_fireteam(fireteam_id=fireteam_id, group_id=group_id, auth=auth)
        return await FireteamResponse.from_dict(data=response, client=self._client)
