import datetime
from typing import Optional

import attr

from bungio.models import BungieMembershipType
from bungio.models.base import BaseModel


@attr.define
class UserData(BaseModel):
    """
    Bungie User Information

    Attributes:
        membership_type: The `membership_type` of the user this data belongs to
        destiny_membership_id: The `destiny_membership_id` of the user this data belongs to
    """

    membership_type: BungieMembershipType = attr.field()
    destiny_membership_id: int = attr.field()


@attr.define
class AuthData(UserData):
    """
    Bungie User Authentication Information

    Attributes:
        membership_type: The `membership_type` of the user this data belongs to
        destiny_membership_id: The `destiny_membership_id` of the user this data belongs to
        token: The token. If None, the expiry date has passed, and it has been invalidated.
        token_expiry: The token expiry date
        refresh_token: The refresh token
        refresh_token_expiry: The refresh token expiry date
    """

    token: Optional[str] = attr.field()
    token_expiry: datetime.datetime = attr.field()
    refresh_token: str = attr.field()
    refresh_token_expiry: datetime.datetime = attr.field()
