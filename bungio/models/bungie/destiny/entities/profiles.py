# DO NOT CHANGE ANY CODE BELOW
# This file is generated automatically by `generate_api_schema.py` and will be overwritten
# Instead, change functions / models by subclassing them in the `./overwrites/` folder. They will be used instead.

from datetime import datetime
from typing import TYPE_CHECKING, Optional, Union

import attr

from bungio.models.base import BaseModel
from bungio.utils import enum_converter

if TYPE_CHECKING:
    from bungio.models import (
        DestinyEventCardDefinition,
        DestinyGameVersions,
        DestinySeasonDefinition,
        DestinyVendorReceipt,
        UserInfoCard,
    )


@attr.define
class DestinyVendorReceiptsComponent(BaseModel):
    """
    For now, this isn't used for much: it's a record of the recent refundable purchases that the user has made. In the future, it could be used for providing refunds/buyback via the API. Wouldn't that be fun?

    None
    Attributes:
        receipts: The receipts for refundable purchases made at a vendor.
    """

    receipts: list["DestinyVendorReceipt"] = attr.field(metadata={"type": """list[DestinyVendorReceipt]"""})


@attr.define
class DestinyProfileComponent(BaseModel):
    """
    The most essential summary information about a Profile (in Destiny 1, we called these "Accounts").

    Tip: Manifest Information
        This model has some attributes which can be filled with additional information found in the manifest (`manifest_...`).
        Without additional work, these attributes will be `None`, since they require additional requests and database lookups.

        To fill the manifest dependent attributes, either:

        - Run `await ThisClass.fetch_manifest_information()`, see [here](/API Reference/Models/base)
        - Set `Client.always_return_manifest_information` to `True`, see [here](/API Reference/client)

    Attributes:
        active_event_card_hash: If populated, this is a reference to the event card that is currently active.
        character_ids: A list of the character IDs, for further querying on your part.
        current_season_hash: If populated, this is a reference to the season that is currently active.
        current_season_reward_power_cap: If populated, this is the reward power cap for the current season.
        date_last_played: The last time the user played with any character on this Profile.
        event_card_hashes_owned: A list of hashes for event cards that a profile owns. Unlike most values in versionsOwned, these stay with the profile across all platforms.
        season_hashes: A list of seasons that this profile owns. Unlike versionsOwned, these stay with the profile across Platforms, and thus will be valid.  It turns out that Stadia Pro subscriptions will give access to seasons but only while playing on Stadia and with an active subscription. So some users (users who have Stadia Pro but choose to play on some other platform) won't see these as available: it will be whatever seasons are available for the platform on which they last played.
        user_info: If you need to render the Profile (their platform name, icon, etc...) somewhere, this property contains that information.
        versions_owned: If you want to know what expansions they own, this will contain that data.  IMPORTANT: This field may not return the data you're interested in for Cross-Saved users. It returns the last ownership data we saw for this account - which is to say, what they've purchased on the platform on which they last played, which now could be a different platform.  If you don't care about per-platform ownership and only care about whatever platform it seems they are playing on most recently, then this should be "good enough." Otherwise, this should be considered deprecated. We do not have a good alternative to provide at this time with platform specific ownership data for DLC.
        manifest_active_event_card_hash: Manifest information for `active_event_card_hash`
        manifest_current_season_hash: Manifest information for `current_season_hash`
    """

    active_event_card_hash: int = attr.field()
    character_ids: list[int] = attr.field(metadata={"type": """list[int]"""})
    current_season_hash: int = attr.field()
    current_season_reward_power_cap: int = attr.field()
    date_last_played: datetime = attr.field()
    event_card_hashes_owned: list[int] = attr.field(metadata={"type": """list[int]"""})
    season_hashes: list[int] = attr.field(metadata={"type": """list[int]"""})
    user_info: "UserInfoCard" = attr.field()
    versions_owned: Union["DestinyGameVersions", int] = attr.field(converter=enum_converter("DestinyGameVersions"))
    manifest_active_event_card_hash: Optional["DestinyEventCardDefinition"] = attr.field(default=None)
    manifest_current_season_hash: Optional["DestinySeasonDefinition"] = attr.field(default=None)
