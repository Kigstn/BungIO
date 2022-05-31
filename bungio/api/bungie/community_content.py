from typing import Optional

import attr

from bungio.models import PostSearchResponse
from bungio.models.auth import AuthData
from bungio.models.base import BaseModel


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
            The model which is returned by bungie. [General endpoint information.](https://bungie-net.github.io/multi/index.html)
        """

        response = await self._client.http.get_community_content(
            media_filter=media_filter, page=page, sort=sort, auth=auth
        )
        return PostSearchResponse.from_dict(data=response, client=self._client)
