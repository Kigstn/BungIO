# DO NOT CHANGE ANY CODE BELOW
# This file is generated automatically by `generate_api_schema.py` and will be overwritten
# Instead, change functions / models by subclassing them in the `./overwrites/` folder. They will be used instead.

from datetime import datetime
from typing import Optional

from bungio.models import ApiUsage, Application
from bungio.models.auth import AuthData
from bungio.models.base import ClientMixin, custom_define


@custom_define()
class AppRouteInterface(ClientMixin):
    async def get_application_api_usage(
        self, application_id: int, auth: AuthData, end: Optional[datetime] = None, start: Optional[datetime] = None
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
            application_id=application_id,
            auth=auth,
            end=end if end is not None else None,
            start=start if start is not None else None,
        )
        return await ApiUsage.from_dict(
            data=response, client=self._client, application_id=application_id, auth=auth, end=end, start=start
        )

    async def get_bungie_applications(self, auth: Optional[AuthData] = None) -> list[Application]:
        """
        Get list of applications created by Bungie.

        Args:
            auth: Authentication information. Required when users with a private profile are queried, or when Bungie feels like it

        Returns:
            The model which is returned by bungie. [General endpoint information.](https://bungie-net.github.io/multi/index.html)
        """

        response = await self._client.http.get_bungie_applications(auth=auth)
        return [
            await Application.from_dict(data=value, client=self._client, auth=auth) for value in response["Response"]
        ]
