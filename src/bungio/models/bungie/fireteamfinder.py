# DO NOT CHANGE ANY CODE BELOW
# This file is generated automatically by `generate_api_schema.py` and will be overwritten
# Instead, change functions / models by subclassing them in the `./overwrites/` folder. They will be used instead.

from datetime import datetime
from typing import Optional, Union, TYPE_CHECKING

from bungio.utils import enum_converter
from bungio.models.base import BaseModel, BaseEnum, custom_define, custom_field

from bungio.models.mixins import DestinyCharacterMixin

if TYPE_CHECKING:
    from bungio.models import BungieMembershipType
    from bungio.models import DestinyActivityDefinition
    from bungio.models import DestinyFireteamFinderActivityGraphDefinition


class DestinyFireteamFinderApplicationType(BaseEnum):
    """
    _No description given by bungie._
    """

    UNKNOWN = 0
    """_No description given by bungie._ """
    CREATOR = 1
    """_No description given by bungie._ """
    SEARCH = 2
    """_No description given by bungie._ """
    INVITE = 3
    """_No description given by bungie._ """
    FRIEND = 4
    """_No description given by bungie._ """
    ENCOUNTER = 5
    """_No description given by bungie._ """
    PUBLIC = 6
    """_No description given by bungie._ """


@custom_define()
class DestinyFireteamFinderApplyToListingResponse(BaseModel):
    """
    _No description given by bungie._

    None
    Attributes:
        application: _No description given by bungie._
        is_applied: _No description given by bungie._
        listing: _No description given by bungie._
    """

    application: "DestinyFireteamFinderApplication" = custom_field()
    is_applied: bool = custom_field()
    listing: "DestinyFireteamFinderListing" = custom_field()


@custom_define()
class DestinyFireteamFinderApplication(BaseModel):
    """
    _No description given by bungie._

    None
    Attributes:
        applicant_set: _No description given by bungie._
        application_id: _No description given by bungie._
        application_type: _No description given by bungie._
        created_date_time: _No description given by bungie._
        listing_id: _No description given by bungie._
        referral_token: _No description given by bungie._
        revision: _No description given by bungie._
        state: _No description given by bungie._
        submitter_id: _No description given by bungie._
    """

    applicant_set: "DestinyFireteamFinderApplicantSet" = custom_field()
    application_id: int = custom_field(metadata={"int64": True})
    application_type: Union["DestinyFireteamFinderApplicationType", int] = custom_field(
        converter=enum_converter("DestinyFireteamFinderApplicationType")
    )
    created_date_time: datetime = custom_field()
    listing_id: int = custom_field(metadata={"int64": True})
    referral_token: int = custom_field(metadata={"int64": True})
    revision: int = custom_field()
    state: Union["DestinyFireteamFinderApplicationState", int] = custom_field(
        converter=enum_converter("DestinyFireteamFinderApplicationState")
    )
    submitter_id: "DestinyFireteamFinderPlayerId" = custom_field()


class DestinyFireteamFinderApplicationState(BaseEnum):
    """
    _No description given by bungie._
    """

    UNKNOWN = 0
    """_No description given by bungie._ """
    WAITING_FOR_APPLICANTS = 1
    """_No description given by bungie._ """
    WAITING_FOR_LOBBY_OWNER = 2
    """_No description given by bungie._ """
    ACCEPTED = 3
    """_No description given by bungie._ """
    REJECTED = 4
    """_No description given by bungie._ """
    DELETED = 5
    """_No description given by bungie._ """
    EXPIRED = 6
    """_No description given by bungie._ """


@custom_define()
class DestinyFireteamFinderPlayerId(BaseModel, DestinyCharacterMixin):
    """
    _No description given by bungie._

    None
    Attributes:
        character_id: _No description given by bungie._
        membership_id: _No description given by bungie._
        membership_type: _No description given by bungie._
    """

    character_id: int = custom_field(metadata={"int64": True})
    membership_id: int = custom_field(metadata={"int64": True})
    membership_type: Union["BungieMembershipType", int] = custom_field(converter=enum_converter("BungieMembershipType"))


