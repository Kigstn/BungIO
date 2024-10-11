# DO NOT CHANGE ANY CODE BELOW
# This file is generated automatically by `generate_api_schema.py` and will be overwritten
# Instead, change functions / models by subclassing them in the `./overwrites/` folder. They will be used instead.

from typing import Optional, Union

from bungio.models import CommunityContentSortMode, ForumTopicsCategoryFiltersEnum, PostSearchResponse
from bungio.models.auth import AuthData
from bungio.models.base import ClientMixin, custom_define


@custom_define()
class CommunityContentRouteInterface(ClientMixin):
    async def get_community_content(
        self,
        media_filter: Union[ForumTopicsCategoryFiltersEnum, int],
        page: int,
        sort: Union[CommunityContentSortMode, int],
        auth: Optional[AuthData] = None,
    ) -> PostSearchResponse:
        """
        Returns community content.

        Args:
            media_filter: The type of media to get
            page: Zero based page
            sort: The sort mode.
            auth: Authentication information. Required when users with a private profile are queried, or when Bungie feels like it

        Returns:
            The model which is returned by bungie. [General endpoint information.](https://bungie-net.github.io/multi/index.html)
        """

        response = await self._client.http.get_community_content(
            media_filter=getattr(media_filter, "value", media_filter),
            page=page,
            sort=getattr(sort, "value", sort),
            auth=auth,
        )
        return await PostSearchResponse.from_dict(
            data=response, client=self._client, media_filter=media_filter, page=page, sort=sort, auth=auth
        )
