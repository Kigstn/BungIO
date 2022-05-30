import datetime
from typing import Any, Optional

import attr

from bungio.models.auth import AuthData
from bungio.models.base import BaseModel
from bungio.models.bungie.forum import PostSearchResponse


@attr.define
class CommunityContentRouteInterface(BaseModel):
    async def get_community_content(
        self, media_filter: int, page: int, sort: int, auth: Optional[AuthData] = None
    ) -> PostSearchResponse:
        """
        Returns community content.

        Args:
            media_filter: The type of media to get
            page: Zero based page
            sort: The sort mode.
            auth: Authentication information. Required when users with a private profile are queried.

        Returns:
            The [model](/API Reference/Models/Bungie API Models/forum/#bungio.models.bungie.forum.PostSearchResponse) which is returned by bungie.
            Click [here](https://bungie-net.github.io/multi/index.html) for general endpoint information.
        """

        response = await self._client.http.get_community_content(
            media_filter=media_filter, page=page, sort=sort, auth=auth
        )
        return PostSearchResponse.from_dict(data=response, client=self._client)