@custom_define()
class DestinyFireteamFinderApplicantSet(BaseModel):
    """
    _No description given by bungie._

    None
    Attributes:
        applicants: _No description given by bungie._
    """

    applicants: list[dict] = custom_field(metadata={"type": """list[dict]"""})


@custom_define()
class DestinyFireteamFinderListing(BaseModel):
    """
    _No description given by bungie._

    None
    Attributes:
        available_slots: _No description given by bungie._
        created_date_time: _No description given by bungie._
        listing_id: _No description given by bungie._
        lobby_id: _No description given by bungie._
        lobby_state: _No description given by bungie._
        owner_id: _No description given by bungie._
        revision: _No description given by bungie._
        settings: _No description given by bungie._
    """

    available_slots: int = custom_field()
    created_date_time: datetime = custom_field()
    listing_id: int = custom_field(metadata={"int64": True})
    lobby_id: int = custom_field(metadata={"int64": True})
    lobby_state: Union["DestinyFireteamFinderLobbyState", int] = custom_field(
        converter=enum_converter("DestinyFireteamFinderLobbyState")
    )
    owner_id: "DestinyFireteamFinderPlayerId" = custom_field()
    revision: int = custom_field()
    settings: "DestinyFireteamFinderLobbySettings" = custom_field()


@custom_define()
class DestinyFireteamFinderLobbySettings(BaseModel):
    """
    _No description given by bungie._

    Tip: Manifest Information
        This model has some attributes which can be filled with additional information found in the manifest (`manifest_...`).
        Without additional work, these attributes will be `None`, since they require additional requests and database lookups.

        To fill the manifest dependent attributes, either:

        - Run `await ThisClass.fetch_manifest_information()`, see [here](/API Reference/Models/base)
        - Set `Client.always_return_manifest_information` to `True`, see [here](/API Reference/client)

    Attributes:
        activity_graph_hash: _No description given by bungie._
        activity_hash: _No description given by bungie._
        clan_id: _No description given by bungie._
        listing_values: _No description given by bungie._
        max_player_count: _No description given by bungie._
        online_players_only: _No description given by bungie._
        privacy_scope: _No description given by bungie._
        scheduled_date_time: _No description given by bungie._
        manifest_activity_graph_hash: Manifest information for `activity_graph_hash`
        manifest_activity_hash: Manifest information for `activity_hash`
    """

    activity_graph_hash: int = custom_field()
    activity_hash: int = custom_field()
    clan_id: int = custom_field(metadata={"int64": True})
    listing_values: list["DestinyFireteamFinderListingValue"] = custom_field(
        metadata={"type": """list[DestinyFireteamFinderListingValue]"""}
    )
    max_player_count: int = custom_field()
    online_players_only: bool = custom_field()
    privacy_scope: Union["DestinyFireteamFinderLobbyPrivacyScope", int] = custom_field(
        converter=enum_converter("DestinyFireteamFinderLobbyPrivacyScope")
    )
    scheduled_date_time: datetime = custom_field()
    manifest_activity_graph_hash: Optional["DestinyFireteamFinderActivityGraphDefinition"] = custom_field(default=None)
    manifest_activity_hash: Optional["DestinyActivityDefinition"] = custom_field(default=None)


class DestinyFireteamFinderLobbyPrivacyScope(BaseEnum):
    """
    _No description given by bungie._
    """

    UNKNOWN = 0
    """_No description given by bungie._ """
    OPEN = 1
    """_No description given by bungie._ """
    APPLICATIONS = 2
    """_No description given by bungie._ """
    CLAN = 3
    """_No description given by bungie._ """
    FRIENDS = 4
    """_No description given by bungie._ """


@custom_define()
class DestinyFireteamFinderListingValue(BaseModel):
    """
    _No description given by bungie._

    None
    Attributes:
        value_type: _No description given by bungie._
        values: _No description given by bungie._
    """

    value_type: int = custom_field()
    values: list[int] = custom_field(metadata={"type": """list[int]"""})


