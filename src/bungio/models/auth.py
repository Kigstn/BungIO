from __future__ import annotations

import datetime
from typing import TYPE_CHECKING, Optional, Union

from bungio.models.base import BaseModel, custom_define, custom_field
from bungio.utils import enum_converter

if TYPE_CHECKING:
    from bungio.models import BungieMembershipType

__all__ = ("AuthData",)


@custom_define()
class AuthData(BaseModel):
    """
    Bungie User Authentication Information

    Attributes:
        token: The token. If None, the expiry date has passed, and it has been invalidated.
        token_expiry: The token expiry date
        refresh_token: The refresh token
        refresh_token_expiry: The refresh token expiry date
        membership_type: The `membership_type` of the user this data belongs to
        membership_id: The `membership_id` of the user this data belongs to
        bungie_name: The bungie name of the user this data belongs to. Can be `None` if the user has not launched the game after they got introduced
        cross_save_setup: If the user has cross save set up. If this is `False`, the membership information may be for an unwanted system
    """

    token: Optional[str] = custom_field()
    token_expiry: datetime.datetime = custom_field()
    refresh_token: str = custom_field()
    refresh_token_expiry: datetime.datetime = custom_field()
    membership_type: Union["BungieMembershipType", int] = custom_field(converter=enum_converter("BungieMembershipType"))
    membership_id: int = custom_field()
    bungie_name: Optional[str] = custom_field()
    cross_save_setup: bool = custom_field(default=True)

    async def refresh(self):
        """
        Check if tokens need to be refreshed and then do that.
        Gets called automatically when doing requests with AuthData.

        Tip: Staying up to date
            This dispatches the `Client.on_token_update()` event

        Raises:
            InvalidAuthentication: If authentication is invalid

        Returns:
            The working authentication info.
        """

        await self._client.get_working_auth(auth=self)
