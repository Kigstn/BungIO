# DO NOT CHANGE ANY CODE BELOW
# This file is generated automatically by `generate_api_schema.py` and will be overwritten
# Instead, change functions / models by subclassing them in the `./overwrites/` folder. They will be used instead.

from typing import Optional

from bungio.models.auth import AuthData
from bungio.models.base import ClientMixin, custom_define
from bungio.utils import AllowAsyncIteration


@custom_define()
class GetAvailableLocalesRouteInterface(ClientMixin):
    async def get_available_locales(self, auth: Optional[AuthData] = None) -> dict[str, str]:
        """
        List of available localization cultures

        Args:
            auth: Authentication information. Required when users with a private profile are queried, or when Bungie feels like it

        Returns:
            The model which is returned by bungie. [General endpoint information.](https://bungie-net.github.io/multi/index.html)
        """

        response = await self._client.http.get_available_locales(auth=auth)
        return {key: value async for key, value in AllowAsyncIteration(response["Response"].items())}
