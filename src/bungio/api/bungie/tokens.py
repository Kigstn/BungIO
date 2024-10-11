# DO NOT CHANGE ANY CODE BELOW
# This file is generated automatically by `generate_api_schema.py` and will be overwritten
# Instead, change functions / models by subclassing them in the `./overwrites/` folder. They will be used instead.

from typing import Optional, Union

from bungio.models import (
    BungieMembershipType,
    BungieRewardDisplay,
    PartnerOfferClaimRequest,
    PartnerOfferSkuHistoryResponse,
    PartnerRewardHistoryResponse,
)
from bungio.models.auth import AuthData
from bungio.models.base import ClientMixin, custom_define
from bungio.utils import AllowAsyncIteration


@custom_define()
class TokensRouteInterface(ClientMixin):
    async def force_drops_repair(self, auth: AuthData) -> bool:
        """
        Twitch Drops self-repair function - scans twitch for drops not marked as fulfilled and resyncs them.

        Warning: Requires Authentication.
            Required oauth2 scopes: PartnerOfferGrant

        Args:
            auth: Authentication information.

        Returns:
            The model which is returned by bungie. [General endpoint information.](https://bungie-net.github.io/multi/index.html)
        """

        response = await self._client.http.force_drops_repair(auth=auth)
        return response["Response"]

    async def claim_partner_offer(self, data: PartnerOfferClaimRequest, auth: AuthData) -> bool:
        """
        Claim a partner offer as the authenticated user.

        Warning: Requires Authentication.
            Required oauth2 scopes: PartnerOfferGrant

        Args:
            data: The required data for this request.
            auth: Authentication information.

        Returns:
            The model which is returned by bungie. [General endpoint information.](https://bungie-net.github.io/multi/index.html)
        """

        response = await self._client.http.claim_partner_offer(auth=auth, **data.to_dict(_return_to_bungie_case=False))
        return response["Response"]

    async def apply_missing_partner_offers_without_claim(
        self, partner_application_id: int, target_bnet_membership_id: int, auth: AuthData
    ) -> bool:
        """
        Apply a partner offer to the targeted user. This endpoint does not claim a new offer, but any already claimed offers will be applied to the game if not already.

        Warning: Requires Authentication.
            Required oauth2 scopes: PartnerOfferGrant

        Args:
            partner_application_id: The partner application identifier.
            target_bnet_membership_id: The bungie.net user to apply missing offers to. If not self, elevated permissions are required.
            auth: Authentication information.

        Returns:
            The model which is returned by bungie. [General endpoint information.](https://bungie-net.github.io/multi/index.html)
        """

        response = await self._client.http.apply_missing_partner_offers_without_claim(
            partner_application_id=partner_application_id,
            target_bnet_membership_id=target_bnet_membership_id,
            auth=auth,
        )
        return response["Response"]

    async def get_partner_offer_sku_history(
        self, partner_application_id: int, target_bnet_membership_id: int, auth: AuthData
    ) -> list[PartnerOfferSkuHistoryResponse]:
        """
        Returns the partner sku and offer history of the targeted user. Elevated permissions are required to see users that are not yourself.

        Warning: Requires Authentication.
            Required oauth2 scopes: PartnerOfferGrant

        Args:
            partner_application_id: The partner application identifier.
            target_bnet_membership_id: The bungie.net user to apply missing offers to. If not self, elevated permissions are required.
            auth: Authentication information.

        Returns:
            The model which is returned by bungie. [General endpoint information.](https://bungie-net.github.io/multi/index.html)
        """

        response = await self._client.http.get_partner_offer_sku_history(
            partner_application_id=partner_application_id,
            target_bnet_membership_id=target_bnet_membership_id,
            auth=auth,
        )
        return [
            await PartnerOfferSkuHistoryResponse.from_dict(
                data=value,
                client=self._client,
                partner_application_id=partner_application_id,
                target_bnet_membership_id=target_bnet_membership_id,
                auth=auth,
            )
            for value in response["Response"]
        ]

    async def get_partner_reward_history(
        self, partner_application_id: int, target_bnet_membership_id: int, auth: AuthData
    ) -> PartnerRewardHistoryResponse:
        """
        Returns the partner rewards history of the targeted user, both partner offers and Twitch drops.

        Warning: Requires Authentication.
            Required oauth2 scopes: PartnerOfferGrant

        Args:
            partner_application_id: The partner application identifier.
            target_bnet_membership_id: The bungie.net user to return reward history for.
            auth: Authentication information.

        Returns:
            The model which is returned by bungie. [General endpoint information.](https://bungie-net.github.io/multi/index.html)
        """

        response = await self._client.http.get_partner_reward_history(
            partner_application_id=partner_application_id,
            target_bnet_membership_id=target_bnet_membership_id,
            auth=auth,
        )
        return await PartnerRewardHistoryResponse.from_dict(
            data=response,
            client=self._client,
            partner_application_id=partner_application_id,
            target_bnet_membership_id=target_bnet_membership_id,
            auth=auth,
        )

    async def get_bungie_rewards_for_user(self, membership_id: int, auth: AuthData) -> dict[str, BungieRewardDisplay]:
        """
        Returns the bungie rewards for the targeted user.

        Warning: Requires Authentication.
            Required oauth2 scopes: ReadAndApplyTokens

        Args:
            membership_id: bungie.net user membershipId for requested user rewards. If not self, elevated permissions are required.
            auth: Authentication information.

        Returns:
            The model which is returned by bungie. [General endpoint information.](https://bungie-net.github.io/multi/index.html)
        """

        response = await self._client.http.get_bungie_rewards_for_user(membership_id=membership_id, auth=auth)
        return {
            key: await BungieRewardDisplay.from_dict(
                data=value, client=self._client, membership_id=membership_id, auth=auth
            )
            async for key, value in AllowAsyncIteration(response["Response"].items())
        }

    async def get_bungie_rewards_for_platform_user(
        self, membership_id: int, membership_type: Union[BungieMembershipType, int], auth: AuthData
    ) -> dict[str, BungieRewardDisplay]:
        """
        Returns the bungie rewards for the targeted user when a platform membership Id and Type are used.

        Warning: Requires Authentication.
            Required oauth2 scopes: ReadAndApplyTokens

        Args:
            membership_id: users platform membershipId for requested user rewards. If not self, elevated permissions are required.
            membership_type: The target Destiny 2 membership type.
            auth: Authentication information.

        Returns:
            The model which is returned by bungie. [General endpoint information.](https://bungie-net.github.io/multi/index.html)
        """

        response = await self._client.http.get_bungie_rewards_for_platform_user(
            membership_id=membership_id, membership_type=getattr(membership_type, "value", membership_type), auth=auth
        )
        return {
            key: await BungieRewardDisplay.from_dict(
                data=value, client=self._client, membership_id=membership_id, membership_type=membership_type, auth=auth
            )
            async for key, value in AllowAsyncIteration(response["Response"].items())
        }

    async def get_bungie_rewards_list(self, auth: Optional[AuthData] = None) -> dict[str, BungieRewardDisplay]:
        """
        Returns a list of the current bungie rewards

        Args:
            auth: Authentication information. Required when users with a private profile are queried, or when Bungie feels like it

        Returns:
            The model which is returned by bungie. [General endpoint information.](https://bungie-net.github.io/multi/index.html)
        """

        response = await self._client.http.get_bungie_rewards_list(auth=auth)
        return {
            key: await BungieRewardDisplay.from_dict(data=value, client=self._client, auth=auth)
            async for key, value in AllowAsyncIteration(response["Response"].items())
        }