class DestinyFireteamFinderLobbyState(BaseEnum):
    """
    _No description given by bungie._
    """

    UNKNOWN = 0
    """_No description given by bungie._ """
    INACTIVE = 1
    """_No description given by bungie._ """
    ACTIVE = 2
    """_No description given by bungie._ """
    EXPIRED = 3
    """_No description given by bungie._ """
    CLOSED = 4
    """_No description given by bungie._ """
    CANCELED = 5
    """_No description given by bungie._ """
    DELETED = 6
    """_No description given by bungie._ """


@custom_define()
class DestinyFireteamFinderBulkGetListingStatusResponse(BaseModel):
    """
    _No description given by bungie._

    None
    Attributes:
        listing_status: _No description given by bungie._
    """

    listing_status: list["DestinyFireteamFinderListingStatus"] = custom_field(
        metadata={"type": """list[DestinyFireteamFinderListingStatus]"""}
    )


@custom_define()
class DestinyFireteamFinderListingStatus(BaseModel):
    """
    _No description given by bungie._

    None
    Attributes:
        available_slots: _No description given by bungie._
        listing_id: _No description given by bungie._
        listing_revision: _No description given by bungie._
    """

    available_slots: int = custom_field()
    listing_id: int = custom_field(metadata={"int64": True})
    listing_revision: int = custom_field()


@custom_define()
class DestinyFireteamFinderLobbyListingReference(BaseModel):
    """
    _No description given by bungie._

    None
    Attributes:
        listing_id: _No description given by bungie._
        lobby_id: _No description given by bungie._
    """

    listing_id: int = custom_field(metadata={"int64": True})
    lobby_id: int = custom_field(metadata={"int64": True})


@custom_define()
class DestinyFireteamFinderGetApplicationResponse(BaseModel):
    """
    _No description given by bungie._

    None
    Attributes:
        applicant_set: _No description given by bungie._
        application_id: _No description given by bungie._
        application_type: _No description given by bungie._
        created_date_time: _No description given by bungie._
        listing_id: _No description given by bungie._
        referral_token: _No description given by bungie._
        revision: _No description given by bungie._
        state: _No description given by bungie._
        submitter_id: _No description given by bungie._
    """

    applicant_set: "DestinyFireteamFinderApplicantSet" = custom_field()
    application_id: int = custom_field(metadata={"int64": True})
    application_type: Union["DestinyFireteamFinderApplicationType", int] = custom_field(
        converter=enum_converter("DestinyFireteamFinderApplicationType")
    )
    created_date_time: datetime = custom_field()
    listing_id: int = custom_field(metadata={"int64": True})
    referral_token: int = custom_field(metadata={"int64": True})
    revision: int = custom_field()
    state: Union["DestinyFireteamFinderApplicationState", int] = custom_field(
        converter=enum_converter("DestinyFireteamFinderApplicationState")
    )
    submitter_id: "DestinyFireteamFinderPlayerId" = custom_field()


@custom_define()
class DestinyFireteamFinderGetListingApplicationsResponse(BaseModel):
    """
    _No description given by bungie._

    None
    Attributes:
        applications: _No description given by bungie._
        next_page_token: _No description given by bungie._
        page_size: _No description given by bungie._
    """

    applications: list["DestinyFireteamFinderApplication"] = custom_field(
        metadata={"type": """list[DestinyFireteamFinderApplication]"""}
    )
    next_page_token: str = custom_field()
    page_size: int = custom_field()


