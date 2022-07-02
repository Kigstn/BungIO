# DO NOT CHANGE ANY CODE BELOW
# This file is generated automatically by `generate_api_schema.py` and will be overwritten
# Instead, change functions / models by subclassing them in the `./overwrites/` folder. They will be used instead.

from datetime import datetime
from typing import TYPE_CHECKING

import attr

from bungio.models.base import BaseModel
from bungio.models.mixins import DestinyUserMixin

if TYPE_CHECKING:
    from bungio.models import (
        DestinyCollectibleDefinition,
        DestinyInventoryItemDefinition,
        DestinyRecordDefinition,
    )


@attr.define
class PartnerOfferClaimRequest(BaseModel):
    """
    _No description given by bungie._

    None
    Attributes:
        bungie_net_membership_id: _No description given by bungie._
        partner_offer_id: _No description given by bungie._
        transaction_id: _No description given by bungie._
    """

    bungie_net_membership_id: int = attr.field()
    partner_offer_id: str = attr.field()
    transaction_id: str = attr.field()


@attr.define
class PartnerOfferSkuHistoryResponse(BaseModel):
    """
    _No description given by bungie._

    None
    Attributes:
        all_offers_applied: _No description given by bungie._
        claim_date: _No description given by bungie._
        localized_description: _No description given by bungie._
        localized_name: _No description given by bungie._
        sku_identifier: _No description given by bungie._
        sku_offers: _No description given by bungie._
        transaction_id: _No description given by bungie._
    """

    all_offers_applied: bool = attr.field()
    claim_date: datetime = attr.field()
    localized_description: str = attr.field()
    localized_name: str = attr.field()
    sku_identifier: str = attr.field()
    sku_offers: list["PartnerOfferHistoryResponse"] = attr.field(
        metadata={"type": """list[PartnerOfferHistoryResponse]"""}
    )
    transaction_id: str = attr.field()


@attr.define
class PartnerOfferHistoryResponse(BaseModel, DestinyUserMixin):
    """
    _No description given by bungie._

    None
    Attributes:
        apply_date: _No description given by bungie._
        is_consumable: _No description given by bungie._
        localized_description: _No description given by bungie._
        localized_name: _No description given by bungie._
        membership_id: _No description given by bungie._
        membership_type: _No description given by bungie._
        partner_offer_key: _No description given by bungie._
        quantity_applied: _No description given by bungie._
    """

    apply_date: datetime = attr.field()
    is_consumable: bool = attr.field()
    localized_description: str = attr.field()
    localized_name: str = attr.field()
    membership_id: int = attr.field()
    membership_type: int = attr.field()
    partner_offer_key: str = attr.field()
    quantity_applied: int = attr.field()


@attr.define
class BungieRewardDisplay(BaseModel):
    """
    _No description given by bungie._

    None
    Attributes:
        objective_display_properties: _No description given by bungie._
        reward_display_properties: _No description given by bungie._
        user_reward_availability_model: _No description given by bungie._
    """

    objective_display_properties: "RewardDisplayProperties" = attr.field()
    reward_display_properties: "RewardDisplayProperties" = attr.field()
    user_reward_availability_model: "UserRewardAvailabilityModel" = attr.field()


@attr.define
class UserRewardAvailabilityModel(BaseModel):
    """
    _No description given by bungie._

    None
    Attributes:
        availability_model: _No description given by bungie._
        is_available_for_user: _No description given by bungie._
        is_unlocked_for_user: _No description given by bungie._
    """

    availability_model: "RewardAvailabilityModel" = attr.field()
    is_available_for_user: bool = attr.field()
    is_unlocked_for_user: bool = attr.field()


@attr.define
class RewardAvailabilityModel(BaseModel):
    """
    _No description given by bungie._

    None
    Attributes:
        collectible_definitions: _No description given by bungie._
        decrypted_token: _No description given by bungie._
        game_earn_by_date: _No description given by bungie._
        has_existing_code: _No description given by bungie._
        has_offer: _No description given by bungie._
        is_loyalty_reward: _No description given by bungie._
        is_offer: _No description given by bungie._
        offer_applied: _No description given by bungie._
        record_definitions: _No description given by bungie._
        redemption_end_date: _No description given by bungie._
        shopify_end_date: _No description given by bungie._
    """

    collectible_definitions: list["CollectibleDefinitions"] = attr.field(
        metadata={"type": """list[CollectibleDefinitions]"""}
    )
    decrypted_token: str = attr.field()
    game_earn_by_date: datetime = attr.field()
    has_existing_code: bool = attr.field()
    has_offer: bool = attr.field()
    is_loyalty_reward: bool = attr.field()
    is_offer: bool = attr.field()
    offer_applied: bool = attr.field()
    record_definitions: list["DestinyRecordDefinition"] = attr.field(
        metadata={"type": """list[DestinyRecordDefinition]"""}
    )
    redemption_end_date: datetime = attr.field()
    shopify_end_date: datetime = attr.field()


@attr.define
class CollectibleDefinitions(BaseModel):
    """
    _No description given by bungie._

    None
    Attributes:
        collectible_definition: _No description given by bungie._
        destiny_inventory_item_definition: _No description given by bungie._
    """

    collectible_definition: "DestinyCollectibleDefinition" = attr.field()
    destiny_inventory_item_definition: "DestinyInventoryItemDefinition" = attr.field()


@attr.define
class RewardDisplayProperties(BaseModel):
    """
    _No description given by bungie._

    None
    Attributes:
        description: _No description given by bungie._
        image_path: _No description given by bungie._
        name: _No description given by bungie._
    """

    description: str = attr.field()
    image_path: str = attr.field()
    name: str = attr.field()
