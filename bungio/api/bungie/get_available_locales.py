from typing import Optional

import attr

from bungio.models.auth import AuthData
from bungio.models.base import ClientMixin


@attr.define
class GetAvailableLocalesRouteInterface(ClientMixin):
    async def get_available_locales(self, auth: Optional[AuthData] = None) -> dict[str, str]:
        """
        List of available localization cultures

        Args:
            auth: Authentication information. Required when users with a private profile are queried.

        Returns:
            The model which is returned by bungie. [General endpoint information.](https://bungie-net.github.io/multi/index.html)
        """

        response = await self._client.http.get_available_locales(auth=auth)
        return {key: value async for key, value in response["Response"].items()}
