import datetime
from typing import TYPE_CHECKING

import attr

from bungio.models.base import BaseEnum, BaseModel

if TYPE_CHECKING:
    from bungio.models import BungieMembershipType


@attr.define
class AwaInitializeResponse(BaseModel):
    """
    _No description given by bungie_

    Attributes:
        correlation_id: ID used to get the token. Present this ID to the user as it will identify this specific request on their device.
        sent_to_self: True if the PUSH message will only be sent to the device that made this request.
    """

    correlation_id: str = attr.field()
    sent_to_self: bool = attr.field()


@attr.define
class AwaPermissionRequested(BaseModel):
    """
    _No description given by bungie_

    Attributes:
        type: Type of advanced write action.
        affected_item_id: Item instance ID the action shall be applied to. This is optional for all but a new AwaType values. Rule of thumb is to provide the item instance ID if one is available.
        membership_type: Destiny membership type of the account to modify.
        character_id: Destiny character ID, if applicable, that will be affected by the action.
    """

    type: "AwaType" = attr.field()
    affected_item_id: int = attr.field()
    membership_type: "BungieMembershipType" = attr.field()
    character_id: int = attr.field()


class AwaType(BaseEnum):
    """
    _No description given by bungie_
    """

    NONE = 0
    """_No description given by bungie_ """
    INSERT_PLUGS = 1
    """Insert plugs into sockets. """


@attr.define
class AwaUserResponse(BaseModel):
    """
    _No description given by bungie_

    Attributes:
        selection: Indication of the selection the user has made (Approving or rejecting the action)
        correlation_id: Correlation ID of the request
        nonce: Secret nonce received via the PUSH notification.
    """

    selection: "AwaUserSelection" = attr.field()
    correlation_id: str = attr.field()
    nonce: list[int] = attr.field()


class AwaUserSelection(BaseEnum):
    """
    _No description given by bungie_
    """

    NONE = 0
    """_No description given by bungie_ """
    REJECTED = 1
    """_No description given by bungie_ """
    APPROVED = 2
    """_No description given by bungie_ """


@attr.define
class AwaAuthorizationResult(BaseModel):
    """
    _No description given by bungie_

    Attributes:
        user_selection: Indication of how the user responded to the request. If the value is "Approved" the actionToken will contain the token that can be presented when performing the advanced write action.
        response_reason: _No description given by bungie_
        developer_note: Message to the app developer to help understand the response.
        action_token: Credential used to prove the user authorized an advanced write action.
        maximum_number_of_uses: This token may be used to perform the requested action this number of times, at a maximum. If this value is 0, then there is no limit.
        valid_until: Time, UTC, when token expires.
        type: Advanced Write Action Type from the permission request.
        membership_type: MembershipType from the permission request.
    """

    user_selection: "AwaUserSelection" = attr.field()
    response_reason: "AwaResponseReason" = attr.field()
    developer_note: str = attr.field()
    action_token: str = attr.field()
    maximum_number_of_uses: int = attr.field()
    valid_until: datetime.datetime = attr.field()
    type: "AwaType" = attr.field()
    membership_type: "BungieMembershipType" = attr.field()


class AwaResponseReason(BaseEnum):
    """
    _No description given by bungie_
    """

    NONE = 0
    """_No description given by bungie_ """
    ANSWERED = 1
    """User provided an answer """
    TIMED_OUT = 2
    """The HTTP request timed out, a new request may be made and an answer may still be provided. """
    REPLACED = 3
    """This request was replaced by another request. """
