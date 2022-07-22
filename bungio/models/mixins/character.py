from datetime import datetime
from typing import TYPE_CHECKING, AsyncGenerator, ForwardRef, Optional, Union

import attr

from bungio.models.base import MISSING, ClientMixin, FuzzyAttrFinder

if TYPE_CHECKING:
    # AUTOMATIC IMPORTS START
    from bungio.models import (
        BungieMembershipType,
        DestinyActivityHistoryResults,
        DestinyActivityModeType,
        DestinyAggregateActivityResults,
        DestinyCharacterResponse,
        DestinyCollectibleNodeDetailResponse,
        DestinyComponentType,
        DestinyHistoricalStatsByPeriod,
        DestinyHistoricalWeaponStatsData,
        DestinyLeaderboard,
        DestinyStatsGroupType,
        DestinyVendorFilter,
        DestinyVendorResponse,
        DestinyVendorsResponse,
        PeriodType,
    )

    # AUTOMATIC IMPORTS END
    from bungio.models.auth import AuthData
    from bungio.models.overwrites import DestinyHistoricalStatsPeriodGroup

__all__ = ("DestinyCharacterMixin",)


@attr.define
class DestinyCharacterMixin(ClientMixin, FuzzyAttrFinder):
    async def yield_activity_history(
        self,
        mode: Union["DestinyActivityModeType", int],
        earliest_allowed_datetime: Optional[datetime] = None,
        latest_allowed_datetime: Optional[datetime] = None,
        auth: Optional["AuthData"] = None,
    ) -> AsyncGenerator["DestinyHistoricalStatsPeriodGroup", None]:
        """
        Yields character activity history. Sorted by date descending, the latest one first.

        Args:
            mode: A filter for the activity mode to be returned. None returns all activities. See the documentation for DestinyActivityModeType for valid values, and pass in string representation.
            earliest_allowed_datetime: The earliest time the activity is allowed to have, fe. only entries after the 1/1/2020.
            latest_allowed_datetime: The latest time the activity is allowed to have, fe. only entries before the 1/1/2020.
            auth: Authentication information. Required when users with a private profile are queried, or when Bungie feels like it

        Returns:
            A generator for the model which is returned by bungie. [General endpoint information.](https://bungie-net.github.io/multi/index.html)
        """

        stop = False
        page = 0
        while True:
            if stop:
                break

            activities = await self.get_activity_history(count=250, mode=mode, page=page, auth=auth)

            # break if empty, fe. when pages are over
            if activities.activities is MISSING:
                break

            # yield the activities
            for activity in activities.activities:
                # check times if wanted
                if earliest_allowed_datetime or latest_allowed_datetime:
                    # check if the activity started later than the earliest allowed, else pass this one and do the next
                    # This works bc Bungie sorts the api with the newest entry on top
                    if earliest_allowed_datetime:
                        if activity.period < earliest_allowed_datetime:
                            stop = True
                            break

                    # check if the time is still in the timeframe, else break
                    if latest_allowed_datetime:
                        if activity.period > latest_allowed_datetime:
                            continue

                yield activity
            page += 1

    # DO NOT CHANGE ANY CODE BELOW. Automatically generated and overwritten

    async def get_character(
        self, components: list[Union["DestinyComponentType", int]], auth: Optional["AuthData"] = None
    ) -> "DestinyCharacterResponse":
        """
        Returns character information for the supplied character.

        Args:
            components: A comma separated list of components to return (as strings or numeric values). See the DestinyComponentType enum for valid components to request. You must request at least one component to receive results.
            auth: Authentication information. Required when users with a private profile are queried, or when Bungie feels like it

        Returns:
            The model which is returned by bungie. [General endpoint information.](https://bungie-net.github.io/multi/index.html)
        """

        return await self._client.api.get_character(
            character_id=self._fuzzy_getattr("character_id"),
            destiny_membership_id=self._fuzzy_getattr("membership_id"),
            membership_type=self._fuzzy_getattr("membership_type"),
            components=components,
            auth=auth,
        )

    async def get_vendors(
        self,
        components: list[Union["DestinyComponentType", int]],
        filter: Union["DestinyVendorFilter", int],
        auth: Optional["AuthData"] = None,
    ) -> "DestinyVendorsResponse":
        """
        Get currently available vendors from the list of vendors that can possibly have rotating inventory. Note that this does not include things like preview vendors and vendors-as-kiosks, neither of whom have rotating/dynamic inventories. Use their definitions as-is for those.

        Args:
            components: A comma separated list of components to return (as strings or numeric values). See the DestinyComponentType enum for valid components to request. You must request at least one component to receive results.
            filter: The filter of what vendors and items to return, if any.
            auth: Authentication information. Required when users with a private profile are queried, or when Bungie feels like it

        Returns:
            The model which is returned by bungie. [General endpoint information.](https://bungie-net.github.io/multi/index.html)
        """

        return await self._client.api.get_vendors(
            character_id=self._fuzzy_getattr("character_id"),
            destiny_membership_id=self._fuzzy_getattr("membership_id"),
            membership_type=self._fuzzy_getattr("membership_type"),
            components=components,
            filter=filter,
            auth=auth,
        )

    async def get_vendor(
        self, vendor_hash: int, components: list[Union["DestinyComponentType", int]], auth: Optional["AuthData"] = None
    ) -> "DestinyVendorResponse":
        """
        Get the details of a specific Vendor.

        Args:
            vendor_hash: The Hash identifier of the Vendor to be returned.
            components: A comma separated list of components to return (as strings or numeric values). See the DestinyComponentType enum for valid components to request. You must request at least one component to receive results.
            auth: Authentication information. Required when users with a private profile are queried, or when Bungie feels like it

        Returns:
            The model which is returned by bungie. [General endpoint information.](https://bungie-net.github.io/multi/index.html)
        """

        return await self._client.api.get_vendor(
            character_id=self._fuzzy_getattr("character_id"),
            destiny_membership_id=self._fuzzy_getattr("membership_id"),
            membership_type=self._fuzzy_getattr("membership_type"),
            vendor_hash=vendor_hash,
            components=components,
            auth=auth,
        )

    async def get_collectible_node_details(
        self,
        collectible_presentation_node_hash: int,
        components: list[Union["DestinyComponentType", int]],
        auth: Optional["AuthData"] = None,
    ) -> "DestinyCollectibleNodeDetailResponse":
        """
        Given a Presentation Node that has Collectibles as direct descendants, this will return item details about those descendants in the context of the requesting character.

        Args:
            collectible_presentation_node_hash: The hash identifier of the Presentation Node for whom we should return collectible details. Details will only be returned for collectibles that are direct descendants of this node.
            components: A comma separated list of components to return (as strings or numeric values). See the DestinyComponentType enum for valid components to request. You must request at least one component to receive results.
            auth: Authentication information. Required when users with a private profile are queried, or when Bungie feels like it

        Returns:
            The model which is returned by bungie. [General endpoint information.](https://bungie-net.github.io/multi/index.html)
        """

        return await self._client.api.get_collectible_node_details(
            character_id=self._fuzzy_getattr("character_id"),
            collectible_presentation_node_hash=collectible_presentation_node_hash,
            destiny_membership_id=self._fuzzy_getattr("membership_id"),
            membership_type=self._fuzzy_getattr("membership_type"),
            components=components,
            auth=auth,
        )

    async def get_leaderboards_for_character(
        self, maxtop: int, modes: str, statid: str, auth: Optional["AuthData"] = None
    ) -> dict[str, dict[str, "DestinyLeaderboard"]]:
        """
        Gets leaderboards with the signed in user's friends and the supplied destinyMembershipId as the focus. PREVIEW: This endpoint is still in beta, and may experience rough edges. The schema is in final form, but there may be bugs that prevent desirable operation.

        Args:
            maxtop: Maximum number of top players to return. Use a large number to get entire leaderboard.
            modes: List of game modes for which to get leaderboards. See the documentation for DestinyActivityModeType for valid values, and pass in string representation, comma delimited.
            statid: ID of stat to return rather than returning all Leaderboard stats.
            auth: Authentication information. Required when users with a private profile are queried, or when Bungie feels like it

        Returns:
            The model which is returned by bungie. [General endpoint information.](https://bungie-net.github.io/multi/index.html)
        """

        return await self._client.api.get_leaderboards_for_character(
            character_id=self._fuzzy_getattr("character_id"),
            destiny_membership_id=self._fuzzy_getattr("membership_id"),
            membership_type=self._fuzzy_getattr("membership_type"),
            maxtop=maxtop,
            modes=modes,
            statid=statid,
            auth=auth,
        )

    async def get_historical_stats(
        self,
        dayend: datetime,
        daystart: datetime,
        groups: list[Union["DestinyStatsGroupType", int]],
        modes: list[Union["DestinyActivityModeType", int]],
        period_type: Union["PeriodType", int],
        auth: Optional["AuthData"] = None,
    ) -> dict[str, "DestinyHistoricalStatsByPeriod"]:
        """
        Gets historical stats for indicated character.

        Args:
            dayend: Last day to return when daily stats are requested. Use the format YYYY-MM-DD. Currently, we cannot allow more than 31 days of daily data to be requested in a single request.
            daystart: First day to return when daily stats are requested. Use the format YYYY-MM-DD. Currently, we cannot allow more than 31 days of daily data to be requested in a single request.
            groups: Group of stats to include, otherwise only general stats are returned. Comma separated list is allowed. Values: General, Weapons, Medals
            modes: Game modes to return. See the documentation for DestinyActivityModeType for valid values, and pass in string representation, comma delimited.
            period_type: Indicates a specific period type to return. Optional. May be: Daily, AllTime, or Activity
            auth: Authentication information. Required when users with a private profile are queried, or when Bungie feels like it

        Returns:
            The model which is returned by bungie. [General endpoint information.](https://bungie-net.github.io/multi/index.html)
        """

        return await self._client.api.get_historical_stats(
            character_id=self._fuzzy_getattr("character_id"),
            destiny_membership_id=self._fuzzy_getattr("membership_id"),
            membership_type=self._fuzzy_getattr("membership_type"),
            dayend=dayend,
            daystart=daystart,
            groups=groups,
            modes=modes,
            period_type=period_type,
            auth=auth,
        )

    async def get_activity_history(
        self, count: int, mode: Union["DestinyActivityModeType", int], page: int, auth: Optional["AuthData"] = None
    ) -> "DestinyActivityHistoryResults":
        """
        Gets activity history stats for indicated character.

        Args:
            count: Number of rows to return
            mode: A filter for the activity mode to be returned. None returns all activities. See the documentation for DestinyActivityModeType for valid values, and pass in string representation.
            page: Page number to return, starting with 0.
            auth: Authentication information. Required when users with a private profile are queried, or when Bungie feels like it

        Returns:
            The model which is returned by bungie. [General endpoint information.](https://bungie-net.github.io/multi/index.html)
        """

        return await self._client.api.get_activity_history(
            character_id=self._fuzzy_getattr("character_id"),
            destiny_membership_id=self._fuzzy_getattr("membership_id"),
            membership_type=self._fuzzy_getattr("membership_type"),
            count=count,
            mode=mode,
            page=page,
            auth=auth,
        )

    async def get_unique_weapon_history(self, auth: Optional["AuthData"] = None) -> "DestinyHistoricalWeaponStatsData":
        """
        Gets details about unique weapon usage, including all exotic weapons.

        Args:
            auth: Authentication information. Required when users with a private profile are queried, or when Bungie feels like it

        Returns:
            The model which is returned by bungie. [General endpoint information.](https://bungie-net.github.io/multi/index.html)
        """

        return await self._client.api.get_unique_weapon_history(
            character_id=self._fuzzy_getattr("character_id"),
            destiny_membership_id=self._fuzzy_getattr("membership_id"),
            membership_type=self._fuzzy_getattr("membership_type"),
            auth=auth,
        )

    async def get_destiny_aggregate_activity_stats(
        self, auth: Optional["AuthData"] = None
    ) -> "DestinyAggregateActivityResults":
        """
        Gets all activities the character has participated in together with aggregate statistics for those activities.

        Args:
            auth: Authentication information. Required when users with a private profile are queried, or when Bungie feels like it

        Returns:
            The model which is returned by bungie. [General endpoint information.](https://bungie-net.github.io/multi/index.html)
        """

        return await self._client.api.get_destiny_aggregate_activity_stats(
            character_id=self._fuzzy_getattr("character_id"),
            destiny_membership_id=self._fuzzy_getattr("membership_id"),
            membership_type=self._fuzzy_getattr("membership_type"),
            auth=auth,
        )
