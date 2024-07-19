# DO NOT CHANGE ANY CODE BELOW
# This file is generated automatically by `generate_api_schema.py` and will be overwritten
# Instead, change functions / models by subclassing them in the `./overwrites/` folder. They will be used instead.

from typing import Optional, Union

from bungio.models.base import ClientMixin, custom_define
from bungio.models.auth import AuthData
from bungio.utils import AllowAsyncIteration

from bungio.models import GroupApplicationListRequest
from bungio.models import SearchResultOfGroupMember
from bungio.models import GroupSearchResponse
from bungio.models import GroupBanRequest
from bungio.models import GroupApplicationResponse
from bungio.models import GroupType
from bungio.models import GroupOptionalConversation
from bungio.models import GroupMembershipSearchResponse
from bungio.models import GroupPotentialMembershipSearchResponse
from bungio.models import BungieMembershipType
from bungio.models import SearchResultOfGroupBan
from bungio.models import RuntimeGroupMemberType
from bungio.models import GroupOptionalConversationEditRequest
from bungio.models import GroupDateRange
from bungio.models import ClanBanner
from bungio.models import GroupOptionalConversationAddRequest
from bungio.models import GroupMemberLeaveResult
from bungio.models import GroupV2Card
from bungio.models import GroupResponse
from bungio.models import GroupQuery
from bungio.models import GroupEditAction
from bungio.models import GroupPotentialMemberStatus
from bungio.models import GroupApplicationRequest
from bungio.models import GroupOptionsEditAction
from bungio.models import SearchResultOfGroupMemberApplication
from bungio.models import GroupTheme
from bungio.models import GroupsForMemberFilter
from bungio.models import EntityActionResult
from bungio.models import GetGroupsForMemberResponse
from bungio.models import GroupNameSearchRequest
from bungio.models import SearchResultOfGroupEditHistory


