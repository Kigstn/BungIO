from datetime import datetime
from typing import TYPE_CHECKING, AsyncGenerator, Optional, Union

from bungio.models.base import ClientMixin, FuzzyAttrFinder, custom_define

if TYPE_CHECKING:
    # AUTOMATIC IMPORTS START
    from bungio.models import GroupPotentialMembershipSearchResponse
    from bungio.models import UserMembershipData
    from bungio.models import DestinyLinkedProfilesResponse
    from bungio.models import BungieRewardDisplay
    from bungio.models import GroupApplicationResponse
    from bungio.models import GetGroupsForMemberResponse
    from bungio.models import RuntimeGroupMemberType
    from bungio.models import DestinyProfileResponse
    from bungio.models import DestinyItemResponse
    from bungio.models import GroupMemberLeaveResult
    from bungio.models import GroupApplicationRequest
    from bungio.models import DestinyHistoricalStatsAccountResult
    from bungio.models import GroupsForMemberFilter
    from bungio.models import GroupBanRequest
    from bungio.models import DestinyComponentType
    from bungio.models import GroupType
    from bungio.models import DestinyLeaderboard
    from bungio.models import GroupMembershipSearchResponse
    from bungio.models import DestinyStatsGroupType
    from bungio.models import GroupPotentialMemberStatus

    # AUTOMATIC IMPORTS END
    from bungio.models.auth import AuthData
    from bungio.models.bungie import DestinyActivityModeType
    from bungio.models.overwrites import DestinyHistoricalStatsPeriodGroup


__all__ = ("DestinyUserMixin",)


