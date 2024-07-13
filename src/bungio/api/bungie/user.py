# DO NOT CHANGE ANY CODE BELOW
# This file is generated automatically by `generate_api_schema.py` and will be overwritten
# Instead, change functions / models by subclassing them in the `./overwrites/` folder. They will be used instead.

from typing import Optional, Union

from bungio.models import (
    BungieCredentialType,
    BungieMembershipType,
    GeneralUser,
    GetCredentialTypesForAccountResponse,
    HardLinkedUserMembership,
    UserMembershipData,
    UserSearchPrefixRequest,
    UserSearchResponse,
    UserTheme,
)
from bungio.models.auth import AuthData
from bungio.models.base import ClientMixin, custom_define
from bungio.utils import AllowAsyncIteration


@custom_define()
class UserRouteInterface(ClientMixin):
    async def get_bungie_net_user_by_id(self, id: int, auth: Optional[AuthData] = None) -> GeneralUser:
        """
        Loads a bungienet user by membership id.

        Args:
            id: The requested Bungie.net membership id.
            auth: Authentication information. Required when users with a private profile are queried, or when Bungie feels like it

        Returns:
            The model which is returned by bungie. [General endpoint information.](https://bungie-net.github.io/multi/index.html)
        """

        response = await self._client.http.get_bungie_net_user_by_id(id=id, auth=auth)
        return await GeneralUser.from_dict(data=response, client=self._client, id=id, auth=auth)

    async def get_sanitized_platform_display_names(
        self, membership_id: int, auth: Optional[AuthData] = None
    ) -> dict[BungieCredentialType, str]:
        """
        Gets a list of all display names linked to this membership id but sanitized (profanity filtered). Obeys all visibility rules of calling user and is heavily cached.

        Args:
            membership_id: The requested membership id to load.
            auth: Authentication information. Required when users with a private profile are queried, or when Bungie feels like it

        Returns:
            The model which is returned by bungie. [General endpoint information.](https://bungie-net.github.io/multi/index.html)
        """

        response = await self._client.http.get_sanitized_platform_display_names(membership_id=membership_id, auth=auth)
        return {key: value async for key, value in AllowAsyncIteration(response["Response"].items())}

    async def get_credential_types_for_target_account(
        self, membership_id: int, auth: Optional[AuthData] = None
    ) -> list[GetCredentialTypesForAccountResponse]:
        """
        Returns a list of credential types attached to the requested account

        Args:
            membership_id: The user's membership id
            auth: Authentication information. Required when users with a private profile are queried, or when Bungie feels like it

        Returns:
            The model which is returned by bungie. [General endpoint information.](https://bungie-net.github.io/multi/index.html)
        """

        response = await self._client.http.get_credential_types_for_target_account(
            membership_id=membership_id, auth=auth
        )
        return [
            await GetCredentialTypesForAccountResponse.from_dict(
                data=value, client=self._client, membership_id=membership_id, auth=auth
            )
            for value in response["Response"]
        ]

    async def get_available_themes(self, auth: Optional[AuthData] = None) -> list[UserTheme]:
        """
        Returns a list of all available user themes.

        Args:
            auth: Authentication information. Required when users with a private profile are queried, or when Bungie feels like it

        Returns:
            The model which is returned by bungie. [General endpoint information.](https://bungie-net.github.io/multi/index.html)
        """

        response = await self._client.http.get_available_themes(auth=auth)
        return [await UserTheme.from_dict(data=value, client=self._client, auth=auth) for value in response["Response"]]

    async def get_membership_data_by_id(
        self, membership_id: int, membership_type: Union[BungieMembershipType, int], auth: Optional[AuthData] = None
    ) -> UserMembershipData:
        """
        Returns a list of accounts associated with the supplied membership ID and membership type. This will include all linked accounts (even when hidden) if supplied credentials permit it.

        Args:
            membership_id: The membership ID of the target user.
            membership_type: Type of the supplied membership ID.
            auth: Authentication information. Required when users with a private profile are queried, or when Bungie feels like it

        Returns:
            The model which is returned by bungie. [General endpoint information.](https://bungie-net.github.io/multi/index.html)
        """

        response = await self._client.http.get_membership_data_by_id(
            membership_id=membership_id, membership_type=getattr(membership_type, "value", membership_type), auth=auth
        )
        return await UserMembershipData.from_dict(
            data=response, client=self._client, membership_id=membership_id, membership_type=membership_type, auth=auth
        )

    async def get_membership_data_for_current_user(self, auth: AuthData) -> UserMembershipData:
        """
        Returns a list of accounts associated with signed in user. This is useful for OAuth implementations that do not give you access to the token response.

        Warning: Requires Authentication.
            Required oauth2 scopes: ReadBasicUserProfile

        Args:
            auth: Authentication information.

        Returns:
            The model which is returned by bungie. [General endpoint information.](https://bungie-net.github.io/multi/index.html)
        """

        response = await self._client.http.get_membership_data_for_current_user(auth=auth)
        return await UserMembershipData.from_dict(data=response, client=self._client, auth=auth)

    async def get_membership_from_hard_linked_credential(
        self, credential: str, cr_type: Union[BungieCredentialType, int], auth: Optional[AuthData] = None
    ) -> HardLinkedUserMembership:
        """
        Gets any hard linked membership given a credential. Only works for credentials that are public (just SteamID64 right now). Cross Save aware.

        Args:
            credential: The credential to look up. Must be a valid SteamID64.
            cr_type: The credential type. 'SteamId' is the only valid value at present.
            auth: Authentication information. Required when users with a private profile are queried, or when Bungie feels like it

        Returns:
            The model which is returned by bungie. [General endpoint information.](https://bungie-net.github.io/multi/index.html)
        """

        response = await self._client.http.get_membership_from_hard_linked_credential(
            credential=credential, cr_type=getattr(cr_type, "value", cr_type), auth=auth
        )
        return await HardLinkedUserMembership.from_dict(
            data=response, client=self._client, credential=credential, cr_type=cr_type, auth=auth
        )

    async def search_by_global_name_prefix(
        self, display_name_prefix: str, page: int, auth: Optional[AuthData] = None
    ) -> UserSearchResponse:
        """
        [OBSOLETE] Do not use this to search users, use SearchByGlobalNamePost instead.

        Args:
            display_name_prefix: The display name prefix you're looking for.
            page: The zero-based page of results you desire.
            auth: Authentication information. Required when users with a private profile are queried, or when Bungie feels like it

        Returns:
            The model which is returned by bungie. [General endpoint information.](https://bungie-net.github.io/multi/index.html)
        """

        response = await self._client.http.search_by_global_name_prefix(
            display_name_prefix=display_name_prefix, page=page, auth=auth
        )
        return await UserSearchResponse.from_dict(
            data=response, client=self._client, display_name_prefix=display_name_prefix, page=page, auth=auth
        )

    async def search_by_global_name_post(
        self, data: UserSearchPrefixRequest, page: int, auth: Optional[AuthData] = None
    ) -> UserSearchResponse:
        """
        Given the prefix of a global display name, returns all users who share that name.

        Args:
            data: The required data for this request.
            page: The zero-based page of results you desire.
            auth: Authentication information. Required when users with a private profile are queried, or when Bungie feels like it

        Returns:
            The model which is returned by bungie. [General endpoint information.](https://bungie-net.github.io/multi/index.html)
        """

        response = await self._client.http.search_by_global_name_post(
            page=page, auth=auth, **data.to_dict(_return_to_bungie_case=False)
        )
        return await UserSearchResponse.from_dict(data=response, client=self._client, page=page, auth=auth)