@custom_define()
class DestinyFireteamFinderLobbyResponse(BaseModel):
    """
    _No description given by bungie._

    None
    Attributes:
        created_date_time: _No description given by bungie._
        listing_id: _No description given by bungie._
        lobby_id: _No description given by bungie._
        owner: _No description given by bungie._
        players: _No description given by bungie._
        revision: _No description given by bungie._
        settings: _No description given by bungie._
        state: _No description given by bungie._
    """

    created_date_time: datetime = custom_field()
    listing_id: int = custom_field(metadata={"int64": True})
    lobby_id: int = custom_field(metadata={"int64": True})
    owner: "DestinyFireteamFinderPlayerId" = custom_field()
    players: list["DestinyFireteamFinderLobbyPlayer"] = custom_field(
        metadata={"type": """list[DestinyFireteamFinderLobbyPlayer]"""}
    )
    revision: int = custom_field()
    settings: "DestinyFireteamFinderLobbySettings" = custom_field()
    state: Union["DestinyFireteamFinderLobbyState", int] = custom_field(
        converter=enum_converter("DestinyFireteamFinderLobbyState")
    )


@custom_define()
class DestinyFireteamFinderLobbyPlayer(BaseModel):
    """
    _No description given by bungie._

    None
    Attributes:
        offer_id: _No description given by bungie._
        player_id: _No description given by bungie._
        referral_token: _No description given by bungie._
        state: _No description given by bungie._
    """

    offer_id: int = custom_field(metadata={"int64": True})
    player_id: "DestinyFireteamFinderPlayerId" = custom_field()
    referral_token: int = custom_field(metadata={"int64": True})
    state: Union["DestinyFireteamFinderPlayerReadinessState", int] = custom_field(
        converter=enum_converter("DestinyFireteamFinderPlayerReadinessState")
    )


class DestinyFireteamFinderPlayerReadinessState(BaseEnum):
    """
    _No description given by bungie._
    """

    UNKNOWN = 0
    """_No description given by bungie._ """
    RESERVED = 1
    """_No description given by bungie._ """
    DISCONNECTED = 2
    """_No description given by bungie._ """
    IN_LOBBY_UNREADY = 3
    """_No description given by bungie._ """
    IN_LOBBY_READY = 4
    """_No description given by bungie._ """
    SUMMONED = 5
    """_No description given by bungie._ """


@custom_define()
class DestinyFireteamFinderGetPlayerLobbiesResponse(BaseModel):
    """
    _No description given by bungie._

    None
    Attributes:
        lobbies: All available lobbies that this player has created or is a member of.
        next_page_token: A string token required to get the next page of results. This will be null or empty if there are no more results.
        page_size: The number of results requested.
    """

    lobbies: list["DestinyFireteamFinderLobbyResponse"] = custom_field(
        metadata={"type": """list[DestinyFireteamFinderLobbyResponse]"""}
    )
    next_page_token: str = custom_field()
    page_size: int = custom_field()


@custom_define()
class DestinyFireteamFinderGetPlayerApplicationsResponse(BaseModel):
    """
    _No description given by bungie._

    None
    Attributes:
        applications: All applications that this player has sent.
        next_page_token: String token to request next page of results.
    """

    applications: list["DestinyFireteamFinderApplication"] = custom_field(
        metadata={"type": """list[DestinyFireteamFinderApplication]"""}
    )
    next_page_token: str = custom_field()


@custom_define()
class DestinyFireteamFinderGetPlayerOffersResponse(BaseModel):
    """
    _No description given by bungie._

    None
    Attributes:
        offers: All offers that this player has recieved.
    """

    offers: list["DestinyFireteamFinderOffer"] = custom_field(metadata={"type": """list[DestinyFireteamFinderOffer]"""})


@custom_define()
class DestinyFireteamFinderOffer(BaseModel):
    """
    _No description given by bungie._

    None
    Attributes:
        application_id: _No description given by bungie._
        created_date_time: _No description given by bungie._
        lobby_id: _No description given by bungie._
        offer_id: _No description given by bungie._
        revision: _No description given by bungie._
        state: _No description given by bungie._
        target_id: _No description given by bungie._
    """

    application_id: int = custom_field(metadata={"int64": True})
    created_date_time: datetime = custom_field()
    lobby_id: int = custom_field(metadata={"int64": True})
    offer_id: int = custom_field(metadata={"int64": True})
    revision: int = custom_field()
    state: Union["DestinyFireteamFinderOfferState", int] = custom_field(
        converter=enum_converter("DestinyFireteamFinderOfferState")
    )
    target_id: "DestinyFireteamFinderPlayerId" = custom_field()


