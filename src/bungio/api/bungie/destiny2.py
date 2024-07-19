# DO NOT CHANGE ANY CODE BELOW
# This file is generated automatically by `generate_api_schema.py` and will be overwritten
# Instead, change functions / models by subclassing them in the `./overwrites/` folder. They will be used instead.

from datetime import datetime
from typing import Optional, Union

from bungio.models.base import ClientMixin, custom_define
from bungio.models.auth import AuthData
from bungio.utils import AllowAsyncIteration

from bungio.models import DestinyItemTransferRequest
from bungio.models import DestinyPublicVendorsResponse
from bungio.models import DestinyPublicMilestone
from bungio.models import DestinyInsertPlugsFreeActionRequest
from bungio.models import DestinyLoadoutUpdateActionRequest
from bungio.models import DestinyPostGameCarnageReportData
from bungio.models import DestinyItemStateRequest
from bungio.models import DestinyItemResponse
from bungio.models import BungieMembershipType
from bungio.models import DestinyVendorResponse
from bungio.models import DestinyItemActionRequest
from bungio.models import DestinyClanAggregateStat
from bungio.models import DestinyEntitySearchResult
from bungio.models import DestinyVendorFilter
from bungio.models import DestinyEquipItemResults
from bungio.models import DestinyHistoricalStatsByPeriod
from bungio.models import AwaUserResponse
from bungio.models import DestinyCollectibleNodeDetailResponse
from bungio.models import DestinyStatsGroupType
from bungio.models import AwaInitializeResponse
from bungio.models import DestinyReportOffensePgcrRequest
from bungio.models import DestinyLoadoutActionRequest
from bungio.models import DestinyInsertPlugsActionRequest
from bungio.models import DestinyActivityHistoryResults
from bungio.models import ExactSearchRequest
from bungio.models import DestinyItemChangeResponse
from bungio.models import PeriodType
from bungio.models import DestinyAggregateActivityResults
from bungio.models import DestinyLinkedProfilesResponse
from bungio.models import DestinyVendorsResponse
from bungio.models import DestinyLeaderboard
from bungio.models import DestinyManifest
from bungio.models import AwaAuthorizationResult
from bungio.models import DestinyProfileResponse
from bungio.models import DestinyMilestoneContent
from bungio.models import DestinyCharacterResponse
from bungio.models import DestinyItemSetActionRequest
from bungio.models import DestinyHistoricalWeaponStatsData
from bungio.models import DestinyPostmasterTransferRequest
from bungio.models import DestinyComponentType
from bungio.models import UserInfoCard
from bungio.models import DestinyHistoricalStatsAccountResult
from bungio.models import DestinyHistoricalStatsDefinition
from bungio.models import AwaPermissionRequested
from bungio.models import DestinyDefinition
from bungio.models import DestinyMilestone
from bungio.models import DestinyActivityModeType


