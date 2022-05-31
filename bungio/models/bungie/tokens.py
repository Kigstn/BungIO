import datetime
from typing import TYPE_CHECKING

import attr

from bungio.models.base import BaseModel

if TYPE_CHECKING:
    from bungio.models import (
        CollectibleDefinitions,
        DestinyCollectibleDefinition,
        DestinyInventoryItemDefinition,
        DestinyRecordDefinition,
        PartnerOfferHistoryResponse,
        RewardAvailabilityModel,
        RewardDisplayProperties,
        UserRewardAvailabilityModel,
    )


@attr.define
class PartnerOfferClaimRequest(BaseModel):
    """
    _No description given_

    Attributes:
        partner_offer_id: _No description given_
        bungie_net_membership_id: _No description given_
        transaction_id: _No description given_
    """

    partner_offer_id: str = attr.field()
    bungie_net_membership_id: int = attr.field()
    transaction_id: str = attr.field()


@attr.define
class PartnerOfferSkuHistoryResponse(BaseModel):
    """
    _No description given_

    Attributes:
        sku_identifier: _No description given_
        localized_name: _No description given_
        localized_description: _No description given_
        claim_date: _No description given_
        all_offers_applied: _No description given_
        transaction_id: _No description given_
        sku_offers: _No description given_
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
    _No description given_

    Attributes:
        partner_offer_key: _No description given_
        membership_id: _No description given_
        membership_type: _No description given_
        localized_name: _No description given_
        localized_description: _No description given_
        is_consumable: _No description given_
        quantity_applied: _No description given_
        apply_date: _No description given_
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
    _No description given_

    Attributes:
        user_reward_availability_model: _No description given_
        objective_display_properties: _No description given_
        reward_display_properties: _No description given_
    """

    user_reward_availability_model: "UserRewardAvailabilityModel" = attr.field()
    objective_display_properties: "RewardDisplayProperties" = attr.field()
    reward_display_properties: "RewardDisplayProperties" = attr.field()


@attr.define
class UserRewardAvailabilityModel(BaseModel):
    """
    _No description given_

    Attributes:
        availability_model: _No description given_
        is_available_for_user: _No description given_
        is_unlocked_for_user: _No description given_
    """

    availability_model: "RewardAvailabilityModel" = attr.field()
    is_available_for_user: bool = attr.field()
    is_unlocked_for_user: bool = attr.field()


@attr.define
class RewardAvailabilityModel(BaseModel):
    """
    _No description given_

    Attributes:
        has_existing_code: _No description given_
        record_definitions: _No description given_
        collectible_definitions: _No description given_
        is_offer: _No description given_
        has_offer: _No description given_
        offer_applied: _No description given_
        decrypted_token: _No description given_
        is_loyalty_reward: _No description given_
        shopify_end_date: _No description given_
        game_earn_by_date: _No description given_
        redemption_end_date: _No description given_
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
    _No description given_

    Attributes:
        collectible_definition: _No description given_
        destiny_inventory_item_definition: _No description given_
    """

    collectible_definition: "DestinyCollectibleDefinition" = attr.field()
    destiny_inventory_item_definition: "DestinyInventoryItemDefinition" = attr.field()


@attr.define
class RewardDisplayProperties(BaseModel):
    """
    _No description given_

    Attributes:
        name: _No description given_
        description: _No description given_
        image_path: _No description given_
    """

    name: str = attr.field()
    description: str = attr.field()
    image_path: str = attr.field()