class DestinyFireteamFinderOfferState(BaseEnum):
    """
    _No description given by bungie._
    """

    UNKNOWN = 0
    """_No description given by bungie._ """
    PENDING = 1
    """_No description given by bungie._ """
    ACCEPTED = 2
    """_No description given by bungie._ """
    REJECTED = 3
    """_No description given by bungie._ """
    DELETED = 4
    """_No description given by bungie._ """
    EXPIRED = 5
    """_No description given by bungie._ """


@custom_define()
class DestinyFireteamFinderGetCharacterActivityAccessResponse(BaseModel):
    """
    _No description given by bungie._

    None
    Attributes:
        fireteam_finder_activity_graph_states: A map of fireteam finder activity graph hashes to visibility and availability states.
    """

    fireteam_finder_activity_graph_states: dict[int, "DestinyFireteamFinderActivityGraphState"] = custom_field(
        metadata={"type": """dict[int, DestinyFireteamFinderActivityGraphState]"""}
    )


@custom_define()
class DestinyFireteamFinderActivityGraphState(BaseModel):
    """
    _No description given by bungie._

    None
    Attributes:
        is_available: Indicates if this fireteam finder activity graph node is available to select for this character.
        is_visible: Indicates if this fireteam finder activity graph node is visible for this character.
    """

    is_available: bool = custom_field()
    is_visible: bool = custom_field()


@custom_define()
class DestinyFireteamFinderGetLobbyOffersResponse(BaseModel):
    """
    _No description given by bungie._

    None
    Attributes:
        offers: _No description given by bungie._
        page_token: _No description given by bungie._
    """

    offers: list["DestinyFireteamFinderOffer"] = custom_field(metadata={"type": """list[DestinyFireteamFinderOffer]"""})
    page_token: str = custom_field()


@custom_define()
class DestinyFireteamFinderHostLobbyResponse(BaseModel):
    """
    _No description given by bungie._

    None
    Attributes:
        application_id: _No description given by bungie._
        listing_id: _No description given by bungie._
        lobby_id: _No description given by bungie._
        offer_id: _No description given by bungie._
    """

    application_id: int = custom_field(metadata={"int64": True})
    listing_id: int = custom_field(metadata={"int64": True})
    lobby_id: int = custom_field(metadata={"int64": True})
    offer_id: int = custom_field(metadata={"int64": True})


@custom_define()
class DestinyFireteamFinderHostLobbyRequest(BaseModel):
    """
    _No description given by bungie._

    Tip: Manifest Information
        This model has some attributes which can be filled with additional information found in the manifest (`manifest_...`).
        Without additional work, these attributes will be `None`, since they require additional requests and database lookups.

        To fill the manifest dependent attributes, either:

        - Run `await ThisClass.fetch_manifest_information()`, see [here](/API Reference/Models/base)
        - Set `Client.always_return_manifest_information` to `True`, see [here](/API Reference/client)

    Attributes:
        activity_graph_hash: _No description given by bungie._
        activity_hash: _No description given by bungie._
        clan_id: _No description given by bungie._
        listing_values: _No description given by bungie._
        max_player_count: _No description given by bungie._
        online_players_only: _No description given by bungie._
        privacy_scope: _No description given by bungie._
        scheduled_date_time: _No description given by bungie._
        manifest_activity_graph_hash: Manifest information for `activity_graph_hash`
        manifest_activity_hash: Manifest information for `activity_hash`
    """

    activity_graph_hash: int = custom_field()
    activity_hash: int = custom_field()
    clan_id: int = custom_field(metadata={"int64": True})
    listing_values: list["DestinyFireteamFinderListingValue"] = custom_field(
        metadata={"type": """list[DestinyFireteamFinderListingValue]"""}
    )
    max_player_count: int = custom_field()
    online_players_only: bool = custom_field()
    privacy_scope: Union["DestinyFireteamFinderLobbyPrivacyScope", int] = custom_field(
        converter=enum_converter("DestinyFireteamFinderLobbyPrivacyScope")
    )
    scheduled_date_time: datetime = custom_field()
    manifest_activity_graph_hash: Optional["DestinyFireteamFinderActivityGraphDefinition"] = custom_field(default=None)
    manifest_activity_hash: Optional["DestinyActivityDefinition"] = custom_field(default=None)


