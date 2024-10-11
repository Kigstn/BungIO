# DO NOT CHANGE ANY CODE BELOW
# This file is generated automatically by `generate_api_schema.py` and will be overwritten
# Instead, change functions / models by subclassing them in the `./overwrites/` folder. They will be used instead.

from typing import Optional, Union

from bungio.models import (
    BungieMembershipType,
    DestinyFireteamFinderApplicationType,
    DestinyFireteamFinderApplyToListingResponse,
    DestinyFireteamFinderBulkGetListingStatusResponse,
    DestinyFireteamFinderGetApplicationResponse,
    DestinyFireteamFinderGetCharacterActivityAccessResponse,
    DestinyFireteamFinderGetListingApplicationsResponse,
    DestinyFireteamFinderGetLobbyOffersResponse,
    DestinyFireteamFinderGetPlayerApplicationsResponse,
    DestinyFireteamFinderGetPlayerLobbiesResponse,
    DestinyFireteamFinderGetPlayerOffersResponse,
    DestinyFireteamFinderHostLobbyRequest,
    DestinyFireteamFinderHostLobbyResponse,
    DestinyFireteamFinderJoinLobbyRequest,
    DestinyFireteamFinderKickPlayerRequest,
    DestinyFireteamFinderListing,
    DestinyFireteamFinderLobbyResponse,
    DestinyFireteamFinderOffer,
    DestinyFireteamFinderRespondToApplicationRequest,
    DestinyFireteamFinderRespondToApplicationResponse,
    DestinyFireteamFinderRespondToAuthenticationRequest,
    DestinyFireteamFinderRespondToAuthenticationResponse,
    DestinyFireteamFinderRespondToOfferRequest,
    DestinyFireteamFinderRespondToOfferResponse,
    DestinyFireteamFinderSearchListingsByClanRequest,
    DestinyFireteamFinderSearchListingsByClanResponse,
    DestinyFireteamFinderSearchListingsByFiltersRequest,
    DestinyFireteamFinderSearchListingsByFiltersResponse,
    DestinyFireteamFinderUpdateLobbySettingsRequest,
    DestinyFireteamFinderUpdateLobbySettingsResponse,
)
from bungio.models.auth import AuthData
from bungio.models.base import ClientMixin, custom_define


