from datetime import datetime
from typing import Callable, Coroutine, Optional, Any, Union

from bungio.http.route import Route
from bungio.models.auth import AuthData


class FireteamFinderRouteHttpRequests:
    request: Callable[..., Coroutine]

    async def activate_lobby(
        self,
        destiny_character_id: int,
        destiny_membership_id: int,
        destiny_membership_type: int,
        lobby_id: int,
        force_activation: Optional[bool] = None,
        auth: Optional[AuthData] = None,
        *args,
        **kwargs,
    ) -> dict:
        """
        Activates a lobby and initializes it as an active Fireteam.

        Args:
            destiny_character_id: A valid Destiny character ID.
            destiny_membership_id: A valid Destiny membership ID.
            destiny_membership_type: A valid Destiny membership type.
            lobby_id: The ID of the lobby to activate.
            force_activation: Optional boolean to forcibly activate the lobby, kicking pending applicants.
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
            Route(
                path=f"/FireteamFinder/Lobby/Activate/{lobby_id}/{destiny_membership_type}/{destiny_membership_id}/{destiny_character_id}/",
                method="POST",
                force_activation=force_activation,
                auth=auth,
            )
        )

    async def activate_lobby_for_new_listing_id(
        self,
        destiny_character_id: int,
        destiny_membership_id: int,
        destiny_membership_type: int,
        lobby_id: int,
        force_activation: Optional[bool] = None,
        auth: Optional[AuthData] = None,
        *args,
        **kwargs,
    ) -> dict:
        """
        Activates a lobby and initializes it as an active Fireteam, returning the updated Listing ID.

        Args:
            destiny_character_id: A valid Destiny character ID.
            destiny_membership_id: A valid Destiny membership ID.
            destiny_membership_type: A valid Destiny membership type.
            lobby_id: The ID of the lobby to activate.
            force_activation: Optional boolean to forcibly activate the lobby, kicking pending applicants.
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
            Route(
                path=f"/FireteamFinder/Lobby/ActivateForNewListingId/{lobby_id}/{destiny_membership_type}/{destiny_membership_id}/{destiny_character_id}/",
                method="POST",
                force_activation=force_activation,
                auth=auth,
            )
        )

    async def apply_to_listing(
        self,
        application_type: int,
        destiny_character_id: int,
        destiny_membership_id: int,
        destiny_membership_type: int,
        listing_id: int,
        auth: Optional[AuthData] = None,
        *args,
        **kwargs,
    ) -> dict:
        """
        Applies to have a character join a fireteam.

        Args:
            application_type: The type of application to apply
            destiny_character_id: A valid Destiny character ID.
            destiny_membership_id: A valid Destiny membership ID.
            destiny_membership_type: A valid Destiny membership type.
            listing_id: The id of the listing to apply to
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
            Route(
                path=f"/FireteamFinder/Listing/{listing_id}/Apply/{application_type}/{destiny_membership_type}/{destiny_membership_id}/{destiny_character_id}/",
                method="POST",
                auth=auth,
            )
        )

    async def bulk_get_listing_status(
        self,
        destiny_character_id: int,
        destiny_membership_id: int,
        destiny_membership_type: int,
        auth: Optional[AuthData] = None,
        *args,
        **kwargs,
    ) -> dict:
        """
        Retrieves Fireteam listing statuses in bulk.

        Args:
            destiny_character_id: A valid Destiny character ID.
            destiny_membership_id: A valid Destiny membership ID.
            destiny_membership_type: A valid Destiny membership type.
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
            Route(
                path=f"/FireteamFinder/Listing/BulkStatus/{destiny_membership_type}/{destiny_membership_id}/{destiny_character_id}/",
                method="POST",
                auth=auth,
            )
        )

    async def get_application(
        self,
        application_id: int,
        destiny_character_id: int,
        destiny_membership_id: int,
        destiny_membership_type: int,
        auth: Optional[AuthData] = None,
        *args,
        **kwargs,
    ) -> dict:
        """
        Retrieves a Fireteam application.

        Args:
            application_id:
            destiny_character_id: A valid Destiny character ID.
            destiny_membership_id: A valid Destiny membership ID.
            destiny_membership_type: A valid Destiny membership type.
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
            Route(
                path=f"/FireteamFinder/Application/{application_id}/{destiny_membership_type}/{destiny_membership_id}/{destiny_character_id}/",
                method="GET",
                auth=auth,
            )
        )

    async def get_listing(self, listing_id: int, auth: Optional[AuthData] = None, *args, **kwargs) -> dict:
        """
        Retrieves a Fireteam listing.

        Args:
            listing_id: The ID of the listing to retrieve.
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

        return await self.request(Route(path=f"/FireteamFinder/Listing/{listing_id}/", method="GET", auth=auth))

    async def get_listing_applications(
        self,
        destiny_character_id: int,
        destiny_membership_id: int,
        destiny_membership_type: int,
        listing_id: int,
        flags: Optional[int] = None,
        next_page_token: Optional[str] = None,
        page_size: Optional[int] = None,
        auth: Optional[AuthData] = None,
        *args,
        **kwargs,
    ) -> dict:
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
                path=f"/FireteamFinder/Listing/{listing_id}/Applications/{destiny_membership_type}/{destiny_membership_id}/{destiny_character_id}/",
                method="GET",
                flags=flags,
                next_page_token=next_page_token,
                page_size=page_size,
                auth=auth,
            )
        )

    async def get_lobby(
        self,
        destiny_character_id: int,
        destiny_membership_id: int,
        destiny_membership_type: int,
        lobby_id: int,
        auth: Optional[AuthData] = None,
        *args,
        **kwargs,
    ) -> dict:
        """
        Retrieves the information for a Fireteam lobby.

        Args:
            destiny_character_id: A valid Destiny character ID.
            destiny_membership_id: A valid Destiny membership ID.
            destiny_membership_type: A valid Destiny membership type.
            lobby_id: The ID of the lobby to retrieve.
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
            Route(
                path=f"/FireteamFinder/Lobby/{lobby_id}/{destiny_membership_type}/{destiny_membership_id}/{destiny_character_id}/",
                method="GET",
                auth=auth,
            )
        )

    async def get_player_lobbies(
        self,
        destiny_character_id: int,
        destiny_membership_id: int,
        destiny_membership_type: int,
        next_page_token: Optional[str] = None,
        page_size: Optional[int] = None,
        auth: Optional[AuthData] = None,
        *args,
        **kwargs,
    ) -> dict:
        """
        Retrieves the information for a Fireteam lobby.

        Args:
            destiny_character_id: A valid Destiny character ID.
            destiny_membership_id: A valid Destiny membership ID.
            destiny_membership_type: A valid Destiny membership type.
            next_page_token: An optional token from a previous response to fetch the next page of results.
            page_size: The maximum number of results to be returned with this page.
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
            Route(
                path=f"/FireteamFinder/PlayerLobbies/{destiny_membership_type}/{destiny_membership_id}/{destiny_character_id}/",
                method="GET",
                next_page_token=next_page_token,
                page_size=page_size,
                auth=auth,
            )
        )

    async def get_player_applications(
        self,
        destiny_character_id: int,
        destiny_membership_id: int,
        destiny_membership_type: int,
        next_page_token: Optional[str] = None,
        page_size: Optional[int] = None,
        auth: Optional[AuthData] = None,
        *args,
        **kwargs,
    ) -> dict:
        """
        Retrieves Fireteam applications that this player has sent or recieved.

        Args:
            destiny_character_id: A valid Destiny character ID.
            destiny_membership_id: A valid Destiny membership ID.
            destiny_membership_type: A valid Destiny membership type.
            next_page_token: An optional token from a previous response to fetch the next page of results.
            page_size: The maximum number of results to be returned with this page.
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
            Route(
                path=f"/FireteamFinder/PlayerApplications/{destiny_membership_type}/{destiny_membership_id}/{destiny_character_id}/",
                method="GET",
                next_page_token=next_page_token,
                page_size=page_size,
                auth=auth,
            )
        )

    async def get_player_offers(
        self,
        destiny_character_id: int,
        destiny_membership_id: int,
        destiny_membership_type: int,
        next_page_token: Optional[str] = None,
        page_size: Optional[int] = None,
        auth: Optional[AuthData] = None,
        *args,
        **kwargs,
    ) -> dict:
        """
        Retrieves Fireteam offers that this player has recieved.

        Args:
            destiny_character_id: A valid Destiny character ID.
            destiny_membership_id: A valid Destiny membership ID.
            destiny_membership_type: A valid Destiny membership type.
            next_page_token: An optional token from a previous response to fetch the next page of results.
            page_size: The maximum number of results to be returned with this page.
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
            Route(
                path=f"/FireteamFinder/PlayerOffers/{destiny_membership_type}/{destiny_membership_id}/{destiny_character_id}/",
                method="GET",
                next_page_token=next_page_token,
                page_size=page_size,
                auth=auth,
            )
        )

    async def get_character_activity_access(
        self,
        destiny_character_id: int,
        destiny_membership_id: int,
        destiny_membership_type: int,
        auth: Optional[AuthData] = None,
        *args,
        **kwargs,
    ) -> dict:
        """
        Retrieves the information for a Fireteam lobby.

        Args:
            destiny_character_id: A valid Destiny character ID.
            destiny_membership_id: A valid Destiny membership ID.
            destiny_membership_type: A valid Destiny membership type.
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
            Route(
                path=f"/FireteamFinder/CharacterActivityAccess/{destiny_membership_type}/{destiny_membership_id}/{destiny_character_id}/",
                method="GET",
                auth=auth,
            )
        )

    async def get_offer(
        self,
        destiny_character_id: int,
        destiny_membership_id: int,
        destiny_membership_type: int,
        offer_id: int,
        auth: Optional[AuthData] = None,
        *args,
        **kwargs,
    ) -> dict:
        """
        Retrieves an offer to a Fireteam lobby.

        Args:
            destiny_character_id: A valid Destiny character ID.
            destiny_membership_id: A valid Destiny membership ID.
            destiny_membership_type: A valid Destiny membership type.
            offer_id: The unique ID of the offer.
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
            Route(
                path=f"/FireteamFinder/Offer/{offer_id}/{destiny_membership_type}/{destiny_membership_id}/{destiny_character_id}/",
                method="GET",
                auth=auth,
            )
        )

    async def get_lobby_offers(
        self,
        destiny_character_id: int,
        destiny_membership_id: int,
        destiny_membership_type: int,
        lobby_id: int,
        next_page_token: Optional[str] = None,
        page_size: Optional[int] = None,
        auth: Optional[AuthData] = None,
        *args,
        **kwargs,
    ) -> dict:
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
                path=f"/FireteamFinder/Lobby/{lobby_id}/Offers/{destiny_membership_type}/{destiny_membership_id}/{destiny_character_id}/",
                method="GET",
                next_page_token=next_page_token,
                page_size=page_size,
                auth=auth,
            )
        )

    async def host_lobby(
        self,
        max_player_count: int,
        online_players_only: bool,
        privacy_scope: Union[Any, int],
        scheduled_date_time: datetime,
        clan_id: int,
        listing_values: list[Any],
        activity_graph_hash: int,
        activity_hash: int,
        destiny_character_id: int,
        destiny_membership_id: int,
        destiny_membership_type: int,
        auth: Optional[AuthData] = None,
        *args,
        **kwargs,
    ) -> dict:
        """
        Creates a new Fireteam lobby and Fireteam Finder listing.

        Args:
            max_player_count: _No description given by bungie._
            online_players_only: _No description given by bungie._
            privacy_scope: _No description given by bungie._
            scheduled_date_time: _No description given by bungie._
            clan_id: _No description given by bungie._
            listing_values: _No description given by bungie._
            activity_graph_hash: _No description given by bungie._
            activity_hash: _No description given by bungie._
            destiny_character_id: A valid Destiny character ID.
            destiny_membership_id: A valid Destiny membership ID.
            destiny_membership_type: A valid Destiny membership type.
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

        data = {
            "maxPlayerCount": max_player_count,
            "onlinePlayersOnly": online_players_only,
            "privacyScope": privacy_scope,
            "scheduledDateTime": scheduled_date_time,
            "clanId": clan_id,
            "listingValues": listing_values,
            "activityGraphHash": activity_graph_hash,
            "activityHash": activity_hash,
        }

        return await self.request(
            Route(
                path=f"/FireteamFinder/Lobby/Host/{destiny_membership_type}/{destiny_membership_id}/{destiny_character_id}/",
                method="POST",
                data=data,
                auth=auth,
            )
        )

    async def join_lobby(
        self,
        lobby_id: int,
        offer_id: int,
        destiny_character_id: int,
        destiny_membership_id: int,
        destiny_membership_type: int,
        auth: Optional[AuthData] = None,
        *args,
        **kwargs,
    ) -> dict:
        """
        Sends a request to join an available Fireteam lobby.

        Args:
            lobby_id: _No description given by bungie._
            offer_id: _No description given by bungie._
            destiny_character_id: A valid Destiny character ID.
            destiny_membership_id: A valid Destiny membership ID.
            destiny_membership_type: A valid Destiny membership type.
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

        data = {
            "lobbyId": lobby_id,
            "offerId": offer_id,
        }

        return await self.request(
            Route(
                path=f"/FireteamFinder/Lobby/Join/{destiny_membership_type}/{destiny_membership_id}/{destiny_character_id}/",
                method="POST",
                data=data,
                auth=auth,
            )
        )

    async def kick_player(
        self,
        target_membership_type: Union[Any, int],
        target_character_id: int,
        destiny_character_id: int,
        destiny_membership_id: int,
        destiny_membership_type: int,
        lobby_id: int,
        target_membership_id: int,
        auth: Optional[AuthData] = None,
        *args,
        **kwargs,
    ) -> dict:
        """
        Kicks a player from a Fireteam Finder lobby.

        Args:
            target_membership_type: _No description given by bungie._
            target_character_id: _No description given by bungie._
            destiny_character_id: A valid Destiny character ID.
            destiny_membership_id: A valid Destiny membership ID.
            destiny_membership_type: A valid Destiny membership type.
            lobby_id: The ID of the lobby to kick the player from.
            target_membership_id: A valid Destiny membership ID of the player to kick.
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

        data = {
            "targetMembershipType": target_membership_type,
            "targetCharacterId": target_character_id,
        }

        return await self.request(
            Route(
                path=f"/FireteamFinder/Lobby/{lobby_id}/KickPlayer/{target_membership_id}/{destiny_membership_type}/{destiny_membership_id}/{destiny_character_id}/",
                method="POST",
                data=data,
                auth=auth,
            )
        )

    async def leave_application(
        self,
        application_id: int,
        destiny_character_id: int,
        destiny_membership_id: int,
        destiny_membership_type: int,
        auth: Optional[AuthData] = None,
        *args,
        **kwargs,
    ) -> dict:
        """
        Sends a request to leave a Fireteam listing application.

        Args:
            application_id: The ID of the application to leave.
            destiny_character_id: A valid Destiny character ID.
            destiny_membership_id: A valid Destiny membership ID.
            destiny_membership_type: A valid Destiny membership type.
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
            Route(
                path=f"/FireteamFinder/Application/Leave/{application_id}/{destiny_membership_type}/{destiny_membership_id}/{destiny_character_id}/",
                method="POST",
                auth=auth,
            )
        )

    async def leave_lobby(
        self,
        destiny_character_id: int,
        destiny_membership_id: int,
        destiny_membership_type: int,
        lobby_id: int,
        auth: Optional[AuthData] = None,
        *args,
        **kwargs,
    ) -> dict:
        """
        Sends a request to leave a Fireteam lobby.

        Args:
            destiny_character_id: A valid Destiny character ID.
            destiny_membership_id: A valid Destiny membership ID.
            destiny_membership_type: A valid Destiny membership type.
            lobby_id: The ID of the lobby to leave.
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
            Route(
                path=f"/FireteamFinder/Lobby/Leave/{lobby_id}/{destiny_membership_type}/{destiny_membership_id}/{destiny_character_id}/",
                method="POST",
                auth=auth,
            )
        )

    async def respond_to_application(
        self,
        accepted: bool,
        application_id: int,
        destiny_character_id: int,
        destiny_membership_id: int,
        destiny_membership_type: int,
        auth: Optional[AuthData] = None,
        *args,
        **kwargs,
    ) -> dict:
        """
        Responds to an application sent to a Fireteam lobby.

        Args:
            accepted: _No description given by bungie._
            application_id: The application ID to respond to.
            destiny_character_id: A valid Destiny character ID.
            destiny_membership_id: A valid Destiny membership ID.
            destiny_membership_type: A valid Destiny membership type.
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

        data = {
            "accepted": accepted,
        }

        return await self.request(
            Route(
                path=f"/FireteamFinder/Application/Respond/{application_id}/{destiny_membership_type}/{destiny_membership_id}/{destiny_character_id}/",
                method="POST",
                data=data,
                auth=auth,
            )
        )

    async def respond_to_authentication(
        self,
        confirmed: bool,
        application_id: int,
        destiny_character_id: int,
        destiny_membership_id: int,
        destiny_membership_type: int,
        auth: Optional[AuthData] = None,
        *args,
        **kwargs,
    ) -> dict:
        """
        Responds to an authentication request for a Fireteam.

        Args:
            confirmed: _No description given by bungie._
            application_id: The ID of the application whose authentication to confirm.
            destiny_character_id: A valid Destiny character ID.
            destiny_membership_id: A valid Destiny membership ID.
            destiny_membership_type: A valid Destiny membership type.
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

        data = {
            "confirmed": confirmed,
        }

        return await self.request(
            Route(
                path=f"/FireteamFinder/Authentication/Respond/{application_id}/{destiny_membership_type}/{destiny_membership_id}/{destiny_character_id}/",
                method="POST",
                data=data,
                auth=auth,
            )
        )

    async def respond_to_offer(
        self,
        accepted: bool,
        destiny_character_id: int,
        destiny_membership_id: int,
        destiny_membership_type: int,
        offer_id: int,
        auth: Optional[AuthData] = None,
        *args,
        **kwargs,
    ) -> dict:
        """
        Responds to a Fireteam lobby offer.

        Args:
            accepted: _No description given by bungie._
            destiny_character_id: A valid Destiny character ID.
            destiny_membership_id: A valid Destiny membership ID.
            destiny_membership_type: A valid Destiny membership type.
            offer_id: The unique ID of the offer.
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

        data = {
            "accepted": accepted,
        }

        return await self.request(
            Route(
                path=f"/FireteamFinder/Offer/Respond/{offer_id}/{destiny_membership_type}/{destiny_membership_id}/{destiny_character_id}/",
                method="POST",
                data=data,
                auth=auth,
            )
        )

    async def search_listings_by_clan(
        self,
        page_size: int,
        page_token: str,
        lobby_state: Union[Any, int],
        destiny_character_id: int,
        destiny_membership_id: int,
        destiny_membership_type: int,
        auth: Optional[AuthData] = None,
        *args,
        **kwargs,
    ) -> dict:
        """
        Returns search results for available Fireteams provided a clan.

        Args:
            page_size: _No description given by bungie._
            page_token: _No description given by bungie._
            lobby_state: _No description given by bungie._
            destiny_character_id: A valid Destiny character ID.
            destiny_membership_id: A valid Destiny membership ID.
            destiny_membership_type: A valid Destiny membership type.
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

        data = {
            "pageSize": page_size,
            "pageToken": page_token,
            "lobbyState": lobby_state,
        }

        return await self.request(
            Route(
                path=f"/FireteamFinder/Search/Clan/{destiny_membership_type}/{destiny_membership_id}/{destiny_character_id}/",
                method="POST",
                data=data,
                auth=auth,
            )
        )

    async def search_listings_by_filters(
        self,
        filters: list[Any],
        page_size: int,
        page_token: str,
        lobby_state: Union[Any, int],
        destiny_character_id: int,
        destiny_membership_id: int,
        destiny_membership_type: int,
        auth: Optional[AuthData] = None,
        *args,
        **kwargs,
    ) -> dict:
        """
        Returns search results for available Fireteams provided search filters.

        Args:
            filters: _No description given by bungie._
            page_size: _No description given by bungie._
            page_token: _No description given by bungie._
            lobby_state: _No description given by bungie._
            destiny_character_id: A valid Destiny character ID.
            destiny_membership_id: A valid Destiny membership ID.
            destiny_membership_type: A valid Destiny membership type.
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

        data = {
            "filters": filters,
            "pageSize": page_size,
            "pageToken": page_token,
            "lobbyState": lobby_state,
        }

        return await self.request(
            Route(
                path=f"/FireteamFinder/Search/{destiny_membership_type}/{destiny_membership_id}/{destiny_character_id}/",
                method="POST",
                data=data,
                auth=auth,
            )
        )

    async def update_lobby_settings(
        self,
        updated_settings: Any,
        destiny_character_id: int,
        destiny_membership_id: int,
        destiny_membership_type: int,
        lobby_id: int,
        auth: Optional[AuthData] = None,
        *args,
        **kwargs,
    ) -> dict:
        """
        Updates the settings for a Fireteam lobby.

        Args:
            updated_settings: _No description given by bungie._
            destiny_character_id: A valid Destiny character ID.
            destiny_membership_id: A valid Destiny membership ID.
            destiny_membership_type: A valid Destiny membership type.
            lobby_id: The ID of the lobby to update.
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

        data = {
            "updatedSettings": updated_settings,
        }

        return await self.request(
            Route(
                path=f"/FireteamFinder/Lobby/UpdateSettings/{lobby_id}/{destiny_membership_type}/{destiny_membership_id}/{destiny_character_id}/",
                method="POST",
                data=data,
                auth=auth,
            )
        )
