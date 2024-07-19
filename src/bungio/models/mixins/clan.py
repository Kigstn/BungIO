from typing import TYPE_CHECKING, Optional, Union

from bungio.models.base import ClientMixin, FuzzyAttrFinder, custom_define

if TYPE_CHECKING:
    # AUTOMATIC IMPORTS START
    from bungio.models import FireteamResponse
    from bungio.models import BungieMembershipType
    from bungio.models import EntityActionResult
    from bungio.models import FireteamDateRange
    from bungio.models import GroupOptionalConversationEditRequest
    from bungio.models import ClanBanner
    from bungio.models import SearchResultOfFireteamSummary
    from bungio.models import GroupEditAction
    from bungio.models import GroupApplicationListRequest
    from bungio.models import RuntimeGroupMemberType
    from bungio.models import SearchResultOfGroupMember
    from bungio.models import SearchResultOfGroupMemberApplication
    from bungio.models import GroupOptionsEditAction
    from bungio.models import GroupApplicationRequest
    from bungio.models import SearchResultOfFireteamResponse
    from bungio.models import GroupOptionalConversation
    from bungio.models import SearchResultOfGroupEditHistory
    from bungio.models import DestinyMilestone
    from bungio.models import FireteamSlotSearch
    from bungio.models import GroupOptionalConversationAddRequest
    from bungio.models import DestinyLeaderboard
    from bungio.models import GroupResponse
    from bungio.models import FireteamPublicSearchOption
    from bungio.models import FireteamPlatform
    from bungio.models import SearchResultOfGroupBan
    from bungio.models import DestinyClanAggregateStat

    # AUTOMATIC IMPORTS END
    from bungio.models.auth import AuthData

__all__ = ("DestinyClanMixin",)


