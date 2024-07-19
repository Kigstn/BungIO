# DO NOT CHANGE ANY CODE BELOW
# This file is generated automatically by `generate_api_schema.py` and will be overwritten
# Instead, change functions / models by subclassing them in the `./overwrites/` folder. They will be used instead.

from typing import Optional, Union

from bungio.models.base import ClientMixin, custom_define
from bungio.models.auth import AuthData

from bungio.models import BungieFriendRequestListResponse
from bungio.models import BungieFriendListResponse
from bungio.models import PlatformFriendType
from bungio.models import PlatformFriendResponse


@custom_define()
class SocialRouteInterface(ClientMixin):
    async def get_friend_list(self, auth: AuthData) -> BungieFriendListResponse:
        """
        Returns your Bungie Friend list

        Warning: Requires Authentication.
            Required oauth2 scopes: ReadUserData

        Args:
            auth: Authentication information.

        Returns:
            The model which is returned by bungie. [General endpoint information.](https://bungie-net.github.io/multi/index.html)
        """

        response = await self._client.http.get_friend_list(auth=auth)
        return await BungieFriendListResponse.from_dict(data=response, client=self._client, auth=auth)

    async def get_friend_request_list(self, auth: AuthData) -> BungieFriendRequestListResponse:
        """
        Returns your friend request queue.

        Warning: Requires Authentication.
            Required oauth2 scopes: ReadUserData

        Args:
            auth: Authentication information.

        Returns:
            The model which is returned by bungie. [General endpoint information.](https://bungie-net.github.io/multi/index.html)
        """

        response = await self._client.http.get_friend_request_list(auth=auth)
        return await BungieFriendRequestListResponse.from_dict(data=response, client=self._client, auth=auth)

    async def issue_friend_request(self, membership_id: str, auth: AuthData) -> bool:
        """
        Requests a friend relationship with the target user. Any of the target user's linked membership ids are valid inputs.

        Warning: Requires Authentication.
            Required oauth2 scopes: BnetWrite

        Args:
            membership_id: The membership id of the user you wish to add.
            auth: Authentication information.

        Returns:
            The model which is returned by bungie. [General endpoint information.](https://bungie-net.github.io/multi/index.html)
        """

        response = await self._client.http.issue_friend_request(membership_id=membership_id, auth=auth)
        return response["Response"]

    async def accept_friend_request(self, membership_id: str, auth: AuthData) -> bool:
        """
        Accepts a friend relationship with the target user. The user must be on your incoming friend request list, though no error will occur if they are not.

        Warning: Requires Authentication.
            Required oauth2 scopes: BnetWrite

        Args:
            membership_id: The membership id of the user you wish to accept.
            auth: Authentication information.

        Returns:
            The model which is returned by bungie. [General endpoint information.](https://bungie-net.github.io/multi/index.html)
        """

        response = await self._client.http.accept_friend_request(membership_id=membership_id, auth=auth)
        return response["Response"]

    async def decline_friend_request(self, membership_id: str, auth: AuthData) -> bool:
        """
        Declines a friend relationship with the target user. The user must be on your incoming friend request list, though no error will occur if they are not.

        Warning: Requires Authentication.
            Required oauth2 scopes: BnetWrite

        Args:
            membership_id: The membership id of the user you wish to decline.
            auth: Authentication information.

        Returns:
            The model which is returned by bungie. [General endpoint information.](https://bungie-net.github.io/multi/index.html)
        """

        response = await self._client.http.decline_friend_request(membership_id=membership_id, auth=auth)
        return response["Response"]

    async def remove_friend(self, membership_id: str, auth: AuthData) -> bool:
        """
        Remove a friend relationship with the target user. The user must be on your friend list, though no error will occur if they are not.

        Warning: Requires Authentication.
            Required oauth2 scopes: BnetWrite

        Args:
            membership_id: The membership id of the user you wish to remove.
            auth: Authentication information.

        Returns:
            The model which is returned by bungie. [General endpoint information.](https://bungie-net.github.io/multi/index.html)
        """

        response = await self._client.http.remove_friend(membership_id=membership_id, auth=auth)
        return response["Response"]

    async def remove_friend_request(self, membership_id: str, auth: AuthData) -> bool:
        """
        Remove a friend relationship with the target user. The user must be on your outgoing request friend list, though no error will occur if they are not.

        Warning: Requires Authentication.
            Required oauth2 scopes: BnetWrite

        Args:
            membership_id: The membership id of the user you wish to remove.
            auth: Authentication information.

        Returns:
            The model which is returned by bungie. [General endpoint information.](https://bungie-net.github.io/multi/index.html)
        """

        response = await self._client.http.remove_friend_request(membership_id=membership_id, auth=auth)
        return response["Response"]

    async def get_platform_friend_list(
        self, friend_platform: Union[PlatformFriendType, int], page: str, auth: Optional[AuthData] = None
    ) -> PlatformFriendResponse:
        """
        Gets the platform friend of the requested type, with additional information if they have Bungie accounts. Must have a recent login session with said platform.

        Args:
            friend_platform: The platform friend type.
            page: The zero based page to return. Page size is 100.
            auth: Authentication information. Required when users with a private profile are queried, or when Bungie feels like it

        Returns:
            The model which is returned by bungie. [General endpoint information.](https://bungie-net.github.io/multi/index.html)
        """

        response = await self._client.http.get_platform_friend_list(
            friend_platform=getattr(friend_platform, "value", friend_platform), page=page, auth=auth
        )
        return await PlatformFriendResponse.from_dict(
            data=response, client=self._client, friend_platform=friend_platform, page=page, auth=auth
        )