@custom_define()
class DestinyUserMixin(ClientMixin, FuzzyAttrFinder):
    @property
    def full_bungie_name(self) -> str:
        """
        Return the formatted bungie name like it is seen in-game. This includes the four numbers

        Returns:
            The full bungie name
        """

        return f"""{self.bungie_global_display_name}#{str(self.bungie_global_display_name_code).zfill(4)}"""

    async def yield_activity_history(
        self,
        mode: Union["DestinyActivityModeType", int],
        earliest_allowed_datetime: Optional[datetime] = None,
        latest_allowed_datetime: Optional[datetime] = None,
        auth: Optional["AuthData"] = None,
    ) -> AsyncGenerator["DestinyHistoricalStatsPeriodGroup", None]:
        """
        Yields account activity history, no matter the character. Sorted by date descending, the latest one first.

        Args:
            mode: A filter for the activity mode to be returned. None returns all activities. See the documentation for DestinyActivityModeType for valid values, and pass in string representation.
            earliest_allowed_datetime: The earliest time the activity is allowed to have, fe. only entries after the 1/1/2020.
            latest_allowed_datetime: The latest time the activity is allowed to have, fe. only entries before the 1/1/2020.
            auth: Authentication information. Required when users with a private profile are queried, or when Bungie feels like it

        Returns:
            A generator for the model which is returned by bungie. [General endpoint information.](https://bungie-net.github.io/multi/index.html)
        """
        from bungio.models.basic import DestinyCharacter

        # get character ids and gen functions
        # use the stats page to also get deleted chars
        data = await self.get_historical_stats_for_account(groups=[0], auth=auth)

        characters = [
            DestinyCharacter(
                membership_id=self._fuzzy_getattr("membership_id"),
                membership_type=self._fuzzy_getattr("membership_type"),
                character_id=character.character_id,
            )
            for character in data.characters
        ]

        funcs = {
            i: character.yield_activity_history(
                mode=mode,
                earliest_allowed_datetime=earliest_allowed_datetime,
                latest_allowed_datetime=latest_allowed_datetime,
                auth=auth,
            )
            for i, character in enumerate(characters)
        }

        # gen the first values
        entries = {i: await anext(func, None) for i, func in funcs.items()}

        # loop through all generators and return the newest values
        while True:
            # calculate the newest entry
            newest: Optional["DestinyHistoricalStatsPeriodGroup"] = None
            newest_index: int = 0
            for i, entry in entries.items():
                if entry is not None and (newest is None or entry.period > newest.period):
                    newest = entry
                    newest_index = i

            if newest:
                yield newest

                # get a new value from the func that just yielded
                entries[newest_index] = await anext(funcs[newest_index], None)
            else:
                break

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
        self, group_id: int, member_type: Union["RuntimeGroupMemberType", int], auth: "AuthData"
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
        self,
        filter: Union["GroupsForMemberFilter", int],
        group_type: Union["GroupType", int],
        auth: Optional["AuthData"] = None,
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
        self, group_type: Union["GroupType", int], auth: Optional["AuthData"] = None
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
        self,
        filter: Union["GroupPotentialMemberStatus", int],
        group_type: Union["GroupType", int],
        auth: Optional["AuthData"] = None,
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

    async def get_bungie_rewards_for_platform_user(self, auth: "AuthData") -> dict[str, "BungieRewardDisplay"]:
        """
        Returns the bungie rewards for the targeted user when a platform membership Id and Type are used.

        Warning: Requires Authentication.
            Required oauth2 scopes: ReadAndApplyTokens

        Args:
            auth: Authentication information.

        Returns:
            The model which is returned by bungie. [General endpoint information.](https://bungie-net.github.io/multi/index.html)
        """

        return await self._client.api.get_bungie_rewards_for_platform_user(
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
        self, components: list[Union["DestinyComponentType", int]], auth: Optional["AuthData"] = None
    ) -> "DestinyProfileResponse":
        """
        Returns Destiny Profile information for the supplied membership.

        Args:
            components: A comma separated list of components to return (as strings or numeric values). See the DestinyComponentType enum for valid components to request. You must request at least one component to receive results.
            auth: Authentication information. Required when users with a private profile are queried, or when Bungie feels like it

        Returns:
            The model which is returned by bungie. [General endpoint information.](https://bungie-net.github.io/multi/index.html)
        """

        return await self._client.api.get_profile(
            destiny_membership_id=self._fuzzy_getattr("membership_id"),
            membership_type=self._fuzzy_getattr("membership_type"),
            components=components,
            auth=auth,
        )

    async def get_item(
        self,
        item_instance_id: int,
        components: list[Union["DestinyComponentType", int]],
        auth: Optional["AuthData"] = None,
    ) -> "DestinyItemResponse":
        """
        Retrieve the details of an instanced Destiny Item. An instanced Destiny item is one with an ItemInstanceId. Non-instanced items, such as materials, have no useful instance-specific details and thus are not queryable here.

        Args:
            item_instance_id: The Instance ID of the destiny item.
            components: A comma separated list of components to return (as strings or numeric values). See the DestinyComponentType enum for valid components to request. You must request at least one component to receive results.
            auth: Authentication information. Required when users with a private profile are queried, or when Bungie feels like it

        Returns:
            The model which is returned by bungie. [General endpoint information.](https://bungie-net.github.io/multi/index.html)
        """

        return await self._client.api.get_item(
            destiny_membership_id=self._fuzzy_getattr("membership_id"),
            item_instance_id=item_instance_id,
            membership_type=self._fuzzy_getattr("membership_type"),
            components=components,
            auth=auth,
        )

    async def get_leaderboards(
        self, maxtop: int, modes: str, statid: str, auth: Optional["AuthData"] = None
    ) -> dict[str, dict[str, "DestinyLeaderboard"]]:
        """
        Gets leaderboards with the signed in user's friends and the supplied destinyMembershipId as the focus. PREVIEW: This endpoint has not yet been implemented. It is being returned for a preview of future functionality, and for public comment/suggestion/preparation.

        Args:
            maxtop: Maximum number of top players to return. Use a large number to get entire leaderboard.
            modes: List of game modes for which to get leaderboards. See the documentation for DestinyActivityModeType for valid values, and pass in string representation, comma delimited.
            statid: ID of stat to return rather than returning all Leaderboard stats.
            auth: Authentication information. Required when users with a private profile are queried, or when Bungie feels like it

        Returns:
            The model which is returned by bungie. [General endpoint information.](https://bungie-net.github.io/multi/index.html)
        """

        return await self._client.api.get_leaderboards(
            destiny_membership_id=self._fuzzy_getattr("membership_id"),
            membership_type=self._fuzzy_getattr("membership_type"),
            maxtop=maxtop,
            modes=modes,
            statid=statid,
            auth=auth,
        )

    async def get_historical_stats_for_account(
        self, groups: list[Union["DestinyStatsGroupType", int]], auth: Optional["AuthData"] = None
    ) -> "DestinyHistoricalStatsAccountResult":
        """
        Gets aggregate historical stats organized around each character for a given account.

        Args:
            groups: Groups of stats to include, otherwise only general stats are returned. Comma separated list is allowed. Values: General, Weapons, Medals.
            auth: Authentication information. Required when users with a private profile are queried, or when Bungie feels like it

        Returns:
            The model which is returned by bungie. [General endpoint information.](https://bungie-net.github.io/multi/index.html)
        """

        return await self._client.api.get_historical_stats_for_account(
            destiny_membership_id=self._fuzzy_getattr("membership_id"),
            membership_type=self._fuzzy_getattr("membership_type"),
            groups=groups,
            auth=auth,
        )
