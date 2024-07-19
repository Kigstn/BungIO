# DO NOT CHANGE ANY CODE BELOW
# This file is generated automatically by `generate_api_schema.py` and will be overwritten
# Instead, change functions / models by subclassing them in the `./overwrites/` folder. They will be used instead.

from datetime import datetime
from typing import TYPE_CHECKING

from bungio.models.base import BaseModel, custom_define, custom_field

from bungio.models.mixins import DestinyUserMixin

if TYPE_CHECKING:
    from bungio.models import DestinyCollectibleDefinition
    from bungio.models import DestinyInventoryItemDefinition
    from bungio.models import DestinyRecordDefinition


@custom_define()
class PartnerOfferClaimRequest(BaseModel):
    """
    _No description given by bungie._

    None
    Attributes:
        bungie_net_membership_id: _No description given by bungie._
        partner_offer_id: _No description given by bungie._
        transaction_id: _No description given by bungie._
    """

    bungie_net_membership_id: int = custom_field(metadata={"int64": True})
    partner_offer_id: str = custom_field()
    transaction_id: str = custom_field()


@custom_define()
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

    all_offers_applied: bool = custom_field()
    claim_date: datetime = custom_field()
    localized_description: str = custom_field()
    localized_name: str = custom_field()
    sku_identifier: str = custom_field()
    sku_offers: list["PartnerOfferHistoryResponse"] = custom_field(
        metadata={"type": """list[PartnerOfferHistoryResponse]"""}
    )
    transaction_id: str = custom_field()


@custom_define()
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

    apply_date: datetime = custom_field()
    is_consumable: bool = custom_field()
    localized_description: str = custom_field()
    localized_name: str = custom_field()
    membership_id: int = custom_field(metadata={"int64": True})
    membership_type: int = custom_field()
    partner_offer_key: str = custom_field()
    quantity_applied: int = custom_field()


@custom_define()
class PartnerRewardHistoryResponse(BaseModel):
    """
    _No description given by bungie._

    None
    Attributes:
        partner_offers: _No description given by bungie._
        twitch_drops: _No description given by bungie._
    """

    partner_offers: list["PartnerOfferSkuHistoryResponse"] = custom_field(
        metadata={"type": """list[PartnerOfferSkuHistoryResponse]"""}
    )
    twitch_drops: list["TwitchDropHistoryResponse"] = custom_field(
        metadata={"type": """list[TwitchDropHistoryResponse]"""}
    )


@custom_define()
class TwitchDropHistoryResponse(BaseModel):
    """
    _No description given by bungie._

    None
    Attributes:
        claim_state: _No description given by bungie._
        created_at: _No description given by bungie._
        description: _No description given by bungie._
        title: _No description given by bungie._
    """

    claim_state: int = custom_field()
    created_at: datetime = custom_field()
    description: str = custom_field()
    title: str = custom_field()


@custom_define()
class BungieRewardDisplay(BaseModel):
    """
    _No description given by bungie._

    None
    Attributes:
        objective_display_properties: _No description given by bungie._
        reward_display_properties: _No description given by bungie._
        user_reward_availability_model: _No description given by bungie._
    """

    objective_display_properties: "RewardDisplayProperties" = custom_field()
    reward_display_properties: "RewardDisplayProperties" = custom_field()
    user_reward_availability_model: "UserRewardAvailabilityModel" = custom_field()


@custom_define()
class UserRewardAvailabilityModel(BaseModel):
    """
    _No description given by bungie._

    None
    Attributes:
        availability_model: _No description given by bungie._
        is_available_for_user: _No description given by bungie._
        is_unlocked_for_user: _No description given by bungie._
    """

    availability_model: "RewardAvailabilityModel" = custom_field()
    is_available_for_user: bool = custom_field()
    is_unlocked_for_user: bool = custom_field()


@custom_define()
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

    collectible_definitions: list["CollectibleDefinitions"] = custom_field(
        metadata={"type": """list[CollectibleDefinitions]"""}
    )
    decrypted_token: str = custom_field()
    game_earn_by_date: datetime = custom_field()
    has_existing_code: bool = custom_field()
    has_offer: bool = custom_field()
    is_loyalty_reward: bool = custom_field()
    is_offer: bool = custom_field()
    offer_applied: bool = custom_field()
    record_definitions: list["DestinyRecordDefinition"] = custom_field(
        metadata={"type": """list[DestinyRecordDefinition]"""}
    )
    redemption_end_date: datetime = custom_field()
    shopify_end_date: datetime = custom_field()


@custom_define()
class CollectibleDefinitions(BaseModel):
    """
    _No description given by bungie._

    None
    Attributes:
        collectible_definition: _No description given by bungie._
        destiny_inventory_item_definition: _No description given by bungie._
    """

    collectible_definition: "DestinyCollectibleDefinition" = custom_field()
    destiny_inventory_item_definition: "DestinyInventoryItemDefinition" = custom_field()


@custom_define()
class RewardDisplayProperties(BaseModel):
    """
    _No description given by bungie._

    None
    Attributes:
        description: _No description given by bungie._
        image_path: _No description given by bungie._
        name: _No description given by bungie._
    """

    description: str = custom_field()
    image_path: str = custom_field()
    name: str = custom_field()