@custom_define()
class GroupV2RouteInterface(ClientMixin):
    async def get_available_avatars(self, auth: Optional[AuthData] = None) -> dict[int, str]:
        """
        Returns a list of all available group avatars for the signed-in user.

        Args:
            auth: Authentication information. Required when users with a private profile are queried, or when Bungie feels like it

        Returns:
            The model which is returned by bungie. [General endpoint information.](https://bungie-net.github.io/multi/index.html)
        """

        response = await self._client.http.get_available_avatars(auth=auth)
        return {key: value async for key, value in AllowAsyncIteration(response["Response"].items())}

    async def get_available_themes(self, auth: Optional[AuthData] = None) -> list[GroupTheme]:
        """
        Returns a list of all available group themes.

        Args:
            auth: Authentication information. Required when users with a private profile are queried, or when Bungie feels like it

        Returns:
            The model which is returned by bungie. [General endpoint information.](https://bungie-net.github.io/multi/index.html)
        """

        response = await self._client.http.get_available_themes(auth=auth)
        return [
            await GroupTheme.from_dict(data=value, client=self._client, auth=auth) for value in response["Response"]
        ]

    async def get_user_clan_invite_setting(self, m_type: Union[BungieMembershipType, int], auth: AuthData) -> bool:
        """
        Gets the state of the user's clan invite preferences for a particular membership type - true if they wish to be invited to clans, false otherwise.

        Warning: Requires Authentication.
            Required oauth2 scopes: ReadUserData

        Args:
            m_type: The Destiny membership type of the account we wish to access settings.
            auth: Authentication information.

        Returns:
            The model which is returned by bungie. [General endpoint information.](https://bungie-net.github.io/multi/index.html)
        """

        response = await self._client.http.get_user_clan_invite_setting(
            m_type=getattr(m_type, "value", m_type), auth=auth
        )
        return response["Response"]

    async def get_recommended_groups(
        self, create_date_range: Union[GroupDateRange, int], group_type: Union[GroupType, int], auth: AuthData
    ) -> list[GroupV2Card]:
        """
        Gets groups recommended for you based on the groups to whom those you follow belong.

        Warning: Requires Authentication.
            Required oauth2 scopes: ReadGroups

        Args:
            create_date_range: Requested range in which to pull recommended groups
            group_type: Type of groups requested
            auth: Authentication information.

        Returns:
            The model which is returned by bungie. [General endpoint information.](https://bungie-net.github.io/multi/index.html)
        """

        response = await self._client.http.get_recommended_groups(
            create_date_range=getattr(create_date_range, "value", create_date_range),
            group_type=getattr(group_type, "value", group_type),
            auth=auth,
        )
        return [
            await GroupV2Card.from_dict(
                data=value, client=self._client, create_date_range=create_date_range, group_type=group_type, auth=auth
            )
            for value in response["Response"]
        ]

    async def group_search(self, data: GroupQuery, auth: Optional[AuthData] = None) -> GroupSearchResponse:
        """
        Search for Groups.

        Args:
            data: The required data for this request.
            auth: Authentication information. Required when users with a private profile are queried, or when Bungie feels like it

        Returns:
            The model which is returned by bungie. [General endpoint information.](https://bungie-net.github.io/multi/index.html)
        """

        response = await self._client.http.group_search(auth=auth, **data.to_dict(_return_to_bungie_case=False))
        return await GroupSearchResponse.from_dict(data=response, client=self._client, auth=auth)

    async def get_group(self, group_id: int, auth: Optional[AuthData] = None) -> GroupResponse:
        """
        Get information about a specific group of the given ID.

        Args:
            group_id: Requested group's id.
            auth: Authentication information. Required when users with a private profile are queried, or when Bungie feels like it

        Returns:
            The model which is returned by bungie. [General endpoint information.](https://bungie-net.github.io/multi/index.html)
        """

        response = await self._client.http.get_group(group_id=group_id, auth=auth)
        return await GroupResponse.from_dict(data=response, client=self._client, group_id=group_id, auth=auth)

    async def get_group_by_name(
        self, group_name: str, group_type: Union[GroupType, int], auth: Optional[AuthData] = None
    ) -> GroupResponse:
        """
        Get information about a specific group with the given name and type.

        Args:
            group_name: Exact name of the group to find.
            group_type: Type of group to find.
            auth: Authentication information. Required when users with a private profile are queried, or when Bungie feels like it

        Returns:
            The model which is returned by bungie. [General endpoint information.](https://bungie-net.github.io/multi/index.html)
        """

        response = await self._client.http.get_group_by_name(
            group_name=group_name, group_type=getattr(group_type, "value", group_type), auth=auth
        )
        return await GroupResponse.from_dict(
            data=response, client=self._client, group_name=group_name, group_type=group_type, auth=auth
        )

    async def get_group_by_name_v2(
        self, data: GroupNameSearchRequest, auth: Optional[AuthData] = None
    ) -> GroupResponse:
        """
        Get information about a specific group with the given name and type. The POST version.

        Args:
            data: The required data for this request.
            auth: Authentication information. Required when users with a private profile are queried, or when Bungie feels like it

        Returns:
            The model which is returned by bungie. [General endpoint information.](https://bungie-net.github.io/multi/index.html)
        """

        response = await self._client.http.get_group_by_name_v2(auth=auth, **data.to_dict(_return_to_bungie_case=False))
        return await GroupResponse.from_dict(data=response, client=self._client, auth=auth)

    async def get_group_optional_conversations(
        self, group_id: int, auth: Optional[AuthData] = None
    ) -> list[GroupOptionalConversation]:
        """
        Gets a list of available optional conversation channels and their settings.

        Args:
            group_id: Requested group's id.
            auth: Authentication information. Required when users with a private profile are queried, or when Bungie feels like it

        Returns:
            The model which is returned by bungie. [General endpoint information.](https://bungie-net.github.io/multi/index.html)
        """

        response = await self._client.http.get_group_optional_conversations(group_id=group_id, auth=auth)
        return [
            await GroupOptionalConversation.from_dict(data=value, client=self._client, group_id=group_id, auth=auth)
            for value in response["Response"]
        ]

    async def edit_group(self, data: GroupEditAction, group_id: int, auth: AuthData) -> int:
        """
        Edit an existing group. You must have suitable permissions in the group to perform this operation. This latest revision will only edit the fields you pass in - pass null for properties you want to leave unaltered.

        Warning: Requires Authentication.
            Required oauth2 scopes: AdminGroups

        Args:
            data: The required data for this request.
            group_id: Group ID of the group to edit.
            auth: Authentication information.

        Returns:
            The model which is returned by bungie. [General endpoint information.](https://bungie-net.github.io/multi/index.html)
        """

        response = await self._client.http.edit_group(
            group_id=group_id, auth=auth, **data.to_dict(_return_to_bungie_case=False)
        )
        return response["Response"]

    async def edit_clan_banner(self, data: ClanBanner, group_id: int, auth: AuthData) -> int:
        """
        Edit an existing group's clan banner. You must have suitable permissions in the group to perform this operation. All fields are required.

        Warning: Requires Authentication.
            Required oauth2 scopes: AdminGroups

        Args:
            data: The required data for this request.
            group_id: Group ID of the group to edit.
            auth: Authentication information.

        Returns:
            The model which is returned by bungie. [General endpoint information.](https://bungie-net.github.io/multi/index.html)
        """

        response = await self._client.http.edit_clan_banner(
            group_id=group_id, auth=auth, **data.to_dict(_return_to_bungie_case=False)
        )
        return response["Response"]

    async def edit_founder_options(self, data: GroupOptionsEditAction, group_id: int, auth: AuthData) -> int:
        """
        Edit group options only available to a founder. You must have suitable permissions in the group to perform this operation.

        Warning: Requires Authentication.
            Required oauth2 scopes: AdminGroups

        Args:
            data: The required data for this request.
            group_id: Group ID of the group to edit.
            auth: Authentication information.

        Returns:
            The model which is returned by bungie. [General endpoint information.](https://bungie-net.github.io/multi/index.html)
        """

        response = await self._client.http.edit_founder_options(
            group_id=group_id, auth=auth, **data.to_dict(_return_to_bungie_case=False)
        )
        return response["Response"]

    async def add_optional_conversation(
        self, data: GroupOptionalConversationAddRequest, group_id: int, auth: AuthData
    ) -> int:
        """
        Add a new optional conversation/chat channel. Requires admin permissions to the group.

        Warning: Requires Authentication.
            Required oauth2 scopes: AdminGroups

        Args:
            data: The required data for this request.
            group_id: Group ID of the group to edit.
            auth: Authentication information.

        Returns:
            The model which is returned by bungie. [General endpoint information.](https://bungie-net.github.io/multi/index.html)
        """

        response = await self._client.http.add_optional_conversation(
            group_id=group_id, auth=auth, **data.to_dict(_return_to_bungie_case=False)
        )
        return response["Response"]

    async def edit_optional_conversation(
        self, data: GroupOptionalConversationEditRequest, conversation_id: int, group_id: int, auth: AuthData
    ) -> int:
        """
        Edit the settings of an optional conversation/chat channel. Requires admin permissions to the group.

        Warning: Requires Authentication.
            Required oauth2 scopes: AdminGroups

        Args:
            data: The required data for this request.
            conversation_id: Conversation Id of the channel being edited.
            group_id: Group ID of the group to edit.
            auth: Authentication information.

        Returns:
            The model which is returned by bungie. [General endpoint information.](https://bungie-net.github.io/multi/index.html)
        """

        response = await self._client.http.edit_optional_conversation(
            conversation_id=conversation_id, group_id=group_id, auth=auth, **data.to_dict(_return_to_bungie_case=False)
        )
        return response["Response"]

    async def get_members_of_group(
        self,
        currentpage: int,
        group_id: int,
        member_type: Optional[Union[RuntimeGroupMemberType, int]] = None,
        name_search: Optional[str] = None,
        auth: Optional[AuthData] = None,
    ) -> SearchResultOfGroupMember:
        """
        Get the list of members in a given group.

        Args:
            currentpage: Page number (starting with 1). Each page has a fixed size of 50 items per page.
            group_id: The ID of the group.
            member_type: Filter out other member types. Use None for all members.
            name_search: The name fragment upon which a search should be executed for members with matching display or unique names.
            auth: Authentication information. Required when users with a private profile are queried, or when Bungie feels like it

        Returns:
            The model which is returned by bungie. [General endpoint information.](https://bungie-net.github.io/multi/index.html)
        """

        response = await self._client.http.get_members_of_group(
            currentpage=currentpage,
            group_id=group_id,
            member_type=getattr(member_type, "value", member_type) if member_type is not None else None,
            name_search=name_search if name_search is not None else None,
            auth=auth,
        )
        return await SearchResultOfGroupMember.from_dict(
            data=response,
            client=self._client,
            currentpage=currentpage,
            group_id=group_id,
            member_type=member_type,
            name_search=name_search,
            auth=auth,
        )

    async def get_admins_and_founder_of_group(
        self, currentpage: int, group_id: int, auth: Optional[AuthData] = None
    ) -> SearchResultOfGroupMember:
        """
        Get the list of members in a given group who are of admin level or higher.

        Args:
            currentpage: Page number (starting with 1). Each page has a fixed size of 50 items per page.
            group_id: The ID of the group.
            auth: Authentication information. Required when users with a private profile are queried, or when Bungie feels like it

        Returns:
            The model which is returned by bungie. [General endpoint information.](https://bungie-net.github.io/multi/index.html)
        """

        response = await self._client.http.get_admins_and_founder_of_group(
            currentpage=currentpage, group_id=group_id, auth=auth
        )
        return await SearchResultOfGroupMember.from_dict(
            data=response, client=self._client, currentpage=currentpage, group_id=group_id, auth=auth
        )

    async def edit_group_membership(
        self,
        group_id: int,
        membership_id: int,
        membership_type: Union[BungieMembershipType, int],
        member_type: Union[RuntimeGroupMemberType, int],
        auth: AuthData,
    ) -> int:
        """
        Edit the membership type of a given member. You must have suitable permissions in the group to perform this operation.

        Warning: Requires Authentication.
            Required oauth2 scopes: AdminGroups

        Args:
            group_id: ID of the group to which the member belongs.
            membership_id: Membership ID to modify.
            membership_type: Membership type of the provide membership ID.
            member_type: New membertype for the specified member.
            auth: Authentication information.

        Returns:
            The model which is returned by bungie. [General endpoint information.](https://bungie-net.github.io/multi/index.html)
        """

        response = await self._client.http.edit_group_membership(
            group_id=group_id,
            membership_id=membership_id,
            membership_type=getattr(membership_type, "value", membership_type),
            member_type=getattr(member_type, "value", member_type),
            auth=auth,
        )
        return response["Response"]

    async def kick_member(
        self, group_id: int, membership_id: int, membership_type: Union[BungieMembershipType, int], auth: AuthData
    ) -> GroupMemberLeaveResult:
        """
        Kick a member from the given group, forcing them to reapply if they wish to re-join the group. You must have suitable permissions in the group to perform this operation.

        Warning: Requires Authentication.
            Required oauth2 scopes: AdminGroups

        Args:
            group_id: Group ID to kick the user from.
            membership_id: Membership ID to kick.
            membership_type: Membership type of the provided membership ID.
            auth: Authentication information.

        Returns:
            The model which is returned by bungie. [General endpoint information.](https://bungie-net.github.io/multi/index.html)
        """

        response = await self._client.http.kick_member(
            group_id=group_id,
            membership_id=membership_id,
            membership_type=getattr(membership_type, "value", membership_type),
            auth=auth,
        )
        return await GroupMemberLeaveResult.from_dict(
            data=response,
            client=self._client,
            group_id=group_id,
            membership_id=membership_id,
            membership_type=membership_type,
            auth=auth,
        )

    async def ban_member(
        self,
        data: GroupBanRequest,
        group_id: int,
        membership_id: int,
        membership_type: Union[BungieMembershipType, int],
        auth: AuthData,
    ) -> int:
        """
        Bans the requested member from the requested group for the specified period of time.

        Warning: Requires Authentication.
            Required oauth2 scopes: AdminGroups

        Args:
            data: The required data for this request.
            group_id: Group ID that has the member to ban.
            membership_id: Membership ID of the member to ban from the group.
            membership_type: Membership type of the provided membership ID.
            auth: Authentication information.

        Returns:
            The model which is returned by bungie. [General endpoint information.](https://bungie-net.github.io/multi/index.html)
        """

        response = await self._client.http.ban_member(
            group_id=group_id,
            membership_id=membership_id,
            membership_type=getattr(membership_type, "value", membership_type),
            auth=auth,
            **data.to_dict(_return_to_bungie_case=False),
        )
        return response["Response"]

    async def unban_member(
        self, group_id: int, membership_id: int, membership_type: Union[BungieMembershipType, int], auth: AuthData
    ) -> int:
        """
        Unbans the requested member, allowing them to re-apply for membership.

        Warning: Requires Authentication.
            Required oauth2 scopes: AdminGroups

        Args:
            group_id:
            membership_id: Membership ID of the member to unban from the group
            membership_type: Membership type of the provided membership ID.
            auth: Authentication information.

        Returns:
            The model which is returned by bungie. [General endpoint information.](https://bungie-net.github.io/multi/index.html)
        """

        response = await self._client.http.unban_member(
            group_id=group_id,
            membership_id=membership_id,
            membership_type=getattr(membership_type, "value", membership_type),
            auth=auth,
        )
        return response["Response"]

    async def get_banned_members_of_group(
        self, currentpage: int, group_id: int, auth: AuthData
    ) -> SearchResultOfGroupBan:
        """
        Get the list of banned members in a given group. Only accessible to group Admins and above. Not applicable to all groups. Check group features.

        Warning: Requires Authentication.
            Required oauth2 scopes: AdminGroups

        Args:
            currentpage: Page number (starting with 1). Each page has a fixed size of 50 entries.
            group_id: Group ID whose banned members you are fetching
            auth: Authentication information.

        Returns:
            The model which is returned by bungie. [General endpoint information.](https://bungie-net.github.io/multi/index.html)
        """

        response = await self._client.http.get_banned_members_of_group(
            currentpage=currentpage, group_id=group_id, auth=auth
        )
        return await SearchResultOfGroupBan.from_dict(
            data=response, client=self._client, currentpage=currentpage, group_id=group_id, auth=auth
        )

    async def get_group_edit_history(
        self, currentpage: int, group_id: int, auth: AuthData
    ) -> SearchResultOfGroupEditHistory:
        """
        Get the list of edits made to a given group. Only accessible to group Admins and above.

        Warning: Requires Authentication.
            Required oauth2 scopes: AdminGroups

        Args:
            currentpage: Page number (starting with 1). Each page has a fixed size of 50 entries.
            group_id: Group ID whose edit history you are fetching
            auth: Authentication information.

        Returns:
            The model which is returned by bungie. [General endpoint information.](https://bungie-net.github.io/multi/index.html)
        """

        response = await self._client.http.get_group_edit_history(currentpage=currentpage, group_id=group_id, auth=auth)
        return await SearchResultOfGroupEditHistory.from_dict(
            data=response, client=self._client, currentpage=currentpage, group_id=group_id, auth=auth
        )

    async def abdicate_foundership(
        self,
        founder_id_new: int,
        group_id: int,
        membership_type: Union[BungieMembershipType, int],
        auth: Optional[AuthData] = None,
    ) -> bool:
        """
        An administrative method to allow the founder of a group or clan to give up their position to another admin permanently.

        Args:
            founder_id_new: The new founder for this group. Must already be a group admin.
            group_id: The target group id.
            membership_type: Membership type of the provided founderIdNew.
            auth: Authentication information. Required when users with a private profile are queried, or when Bungie feels like it

        Returns:
            The model which is returned by bungie. [General endpoint information.](https://bungie-net.github.io/multi/index.html)
        """

        response = await self._client.http.abdicate_foundership(
            founder_id_new=founder_id_new,
            group_id=group_id,
            membership_type=getattr(membership_type, "value", membership_type),
            auth=auth,
        )
        return response["Response"]

    async def get_pending_memberships(
        self, currentpage: int, group_id: int, auth: AuthData
    ) -> SearchResultOfGroupMemberApplication:
        """
        Get the list of users who are awaiting a decision on their application to join a given group. Modified to include application info.

        Warning: Requires Authentication.
            Required oauth2 scopes: AdminGroups

        Args:
            currentpage: Page number (starting with 1). Each page has a fixed size of 50 items per page.
            group_id: ID of the group.
            auth: Authentication information.

        Returns:
            The model which is returned by bungie. [General endpoint information.](https://bungie-net.github.io/multi/index.html)
        """

        response = await self._client.http.get_pending_memberships(
            currentpage=currentpage, group_id=group_id, auth=auth
        )
        return await SearchResultOfGroupMemberApplication.from_dict(
            data=response, client=self._client, currentpage=currentpage, group_id=group_id, auth=auth
        )

    async def get_invited_individuals(
        self, currentpage: int, group_id: int, auth: AuthData
    ) -> SearchResultOfGroupMemberApplication:
        """
        Get the list of users who have been invited into the group.

        Warning: Requires Authentication.
            Required oauth2 scopes: AdminGroups

        Args:
            currentpage: Page number (starting with 1). Each page has a fixed size of 50 items per page.
            group_id: ID of the group.
            auth: Authentication information.

        Returns:
            The model which is returned by bungie. [General endpoint information.](https://bungie-net.github.io/multi/index.html)
        """

        response = await self._client.http.get_invited_individuals(
            currentpage=currentpage, group_id=group_id, auth=auth
        )
        return await SearchResultOfGroupMemberApplication.from_dict(
            data=response, client=self._client, currentpage=currentpage, group_id=group_id, auth=auth
        )

    async def approve_all_pending(
        self, data: GroupApplicationRequest, group_id: int, auth: AuthData
    ) -> list[EntityActionResult]:
        """
        Approve all of the pending users for the given group.

        Warning: Requires Authentication.
            Required oauth2 scopes: AdminGroups

        Args:
            data: The required data for this request.
            group_id: ID of the group.
            auth: Authentication information.

        Returns:
            The model which is returned by bungie. [General endpoint information.](https://bungie-net.github.io/multi/index.html)
        """

        response = await self._client.http.approve_all_pending(
            group_id=group_id, auth=auth, **data.to_dict(_return_to_bungie_case=False)
        )
        return [
            await EntityActionResult.from_dict(data=value, client=self._client, group_id=group_id, auth=auth)
            for value in response["Response"]
        ]

    async def deny_all_pending(
        self, data: GroupApplicationRequest, group_id: int, auth: AuthData
    ) -> list[EntityActionResult]:
        """
        Deny all of the pending users for the given group.

        Warning: Requires Authentication.
            Required oauth2 scopes: AdminGroups

        Args:
            data: The required data for this request.
            group_id: ID of the group.
            auth: Authentication information.

        Returns:
            The model which is returned by bungie. [General endpoint information.](https://bungie-net.github.io/multi/index.html)
        """

        response = await self._client.http.deny_all_pending(
            group_id=group_id, auth=auth, **data.to_dict(_return_to_bungie_case=False)
        )
        return [
            await EntityActionResult.from_dict(data=value, client=self._client, group_id=group_id, auth=auth)
            for value in response["Response"]
        ]

    async def approve_pending_for_list(
        self, data: GroupApplicationListRequest, group_id: int, auth: AuthData
    ) -> list[EntityActionResult]:
        """
        Approve all of the pending users for the given group.

        Warning: Requires Authentication.
            Required oauth2 scopes: AdminGroups

        Args:
            data: The required data for this request.
            group_id: ID of the group.
            auth: Authentication information.

        Returns:
            The model which is returned by bungie. [General endpoint information.](https://bungie-net.github.io/multi/index.html)
        """

        response = await self._client.http.approve_pending_for_list(
            group_id=group_id, auth=auth, **data.to_dict(_return_to_bungie_case=False)
        )
        return [
            await EntityActionResult.from_dict(data=value, client=self._client, group_id=group_id, auth=auth)
            for value in response["Response"]
        ]

    async def approve_pending(
        self,
        data: GroupApplicationRequest,
        group_id: int,
        membership_id: int,
        membership_type: Union[BungieMembershipType, int],
        auth: AuthData,
    ) -> bool:
        """
        Approve the given membershipId to join the group/clan as long as they have applied.

        Warning: Requires Authentication.
            Required oauth2 scopes: AdminGroups

        Args:
            data: The required data for this request.
            group_id: ID of the group.
            membership_id: The membership id being approved.
            membership_type: Membership type of the supplied membership ID.
            auth: Authentication information.

        Returns:
            The model which is returned by bungie. [General endpoint information.](https://bungie-net.github.io/multi/index.html)
        """

        response = await self._client.http.approve_pending(
            group_id=group_id,
            membership_id=membership_id,
            membership_type=getattr(membership_type, "value", membership_type),
            auth=auth,
            **data.to_dict(_return_to_bungie_case=False),
        )
        return response["Response"]

    async def deny_pending_for_list(
        self, data: GroupApplicationListRequest, group_id: int, auth: AuthData
    ) -> list[EntityActionResult]:
        """
        Deny all of the pending users for the given group that match the passed-in .

        Warning: Requires Authentication.
            Required oauth2 scopes: AdminGroups

        Args:
            data: The required data for this request.
            group_id: ID of the group.
            auth: Authentication information.

        Returns:
            The model which is returned by bungie. [General endpoint information.](https://bungie-net.github.io/multi/index.html)
        """

        response = await self._client.http.deny_pending_for_list(
            group_id=group_id, auth=auth, **data.to_dict(_return_to_bungie_case=False)
        )
        return [
            await EntityActionResult.from_dict(data=value, client=self._client, group_id=group_id, auth=auth)
            for value in response["Response"]
        ]

    async def get_groups_for_member(
        self,
        filter: Union[GroupsForMemberFilter, int],
        group_type: Union[GroupType, int],
        membership_id: int,
        membership_type: Union[BungieMembershipType, int],
        auth: Optional[AuthData] = None,
    ) -> GetGroupsForMemberResponse:
        """
        Get information about the groups that a given member has joined.

        Args:
            filter: Filter apply to list of joined groups.
            group_type: Type of group the supplied member founded.
            membership_id: Membership ID to for which to find founded groups.
            membership_type: Membership type of the supplied membership ID.
            auth: Authentication information. Required when users with a private profile are queried, or when Bungie feels like it

        Returns:
            The model which is returned by bungie. [General endpoint information.](https://bungie-net.github.io/multi/index.html)
        """

        response = await self._client.http.get_groups_for_member(
            filter=getattr(filter, "value", filter),
            group_type=getattr(group_type, "value", group_type),
            membership_id=membership_id,
            membership_type=getattr(membership_type, "value", membership_type),
            auth=auth,
        )
        return await GetGroupsForMemberResponse.from_dict(
            data=response,
            client=self._client,
            filter=filter,
            group_type=group_type,
            membership_id=membership_id,
            membership_type=membership_type,
            auth=auth,
        )

    async def recover_group_for_founder(
        self,
        group_type: Union[GroupType, int],
        membership_id: int,
        membership_type: Union[BungieMembershipType, int],
        auth: Optional[AuthData] = None,
    ) -> GroupMembershipSearchResponse:
        """
        Allows a founder to manually recover a group they can see in game but not on bungie.net

        Args:
            group_type: Type of group the supplied member founded.
            membership_id: Membership ID to for which to find founded groups.
            membership_type: Membership type of the supplied membership ID.
            auth: Authentication information. Required when users with a private profile are queried, or when Bungie feels like it

        Returns:
            The model which is returned by bungie. [General endpoint information.](https://bungie-net.github.io/multi/index.html)
        """

        response = await self._client.http.recover_group_for_founder(
            group_type=getattr(group_type, "value", group_type),
            membership_id=membership_id,
            membership_type=getattr(membership_type, "value", membership_type),
            auth=auth,
        )
        return await GroupMembershipSearchResponse.from_dict(
            data=response,
            client=self._client,
            group_type=group_type,
            membership_id=membership_id,
            membership_type=membership_type,
            auth=auth,
        )

    async def get_potential_groups_for_member(
        self,
        filter: Union[GroupPotentialMemberStatus, int],
        group_type: Union[GroupType, int],
        membership_id: int,
        membership_type: Union[BungieMembershipType, int],
        auth: Optional[AuthData] = None,
    ) -> GroupPotentialMembershipSearchResponse:
        """
        Get information about the groups that a given member has applied to or been invited to.

        Args:
            filter: Filter apply to list of potential joined groups.
            group_type: Type of group the supplied member applied.
            membership_id: Membership ID to for which to find applied groups.
            membership_type: Membership type of the supplied membership ID.
            auth: Authentication information. Required when users with a private profile are queried, or when Bungie feels like it

        Returns:
            The model which is returned by bungie. [General endpoint information.](https://bungie-net.github.io/multi/index.html)
        """

        response = await self._client.http.get_potential_groups_for_member(
            filter=getattr(filter, "value", filter),
            group_type=getattr(group_type, "value", group_type),
            membership_id=membership_id,
            membership_type=getattr(membership_type, "value", membership_type),
            auth=auth,
        )
        return await GroupPotentialMembershipSearchResponse.from_dict(
            data=response,
            client=self._client,
            filter=filter,
            group_type=group_type,
            membership_id=membership_id,
            membership_type=membership_type,
            auth=auth,
        )

    async def individual_group_invite(
        self,
        data: GroupApplicationRequest,
        group_id: int,
        membership_id: int,
        membership_type: Union[BungieMembershipType, int],
        auth: AuthData,
    ) -> GroupApplicationResponse:
        """
        Invite a user to join this group.

        Warning: Requires Authentication.
            Required oauth2 scopes: AdminGroups

        Args:
            data: The required data for this request.
            group_id: ID of the group you would like to join.
            membership_id: Membership id of the account being invited.
            membership_type: MembershipType of the account being invited.
            auth: Authentication information.

        Returns:
            The model which is returned by bungie. [General endpoint information.](https://bungie-net.github.io/multi/index.html)
        """

        response = await self._client.http.individual_group_invite(
            group_id=group_id,
            membership_id=membership_id,
            membership_type=getattr(membership_type, "value", membership_type),
            auth=auth,
            **data.to_dict(_return_to_bungie_case=False),
        )
        return await GroupApplicationResponse.from_dict(
            data=response,
            client=self._client,
            group_id=group_id,
            membership_id=membership_id,
            membership_type=membership_type,
            auth=auth,
        )

    async def individual_group_invite_cancel(
        self, group_id: int, membership_id: int, membership_type: Union[BungieMembershipType, int], auth: AuthData
    ) -> GroupApplicationResponse:
        """
        Cancels a pending invitation to join a group.

        Warning: Requires Authentication.
            Required oauth2 scopes: AdminGroups

        Args:
            group_id: ID of the group you would like to join.
            membership_id: Membership id of the account being cancelled.
            membership_type: MembershipType of the account being cancelled.
            auth: Authentication information.

        Returns:
            The model which is returned by bungie. [General endpoint information.](https://bungie-net.github.io/multi/index.html)
        """

        response = await self._client.http.individual_group_invite_cancel(
            group_id=group_id,
            membership_id=membership_id,
            membership_type=getattr(membership_type, "value", membership_type),
            auth=auth,
        )
        return await GroupApplicationResponse.from_dict(
            data=response,
            client=self._client,
            group_id=group_id,
            membership_id=membership_id,
            membership_type=membership_type,
            auth=auth,
        )
