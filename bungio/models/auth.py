import datetime
from typing import Optional

import attr

from bungio.models.base import BaseModel


@attr.define
class AuthData(BaseModel):
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

    membership_type: int
    destiny_membership_id: int

    token: Optional[str]
    token_expiry: datetime.datetime
    refresh_token: str
    refresh_token_expiry: datetime.datetime
