from datetime import datetime
from typing import TYPE_CHECKING, Optional

import attr

from bungio.models.base import ClientMixin, FuzzyAttrFinder

if TYPE_CHECKING:
    # AUTOMATIC IMPORTS START
    from bungio.models import (
        BungieMembershipType,
        DestinyComponentType,
        DestinyHistoricalStatsAccountResult,
        DestinyItemResponse,
        DestinyLeaderboard,
        DestinyLinkedProfilesResponse,
        DestinyProfileResponse,
        DestinyStatsGroupType,
        GetGroupsForMemberResponse,
        GroupApplicationRequest,
        GroupApplicationResponse,
        GroupBanRequest,
        GroupMemberLeaveResult,
        GroupMembershipSearchResponse,
        GroupPotentialMembershipSearchResponse,
        GroupPotentialMemberStatus,
        GroupsForMemberFilter,
        GroupType,
        RuntimeGroupMemberType,
        UserMembershipData,
    )
    from bungio.models.auth import AuthData

    # AUTOMATIC IMPORTS END


@attr.define
class DestinyUser(ClientMixin, FuzzyAttrFinder):
    # DO NOT CHANGE ANY CODE BELOW. Automatically generated and overwritten

    async def get_membership_data_by_id(self, auth: Optional["AuthData"] = None) -> "UserMembershipData":
        """
        Returns a list of accounts associated with the supplied membership ID and membership type. This will include all linked accounts (even when hidden) if supplied credentials permit it.

        Args:
            auth: Authentication information. Required when users with a private profile are queried, or when Bungie feels like it

        Returns:
            The model which is returned by bungie. [General endpoint information.](https://bungie-net.github.io/multi/index.html)
        """

        return await self._client.api.get_membership_data_by_id(
            membership_id=self._fuzzy_getattr("membership_id"),
            membership_type=self._fuzzy_getattr("membership_type"),
            auth=auth,
        )

    async def edit_group_membership(
        self, group_id: int, member_type: "RuntimeGroupMemberType", auth: "AuthData"
    ) -> int:
        """
        Edit the membership type of a given member. You must have suitable permissions in the group to perform this operation.

        Warning: Requires Authentication.
            Required oauth2 scopes: AdminGroups

        Args:
            group_id: ID of the group to which the member belongs.
            member_type: New membertype for the specified member.
            auth: Authentication information.

        Returns:
            The model which is returned by bungie. [General endpoint information.](https://bungie-net.github.io/multi/index.html)
        """

        return await self._client.api.edit_group_membership(
            group_id=group_id,
            membership_id=self._fuzzy_getattr("membership_id"),
            membership_type=self._fuzzy_getattr("membership_type"),
            member_type=member_type,
            auth=auth,
        )

    async def kick_member(self, group_id: int, auth: "AuthData") -> "GroupMemberLeaveResult":
        """
        Kick a member from the given group, forcing them to reapply if they wish to re-join the group. You must have suitable permissions in the group to perform this operation.

        Warning: Requires Authentication.
            Required oauth2 scopes: AdminGroups

        Args:
            group_id: Group ID to kick the user from.
            auth: Authentication information.

        Returns:
            The model which is returned by bungie. [General endpoint information.](https://bungie-net.github.io/multi/index.html)
        """

        return await self._client.api.kick_member(
            group_id=group_id,
            membership_id=self._fuzzy_getattr("membership_id"),
            membership_type=self._fuzzy_getattr("membership_type"),
            auth=auth,
        )

    async def ban_member(self, data: "GroupBanRequest", group_id: int, auth: "AuthData") -> int:
        """
        Bans the requested member from the requested group for the specified period of time.

        Warning: Requires Authentication.
            Required oauth2 scopes: AdminGroups

        Args:
            data: The required data for this request.
            group_id: Group ID that has the member to ban.
            auth: Authentication information.

        Returns:
            The model which is returned by bungie. [General endpoint information.](https://bungie-net.github.io/multi/index.html)
        """

        return await self._client.api.ban_member(
            data=data,
            group_id=group_id,
            membership_id=self._fuzzy_getattr("membership_id"),
            membership_type=self._fuzzy_getattr("membership_type"),
            auth=auth,
        )

    async def unban_member(self, group_id: int, auth: "AuthData") -> int:
        """
        Unbans the requested member, allowing them to re-apply for membership.

        Warning: Requires Authentication.
            Required oauth2 scopes: AdminGroups

        Args:
            group_id:
            auth: Authentication information.

        Returns:
            The model which is returned by bungie. [General endpoint information.](https://bungie-net.github.io/multi/index.html)
        """

        return await self._client.api.unban_member(
            group_id=group_id,
            membership_id=self._fuzzy_getattr("membership_id"),
            membership_type=self._fuzzy_getattr("membership_type"),
            auth=auth,
        )

    async def approve_pending(self, data: "GroupApplicationRequest", group_id: int, auth: "AuthData") -> bool:
        """
        Approve the given membershipId to join the group/clan as long as they have applied.

        Warning: Requires Authentication.
            Required oauth2 scopes: AdminGroups

        Args:
            data: The required data for this request.
            group_id: ID of the group.
            auth: Authentication information.

        Returns:
            The model which is returned by bungie. [General endpoint information.](https://bungie-net.github.io/multi/index.html)
        """

        return await self._client.api.approve_pending(
            data=data,
            group_id=group_id,
            membership_id=self._fuzzy_getattr("membership_id"),
            membership_type=self._fuzzy_getattr("membership_type"),
            auth=auth,
        )

    async def get_groups_for_member(
        self, filter: "GroupsForMemberFilter", group_type: "GroupType", auth: Optional["AuthData"] = None
    ) -> "GetGroupsForMemberResponse":
        """
        Get information about the groups that a given member has joined.

        Args:
            filter: Filter apply to list of joined groups.
            group_type: Type of group the supplied member founded.
            auth: Authentication information. Required when users with a private profile are queried, or when Bungie feels like it

        Returns:
            The model which is returned by bungie. [General endpoint information.](https://bungie-net.github.io/multi/index.html)
        """

        return await self._client.api.get_groups_for_member(
            filter=filter,
            group_type=group_type,
            membership_id=self._fuzzy_getattr("membership_id"),
            membership_type=self._fuzzy_getattr("membership_type"),
            auth=auth,
        )

    async def recover_group_for_founder(
        self, group_type: "GroupType", auth: Optional["AuthData"] = None
    ) -> "GroupMembershipSearchResponse":
        """
        Allows a founder to manually recover a group they can see in game but not on bungie.net

        Args:
            group_type: Type of group the supplied member founded.
            auth: Authentication information. Required when users with a private profile are queried, or when Bungie feels like it

        Returns:
            The model which is returned by bungie. [General endpoint information.](https://bungie-net.github.io/multi/index.html)
        """

        return await self._client.api.recover_group_for_founder(
            group_type=group_type,
            membership_id=self._fuzzy_getattr("membership_id"),
            membership_type=self._fuzzy_getattr("membership_type"),
            auth=auth,
        )

    async def get_potential_groups_for_member(
        self, filter: "GroupPotentialMemberStatus", group_type: "GroupType", auth: Optional["AuthData"] = None
    ) -> "GroupPotentialMembershipSearchResponse":
        """
        Get information about the groups that a given member has applied to or been invited to.

        Args:
            filter: Filter apply to list of potential joined groups.
            group_type: Type of group the supplied member applied.
            auth: Authentication information. Required when users with a private profile are queried, or when Bungie feels like it

        Returns:
            The model which is returned by bungie. [General endpoint information.](https://bungie-net.github.io/multi/index.html)
        """

        return await self._client.api.get_potential_groups_for_member(
            filter=filter,
            group_type=group_type,
            membership_id=self._fuzzy_getattr("membership_id"),
            membership_type=self._fuzzy_getattr("membership_type"),
            auth=auth,
        )

    async def individual_group_invite(
        self, data: "GroupApplicationRequest", group_id: int, auth: "AuthData"
    ) -> "GroupApplicationResponse":
        """
        Invite a user to join this group.

        Warning: Requires Authentication.
            Required oauth2 scopes: AdminGroups

        Args:
            data: The required data for this request.
            group_id: ID of the group you would like to join.
            auth: Authentication information.

        Returns:
            The model which is returned by bungie. [General endpoint information.](https://bungie-net.github.io/multi/index.html)
        """

        return await self._client.api.individual_group_invite(
            data=data,
            group_id=group_id,
            membership_id=self._fuzzy_getattr("membership_id"),
            membership_type=self._fuzzy_getattr("membership_type"),
            auth=auth,
        )

    async def individual_group_invite_cancel(self, group_id: int, auth: "AuthData") -> "GroupApplicationResponse":
        """
        Cancels a pending invitation to join a group.

        Warning: Requires Authentication.
            Required oauth2 scopes: AdminGroups

        Args:
            group_id: ID of the group you would like to join.
            auth: Authentication information.

        Returns:
            The model which is returned by bungie. [General endpoint information.](https://bungie-net.github.io/multi/index.html)
        """

        return await self._client.api.individual_group_invite_cancel(
            group_id=group_id,
            membership_id=self._fuzzy_getattr("membership_id"),
            membership_type=self._fuzzy_getattr("membership_type"),
            auth=auth,
        )

    async def get_linked_profiles(
        self, get_all_memberships: bool, auth: Optional["AuthData"] = None
    ) -> "DestinyLinkedProfilesResponse":
        """
        Returns a summary information about all profiles linked to the requesting membership type/membership ID that have valid Destiny information. The passed-in Membership Type/Membership ID may be a Bungie.Net membership or a Destiny membership. It only returns the minimal amount of data to begin making more substantive requests, but will hopefully serve as a useful alternative to UserServices for people who just care about Destiny data. Note that it will only return linked accounts whose linkages you are allowed to view.

        Args:
            get_all_memberships: (optional) if set to 'true', all memberships regardless of whether they're obscured by overrides will be returned. Normal privacy restrictions on account linking will still apply no matter what.
            auth: Authentication information. Required when users with a private profile are queried, or when Bungie feels like it

        Returns:
            The model which is returned by bungie. [General endpoint information.](https://bungie-net.github.io/multi/index.html)
        """

        return await self._client.api.get_linked_profiles(
            membership_id=self._fuzzy_getattr("membership_id"),
            membership_type=self._fuzzy_getattr("membership_type"),
            get_all_memberships=get_all_memberships,
            auth=auth,
        )

    async def get_profile(
        self, destiny_membership_id: int, components: list["DestinyComponentType"], auth: Optional["AuthData"] = None
    ) -> "DestinyProfileResponse":
        """
        Returns Destiny Profile information for the supplied membership.

        Args:
            destiny_membership_id: Destiny membership ID.
            components: A comma separated list of components to return (as strings or numeric values). See the DestinyComponentType enum for valid components to request. You must request at least one component to receive results.
            auth: Authentication information. Required when users with a private profile are queried, or when Bungie feels like it

        Returns:
            The model which is returned by bungie. [General endpoint information.](https://bungie-net.github.io/multi/index.html)
        """

        return await self._client.api.get_profile(
            destiny_membership_id=destiny_membership_id,
            membership_type=self._fuzzy_getattr("membership_type"),
            components=components,
            auth=auth,
        )

    async def get_item(
        self,
        destiny_membership_id: int,
        item_instance_id: int,
        components: list["DestinyComponentType"],
        auth: Optional["AuthData"] = None,
    ) -> "DestinyItemResponse":
        """
        Retrieve the details of an instanced Destiny Item. An instanced Destiny item is one with an ItemInstanceId. Non-instanced items, such as materials, have no useful instance-specific details and thus are not queryable here.

        Args:
            destiny_membership_id: The membership ID of the destiny profile.
            item_instance_id: The Instance ID of the destiny item.
            components: A comma separated list of components to return (as strings or numeric values). See the DestinyComponentType enum for valid components to request. You must request at least one component to receive results.
            auth: Authentication information. Required when users with a private profile are queried, or when Bungie feels like it

        Returns:
            The model which is returned by bungie. [General endpoint information.](https://bungie-net.github.io/multi/index.html)
        """

        return await self._client.api.get_item(
            destiny_membership_id=destiny_membership_id,
            item_instance_id=item_instance_id,
            membership_type=self._fuzzy_getattr("membership_type"),
            components=components,
            auth=auth,
        )

    async def get_leaderboards(
        self, destiny_membership_id: int, maxtop: int, modes: str, statid: str, auth: Optional["AuthData"] = None
    ) -> dict[str, dict[str, "DestinyLeaderboard"]]:
        """
        Gets leaderboards with the signed in user's friends and the supplied destinyMembershipId as the focus. PREVIEW: This endpoint has not yet been implemented. It is being returned for a preview of future functionality, and for public comment/suggestion/preparation.

        Args:
            destiny_membership_id: The Destiny membershipId of the user to retrieve.
            maxtop: Maximum number of top players to return. Use a large number to get entire leaderboard.
            modes: List of game modes for which to get leaderboards. See the documentation for DestinyActivityModeType for valid values, and pass in string representation, comma delimited.
            statid: ID of stat to return rather than returning all Leaderboard stats.
            auth: Authentication information. Required when users with a private profile are queried, or when Bungie feels like it

        Returns:
            The model which is returned by bungie. [General endpoint information.](https://bungie-net.github.io/multi/index.html)
        """

        return await self._client.api.get_leaderboards(
            destiny_membership_id=destiny_membership_id,
            membership_type=self._fuzzy_getattr("membership_type"),
            maxtop=maxtop,
            modes=modes,
            statid=statid,
            auth=auth,
        )

    async def get_historical_stats_for_account(
        self, destiny_membership_id: int, groups: list["DestinyStatsGroupType"], auth: Optional["AuthData"] = None
    ) -> "DestinyHistoricalStatsAccountResult":
        """
        Gets aggregate historical stats organized around each character for a given account.

        Args:
            destiny_membership_id: The Destiny membershipId of the user to retrieve.
            groups: Groups of stats to include, otherwise only general stats are returned. Comma separated list is allowed. Values: General, Weapons, Medals.
            auth: Authentication information. Required when users with a private profile are queried, or when Bungie feels like it

        Returns:
            The model which is returned by bungie. [General endpoint information.](https://bungie-net.github.io/multi/index.html)
        """

        return await self._client.api.get_historical_stats_for_account(
            destiny_membership_id=destiny_membership_id,
            membership_type=self._fuzzy_getattr("membership_type"),
            groups=groups,
            auth=auth,
        )
