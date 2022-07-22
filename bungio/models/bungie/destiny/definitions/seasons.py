# DO NOT CHANGE ANY CODE BELOW
# This file is generated automatically by `generate_api_schema.py` and will be overwritten
# Instead, change functions / models by subclassing them in the `./overwrites/` folder. They will be used instead.

from datetime import datetime
from typing import TYPE_CHECKING, Optional

import attr

from bungio.models.base import BaseModel, ManifestModel

if TYPE_CHECKING:
    from bungio.models import (
        DestinyColor,
        DestinyDisplayPropertiesDefinition,
        DestinyInventoryItemDefinition,
        DestinyPresentationNodeDefinition,
        DestinyProgressionDefinition,
        DestinyVendorDefinition,
    )


@attr.define
class DestinySeasonDefinition(ManifestModel):
    """
    Defines a canonical "Season" of Destiny: a range of a few months where the game highlights certain challenges, provides new loot, has new Clan-related rewards and celebrates various seasonal events.

    Tip: Manifest Information
        This model has some attributes which can be filled with additional information found in the manifest (`manifest_...`).
        Without additional work, these attributes will be `None`, since they require additional requests and database lookups.

        To fill the manifest dependent attributes, either:

        - Run `await ThisClass.fetch_manifest_information()`, see [here](/API Reference/Models/base)
        - Set `Client.always_return_manifest_information` to `True`, see [here](/API Reference/client)

    Attributes:
        artifact_item_hash: _No description given by bungie._
        background_image_path: _No description given by bungie._
        display_properties: _No description given by bungie._
        end_date: _No description given by bungie._
        hash: The unique identifier for this entity. Guaranteed to be unique for the type of entity, but not globally. When entities refer to each other in Destiny content, it is this hash that they are referring to.
        index: The index of the entity as it was found in the investment tables.
        preview: Optional - Defines the promotional text, images, and links to preview this season.
        redacted: If this is true, then there is an entity with this identifier/type combination, but BNet is not yet allowed to show it. Sorry!
        seal_presentation_node_hash: _No description given by bungie._
        season_number: _No description given by bungie._
        season_pass_hash: _No description given by bungie._
        season_pass_progression_hash: _No description given by bungie._
        seasonal_challenges_presentation_node_hash: _No description given by bungie._
        start_date: _No description given by bungie._
        manifest_artifact_item_hash: Manifest information for `artifact_item_hash`
        manifest_seal_presentation_node_hash: Manifest information for `seal_presentation_node_hash`
        manifest_season_pass_hash: Manifest information for `season_pass_hash`
        manifest_season_pass_progression_hash: Manifest information for `season_pass_progression_hash`
        manifest_seasonal_challenges_presentation_node_hash: Manifest information for `seasonal_challenges_presentation_node_hash`
    """

    artifact_item_hash: int = attr.field()
    background_image_path: str = attr.field()
    display_properties: "DestinyDisplayPropertiesDefinition" = attr.field()
    end_date: datetime = attr.field()
    hash: int = attr.field()
    index: int = attr.field()
    preview: "DestinySeasonPreviewDefinition" = attr.field()
    redacted: bool = attr.field()
    seal_presentation_node_hash: int = attr.field()
    season_number: int = attr.field()
    season_pass_hash: int = attr.field()
    season_pass_progression_hash: int = attr.field()
    seasonal_challenges_presentation_node_hash: int = attr.field()
    start_date: datetime = attr.field()
    manifest_artifact_item_hash: Optional["DestinyInventoryItemDefinition"] = attr.field(default=None)
    manifest_seal_presentation_node_hash: Optional["DestinyPresentationNodeDefinition"] = attr.field(default=None)
    manifest_season_pass_hash: Optional["DestinySeasonPassDefinition"] = attr.field(default=None)
    manifest_season_pass_progression_hash: Optional["DestinyProgressionDefinition"] = attr.field(default=None)
    manifest_seasonal_challenges_presentation_node_hash: Optional["DestinyPresentationNodeDefinition"] = attr.field(
        default=None
    )


@attr.define
class DestinySeasonPreviewDefinition(BaseModel):
    """
    Defines the promotional text, images, and links to preview this season.

    None
    Attributes:
        description: A localized description of the season.
        images: A list of images to preview the seasonal content. Should have at least three to show.
        link_path: A relative path to learn more about the season. Web browsers should be automatically redirected to the user's Bungie.net locale. For example: "/SeasonOfTheChosen" will redirect to "/7/en/Seasons/SeasonOfTheChosen" for English users.
        video_link: An optional link to a localized video, probably YouTube.
    """

    description: str = attr.field()
    images: list["DestinySeasonPreviewImageDefinition"] = attr.field(
        metadata={"type": """list[DestinySeasonPreviewImageDefinition]"""}
    )
    link_path: str = attr.field()
    video_link: str = attr.field()


@attr.define
class DestinySeasonPreviewImageDefinition(BaseModel):
    """
    Defines the thumbnail icon, high-res image, and video link for promotional images

    None
    Attributes:
        high_res_image: An optional path to a high-resolution image, probably 1920x1080.
        thumbnail_image: A thumbnail icon path to preview seasonal content, probably 480x270.
    """

    high_res_image: str = attr.field()
    thumbnail_image: str = attr.field()


