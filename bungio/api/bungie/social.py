import datetime
from typing import Any, Optional

import attr

from bungio.models.auth import AuthData
from bungio.models.base import BaseModel
from bungio.models.bungie.social.friends import (
    BungieFriendListResponse,
    BungieFriendRequestListResponse,
    PlatformFriendResponse,
)


@attr.define
class SocialRouteInterface(BaseModel):
    async def get_friend_list(self, auth: AuthData) -> BungieFriendListResponse:
        """
        Returns your Bungie Friend list

        Warning: Requires Authentication.
            Required oauth2 scopes: ReadUserData

        Args:
            auth: Authentication information.

        Returns:
            The [model](/API Reference/Models/Bungie API Models/social.friends/#bungio.models.bungie.social.friends.BungieFriendListResponse) which is returned by bungie.
            Click [here](https://bungie-net.github.io/multi/index.html) for general endpoint information.
        """

        response = await self._client.http.get_friend_list(auth=auth)
        return BungieFriendListResponse.from_dict(data=response, client=self._client)

    async def get_friend_request_list(self, auth: AuthData) -> BungieFriendRequestListResponse:
        """
        Returns your friend request queue.

        Warning: Requires Authentication.
            Required oauth2 scopes: ReadUserData

        Args:
            auth: Authentication information.

        Returns:
            The [model](/API Reference/Models/Bungie API Models/social.friends/#bungio.models.bungie.social.friends.BungieFriendRequestListResponse) which is returned by bungie.
            Click [here](https://bungie-net.github.io/multi/index.html) for general endpoint information.
        """

        response = await self._client.http.get_friend_request_list(auth=auth)
        return BungieFriendRequestListResponse.from_dict(data=response, client=self._client)

    async def issue_friend_request(self, membership_id: str, auth: AuthData) -> bool:
        """
        Requests a friend relationship with the target user. Any of the target user's linked membership ids are valid inputs.

        Warning: Requires Authentication.
            Required oauth2 scopes: BnetWrite

        Args:
            membership_id: The membership id of the user you wish to add.
            auth: Authentication information.

        Returns:
            The [model](/API Reference/Models/Bungie API Models//#.bool) which is returned by bungie.
            Click [here](https://bungie-net.github.io/multi/index.html) for general endpoint information.
        """

        response = await self._client.http.issue_friend_request(membership_id=membership_id, auth=auth)
        return response["Result"]

    async def accept_friend_request(self, membership_id: str, auth: AuthData) -> bool:
        """
        Accepts a friend relationship with the target user. The user must be on your incoming friend request list, though no error will occur if they are not.

        Warning: Requires Authentication.
            Required oauth2 scopes: BnetWrite

        Args:
            membership_id: The membership id of the user you wish to accept.
            auth: Authentication information.

        Returns:
            The [model](/API Reference/Models/Bungie API Models//#.bool) which is returned by bungie.
            Click [here](https://bungie-net.github.io/multi/index.html) for general endpoint information.
        """

        response = await self._client.http.accept_friend_request(membership_id=membership_id, auth=auth)
        return response["Result"]

    async def decline_friend_request(self, membership_id: str, auth: AuthData) -> bool:
        """
        Declines a friend relationship with the target user. The user must be on your incoming friend request list, though no error will occur if they are not.

        Warning: Requires Authentication.
            Required oauth2 scopes: BnetWrite

        Args:
            membership_id: The membership id of the user you wish to decline.
            auth: Authentication information.

        Returns:
            The [model](/API Reference/Models/Bungie API Models//#.bool) which is returned by bungie.
            Click [here](https://bungie-net.github.io/multi/index.html) for general endpoint information.
        """

        response = await self._client.http.decline_friend_request(membership_id=membership_id, auth=auth)
        return response["Result"]

    async def remove_friend(self, membership_id: str, auth: AuthData) -> bool:
        """
        Remove a friend relationship with the target user. The user must be on your friend list, though no error will occur if they are not.

        Warning: Requires Authentication.
            Required oauth2 scopes: BnetWrite

        Args:
            membership_id: The membership id of the user you wish to remove.
            auth: Authentication information.

        Returns:
            The [model](/API Reference/Models/Bungie API Models//#.bool) which is returned by bungie.
            Click [here](https://bungie-net.github.io/multi/index.html) for general endpoint information.
        """

        response = await self._client.http.remove_friend(membership_id=membership_id, auth=auth)
        return response["Result"]

    async def remove_friend_request(self, membership_id: str, auth: AuthData) -> bool:
        """
        Remove a friend relationship with the target user. The user must be on your outgoing request friend list, though no error will occur if they are not.

        Warning: Requires Authentication.
            Required oauth2 scopes: BnetWrite

        Args:
            membership_id: The membership id of the user you wish to remove.
            auth: Authentication information.

        Returns:
            The [model](/API Reference/Models/Bungie API Models//#.bool) which is returned by bungie.
            Click [here](https://bungie-net.github.io/multi/index.html) for general endpoint information.
        """

        response = await self._client.http.remove_friend_request(membership_id=membership_id, auth=auth)
        return response["Result"]

    async def get_platform_friend_list(
        self, friend_platform: int, page: str, auth: Optional[AuthData] = None
    ) -> PlatformFriendResponse:
        """
        Gets the platform friend of the requested type, with additional information if they have Bungie accounts. Must have a recent login session with said platform.

        Args:
            friend_platform: The platform friend type.
            page: The zero based page to return. Page size is 100.
            auth: Authentication information. Required when users with a private profile are queried.

        Returns:
            The [model](/API Reference/Models/Bungie API Models/social.friends/#bungio.models.bungie.social.friends.PlatformFriendResponse) which is returned by bungie.
            Click [here](https://bungie-net.github.io/multi/index.html) for general endpoint information.
        """

        response = await self._client.http.get_platform_friend_list(
            friend_platform=friend_platform, page=page, auth=auth
        )
        return PlatformFriendResponse.from_dict(data=response, client=self._client)
