# DO NOT CHANGE ANY CODE BELOW
# This file is generated automatically by `generate_api_schema.py` and will be overwritten
# Instead, change functions / models by subclassing them in the `./overwrites/` folder. They will be used instead.

from typing import Optional, Union

from bungio.models.base import ClientMixin, custom_define
from bungio.models.auth import AuthData

from bungio.models import FireteamDateRange
from bungio.models import SearchResultOfFireteamResponse
from bungio.models import SearchResultOfFireteamSummary
from bungio.models import FireteamPlatform
from bungio.models import FireteamPublicSearchOption
from bungio.models import FireteamResponse
from bungio.models import FireteamSlotSearch


@custom_define()
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
        date_range: Union[FireteamDateRange, int],
        group_id: int,
        page: int,
        platform: Union[FireteamPlatform, int],
        public_only: Union[FireteamPublicSearchOption, int],
        slot_filter: Union[FireteamSlotSearch, int],
        auth: AuthData,
        exclude_immediate: Optional[bool] = None,
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
            exclude_immediate: If you wish the result to exclude immediate fireteams, set this to true. Immediate-only can be forced using the dateRange enum.
            lang_filter: An optional language filter.

        Returns:
            The model which is returned by bungie. [General endpoint information.](https://bungie-net.github.io/multi/index.html)
        """

        response = await self._client.http.get_available_clan_fireteams(
            activity_type=activity_type,
            date_range=getattr(date_range, "value", date_range),
            group_id=group_id,
            page=page,
            platform=getattr(platform, "value", platform),
            public_only=getattr(public_only, "value", public_only),
            slot_filter=getattr(slot_filter, "value", slot_filter),
            auth=auth,
            exclude_immediate=exclude_immediate if exclude_immediate is not None else None,
            lang_filter=lang_filter if lang_filter is not None else None,
        )
        return await SearchResultOfFireteamSummary.from_dict(
            data=response,
            client=self._client,
            activity_type=activity_type,
            date_range=date_range,
            group_id=group_id,
            page=page,
            platform=platform,
            public_only=public_only,
            slot_filter=slot_filter,
            auth=auth,
            exclude_immediate=exclude_immediate,
            lang_filter=lang_filter,
        )

    async def search_public_available_clan_fireteams(
        self,
        activity_type: int,
        date_range: Union[FireteamDateRange, int],
        page: int,
        platform: Union[FireteamPlatform, int],
        slot_filter: Union[FireteamSlotSearch, int],
        auth: AuthData,
        exclude_immediate: Optional[bool] = None,
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
            exclude_immediate: If you wish the result to exclude immediate fireteams, set this to true. Immediate-only can be forced using the dateRange enum.
            lang_filter: An optional language filter.

        Returns:
            The model which is returned by bungie. [General endpoint information.](https://bungie-net.github.io/multi/index.html)
        """

        response = await self._client.http.search_public_available_clan_fireteams(
            activity_type=activity_type,
            date_range=getattr(date_range, "value", date_range),
            page=page,
            platform=getattr(platform, "value", platform),
            slot_filter=getattr(slot_filter, "value", slot_filter),
            auth=auth,
            exclude_immediate=exclude_immediate if exclude_immediate is not None else None,
            lang_filter=lang_filter if lang_filter is not None else None,
        )
        return await SearchResultOfFireteamSummary.from_dict(
            data=response,
            client=self._client,
            activity_type=activity_type,
            date_range=date_range,
            page=page,
            platform=platform,
            slot_filter=slot_filter,
            auth=auth,
            exclude_immediate=exclude_immediate,
            lang_filter=lang_filter,
        )

    async def get_my_clan_fireteams(
        self,
        group_id: int,
        include_closed: bool,
        page: int,
        platform: Union[FireteamPlatform, int],
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
            platform=getattr(platform, "value", platform),
            auth=auth,
            group_filter=group_filter if group_filter is not None else None,
            lang_filter=lang_filter if lang_filter is not None else None,
        )
        return await SearchResultOfFireteamResponse.from_dict(
            data=response,
            client=self._client,
            group_id=group_id,
            include_closed=include_closed,
            page=page,
            platform=platform,
            auth=auth,
            group_filter=group_filter,
            lang_filter=lang_filter,
        )

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
        return await FireteamResponse.from_dict(
            data=response, client=self._client, fireteam_id=fireteam_id, group_id=group_id, auth=auth
        )