@custom_define()
class FireteamFinderRouteInterface(ClientMixin):
    async def activate_lobby(
        self,
        destiny_character_id: int,
        destiny_membership_id: int,
        destiny_membership_type: Union[BungieMembershipType, int],
        lobby_id: int,
        force_activation: Optional[bool] = None,
        auth: Optional[AuthData] = None,
    ) -> bool:
        """
        Activates a lobby and initializes it as an active Fireteam.

        Args:
            destiny_character_id: A valid Destiny character ID.
            destiny_membership_id: A valid Destiny membership ID.
            destiny_membership_type: A valid Destiny membership type.
            lobby_id: The ID of the lobby to activate.
            force_activation: Optional boolean to forcibly activate the lobby, kicking pending applicants.
            auth: Authentication information. Required when users with a private profile are queried, or when Bungie feels like it

        Returns:
            The model which is returned by bungie. [General endpoint information.](https://bungie-net.github.io/multi/index.html)
        """

        response = await self._client.http.activate_lobby(
            destiny_character_id=destiny_character_id,
            destiny_membership_id=destiny_membership_id,
            destiny_membership_type=getattr(destiny_membership_type, "value", destiny_membership_type),
            lobby_id=lobby_id,
            force_activation=force_activation if force_activation is not None else None,
            auth=auth,
        )
        return response["Response"]

    async def activate_lobby_for_new_listing_id(
        self,
        destiny_character_id: int,
        destiny_membership_id: int,
        destiny_membership_type: Union[BungieMembershipType, int],
        lobby_id: int,
        force_activation: Optional[bool] = None,
        auth: Optional[AuthData] = None,
    ) -> bool:
        """
        Activates a lobby and initializes it as an active Fireteam, returning the updated Listing ID.

        Args:
            destiny_character_id: A valid Destiny character ID.
            destiny_membership_id: A valid Destiny membership ID.
            destiny_membership_type: A valid Destiny membership type.
            lobby_id: The ID of the lobby to activate.
            force_activation: Optional boolean to forcibly activate the lobby, kicking pending applicants.
            auth: Authentication information. Required when users with a private profile are queried, or when Bungie feels like it

        Returns:
            The model which is returned by bungie. [General endpoint information.](https://bungie-net.github.io/multi/index.html)
        """

        response = await self._client.http.activate_lobby_for_new_listing_id(
            destiny_character_id=destiny_character_id,
            destiny_membership_id=destiny_membership_id,
            destiny_membership_type=getattr(destiny_membership_type, "value", destiny_membership_type),
            lobby_id=lobby_id,
            force_activation=force_activation if force_activation is not None else None,
            auth=auth,
        )
        return response["Response"]

    async def apply_to_listing(
        self,
        application_type: Union[DestinyFireteamFinderApplicationType, int],
        destiny_character_id: int,
        destiny_membership_id: int,
        destiny_membership_type: Union[BungieMembershipType, int],
        listing_id: int,
        auth: Optional[AuthData] = None,
    ) -> DestinyFireteamFinderApplyToListingResponse:
        """
        Applies to have a character join a fireteam.

        Args:
            application_type: The type of application to apply
            destiny_character_id: A valid Destiny character ID.
            destiny_membership_id: A valid Destiny membership ID.
            destiny_membership_type: A valid Destiny membership type.
            listing_id: The id of the listing to apply to
            auth: Authentication information. Required when users with a private profile are queried, or when Bungie feels like it

        Returns:
            The model which is returned by bungie. [General endpoint information.](https://bungie-net.github.io/multi/index.html)
        """

        response = await self._client.http.apply_to_listing(
            application_type=getattr(application_type, "value", application_type),
            destiny_character_id=destiny_character_id,
            destiny_membership_id=destiny_membership_id,
            destiny_membership_type=getattr(destiny_membership_type, "value", destiny_membership_type),
            listing_id=listing_id,
            auth=auth,
        )
        return await DestinyFireteamFinderApplyToListingResponse.from_dict(
            data=response,
            client=self._client,
            application_type=application_type,
            destiny_character_id=destiny_character_id,
            destiny_membership_id=destiny_membership_id,
            destiny_membership_type=destiny_membership_type,
            listing_id=listing_id,
            auth=auth,
        )

    async def bulk_get_listing_status(
        self,
        data: dict,
        destiny_character_id: int,
        destiny_membership_id: int,
        destiny_membership_type: Union[BungieMembershipType, int],
        auth: Optional[AuthData] = None,
    ) -> DestinyFireteamFinderBulkGetListingStatusResponse:
        """
        Retrieves Fireteam listing statuses in bulk.

        Args:
            data: The required data for this request.
            destiny_character_id: A valid Destiny character ID.
            destiny_membership_id: A valid Destiny membership ID.
            destiny_membership_type: A valid Destiny membership type.
            auth: Authentication information. Required when users with a private profile are queried, or when Bungie feels like it

        Returns:
            The model which is returned by bungie. [General endpoint information.](https://bungie-net.github.io/multi/index.html)
        """

        response = await self._client.http.bulk_get_listing_status(
            destiny_character_id=destiny_character_id,
            destiny_membership_id=destiny_membership_id,
            destiny_membership_type=getattr(destiny_membership_type, "value", destiny_membership_type),
            auth=auth,
            **data.to_dict(_return_to_bungie_case=False),
        )
        return await DestinyFireteamFinderBulkGetListingStatusResponse.from_dict(
            data=response,
            client=self._client,
            destiny_character_id=destiny_character_id,
            destiny_membership_id=destiny_membership_id,
            destiny_membership_type=destiny_membership_type,
            auth=auth,
        )

    async def get_application(
        self,
        application_id: int,
        destiny_character_id: int,
        destiny_membership_id: int,
        destiny_membership_type: Union[BungieMembershipType, int],
        auth: Optional[AuthData] = None,
    ) -> DestinyFireteamFinderGetApplicationResponse:
        """
        Retrieves a Fireteam application.

        Args:
            application_id:
            destiny_character_id: A valid Destiny character ID.
            destiny_membership_id: A valid Destiny membership ID.
            destiny_membership_type: A valid Destiny membership type.
            auth: Authentication information. Required when users with a private profile are queried, or when Bungie feels like it

        Returns:
            The model which is returned by bungie. [General endpoint information.](https://bungie-net.github.io/multi/index.html)
        """

        response = await self._client.http.get_application(
            application_id=application_id,
            destiny_character_id=destiny_character_id,
            destiny_membership_id=destiny_membership_id,
            destiny_membership_type=getattr(destiny_membership_type, "value", destiny_membership_type),
            auth=auth,
        )
        return await DestinyFireteamFinderGetApplicationResponse.from_dict(
            data=response,
            client=self._client,
            application_id=application_id,
            destiny_character_id=destiny_character_id,
            destiny_membership_id=destiny_membership_id,
            destiny_membership_type=destiny_membership_type,
            auth=auth,
        )

    async def get_listing(self, listing_id: int, auth: Optional[AuthData] = None) -> DestinyFireteamFinderListing:
        """
        Retrieves a Fireteam listing.

        Args:
            listing_id: The ID of the listing to retrieve.
            auth: Authentication information. Required when users with a private profile are queried, or when Bungie feels like it

        Returns:
            The model which is returned by bungie. [General endpoint information.](https://bungie-net.github.io/multi/index.html)
        """

        response = await self._client.http.get_listing(listing_id=listing_id, auth=auth)
        return await DestinyFireteamFinderListing.from_dict(
            data=response, client=self._client, listing_id=listing_id, auth=auth
        )

    async def get_listing_applications(
        self,
        destiny_character_id: int,
        destiny_membership_id: int,
        destiny_membership_type: Union[BungieMembershipType, int],
        listing_id: int,
        flags: Optional[int] = None,
        next_page_token: Optional[str] = None,
        page_size: Optional[int] = None,
        auth: Optional[AuthData] = None,
    ) -> DestinyFireteamFinderGetListingApplicationsResponse:
        """
        Retrieves all applications to a Fireteam Finder listing.

        Args:
            destiny_character_id: A valid Destiny character ID.
            destiny_membership_id: A valid Destiny membership ID.
            destiny_membership_type: A valid Destiny membership type.
            listing_id: The ID of the listing whose applications to retrieve.
            flags: Optional flag representing a filter on the state of the application.
            next_page_token: An optional token from a previous response to fetch the next page of results.
            page_size: The maximum number of results to be returned with this page.
            auth: Authentication information. Required when users with a private profile are queried, or when Bungie feels like it

        Returns:
            The model which is returned by bungie. [General endpoint information.](https://bungie-net.github.io/multi/index.html)
        """

        response = await self._client.http.get_listing_applications(
            destiny_character_id=destiny_character_id,
            destiny_membership_id=destiny_membership_id,
            destiny_membership_type=getattr(destiny_membership_type, "value", destiny_membership_type),
            listing_id=listing_id,
            flags=flags if flags is not None else None,
            next_page_token=next_page_token if next_page_token is not None else None,
            page_size=page_size if page_size is not None else None,
            auth=auth,
        )
        return await DestinyFireteamFinderGetListingApplicationsResponse.from_dict(
            data=response,
            client=self._client,
            destiny_character_id=destiny_character_id,
            destiny_membership_id=destiny_membership_id,
            destiny_membership_type=destiny_membership_type,
            listing_id=listing_id,
            flags=flags,
            next_page_token=next_page_token,
            page_size=page_size,
            auth=auth,
        )

    async def get_lobby(
        self,
        destiny_character_id: int,
        destiny_membership_id: int,
        destiny_membership_type: Union[BungieMembershipType, int],
        lobby_id: int,
        auth: Optional[AuthData] = None,
    ) -> DestinyFireteamFinderLobbyResponse:
        """
        Retrieves the information for a Fireteam lobby.

        Args:
            destiny_character_id: A valid Destiny character ID.
            destiny_membership_id: A valid Destiny membership ID.
            destiny_membership_type: A valid Destiny membership type.
            lobby_id: The ID of the lobby to retrieve.
            auth: Authentication information. Required when users with a private profile are queried, or when Bungie feels like it

        Returns:
            The model which is returned by bungie. [General endpoint information.](https://bungie-net.github.io/multi/index.html)
        """

        response = await self._client.http.get_lobby(
            destiny_character_id=destiny_character_id,
            destiny_membership_id=destiny_membership_id,
            destiny_membership_type=getattr(destiny_membership_type, "value", destiny_membership_type),
            lobby_id=lobby_id,
            auth=auth,
        )
        return await DestinyFireteamFinderLobbyResponse.from_dict(
            data=response,
            client=self._client,
            destiny_character_id=destiny_character_id,
            destiny_membership_id=destiny_membership_id,
            destiny_membership_type=destiny_membership_type,
            lobby_id=lobby_id,
            auth=auth,
        )

    async def get_player_lobbies(
        self,
        destiny_character_id: int,
        destiny_membership_id: int,
        destiny_membership_type: Union[BungieMembershipType, int],
        next_page_token: Optional[str] = None,
        page_size: Optional[int] = None,
        auth: Optional[AuthData] = None,
    ) -> DestinyFireteamFinderGetPlayerLobbiesResponse:
        """
        Retrieves the information for a Fireteam lobby.

        Args:
            destiny_character_id: A valid Destiny character ID.
            destiny_membership_id: A valid Destiny membership ID.
            destiny_membership_type: A valid Destiny membership type.
            next_page_token: An optional token from a previous response to fetch the next page of results.
            page_size: The maximum number of results to be returned with this page.
            auth: Authentication information. Required when users with a private profile are queried, or when Bungie feels like it

        Returns:
            The model which is returned by bungie. [General endpoint information.](https://bungie-net.github.io/multi/index.html)
        """

        response = await self._client.http.get_player_lobbies(
            destiny_character_id=destiny_character_id,
            destiny_membership_id=destiny_membership_id,
            destiny_membership_type=getattr(destiny_membership_type, "value", destiny_membership_type),
            next_page_token=next_page_token if next_page_token is not None else None,
            page_size=page_size if page_size is not None else None,
            auth=auth,
        )
        return await DestinyFireteamFinderGetPlayerLobbiesResponse.from_dict(
            data=response,
            client=self._client,
            destiny_character_id=destiny_character_id,
            destiny_membership_id=destiny_membership_id,
            destiny_membership_type=destiny_membership_type,
            next_page_token=next_page_token,
            page_size=page_size,
            auth=auth,
        )

    async def get_player_applications(
        self,
        destiny_character_id: int,
        destiny_membership_id: int,
        destiny_membership_type: Union[BungieMembershipType, int],
        next_page_token: Optional[str] = None,
        page_size: Optional[int] = None,
        auth: Optional[AuthData] = None,
    ) -> DestinyFireteamFinderGetPlayerApplicationsResponse:
        """
        Retrieves Fireteam applications that this player has sent or recieved.

        Args:
            destiny_character_id: A valid Destiny character ID.
            destiny_membership_id: A valid Destiny membership ID.
            destiny_membership_type: A valid Destiny membership type.
            next_page_token: An optional token from a previous response to fetch the next page of results.
            page_size: The maximum number of results to be returned with this page.
            auth: Authentication information. Required when users with a private profile are queried, or when Bungie feels like it

        Returns:
            The model which is returned by bungie. [General endpoint information.](https://bungie-net.github.io/multi/index.html)
        """

        response = await self._client.http.get_player_applications(
            destiny_character_id=destiny_character_id,
            destiny_membership_id=destiny_membership_id,
            destiny_membership_type=getattr(destiny_membership_type, "value", destiny_membership_type),
            next_page_token=next_page_token if next_page_token is not None else None,
            page_size=page_size if page_size is not None else None,
            auth=auth,
        )
        return await DestinyFireteamFinderGetPlayerApplicationsResponse.from_dict(
            data=response,
            client=self._client,
            destiny_character_id=destiny_character_id,
            destiny_membership_id=destiny_membership_id,
            destiny_membership_type=destiny_membership_type,
            next_page_token=next_page_token,
            page_size=page_size,
            auth=auth,
        )

    async def get_player_offers(
        self,
        destiny_character_id: int,
        destiny_membership_id: int,
        destiny_membership_type: Union[BungieMembershipType, int],
        next_page_token: Optional[str] = None,
        page_size: Optional[int] = None,
        auth: Optional[AuthData] = None,
    ) -> DestinyFireteamFinderGetPlayerOffersResponse:
        """
        Retrieves Fireteam offers that this player has recieved.

        Args:
            destiny_character_id: A valid Destiny character ID.
            destiny_membership_id: A valid Destiny membership ID.
            destiny_membership_type: A valid Destiny membership type.
            next_page_token: An optional token from a previous response to fetch the next page of results.
            page_size: The maximum number of results to be returned with this page.
            auth: Authentication information. Required when users with a private profile are queried, or when Bungie feels like it

        Returns:
            The model which is returned by bungie. [General endpoint information.](https://bungie-net.github.io/multi/index.html)
        """

        response = await self._client.http.get_player_offers(
            destiny_character_id=destiny_character_id,
            destiny_membership_id=destiny_membership_id,
            destiny_membership_type=getattr(destiny_membership_type, "value", destiny_membership_type),
            next_page_token=next_page_token if next_page_token is not None else None,
            page_size=page_size if page_size is not None else None,
            auth=auth,
        )
        return await DestinyFireteamFinderGetPlayerOffersResponse.from_dict(
            data=response,
            client=self._client,
            destiny_character_id=destiny_character_id,
            destiny_membership_id=destiny_membership_id,
            destiny_membership_type=destiny_membership_type,
            next_page_token=next_page_token,
            page_size=page_size,
            auth=auth,
        )

    async def get_character_activity_access(
        self,
        destiny_character_id: int,
        destiny_membership_id: int,
        destiny_membership_type: Union[BungieMembershipType, int],
        auth: Optional[AuthData] = None,
    ) -> DestinyFireteamFinderGetCharacterActivityAccessResponse:
        """
        Retrieves the information for a Fireteam lobby.

        Args:
            destiny_character_id: A valid Destiny character ID.
            destiny_membership_id: A valid Destiny membership ID.
            destiny_membership_type: A valid Destiny membership type.
            auth: Authentication information. Required when users with a private profile are queried, or when Bungie feels like it

        Returns:
            The model which is returned by bungie. [General endpoint information.](https://bungie-net.github.io/multi/index.html)
        """

        response = await self._client.http.get_character_activity_access(
            destiny_character_id=destiny_character_id,
            destiny_membership_id=destiny_membership_id,
            destiny_membership_type=getattr(destiny_membership_type, "value", destiny_membership_type),
            auth=auth,
        )
        return await DestinyFireteamFinderGetCharacterActivityAccessResponse.from_dict(
            data=response,
            client=self._client,
            destiny_character_id=destiny_character_id,
            destiny_membership_id=destiny_membership_id,
            destiny_membership_type=destiny_membership_type,
            auth=auth,
        )

    async def get_offer(
        self,
        destiny_character_id: int,
        destiny_membership_id: int,
        destiny_membership_type: Union[BungieMembershipType, int],
        offer_id: int,
        auth: Optional[AuthData] = None,
    ) -> DestinyFireteamFinderOffer:
        """
        Retrieves an offer to a Fireteam lobby.

        Args:
            destiny_character_id: A valid Destiny character ID.
            destiny_membership_id: A valid Destiny membership ID.
            destiny_membership_type: A valid Destiny membership type.
            offer_id: The unique ID of the offer.
            auth: Authentication information. Required when users with a private profile are queried, or when Bungie feels like it

        Returns:
            The model which is returned by bungie. [General endpoint information.](https://bungie-net.github.io/multi/index.html)
        """

        response = await self._client.http.get_offer(
            destiny_character_id=destiny_character_id,
            destiny_membership_id=destiny_membership_id,
            destiny_membership_type=getattr(destiny_membership_type, "value", destiny_membership_type),
            offer_id=offer_id,
            auth=auth,
        )
        return await DestinyFireteamFinderOffer.from_dict(
            data=response,
            client=self._client,
            destiny_character_id=destiny_character_id,
            destiny_membership_id=destiny_membership_id,
            destiny_membership_type=destiny_membership_type,
            offer_id=offer_id,
            auth=auth,
        )

    async def get_lobby_offers(
        self,
        destiny_character_id: int,
        destiny_membership_id: int,
        destiny_membership_type: Union[BungieMembershipType, int],
        lobby_id: int,
        next_page_token: Optional[str] = None,
        page_size: Optional[int] = None,
        auth: Optional[AuthData] = None,
    ) -> DestinyFireteamFinderGetLobbyOffersResponse:
        """
        Retrieves all offers relevant to a Fireteam lobby.

        Args:
            destiny_character_id: A valid Destiny character ID.
            destiny_membership_id: A valid Destiny membership ID.
            destiny_membership_type: A valid Destiny membership type.
            lobby_id: The unique ID of the lobby.
            next_page_token: An optional token from a previous response to fetch the next page of results.
            page_size: The maximum number of results to be returned with this page.
            auth: Authentication information. Required when users with a private profile are queried, or when Bungie feels like it

        Returns:
            The model which is returned by bungie. [General endpoint information.](https://bungie-net.github.io/multi/index.html)
        """

        response = await self._client.http.get_lobby_offers(
            destiny_character_id=destiny_character_id,
            destiny_membership_id=destiny_membership_id,
            destiny_membership_type=getattr(destiny_membership_type, "value", destiny_membership_type),
            lobby_id=lobby_id,
            next_page_token=next_page_token if next_page_token is not None else None,
            page_size=page_size if page_size is not None else None,
            auth=auth,
        )
        return await DestinyFireteamFinderGetLobbyOffersResponse.from_dict(
            data=response,
            client=self._client,
            destiny_character_id=destiny_character_id,
            destiny_membership_id=destiny_membership_id,
            destiny_membership_type=destiny_membership_type,
            lobby_id=lobby_id,
            next_page_token=next_page_token,
            page_size=page_size,
            auth=auth,
        )

    async def host_lobby(
        self,
        data: DestinyFireteamFinderHostLobbyRequest,
        destiny_character_id: int,
        destiny_membership_id: int,
        destiny_membership_type: Union[BungieMembershipType, int],
        auth: Optional[AuthData] = None,
    ) -> DestinyFireteamFinderHostLobbyResponse:
        """
        Creates a new Fireteam lobby and Fireteam Finder listing.

        Args:
            data: The required data for this request.
            destiny_character_id: A valid Destiny character ID.
            destiny_membership_id: A valid Destiny membership ID.
            destiny_membership_type: A valid Destiny membership type.
            auth: Authentication information. Required when users with a private profile are queried, or when Bungie feels like it

        Returns:
            The model which is returned by bungie. [General endpoint information.](https://bungie-net.github.io/multi/index.html)
        """

        response = await self._client.http.host_lobby(
            destiny_character_id=destiny_character_id,
            destiny_membership_id=destiny_membership_id,
            destiny_membership_type=getattr(destiny_membership_type, "value", destiny_membership_type),
            auth=auth,
            **data.to_dict(_return_to_bungie_case=False),
        )
        return await DestinyFireteamFinderHostLobbyResponse.from_dict(
            data=response,
            client=self._client,
            destiny_character_id=destiny_character_id,
            destiny_membership_id=destiny_membership_id,
            destiny_membership_type=destiny_membership_type,
            auth=auth,
        )

    async def join_lobby(
        self,
        data: DestinyFireteamFinderJoinLobbyRequest,
        destiny_character_id: int,
        destiny_membership_id: int,
        destiny_membership_type: Union[BungieMembershipType, int],
        auth: Optional[AuthData] = None,
    ) -> DestinyFireteamFinderLobbyResponse:
        """
        Sends a request to join an available Fireteam lobby.

        Args:
            data: The required data for this request.
            destiny_character_id: A valid Destiny character ID.
            destiny_membership_id: A valid Destiny membership ID.
            destiny_membership_type: A valid Destiny membership type.
            auth: Authentication information. Required when users with a private profile are queried, or when Bungie feels like it

        Returns:
            The model which is returned by bungie. [General endpoint information.](https://bungie-net.github.io/multi/index.html)
        """

        response = await self._client.http.join_lobby(
            destiny_character_id=destiny_character_id,
            destiny_membership_id=destiny_membership_id,
            destiny_membership_type=getattr(destiny_membership_type, "value", destiny_membership_type),
            auth=auth,
            **data.to_dict(_return_to_bungie_case=False),
        )
        return await DestinyFireteamFinderLobbyResponse.from_dict(
            data=response,
            client=self._client,
            destiny_character_id=destiny_character_id,
            destiny_membership_id=destiny_membership_id,
            destiny_membership_type=destiny_membership_type,
            auth=auth,
        )

    async def kick_player(
        self,
        data: DestinyFireteamFinderKickPlayerRequest,
        destiny_character_id: int,
        destiny_membership_id: int,
        destiny_membership_type: Union[BungieMembershipType, int],
        lobby_id: int,
        target_membership_id: int,
        auth: Optional[AuthData] = None,
    ) -> bool:
        """
        Kicks a player from a Fireteam Finder lobby.

        Args:
            data: The required data for this request.
            destiny_character_id: A valid Destiny character ID.
            destiny_membership_id: A valid Destiny membership ID.
            destiny_membership_type: A valid Destiny membership type.
            lobby_id: The ID of the lobby to kick the player from.
            target_membership_id: A valid Destiny membership ID of the player to kick.
            auth: Authentication information. Required when users with a private profile are queried, or when Bungie feels like it

        Returns:
            The model which is returned by bungie. [General endpoint information.](https://bungie-net.github.io/multi/index.html)
        """

        response = await self._client.http.kick_player(
            destiny_character_id=destiny_character_id,
            destiny_membership_id=destiny_membership_id,
            destiny_membership_type=getattr(destiny_membership_type, "value", destiny_membership_type),
            lobby_id=lobby_id,
            target_membership_id=target_membership_id,
            auth=auth,
            **data.to_dict(_return_to_bungie_case=False),
        )
        return response["Response"]

    async def leave_application(
        self,
        application_id: int,
        destiny_character_id: int,
        destiny_membership_id: int,
        destiny_membership_type: Union[BungieMembershipType, int],
        auth: Optional[AuthData] = None,
    ) -> bool:
        """
        Sends a request to leave a Fireteam listing application.

        Args:
            application_id: The ID of the application to leave.
            destiny_character_id: A valid Destiny character ID.
            destiny_membership_id: A valid Destiny membership ID.
            destiny_membership_type: A valid Destiny membership type.
            auth: Authentication information. Required when users with a private profile are queried, or when Bungie feels like it

        Returns:
            The model which is returned by bungie. [General endpoint information.](https://bungie-net.github.io/multi/index.html)
        """

        response = await self._client.http.leave_application(
            application_id=application_id,
            destiny_character_id=destiny_character_id,
            destiny_membership_id=destiny_membership_id,
            destiny_membership_type=getattr(destiny_membership_type, "value", destiny_membership_type),
            auth=auth,
        )
        return response["Response"]

    async def leave_lobby(
        self,
        destiny_character_id: int,
        destiny_membership_id: int,
        destiny_membership_type: Union[BungieMembershipType, int],
        lobby_id: int,
        auth: Optional[AuthData] = None,
    ) -> bool:
        """
        Sends a request to leave a Fireteam lobby.

        Args:
            destiny_character_id: A valid Destiny character ID.
            destiny_membership_id: A valid Destiny membership ID.
            destiny_membership_type: A valid Destiny membership type.
            lobby_id: The ID of the lobby to leave.
            auth: Authentication information. Required when users with a private profile are queried, or when Bungie feels like it

        Returns:
            The model which is returned by bungie. [General endpoint information.](https://bungie-net.github.io/multi/index.html)
        """

        response = await self._client.http.leave_lobby(
            destiny_character_id=destiny_character_id,
            destiny_membership_id=destiny_membership_id,
            destiny_membership_type=getattr(destiny_membership_type, "value", destiny_membership_type),
            lobby_id=lobby_id,
            auth=auth,
        )
        return response["Response"]

    async def respond_to_application(
        self,
        data: DestinyFireteamFinderRespondToApplicationRequest,
        application_id: int,
        destiny_character_id: int,
        destiny_membership_id: int,
        destiny_membership_type: Union[BungieMembershipType, int],
        auth: Optional[AuthData] = None,
    ) -> DestinyFireteamFinderRespondToApplicationResponse:
        """
        Responds to an application sent to a Fireteam lobby.

        Args:
            data: The required data for this request.
            application_id: The application ID to respond to.
            destiny_character_id: A valid Destiny character ID.
            destiny_membership_id: A valid Destiny membership ID.
            destiny_membership_type: A valid Destiny membership type.
            auth: Authentication information. Required when users with a private profile are queried, or when Bungie feels like it

        Returns:
            The model which is returned by bungie. [General endpoint information.](https://bungie-net.github.io/multi/index.html)
        """

        response = await self._client.http.respond_to_application(
            application_id=application_id,
            destiny_character_id=destiny_character_id,
            destiny_membership_id=destiny_membership_id,
            destiny_membership_type=getattr(destiny_membership_type, "value", destiny_membership_type),
            auth=auth,
            **data.to_dict(_return_to_bungie_case=False),
        )
        return await DestinyFireteamFinderRespondToApplicationResponse.from_dict(
            data=response,
            client=self._client,
            application_id=application_id,
            destiny_character_id=destiny_character_id,
            destiny_membership_id=destiny_membership_id,
            destiny_membership_type=destiny_membership_type,
            auth=auth,
        )

    async def respond_to_authentication(
        self,
        data: DestinyFireteamFinderRespondToAuthenticationRequest,
        application_id: int,
        destiny_character_id: int,
        destiny_membership_id: int,
        destiny_membership_type: Union[BungieMembershipType, int],
        auth: Optional[AuthData] = None,
    ) -> DestinyFireteamFinderRespondToAuthenticationResponse:
        """
        Responds to an authentication request for a Fireteam.

        Args:
            data: The required data for this request.
            application_id: The ID of the application whose authentication to confirm.
            destiny_character_id: A valid Destiny character ID.
            destiny_membership_id: A valid Destiny membership ID.
            destiny_membership_type: A valid Destiny membership type.
            auth: Authentication information. Required when users with a private profile are queried, or when Bungie feels like it

        Returns:
            The model which is returned by bungie. [General endpoint information.](https://bungie-net.github.io/multi/index.html)
        """

        response = await self._client.http.respond_to_authentication(
            application_id=application_id,
            destiny_character_id=destiny_character_id,
            destiny_membership_id=destiny_membership_id,
            destiny_membership_type=getattr(destiny_membership_type, "value", destiny_membership_type),
            auth=auth,
            **data.to_dict(_return_to_bungie_case=False),
        )
        return await DestinyFireteamFinderRespondToAuthenticationResponse.from_dict(
            data=response,
            client=self._client,
            application_id=application_id,
            destiny_character_id=destiny_character_id,
            destiny_membership_id=destiny_membership_id,
            destiny_membership_type=destiny_membership_type,
            auth=auth,
        )

    async def respond_to_offer(
        self,
        data: DestinyFireteamFinderRespondToOfferRequest,
        destiny_character_id: int,
        destiny_membership_id: int,
        destiny_membership_type: Union[BungieMembershipType, int],
        offer_id: int,
        auth: Optional[AuthData] = None,
    ) -> DestinyFireteamFinderRespondToOfferResponse:
        """
        Responds to a Fireteam lobby offer.

        Args:
            data: The required data for this request.
            destiny_character_id: A valid Destiny character ID.
            destiny_membership_id: A valid Destiny membership ID.
            destiny_membership_type: A valid Destiny membership type.
            offer_id: The unique ID of the offer.
            auth: Authentication information. Required when users with a private profile are queried, or when Bungie feels like it

        Returns:
            The model which is returned by bungie. [General endpoint information.](https://bungie-net.github.io/multi/index.html)
        """

        response = await self._client.http.respond_to_offer(
            destiny_character_id=destiny_character_id,
            destiny_membership_id=destiny_membership_id,
            destiny_membership_type=getattr(destiny_membership_type, "value", destiny_membership_type),
            offer_id=offer_id,
            auth=auth,
            **data.to_dict(_return_to_bungie_case=False),
        )
        return await DestinyFireteamFinderRespondToOfferResponse.from_dict(
            data=response,
            client=self._client,
            destiny_character_id=destiny_character_id,
            destiny_membership_id=destiny_membership_id,
            destiny_membership_type=destiny_membership_type,
            offer_id=offer_id,
            auth=auth,
        )

    async def search_listings_by_clan(
        self,
        data: DestinyFireteamFinderSearchListingsByClanRequest,
        destiny_character_id: int,
        destiny_membership_id: int,
        destiny_membership_type: Union[BungieMembershipType, int],
        auth: Optional[AuthData] = None,
    ) -> DestinyFireteamFinderSearchListingsByClanResponse:
        """
        Returns search results for available Fireteams provided a clan.

        Args:
            data: The required data for this request.
            destiny_character_id: A valid Destiny character ID.
            destiny_membership_id: A valid Destiny membership ID.
            destiny_membership_type: A valid Destiny membership type.
            auth: Authentication information. Required when users with a private profile are queried, or when Bungie feels like it

        Returns:
            The model which is returned by bungie. [General endpoint information.](https://bungie-net.github.io/multi/index.html)
        """

        response = await self._client.http.search_listings_by_clan(
            destiny_character_id=destiny_character_id,
            destiny_membership_id=destiny_membership_id,
            destiny_membership_type=getattr(destiny_membership_type, "value", destiny_membership_type),
            auth=auth,
            **data.to_dict(_return_to_bungie_case=False),
        )
        return await DestinyFireteamFinderSearchListingsByClanResponse.from_dict(
            data=response,
            client=self._client,
            destiny_character_id=destiny_character_id,
            destiny_membership_id=destiny_membership_id,
            destiny_membership_type=destiny_membership_type,
            auth=auth,
        )

    async def search_listings_by_filters(
        self,
        data: DestinyFireteamFinderSearchListingsByFiltersRequest,
        destiny_character_id: int,
        destiny_membership_id: int,
        destiny_membership_type: Union[BungieMembershipType, int],
        auth: Optional[AuthData] = None,
    ) -> DestinyFireteamFinderSearchListingsByFiltersResponse:
        """
        Returns search results for available Fireteams provided search filters.

        Args:
            data: The required data for this request.
            destiny_character_id: A valid Destiny character ID.
            destiny_membership_id: A valid Destiny membership ID.
            destiny_membership_type: A valid Destiny membership type.
            auth: Authentication information. Required when users with a private profile are queried, or when Bungie feels like it

        Returns:
            The model which is returned by bungie. [General endpoint information.](https://bungie-net.github.io/multi/index.html)
        """

        response = await self._client.http.search_listings_by_filters(
            destiny_character_id=destiny_character_id,
            destiny_membership_id=destiny_membership_id,
            destiny_membership_type=getattr(destiny_membership_type, "value", destiny_membership_type),
            auth=auth,
            **data.to_dict(_return_to_bungie_case=False),
        )
        return await DestinyFireteamFinderSearchListingsByFiltersResponse.from_dict(
            data=response,
            client=self._client,
            destiny_character_id=destiny_character_id,
            destiny_membership_id=destiny_membership_id,
            destiny_membership_type=destiny_membership_type,
            auth=auth,
        )

    async def update_lobby_settings(
        self,
        data: DestinyFireteamFinderUpdateLobbySettingsRequest,
        destiny_character_id: int,
        destiny_membership_id: int,
        destiny_membership_type: Union[BungieMembershipType, int],
        lobby_id: int,
        auth: Optional[AuthData] = None,
    ) -> DestinyFireteamFinderUpdateLobbySettingsResponse:
        """
        Updates the settings for a Fireteam lobby.

        Args:
            data: The required data for this request.
            destiny_character_id: A valid Destiny character ID.
            destiny_membership_id: A valid Destiny membership ID.
            destiny_membership_type: A valid Destiny membership type.
            lobby_id: The ID of the lobby to update.
            auth: Authentication information. Required when users with a private profile are queried, or when Bungie feels like it

        Returns:
            The model which is returned by bungie. [General endpoint information.](https://bungie-net.github.io/multi/index.html)
        """

        response = await self._client.http.update_lobby_settings(
            destiny_character_id=destiny_character_id,
            destiny_membership_id=destiny_membership_id,
            destiny_membership_type=getattr(destiny_membership_type, "value", destiny_membership_type),
            lobby_id=lobby_id,
            auth=auth,
            **data.to_dict(_return_to_bungie_case=False),
        )
        return await DestinyFireteamFinderUpdateLobbySettingsResponse.from_dict(
            data=response,
            client=self._client,
            destiny_character_id=destiny_character_id,
            destiny_membership_id=destiny_membership_id,
            destiny_membership_type=destiny_membership_type,
            lobby_id=lobby_id,
            auth=auth,
        )
