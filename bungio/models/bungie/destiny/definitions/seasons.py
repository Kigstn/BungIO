import datetime
from typing import TYPE_CHECKING

import attr

from bungio.models.base import BaseModel

if TYPE_CHECKING:
    from bungio.models import (
        DestinyDisplayPropertiesDefinition,
        DestinySeasonPreviewDefinition,
        DestinySeasonPreviewImageDefinition,
    )


@attr.define
class DestinySeasonDefinition(BaseModel):
    """
    Defines a canonical "Season" of Destiny: a range of a few months where the game highlights certain challenges, provides new loot, has new Clan-related rewards and celebrates various seasonal events.

    Attributes:
        display_properties: _No description given by bungie_
        background_image_path: _No description given by bungie_
        season_number: _No description given by bungie_
        start_date: _No description given by bungie_
        end_date: _No description given by bungie_
        season_pass_hash: _No description given by bungie_
        season_pass_progression_hash: _No description given by bungie_
        artifact_item_hash: _No description given by bungie_
        seal_presentation_node_hash: _No description given by bungie_
        seasonal_challenges_presentation_node_hash: _No description given by bungie_
        preview: Optional - Defines the promotional text, images, and links to preview this season.
        hash: The unique identifier for this entity. Guaranteed to be unique for the type of entity, but not globally. When entities refer to each other in Destiny content, it is this hash that they are referring to.
        index: The index of the entity as it was found in the investment tables.
        redacted: If this is true, then there is an entity with this identifier/type combination, but BNet is not yet allowed to show it. Sorry!
    """

    display_properties: "DestinyDisplayPropertiesDefinition" = attr.field()
    background_image_path: str = attr.field()
    season_number: int = attr.field()
    start_date: datetime.datetime = attr.field()
    end_date: datetime.datetime = attr.field()
    season_pass_hash: int = attr.field()
    season_pass_progression_hash: int = attr.field()
    artifact_item_hash: int = attr.field()
    seal_presentation_node_hash: int = attr.field()
    seasonal_challenges_presentation_node_hash: int = attr.field()
    preview: "DestinySeasonPreviewDefinition" = attr.field()
    hash: int = attr.field()
    index: int = attr.field()
    redacted: bool = attr.field()


@attr.define
class DestinySeasonPreviewDefinition(BaseModel):
    """
    Defines the promotional text, images, and links to preview this season.

    Attributes:
        description: A localized description of the season.
        link_path: A relative path to learn more about the season. Web browsers should be automatically redirected to the user's Bungie.net locale. For example: "/SeasonOfTheChosen" will redirect to "/7/en/Seasons/SeasonOfTheChosen" for English users.
        video_link: An optional link to a localized video, probably YouTube.
        images: A list of images to preview the seasonal content. Should have at least three to show.
    """

    description: str = attr.field()
    link_path: str = attr.field()
    video_link: str = attr.field()
    images: list["DestinySeasonPreviewImageDefinition"] = attr.field()


@attr.define
class DestinySeasonPreviewImageDefinition(BaseModel):
    """
    Defines the thumbnail icon, high-res image, and video link for promotional images

    Attributes:
        thumbnail_image: A thumbnail icon path to preview seasonal content, probably 480x270.
        high_res_image: An optional path to a high-resolution image, probably 1920x1080.
    """

    thumbnail_image: str = attr.field()
    high_res_image: str = attr.field()


@attr.define
class DestinySeasonPassDefinition(BaseModel):
    """
    _No description given by bungie_

    Attributes:
        display_properties: _No description given by bungie_
        reward_progression_hash: This is the progression definition related to the progression for the initial levels 1-100 that provide item rewards for the Season pass. Further experience after you reach the limit is provided in the "Prestige" progression referred to by prestigeProgressionHash.
        prestige_progression_hash: I know what you're thinking, but I promise we're not going to duplicate and drown you. Instead, we're giving you sweet, sweet power bonuses.  Prestige progression is further progression that you can make on the Season pass after you gain max ranks, that will ultimately increase your power/light level over the theoretical limit.
        hash: The unique identifier for this entity. Guaranteed to be unique for the type of entity, but not globally. When entities refer to each other in Destiny content, it is this hash that they are referring to.
        index: The index of the entity as it was found in the investment tables.
        redacted: If this is true, then there is an entity with this identifier/type combination, but BNet is not yet allowed to show it. Sorry!
    """

    display_properties: "DestinyDisplayPropertiesDefinition" = attr.field()
    reward_progression_hash: int = attr.field()
    prestige_progression_hash: int = attr.field()
    hash: int = attr.field()
    index: int = attr.field()
    redacted: bool = attr.field()
