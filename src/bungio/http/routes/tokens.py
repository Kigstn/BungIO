from typing import Callable, Coroutine, Optional

from bungio.http.route import Route
from bungio.models.auth import AuthData


class TokensRouteHttpRequests:
    request: Callable[..., Coroutine]

    async def force_drops_repair(self, auth: AuthData, *args, **kwargs) -> dict:
        """
        Twitch Drops self-repair function - scans twitch for drops not marked as fulfilled and resyncs them.

        Warning: Requires Authentication.
            Required oauth2 scopes: PartnerOfferGrant

        Args:
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

        return await self.request(Route(path="/Tokens/Partner/ForceDropsRepair/", method="POST", auth=auth))

    async def claim_partner_offer(
        self, partner_offer_id: str, bungie_net_membership_id: int, transaction_id: str, auth: AuthData, *args, **kwargs
    ) -> dict:
        """
        Claim a partner offer as the authenticated user.

        Warning: Requires Authentication.
            Required oauth2 scopes: PartnerOfferGrant

        Args:
            partner_offer_id: _No description given by bungie._
            bungie_net_membership_id: _No description given by bungie._
            transaction_id: _No description given by bungie._
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
            "PartnerOfferId": partner_offer_id,
            "BungieNetMembershipId": bungie_net_membership_id,
            "TransactionId": transaction_id,
        }

        return await self.request(Route(path="/Tokens/Partner/ClaimOffer/", method="POST", data=data, auth=auth))

    async def apply_missing_partner_offers_without_claim(
        self, partner_application_id: int, target_bnet_membership_id: int, auth: AuthData, *args, **kwargs
    ) -> dict:
        """
        Apply a partner offer to the targeted user. This endpoint does not claim a new offer, but any already claimed offers will be applied to the game if not already.

        Warning: Requires Authentication.
            Required oauth2 scopes: PartnerOfferGrant

        Args:
            partner_application_id: The partner application identifier.
            target_bnet_membership_id: The bungie.net user to apply missing offers to. If not self, elevated permissions are required.
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
                path=f"/Tokens/Partner/ApplyMissingOffers/{partner_application_id}/{target_bnet_membership_id}/",
                method="POST",
                auth=auth,
            )
        )

    async def get_partner_offer_sku_history(
        self, partner_application_id: int, target_bnet_membership_id: int, auth: AuthData, *args, **kwargs
    ) -> dict:
        """
        Returns the partner sku and offer history of the targeted user. Elevated permissions are required to see users that are not yourself.

        Warning: Requires Authentication.
            Required oauth2 scopes: PartnerOfferGrant

        Args:
            partner_application_id: The partner application identifier.
            target_bnet_membership_id: The bungie.net user to apply missing offers to. If not self, elevated permissions are required.
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
                path=f"/Tokens/Partner/History/{partner_application_id}/{target_bnet_membership_id}/",
                method="GET",
                auth=auth,
            )
        )

    async def get_partner_reward_history(
        self, partner_application_id: int, target_bnet_membership_id: int, auth: AuthData, *args, **kwargs
    ) -> dict:
        """
        Returns the partner rewards history of the targeted user, both partner offers and Twitch drops.

        Warning: Requires Authentication.
            Required oauth2 scopes: PartnerOfferGrant

        Args:
            partner_application_id: The partner application identifier.
            target_bnet_membership_id: The bungie.net user to return reward history for.
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
                path=f"/Tokens/Partner/History/{target_bnet_membership_id}/Application/{partner_application_id}/",
                method="GET",
                auth=auth,
            )
        )

    async def get_bungie_rewards_for_user(self, membership_id: int, auth: AuthData, *args, **kwargs) -> dict:
        """
        Returns the bungie rewards for the targeted user.

        Warning: Requires Authentication.
            Required oauth2 scopes: ReadAndApplyTokens

        Args:
            membership_id: bungie.net user membershipId for requested user rewards. If not self, elevated permissions are required.
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
            Route(path=f"/Tokens/Rewards/GetRewardsForUser/{membership_id}/", method="GET", auth=auth)
        )

    async def get_bungie_rewards_for_platform_user(
        self, membership_id: int, membership_type: int, auth: AuthData, *args, **kwargs
    ) -> dict:
        """
        Returns the bungie rewards for the targeted user when a platform membership Id and Type are used.

        Warning: Requires Authentication.
            Required oauth2 scopes: ReadAndApplyTokens

        Args:
            membership_id: users platform membershipId for requested user rewards. If not self, elevated permissions are required.
            membership_type: The target Destiny 2 membership type.
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
                path=f"/Tokens/Rewards/GetRewardsForPlatformUser/{membership_id}/{membership_type}/",
                method="GET",
                auth=auth,
            )
        )

    async def get_bungie_rewards_list(self, auth: Optional[AuthData] = None, *args, **kwargs) -> dict:
        """
        Returns a list of the current bungie rewards

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

        return await self.request(Route(path="/Tokens/Rewards/BungieRewards/", method="GET", auth=auth))
