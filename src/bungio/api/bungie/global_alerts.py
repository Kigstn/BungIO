# DO NOT CHANGE ANY CODE BELOW
# This file is generated automatically by `generate_api_schema.py` and will be overwritten
# Instead, change functions / models by subclassing them in the `./overwrites/` folder. They will be used instead.

from typing import Optional

from bungio.models.base import ClientMixin, custom_define
from bungio.models.auth import AuthData

from bungio.models import GlobalAlert


@custom_define()
class GlobalAlertsRouteInterface(ClientMixin):
    async def get_global_alerts(
        self, includestreaming: Optional[bool] = None, auth: Optional[AuthData] = None
    ) -> list[GlobalAlert]:
        """
        Gets any active global alert for display in the forum banners, help pages, etc. Usually used for DOC alerts.

        Args:
            includestreaming: Determines whether Streaming Alerts are included in results
            auth: Authentication information. Required when users with a private profile are queried, or when Bungie feels like it

        Returns:
            The model which is returned by bungie. [General endpoint information.](https://bungie-net.github.io/multi/index.html)
        """

        response = await self._client.http.get_global_alerts(
            includestreaming=includestreaming if includestreaming is not None else None, auth=auth
        )
        return [
            await GlobalAlert.from_dict(data=value, client=self._client, includestreaming=includestreaming, auth=auth)
            for value in response["Response"]
        ]
