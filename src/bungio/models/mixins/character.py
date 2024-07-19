from datetime import datetime
from typing import TYPE_CHECKING, AsyncGenerator, Optional, Union

from bungio.models.base import MISSING, ClientMixin, FuzzyAttrFinder, custom_define

if TYPE_CHECKING:
    # AUTOMATIC IMPORTS START
    from bungio.models import DestinyFireteamFinderLobbyResponse
    from bungio.models import DestinyFireteamFinderBulkGetListingStatusResponse
    from bungio.models import DestinyHistoricalStatsByPeriod
    from bungio.models import DestinyFireteamFinderGetPlayerOffersResponse
    from bungio.models import DestinyFireteamFinderRespondToApplicationResponse
    from bungio.models import DestinyAggregateActivityResults
    from bungio.models import DestinyFireteamFinderApplicationType
    from bungio.models import DestinyFireteamFinderHostLobbyResponse
    from bungio.models import DestinyFireteamFinderKickPlayerRequest
    from bungio.models import DestinyHistoricalWeaponStatsData
    from bungio.models import DestinyFireteamFinderUpdateLobbySettingsRequest
    from bungio.models import DestinyFireteamFinderSearchListingsByFiltersRequest
    from bungio.models import DestinyFireteamFinderRespondToAuthenticationResponse
    from bungio.models import DestinyVendorFilter
    from bungio.models import DestinyVendorResponse
    from bungio.models import DestinyFireteamFinderSearchListingsByClanRequest
    from bungio.models import DestinyFireteamFinderApplyToListingResponse
    from bungio.models import DestinyFireteamFinderSearchListingsByFiltersResponse
    from bungio.models import DestinyCollectibleNodeDetailResponse
    from bungio.models import DestinyFireteamFinderSearchListingsByClanResponse
    from bungio.models import DestinyFireteamFinderGetPlayerApplicationsResponse
    from bungio.models import DestinyFireteamFinderJoinLobbyRequest
    from bungio.models import DestinyFireteamFinderHostLobbyRequest
    from bungio.models import DestinyFireteamFinderGetPlayerLobbiesResponse
    from bungio.models import DestinyFireteamFinderGetApplicationResponse
    from bungio.models import DestinyStatsGroupType
    from bungio.models import DestinyFireteamFinderRespondToOfferRequest
    from bungio.models import DestinyFireteamFinderRespondToAuthenticationRequest
    from bungio.models import DestinyVendorsResponse
    from bungio.models import DestinyActivityModeType
    from bungio.models import DestinyFireteamFinderOffer
    from bungio.models import DestinyFireteamFinderGetLobbyOffersResponse
    from bungio.models import DestinyCharacterResponse
    from bungio.models import DestinyFireteamFinderUpdateLobbySettingsResponse
    from bungio.models import DestinyActivityHistoryResults
    from bungio.models import DestinyFireteamFinderRespondToOfferResponse
    from bungio.models import PeriodType
    from bungio.models import DestinyFireteamFinderGetCharacterActivityAccessResponse
    from bungio.models import DestinyFireteamFinderGetListingApplicationsResponse
    from bungio.models import DestinyComponentType
    from bungio.models import DestinyLeaderboard
    from bungio.models import DestinyFireteamFinderRespondToApplicationRequest

    # AUTOMATIC IMPORTS END
    from bungio.models.auth import AuthData
    from bungio.models.overwrites import DestinyHistoricalStatsPeriodGroup

__all__ = ("DestinyCharacterMixin",)


