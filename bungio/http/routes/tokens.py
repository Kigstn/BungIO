import datetime
from typing import Callable, Coroutine, Optional

from bungio.http.route import Route
from bungio.models.auth import AuthData


class TokensRequests:
    request: Callable[..., Coroutine]

    async def claim_partner_offer(self, auth: AuthData) -> dict:
        """
        Claim a partner offer as the authenticated user.

        Warning: Requires Authentication.
            Required oauth2 scopes: PartnerOfferGrant

        Args:
            auth: Authentication information.

        Returns:
            The json response
        """

        return await self.request(Route(path=f"/Tokens/Partner/ClaimOffer/", method="POST", auth=auth))

    async def apply_missing_partner_offers_without_claim(
        self, partner_application_id: int, target_bnet_membership_id: int, auth: AuthData
    ) -> dict:
        """
        Apply a partner offer to the targeted user. This endpoint does not claim a new offer, but any already claimed offers will be applied to the game if not already.

        Warning: Requires Authentication.
            Required oauth2 scopes: PartnerOfferGrant

        Args:
            partner_application_id: The partner application identifier.
            target_bnet_membership_id: The bungie.net user to apply missing offers to. If not self, elevated permissions are required.
            auth: Authentication information.

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
        self, partner_application_id: int, target_bnet_membership_id: int, auth: AuthData
    ) -> dict:
        """
        Returns the partner sku and offer history of the targeted user. Elevated permissions are required to see users that are not yourself.

        Warning: Requires Authentication.
            Required oauth2 scopes: PartnerOfferGrant

        Args:
            partner_application_id: The partner application identifier.
            target_bnet_membership_id: The bungie.net user to apply missing offers to. If not self, elevated permissions are required.
            auth: Authentication information.

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