@custom_define()
class DestinyClanMixin(ClientMixin, FuzzyAttrFinder):
    # DO NOT CHANGE ANY CODE BELOW. Automatically generated and overwritten

    async def get_group(self, auth: Optional["AuthData"] = None) -> "GroupResponse":
        """
        Get information about a specific group of the given ID.

        Args:
            auth: Authentication information. Required when users with a private profile are queried, or when Bungie feels like it

        Returns:
            The model which is returned by bungie. [General endpoint information.](https://bungie-net.github.io/multi/index.html)
        """

        return await self._client.api.get_group(group_id=self._fuzzy_getattr("group_id"), auth=auth)

    async def get_group_optional_conversations(
        self, auth: Optional["AuthData"] = None
    ) -> list["GroupOptionalConversation"]:
        """
        Gets a list of available optional conversation channels and their settings.

        Args:
            auth: Authentication information. Required when users with a private profile are queried, or when Bungie feels like it

        Returns:
            The model which is returned by bungie. [General endpoint information.](https://bungie-net.github.io/multi/index.html)
        """

        return await self._client.api.get_group_optional_conversations(
            group_id=self._fuzzy_getattr("group_id"), auth=auth
        )

    async def edit_group(self, data: "GroupEditAction", auth: "AuthData") -> int:
        """
        Edit an existing group. You must have suitable permissions in the group to perform this operation. This latest revision will only edit the fields you pass in - pass null for properties you want to leave unaltered.

        Warning: Requires Authentication.
            Required oauth2 scopes: AdminGroups

        Args:
            data: The required data for this request.
            auth: Authentication information.

        Returns:
            The model which is returned by bungie. [General endpoint information.](https://bungie-net.github.io/multi/index.html)
        """

        return await self._client.api.edit_group(data=data, group_id=self._fuzzy_getattr("group_id"), auth=auth)

    async def edit_clan_banner(self, data: "ClanBanner", auth: "AuthData") -> int:
        """
        Edit an existing group's clan banner. You must have suitable permissions in the group to perform this operation. All fields are required.

        Warning: Requires Authentication.
            Required oauth2 scopes: AdminGroups

        Args:
            data: The required data for this request.
            auth: Authentication information.

        Returns:
            The model which is returned by bungie. [General endpoint information.](https://bungie-net.github.io/multi/index.html)
        """

        return await self._client.api.edit_clan_banner(data=data, group_id=self._fuzzy_getattr("group_id"), auth=auth)

    async def edit_founder_options(self, data: "GroupOptionsEditAction", auth: "AuthData") -> int:
        """
        Edit group options only available to a founder. You must have suitable permissions in the group to perform this operation.

        Warning: Requires Authentication.
            Required oauth2 scopes: AdminGroups

        Args:
            data: The required data for this request.
            auth: Authentication information.

        Returns:
            The model which is returned by bungie. [General endpoint information.](https://bungie-net.github.io/multi/index.html)
        """

        return await self._client.api.edit_founder_options(
            data=data, group_id=self._fuzzy_getattr("group_id"), auth=auth
        )

    async def add_optional_conversation(self, data: "GroupOptionalConversationAddRequest", auth: "AuthData") -> int:
        """
        Add a new optional conversation/chat channel. Requires admin permissions to the group.

        Warning: Requires Authentication.
            Required oauth2 scopes: AdminGroups

        Args:
            data: The required data for this request.
            auth: Authentication information.

        Returns:
            The model which is returned by bungie. [General endpoint information.](https://bungie-net.github.io/multi/index.html)
        """

        return await self._client.api.add_optional_conversation(
            data=data, group_id=self._fuzzy_getattr("group_id"), auth=auth
        )

    async def edit_optional_conversation(
        self, data: "GroupOptionalConversationEditRequest", conversation_id: int, auth: "AuthData"
    ) -> int:
        """
        Edit the settings of an optional conversation/chat channel. Requires admin permissions to the group.

        Warning: Requires Authentication.
            Required oauth2 scopes: AdminGroups

        Args:
            data: The required data for this request.
            conversation_id: Conversation Id of the channel being edited.
            auth: Authentication information.

        Returns:
            The model which is returned by bungie. [General endpoint information.](https://bungie-net.github.io/multi/index.html)
        """

        return await self._client.api.edit_optional_conversation(
            data=data, conversation_id=conversation_id, group_id=self._fuzzy_getattr("group_id"), auth=auth
        )

    async def get_members_of_group(
        self,
        currentpage: int,
        member_type: Union["RuntimeGroupMemberType", int],
        name_search: str,
        auth: Optional["AuthData"] = None,
    ) -> "SearchResultOfGroupMember":
        """
        Get the list of members in a given group.

        Args:
            currentpage: Page number (starting with 1). Each page has a fixed size of 50 items per page.
            member_type: Filter out other member types. Use None for all members.
            name_search: The name fragment upon which a search should be executed for members with matching display or unique names.
            auth: Authentication information. Required when users with a private profile are queried, or when Bungie feels like it

        Returns:
            The model which is returned by bungie. [General endpoint information.](https://bungie-net.github.io/multi/index.html)
        """

        return await self._client.api.get_members_of_group(
            currentpage=currentpage,
            group_id=self._fuzzy_getattr("group_id"),
            member_type=member_type,
            name_search=name_search,
            auth=auth,
        )

    async def get_admins_and_founder_of_group(
        self, currentpage: int, auth: Optional["AuthData"] = None
    ) -> "SearchResultOfGroupMember":
        """
        Get the list of members in a given group who are of admin level or higher.

        Args:
            currentpage: Page number (starting with 1). Each page has a fixed size of 50 items per page.
            auth: Authentication information. Required when users with a private profile are queried, or when Bungie feels like it

        Returns:
            The model which is returned by bungie. [General endpoint information.](https://bungie-net.github.io/multi/index.html)
        """

        return await self._client.api.get_admins_and_founder_of_group(
            currentpage=currentpage, group_id=self._fuzzy_getattr("group_id"), auth=auth
        )

    async def get_banned_members_of_group(self, currentpage: int, auth: "AuthData") -> "SearchResultOfGroupBan":
        """
        Get the list of banned members in a given group. Only accessible to group Admins and above. Not applicable to all groups. Check group features.

        Warning: Requires Authentication.
            Required oauth2 scopes: AdminGroups

        Args:
            currentpage: Page number (starting with 1). Each page has a fixed size of 50 entries.
            auth: Authentication information.

        Returns:
            The model which is returned by bungie. [General endpoint information.](https://bungie-net.github.io/multi/index.html)
        """

        return await self._client.api.get_banned_members_of_group(
            currentpage=currentpage, group_id=self._fuzzy_getattr("group_id"), auth=auth
        )

    async def get_group_edit_history(self, currentpage: int, auth: "AuthData") -> "SearchResultOfGroupEditHistory":
        """
        Get the list of edits made to a given group. Only accessible to group Admins and above.

        Warning: Requires Authentication.
            Required oauth2 scopes: AdminGroups

        Args:
            currentpage: Page number (starting with 1). Each page has a fixed size of 50 entries.
            auth: Authentication information.

        Returns:
            The model which is returned by bungie. [General endpoint information.](https://bungie-net.github.io/multi/index.html)
        """

        return await self._client.api.get_group_edit_history(
            currentpage=currentpage, group_id=self._fuzzy_getattr("group_id"), auth=auth
        )

    async def abdicate_foundership(
        self,
        founder_id_new: int,
        membership_type: Union["BungieMembershipType", int],
        auth: Optional["AuthData"] = None,
    ) -> bool:
        """
        An administrative method to allow the founder of a group or clan to give up their position to another admin permanently.

        Args:
            founder_id_new: The new founder for this group. Must already be a group admin.
            membership_type: Membership type of the provided founderIdNew.
            auth: Authentication information. Required when users with a private profile are queried, or when Bungie feels like it

        Returns:
            The model which is returned by bungie. [General endpoint information.](https://bungie-net.github.io/multi/index.html)
        """

        return await self._client.api.abdicate_foundership(
            founder_id_new=founder_id_new,
            group_id=self._fuzzy_getattr("group_id"),
            membership_type=membership_type,
            auth=auth,
        )

    async def get_pending_memberships(
        self, currentpage: int, auth: "AuthData"
    ) -> "SearchResultOfGroupMemberApplication":
        """
        Get the list of users who are awaiting a decision on their application to join a given group. Modified to include application info.

        Warning: Requires Authentication.
            Required oauth2 scopes: AdminGroups

        Args:
            currentpage: Page number (starting with 1). Each page has a fixed size of 50 items per page.
            auth: Authentication information.

        Returns:
            The model which is returned by bungie. [General endpoint information.](https://bungie-net.github.io/multi/index.html)
        """

        return await self._client.api.get_pending_memberships(
            currentpage=currentpage, group_id=self._fuzzy_getattr("group_id"), auth=auth
        )

    async def get_invited_individuals(
        self, currentpage: int, auth: "AuthData"
    ) -> "SearchResultOfGroupMemberApplication":
        """
        Get the list of users who have been invited into the group.

        Warning: Requires Authentication.
            Required oauth2 scopes: AdminGroups

        Args:
            currentpage: Page number (starting with 1). Each page has a fixed size of 50 items per page.
            auth: Authentication information.

        Returns:
            The model which is returned by bungie. [General endpoint information.](https://bungie-net.github.io/multi/index.html)
        """

        return await self._client.api.get_invited_individuals(
            currentpage=currentpage, group_id=self._fuzzy_getattr("group_id"), auth=auth
        )

    async def approve_all_pending(
        self, data: "GroupApplicationRequest", auth: "AuthData"
    ) -> list["EntityActionResult"]:
        """
        Approve all of the pending users for the given group.

        Warning: Requires Authentication.
            Required oauth2 scopes: AdminGroups

        Args:
            data: The required data for this request.
            auth: Authentication information.

        Returns:
            The model which is returned by bungie. [General endpoint information.](https://bungie-net.github.io/multi/index.html)
        """

        return await self._client.api.approve_all_pending(
            data=data, group_id=self._fuzzy_getattr("group_id"), auth=auth
        )

    async def deny_all_pending(self, data: "GroupApplicationRequest", auth: "AuthData") -> list["EntityActionResult"]:
        """
        Deny all of the pending users for the given group.

        Warning: Requires Authentication.
            Required oauth2 scopes: AdminGroups

        Args:
            data: The required data for this request.
            auth: Authentication information.

        Returns:
            The model which is returned by bungie. [General endpoint information.](https://bungie-net.github.io/multi/index.html)
        """

        return await self._client.api.deny_all_pending(data=data, group_id=self._fuzzy_getattr("group_id"), auth=auth)

    async def approve_pending_for_list(
        self, data: "GroupApplicationListRequest", auth: "AuthData"
    ) -> list["EntityActionResult"]:
        """
        Approve all of the pending users for the given group.

        Warning: Requires Authentication.
            Required oauth2 scopes: AdminGroups

        Args:
            data: The required data for this request.
            auth: Authentication information.

        Returns:
            The model which is returned by bungie. [General endpoint information.](https://bungie-net.github.io/multi/index.html)
        """

        return await self._client.api.approve_pending_for_list(
            data=data, group_id=self._fuzzy_getattr("group_id"), auth=auth
        )

    async def deny_pending_for_list(
        self, data: "GroupApplicationListRequest", auth: "AuthData"
    ) -> list["EntityActionResult"]:
        """
        Deny all of the pending users for the given group that match the passed-in .

        Warning: Requires Authentication.
            Required oauth2 scopes: AdminGroups

        Args:
            data: The required data for this request.
            auth: Authentication information.

        Returns:
            The model which is returned by bungie. [General endpoint information.](https://bungie-net.github.io/multi/index.html)
        """

        return await self._client.api.deny_pending_for_list(
            data=data, group_id=self._fuzzy_getattr("group_id"), auth=auth
        )

    async def get_clan_weekly_reward_state(self, auth: Optional["AuthData"] = None) -> "DestinyMilestone":
        """
        Returns information on the weekly clan rewards and if the clan has earned them or not. Note that this will always report rewards as not redeemed.

        Args:
            auth: Authentication information. Required when users with a private profile are queried, or when Bungie feels like it

        Returns:
            The model which is returned by bungie. [General endpoint information.](https://bungie-net.github.io/multi/index.html)
        """

        return await self._client.api.get_clan_weekly_reward_state(group_id=self._fuzzy_getattr("group_id"), auth=auth)

    async def get_clan_leaderboards(
        self, maxtop: int, modes: str, statid: str, auth: Optional["AuthData"] = None
    ) -> dict[str, dict[str, "DestinyLeaderboard"]]:
        """
        Gets leaderboards with the signed in user's friends and the supplied destinyMembershipId as the focus. PREVIEW: This endpoint is still in beta, and may experience rough edges. The schema is in final form, but there may be bugs that prevent desirable operation.

        Args:
            maxtop: Maximum number of top players to return. Use a large number to get entire leaderboard.
            modes: List of game modes for which to get leaderboards. See the documentation for DestinyActivityModeType for valid values, and pass in string representation, comma delimited.
            statid: ID of stat to return rather than returning all Leaderboard stats.
            auth: Authentication information. Required when users with a private profile are queried, or when Bungie feels like it

        Returns:
            The model which is returned by bungie. [General endpoint information.](https://bungie-net.github.io/multi/index.html)
        """

        return await self._client.api.get_clan_leaderboards(
            group_id=self._fuzzy_getattr("group_id"), maxtop=maxtop, modes=modes, statid=statid, auth=auth
        )

    async def get_clan_aggregate_stats(
        self, modes: str, auth: Optional["AuthData"] = None
    ) -> list["DestinyClanAggregateStat"]:
        """
        Gets aggregated stats for a clan using the same categories as the clan leaderboards. PREVIEW: This endpoint is still in beta, and may experience rough edges. The schema is in final form, but there may be bugs that prevent desirable operation.

        Args:
            modes: List of game modes for which to get leaderboards. See the documentation for DestinyActivityModeType for valid values, and pass in string representation, comma delimited.
            auth: Authentication information. Required when users with a private profile are queried, or when Bungie feels like it

        Returns:
            The model which is returned by bungie. [General endpoint information.](https://bungie-net.github.io/multi/index.html)
        """

        return await self._client.api.get_clan_aggregate_stats(
            group_id=self._fuzzy_getattr("group_id"), modes=modes, auth=auth
        )

    async def get_active_private_clan_fireteam_count(self, auth: "AuthData") -> int:
        """
        Gets a count of all active non-public fireteams for the specified clan. Maximum value returned is 25.

        Warning: Requires Authentication.
            Required oauth2 scopes: ReadGroups

        Args:
            auth: Authentication information.

        Returns:
            The model which is returned by bungie. [General endpoint information.](https://bungie-net.github.io/multi/index.html)
        """

        return await self._client.api.get_active_private_clan_fireteam_count(
            group_id=self._fuzzy_getattr("group_id"), auth=auth
        )

    async def get_available_clan_fireteams(
        self,
        activity_type: int,
        date_range: Union["FireteamDateRange", int],
        page: int,
        platform: Union["FireteamPlatform", int],
        public_only: Union["FireteamPublicSearchOption", int],
        slot_filter: Union["FireteamSlotSearch", int],
        auth: "AuthData",
        exclude_immediate: bool,
        lang_filter: str,
    ) -> "SearchResultOfFireteamSummary":
        """
        Gets a listing of all of this clan's fireteams that are have available slots. Caller is not checked for join criteria so caching is maximized.

        Warning: Requires Authentication.
            Required oauth2 scopes: ReadGroups

        Args:
            activity_type: The activity type to filter by.
            date_range: The date range to grab available fireteams.
            page: Zero based page
            platform: The platform filter.
            public_only: Determines public/private filtering.
            slot_filter: Filters based on available slots
            auth: Authentication information.
            exclude_immediate: If you wish the result to exclude immediate fireteams, set this to true. Immediate-only can be forced using the dateRange enum.
            lang_filter: An optional language filter.

        Returns:
            The model which is returned by bungie. [General endpoint information.](https://bungie-net.github.io/multi/index.html)
        """

        return await self._client.api.get_available_clan_fireteams(
            activity_type=activity_type,
            date_range=date_range,
            group_id=self._fuzzy_getattr("group_id"),
            page=page,
            platform=platform,
            public_only=public_only,
            slot_filter=slot_filter,
            auth=auth,
            exclude_immediate=exclude_immediate,
            lang_filter=lang_filter,
        )

    async def get_my_clan_fireteams(
        self,
        include_closed: bool,
        page: int,
        platform: Union["FireteamPlatform", int],
        auth: "AuthData",
        group_filter: bool,
        lang_filter: str,
    ) -> "SearchResultOfFireteamResponse":
        """
        Gets a listing of all fireteams that caller is an applicant, a member, or an alternate of.

        Warning: Requires Authentication.
            Required oauth2 scopes: ReadGroups

        Args:
            include_closed: If true, return fireteams that have been closed.
            page: Deprecated parameter, ignored.
            platform: The platform filter.
            auth: Authentication information.
            group_filter: If true, filter by clan. Otherwise, ignore the clan and show all of the user's fireteams.
            lang_filter: An optional language filter.

        Returns:
            The model which is returned by bungie. [General endpoint information.](https://bungie-net.github.io/multi/index.html)
        """

        return await self._client.api.get_my_clan_fireteams(
            group_id=self._fuzzy_getattr("group_id"),
            include_closed=include_closed,
            page=page,
            platform=platform,
            auth=auth,
            group_filter=group_filter,
            lang_filter=lang_filter,
        )

    async def get_clan_fireteam(self, fireteam_id: int, auth: "AuthData") -> "FireteamResponse":
        """
        Gets a specific fireteam.

        Warning: Requires Authentication.
            Required oauth2 scopes: ReadGroups

        Args:
            fireteam_id: The unique id of the fireteam.
            auth: Authentication information.

        Returns:
            The model which is returned by bungie. [General endpoint information.](https://bungie-net.github.io/multi/index.html)
        """

        return await self._client.api.get_clan_fireteam(
            fireteam_id=fireteam_id, group_id=self._fuzzy_getattr("group_id"), auth=auth
        )
