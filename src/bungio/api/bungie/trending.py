# DO NOT CHANGE ANY CODE BELOW
# This file is generated automatically by `generate_api_schema.py` and will be overwritten
# Instead, change functions / models by subclassing them in the `./overwrites/` folder. They will be used instead.

from typing import Optional, Union

from bungio.models.base import ClientMixin, custom_define
from bungio.models.auth import AuthData

from bungio.models import SearchResultOfTrendingEntry
from bungio.models import TrendingEntryType
from bungio.models import TrendingDetail
from bungio.models import TrendingCategories


@custom_define()
class TrendingRouteInterface(ClientMixin):
    async def get_trending_categories(self, auth: Optional[AuthData] = None) -> TrendingCategories:
        """
        Returns trending items for Bungie.net, collapsed into the first page of items per category. For pagination within a category, call GetTrendingCategory.

        Args:
            auth: Authentication information. Required when users with a private profile are queried, or when Bungie feels like it

        Returns:
            The model which is returned by bungie. [General endpoint information.](https://bungie-net.github.io/multi/index.html)
        """

        response = await self._client.http.get_trending_categories(auth=auth)
        return await TrendingCategories.from_dict(data=response, client=self._client, auth=auth)

    async def get_trending_category(
        self, category_id: str, page_number: int, auth: Optional[AuthData] = None
    ) -> SearchResultOfTrendingEntry:
        """
        Returns paginated lists of trending items for a category.

        Args:
            category_id: The ID of the category for whom you want additional results.
            page_number: The page # of results to return.
            auth: Authentication information. Required when users with a private profile are queried, or when Bungie feels like it

        Returns:
            The model which is returned by bungie. [General endpoint information.](https://bungie-net.github.io/multi/index.html)
        """

        response = await self._client.http.get_trending_category(
            category_id=category_id, page_number=page_number, auth=auth
        )
        return await SearchResultOfTrendingEntry.from_dict(
            data=response, client=self._client, category_id=category_id, page_number=page_number, auth=auth
        )

    async def get_trending_entry_detail(
        self, identifier: str, trending_entry_type: Union[TrendingEntryType, int], auth: Optional[AuthData] = None
    ) -> TrendingDetail:
        """
        Returns the detailed results for a specific trending entry. Note that trending entries are uniquely identified by a combination of *both* the TrendingEntryType *and* the identifier: the identifier alone is not guaranteed to be globally unique.

        Args:
            identifier: The identifier for the entity to be returned.
            trending_entry_type: The type of entity to be returned.
            auth: Authentication information. Required when users with a private profile are queried, or when Bungie feels like it

        Returns:
            The model which is returned by bungie. [General endpoint information.](https://bungie-net.github.io/multi/index.html)
        """

        response = await self._client.http.get_trending_entry_detail(
            identifier=identifier,
            trending_entry_type=getattr(trending_entry_type, "value", trending_entry_type),
            auth=auth,
        )
        return await TrendingDetail.from_dict(
            data=response,
            client=self._client,
            identifier=identifier,
            trending_entry_type=trending_entry_type,
            auth=auth,
        )
