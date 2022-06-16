import datetime
from typing import Optional

import attr

from bungio.models import ApiUsage, Application
from bungio.models.auth import AuthData
from bungio.models.base import BaseModel


@attr.define
class AppRouteInterface(BaseModel):
    async def get_application_api_usage(
        self,
        application_id: int,
        auth: AuthData,
        end: Optional[datetime.datetime] = None,
        start: Optional[datetime.datetime] = None,
    ) -> ApiUsage:
        """
        Get API usage by application for time frame specified. You can go as far back as 30 days ago, and can ask for up to a 48 hour window of time in a single request. You must be authenticated with at least the ReadUserData permission to access this endpoint.

        Warning: Requires Authentication.
            Required oauth2 scopes: ReadUserData

        Args:
            application_id: ID of the application to get usage statistics.
            auth: Authentication information.
            end: End time for query. Goes to now if not specified.
            start: Start time for query. Goes to 24 hours ago if not specified.

        Returns:
            The model which is returned by bungie. [General endpoint information.](https://bungie-net.github.io/multi/index.html)
        """

        response = await self._client.http.get_application_api_usage(
            application_id=application_id, auth=auth, end=end, start=start
        )
        return await ApiUsage.from_dict(data=response, client=self._client)

    async def get_bungie_applications(self, auth: Optional[AuthData] = None) -> list[Application]:
        """
        Get list of applications created by Bungie.

        Args:
            auth: Authentication information. Required when users with a private profile are queried.

        Returns:
            The model which is returned by bungie. [General endpoint information.](https://bungie-net.github.io/multi/index.html)
        """

        response = await self._client.http.get_bungie_applications(auth=auth)
        return [await Application.from_dict(data=value, client=self._client) for value in response["Result"]]
