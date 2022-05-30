import datetime
from typing import Any, Optional

import attr

from bungio.models.auth import AuthData
from bungio.models.base import BaseModel


@attr.define
class GlobalAlertsRouteInterface(BaseModel):
    async def get_global_alerts(
        self, includestreaming: Optional[bool] = None, auth: Optional[AuthData] = None
    ) -> list[dict]:
        """
        Gets any active global alert for display in the forum banners, help pages, etc. Usually used for DOC alerts.

        Args:
            includestreaming: Determines whether Streaming Alerts are included in results
            auth: Authentication information. Required when users with a private profile are queried.

        Returns:
            The [model](/API Reference/Models/Bungie API Models//#.dict) which is returned by bungie.
            Click [here](https://bungie-net.github.io/multi/index.html) for general endpoint information.
        """

        response = await self._client.http.get_global_alerts(includestreaming=includestreaming, auth=auth)
        return response["Result"]
