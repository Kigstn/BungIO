import datetime
from typing import Callable, Coroutine, Optional

from bungio.http.route import Route
from bungio.models.auth import AuthData


class GroupV2Requests:
    request: Callable[..., Coroutine]

    async def get_available_avatars(self, auth: Optional[AuthData] = None) -> dict:
        """
        Returns a list of all available group avatars for the signed-in user.

        Args:
            auth: Authentication information. Required when users with a private profile are queried.

        Returns:
            The json response
        """

        return await self.request(Route(path=f"/GroupV2/GetAvailableAvatars/", method="GET", auth=auth))

    async def get_available_themes(self, auth: Optional[AuthData] = None) -> dict:
        """
        Returns a list of all available group themes.

        Args:
            auth: Authentication information. Required when users with a private profile are queried.

        Returns:
            The json response
        """

        return await self.request(Route(path=f"/GroupV2/GetAvailableThemes/", method="GET", auth=auth))

    async def get_user_clan_invite_setting(self, m_type: int, auth: AuthData) -> dict:
        """
        Gets the state of the user's clan invite preferences for a particular membership type - true if they wish to be invited to clans, false otherwise.

        Warning: Requires Authentication.
            Required oauth2 scopes: ReadUserData

        Args:
            m_type: The Destiny membership type of the account we wish to access settings.
            auth: Authentication information.

        Returns:
            The json response
        """

        return await self.request(Route(path=f"/GroupV2/GetUserClanInviteSetting/{m_type}/", method="GET", auth=auth))

    async def get_recommended_groups(self, create_date_range: int, group_type: int, auth: AuthData) -> dict:
        """
        Gets groups recommended for you based on the groups to whom those you follow belong.

        Warning: Requires Authentication.
            Required oauth2 scopes: ReadGroups

        Args:
            create_date_range: Requested range in which to pull recommended groups
            group_type: Type of groups requested
            auth: Authentication information.

        Returns:
            The json response
        """

        return await self.request(
            Route(path=f"/GroupV2/Recommended/{group_type}/{create_date_range}/", method="POST", auth=auth)
        )

    async def group_search(self, auth: Optional[AuthData] = None) -> dict:
        """
        Search for Groups.

        Args:
            auth: Authentication information. Required when users with a private profile are queried.

        Returns:
            The json response
        """

        return await self.request(Route(path=f"/GroupV2/Search/", method="POST", auth=auth))

    async def get_group(self, group_id: int, auth: Optional[AuthData] = None) -> dict:
        """
        Get information about a specific group of the given ID.

        Args:
            group_id: Requested group's id.
            auth: Authentication information. Required when users with a private profile are queried.

        Returns:
            The json response
        """

        return await self.request(Route(path=f"/GroupV2/{group_id}/", method="GET", auth=auth))

    async def get_group_by_name(self, group_name: str, group_type: int, auth: Optional[AuthData] = None) -> dict:
        """
        Get information about a specific group with the given name and type.

        Args:
            group_name: Exact name of the group to find.
            group_type: Type of group to find.
            auth: Authentication information. Required when users with a private profile are queried.

        Returns:
            The json response
        """

        return await self.request(Route(path=f"/GroupV2/Name/{group_name}/{group_type}/", method="GET", auth=auth))

    async def get_group_by_name_v2(self, auth: Optional[AuthData] = None) -> dict:
        """
        Get information about a specific group with the given name and type. The POST version.

        Args:
            auth: Authentication information. Required when users with a private profile are queried.

        Returns:
            The json response
        """

        return await self.request(Route(path=f"/GroupV2/NameV2/", method="POST", auth=auth))

    async def get_group_optional_conversations(self, group_id: int, auth: Optional[AuthData] = None) -> dict:
        """
        Gets a list of available optional conversation channels and their settings.

        Args:
            group_id: Requested group's id.
            auth: Authentication information. Required when users with a private profile are queried.

        Returns:
            The json response
        """

        return await self.request(Route(path=f"/GroupV2/{group_id}/OptionalConversations/", method="GET", auth=auth))

    async def edit_group(self, group_id: int, auth: AuthData) -> dict:
        """
        Edit an existing group. You must have suitable permissions in the group to perform this operation. This latest revision will only edit the fields you pass in - pass null for properties you want to leave unaltered.

        Warning: Requires Authentication.
            Required oauth2 scopes: AdminGroups

        Args:
            group_id: Group ID of the group to edit.
            auth: Authentication information.

        Returns:
            The json response
        """

        return await self.request(Route(path=f"/GroupV2/{group_id}/Edit/", method="POST", auth=auth))

    async def edit_clan_banner(self, group_id: int, auth: AuthData) -> dict:
        """
        Edit an existing group's clan banner. You must have suitable permissions in the group to perform this operation. All fields are required.

        Warning: Requires Authentication.
            Required oauth2 scopes: AdminGroups

        Args:
            group_id: Group ID of the group to edit.
            auth: Authentication information.

        Returns:
            The json response
        """

        return await self.request(Route(path=f"/GroupV2/{group_id}/EditClanBanner/", method="POST", auth=auth))

    async def edit_founder_options(self, group_id: int, auth: AuthData) -> dict:
        """
        Edit group options only available to a founder. You must have suitable permissions in the group to perform this operation.

        Warning: Requires Authentication.
            Required oauth2 scopes: AdminGroups

        Args:
            group_id: Group ID of the group to edit.
            auth: Authentication information.

        Returns:
            The json response
        """

        return await self.request(Route(path=f"/GroupV2/{group_id}/EditFounderOptions/", method="POST", auth=auth))

    async def add_optional_conversation(self, group_id: int, auth: AuthData) -> dict:
        """
        Add a new optional conversation/chat channel. Requires admin permissions to the group.

        Warning: Requires Authentication.
            Required oauth2 scopes: AdminGroups

        Args:
            group_id: Group ID of the group to edit.
            auth: Authentication information.

        Returns:
            The json response
        """

        return await self.request(
            Route(path=f"/GroupV2/{group_id}/OptionalConversations/Add/", method="POST", auth=auth)
        )

    async def edit_optional_conversation(self, conversation_id: int, group_id: int, auth: AuthData) -> dict:
        """
        Edit the settings of an optional conversation/chat channel. Requires admin permissions to the group.

        Warning: Requires Authentication.
            Required oauth2 scopes: AdminGroups

        Args:
            conversation_id: Conversation Id of the channel being edited.
            group_id: Group ID of the group to edit.
            auth: Authentication information.

        Returns:
            The json response
        """

        return await self.request(
            Route(path=f"/GroupV2/{group_id}/OptionalConversations/Edit/{conversation_id}/", method="POST", auth=auth)
        )

    async def get_members_of_group(
        self,
        currentpage: int,
        group_id: int,
        member_type: Optional[int] = None,
        name_search: Optional[str] = None,
        auth: Optional[AuthData] = None,
    ) -> dict:
        """
        Get the list of members in a given group.

        Args:
            currentpage: Page number (starting with 1). Each page has a fixed size of 50 items per page.
            group_id: The ID of the group.
            member_type: Filter out other member types. Use None for all members.
            name_search: The name fragment upon which a search should be executed for members with matching display or unique names.
            auth: Authentication information. Required when users with a private profile are queried.

        Returns:
            The json response
        """

        return await self.request(
            Route(
                path=f"/GroupV2/{group_id}/Members/",
                method="GET",
                member_type=member_type,
                name_search=name_search,
                auth=auth,
            )
        )

    async def get_admins_and_founder_of_group(
        self, currentpage: int, group_id: int, auth: Optional[AuthData] = None
    ) -> dict:
        """
        Get the list of members in a given group who are of admin level or higher.

        Args:
            currentpage: Page number (starting with 1). Each page has a fixed size of 50 items per page.
            group_id: The ID of the group.
            auth: Authentication information. Required when users with a private profile are queried.

        Returns:
            The json response
        """

        return await self.request(Route(path=f"/GroupV2/{group_id}/AdminsAndFounder/", method="GET", auth=auth))

    async def edit_group_membership(
        self, group_id: int, membership_id: int, membership_type: int, member_type: int, auth: AuthData
    ) -> dict:
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
            The json response
        """

        return await self.request(
            Route(
                path=f"/GroupV2/{group_id}/Members/{membership_type}/{membership_id}/SetMembershipType/{member_type}/",
                method="POST",
                auth=auth,
            )
        )

    async def kick_member(self, group_id: int, membership_id: int, membership_type: int, auth: AuthData) -> dict:
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
            The json response
        """

        return await self.request(
            Route(path=f"/GroupV2/{group_id}/Members/{membership_type}/{membership_id}/Kick/", method="POST", auth=auth)
        )

    async def ban_member(self, group_id: int, membership_id: int, membership_type: int, auth: AuthData) -> dict:
        """
        Bans the requested member from the requested group for the specified period of time.

        Warning: Requires Authentication.
            Required oauth2 scopes: AdminGroups

        Args:
            group_id: Group ID that has the member to ban.
            membership_id: Membership ID of the member to ban from the group.
            membership_type: Membership type of the provided membership ID.
            auth: Authentication information.

        Returns:
            The json response
        """

        return await self.request(
            Route(path=f"/GroupV2/{group_id}/Members/{membership_type}/{membership_id}/Ban/", method="POST", auth=auth)
        )

    async def unban_member(self, group_id: int, membership_id: int, membership_type: int, auth: AuthData) -> dict:
        """
        Unbans the requested member, allowing them to re-apply for membership.

        Warning: Requires Authentication.
            Required oauth2 scopes: AdminGroups

        Args:
            group_id: Not specified.
            membership_id: Membership ID of the member to unban from the group
            membership_type: Membership type of the provided membership ID.
            auth: Authentication information.

        Returns:
            The json response
        """

        return await self.request(
            Route(
                path=f"/GroupV2/{group_id}/Members/{membership_type}/{membership_id}/Unban/", method="POST", auth=auth
            )
        )

    async def get_banned_members_of_group(self, currentpage: int, group_id: int, auth: AuthData) -> dict:
        """
        Get the list of banned members in a given group. Only accessible to group Admins and above. Not applicable to all groups. Check group features.

        Warning: Requires Authentication.
            Required oauth2 scopes: AdminGroups

        Args:
            currentpage: Page number (starting with 1). Each page has a fixed size of 50 entries.
            group_id: Group ID whose banned members you are fetching
            auth: Authentication information.

        Returns:
            The json response
        """

        return await self.request(Route(path=f"/GroupV2/{group_id}/Banned/", method="GET", auth=auth))

    async def abdicate_foundership(
        self, founder_id_new: int, group_id: int, membership_type: int, auth: Optional[AuthData] = None
    ) -> dict:
        """
        An administrative method to allow the founder of a group or clan to give up their position to another admin permanently.

        Args:
            founder_id_new: The new founder for this group. Must already be a group admin.
            group_id: The target group id.
            membership_type: Membership type of the provided founderIdNew.
            auth: Authentication information. Required when users with a private profile are queried.

        Returns:
            The json response
        """

        return await self.request(
            Route(
                path=f"/GroupV2/{group_id}/Admin/AbdicateFoundership/{membership_type}/{founder_id_new}/",
                method="POST",
                auth=auth,
            )
        )

    async def get_pending_memberships(self, currentpage: int, group_id: int, auth: AuthData) -> dict:
        """
        Get the list of users who are awaiting a decision on their application to join a given group. Modified to include application info.

        Warning: Requires Authentication.
            Required oauth2 scopes: AdminGroups

        Args:
            currentpage: Page number (starting with 1). Each page has a fixed size of 50 items per page.
            group_id: ID of the group.
            auth: Authentication information.

        Returns:
            The json response
        """

        return await self.request(Route(path=f"/GroupV2/{group_id}/Members/Pending/", method="GET", auth=auth))

    async def get_invited_individuals(self, currentpage: int, group_id: int, auth: AuthData) -> dict:
        """
        Get the list of users who have been invited into the group.

        Warning: Requires Authentication.
            Required oauth2 scopes: AdminGroups

        Args:
            currentpage: Page number (starting with 1). Each page has a fixed size of 50 items per page.
            group_id: ID of the group.
            auth: Authentication information.

        Returns:
            The json response
        """

        return await self.request(
            Route(path=f"/GroupV2/{group_id}/Members/InvitedIndividuals/", method="GET", auth=auth)
        )

    async def approve_all_pending(self, group_id: int, auth: AuthData) -> dict:
        """
        Approve all of the pending users for the given group.

        Warning: Requires Authentication.
            Required oauth2 scopes: AdminGroups

        Args:
            group_id: ID of the group.
            auth: Authentication information.

        Returns:
            The json response
        """

        return await self.request(Route(path=f"/GroupV2/{group_id}/Members/ApproveAll/", method="POST", auth=auth))

    async def deny_all_pending(self, group_id: int, auth: AuthData) -> dict:
        """
        Deny all of the pending users for the given group.

        Warning: Requires Authentication.
            Required oauth2 scopes: AdminGroups

        Args:
            group_id: ID of the group.
            auth: Authentication information.

        Returns:
            The json response
        """

        return await self.request(Route(path=f"/GroupV2/{group_id}/Members/DenyAll/", method="POST", auth=auth))

    async def approve_pending_for_list(self, group_id: int, auth: AuthData) -> dict:
        """
        Approve all of the pending users for the given group.

        Warning: Requires Authentication.
            Required oauth2 scopes: AdminGroups

        Args:
            group_id: ID of the group.
            auth: Authentication information.

        Returns:
            The json response
        """

        return await self.request(Route(path=f"/GroupV2/{group_id}/Members/ApproveList/", method="POST", auth=auth))

    async def approve_pending(self, group_id: int, membership_id: int, membership_type: int, auth: AuthData) -> dict:
        """
        Approve the given membershipId to join the group/clan as long as they have applied.

        Warning: Requires Authentication.
            Required oauth2 scopes: AdminGroups

        Args:
            group_id: ID of the group.
            membership_id: The membership id being approved.
            membership_type: Membership type of the supplied membership ID.
            auth: Authentication information.

        Returns:
            The json response
        """

        return await self.request(
            Route(
                path=f"/GroupV2/{group_id}/Members/Approve/{membership_type}/{membership_id}/", method="POST", auth=auth
            )
        )

    async def deny_pending_for_list(self, group_id: int, auth: AuthData) -> dict:
        """
        Deny all of the pending users for the given group that match the passed-in .

        Warning: Requires Authentication.
            Required oauth2 scopes: AdminGroups

        Args:
            group_id: ID of the group.
            auth: Authentication information.

        Returns:
            The json response
        """

        return await self.request(Route(path=f"/GroupV2/{group_id}/Members/DenyList/", method="POST", auth=auth))

    async def get_groups_for_member(
        self, filter: int, group_type: int, membership_id: int, membership_type: int, auth: Optional[AuthData] = None
    ) -> dict:
        """
        Get information about the groups that a given member has joined.

        Args:
            filter: Filter apply to list of joined groups.
            group_type: Type of group the supplied member founded.
            membership_id: Membership ID to for which to find founded groups.
            membership_type: Membership type of the supplied membership ID.
            auth: Authentication information. Required when users with a private profile are queried.

        Returns:
            The json response
        """

        return await self.request(
            Route(
                path=f"/GroupV2/User/{membership_type}/{membership_id}/{filter}/{group_type}/", method="GET", auth=auth
            )
        )

    async def recover_group_for_founder(
        self, group_type: int, membership_id: int, membership_type: int, auth: Optional[AuthData] = None
    ) -> dict:
        """
        Allows a founder to manually recover a group they can see in game but not on bungie.net

        Args:
            group_type: Type of group the supplied member founded.
            membership_id: Membership ID to for which to find founded groups.
            membership_type: Membership type of the supplied membership ID.
            auth: Authentication information. Required when users with a private profile are queried.

        Returns:
            The json response
        """

        return await self.request(
            Route(path=f"/GroupV2/Recover/{membership_type}/{membership_id}/{group_type}/", method="GET", auth=auth)
        )

    async def get_potential_groups_for_member(
        self, filter: int, group_type: int, membership_id: int, membership_type: int, auth: Optional[AuthData] = None
    ) -> dict:
        """
        Get information about the groups that a given member has applied to or been invited to.

        Args:
            filter: Filter apply to list of potential joined groups.
            group_type: Type of group the supplied member applied.
            membership_id: Membership ID to for which to find applied groups.
            membership_type: Membership type of the supplied membership ID.
            auth: Authentication information. Required when users with a private profile are queried.

        Returns:
            The json response
        """

        return await self.request(
            Route(
                path=f"/GroupV2/User/Potential/{membership_type}/{membership_id}/{filter}/{group_type}/",
                method="GET",
                auth=auth,
            )
        )

    async def individual_group_invite(
        self, group_id: int, membership_id: int, membership_type: int, auth: AuthData
    ) -> dict:
        """
        Invite a user to join this group.

        Warning: Requires Authentication.
            Required oauth2 scopes: AdminGroups

        Args:
            group_id: ID of the group you would like to join.
            membership_id: Membership id of the account being invited.
            membership_type: MembershipType of the account being invited.
            auth: Authentication information.

        Returns:
            The json response
        """

        return await self.request(
            Route(
                path=f"/GroupV2/{group_id}/Members/IndividualInvite/{membership_type}/{membership_id}/",
                method="POST",
                auth=auth,
            )
        )

    async def individual_group_invite_cancel(
        self, group_id: int, membership_id: int, membership_type: int, auth: AuthData
    ) -> dict:
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
            The json response
        """

        return await self.request(
            Route(
                path=f"/GroupV2/{group_id}/Members/IndividualInviteCancel/{membership_type}/{membership_id}/",
                method="POST",
                auth=auth,
            )
        )