@custom_define()
class DestinyFireteamFinderJoinLobbyRequest(BaseModel):
    """
    _No description given by bungie._

    None
    Attributes:
        lobby_id: _No description given by bungie._
        offer_id: _No description given by bungie._
    """

    lobby_id: int = custom_field(metadata={"int64": True})
    offer_id: int = custom_field(metadata={"int64": True})


@custom_define()
class DestinyFireteamFinderKickPlayerRequest(BaseModel):
    """
    _No description given by bungie._

    None
    Attributes:
        target_character_id: _No description given by bungie._
        target_membership_type: _No description given by bungie._
    """

    target_character_id: int = custom_field(metadata={"int64": True})
    target_membership_type: Union["BungieMembershipType", int] = custom_field(
        converter=enum_converter("BungieMembershipType")
    )


@custom_define()
class DestinyFireteamFinderRespondToApplicationResponse(BaseModel):
    """
    _No description given by bungie._

    None
    Attributes:
        application_id: _No description given by bungie._
        application_revision: _No description given by bungie._
    """

    application_id: int = custom_field(metadata={"int64": True})
    application_revision: int = custom_field()


@custom_define()
class DestinyFireteamFinderRespondToApplicationRequest(BaseModel):
    """
    _No description given by bungie._

    None
    Attributes:
        accepted: _No description given by bungie._
    """

    accepted: bool = custom_field()


@custom_define()
class DestinyFireteamFinderRespondToAuthenticationResponse(BaseModel):
    """
    _No description given by bungie._

    None
    Attributes:
        application_id: _No description given by bungie._
        application_revision: _No description given by bungie._
        listing: _No description given by bungie._
        offer: _No description given by bungie._
    """

    application_id: int = custom_field(metadata={"int64": True})
    application_revision: int = custom_field()
    listing: "DestinyFireteamFinderListing" = custom_field()
    offer: "DestinyFireteamFinderOffer" = custom_field()


@custom_define()
class DestinyFireteamFinderRespondToAuthenticationRequest(BaseModel):
    """
    _No description given by bungie._

    None
    Attributes:
        confirmed: _No description given by bungie._
    """

    confirmed: bool = custom_field()


@custom_define()
class DestinyFireteamFinderRespondToOfferResponse(BaseModel):
    """
    _No description given by bungie._

    None
    Attributes:
        offer_id: _No description given by bungie._
        revision: _No description given by bungie._
        state: _No description given by bungie._
    """

    offer_id: int = custom_field(metadata={"int64": True})
    revision: int = custom_field()
    state: Union["DestinyFireteamFinderOfferState", int] = custom_field(
        converter=enum_converter("DestinyFireteamFinderOfferState")
    )


@custom_define()
class DestinyFireteamFinderRespondToOfferRequest(BaseModel):
    """
    _No description given by bungie._

    None
    Attributes:
        accepted: _No description given by bungie._
    """

    accepted: bool = custom_field()


@custom_define()
class DestinyFireteamFinderSearchListingsByClanResponse(BaseModel):
    """
    _No description given by bungie._

    None
    Attributes:
        listings: _No description given by bungie._
        page_token: _No description given by bungie._
    """

    listings: list["DestinyFireteamFinderListing"] = custom_field(
        metadata={"type": """list[DestinyFireteamFinderListing]"""}
    )
    page_token: str = custom_field()


