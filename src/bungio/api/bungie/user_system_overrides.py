# DO NOT CHANGE ANY CODE BELOW
# This file is generated automatically by `generate_api_schema.py` and will be overwritten
# Instead, change functions / models by subclassing them in the `./overwrites/` folder. They will be used instead.

from typing import Optional

from bungio.models import CoreSystem
from bungio.models.auth import AuthData
from bungio.models.base import ClientMixin, custom_define
from bungio.utils import AllowAsyncIteration


@custom_define()
class UserSystemOverridesRouteInterface(ClientMixin):
    async def get_user_system_overrides(self, auth: Optional[AuthData] = None) -> dict[str, CoreSystem]:
        """
        Get the user-specific system overrides that should be respected alongside common systems.

        Args:
            auth: Authentication information. Required when users with a private profile are queried, or when Bungie feels like it

        Returns:
            The model which is returned by bungie. [General endpoint information.](https://bungie-net.github.io/multi/index.html)
        """

        response = await self._client.http.get_user_system_overrides(auth=auth)
        return {
            key: await CoreSystem.from_dict(data=value, client=self._client, auth=auth)
            async for key, value in AllowAsyncIteration(response["Response"].items())
        }
