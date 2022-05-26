import datetime
from typing import TYPE_CHECKING, Any, Optional

import attr

from bungio.models.base import BaseEnum, BaseModel


@attr.define
class PartnerOfferClaimRequest(BaseModel):
    """
    Not specified.

    Attributes:
        partner_offer_id: Not specified.
        bungie_net_membership_id: Not specified.
        transaction_id: Not specified.
    """

    partner_offer_id: str = attr.field()
    bungie_net_membership_id: int = attr.field()
    transaction_id: str = attr.field()


@attr.define
class PartnerOfferSkuHistoryResponse(BaseModel):
    """
    Not specified.

    Attributes:
        sku_identifier: Not specified.
        localized_name: Not specified.
        localized_description: Not specified.
        claim_date: Not specified.
        all_offers_applied: Not specified.
        transaction_id: Not specified.
        sku_offers: Not specified.
    """

    sku_identifier: str = attr.field()
    localized_name: str = attr.field()
    localized_description: str = attr.field()
    claim_date: datetime.datetime = attr.field()
    all_offers_applied: bool = attr.field()
    transaction_id: str = attr.field()
    sku_offers: list["PartnerOfferHistoryResponse"] = attr.field()


@attr.define
class PartnerOfferHistoryResponse(BaseModel):
    """
    Not specified.

    Attributes:
        partner_offer_key: Not specified.
        membership_id: Not specified.
        membership_type: Not specified.
        localized_name: Not specified.
        localized_description: Not specified.
        is_consumable: Not specified.
        quantity_applied: Not specified.
        apply_date: Not specified.
    """

    partner_offer_key: str = attr.field()
    membership_id: int = attr.field()
    membership_type: int = attr.field()
    localized_name: str = attr.field()
    localized_description: str = attr.field()
    is_consumable: bool = attr.field()
    quantity_applied: int = attr.field()
    apply_date: datetime.datetime = attr.field()


@attr.define
class BungieRewardDisplay(BaseModel):
    """
    Not specified.

    Attributes:
        user_reward_availability_model: Not specified.
        objective_display_properties: Not specified.
        reward_display_properties: Not specified.
    """

    user_reward_availability_model: "UserRewardAvailabilityModel" = attr.field()
    objective_display_properties: "RewardDisplayProperties" = attr.field()
    reward_display_properties: "RewardDisplayProperties" = attr.field()


@attr.define
class UserRewardAvailabilityModel(BaseModel):
    """
    Not specified.

    Attributes:
        availability_model: Not specified.
        is_available_for_user: Not specified.
        is_unlocked_for_user: Not specified.
    """

    availability_model: "RewardAvailabilityModel" = attr.field()
    is_available_for_user: bool = attr.field()
    is_unlocked_for_user: bool = attr.field()


@attr.define
class RewardAvailabilityModel(BaseModel):
    """
    Not specified.

    Attributes:
        has_existing_code: Not specified.
        record_definitions: Not specified.
        collectible_definitions: Not specified.
        is_offer: Not specified.
        has_offer: Not specified.
        offer_applied: Not specified.
        decrypted_token: Not specified.
        is_loyalty_reward: Not specified.
        shopify_end_date: Not specified.
        game_earn_by_date: Not specified.
        redemption_end_date: Not specified.
    """

    has_existing_code: bool = attr.field()
    record_definitions: list["DestinyRecordDefinition"] = attr.field()
    collectible_definitions: list["CollectibleDefinitions"] = attr.field()
    is_offer: bool = attr.field()
    has_offer: bool = attr.field()
    offer_applied: bool = attr.field()
    decrypted_token: str = attr.field()
    is_loyalty_reward: bool = attr.field()
    shopify_end_date: datetime.datetime = attr.field()
    game_earn_by_date: datetime.datetime = attr.field()
    redemption_end_date: datetime.datetime = attr.field()


@attr.define
class CollectibleDefinitions(BaseModel):
    """
    Not specified.

    Attributes:
        collectible_definition: Not specified.
        destiny_inventory_item_definition: Not specified.
    """

    collectible_definition: "DestinyCollectibleDefinition" = attr.field()
    destiny_inventory_item_definition: "DestinyInventoryItemDefinition" = attr.field()


@attr.define
class RewardDisplayProperties(BaseModel):
    """
    Not specified.

    Attributes:
        name: Not specified.
        description: Not specified.
        image_path: Not specified.
    """

    name: str = attr.field()
    description: str = attr.field()
    image_path: str = attr.field()
