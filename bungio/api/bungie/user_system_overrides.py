from typing import Any, Optional

import attr

from bungio.models.auth import AuthData
from bungio.models.base import BaseModel


@attr.define
class UserSystemOverridesRouteInterface(BaseModel):
    async def get_user_system_overrides(self, auth: Optional[AuthData] = None) -> Any:
        """
        Get the user-specific system overrides that should be respected alongside common systems.

        Args:
            auth: Authentication information. Required when users with a private profile are queried.

        Returns:
            The model which is returned by bungie. [General endpoint information.](https://bungie-net.github.io/multi/index.html)
        """

        response = await self._client.http.get_user_system_overrides(auth=auth)
        return response["Result"]
