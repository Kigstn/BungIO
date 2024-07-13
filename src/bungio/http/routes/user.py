from typing import Callable, Coroutine, Optional

from bungio.http.route import Route
from bungio.models.auth import AuthData


class UserRouteHttpRequests:
    request: Callable[..., Coroutine]

    async def get_bungie_net_user_by_id(self, id: int, auth: Optional[AuthData] = None, *args, **kwargs) -> dict:
        """
        Loads a bungienet user by membership id.

        Args:
            id: The requested Bungie.net membership id.
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

        return await self.request(Route(path=f"/User/GetBungieNetUserById/{id}/", method="GET", auth=auth))

    async def get_sanitized_platform_display_names(
        self, membership_id: int, auth: Optional[AuthData] = None, *args, **kwargs
    ) -> dict:
        """
        Gets a list of all display names linked to this membership id but sanitized (profanity filtered). Obeys all visibility rules of calling user and is heavily cached.

        Args:
            membership_id: The requested membership id to load.
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
            Route(path=f"/User/GetSanitizedPlatformDisplayNames/{membership_id}/", method="GET", auth=auth)
        )

    async def get_credential_types_for_target_account(
        self, membership_id: int, auth: Optional[AuthData] = None, *args, **kwargs
    ) -> dict:
        """
        Returns a list of credential types attached to the requested account

        Args:
            membership_id: The user's membership id
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
            Route(path=f"/User/GetCredentialTypesForTargetAccount/{membership_id}/", method="GET", auth=auth)
        )

    async def get_available_themes(self, auth: Optional[AuthData] = None, *args, **kwargs) -> dict:
        """
        Returns a list of all available user themes.

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

        return await self.request(Route(path="/User/GetAvailableThemes/", method="GET", auth=auth))

    async def get_membership_data_by_id(
        self, membership_id: int, membership_type: int, auth: Optional[AuthData] = None, *args, **kwargs
    ) -> dict:
        """
        Returns a list of accounts associated with the supplied membership ID and membership type. This will include all linked accounts (even when hidden) if supplied credentials permit it.

        Args:
            membership_id: The membership ID of the target user.
            membership_type: Type of the supplied membership ID.
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
            Route(path=f"/User/GetMembershipsById/{membership_id}/{membership_type}/", method="GET", auth=auth)
        )

    async def get_membership_data_for_current_user(self, auth: AuthData, *args, **kwargs) -> dict:
        """
        Returns a list of accounts associated with signed in user. This is useful for OAuth implementations that do not give you access to the token response.

        Warning: Requires Authentication.
            Required oauth2 scopes: ReadBasicUserProfile

        Args:
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

        return await self.request(Route(path="/User/GetMembershipsForCurrentUser/", method="GET", auth=auth))

    async def get_membership_from_hard_linked_credential(
        self, credential: str, cr_type: int, auth: Optional[AuthData] = None, *args, **kwargs
    ) -> dict:
        """
        Gets any hard linked membership given a credential. Only works for credentials that are public (just SteamID64 right now). Cross Save aware.

        Args:
            credential: The credential to look up. Must be a valid SteamID64.
            cr_type: The credential type. 'SteamId' is the only valid value at present.
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
            Route(path=f"/User/GetMembershipFromHardLinkedCredential/{cr_type}/{credential}/", method="GET", auth=auth)
        )

    async def search_by_global_name_prefix(
        self, display_name_prefix: str, page: int, auth: Optional[AuthData] = None, *args, **kwargs
    ) -> dict:
        """
        [OBSOLETE] Do not use this to search users, use SearchByGlobalNamePost instead.

        Args:
            display_name_prefix: The display name prefix you're looking for.
            page: The zero-based page of results you desire.
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
            Route(path=f"/User/Search/Prefix/{display_name_prefix}/{page}/", method="GET", auth=auth)
        )

    async def search_by_global_name_post(
        self, display_name_prefix: str, page: int, auth: Optional[AuthData] = None, *args, **kwargs
    ) -> dict:
        """
        Given the prefix of a global display name, returns all users who share that name.

        Args:
            display_name_prefix: _No description given by bungie._
            page: The zero-based page of results you desire.
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
            "displayNamePrefix": display_name_prefix,
        }

        return await self.request(Route(path=f"/User/Search/GlobalName/{page}/", method="POST", data=data, auth=auth))