@custom_define()
class Destiny2RouteInterface(ClientMixin):
    async def get_destiny_manifest(self, auth: Optional[AuthData] = None) -> DestinyManifest:
        """
        Returns the current version of the manifest as a json object.

        Args:
            auth: Authentication information. Required when users with a private profile are queried, or when Bungie feels like it

        Returns:
            The model which is returned by bungie. [General endpoint information.](https://bungie-net.github.io/multi/index.html)
        """

        response = await self._client.http.get_destiny_manifest(auth=auth)
        return await DestinyManifest.from_dict(data=response, client=self._client, auth=auth)

    async def get_destiny_entity_definition(
        self, entity_type: str, hash_identifier: int, auth: Optional[AuthData] = None
    ) -> DestinyDefinition:
        """
        Returns the static definition of an entity of the given Type and hash identifier. Examine the API Documentation for the Type Names of entities that have their own definitions. Note that the return type will always *inherit from* DestinyDefinition, but the specific type returned will be the requested entity type if it can be found. Please don't use this as a chatty alternative to the Manifest database if you require large sets of data, but for simple and one-off accesses this should be handy.

        Args:
            entity_type: The type of entity for whom you would like results. These correspond to the entity's definition contract name. For instance, if you are looking for items, this property should be 'DestinyInventoryItemDefinition'. PREVIEW: This endpoint is still in beta, and may experience rough edges. The schema is tentatively in final form, but there may be bugs that prevent desirable operation.
            hash_identifier: The hash identifier for the specific Entity you want returned.
            auth: Authentication information. Required when users with a private profile are queried, or when Bungie feels like it

        Returns:
            The model which is returned by bungie. [General endpoint information.](https://bungie-net.github.io/multi/index.html)
        """

        response = await self._client.http.get_destiny_entity_definition(
            entity_type=entity_type, hash_identifier=hash_identifier, auth=auth
        )
        return await DestinyDefinition.from_dict(
            data=response, client=self._client, entity_type=entity_type, hash_identifier=hash_identifier, auth=auth
        )

    async def search_destiny_player_by_bungie_name(
        self,
        data: ExactSearchRequest,
        membership_type: Union[BungieMembershipType, int],
        auth: Optional[AuthData] = None,
    ) -> list[UserInfoCard]:
        """
        Returns a list of Destiny memberships given a global Bungie Display Name. This method will hide overridden memberships due to cross save.

        Args:
            data: The required data for this request.
            membership_type: A valid non-BungieNet membership type, or All. Indicates which memberships to return. You probably want this set to All.
            auth: Authentication information. Required when users with a private profile are queried, or when Bungie feels like it

        Returns:
            The model which is returned by bungie. [General endpoint information.](https://bungie-net.github.io/multi/index.html)
        """

        response = await self._client.http.search_destiny_player_by_bungie_name(
            membership_type=getattr(membership_type, "value", membership_type),
            auth=auth,
            **data.to_dict(_return_to_bungie_case=False),
        )
        return [
            await UserInfoCard.from_dict(data=value, client=self._client, membership_type=membership_type, auth=auth)
            for value in response["Response"]
        ]

    async def get_linked_profiles(
        self,
        membership_id: int,
        membership_type: Union[BungieMembershipType, int],
        get_all_memberships: Optional[bool] = None,
        auth: Optional[AuthData] = None,
    ) -> DestinyLinkedProfilesResponse:
        """
        Returns a summary information about all profiles linked to the requesting membership type/membership ID that have valid Destiny information. The passed-in Membership Type/Membership ID may be a Bungie.Net membership or a Destiny membership. It only returns the minimal amount of data to begin making more substantive requests, but will hopefully serve as a useful alternative to UserServices for people who just care about Destiny data. Note that it will only return linked accounts whose linkages you are allowed to view.

        Args:
            membership_id: The ID of the membership whose linked Destiny accounts you want returned. Make sure your membership ID matches its Membership Type: don't pass us a PSN membership ID and the XBox membership type, it's not going to work!
            membership_type: The type for the membership whose linked Destiny accounts you want returned.
            get_all_memberships: (optional) if set to 'true', all memberships regardless of whether they're obscured by overrides will be returned. Normal privacy restrictions on account linking will still apply no matter what.
            auth: Authentication information. Required when users with a private profile are queried, or when Bungie feels like it

        Returns:
            The model which is returned by bungie. [General endpoint information.](https://bungie-net.github.io/multi/index.html)
        """

        response = await self._client.http.get_linked_profiles(
            membership_id=membership_id,
            membership_type=getattr(membership_type, "value", membership_type),
            get_all_memberships=get_all_memberships if get_all_memberships is not None else None,
            auth=auth,
        )
        return await DestinyLinkedProfilesResponse.from_dict(
            data=response,
            client=self._client,
            membership_id=membership_id,
            membership_type=membership_type,
            get_all_memberships=get_all_memberships,
            auth=auth,
        )

    async def get_profile(
        self,
        destiny_membership_id: int,
        membership_type: Union[BungieMembershipType, int],
        components: Optional[list[Union[DestinyComponentType, int]]] = None,
        auth: Optional[AuthData] = None,
    ) -> DestinyProfileResponse:
        """
        Returns Destiny Profile information for the supplied membership.

        Args:
            destiny_membership_id: Destiny membership ID.
            membership_type: A valid non-BungieNet membership type.
            components: A comma separated list of components to return (as strings or numeric values). See the DestinyComponentType enum for valid components to request. You must request at least one component to receive results.
            auth: Authentication information. Required when users with a private profile are queried, or when Bungie feels like it

        Returns:
            The model which is returned by bungie. [General endpoint information.](https://bungie-net.github.io/multi/index.html)
        """

        response = await self._client.http.get_profile(
            destiny_membership_id=destiny_membership_id,
            membership_type=getattr(membership_type, "value", membership_type),
            components=[getattr(x, "value", x) for x in components] if components is not None else None,
            auth=auth,
        )
        return await DestinyProfileResponse.from_dict(
            data=response,
            client=self._client,
            destiny_membership_id=destiny_membership_id,
            membership_type=membership_type,
            components=components,
            auth=auth,
        )

    async def get_character(
        self,
        character_id: int,
        destiny_membership_id: int,
        membership_type: Union[BungieMembershipType, int],
        components: Optional[list[Union[DestinyComponentType, int]]] = None,
        auth: Optional[AuthData] = None,
    ) -> DestinyCharacterResponse:
        """
        Returns character information for the supplied character.

        Args:
            character_id: ID of the character.
            destiny_membership_id: Destiny membership ID.
            membership_type: A valid non-BungieNet membership type.
            components: A comma separated list of components to return (as strings or numeric values). See the DestinyComponentType enum for valid components to request. You must request at least one component to receive results.
            auth: Authentication information. Required when users with a private profile are queried, or when Bungie feels like it

        Returns:
            The model which is returned by bungie. [General endpoint information.](https://bungie-net.github.io/multi/index.html)
        """

        response = await self._client.http.get_character(
            character_id=character_id,
            destiny_membership_id=destiny_membership_id,
            membership_type=getattr(membership_type, "value", membership_type),
            components=[getattr(x, "value", x) for x in components] if components is not None else None,
            auth=auth,
        )
        return await DestinyCharacterResponse.from_dict(
            data=response,
            client=self._client,
            character_id=character_id,
            destiny_membership_id=destiny_membership_id,
            membership_type=membership_type,
            components=components,
            auth=auth,
        )

    async def get_clan_weekly_reward_state(self, group_id: int, auth: Optional[AuthData] = None) -> DestinyMilestone:
        """
        Returns information on the weekly clan rewards and if the clan has earned them or not. Note that this will always report rewards as not redeemed.

        Args:
            group_id: A valid group id of clan.
            auth: Authentication information. Required when users with a private profile are queried, or when Bungie feels like it

        Returns:
            The model which is returned by bungie. [General endpoint information.](https://bungie-net.github.io/multi/index.html)
        """

        response = await self._client.http.get_clan_weekly_reward_state(group_id=group_id, auth=auth)
        return await DestinyMilestone.from_dict(data=response, client=self._client, group_id=group_id, auth=auth)

    async def get_clan_banner_source(self, auth: Optional[AuthData] = None) -> dict:
        """
        Returns the dictionary of values for the Clan Banner

        Args:
            auth: Authentication information. Required when users with a private profile are queried, or when Bungie feels like it

        Returns:
            The model which is returned by bungie. [General endpoint information.](https://bungie-net.github.io/multi/index.html)
        """

        response = await self._client.http.get_clan_banner_source(auth=auth)
        return response["Response"]

    async def get_item(
        self,
        destiny_membership_id: int,
        item_instance_id: int,
        membership_type: Union[BungieMembershipType, int],
        components: Optional[list[Union[DestinyComponentType, int]]] = None,
        auth: Optional[AuthData] = None,
    ) -> DestinyItemResponse:
        """
        Retrieve the details of an instanced Destiny Item. An instanced Destiny item is one with an ItemInstanceId. Non-instanced items, such as materials, have no useful instance-specific details and thus are not queryable here.

        Args:
            destiny_membership_id: The membership ID of the destiny profile.
            item_instance_id: The Instance ID of the destiny item.
            membership_type: A valid non-BungieNet membership type.
            components: A comma separated list of components to return (as strings or numeric values). See the DestinyComponentType enum for valid components to request. You must request at least one component to receive results.
            auth: Authentication information. Required when users with a private profile are queried, or when Bungie feels like it

        Returns:
            The model which is returned by bungie. [General endpoint information.](https://bungie-net.github.io/multi/index.html)
        """

        response = await self._client.http.get_item(
            destiny_membership_id=destiny_membership_id,
            item_instance_id=item_instance_id,
            membership_type=getattr(membership_type, "value", membership_type),
            components=[getattr(x, "value", x) for x in components] if components is not None else None,
            auth=auth,
        )
        return await DestinyItemResponse.from_dict(
            data=response,
            client=self._client,
            destiny_membership_id=destiny_membership_id,
            item_instance_id=item_instance_id,
            membership_type=membership_type,
            components=components,
            auth=auth,
        )

    async def get_vendors(
        self,
        character_id: int,
        destiny_membership_id: int,
        membership_type: Union[BungieMembershipType, int],
        components: Optional[list[Union[DestinyComponentType, int]]] = None,
        filter: Optional[Union[DestinyVendorFilter, int]] = None,
        auth: Optional[AuthData] = None,
    ) -> DestinyVendorsResponse:
        """
        Get currently available vendors from the list of vendors that can possibly have rotating inventory. Note that this does not include things like preview vendors and vendors-as-kiosks, neither of whom have rotating/dynamic inventories. Use their definitions as-is for those.

        Args:
            character_id: The Destiny Character ID of the character for whom we're getting vendor info.
            destiny_membership_id: Destiny membership ID of another user. You may be denied.
            membership_type: A valid non-BungieNet membership type.
            components: A comma separated list of components to return (as strings or numeric values). See the DestinyComponentType enum for valid components to request. You must request at least one component to receive results.
            filter: The filter of what vendors and items to return, if any.
            auth: Authentication information. Required when users with a private profile are queried, or when Bungie feels like it

        Returns:
            The model which is returned by bungie. [General endpoint information.](https://bungie-net.github.io/multi/index.html)
        """

        response = await self._client.http.get_vendors(
            character_id=character_id,
            destiny_membership_id=destiny_membership_id,
            membership_type=getattr(membership_type, "value", membership_type),
            components=[getattr(x, "value", x) for x in components] if components is not None else None,
            filter=getattr(filter, "value", filter) if filter is not None else None,
            auth=auth,
        )
        return await DestinyVendorsResponse.from_dict(
            data=response,
            client=self._client,
            character_id=character_id,
            destiny_membership_id=destiny_membership_id,
            membership_type=membership_type,
            components=components,
            filter=filter,
            auth=auth,
        )

    async def get_vendor(
        self,
        character_id: int,
        destiny_membership_id: int,
        membership_type: Union[BungieMembershipType, int],
        vendor_hash: int,
        components: Optional[list[Union[DestinyComponentType, int]]] = None,
        auth: Optional[AuthData] = None,
    ) -> DestinyVendorResponse:
        """
        Get the details of a specific Vendor.

        Args:
            character_id: The Destiny Character ID of the character for whom we're getting vendor info.
            destiny_membership_id: Destiny membership ID of another user. You may be denied.
            membership_type: A valid non-BungieNet membership type.
            vendor_hash: The Hash identifier of the Vendor to be returned.
            components: A comma separated list of components to return (as strings or numeric values). See the DestinyComponentType enum for valid components to request. You must request at least one component to receive results.
            auth: Authentication information. Required when users with a private profile are queried, or when Bungie feels like it

        Returns:
            The model which is returned by bungie. [General endpoint information.](https://bungie-net.github.io/multi/index.html)
        """

        response = await self._client.http.get_vendor(
            character_id=character_id,
            destiny_membership_id=destiny_membership_id,
            membership_type=getattr(membership_type, "value", membership_type),
            vendor_hash=vendor_hash,
            components=[getattr(x, "value", x) for x in components] if components is not None else None,
            auth=auth,
        )
        return await DestinyVendorResponse.from_dict(
            data=response,
            client=self._client,
            character_id=character_id,
            destiny_membership_id=destiny_membership_id,
            membership_type=membership_type,
            vendor_hash=vendor_hash,
            components=components,
            auth=auth,
        )

    async def get_public_vendors(
        self, components: Optional[list[Union[DestinyComponentType, int]]] = None, auth: Optional[AuthData] = None
    ) -> DestinyPublicVendorsResponse:
        """
        Get items available from vendors where the vendors have items for sale that are common for everyone. If any portion of the Vendor's available inventory is character or account specific, we will be unable to return their data from this endpoint due to the way that available inventory is computed. As I am often guilty of saying: 'It's a long story...'

        Args:
            components: A comma separated list of components to return (as strings or numeric values). See the DestinyComponentType enum for valid components to request. You must request at least one component to receive results.
            auth: Authentication information. Required when users with a private profile are queried, or when Bungie feels like it

        Returns:
            The model which is returned by bungie. [General endpoint information.](https://bungie-net.github.io/multi/index.html)
        """

        response = await self._client.http.get_public_vendors(
            components=[getattr(x, "value", x) for x in components] if components is not None else None, auth=auth
        )
        return await DestinyPublicVendorsResponse.from_dict(
            data=response, client=self._client, components=components, auth=auth
        )

    async def get_collectible_node_details(
        self,
        character_id: int,
        collectible_presentation_node_hash: int,
        destiny_membership_id: int,
        membership_type: Union[BungieMembershipType, int],
        components: Optional[list[Union[DestinyComponentType, int]]] = None,
        auth: Optional[AuthData] = None,
    ) -> DestinyCollectibleNodeDetailResponse:
        """
        Given a Presentation Node that has Collectibles as direct descendants, this will return item details about those descendants in the context of the requesting character.

        Args:
            character_id: The Destiny Character ID of the character for whom we're getting collectible detail info.
            collectible_presentation_node_hash: The hash identifier of the Presentation Node for whom we should return collectible details. Details will only be returned for collectibles that are direct descendants of this node.
            destiny_membership_id: Destiny membership ID of another user. You may be denied.
            membership_type: A valid non-BungieNet membership type.
            components: A comma separated list of components to return (as strings or numeric values). See the DestinyComponentType enum for valid components to request. You must request at least one component to receive results.
            auth: Authentication information. Required when users with a private profile are queried, or when Bungie feels like it

        Returns:
            The model which is returned by bungie. [General endpoint information.](https://bungie-net.github.io/multi/index.html)
        """

        response = await self._client.http.get_collectible_node_details(
            character_id=character_id,
            collectible_presentation_node_hash=collectible_presentation_node_hash,
            destiny_membership_id=destiny_membership_id,
            membership_type=getattr(membership_type, "value", membership_type),
            components=[getattr(x, "value", x) for x in components] if components is not None else None,
            auth=auth,
        )
        return await DestinyCollectibleNodeDetailResponse.from_dict(
            data=response,
            client=self._client,
            character_id=character_id,
            collectible_presentation_node_hash=collectible_presentation_node_hash,
            destiny_membership_id=destiny_membership_id,
            membership_type=membership_type,
            components=components,
            auth=auth,
        )

    async def transfer_item(self, data: DestinyItemTransferRequest, auth: AuthData) -> int:
        """
        Transfer an item to/from your vault. You must have a valid Destiny account. You must also pass BOTH a reference AND an instance ID if it's an instanced item. itshappening.gif

        Warning: Requires Authentication.
            Required oauth2 scopes: MoveEquipDestinyItems

        Args:
            data: The required data for this request.
            auth: Authentication information.

        Returns:
            The model which is returned by bungie. [General endpoint information.](https://bungie-net.github.io/multi/index.html)
        """

        response = await self._client.http.transfer_item(auth=auth, **data.to_dict(_return_to_bungie_case=False))
        return response["Response"]

    async def pull_from_postmaster(self, data: DestinyPostmasterTransferRequest, auth: AuthData) -> int:
        """
        Extract an item from the Postmaster, with whatever implications that may entail. You must have a valid Destiny account. You must also pass BOTH a reference AND an instance ID if it's an instanced item.

        Warning: Requires Authentication.
            Required oauth2 scopes: MoveEquipDestinyItems

        Args:
            data: The required data for this request.
            auth: Authentication information.

        Returns:
            The model which is returned by bungie. [General endpoint information.](https://bungie-net.github.io/multi/index.html)
        """

        response = await self._client.http.pull_from_postmaster(auth=auth, **data.to_dict(_return_to_bungie_case=False))
        return response["Response"]

    async def equip_item(self, data: DestinyItemActionRequest, auth: AuthData) -> int:
        """
        Equip an item. You must have a valid Destiny Account, and either be in a social space, in orbit, or offline.

        Warning: Requires Authentication.
            Required oauth2 scopes: MoveEquipDestinyItems

        Args:
            data: The required data for this request.
            auth: Authentication information.

        Returns:
            The model which is returned by bungie. [General endpoint information.](https://bungie-net.github.io/multi/index.html)
        """

        response = await self._client.http.equip_item(auth=auth, **data.to_dict(_return_to_bungie_case=False))
        return response["Response"]

    async def equip_items(self, data: DestinyItemSetActionRequest, auth: AuthData) -> DestinyEquipItemResults:
        """
        Equip a list of items by itemInstanceIds. You must have a valid Destiny Account, and either be in a social space, in orbit, or offline. Any items not found on your character will be ignored.

        Warning: Requires Authentication.
            Required oauth2 scopes: MoveEquipDestinyItems

        Args:
            data: The required data for this request.
            auth: Authentication information.

        Returns:
            The model which is returned by bungie. [General endpoint information.](https://bungie-net.github.io/multi/index.html)
        """

        response = await self._client.http.equip_items(auth=auth, **data.to_dict(_return_to_bungie_case=False))
        return await DestinyEquipItemResults.from_dict(data=response, client=self._client, auth=auth)

    async def equip_loadout(self, data: DestinyLoadoutActionRequest, auth: AuthData) -> int:
        """
        Equip a loadout. You must have a valid Destiny Account, and either be in a social space, in orbit, or offline.

        Warning: Requires Authentication.
            Required oauth2 scopes: MoveEquipDestinyItems

        Args:
            data: The required data for this request.
            auth: Authentication information.

        Returns:
            The model which is returned by bungie. [General endpoint information.](https://bungie-net.github.io/multi/index.html)
        """

        response = await self._client.http.equip_loadout(auth=auth, **data.to_dict(_return_to_bungie_case=False))
        return response["Response"]

    async def snapshot_loadout(self, data: DestinyLoadoutUpdateActionRequest, auth: AuthData) -> int:
        """
        Snapshot a loadout with the currently equipped items.

        Warning: Requires Authentication.
            Required oauth2 scopes: MoveEquipDestinyItems

        Args:
            data: The required data for this request.
            auth: Authentication information.

        Returns:
            The model which is returned by bungie. [General endpoint information.](https://bungie-net.github.io/multi/index.html)
        """

        response = await self._client.http.snapshot_loadout(auth=auth, **data.to_dict(_return_to_bungie_case=False))
        return response["Response"]

    async def update_loadout_identifiers(self, data: DestinyLoadoutUpdateActionRequest, auth: AuthData) -> int:
        """
        Update the color, icon, and name of a loadout.

        Warning: Requires Authentication.
            Required oauth2 scopes: MoveEquipDestinyItems

        Args:
            data: The required data for this request.
            auth: Authentication information.

        Returns:
            The model which is returned by bungie. [General endpoint information.](https://bungie-net.github.io/multi/index.html)
        """

        response = await self._client.http.update_loadout_identifiers(
            auth=auth, **data.to_dict(_return_to_bungie_case=False)
        )
        return response["Response"]

    async def clear_loadout(self, data: DestinyLoadoutActionRequest, auth: AuthData) -> int:
        """
        Clear the identifiers and items of a loadout.

        Warning: Requires Authentication.
            Required oauth2 scopes: MoveEquipDestinyItems

        Args:
            data: The required data for this request.
            auth: Authentication information.

        Returns:
            The model which is returned by bungie. [General endpoint information.](https://bungie-net.github.io/multi/index.html)
        """

        response = await self._client.http.clear_loadout(auth=auth, **data.to_dict(_return_to_bungie_case=False))
        return response["Response"]

    async def set_item_lock_state(self, data: DestinyItemStateRequest, auth: AuthData) -> int:
        """
        Set the Lock State for an instanced item. You must have a valid Destiny Account.

        Warning: Requires Authentication.
            Required oauth2 scopes: MoveEquipDestinyItems

        Args:
            data: The required data for this request.
            auth: Authentication information.

        Returns:
            The model which is returned by bungie. [General endpoint information.](https://bungie-net.github.io/multi/index.html)
        """

        response = await self._client.http.set_item_lock_state(auth=auth, **data.to_dict(_return_to_bungie_case=False))
        return response["Response"]

    async def set_quest_tracked_state(self, data: DestinyItemStateRequest, auth: AuthData) -> int:
        """
        Set the Tracking State for an instanced item, if that item is a Quest or Bounty. You must have a valid Destiny Account. Yeah, it's an item.

        Warning: Requires Authentication.
            Required oauth2 scopes: MoveEquipDestinyItems

        Args:
            data: The required data for this request.
            auth: Authentication information.

        Returns:
            The model which is returned by bungie. [General endpoint information.](https://bungie-net.github.io/multi/index.html)
        """

        response = await self._client.http.set_quest_tracked_state(
            auth=auth, **data.to_dict(_return_to_bungie_case=False)
        )
        return response["Response"]

    async def insert_socket_plug(
        self, data: DestinyInsertPlugsActionRequest, auth: AuthData
    ) -> DestinyItemChangeResponse:
        """
        Insert a plug into a socketed item. I know how it sounds, but I assure you it's much more G-rated than you might be guessing. We haven't decided yet whether this will be able to insert plugs that have side effects, but if we do it will require special scope permission for an application attempting to do so. You must have a valid Destiny Account, and either be in a social space, in orbit, or offline. Request must include proof of permission for 'InsertPlugs' from the account owner.

        Warning: Requires Authentication.
            Required oauth2 scopes: AdvancedWriteActions

        Args:
            data: The required data for this request.
            auth: Authentication information.

        Returns:
            The model which is returned by bungie. [General endpoint information.](https://bungie-net.github.io/multi/index.html)
        """

        response = await self._client.http.insert_socket_plug(auth=auth, **data.to_dict(_return_to_bungie_case=False))
        return await DestinyItemChangeResponse.from_dict(data=response, client=self._client, auth=auth)

    async def insert_socket_plug_free(
        self, data: DestinyInsertPlugsFreeActionRequest, auth: AuthData
    ) -> DestinyItemChangeResponse:
        """
        Insert a 'free' plug into an item's socket. This does not require 'Advanced Write Action' authorization and is available to 3rd-party apps, but will only work on 'free and reversible' socket actions (Perks, Armor Mods, Shaders, Ornaments, etc.). You must have a valid Destiny Account, and the character must either be in a social space, in orbit, or offline.

        Warning: Requires Authentication.
            Required oauth2 scopes: MoveEquipDestinyItems

        Args:
            data: The required data for this request.
            auth: Authentication information.

        Returns:
            The model which is returned by bungie. [General endpoint information.](https://bungie-net.github.io/multi/index.html)
        """

        response = await self._client.http.insert_socket_plug_free(
            auth=auth, **data.to_dict(_return_to_bungie_case=False)
        )
        return await DestinyItemChangeResponse.from_dict(data=response, client=self._client, auth=auth)

    async def get_post_game_carnage_report(
        self, activity_id: int, auth: Optional[AuthData] = None
    ) -> DestinyPostGameCarnageReportData:
        """
        Gets the available post game carnage report for the activity ID.

        Args:
            activity_id: The ID of the activity whose PGCR is requested.
            auth: Authentication information. Required when users with a private profile are queried, or when Bungie feels like it

        Returns:
            The model which is returned by bungie. [General endpoint information.](https://bungie-net.github.io/multi/index.html)
        """

        response = await self._client.http.get_post_game_carnage_report(activity_id=activity_id, auth=auth)
        return await DestinyPostGameCarnageReportData.from_dict(
            data=response, client=self._client, activity_id=activity_id, auth=auth
        )

    async def report_offensive_post_game_carnage_report_player(
        self, data: DestinyReportOffensePgcrRequest, activity_id: int, auth: AuthData
    ) -> int:
        """
        Report a player that you met in an activity that was engaging in ToS-violating activities. Both you and the offending player must have played in the activityId passed in. Please use this judiciously and only when you have strong suspicions of violation, pretty please.

        Warning: Requires Authentication.
            Required oauth2 scopes: BnetWrite

        Args:
            data: The required data for this request.
            activity_id: The ID of the activity where you ran into the brigand that you're reporting.
            auth: Authentication information.

        Returns:
            The model which is returned by bungie. [General endpoint information.](https://bungie-net.github.io/multi/index.html)
        """

        response = await self._client.http.report_offensive_post_game_carnage_report_player(
            activity_id=activity_id, auth=auth, **data.to_dict(_return_to_bungie_case=False)
        )
        return response["Response"]

    async def get_historical_stats_definition(
        self, auth: Optional[AuthData] = None
    ) -> dict[str, DestinyHistoricalStatsDefinition]:
        """
        Gets historical stats definitions.

        Args:
            auth: Authentication information. Required when users with a private profile are queried, or when Bungie feels like it

        Returns:
            The model which is returned by bungie. [General endpoint information.](https://bungie-net.github.io/multi/index.html)
        """

        response = await self._client.http.get_historical_stats_definition(auth=auth)
        return {
            key: await DestinyHistoricalStatsDefinition.from_dict(data=value, client=self._client, auth=auth)
            async for key, value in AllowAsyncIteration(response["Response"].items())
        }

    async def get_clan_leaderboards(
        self,
        group_id: int,
        maxtop: Optional[int] = None,
        modes: Optional[str] = None,
        statid: Optional[str] = None,
        auth: Optional[AuthData] = None,
    ) -> dict[str, dict[str, DestinyLeaderboard]]:
        """
        Gets leaderboards with the signed in user's friends and the supplied destinyMembershipId as the focus. PREVIEW: This endpoint is still in beta, and may experience rough edges. The schema is in final form, but there may be bugs that prevent desirable operation.

        Args:
            group_id: Group ID of the clan whose leaderboards you wish to fetch.
            maxtop: Maximum number of top players to return. Use a large number to get entire leaderboard.
            modes: List of game modes for which to get leaderboards. See the documentation for DestinyActivityModeType for valid values, and pass in string representation, comma delimited.
            statid: ID of stat to return rather than returning all Leaderboard stats.
            auth: Authentication information. Required when users with a private profile are queried, or when Bungie feels like it

        Returns:
            The model which is returned by bungie. [General endpoint information.](https://bungie-net.github.io/multi/index.html)
        """

        response = await self._client.http.get_clan_leaderboards(
            group_id=group_id,
            maxtop=maxtop if maxtop is not None else None,
            modes=modes if modes is not None else None,
            statid=statid if statid is not None else None,
            auth=auth,
        )
        return {
            key: {
                key2: await DestinyLeaderboard.from_dict(
                    data=value2,
                    client=self._client,
                    group_id=group_id,
                    maxtop=maxtop,
                    modes=modes,
                    statid=statid,
                    auth=auth,
                )
                async for key2, value2 in AllowAsyncIteration(value.items())
            }
            async for key, value in AllowAsyncIteration(response["Response"].items())
        }

    async def get_clan_aggregate_stats(
        self, group_id: int, modes: Optional[str] = None, auth: Optional[AuthData] = None
    ) -> list[DestinyClanAggregateStat]:
        """
        Gets aggregated stats for a clan using the same categories as the clan leaderboards. PREVIEW: This endpoint is still in beta, and may experience rough edges. The schema is in final form, but there may be bugs that prevent desirable operation.

        Args:
            group_id: Group ID of the clan whose leaderboards you wish to fetch.
            modes: List of game modes for which to get leaderboards. See the documentation for DestinyActivityModeType for valid values, and pass in string representation, comma delimited.
            auth: Authentication information. Required when users with a private profile are queried, or when Bungie feels like it

        Returns:
            The model which is returned by bungie. [General endpoint information.](https://bungie-net.github.io/multi/index.html)
        """

        response = await self._client.http.get_clan_aggregate_stats(
            group_id=group_id, modes=modes if modes is not None else None, auth=auth
        )
        return [
            await DestinyClanAggregateStat.from_dict(
                data=value, client=self._client, group_id=group_id, modes=modes, auth=auth
            )
            for value in response["Response"]
        ]

    async def get_leaderboards(
        self,
        destiny_membership_id: int,
        membership_type: Union[BungieMembershipType, int],
        maxtop: Optional[int] = None,
        modes: Optional[str] = None,
        statid: Optional[str] = None,
        auth: Optional[AuthData] = None,
    ) -> dict[str, dict[str, DestinyLeaderboard]]:
        """
        Gets leaderboards with the signed in user's friends and the supplied destinyMembershipId as the focus. PREVIEW: This endpoint has not yet been implemented. It is being returned for a preview of future functionality, and for public comment/suggestion/preparation.

        Args:
            destiny_membership_id: The Destiny membershipId of the user to retrieve.
            membership_type: A valid non-BungieNet membership type.
            maxtop: Maximum number of top players to return. Use a large number to get entire leaderboard.
            modes: List of game modes for which to get leaderboards. See the documentation for DestinyActivityModeType for valid values, and pass in string representation, comma delimited.
            statid: ID of stat to return rather than returning all Leaderboard stats.
            auth: Authentication information. Required when users with a private profile are queried, or when Bungie feels like it

        Returns:
            The model which is returned by bungie. [General endpoint information.](https://bungie-net.github.io/multi/index.html)
        """

        response = await self._client.http.get_leaderboards(
            destiny_membership_id=destiny_membership_id,
            membership_type=getattr(membership_type, "value", membership_type),
            maxtop=maxtop if maxtop is not None else None,
            modes=modes if modes is not None else None,
            statid=statid if statid is not None else None,
            auth=auth,
        )
        return {
            key: {
                key2: await DestinyLeaderboard.from_dict(
                    data=value2,
                    client=self._client,
                    destiny_membership_id=destiny_membership_id,
                    membership_type=membership_type,
                    maxtop=maxtop,
                    modes=modes,
                    statid=statid,
                    auth=auth,
                )
                async for key2, value2 in AllowAsyncIteration(value.items())
            }
            async for key, value in AllowAsyncIteration(response["Response"].items())
        }

    async def get_leaderboards_for_character(
        self,
        character_id: int,
        destiny_membership_id: int,
        membership_type: Union[BungieMembershipType, int],
        maxtop: Optional[int] = None,
        modes: Optional[str] = None,
        statid: Optional[str] = None,
        auth: Optional[AuthData] = None,
    ) -> dict[str, dict[str, DestinyLeaderboard]]:
        """
        Gets leaderboards with the signed in user's friends and the supplied destinyMembershipId as the focus. PREVIEW: This endpoint is still in beta, and may experience rough edges. The schema is in final form, but there may be bugs that prevent desirable operation.

        Args:
            character_id: The specific character to build the leaderboard around for the provided Destiny Membership.
            destiny_membership_id: The Destiny membershipId of the user to retrieve.
            membership_type: A valid non-BungieNet membership type.
            maxtop: Maximum number of top players to return. Use a large number to get entire leaderboard.
            modes: List of game modes for which to get leaderboards. See the documentation for DestinyActivityModeType for valid values, and pass in string representation, comma delimited.
            statid: ID of stat to return rather than returning all Leaderboard stats.
            auth: Authentication information. Required when users with a private profile are queried, or when Bungie feels like it

        Returns:
            The model which is returned by bungie. [General endpoint information.](https://bungie-net.github.io/multi/index.html)
        """

        response = await self._client.http.get_leaderboards_for_character(
            character_id=character_id,
            destiny_membership_id=destiny_membership_id,
            membership_type=getattr(membership_type, "value", membership_type),
            maxtop=maxtop if maxtop is not None else None,
            modes=modes if modes is not None else None,
            statid=statid if statid is not None else None,
            auth=auth,
        )
        return {
            key: {
                key2: await DestinyLeaderboard.from_dict(
                    data=value2,
                    client=self._client,
                    character_id=character_id,
                    destiny_membership_id=destiny_membership_id,
                    membership_type=membership_type,
                    maxtop=maxtop,
                    modes=modes,
                    statid=statid,
                    auth=auth,
                )
                async for key2, value2 in AllowAsyncIteration(value.items())
            }
            async for key, value in AllowAsyncIteration(response["Response"].items())
        }

    async def search_destiny_entities(
        self, search_term: str, type: str, page: Optional[int] = None, auth: Optional[AuthData] = None
    ) -> DestinyEntitySearchResult:
        """
        Gets a page list of Destiny items.

        Args:
            search_term: The string to use when searching for Destiny entities.
            type: The type of entity for whom you would like results. These correspond to the entity's definition contract name. For instance, if you are looking for items, this property should be 'DestinyInventoryItemDefinition'.
            page: Page number to return, starting with 0.
            auth: Authentication information. Required when users with a private profile are queried, or when Bungie feels like it

        Returns:
            The model which is returned by bungie. [General endpoint information.](https://bungie-net.github.io/multi/index.html)
        """

        response = await self._client.http.search_destiny_entities(
            search_term=search_term, type=type, page=page if page is not None else None, auth=auth
        )
        return await DestinyEntitySearchResult.from_dict(
            data=response, client=self._client, search_term=search_term, type=type, page=page, auth=auth
        )

    async def get_historical_stats(
        self,
        character_id: int,
        destiny_membership_id: int,
        membership_type: Union[BungieMembershipType, int],
        dayend: Optional[datetime] = None,
        daystart: Optional[datetime] = None,
        groups: Optional[list[Union[DestinyStatsGroupType, int]]] = None,
        modes: Optional[list[Union[DestinyActivityModeType, int]]] = None,
        period_type: Optional[Union[PeriodType, int]] = None,
        auth: Optional[AuthData] = None,
    ) -> dict[str, DestinyHistoricalStatsByPeriod]:
        """
        Gets historical stats for indicated character.

        Args:
            character_id: The id of the character to retrieve. You can omit this character ID or set it to 0 to get aggregate stats across all characters.
            destiny_membership_id: The Destiny membershipId of the user to retrieve.
            membership_type: A valid non-BungieNet membership type.
            dayend: Last day to return when daily stats are requested. Use the format YYYY-MM-DD. Currently, we cannot allow more than 31 days of daily data to be requested in a single request.
            daystart: First day to return when daily stats are requested. Use the format YYYY-MM-DD. Currently, we cannot allow more than 31 days of daily data to be requested in a single request.
            groups: Group of stats to include, otherwise only general stats are returned. Comma separated list is allowed. Values: General, Weapons, Medals
            modes: Game modes to return. See the documentation for DestinyActivityModeType for valid values, and pass in string representation, comma delimited.
            period_type: Indicates a specific period type to return. Optional. May be: Daily, AllTime, or Activity
            auth: Authentication information. Required when users with a private profile are queried, or when Bungie feels like it

        Returns:
            The model which is returned by bungie. [General endpoint information.](https://bungie-net.github.io/multi/index.html)
        """

        response = await self._client.http.get_historical_stats(
            character_id=character_id,
            destiny_membership_id=destiny_membership_id,
            membership_type=getattr(membership_type, "value", membership_type),
            dayend=dayend if dayend is not None else None,
            daystart=daystart if daystart is not None else None,
            groups=[getattr(x, "value", x) for x in groups] if groups is not None else None,
            modes=[getattr(x, "value", x) for x in modes] if modes is not None else None,
            period_type=getattr(period_type, "value", period_type) if period_type is not None else None,
            auth=auth,
        )
        return {
            key: await DestinyHistoricalStatsByPeriod.from_dict(
                data=value,
                client=self._client,
                character_id=character_id,
                destiny_membership_id=destiny_membership_id,
                membership_type=membership_type,
                dayend=dayend,
                daystart=daystart,
                groups=groups,
                modes=modes,
                period_type=period_type,
                auth=auth,
            )
            async for key, value in AllowAsyncIteration(response["Response"].items())
        }

    async def get_historical_stats_for_account(
        self,
        destiny_membership_id: int,
        membership_type: Union[BungieMembershipType, int],
        groups: Optional[list[Union[DestinyStatsGroupType, int]]] = None,
        auth: Optional[AuthData] = None,
    ) -> DestinyHistoricalStatsAccountResult:
        """
        Gets aggregate historical stats organized around each character for a given account.

        Args:
            destiny_membership_id: The Destiny membershipId of the user to retrieve.
            membership_type: A valid non-BungieNet membership type.
            groups: Groups of stats to include, otherwise only general stats are returned. Comma separated list is allowed. Values: General, Weapons, Medals.
            auth: Authentication information. Required when users with a private profile are queried, or when Bungie feels like it

        Returns:
            The model which is returned by bungie. [General endpoint information.](https://bungie-net.github.io/multi/index.html)
        """

        response = await self._client.http.get_historical_stats_for_account(
            destiny_membership_id=destiny_membership_id,
            membership_type=getattr(membership_type, "value", membership_type),
            groups=[getattr(x, "value", x) for x in groups] if groups is not None else None,
            auth=auth,
        )
        return await DestinyHistoricalStatsAccountResult.from_dict(
            data=response,
            client=self._client,
            destiny_membership_id=destiny_membership_id,
            membership_type=membership_type,
            groups=groups,
            auth=auth,
        )

    async def get_activity_history(
        self,
        character_id: int,
        destiny_membership_id: int,
        membership_type: Union[BungieMembershipType, int],
        count: Optional[int] = None,
        mode: Optional[Union[DestinyActivityModeType, int]] = None,
        page: Optional[int] = None,
        auth: Optional[AuthData] = None,
    ) -> DestinyActivityHistoryResults:
        """
        Gets activity history stats for indicated character.

        Args:
            character_id: The id of the character to retrieve.
            destiny_membership_id: The Destiny membershipId of the user to retrieve.
            membership_type: A valid non-BungieNet membership type.
            count: Number of rows to return
            mode: A filter for the activity mode to be returned. None returns all activities. See the documentation for DestinyActivityModeType for valid values, and pass in string representation.
            page: Page number to return, starting with 0.
            auth: Authentication information. Required when users with a private profile are queried, or when Bungie feels like it

        Returns:
            The model which is returned by bungie. [General endpoint information.](https://bungie-net.github.io/multi/index.html)
        """

        response = await self._client.http.get_activity_history(
            character_id=character_id,
            destiny_membership_id=destiny_membership_id,
            membership_type=getattr(membership_type, "value", membership_type),
            count=count if count is not None else None,
            mode=getattr(mode, "value", mode) if mode is not None else None,
            page=page if page is not None else None,
            auth=auth,
        )
        return await DestinyActivityHistoryResults.from_dict(
            data=response,
            client=self._client,
            character_id=character_id,
            destiny_membership_id=destiny_membership_id,
            membership_type=membership_type,
            count=count,
            mode=mode,
            page=page,
            auth=auth,
        )

    async def get_unique_weapon_history(
        self,
        character_id: int,
        destiny_membership_id: int,
        membership_type: Union[BungieMembershipType, int],
        auth: Optional[AuthData] = None,
    ) -> DestinyHistoricalWeaponStatsData:
        """
        Gets details about unique weapon usage, including all exotic weapons.

        Args:
            character_id: The id of the character to retrieve.
            destiny_membership_id: The Destiny membershipId of the user to retrieve.
            membership_type: A valid non-BungieNet membership type.
            auth: Authentication information. Required when users with a private profile are queried, or when Bungie feels like it

        Returns:
            The model which is returned by bungie. [General endpoint information.](https://bungie-net.github.io/multi/index.html)
        """

        response = await self._client.http.get_unique_weapon_history(
            character_id=character_id,
            destiny_membership_id=destiny_membership_id,
            membership_type=getattr(membership_type, "value", membership_type),
            auth=auth,
        )
        return await DestinyHistoricalWeaponStatsData.from_dict(
            data=response,
            client=self._client,
            character_id=character_id,
            destiny_membership_id=destiny_membership_id,
            membership_type=membership_type,
            auth=auth,
        )

    async def get_destiny_aggregate_activity_stats(
        self,
        character_id: int,
        destiny_membership_id: int,
        membership_type: Union[BungieMembershipType, int],
        auth: Optional[AuthData] = None,
    ) -> DestinyAggregateActivityResults:
        """
        Gets all activities the character has participated in together with aggregate statistics for those activities.

        Args:
            character_id: The specific character whose activities should be returned.
            destiny_membership_id: The Destiny membershipId of the user to retrieve.
            membership_type: A valid non-BungieNet membership type.
            auth: Authentication information. Required when users with a private profile are queried, or when Bungie feels like it

        Returns:
            The model which is returned by bungie. [General endpoint information.](https://bungie-net.github.io/multi/index.html)
        """

        response = await self._client.http.get_destiny_aggregate_activity_stats(
            character_id=character_id,
            destiny_membership_id=destiny_membership_id,
            membership_type=getattr(membership_type, "value", membership_type),
            auth=auth,
        )
        return await DestinyAggregateActivityResults.from_dict(
            data=response,
            client=self._client,
            character_id=character_id,
            destiny_membership_id=destiny_membership_id,
            membership_type=membership_type,
            auth=auth,
        )

    async def get_public_milestone_content(
        self, milestone_hash: int, auth: Optional[AuthData] = None
    ) -> DestinyMilestoneContent:
        """
        Gets custom localized content for the milestone of the given hash, if it exists.

        Args:
            milestone_hash: The identifier for the milestone to be returned.
            auth: Authentication information. Required when users with a private profile are queried, or when Bungie feels like it

        Returns:
            The model which is returned by bungie. [General endpoint information.](https://bungie-net.github.io/multi/index.html)
        """

        response = await self._client.http.get_public_milestone_content(milestone_hash=milestone_hash, auth=auth)
        return await DestinyMilestoneContent.from_dict(
            data=response, client=self._client, milestone_hash=milestone_hash, auth=auth
        )

    async def get_public_milestones(self, auth: Optional[AuthData] = None) -> dict[int, DestinyPublicMilestone]:
        """
        Gets public information about currently available Milestones.

        Args:
            auth: Authentication information. Required when users with a private profile are queried, or when Bungie feels like it

        Returns:
            The model which is returned by bungie. [General endpoint information.](https://bungie-net.github.io/multi/index.html)
        """

        response = await self._client.http.get_public_milestones(auth=auth)
        return {
            key: await DestinyPublicMilestone.from_dict(data=value, client=self._client, auth=auth)
            async for key, value in AllowAsyncIteration(response["Response"].items())
        }

    async def awa_initialize_request(self, data: AwaPermissionRequested, auth: AuthData) -> AwaInitializeResponse:
        """
        Initialize a request to perform an advanced write action.

        Warning: Requires Authentication.
            Required oauth2 scopes: AdvancedWriteActions

        Args:
            data: The required data for this request.
            auth: Authentication information.

        Returns:
            The model which is returned by bungie. [General endpoint information.](https://bungie-net.github.io/multi/index.html)
        """

        response = await self._client.http.awa_initialize_request(
            auth=auth, **data.to_dict(_return_to_bungie_case=False)
        )
        return await AwaInitializeResponse.from_dict(data=response, client=self._client, auth=auth)

    async def awa_provide_authorization_result(self, data: AwaUserResponse, auth: Optional[AuthData] = None) -> int:
        """
        Provide the result of the user interaction. Called by the Bungie Destiny App to approve or reject a request.

        Args:
            data: The required data for this request.
            auth: Authentication information. Required when users with a private profile are queried, or when Bungie feels like it

        Returns:
            The model which is returned by bungie. [General endpoint information.](https://bungie-net.github.io/multi/index.html)
        """

        response = await self._client.http.awa_provide_authorization_result(
            auth=auth, **data.to_dict(_return_to_bungie_case=False)
        )
        return response["Response"]

    async def awa_get_action_token(self, correlation_id: str, auth: AuthData) -> AwaAuthorizationResult:
        """
        Returns the action token if user approves the request.

        Warning: Requires Authentication.
            Required oauth2 scopes: AdvancedWriteActions

        Args:
            correlation_id: The identifier for the advanced write action request.
            auth: Authentication information.

        Returns:
            The model which is returned by bungie. [General endpoint information.](https://bungie-net.github.io/multi/index.html)
        """

        response = await self._client.http.awa_get_action_token(correlation_id=correlation_id, auth=auth)
        return await AwaAuthorizationResult.from_dict(
            data=response, client=self._client, correlation_id=correlation_id, auth=auth
        )
