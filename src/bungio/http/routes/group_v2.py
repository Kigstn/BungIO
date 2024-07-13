from typing import Callable, Coroutine, Optional, Any, Union

from bungio.http.route import Route
from bungio.models.auth import AuthData


class GroupV2RouteHttpRequests:
    request: Callable[..., Coroutine]

    async def get_available_avatars(self, auth: Optional[AuthData] = None, *args, **kwargs) -> dict:
        """
        Returns a list of all available group avatars for the signed-in user.

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

        return await self.request(Route(path="/GroupV2/GetAvailableAvatars/", method="GET", auth=auth))

    async def get_available_themes(self, auth: Optional[AuthData] = None, *args, **kwargs) -> dict:
        """
        Returns a list of all available group themes.

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

        return await self.request(Route(path="/GroupV2/GetAvailableThemes/", method="GET", auth=auth))

    async def get_user_clan_invite_setting(self, m_type: int, auth: AuthData, *args, **kwargs) -> dict:
        """
        Gets the state of the user's clan invite preferences for a particular membership type - true if they wish to be invited to clans, false otherwise.

        Warning: Requires Authentication.
            Required oauth2 scopes: ReadUserData

        Args:
            m_type: The Destiny membership type of the account we wish to access settings.
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

        return await self.request(Route(path=f"/GroupV2/GetUserClanInviteSetting/{m_type}/", method="GET", auth=auth))

    async def get_recommended_groups(
        self, create_date_range: int, group_type: int, auth: AuthData, *args, **kwargs
    ) -> dict:
        """
        Gets groups recommended for you based on the groups to whom those you follow belong.

        Warning: Requires Authentication.
            Required oauth2 scopes: ReadGroups

        Args:
            create_date_range: Requested range in which to pull recommended groups
            group_type: Type of groups requested
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
            Route(path=f"/GroupV2/Recommended/{group_type}/{create_date_range}/", method="POST", auth=auth)
        )

    async def group_search(
        self,
        name: str,
        group_type: Union[Any, int],
        creation_date: Union[Any, int],
        sort_by: Union[Any, int],
        group_member_count_filter: int,
        locale_filter: str,
        tag_text: str,
        items_per_page: int,
        current_page: int,
        request_continuation_token: str,
        auth: Optional[AuthData] = None,
        *args,
        **kwargs,
    ) -> dict:
        """
        Search for Groups.

        Args:
            name: _No description given by bungie._
            group_type: _No description given by bungie._
            creation_date: _No description given by bungie._
            sort_by: _No description given by bungie._
            group_member_count_filter: _No description given by bungie._
            locale_filter: _No description given by bungie._
            tag_text: _No description given by bungie._
            items_per_page: _No description given by bungie._
            current_page: _No description given by bungie._
            request_continuation_token: _No description given by bungie._
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
            "name": name,
            "groupType": group_type,
            "creationDate": creation_date,
            "sortBy": sort_by,
            "groupMemberCountFilter": group_member_count_filter,
            "localeFilter": locale_filter,
            "tagText": tag_text,
            "itemsPerPage": items_per_page,
            "currentPage": current_page,
            "requestContinuationToken": request_continuation_token,
        }

        return await self.request(Route(path="/GroupV2/Search/", method="POST", data=data, auth=auth))

    async def get_group(self, group_id: int, auth: Optional[AuthData] = None, *args, **kwargs) -> dict:
        """
        Get information about a specific group of the given ID.

        Args:
            group_id: Requested group's id.
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

        return await self.request(Route(path=f"/GroupV2/{group_id}/", method="GET", auth=auth))

    async def get_group_by_name(
        self, group_name: str, group_type: int, auth: Optional[AuthData] = None, *args, **kwargs
    ) -> dict:
        """
        Get information about a specific group with the given name and type.

        Args:
            group_name: Exact name of the group to find.
            group_type: Type of group to find.
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

        return await self.request(Route(path=f"/GroupV2/Name/{group_name}/{group_type}/", method="GET", auth=auth))

    async def get_group_by_name_v2(
        self, group_name: str, group_type: Union[Any, int], auth: Optional[AuthData] = None, *args, **kwargs
    ) -> dict:
        """
        Get information about a specific group with the given name and type. The POST version.

        Args:
            group_name: _No description given by bungie._
            group_type: _No description given by bungie._
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
            "groupName": group_name,
            "groupType": group_type,
        }

        return await self.request(Route(path="/GroupV2/NameV2/", method="POST", data=data, auth=auth))

    async def get_group_optional_conversations(
        self, group_id: int, auth: Optional[AuthData] = None, *args, **kwargs
    ) -> dict:
        """
        Gets a list of available optional conversation channels and their settings.

        Args:
            group_id: Requested group's id.
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

        return await self.request(Route(path=f"/GroupV2/{group_id}/OptionalConversations/", method="GET", auth=auth))

    async def edit_group(
        self,
        name: str,
        about: str,
        motto: str,
        theme: str,
        avatar_image_index: int,
        tags: str,
        is_public: bool,
        membership_option: int,
        is_public_topic_admin_only: bool,
        allow_chat: bool,
        chat_security: int,
        callsign: str,
        locale: str,
        homepage: int,
        enable_invitation_messaging_for_admins: bool,
        default_publicity: int,
        group_id: int,
        auth: AuthData,
        *args,
        **kwargs,
    ) -> dict:
        """
        Edit an existing group. You must have suitable permissions in the group to perform this operation. This latest revision will only edit the fields you pass in - pass null for properties you want to leave unaltered.

        Warning: Requires Authentication.
            Required oauth2 scopes: AdminGroups

        Args:
            name: _No description given by bungie._
            about: _No description given by bungie._
            motto: _No description given by bungie._
            theme: _No description given by bungie._
            avatar_image_index: _No description given by bungie._
            tags: _No description given by bungie._
            is_public: _No description given by bungie._
            membership_option: _No description given by bungie._
            is_public_topic_admin_only: _No description given by bungie._
            allow_chat: _No description given by bungie._
            chat_security: _No description given by bungie._
            callsign: _No description given by bungie._
            locale: _No description given by bungie._
            homepage: _No description given by bungie._
            enable_invitation_messaging_for_admins: _No description given by bungie._
            default_publicity: _No description given by bungie._
            group_id: Group ID of the group to edit.
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

        data = {
            "name": name,
            "about": about,
            "motto": motto,
            "theme": theme,
            "avatarImageIndex": avatar_image_index,
            "tags": tags,
            "isPublic": is_public,
            "membershipOption": membership_option,
            "isPublicTopicAdminOnly": is_public_topic_admin_only,
            "allowChat": allow_chat,
            "chatSecurity": chat_security,
            "callsign": callsign,
            "locale": locale,
            "homepage": homepage,
            "enableInvitationMessagingForAdmins": enable_invitation_messaging_for_admins,
            "defaultPublicity": default_publicity,
        }

        return await self.request(Route(path=f"/GroupV2/{group_id}/Edit/", method="POST", data=data, auth=auth))

    async def edit_clan_banner(
        self,
        decal_id: int,
        decal_color_id: int,
        decal_background_color_id: int,
        gonfalon_id: int,
        gonfalon_color_id: int,
        gonfalon_detail_id: int,
        gonfalon_detail_color_id: int,
        group_id: int,
        auth: AuthData,
        *args,
        **kwargs,
    ) -> dict:
        """
        Edit an existing group's clan banner. You must have suitable permissions in the group to perform this operation. All fields are required.

        Warning: Requires Authentication.
            Required oauth2 scopes: AdminGroups

        Args:
            decal_id: _No description given by bungie._
            decal_color_id: _No description given by bungie._
            decal_background_color_id: _No description given by bungie._
            gonfalon_id: _No description given by bungie._
            gonfalon_color_id: _No description given by bungie._
            gonfalon_detail_id: _No description given by bungie._
            gonfalon_detail_color_id: _No description given by bungie._
            group_id: Group ID of the group to edit.
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

        data = {
            "decalId": decal_id,
            "decalColorId": decal_color_id,
            "decalBackgroundColorId": decal_background_color_id,
            "gonfalonId": gonfalon_id,
            "gonfalonColorId": gonfalon_color_id,
            "gonfalonDetailId": gonfalon_detail_id,
            "gonfalonDetailColorId": gonfalon_detail_color_id,
        }

        return await self.request(
            Route(path=f"/GroupV2/{group_id}/EditClanBanner/", method="POST", data=data, auth=auth)
        )

    async def edit_founder_options(
        self,
        invite_permission_override: bool,
        update_culture_permission_override: bool,
        host_guided_game_permission_override: int,
        update_banner_permission_override: bool,
        join_level: int,
        group_id: int,
        auth: AuthData,
        *args,
        **kwargs,
    ) -> dict:
        """
        Edit group options only available to a founder. You must have suitable permissions in the group to perform this operation.

        Warning: Requires Authentication.
            Required oauth2 scopes: AdminGroups

        Args:
            invite_permission_override: Minimum Member Level allowed to invite new members to group Always Allowed: Founder, Acting Founder True means admins have this power, false means they don't Default is false for clans, true for groups.
            update_culture_permission_override: Minimum Member Level allowed to update group culture Always Allowed: Founder, Acting Founder True means admins have this power, false means they don't Default is false for clans, true for groups.
            host_guided_game_permission_override: Minimum Member Level allowed to host guided games Always Allowed: Founder, Acting Founder, Admin Allowed Overrides: None, Member, Beginner Default is Member for clans, None for groups, although this means nothing for groups.
            update_banner_permission_override: Minimum Member Level allowed to update banner Always Allowed: Founder, Acting Founder True means admins have this power, false means they don't Default is false for clans, true for groups.
            join_level: Level to join a member at when accepting an invite, application, or joining an open clan Default is Beginner.
            group_id: Group ID of the group to edit.
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

        data = {
            "InvitePermissionOverride": invite_permission_override,
            "UpdateCulturePermissionOverride": update_culture_permission_override,
            "HostGuidedGamePermissionOverride": host_guided_game_permission_override,
            "UpdateBannerPermissionOverride": update_banner_permission_override,
            "JoinLevel": join_level,
        }

        return await self.request(
            Route(path=f"/GroupV2/{group_id}/EditFounderOptions/", method="POST", data=data, auth=auth)
        )

    async def add_optional_conversation(
        self, chat_name: str, chat_security: Union[Any, int], group_id: int, auth: AuthData, *args, **kwargs
    ) -> dict:
        """
        Add a new optional conversation/chat channel. Requires admin permissions to the group.

        Warning: Requires Authentication.
            Required oauth2 scopes: AdminGroups

        Args:
            chat_name: _No description given by bungie._
            chat_security: _No description given by bungie._
            group_id: Group ID of the group to edit.
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

        data = {
            "chatName": chat_name,
            "chatSecurity": chat_security,
        }

        return await self.request(
            Route(path=f"/GroupV2/{group_id}/OptionalConversations/Add/", method="POST", data=data, auth=auth)
        )

    async def edit_optional_conversation(
        self,
        chat_enabled: bool,
        chat_name: str,
        chat_security: int,
        conversation_id: int,
        group_id: int,
        auth: AuthData,
        *args,
        **kwargs,
    ) -> dict:
        """
        Edit the settings of an optional conversation/chat channel. Requires admin permissions to the group.

        Warning: Requires Authentication.
            Required oauth2 scopes: AdminGroups

        Args:
            chat_enabled: _No description given by bungie._
            chat_name: _No description given by bungie._
            chat_security: _No description given by bungie._
            conversation_id: Conversation Id of the channel being edited.
            group_id: Group ID of the group to edit.
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

        data = {
            "chatEnabled": chat_enabled,
            "chatName": chat_name,
            "chatSecurity": chat_security,
        }

        return await self.request(
            Route(
                path=f"/GroupV2/{group_id}/OptionalConversations/Edit/{conversation_id}/",
                method="POST",
                data=data,
                auth=auth,
            )
        )

    async def get_members_of_group(
        self,
        currentpage: int,
        group_id: int,
        member_type: Optional[int] = None,
        name_search: Optional[str] = None,
        auth: Optional[AuthData] = None,
        *args,
        **kwargs,
    ) -> dict:
        """
        Get the list of members in a given group.

        Args:
            currentpage: Page number (starting with 1). Each page has a fixed size of 50 items per page.
            group_id: The ID of the group.
            member_type: Filter out other member types. Use None for all members.
            name_search: The name fragment upon which a search should be executed for members with matching display or unique names.
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
                path=f"/GroupV2/{group_id}/Members/",
                method="GET",
                member_type=member_type,
                name_search=name_search,
                auth=auth,
            )
        )

    async def get_admins_and_founder_of_group(
        self, currentpage: int, group_id: int, auth: Optional[AuthData] = None, *args, **kwargs
    ) -> dict:
        """
        Get the list of members in a given group who are of admin level or higher.

        Args:
            currentpage: Page number (starting with 1). Each page has a fixed size of 50 items per page.
            group_id: The ID of the group.
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

        return await self.request(Route(path=f"/GroupV2/{group_id}/AdminsAndFounder/", method="GET", auth=auth))

    async def edit_group_membership(
        self, group_id: int, membership_id: int, membership_type: int, member_type: int, auth: AuthData, *args, **kwargs
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
                path=f"/GroupV2/{group_id}/Members/{membership_type}/{membership_id}/SetMembershipType/{member_type}/",
                method="POST",
                auth=auth,
            )
        )

    async def kick_member(
        self, group_id: int, membership_id: int, membership_type: int, auth: AuthData, *args, **kwargs
    ) -> dict:
        """
        Kick a member from the given group, forcing them to reapply if they wish to re-join the group. You must have suitable permissions in the group to perform this operation.

        Warning: Requires Authentication.
            Required oauth2 scopes: AdminGroups

        Args:
            group_id: Group ID to kick the user from.
            membership_id: Membership ID to kick.
            membership_type: Membership type of the provided membership ID.
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
            Route(path=f"/GroupV2/{group_id}/Members/{membership_type}/{membership_id}/Kick/", method="POST", auth=auth)
        )

    async def ban_member(
        self,
        comment: str,
        length: Union[Any, int],
        group_id: int,
        membership_id: int,
        membership_type: int,
        auth: AuthData,
        *args,
        **kwargs,
    ) -> dict:
        """
        Bans the requested member from the requested group for the specified period of time.

        Warning: Requires Authentication.
            Required oauth2 scopes: AdminGroups

        Args:
            comment: _No description given by bungie._
            length: _No description given by bungie._
            group_id: Group ID that has the member to ban.
            membership_id: Membership ID of the member to ban from the group.
            membership_type: Membership type of the provided membership ID.
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

        data = {
            "comment": comment,
            "length": length,
        }

        return await self.request(
            Route(
                path=f"/GroupV2/{group_id}/Members/{membership_type}/{membership_id}/Ban/",
                method="POST",
                data=data,
                auth=auth,
            )
        )

    async def unban_member(
        self, group_id: int, membership_id: int, membership_type: int, auth: AuthData, *args, **kwargs
    ) -> dict:
        """
        Unbans the requested member, allowing them to re-apply for membership.

        Warning: Requires Authentication.
            Required oauth2 scopes: AdminGroups

        Args:
            group_id:
            membership_id: Membership ID of the member to unban from the group
            membership_type: Membership type of the provided membership ID.
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
            Route(
                path=f"/GroupV2/{group_id}/Members/{membership_type}/{membership_id}/Unban/", method="POST", auth=auth
            )
        )

    async def get_banned_members_of_group(
        self, currentpage: int, group_id: int, auth: AuthData, *args, **kwargs
    ) -> dict:
        """
        Get the list of banned members in a given group. Only accessible to group Admins and above. Not applicable to all groups. Check group features.

        Warning: Requires Authentication.
            Required oauth2 scopes: AdminGroups

        Args:
            currentpage: Page number (starting with 1). Each page has a fixed size of 50 entries.
            group_id: Group ID whose banned members you are fetching
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

        return await self.request(Route(path=f"/GroupV2/{group_id}/Banned/", method="GET", auth=auth))

    async def get_group_edit_history(self, currentpage: int, group_id: int, auth: AuthData, *args, **kwargs) -> dict:
        """
        Get the list of edits made to a given group. Only accessible to group Admins and above.

        Warning: Requires Authentication.
            Required oauth2 scopes: AdminGroups

        Args:
            currentpage: Page number (starting with 1). Each page has a fixed size of 50 entries.
            group_id: Group ID whose edit history you are fetching
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

        return await self.request(Route(path=f"/GroupV2/{group_id}/EditHistory/", method="GET", auth=auth))

    async def abdicate_foundership(
        self, founder_id_new: int, group_id: int, membership_type: int, auth: Optional[AuthData] = None, *args, **kwargs
    ) -> dict:
        """
        An administrative method to allow the founder of a group or clan to give up their position to another admin permanently.

        Args:
            founder_id_new: The new founder for this group. Must already be a group admin.
            group_id: The target group id.
            membership_type: Membership type of the provided founderIdNew.
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
                path=f"/GroupV2/{group_id}/Admin/AbdicateFoundership/{membership_type}/{founder_id_new}/",
                method="POST",
                auth=auth,
            )
        )

    async def get_pending_memberships(self, currentpage: int, group_id: int, auth: AuthData, *args, **kwargs) -> dict:
        """
        Get the list of users who are awaiting a decision on their application to join a given group. Modified to include application info.

        Warning: Requires Authentication.
            Required oauth2 scopes: AdminGroups

        Args:
            currentpage: Page number (starting with 1). Each page has a fixed size of 50 items per page.
            group_id: ID of the group.
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

        return await self.request(Route(path=f"/GroupV2/{group_id}/Members/Pending/", method="GET", auth=auth))

    async def get_invited_individuals(self, currentpage: int, group_id: int, auth: AuthData, *args, **kwargs) -> dict:
        """
        Get the list of users who have been invited into the group.

        Warning: Requires Authentication.
            Required oauth2 scopes: AdminGroups

        Args:
            currentpage: Page number (starting with 1). Each page has a fixed size of 50 items per page.
            group_id: ID of the group.
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
            Route(path=f"/GroupV2/{group_id}/Members/InvitedIndividuals/", method="GET", auth=auth)
        )

    async def approve_all_pending(self, message: str, group_id: int, auth: AuthData, *args, **kwargs) -> dict:
        """
        Approve all of the pending users for the given group.

        Warning: Requires Authentication.
            Required oauth2 scopes: AdminGroups

        Args:
            message: _No description given by bungie._
            group_id: ID of the group.
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

        data = {
            "message": message,
        }

        return await self.request(
            Route(path=f"/GroupV2/{group_id}/Members/ApproveAll/", method="POST", data=data, auth=auth)
        )

    async def deny_all_pending(self, message: str, group_id: int, auth: AuthData, *args, **kwargs) -> dict:
        """
        Deny all of the pending users for the given group.

        Warning: Requires Authentication.
            Required oauth2 scopes: AdminGroups

        Args:
            message: _No description given by bungie._
            group_id: ID of the group.
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

        data = {
            "message": message,
        }

        return await self.request(
            Route(path=f"/GroupV2/{group_id}/Members/DenyAll/", method="POST", data=data, auth=auth)
        )

    async def approve_pending_for_list(
        self, memberships: list[Any], message: str, group_id: int, auth: AuthData, *args, **kwargs
    ) -> dict:
        """
        Approve all of the pending users for the given group.

        Warning: Requires Authentication.
            Required oauth2 scopes: AdminGroups

        Args:
            memberships: _No description given by bungie._
            message: _No description given by bungie._
            group_id: ID of the group.
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

        data = {
            "memberships": memberships,
            "message": message,
        }

        return await self.request(
            Route(path=f"/GroupV2/{group_id}/Members/ApproveList/", method="POST", data=data, auth=auth)
        )

    async def approve_pending(
        self, message: str, group_id: int, membership_id: int, membership_type: int, auth: AuthData, *args, **kwargs
    ) -> dict:
        """
        Approve the given membershipId to join the group/clan as long as they have applied.

        Warning: Requires Authentication.
            Required oauth2 scopes: AdminGroups

        Args:
            message: _No description given by bungie._
            group_id: ID of the group.
            membership_id: The membership id being approved.
            membership_type: Membership type of the supplied membership ID.
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

        data = {
            "message": message,
        }

        return await self.request(
            Route(
                path=f"/GroupV2/{group_id}/Members/Approve/{membership_type}/{membership_id}/",
                method="POST",
                data=data,
                auth=auth,
            )
        )

    async def deny_pending_for_list(
        self, memberships: list[Any], message: str, group_id: int, auth: AuthData, *args, **kwargs
    ) -> dict:
        """
        Deny all of the pending users for the given group that match the passed-in .

        Warning: Requires Authentication.
            Required oauth2 scopes: AdminGroups

        Args:
            memberships: _No description given by bungie._
            message: _No description given by bungie._
            group_id: ID of the group.
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

        data = {
            "memberships": memberships,
            "message": message,
        }

        return await self.request(
            Route(path=f"/GroupV2/{group_id}/Members/DenyList/", method="POST", data=data, auth=auth)
        )

    async def get_groups_for_member(
        self,
        filter: int,
        group_type: int,
        membership_id: int,
        membership_type: int,
        auth: Optional[AuthData] = None,
        *args,
        **kwargs,
    ) -> dict:
        """
        Get information about the groups that a given member has joined.

        Args:
            filter: Filter apply to list of joined groups.
            group_type: Type of group the supplied member founded.
            membership_id: Membership ID to for which to find founded groups.
            membership_type: Membership type of the supplied membership ID.
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
                path=f"/GroupV2/User/{membership_type}/{membership_id}/{filter}/{group_type}/", method="GET", auth=auth
            )
        )

    async def recover_group_for_founder(
        self,
        group_type: int,
        membership_id: int,
        membership_type: int,
        auth: Optional[AuthData] = None,
        *args,
        **kwargs,
    ) -> dict:
        """
        Allows a founder to manually recover a group they can see in game but not on bungie.net

        Args:
            group_type: Type of group the supplied member founded.
            membership_id: Membership ID to for which to find founded groups.
            membership_type: Membership type of the supplied membership ID.
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
            Route(path=f"/GroupV2/Recover/{membership_type}/{membership_id}/{group_type}/", method="GET", auth=auth)
        )

    async def get_potential_groups_for_member(
        self,
        filter: int,
        group_type: int,
        membership_id: int,
        membership_type: int,
        auth: Optional[AuthData] = None,
        *args,
        **kwargs,
    ) -> dict:
        """
        Get information about the groups that a given member has applied to or been invited to.

        Args:
            filter: Filter apply to list of potential joined groups.
            group_type: Type of group the supplied member applied.
            membership_id: Membership ID to for which to find applied groups.
            membership_type: Membership type of the supplied membership ID.
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
                path=f"/GroupV2/User/Potential/{membership_type}/{membership_id}/{filter}/{group_type}/",
                method="GET",
                auth=auth,
            )
        )

    async def individual_group_invite(
        self, message: str, group_id: int, membership_id: int, membership_type: int, auth: AuthData, *args, **kwargs
    ) -> dict:
        """
        Invite a user to join this group.

        Warning: Requires Authentication.
            Required oauth2 scopes: AdminGroups

        Args:
            message: _No description given by bungie._
            group_id: ID of the group you would like to join.
            membership_id: Membership id of the account being invited.
            membership_type: MembershipType of the account being invited.
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

        data = {
            "message": message,
        }

        return await self.request(
            Route(
                path=f"/GroupV2/{group_id}/Members/IndividualInvite/{membership_type}/{membership_id}/",
                method="POST",
                data=data,
                auth=auth,
            )
        )

    async def individual_group_invite_cancel(
        self, group_id: int, membership_id: int, membership_type: int, auth: AuthData, *args, **kwargs
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
                path=f"/GroupV2/{group_id}/Members/IndividualInviteCancel/{membership_type}/{membership_id}/",
                method="POST",
                auth=auth,
            )
        )
