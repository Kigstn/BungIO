import datetime
from typing import Callable, Coroutine, Optional

from bungio.http.route import Route
from bungio.models.auth import AuthData


class GlobalAlertsRequests:
    request: Callable[..., Coroutine]

    async def get_global_alerts(self, includestreaming: Optional[bool] = None, auth: Optional[AuthData] = None) -> dict:
        """
        Gets any active global alert for display in the forum banners, help pages, etc. Usually used for DOC alerts.

        Args:
            includestreaming: Determines whether Streaming Alerts are included in results
            auth: Authentication information. Required when users with a private profile are queried.

        Returns:
            The json response
        """

        return await self.request(
            Route(path=f"/GlobalAlerts/", method="GET", includestreaming=includestreaming, auth=auth)
        )
