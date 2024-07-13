from datetime import datetime
from typing import Callable, Coroutine, Optional, Any, Union

from bungio.http.route import Route
from bungio.models.auth import AuthData


class Destiny2RouteHttpRequests:
    request: Callable[..., Coroutine]

    async def get_destiny_manifest(self, auth: Optional[AuthData] = None, *args, **kwargs) -> dict:
        """
        Returns the current version of the manifest as a json object.

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

        return await self.request(Route(path="/Destiny2/Manifest/", method="GET", auth=auth))

    async def get_destiny_entity_definition(
        self, entity_type: str, hash_identifier: int, auth: Optional[AuthData] = None, *args, **kwargs
    ) -> dict:
        """
        Returns the static definition of an entity of the given Type and hash identifier. Examine the API Documentation for the Type Names of entities that have their own definitions. Note that the return type will always *inherit from* DestinyDefinition, but the specific type returned will be the requested entity type if it can be found. Please don't use this as a chatty alternative to the Manifest database if you require large sets of data, but for simple and one-off accesses this should be handy.

        Args:
            entity_type: The type of entity for whom you would like results. These correspond to the entity's definition contract name. For instance, if you are looking for items, this property should be 'DestinyInventoryItemDefinition'. PREVIEW: This endpoint is still in beta, and may experience rough edges. The schema is tentatively in final form, but there may be bugs that prevent desirable operation.
            hash_identifier: The hash identifier for the specific Entity you want returned.
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
            Route(path=f"/Destiny2/Manifest/{entity_type}/{hash_identifier}/", method="GET", auth=auth)
        )

    async def search_destiny_player_by_bungie_name(
        self,
        display_name: str,
        display_name_code: int,
        membership_type: int,
        auth: Optional[AuthData] = None,
        *args,
        **kwargs,
    ) -> dict:
        """
        Returns a list of Destiny memberships given a global Bungie Display Name. This method will hide overridden memberships due to cross save.

        Args:
            display_name: _No description given by bungie._
            display_name_code: _No description given by bungie._
            membership_type: A valid non-BungieNet membership type, or All. Indicates which memberships to return. You probably want this set to All.
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
            "displayName": display_name,
            "displayNameCode": display_name_code,
        }

        return await self.request(
            Route(
                path=f"/Destiny2/SearchDestinyPlayerByBungieName/{membership_type}/",
                method="POST",
                data=data,
                auth=auth,
            )
        )

    async def get_linked_profiles(
        self,
        membership_id: int,
        membership_type: int,
        get_all_memberships: Optional[bool] = None,
        auth: Optional[AuthData] = None,
        *args,
        **kwargs,
    ) -> dict:
        """
        Returns a summary information about all profiles linked to the requesting membership type/membership ID that have valid Destiny information. The passed-in Membership Type/Membership ID may be a Bungie.Net membership or a Destiny membership. It only returns the minimal amount of data to begin making more substantive requests, but will hopefully serve as a useful alternative to UserServices for people who just care about Destiny data. Note that it will only return linked accounts whose linkages you are allowed to view.

        Args:
            membership_id: The ID of the membership whose linked Destiny accounts you want returned. Make sure your membership ID matches its Membership Type: don't pass us a PSN membership ID and the XBox membership type, it's not going to work!
            membership_type: The type for the membership whose linked Destiny accounts you want returned.
            get_all_memberships: (optional) if set to 'true', all memberships regardless of whether they're obscured by overrides will be returned. Normal privacy restrictions on account linking will still apply no matter what.
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
                path=f"/Destiny2/{membership_type}/Profile/{membership_id}/LinkedProfiles/",
                method="GET",
                get_all_memberships=get_all_memberships,
                auth=auth,
            )
        )

    async def get_profile(
        self,
        destiny_membership_id: int,
        membership_type: int,
        components: Optional[int] = None,
        auth: Optional[AuthData] = None,
        *args,
        **kwargs,
    ) -> dict:
        """
        Returns Destiny Profile information for the supplied membership.

        Args:
            destiny_membership_id: Destiny membership ID.
            membership_type: A valid non-BungieNet membership type.
            components: A comma separated list of components to return (as strings or numeric values). See the DestinyComponentType enum for valid components to request. You must request at least one component to receive results.
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
                path=f"/Destiny2/{membership_type}/Profile/{destiny_membership_id}/",
                method="GET",
                components=components,
                auth=auth,
            )
        )

    async def get_character(
        self,
        character_id: int,
        destiny_membership_id: int,
        membership_type: int,
        components: Optional[int] = None,
        auth: Optional[AuthData] = None,
        *args,
        **kwargs,
    ) -> dict:
        """
        Returns character information for the supplied character.

        Args:
            character_id: ID of the character.
            destiny_membership_id: Destiny membership ID.
            membership_type: A valid non-BungieNet membership type.
            components: A comma separated list of components to return (as strings or numeric values). See the DestinyComponentType enum for valid components to request. You must request at least one component to receive results.
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
                path=f"/Destiny2/{membership_type}/Profile/{destiny_membership_id}/Character/{character_id}/",
                method="GET",
                components=components,
                auth=auth,
            )
        )

    async def get_clan_weekly_reward_state(
        self, group_id: int, auth: Optional[AuthData] = None, *args, **kwargs
    ) -> dict:
        """
        Returns information on the weekly clan rewards and if the clan has earned them or not. Note that this will always report rewards as not redeemed.

        Args:
            group_id: A valid group id of clan.
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

        return await self.request(Route(path=f"/Destiny2/Clan/{group_id}/WeeklyRewardState/", method="GET", auth=auth))

    async def get_clan_banner_source(self, auth: Optional[AuthData] = None, *args, **kwargs) -> dict:
        """
        Returns the dictionary of values for the Clan Banner

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

        return await self.request(Route(path="/Destiny2/Clan/ClanBannerDictionary/", method="GET", auth=auth))

    async def get_item(
        self,
        destiny_membership_id: int,
        item_instance_id: int,
        membership_type: int,
        components: Optional[int] = None,
        auth: Optional[AuthData] = None,
        *args,
        **kwargs,
    ) -> dict:
        """
        Retrieve the details of an instanced Destiny Item. An instanced Destiny item is one with an ItemInstanceId. Non-instanced items, such as materials, have no useful instance-specific details and thus are not queryable here.

        Args:
            destiny_membership_id: The membership ID of the destiny profile.
            item_instance_id: The Instance ID of the destiny item.
            membership_type: A valid non-BungieNet membership type.
            components: A comma separated list of components to return (as strings or numeric values). See the DestinyComponentType enum for valid components to request. You must request at least one component to receive results.
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
                path=f"/Destiny2/{membership_type}/Profile/{destiny_membership_id}/Item/{item_instance_id}/",
                method="GET",
                components=components,
                auth=auth,
            )
        )

    async def get_vendors(
        self,
        character_id: int,
        destiny_membership_id: int,
        membership_type: int,
        components: Optional[int] = None,
        filter: Optional[int] = None,
        auth: Optional[AuthData] = None,
        *args,
        **kwargs,
    ) -> dict:
        """
        Get currently available vendors from the list of vendors that can possibly have rotating inventory. Note that this does not include things like preview vendors and vendors-as-kiosks, neither of whom have rotating/dynamic inventories. Use their definitions as-is for those.

        Args:
            character_id: The Destiny Character ID of the character for whom we're getting vendor info.
            destiny_membership_id: Destiny membership ID of another user. You may be denied.
            membership_type: A valid non-BungieNet membership type.
            components: A comma separated list of components to return (as strings or numeric values). See the DestinyComponentType enum for valid components to request. You must request at least one component to receive results.
            filter: The filter of what vendors and items to return, if any.
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
                path=f"/Destiny2/{membership_type}/Profile/{destiny_membership_id}/Character/{character_id}/Vendors/",
                method="GET",
                components=components,
                filter=filter,
                auth=auth,
            )
        )

    async def get_vendor(
        self,
        character_id: int,
        destiny_membership_id: int,
        membership_type: int,
        vendor_hash: int,
        components: Optional[int] = None,
        auth: Optional[AuthData] = None,
        *args,
        **kwargs,
    ) -> dict:
        """
        Get the details of a specific Vendor.

        Args:
            character_id: The Destiny Character ID of the character for whom we're getting vendor info.
            destiny_membership_id: Destiny membership ID of another user. You may be denied.
            membership_type: A valid non-BungieNet membership type.
            vendor_hash: The Hash identifier of the Vendor to be returned.
            components: A comma separated list of components to return (as strings or numeric values). See the DestinyComponentType enum for valid components to request. You must request at least one component to receive results.
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
                path=f"/Destiny2/{membership_type}/Profile/{destiny_membership_id}/Character/{character_id}/Vendors/{vendor_hash}/",
                method="GET",
                components=components,
                auth=auth,
            )
        )

    async def get_public_vendors(
        self, components: Optional[int] = None, auth: Optional[AuthData] = None, *args, **kwargs
    ) -> dict:
        """
        Get items available from vendors where the vendors have items for sale that are common for everyone. If any portion of the Vendor's available inventory is character or account specific, we will be unable to return their data from this endpoint due to the way that available inventory is computed. As I am often guilty of saying: 'It's a long story...'

        Args:
            components: A comma separated list of components to return (as strings or numeric values). See the DestinyComponentType enum for valid components to request. You must request at least one component to receive results.
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

        return await self.request(Route(path="/Destiny2/Vendors/", method="GET", components=components, auth=auth))

    async def get_collectible_node_details(
        self,
        character_id: int,
        collectible_presentation_node_hash: int,
        destiny_membership_id: int,
        membership_type: int,
        components: Optional[int] = None,
        auth: Optional[AuthData] = None,
        *args,
        **kwargs,
    ) -> dict:
        """
        Given a Presentation Node that has Collectibles as direct descendants, this will return item details about those descendants in the context of the requesting character.

        Args:
            character_id: The Destiny Character ID of the character for whom we're getting collectible detail info.
            collectible_presentation_node_hash: The hash identifier of the Presentation Node for whom we should return collectible details. Details will only be returned for collectibles that are direct descendants of this node.
            destiny_membership_id: Destiny membership ID of another user. You may be denied.
            membership_type: A valid non-BungieNet membership type.
            components: A comma separated list of components to return (as strings or numeric values). See the DestinyComponentType enum for valid components to request. You must request at least one component to receive results.
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
                path=f"/Destiny2/{membership_type}/Profile/{destiny_membership_id}/Character/{character_id}/Collectibles/{collectible_presentation_node_hash}/",
                method="GET",
                components=components,
                auth=auth,
            )
        )

    async def transfer_item(
        self,
        item_reference_hash: int,
        stack_size: int,
        transfer_to_vault: bool,
        item_id: int,
        character_id: int,
        membership_type: Union[Any, int],
        auth: AuthData,
        *args,
        **kwargs,
    ) -> dict:
        """
        Transfer an item to/from your vault. You must have a valid Destiny account. You must also pass BOTH a reference AND an instance ID if it's an instanced item. itshappening.gif

        Warning: Requires Authentication.
            Required oauth2 scopes: MoveEquipDestinyItems

        Args:
            item_reference_hash: _No description given by bungie._
            stack_size: _No description given by bungie._
            transfer_to_vault: _No description given by bungie._
            item_id: The instance ID of the item for this action request.
            character_id: _No description given by bungie._
            membership_type: _No description given by bungie._
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
            "itemReferenceHash": item_reference_hash,
            "stackSize": stack_size,
            "transferToVault": transfer_to_vault,
            "itemId": item_id,
            "characterId": character_id,
            "membershipType": membership_type,
        }

        return await self.request(
            Route(path="/Destiny2/Actions/Items/TransferItem/", method="POST", data=data, auth=auth)
        )

    async def pull_from_postmaster(
        self,
        item_reference_hash: int,
        stack_size: int,
        item_id: int,
        character_id: int,
        membership_type: Union[Any, int],
        auth: AuthData,
        *args,
        **kwargs,
    ) -> dict:
        """
        Extract an item from the Postmaster, with whatever implications that may entail. You must have a valid Destiny account. You must also pass BOTH a reference AND an instance ID if it's an instanced item.

        Warning: Requires Authentication.
            Required oauth2 scopes: MoveEquipDestinyItems

        Args:
            item_reference_hash: _No description given by bungie._
            stack_size: _No description given by bungie._
            item_id: The instance ID of the item for this action request.
            character_id: _No description given by bungie._
            membership_type: _No description given by bungie._
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
            "itemReferenceHash": item_reference_hash,
            "stackSize": stack_size,
            "itemId": item_id,
            "characterId": character_id,
            "membershipType": membership_type,
        }

        return await self.request(
            Route(path="/Destiny2/Actions/Items/PullFromPostmaster/", method="POST", data=data, auth=auth)
        )

    async def equip_item(
        self, item_id: int, character_id: int, membership_type: Union[Any, int], auth: AuthData, *args, **kwargs
    ) -> dict:
        """
        Equip an item. You must have a valid Destiny Account, and either be in a social space, in orbit, or offline.

        Warning: Requires Authentication.
            Required oauth2 scopes: MoveEquipDestinyItems

        Args:
            item_id: The instance ID of the item for this action request.
            character_id: _No description given by bungie._
            membership_type: _No description given by bungie._
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
            "itemId": item_id,
            "characterId": character_id,
            "membershipType": membership_type,
        }

        return await self.request(Route(path="/Destiny2/Actions/Items/EquipItem/", method="POST", data=data, auth=auth))

    async def equip_items(
        self, item_ids: list[int], character_id: int, membership_type: Union[Any, int], auth: AuthData, *args, **kwargs
    ) -> dict:
        """
        Equip a list of items by itemInstanceIds. You must have a valid Destiny Account, and either be in a social space, in orbit, or offline. Any items not found on your character will be ignored.

        Warning: Requires Authentication.
            Required oauth2 scopes: MoveEquipDestinyItems

        Args:
            item_ids: _No description given by bungie._
            character_id: _No description given by bungie._
            membership_type: _No description given by bungie._
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
            "itemIds": item_ids,
            "characterId": character_id,
            "membershipType": membership_type,
        }

        return await self.request(
            Route(path="/Destiny2/Actions/Items/EquipItems/", method="POST", data=data, auth=auth)
        )

    async def equip_loadout(
        self, loadout_index: int, character_id: int, membership_type: Union[Any, int], auth: AuthData, *args, **kwargs
    ) -> dict:
        """
        Equip a loadout. You must have a valid Destiny Account, and either be in a social space, in orbit, or offline.

        Warning: Requires Authentication.
            Required oauth2 scopes: MoveEquipDestinyItems

        Args:
            loadout_index: The index of the loadout for this action request.
            character_id: _No description given by bungie._
            membership_type: _No description given by bungie._
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
            "loadoutIndex": loadout_index,
            "characterId": character_id,
            "membershipType": membership_type,
        }

        return await self.request(
            Route(path="/Destiny2/Actions/Loadouts/EquipLoadout/", method="POST", data=data, auth=auth)
        )

    async def snapshot_loadout(
        self,
        color_hash: int,
        icon_hash: int,
        name_hash: int,
        loadout_index: int,
        character_id: int,
        membership_type: Union[Any, int],
        auth: AuthData,
        *args,
        **kwargs,
    ) -> dict:
        """
        Snapshot a loadout with the currently equipped items.

        Warning: Requires Authentication.
            Required oauth2 scopes: MoveEquipDestinyItems

        Args:
            color_hash: _No description given by bungie._
            icon_hash: _No description given by bungie._
            name_hash: _No description given by bungie._
            loadout_index: The index of the loadout for this action request.
            character_id: _No description given by bungie._
            membership_type: _No description given by bungie._
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
            "colorHash": color_hash,
            "iconHash": icon_hash,
            "nameHash": name_hash,
            "loadoutIndex": loadout_index,
            "characterId": character_id,
            "membershipType": membership_type,
        }

        return await self.request(
            Route(path="/Destiny2/Actions/Loadouts/SnapshotLoadout/", method="POST", data=data, auth=auth)
        )

    async def update_loadout_identifiers(
        self,
        color_hash: int,
        icon_hash: int,
        name_hash: int,
        loadout_index: int,
        character_id: int,
        membership_type: Union[Any, int],
        auth: AuthData,
        *args,
        **kwargs,
    ) -> dict:
        """
        Update the color, icon, and name of a loadout.

        Warning: Requires Authentication.
            Required oauth2 scopes: MoveEquipDestinyItems

        Args:
            color_hash: _No description given by bungie._
            icon_hash: _No description given by bungie._
            name_hash: _No description given by bungie._
            loadout_index: The index of the loadout for this action request.
            character_id: _No description given by bungie._
            membership_type: _No description given by bungie._
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
            "colorHash": color_hash,
            "iconHash": icon_hash,
            "nameHash": name_hash,
            "loadoutIndex": loadout_index,
            "characterId": character_id,
            "membershipType": membership_type,
        }

        return await self.request(
            Route(path="/Destiny2/Actions/Loadouts/UpdateLoadoutIdentifiers/", method="POST", data=data, auth=auth)
        )

    async def clear_loadout(
        self, loadout_index: int, character_id: int, membership_type: Union[Any, int], auth: AuthData, *args, **kwargs
    ) -> dict:
        """
        Clear the identifiers and items of a loadout.

        Warning: Requires Authentication.
            Required oauth2 scopes: MoveEquipDestinyItems

        Args:
            loadout_index: The index of the loadout for this action request.
            character_id: _No description given by bungie._
            membership_type: _No description given by bungie._
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
            "loadoutIndex": loadout_index,
            "characterId": character_id,
            "membershipType": membership_type,
        }

        return await self.request(
            Route(path="/Destiny2/Actions/Loadouts/ClearLoadout/", method="POST", data=data, auth=auth)
        )

    async def set_item_lock_state(
        self,
        state: bool,
        item_id: int,
        character_id: int,
        membership_type: Union[Any, int],
        auth: AuthData,
        *args,
        **kwargs,
    ) -> dict:
        """
        Set the Lock State for an instanced item. You must have a valid Destiny Account.

        Warning: Requires Authentication.
            Required oauth2 scopes: MoveEquipDestinyItems

        Args:
            state: _No description given by bungie._
            item_id: The instance ID of the item for this action request.
            character_id: _No description given by bungie._
            membership_type: _No description given by bungie._
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
            "state": state,
            "itemId": item_id,
            "characterId": character_id,
            "membershipType": membership_type,
        }

        return await self.request(
            Route(path="/Destiny2/Actions/Items/SetLockState/", method="POST", data=data, auth=auth)
        )

    async def set_quest_tracked_state(
        self,
        state: bool,
        item_id: int,
        character_id: int,
        membership_type: Union[Any, int],
        auth: AuthData,
        *args,
        **kwargs,
    ) -> dict:
        """
        Set the Tracking State for an instanced item, if that item is a Quest or Bounty. You must have a valid Destiny Account. Yeah, it's an item.

        Warning: Requires Authentication.
            Required oauth2 scopes: MoveEquipDestinyItems

        Args:
            state: _No description given by bungie._
            item_id: The instance ID of the item for this action request.
            character_id: _No description given by bungie._
            membership_type: _No description given by bungie._
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
            "state": state,
            "itemId": item_id,
            "characterId": character_id,
            "membershipType": membership_type,
        }

        return await self.request(
            Route(path="/Destiny2/Actions/Items/SetTrackedState/", method="POST", data=data, auth=auth)
        )

    async def insert_socket_plug(
        self,
        action_token: str,
        item_instance_id: int,
        plug: Any,
        character_id: int,
        membership_type: Union[Any, int],
        auth: AuthData,
        *args,
        **kwargs,
    ) -> dict:
        """
        Insert a plug into a socketed item. I know how it sounds, but I assure you it's much more G-rated than you might be guessing. We haven't decided yet whether this will be able to insert plugs that have side effects, but if we do it will require special scope permission for an application attempting to do so. You must have a valid Destiny Account, and either be in a social space, in orbit, or offline. Request must include proof of permission for 'InsertPlugs' from the account owner.

        Warning: Requires Authentication.
            Required oauth2 scopes: AdvancedWriteActions

        Args:
            action_token: Action token provided by the AwaGetActionToken API call.
            item_instance_id: The instance ID of the item having a plug inserted. Only instanced items can have sockets.
            plug: The plugs being inserted.
            character_id: _No description given by bungie._
            membership_type: _No description given by bungie._
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
            "actionToken": action_token,
            "itemInstanceId": item_instance_id,
            "plug": plug,
            "characterId": character_id,
            "membershipType": membership_type,
        }

        return await self.request(
            Route(path="/Destiny2/Actions/Items/InsertSocketPlug/", method="POST", data=data, auth=auth)
        )

    async def insert_socket_plug_free(
        self,
        plug: Any,
        item_id: int,
        character_id: int,
        membership_type: Union[Any, int],
        auth: AuthData,
        *args,
        **kwargs,
    ) -> dict:
        """
        Insert a 'free' plug into an item's socket. This does not require 'Advanced Write Action' authorization and is available to 3rd-party apps, but will only work on 'free and reversible' socket actions (Perks, Armor Mods, Shaders, Ornaments, etc.). You must have a valid Destiny Account, and the character must either be in a social space, in orbit, or offline.

        Warning: Requires Authentication.
            Required oauth2 scopes: MoveEquipDestinyItems

        Args:
            plug: The plugs being inserted.
            item_id: The instance ID of the item for this action request.
            character_id: _No description given by bungie._
            membership_type: _No description given by bungie._
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
            "plug": plug,
            "itemId": item_id,
            "characterId": character_id,
            "membershipType": membership_type,
        }

        return await self.request(
            Route(path="/Destiny2/Actions/Items/InsertSocketPlugFree/", method="POST", data=data, auth=auth)
        )

    async def get_post_game_carnage_report(
        self, activity_id: int, auth: Optional[AuthData] = None, *args, **kwargs
    ) -> dict:
        """
        Gets the available post game carnage report for the activity ID.

        Args:
            activity_id: The ID of the activity whose PGCR is requested.
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
            Route(path=f"/Destiny2/Stats/PostGameCarnageReport/{activity_id}/", method="GET", auth=auth)
        )

    async def report_offensive_post_game_carnage_report_player(
        self,
        reason_category_hashes: list[int],
        reason_hashes: list[int],
        offending_character_id: int,
        activity_id: int,
        auth: AuthData,
        *args,
        **kwargs,
    ) -> dict:
        """
        Report a player that you met in an activity that was engaging in ToS-violating activities. Both you and the offending player must have played in the activityId passed in. Please use this judiciously and only when you have strong suspicions of violation, pretty please.

        Warning: Requires Authentication.
            Required oauth2 scopes: BnetWrite

        Args:
            reason_category_hashes: So you've decided to report someone instead of cursing them and their descendants. Well, okay then. This is the category or categorie(s) of infractions for which you are reporting the user. These are hash identifiers that map to DestinyReportReasonCategoryDefinition entries.
            reason_hashes: If applicable, provide a more specific reason(s) within the general category of problems provided by the reasonHash. This is also an identifier for a reason. All reasonHashes provided must be children of at least one the reasonCategoryHashes provided.
            offending_character_id: Within the PGCR provided when calling the Reporting endpoint, this should be the character ID of the user that you thought was violating terms of use. They must exist in the PGCR provided.
            activity_id: The ID of the activity where you ran into the brigand that you're reporting.
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
            "reasonCategoryHashes": reason_category_hashes,
            "reasonHashes": reason_hashes,
            "offendingCharacterId": offending_character_id,
        }

        return await self.request(
            Route(
                path=f"/Destiny2/Stats/PostGameCarnageReport/{activity_id}/Report/", method="POST", data=data, auth=auth
            )
        )

    async def get_historical_stats_definition(self, auth: Optional[AuthData] = None, *args, **kwargs) -> dict:
        """
        Gets historical stats definitions.

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

        return await self.request(Route(path="/Destiny2/Stats/Definition/", method="GET", auth=auth))

    async def get_clan_leaderboards(
        self,
        group_id: int,
        maxtop: Optional[int] = None,
        modes: Optional[str] = None,
        statid: Optional[str] = None,
        auth: Optional[AuthData] = None,
        *args,
        **kwargs,
    ) -> dict:
        """
        Gets leaderboards with the signed in user's friends and the supplied destinyMembershipId as the focus. PREVIEW: This endpoint is still in beta, and may experience rough edges. The schema is in final form, but there may be bugs that prevent desirable operation.

        Args:
            group_id: Group ID of the clan whose leaderboards you wish to fetch.
            maxtop: Maximum number of top players to return. Use a large number to get entire leaderboard.
            modes: List of game modes for which to get leaderboards. See the documentation for DestinyActivityModeType for valid values, and pass in string representation, comma delimited.
            statid: ID of stat to return rather than returning all Leaderboard stats.
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
                path=f"/Destiny2/Stats/Leaderboards/Clans/{group_id}/",
                method="GET",
                maxtop=maxtop,
                modes=modes,
                statid=statid,
                auth=auth,
            )
        )

    async def get_clan_aggregate_stats(
        self, group_id: int, modes: Optional[str] = None, auth: Optional[AuthData] = None, *args, **kwargs
    ) -> dict:
        """
        Gets aggregated stats for a clan using the same categories as the clan leaderboards. PREVIEW: This endpoint is still in beta, and may experience rough edges. The schema is in final form, but there may be bugs that prevent desirable operation.

        Args:
            group_id: Group ID of the clan whose leaderboards you wish to fetch.
            modes: List of game modes for which to get leaderboards. See the documentation for DestinyActivityModeType for valid values, and pass in string representation, comma delimited.
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
            Route(path=f"/Destiny2/Stats/AggregateClanStats/{group_id}/", method="GET", modes=modes, auth=auth)
        )

    async def get_leaderboards(
        self,
        destiny_membership_id: int,
        membership_type: int,
        maxtop: Optional[int] = None,
        modes: Optional[str] = None,
        statid: Optional[str] = None,
        auth: Optional[AuthData] = None,
        *args,
        **kwargs,
    ) -> dict:
        """
        Gets leaderboards with the signed in user's friends and the supplied destinyMembershipId as the focus. PREVIEW: This endpoint has not yet been implemented. It is being returned for a preview of future functionality, and for public comment/suggestion/preparation.

        Args:
            destiny_membership_id: The Destiny membershipId of the user to retrieve.
            membership_type: A valid non-BungieNet membership type.
            maxtop: Maximum number of top players to return. Use a large number to get entire leaderboard.
            modes: List of game modes for which to get leaderboards. See the documentation for DestinyActivityModeType for valid values, and pass in string representation, comma delimited.
            statid: ID of stat to return rather than returning all Leaderboard stats.
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
                path=f"/Destiny2/{membership_type}/Account/{destiny_membership_id}/Stats/Leaderboards/",
                method="GET",
                maxtop=maxtop,
                modes=modes,
                statid=statid,
                auth=auth,
            )
        )

    async def get_leaderboards_for_character(
        self,
        character_id: int,
        destiny_membership_id: int,
        membership_type: int,
        maxtop: Optional[int] = None,
        modes: Optional[str] = None,
        statid: Optional[str] = None,
        auth: Optional[AuthData] = None,
        *args,
        **kwargs,
    ) -> dict:
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
                path=f"/Destiny2/Stats/Leaderboards/{membership_type}/{destiny_membership_id}/{character_id}/",
                method="GET",
                maxtop=maxtop,
                modes=modes,
                statid=statid,
                auth=auth,
            )
        )

    async def search_destiny_entities(
        self, search_term: str, type: str, page: Optional[int] = None, auth: Optional[AuthData] = None, *args, **kwargs
    ) -> dict:
        """
        Gets a page list of Destiny items.

        Args:
            search_term: The string to use when searching for Destiny entities.
            type: The type of entity for whom you would like results. These correspond to the entity's definition contract name. For instance, if you are looking for items, this property should be 'DestinyInventoryItemDefinition'.
            page: Page number to return, starting with 0.
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
            Route(path=f"/Destiny2/Armory/Search/{type}/{search_term}/", method="GET", page=page, auth=auth)
        )

    async def get_historical_stats(
        self,
        character_id: int,
        destiny_membership_id: int,
        membership_type: int,
        dayend: Optional[datetime] = None,
        daystart: Optional[datetime] = None,
        groups: Optional[int] = None,
        modes: Optional[int] = None,
        period_type: Optional[int] = None,
        auth: Optional[AuthData] = None,
        *args,
        **kwargs,
    ) -> dict:
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
                path=f"/Destiny2/{membership_type}/Account/{destiny_membership_id}/Character/{character_id}/Stats/",
                method="GET",
                dayend=dayend,
                daystart=daystart,
                groups=groups,
                modes=modes,
                period_type=period_type,
                auth=auth,
            )
        )

    async def get_historical_stats_for_account(
        self,
        destiny_membership_id: int,
        membership_type: int,
        groups: Optional[int] = None,
        auth: Optional[AuthData] = None,
        *args,
        **kwargs,
    ) -> dict:
        """
        Gets aggregate historical stats organized around each character for a given account.

        Args:
            destiny_membership_id: The Destiny membershipId of the user to retrieve.
            membership_type: A valid non-BungieNet membership type.
            groups: Groups of stats to include, otherwise only general stats are returned. Comma separated list is allowed. Values: General, Weapons, Medals.
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
                path=f"/Destiny2/{membership_type}/Account/{destiny_membership_id}/Stats/",
                method="GET",
                groups=groups,
                auth=auth,
            )
        )

    async def get_activity_history(
        self,
        character_id: int,
        destiny_membership_id: int,
        membership_type: int,
        count: Optional[int] = None,
        mode: Optional[int] = None,
        page: Optional[int] = None,
        auth: Optional[AuthData] = None,
        *args,
        **kwargs,
    ) -> dict:
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
                path=f"/Destiny2/{membership_type}/Account/{destiny_membership_id}/Character/{character_id}/Stats/Activities/",
                method="GET",
                count=count,
                mode=mode,
                page=page,
                auth=auth,
            )
        )

    async def get_unique_weapon_history(
        self,
        character_id: int,
        destiny_membership_id: int,
        membership_type: int,
        auth: Optional[AuthData] = None,
        *args,
        **kwargs,
    ) -> dict:
        """
        Gets details about unique weapon usage, including all exotic weapons.

        Args:
            character_id: The id of the character to retrieve.
            destiny_membership_id: The Destiny membershipId of the user to retrieve.
            membership_type: A valid non-BungieNet membership type.
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
                path=f"/Destiny2/{membership_type}/Account/{destiny_membership_id}/Character/{character_id}/Stats/UniqueWeapons/",
                method="GET",
                auth=auth,
            )
        )

    async def get_destiny_aggregate_activity_stats(
        self,
        character_id: int,
        destiny_membership_id: int,
        membership_type: int,
        auth: Optional[AuthData] = None,
        *args,
        **kwargs,
    ) -> dict:
        """
        Gets all activities the character has participated in together with aggregate statistics for those activities.

        Args:
            character_id: The specific character whose activities should be returned.
            destiny_membership_id: The Destiny membershipId of the user to retrieve.
            membership_type: A valid non-BungieNet membership type.
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
                path=f"/Destiny2/{membership_type}/Account/{destiny_membership_id}/Character/{character_id}/Stats/AggregateActivityStats/",
                method="GET",
                auth=auth,
            )
        )

    async def get_public_milestone_content(
        self, milestone_hash: int, auth: Optional[AuthData] = None, *args, **kwargs
    ) -> dict:
        """
        Gets custom localized content for the milestone of the given hash, if it exists.

        Args:
            milestone_hash: The identifier for the milestone to be returned.
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
            Route(path=f"/Destiny2/Milestones/{milestone_hash}/Content/", method="GET", auth=auth)
        )

    async def get_public_milestones(self, auth: Optional[AuthData] = None, *args, **kwargs) -> dict:
        """
        Gets public information about currently available Milestones.

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

        return await self.request(Route(path="/Destiny2/Milestones/", method="GET", auth=auth))

    async def awa_initialize_request(
        self,
        type: Union[Any, int],
        affected_item_id: int,
        membership_type: Union[Any, int],
        character_id: int,
        auth: AuthData,
        *args,
        **kwargs,
    ) -> dict:
        """
        Initialize a request to perform an advanced write action.

        Warning: Requires Authentication.
            Required oauth2 scopes: AdvancedWriteActions

        Args:
            type: Type of advanced write action.
            affected_item_id: Item instance ID the action shall be applied to. This is optional for all but a new AwaType values. Rule of thumb is to provide the item instance ID if one is available.
            membership_type: Destiny membership type of the account to modify.
            character_id: Destiny character ID, if applicable, that will be affected by the action.
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
            "type": type,
            "affectedItemId": affected_item_id,
            "membershipType": membership_type,
            "characterId": character_id,
        }

        return await self.request(Route(path="/Destiny2/Awa/Initialize/", method="POST", data=data, auth=auth))

    async def awa_provide_authorization_result(
        self,
        selection: Union[Any, int],
        correlation_id: str,
        nonce: list[int],
        auth: Optional[AuthData] = None,
        *args,
        **kwargs,
    ) -> dict:
        """
        Provide the result of the user interaction. Called by the Bungie Destiny App to approve or reject a request.

        Args:
            selection: Indication of the selection the user has made (Approving or rejecting the action)
            correlation_id: Correlation ID of the request
            nonce: Secret nonce received via the PUSH notification.
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
            "selection": selection,
            "correlationId": correlation_id,
            "nonce": nonce,
        }

        return await self.request(
            Route(path="/Destiny2/Awa/AwaProvideAuthorizationResult/", method="POST", data=data, auth=auth)
        )

    async def awa_get_action_token(self, correlation_id: str, auth: AuthData, *args, **kwargs) -> dict:
        """
        Returns the action token if user approves the request.

        Warning: Requires Authentication.
            Required oauth2 scopes: AdvancedWriteActions

        Args:
            correlation_id: The identifier for the advanced write action request.
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
            Route(path=f"/Destiny2/Awa/GetActionToken/{correlation_id}/", method="GET", auth=auth)
        )
