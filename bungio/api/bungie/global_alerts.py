from typing import Optional

import attr

from bungio.models import GlobalAlert
from bungio.models.auth import AuthData
from bungio.models.base import BaseModel


@attr.define
class GlobalAlertsRouteInterface(BaseModel):
    async def get_global_alerts(
        self, includestreaming: Optional[bool] = None, auth: Optional[AuthData] = None
    ) -> list[GlobalAlert]:
        """
        Gets any active global alert for display in the forum banners, help pages, etc. Usually used for DOC alerts.

        Args:
            includestreaming: Determines whether Streaming Alerts are included in results
            auth: Authentication information. Required when users with a private profile are queried.

        Returns:
            The model which is returned by bungie. [General endpoint information.](https://bungie-net.github.io/multi/index.html)
        """

        response = await self._client.http.get_global_alerts(includestreaming=includestreaming, auth=auth)
        return [await GlobalAlert.from_dict(data=value, client=self._client) for value in response["Result"]]
