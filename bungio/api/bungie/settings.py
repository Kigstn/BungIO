# DO NOT CHANGE ANY CODE BELOW
# This file is generated automatically by `generate_api_schema.py` and will be overwritten
# Instead, change functions / models by subclassing them in the `./overwrites/` folder. They will be used instead.

from typing import Optional

from bungio.models import CoreSettingsConfiguration
from bungio.models.auth import AuthData
from bungio.models.base import ClientMixin, custom_define


@custom_define()
class SettingsRouteInterface(ClientMixin):
    async def get_common_settings(self, auth: Optional[AuthData] = None) -> CoreSettingsConfiguration:
        """
        Get the common settings used by the Bungie.Net environment.

        Args:
            auth: Authentication information. Required when users with a private profile are queried, or when Bungie feels like it

        Returns:
            The model which is returned by bungie. [General endpoint information.](https://bungie-net.github.io/multi/index.html)
        """

        response = await self._client.http.get_common_settings(auth=auth)
        return await CoreSettingsConfiguration.from_dict(data=response, client=self._client, auth=auth)
