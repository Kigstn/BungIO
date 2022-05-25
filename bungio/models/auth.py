import datetime

import attr

from bungio.models.base import BaseModel


@attr.s
class AuthData(BaseModel):
    """
    Bungie User Authentication Information

    Attributes:
        token: The token
        refresh_token: The refresh token
        token_expiry: The token expiry date
        refresh_token_expiry: The refresh token expiry date
    """

    token: str
    refresh_token: str
    token_expiry: datetime.datetime
    refresh_token_expiry: datetime.datetime
