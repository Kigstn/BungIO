# DO NOT CHANGE ANY CODE BELOW
# This file is generated automatically by `generate_api_schema.py` and will be overwritten
# Instead, change functions / models by subclassing them in the `./overwrites/` folder. They will be used instead.

from datetime import datetime
from typing import TYPE_CHECKING, Union

import attr

from bungio.models.base import BaseEnum, BaseModel
from bungio.utils import enum_converter

if TYPE_CHECKING:
    from bungio.models import BungieMembershipType


@attr.define
class AwaInitializeResponse(BaseModel):
    """
    _No description given by bungie._

    None
    Attributes:
        correlation_id: ID used to get the token. Present this ID to the user as it will identify this specific request on their device.
        sent_to_self: True if the PUSH message will only be sent to the device that made this request.
    """

    correlation_id: str = attr.field()
    sent_to_self: bool = attr.field()


@attr.define
class AwaPermissionRequested(BaseModel):
    """
    _No description given by bungie._

    None
    Attributes:
        affected_item_id: Item instance ID the action shall be applied to. This is optional for all but a new AwaType values. Rule of thumb is to provide the item instance ID if one is available.
        character_id: Destiny character ID, if applicable, that will be affected by the action.
        membership_type: Destiny membership type of the account to modify.
        type: Type of advanced write action.
    """

    affected_item_id: int = attr.field()
    character_id: int = attr.field()
    membership_type: Union["BungieMembershipType", int] = attr.field(converter=enum_converter("BungieMembershipType"))
    type: Union["AwaType", int] = attr.field(converter=enum_converter("AwaType"))


class AwaType(BaseEnum):
    """
    _No description given by bungie._
    """

    NONE = 0
    """_No description given by bungie._ """
    INSERT_PLUGS = 1
    """Insert plugs into sockets. """


@attr.define
class AwaUserResponse(BaseModel):
    """
    _No description given by bungie._

    None
    Attributes:
        correlation_id: Correlation ID of the request
        nonce: Secret nonce received via the PUSH notification.
        selection: Indication of the selection the user has made (Approving or rejecting the action)
    """

    correlation_id: str = attr.field()
    nonce: list[int] = attr.field(metadata={"type": """list[int]"""})
    selection: Union["AwaUserSelection", int] = attr.field(converter=enum_converter("AwaUserSelection"))


class AwaUserSelection(BaseEnum):
    """
    _No description given by bungie._
    """

    NONE = 0
    """_No description given by bungie._ """
    REJECTED = 1
    """_No description given by bungie._ """
    APPROVED = 2
    """_No description given by bungie._ """


@attr.define
class AwaAuthorizationResult(BaseModel):
    """
    _No description given by bungie._

    None
    Attributes:
        action_token: Credential used to prove the user authorized an advanced write action.
        developer_note: Message to the app developer to help understand the response.
        maximum_number_of_uses: This token may be used to perform the requested action this number of times, at a maximum. If this value is 0, then there is no limit.
        membership_type: MembershipType from the permission request.
        response_reason: _No description given by bungie._
        type: Advanced Write Action Type from the permission request.
        user_selection: Indication of how the user responded to the request. If the value is "Approved" the actionToken will contain the token that can be presented when performing the advanced write action.
        valid_until: Time, UTC, when token expires.
    """

    action_token: str = attr.field()
    developer_note: str = attr.field()
    maximum_number_of_uses: int = attr.field()
    membership_type: Union["BungieMembershipType", int] = attr.field(converter=enum_converter("BungieMembershipType"))
    response_reason: Union["AwaResponseReason", int] = attr.field(converter=enum_converter("AwaResponseReason"))
    type: Union["AwaType", int] = attr.field(converter=enum_converter("AwaType"))
    user_selection: Union["AwaUserSelection", int] = attr.field(converter=enum_converter("AwaUserSelection"))
    valid_until: datetime = attr.field()


class AwaResponseReason(BaseEnum):
    """
    _No description given by bungie._
    """

    NONE = 0
    """_No description given by bungie._ """
    ANSWERED = 1
    """User provided an answer """
    TIMED_OUT = 2
    """The HTTP request timed out, a new request may be made and an answer may still be provided. """
    REPLACED = 3
    """This request was replaced by another request. """
