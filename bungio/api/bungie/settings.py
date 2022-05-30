import datetime
from typing import Any, Optional

import attr

from bungio.models.auth import AuthData
from bungio.models.base import BaseModel
from bungio.models.bungie.common.models import CoreSettingsConfiguration


@attr.define
class SettingsRouteInterface(BaseModel):
    async def get_common_settings(self, auth: Optional[AuthData] = None) -> CoreSettingsConfiguration:
        """
        Get the common settings used by the Bungie.Net environment.

        Args:
            auth: Authentication information. Required when users with a private profile are queried.

        Returns:
            The [model](/API Reference/Models/Bungie API Models/common.models/#bungio.models.bungie.common.models.CoreSettingsConfiguration) which is returned by bungie.
            Click [here](https://bungie-net.github.io/multi/index.html) for general endpoint information.
        """

        response = await self._client.http.get_common_settings(auth=auth)
        return CoreSettingsConfiguration.from_dict(data=response, client=self._client)