@custom_define()
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

    async def activate_lobby(self, lobby_id: int, force_activation: bool, auth: Optional["AuthData"] = None) -> bool:
        """
        Activates a lobby and initializes it as an active Fireteam.

        Args:
            lobby_id: The ID of the lobby to activate.
            force_activation: Optional boolean to forcibly activate the lobby, kicking pending applicants.
            auth: Authentication information. Required when users with a private profile are queried, or when Bungie feels like it

        Returns:
            The model which is returned by bungie. [General endpoint information.](https://bungie-net.github.io/multi/index.html)
        """

        return await self._client.api.activate_lobby(
            destiny_character_id=self._fuzzy_getattr("character_id"),
            destiny_membership_id=self._fuzzy_getattr("membership_id"),
            destiny_membership_type=self._fuzzy_getattr("membership_type"),
            lobby_id=lobby_id,
            force_activation=force_activation,
            auth=auth,
        )

    async def activate_lobby_for_new_listing_id(
        self, lobby_id: int, force_activation: bool, auth: Optional["AuthData"] = None
    ) -> bool:
        """
        Activates a lobby and initializes it as an active Fireteam, returning the updated Listing ID.

        Args:
            lobby_id: The ID of the lobby to activate.
            force_activation: Optional boolean to forcibly activate the lobby, kicking pending applicants.
            auth: Authentication information. Required when users with a private profile are queried, or when Bungie feels like it

        Returns:
            The model which is returned by bungie. [General endpoint information.](https://bungie-net.github.io/multi/index.html)
        """

        return await self._client.api.activate_lobby_for_new_listing_id(
            destiny_character_id=self._fuzzy_getattr("character_id"),
            destiny_membership_id=self._fuzzy_getattr("membership_id"),
            destiny_membership_type=self._fuzzy_getattr("membership_type"),
            lobby_id=lobby_id,
            force_activation=force_activation,
            auth=auth,
        )

    async def apply_to_listing(
        self,
        application_type: Union["DestinyFireteamFinderApplicationType", int],
        listing_id: int,
        auth: Optional["AuthData"] = None,
    ) -> "DestinyFireteamFinderApplyToListingResponse":
        """
        Applies to have a character join a fireteam.

        Args:
            application_type: The type of application to apply
            listing_id: The id of the listing to apply to
            auth: Authentication information. Required when users with a private profile are queried, or when Bungie feels like it

        Returns:
            The model which is returned by bungie. [General endpoint information.](https://bungie-net.github.io/multi/index.html)
        """

        return await self._client.api.apply_to_listing(
            application_type=application_type,
            destiny_character_id=self._fuzzy_getattr("character_id"),
            destiny_membership_id=self._fuzzy_getattr("membership_id"),
            destiny_membership_type=self._fuzzy_getattr("membership_type"),
            listing_id=listing_id,
            auth=auth,
        )

    async def bulk_get_listing_status(
        self, data: dict, auth: Optional["AuthData"] = None
    ) -> "DestinyFireteamFinderBulkGetListingStatusResponse":
        """
        Retrieves Fireteam listing statuses in bulk.

        Args:
            data: The required data for this request.
            auth: Authentication information. Required when users with a private profile are queried, or when Bungie feels like it

        Returns:
            The model which is returned by bungie. [General endpoint information.](https://bungie-net.github.io/multi/index.html)
        """

        return await self._client.api.bulk_get_listing_status(
            data=data,
            destiny_character_id=self._fuzzy_getattr("character_id"),
            destiny_membership_id=self._fuzzy_getattr("membership_id"),
            destiny_membership_type=self._fuzzy_getattr("membership_type"),
            auth=auth,
        )

    async def get_application(
        self, application_id: int, auth: Optional["AuthData"] = None
    ) -> "DestinyFireteamFinderGetApplicationResponse":
        """
        Retrieves a Fireteam application.

        Args:
            application_id:
            auth: Authentication information. Required when users with a private profile are queried, or when Bungie feels like it

        Returns:
            The model which is returned by bungie. [General endpoint information.](https://bungie-net.github.io/multi/index.html)
        """

        return await self._client.api.get_application(
            application_id=application_id,
            destiny_character_id=self._fuzzy_getattr("character_id"),
            destiny_membership_id=self._fuzzy_getattr("membership_id"),
            destiny_membership_type=self._fuzzy_getattr("membership_type"),
            auth=auth,
        )

    async def get_listing_applications(
        self, listing_id: int, flags: int, next_page_token: str, page_size: int, auth: Optional["AuthData"] = None
    ) -> "DestinyFireteamFinderGetListingApplicationsResponse":
        """
        Retrieves all applications to a Fireteam Finder listing.

        Args:
            listing_id: The ID of the listing whose applications to retrieve.
            flags: Optional flag representing a filter on the state of the application.
            next_page_token: An optional token from a previous response to fetch the next page of results.
            page_size: The maximum number of results to be returned with this page.
            auth: Authentication information. Required when users with a private profile are queried, or when Bungie feels like it

        Returns:
            The model which is returned by bungie. [General endpoint information.](https://bungie-net.github.io/multi/index.html)
        """

        return await self._client.api.get_listing_applications(
            destiny_character_id=self._fuzzy_getattr("character_id"),
            destiny_membership_id=self._fuzzy_getattr("membership_id"),
            destiny_membership_type=self._fuzzy_getattr("membership_type"),
            listing_id=listing_id,
            flags=flags,
            next_page_token=next_page_token,
            page_size=page_size,
            auth=auth,
        )

    async def get_lobby(self, lobby_id: int, auth: Optional["AuthData"] = None) -> "DestinyFireteamFinderLobbyResponse":
        """
        Retrieves the information for a Fireteam lobby.

        Args:
            lobby_id: The ID of the lobby to retrieve.
            auth: Authentication information. Required when users with a private profile are queried, or when Bungie feels like it

        Returns:
            The model which is returned by bungie. [General endpoint information.](https://bungie-net.github.io/multi/index.html)
        """

        return await self._client.api.get_lobby(
            destiny_character_id=self._fuzzy_getattr("character_id"),
            destiny_membership_id=self._fuzzy_getattr("membership_id"),
            destiny_membership_type=self._fuzzy_getattr("membership_type"),
            lobby_id=lobby_id,
            auth=auth,
        )

    async def get_player_lobbies(
        self, next_page_token: str, page_size: int, auth: Optional["AuthData"] = None
    ) -> "DestinyFireteamFinderGetPlayerLobbiesResponse":
        """
        Retrieves the information for a Fireteam lobby.

        Args:
            next_page_token: An optional token from a previous response to fetch the next page of results.
            page_size: The maximum number of results to be returned with this page.
            auth: Authentication information. Required when users with a private profile are queried, or when Bungie feels like it

        Returns:
            The model which is returned by bungie. [General endpoint information.](https://bungie-net.github.io/multi/index.html)
        """

        return await self._client.api.get_player_lobbies(
            destiny_character_id=self._fuzzy_getattr("character_id"),
            destiny_membership_id=self._fuzzy_getattr("membership_id"),
            destiny_membership_type=self._fuzzy_getattr("membership_type"),
            next_page_token=next_page_token,
            page_size=page_size,
            auth=auth,
        )

    async def get_player_applications(
        self, next_page_token: str, page_size: int, auth: Optional["AuthData"] = None
    ) -> "DestinyFireteamFinderGetPlayerApplicationsResponse":
        """
        Retrieves Fireteam applications that this player has sent or recieved.

        Args:
            next_page_token: An optional token from a previous response to fetch the next page of results.
            page_size: The maximum number of results to be returned with this page.
            auth: Authentication information. Required when users with a private profile are queried, or when Bungie feels like it

        Returns:
            The model which is returned by bungie. [General endpoint information.](https://bungie-net.github.io/multi/index.html)
        """

        return await self._client.api.get_player_applications(
            destiny_character_id=self._fuzzy_getattr("character_id"),
            destiny_membership_id=self._fuzzy_getattr("membership_id"),
            destiny_membership_type=self._fuzzy_getattr("membership_type"),
            next_page_token=next_page_token,
            page_size=page_size,
            auth=auth,
        )

    async def get_player_offers(
        self, next_page_token: str, page_size: int, auth: Optional["AuthData"] = None
    ) -> "DestinyFireteamFinderGetPlayerOffersResponse":
        """
        Retrieves Fireteam offers that this player has recieved.

        Args:
            next_page_token: An optional token from a previous response to fetch the next page of results.
            page_size: The maximum number of results to be returned with this page.
            auth: Authentication information. Required when users with a private profile are queried, or when Bungie feels like it

        Returns:
            The model which is returned by bungie. [General endpoint information.](https://bungie-net.github.io/multi/index.html)
        """

        return await self._client.api.get_player_offers(
            destiny_character_id=self._fuzzy_getattr("character_id"),
            destiny_membership_id=self._fuzzy_getattr("membership_id"),
            destiny_membership_type=self._fuzzy_getattr("membership_type"),
            next_page_token=next_page_token,
            page_size=page_size,
            auth=auth,
        )

    async def get_character_activity_access(
        self, auth: Optional["AuthData"] = None
    ) -> "DestinyFireteamFinderGetCharacterActivityAccessResponse":
        """
        Retrieves the information for a Fireteam lobby.

        Args:
            auth: Authentication information. Required when users with a private profile are queried, or when Bungie feels like it

        Returns:
            The model which is returned by bungie. [General endpoint information.](https://bungie-net.github.io/multi/index.html)
        """

        return await self._client.api.get_character_activity_access(
            destiny_character_id=self._fuzzy_getattr("character_id"),
            destiny_membership_id=self._fuzzy_getattr("membership_id"),
            destiny_membership_type=self._fuzzy_getattr("membership_type"),
            auth=auth,
        )

    async def get_offer(self, offer_id: int, auth: Optional["AuthData"] = None) -> "DestinyFireteamFinderOffer":
        """
        Retrieves an offer to a Fireteam lobby.

        Args:
            offer_id: The unique ID of the offer.
            auth: Authentication information. Required when users with a private profile are queried, or when Bungie feels like it

        Returns:
            The model which is returned by bungie. [General endpoint information.](https://bungie-net.github.io/multi/index.html)
        """

        return await self._client.api.get_offer(
            destiny_character_id=self._fuzzy_getattr("character_id"),
            destiny_membership_id=self._fuzzy_getattr("membership_id"),
            destiny_membership_type=self._fuzzy_getattr("membership_type"),
            offer_id=offer_id,
            auth=auth,
        )

    async def get_lobby_offers(
        self, lobby_id: int, next_page_token: str, page_size: int, auth: Optional["AuthData"] = None
    ) -> "DestinyFireteamFinderGetLobbyOffersResponse":
        """
        Retrieves all offers relevant to a Fireteam lobby.

        Args:
            lobby_id: The unique ID of the lobby.
            next_page_token: An optional token from a previous response to fetch the next page of results.
            page_size: The maximum number of results to be returned with this page.
            auth: Authentication information. Required when users with a private profile are queried, or when Bungie feels like it

        Returns:
            The model which is returned by bungie. [General endpoint information.](https://bungie-net.github.io/multi/index.html)
        """

        return await self._client.api.get_lobby_offers(
            destiny_character_id=self._fuzzy_getattr("character_id"),
            destiny_membership_id=self._fuzzy_getattr("membership_id"),
            destiny_membership_type=self._fuzzy_getattr("membership_type"),
            lobby_id=lobby_id,
            next_page_token=next_page_token,
            page_size=page_size,
            auth=auth,
        )

    async def host_lobby(
        self, data: "DestinyFireteamFinderHostLobbyRequest", auth: Optional["AuthData"] = None
    ) -> "DestinyFireteamFinderHostLobbyResponse":
        """
        Creates a new Fireteam lobby and Fireteam Finder listing.

        Args:
            data: The required data for this request.
            auth: Authentication information. Required when users with a private profile are queried, or when Bungie feels like it

        Returns:
            The model which is returned by bungie. [General endpoint information.](https://bungie-net.github.io/multi/index.html)
        """

        return await self._client.api.host_lobby(
            data=data,
            destiny_character_id=self._fuzzy_getattr("character_id"),
            destiny_membership_id=self._fuzzy_getattr("membership_id"),
            destiny_membership_type=self._fuzzy_getattr("membership_type"),
            auth=auth,
        )

    async def join_lobby(
        self, data: "DestinyFireteamFinderJoinLobbyRequest", auth: Optional["AuthData"] = None
    ) -> "DestinyFireteamFinderLobbyResponse":
        """
        Sends a request to join an available Fireteam lobby.

        Args:
            data: The required data for this request.
            auth: Authentication information. Required when users with a private profile are queried, or when Bungie feels like it

        Returns:
            The model which is returned by bungie. [General endpoint information.](https://bungie-net.github.io/multi/index.html)
        """

        return await self._client.api.join_lobby(
            data=data,
            destiny_character_id=self._fuzzy_getattr("character_id"),
            destiny_membership_id=self._fuzzy_getattr("membership_id"),
            destiny_membership_type=self._fuzzy_getattr("membership_type"),
            auth=auth,
        )

    async def kick_player(
        self,
        data: "DestinyFireteamFinderKickPlayerRequest",
        lobby_id: int,
        target_membership_id: int,
        auth: Optional["AuthData"] = None,
    ) -> bool:
        """
        Kicks a player from a Fireteam Finder lobby.

        Args:
            data: The required data for this request.
            lobby_id: The ID of the lobby to kick the player from.
            target_membership_id: A valid Destiny membership ID of the player to kick.
            auth: Authentication information. Required when users with a private profile are queried, or when Bungie feels like it

        Returns:
            The model which is returned by bungie. [General endpoint information.](https://bungie-net.github.io/multi/index.html)
        """

        return await self._client.api.kick_player(
            data=data,
            destiny_character_id=self._fuzzy_getattr("character_id"),
            destiny_membership_id=self._fuzzy_getattr("membership_id"),
            destiny_membership_type=self._fuzzy_getattr("membership_type"),
            lobby_id=lobby_id,
            target_membership_id=target_membership_id,
            auth=auth,
        )

    async def leave_application(self, application_id: int, auth: Optional["AuthData"] = None) -> bool:
        """
        Sends a request to leave a Fireteam listing application.

        Args:
            application_id: The ID of the application to leave.
            auth: Authentication information. Required when users with a private profile are queried, or when Bungie feels like it

        Returns:
            The model which is returned by bungie. [General endpoint information.](https://bungie-net.github.io/multi/index.html)
        """

        return await self._client.api.leave_application(
            application_id=application_id,
            destiny_character_id=self._fuzzy_getattr("character_id"),
            destiny_membership_id=self._fuzzy_getattr("membership_id"),
            destiny_membership_type=self._fuzzy_getattr("membership_type"),
            auth=auth,
        )

    async def leave_lobby(self, lobby_id: int, auth: Optional["AuthData"] = None) -> bool:
        """
        Sends a request to leave a Fireteam lobby.

        Args:
            lobby_id: The ID of the lobby to leave.
            auth: Authentication information. Required when users with a private profile are queried, or when Bungie feels like it

        Returns:
            The model which is returned by bungie. [General endpoint information.](https://bungie-net.github.io/multi/index.html)
        """

        return await self._client.api.leave_lobby(
            destiny_character_id=self._fuzzy_getattr("character_id"),
            destiny_membership_id=self._fuzzy_getattr("membership_id"),
            destiny_membership_type=self._fuzzy_getattr("membership_type"),
            lobby_id=lobby_id,
            auth=auth,
        )

    async def respond_to_application(
        self,
        data: "DestinyFireteamFinderRespondToApplicationRequest",
        application_id: int,
        auth: Optional["AuthData"] = None,
    ) -> "DestinyFireteamFinderRespondToApplicationResponse":
        """
        Responds to an application sent to a Fireteam lobby.

        Args:
            data: The required data for this request.
            application_id: The application ID to respond to.
            auth: Authentication information. Required when users with a private profile are queried, or when Bungie feels like it

        Returns:
            The model which is returned by bungie. [General endpoint information.](https://bungie-net.github.io/multi/index.html)
        """

        return await self._client.api.respond_to_application(
            data=data,
            application_id=application_id,
            destiny_character_id=self._fuzzy_getattr("character_id"),
            destiny_membership_id=self._fuzzy_getattr("membership_id"),
            destiny_membership_type=self._fuzzy_getattr("membership_type"),
            auth=auth,
        )

    async def respond_to_authentication(
        self,
        data: "DestinyFireteamFinderRespondToAuthenticationRequest",
        application_id: int,
        auth: Optional["AuthData"] = None,
    ) -> "DestinyFireteamFinderRespondToAuthenticationResponse":
        """
        Responds to an authentication request for a Fireteam.

        Args:
            data: The required data for this request.
            application_id: The ID of the application whose authentication to confirm.
            auth: Authentication information. Required when users with a private profile are queried, or when Bungie feels like it

        Returns:
            The model which is returned by bungie. [General endpoint information.](https://bungie-net.github.io/multi/index.html)
        """

        return await self._client.api.respond_to_authentication(
            data=data,
            application_id=application_id,
            destiny_character_id=self._fuzzy_getattr("character_id"),
            destiny_membership_id=self._fuzzy_getattr("membership_id"),
            destiny_membership_type=self._fuzzy_getattr("membership_type"),
            auth=auth,
        )

    async def respond_to_offer(
        self, data: "DestinyFireteamFinderRespondToOfferRequest", offer_id: int, auth: Optional["AuthData"] = None
    ) -> "DestinyFireteamFinderRespondToOfferResponse":
        """
        Responds to a Fireteam lobby offer.

        Args:
            data: The required data for this request.
            offer_id: The unique ID of the offer.
            auth: Authentication information. Required when users with a private profile are queried, or when Bungie feels like it

        Returns:
            The model which is returned by bungie. [General endpoint information.](https://bungie-net.github.io/multi/index.html)
        """

        return await self._client.api.respond_to_offer(
            data=data,
            destiny_character_id=self._fuzzy_getattr("character_id"),
            destiny_membership_id=self._fuzzy_getattr("membership_id"),
            destiny_membership_type=self._fuzzy_getattr("membership_type"),
            offer_id=offer_id,
            auth=auth,
        )

    async def search_listings_by_clan(
        self, data: "DestinyFireteamFinderSearchListingsByClanRequest", auth: Optional["AuthData"] = None
    ) -> "DestinyFireteamFinderSearchListingsByClanResponse":
        """
        Returns search results for available Fireteams provided a clan.

        Args:
            data: The required data for this request.
            auth: Authentication information. Required when users with a private profile are queried, or when Bungie feels like it

        Returns:
            The model which is returned by bungie. [General endpoint information.](https://bungie-net.github.io/multi/index.html)
        """

        return await self._client.api.search_listings_by_clan(
            data=data,
            destiny_character_id=self._fuzzy_getattr("character_id"),
            destiny_membership_id=self._fuzzy_getattr("membership_id"),
            destiny_membership_type=self._fuzzy_getattr("membership_type"),
            auth=auth,
        )

    async def search_listings_by_filters(
        self, data: "DestinyFireteamFinderSearchListingsByFiltersRequest", auth: Optional["AuthData"] = None
    ) -> "DestinyFireteamFinderSearchListingsByFiltersResponse":
        """
        Returns search results for available Fireteams provided search filters.

        Args:
            data: The required data for this request.
            auth: Authentication information. Required when users with a private profile are queried, or when Bungie feels like it

        Returns:
            The model which is returned by bungie. [General endpoint information.](https://bungie-net.github.io/multi/index.html)
        """

        return await self._client.api.search_listings_by_filters(
            data=data,
            destiny_character_id=self._fuzzy_getattr("character_id"),
            destiny_membership_id=self._fuzzy_getattr("membership_id"),
            destiny_membership_type=self._fuzzy_getattr("membership_type"),
            auth=auth,
        )

    async def update_lobby_settings(
        self, data: "DestinyFireteamFinderUpdateLobbySettingsRequest", lobby_id: int, auth: Optional["AuthData"] = None
    ) -> "DestinyFireteamFinderUpdateLobbySettingsResponse":
        """
        Updates the settings for a Fireteam lobby.

        Args:
            data: The required data for this request.
            lobby_id: The ID of the lobby to update.
            auth: Authentication information. Required when users with a private profile are queried, or when Bungie feels like it

        Returns:
            The model which is returned by bungie. [General endpoint information.](https://bungie-net.github.io/multi/index.html)
        """

        return await self._client.api.update_lobby_settings(
            data=data,
            destiny_character_id=self._fuzzy_getattr("character_id"),
            destiny_membership_id=self._fuzzy_getattr("membership_id"),
            destiny_membership_type=self._fuzzy_getattr("membership_type"),
            lobby_id=lobby_id,
            auth=auth,
        )