@custom_define()
class DestinyFireteamFinderSearchListingsByClanRequest(BaseModel):
    """
    _No description given by bungie._

    None
    Attributes:
        lobby_state: _No description given by bungie._
        page_size: _No description given by bungie._
        page_token: _No description given by bungie._
    """

    lobby_state: Union["DestinyFireteamFinderLobbyState", int] = custom_field(
        converter=enum_converter("DestinyFireteamFinderLobbyState")
    )
    page_size: int = custom_field()
    page_token: str = custom_field()


@custom_define()
class DestinyFireteamFinderSearchListingsByFiltersResponse(BaseModel):
    """
    _No description given by bungie._

    None
    Attributes:
        listings: _No description given by bungie._
        page_token: _No description given by bungie._
    """

    listings: list["DestinyFireteamFinderListing"] = custom_field(
        metadata={"type": """list[DestinyFireteamFinderListing]"""}
    )
    page_token: str = custom_field()


@custom_define()
class DestinyFireteamFinderSearchListingsByFiltersRequest(BaseModel):
    """
    _No description given by bungie._

    None
    Attributes:
        filters: _No description given by bungie._
        lobby_state: _No description given by bungie._
        page_size: _No description given by bungie._
        page_token: _No description given by bungie._
    """

    filters: list["DestinyFireteamFinderListingFilter"] = custom_field(
        metadata={"type": """list[DestinyFireteamFinderListingFilter]"""}
    )
    lobby_state: Union["DestinyFireteamFinderLobbyState", int] = custom_field(
        converter=enum_converter("DestinyFireteamFinderLobbyState")
    )
    page_size: int = custom_field()
    page_token: str = custom_field()


@custom_define()
class DestinyFireteamFinderListingFilter(BaseModel):
    """
    _No description given by bungie._

    None
    Attributes:
        listing_value: _No description given by bungie._
        match_type: _No description given by bungie._
        range_type: _No description given by bungie._
    """

    listing_value: "DestinyFireteamFinderListingValue" = custom_field()
    match_type: Union["DestinyFireteamFinderListingFilterMatchType", int] = custom_field(
        converter=enum_converter("DestinyFireteamFinderListingFilterMatchType")
    )
    range_type: Union["DestinyFireteamFinderListingFilterRangeType", int] = custom_field(
        converter=enum_converter("DestinyFireteamFinderListingFilterRangeType")
    )


class DestinyFireteamFinderListingFilterRangeType(BaseEnum):
    """
    _No description given by bungie._
    """

    UNKNOWN = 0
    """_No description given by bungie._ """
    ALL = 1
    """_No description given by bungie._ """
    ANY = 2
    """_No description given by bungie._ """
    IN_RANGE_INCLUSIVE = 3
    """_No description given by bungie._ """
    IN_RANGE_EXCLUSIVE = 4
    """_No description given by bungie._ """
    GREATER_THAN = 5
    """_No description given by bungie._ """
    GREATER_THAN_OR_EQUAL_TO = 6
    """_No description given by bungie._ """
    LESS_THAN = 7
    """_No description given by bungie._ """
    LESS_THAN_OR_EQUAL_TO = 8
    """_No description given by bungie._ """


class DestinyFireteamFinderListingFilterMatchType(BaseEnum):
    """
    _No description given by bungie._
    """

    UNKNOWN = 0
    """_No description given by bungie._ """
    MUST_NOT = 1
    """_No description given by bungie._ """
    SHOULD = 2
    """_No description given by bungie._ """
    FILTER = 3
    """_No description given by bungie._ """


@custom_define()
class DestinyFireteamFinderUpdateLobbySettingsResponse(BaseModel):
    """
    _No description given by bungie._

    None
    Attributes:
        updated_listing: _No description given by bungie._
        updated_lobby: _No description given by bungie._
    """

    updated_listing: "DestinyFireteamFinderListing" = custom_field()
    updated_lobby: "DestinyFireteamFinderLobbyResponse" = custom_field()


@custom_define()
class DestinyFireteamFinderUpdateLobbySettingsRequest(BaseModel):
    """
    _No description given by bungie._

    None
    Attributes:
        updated_settings: _No description given by bungie._
    """

    updated_settings: "DestinyFireteamFinderLobbySettings" = custom_field()