@attr.define
class DestinySeasonPassDefinition(ManifestModel):
    """
    _No description given by bungie._

    Tip: Manifest Information
        This model has some attributes which can be filled with additional information found in the manifest (`manifest_...`).
        Without additional work, these attributes will be `None`, since they require additional requests and database lookups.

        To fill the manifest dependent attributes, either:

        - Run `await ThisClass.fetch_manifest_information()`, see [here](/API Reference/Models/base)
        - Set `Client.always_return_manifest_information` to `True`, see [here](/API Reference/client)

    Attributes:
        display_properties: _No description given by bungie._
        hash: The unique identifier for this entity. Guaranteed to be unique for the type of entity, but not globally. When entities refer to each other in Destiny content, it is this hash that they are referring to.
        index: The index of the entity as it was found in the investment tables.
        prestige_progression_hash: I know what you're thinking, but I promise we're not going to duplicate and drown you. Instead, we're giving you sweet, sweet power bonuses.  Prestige progression is further progression that you can make on the Season pass after you gain max ranks, that will ultimately increase your power/light level over the theoretical limit.
        redacted: If this is true, then there is an entity with this identifier/type combination, but BNet is not yet allowed to show it. Sorry!
        reward_progression_hash: This is the progression definition related to the progression for the initial levels 1-100 that provide item rewards for the Season pass. Further experience after you reach the limit is provided in the "Prestige" progression referred to by prestigeProgressionHash.
        manifest_prestige_progression_hash: Manifest information for `prestige_progression_hash`
        manifest_reward_progression_hash: Manifest information for `reward_progression_hash`
    """

    display_properties: "DestinyDisplayPropertiesDefinition" = attr.field()
    hash: int = attr.field()
    index: int = attr.field()
    prestige_progression_hash: int = attr.field()
    redacted: bool = attr.field()
    reward_progression_hash: int = attr.field()
    manifest_prestige_progression_hash: Optional["DestinyProgressionDefinition"] = attr.field(default=None)
    manifest_reward_progression_hash: Optional["DestinyProgressionDefinition"] = attr.field(default=None)


@attr.define
class DestinyEventCardDefinition(ManifestModel):
    """
    Defines the properties of an 'Event Card' in Destiny 2, to coincide with a seasonal event for additional challenges, premium rewards, a new seal, and a special title. For example: Solstice of Heroes 2022.

    Tip: Manifest Information
        This model has some attributes which can be filled with additional information found in the manifest (`manifest_...`).
        Without additional work, these attributes will be `None`, since they require additional requests and database lookups.

        To fill the manifest dependent attributes, either:

        - Run `await ThisClass.fetch_manifest_information()`, see [here](/API Reference/Models/base)
        - Set `Client.always_return_manifest_information` to `True`, see [here](/API Reference/client)

    Attributes:
        color: _No description given by bungie._
        display_properties: _No description given by bungie._
        end_time: _No description given by bungie._
        hash: The unique identifier for this entity. Guaranteed to be unique for the type of entity, but not globally. When entities refer to each other in Destiny content, it is this hash that they are referring to.
        images: _No description given by bungie._
        index: The index of the entity as it was found in the investment tables.
        link_redirect_path: _No description given by bungie._
        redacted: If this is true, then there is an entity with this identifier/type combination, but BNet is not yet allowed to show it. Sorry!
        seal_presentation_node_hash: _No description given by bungie._
        ticket_currency_item_hash: _No description given by bungie._
        ticket_vendor_category_hash: _No description given by bungie._
        ticket_vendor_hash: _No description given by bungie._
        triumphs_presentation_node_hash: _No description given by bungie._
        manifest_seal_presentation_node_hash: Manifest information for `seal_presentation_node_hash`
        manifest_ticket_currency_item_hash: Manifest information for `ticket_currency_item_hash`
        manifest_ticket_vendor_hash: Manifest information for `ticket_vendor_hash`
        manifest_triumphs_presentation_node_hash: Manifest information for `triumphs_presentation_node_hash`
    """

    color: "DestinyColor" = attr.field()
    display_properties: "DestinyDisplayPropertiesDefinition" = attr.field()
    end_time: int = attr.field()
    hash: int = attr.field()
    images: "DestinyEventCardImages" = attr.field()
    index: int = attr.field()
    link_redirect_path: str = attr.field()
    redacted: bool = attr.field()
    seal_presentation_node_hash: int = attr.field()
    ticket_currency_item_hash: int = attr.field()
    ticket_vendor_category_hash: int = attr.field()
    ticket_vendor_hash: int = attr.field()
    triumphs_presentation_node_hash: int = attr.field()
    manifest_seal_presentation_node_hash: Optional["DestinyPresentationNodeDefinition"] = attr.field(default=None)
    manifest_ticket_currency_item_hash: Optional["DestinyInventoryItemDefinition"] = attr.field(default=None)
    manifest_ticket_vendor_hash: Optional["DestinyVendorDefinition"] = attr.field(default=None)
    manifest_triumphs_presentation_node_hash: Optional["DestinyPresentationNodeDefinition"] = attr.field(default=None)


@attr.define
class DestinyEventCardImages(BaseModel):
    """
    _No description given by bungie._

    None
    Attributes:
        card_complete_image_path: _No description given by bungie._
        card_complete_wrap_image_path: _No description given by bungie._
        card_incomplete_image_path: _No description given by bungie._
        progress_icon_image_path: _No description given by bungie._
        theme_background_image_path: _No description given by bungie._
        unowned_card_sleeve_image_path: _No description given by bungie._
        unowned_card_sleeve_wrap_image_path: _No description given by bungie._
    """

    card_complete_image_path: str = attr.field()
    card_complete_wrap_image_path: str = attr.field()
    card_incomplete_image_path: str = attr.field()
    progress_icon_image_path: str = attr.field()
    theme_background_image_path: str = attr.field()
    unowned_card_sleeve_image_path: str = attr.field()
    unowned_card_sleeve_wrap_image_path: str = attr.field()
