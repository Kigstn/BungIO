import datetime
from typing import Any, Optional

import attr

from bungio.models.auth import AuthData
from bungio.models.base import BaseModel


@attr.define
class GetAvailableLocalesRouteInterface(BaseModel):
    async def get_available_locales(self, auth: Optional[AuthData] = None) -> Any:
        """
        List of available localization cultures

        Args:
            auth: Authentication information. Required when users with a private profile are queried.

        Returns:
            The [model](/API Reference/Models/Bungie API Models//#.Any) which is returned by bungie.
            Click [here](https://bungie-net.github.io/multi/index.html) for general endpoint information.
        """

        response = await self._client.http.get_available_locales(auth=auth)
        return response["Result"]
