from typing import Callable, Coroutine, Optional

from bungio.http.route import Route
from bungio.models.auth import AuthData


class SocialRouteHttpRequests:
    request: Callable[..., Coroutine]

    async def get_friend_list(self, auth: AuthData, *args, **kwargs) -> dict:
        """
        Returns your Bungie Friend list

        Warning: Requires Authentication.
            Required oauth2 scopes: ReadUserData

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

        return await self.request(Route(path="/Social/Friends/", method="GET", auth=auth))

    async def get_friend_request_list(self, auth: AuthData, *args, **kwargs) -> dict:
        """
        Returns your friend request queue.

        Warning: Requires Authentication.
            Required oauth2 scopes: ReadUserData

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

        return await self.request(Route(path="/Social/Friends/Requests/", method="GET", auth=auth))

    async def issue_friend_request(self, membership_id: str, auth: AuthData, *args, **kwargs) -> dict:
        """
        Requests a friend relationship with the target user. Any of the target user's linked membership ids are valid inputs.

        Warning: Requires Authentication.
            Required oauth2 scopes: BnetWrite

        Args:
            membership_id: The membership id of the user you wish to add.
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

        return await self.request(Route(path=f"/Social/Friends/Add/{membership_id}/", method="POST", auth=auth))

    async def accept_friend_request(self, membership_id: str, auth: AuthData, *args, **kwargs) -> dict:
        """
        Accepts a friend relationship with the target user. The user must be on your incoming friend request list, though no error will occur if they are not.

        Warning: Requires Authentication.
            Required oauth2 scopes: BnetWrite

        Args:
            membership_id: The membership id of the user you wish to accept.
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
            Route(path=f"/Social/Friends/Requests/Accept/{membership_id}/", method="POST", auth=auth)
        )

    async def decline_friend_request(self, membership_id: str, auth: AuthData, *args, **kwargs) -> dict:
        """
        Declines a friend relationship with the target user. The user must be on your incoming friend request list, though no error will occur if they are not.

        Warning: Requires Authentication.
            Required oauth2 scopes: BnetWrite

        Args:
            membership_id: The membership id of the user you wish to decline.
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
            Route(path=f"/Social/Friends/Requests/Decline/{membership_id}/", method="POST", auth=auth)
        )

    async def remove_friend(self, membership_id: str, auth: AuthData, *args, **kwargs) -> dict:
        """
        Remove a friend relationship with the target user. The user must be on your friend list, though no error will occur if they are not.

        Warning: Requires Authentication.
            Required oauth2 scopes: BnetWrite

        Args:
            membership_id: The membership id of the user you wish to remove.
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

        return await self.request(Route(path=f"/Social/Friends/Remove/{membership_id}/", method="POST", auth=auth))

    async def remove_friend_request(self, membership_id: str, auth: AuthData, *args, **kwargs) -> dict:
        """
        Remove a friend relationship with the target user. The user must be on your outgoing request friend list, though no error will occur if they are not.

        Warning: Requires Authentication.
            Required oauth2 scopes: BnetWrite

        Args:
            membership_id: The membership id of the user you wish to remove.
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
            Route(path=f"/Social/Friends/Requests/Remove/{membership_id}/", method="POST", auth=auth)
        )

    async def get_platform_friend_list(
        self, friend_platform: int, page: str, auth: Optional[AuthData] = None, *args, **kwargs
    ) -> dict:
        """
        Gets the platform friend of the requested type, with additional information if they have Bungie accounts. Must have a recent login session with said platform.

        Args:
            friend_platform: The platform friend type.
            page: The zero based page to return. Page size is 100.
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
            Route(path=f"/Social/PlatformFriends/{friend_platform}/{page}/", method="GET", auth=auth)
        )
