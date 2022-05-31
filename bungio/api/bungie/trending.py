from typing import Optional

import attr

from bungio.models import (
    SearchResultOfTrendingEntry,
    TrendingCategories,
    TrendingDetail,
)
from bungio.models.auth import AuthData
from bungio.models.base import BaseModel


@attr.define
class TrendingRouteInterface(BaseModel):
    async def get_trending_categories(self, auth: Optional[AuthData] = None) -> TrendingCategories:
        """
        Returns trending items for Bungie.net, collapsed into the first page of items per category. For pagination within a category, call GetTrendingCategory.

        Args:
            auth: Authentication information. Required when users with a private profile are queried.

        Returns:
            The model which is returned by bungie. [General endpoint information.](https://bungie-net.github.io/multi/index.html)
        """

        response = await self._client.http.get_trending_categories(auth=auth)
        return TrendingCategories.from_dict(data=response, client=self._client)

    async def get_trending_category(
        self, category_id: str, page_number: int, auth: Optional[AuthData] = None
    ) -> SearchResultOfTrendingEntry:
        """
        Returns paginated lists of trending items for a category.

        Args:
            category_id: The ID of the category for whom you want additional results.
            page_number: The page # of results to return.
            auth: Authentication information. Required when users with a private profile are queried.

        Returns:
            The model which is returned by bungie. [General endpoint information.](https://bungie-net.github.io/multi/index.html)
        """

        response = await self._client.http.get_trending_category(
            category_id=category_id, page_number=page_number, auth=auth
        )
        return SearchResultOfTrendingEntry.from_dict(data=response, client=self._client)

    async def get_trending_entry_detail(
        self, identifier: str, trending_entry_type: int, auth: Optional[AuthData] = None
    ) -> TrendingDetail:
        """
        Returns the detailed results for a specific trending entry. Note that trending entries are uniquely identified by a combination of *both* the TrendingEntryType *and* the identifier: the identifier alone is not guaranteed to be globally unique.

        Args:
            identifier: The identifier for the entity to be returned.
            trending_entry_type: The type of entity to be returned.
            auth: Authentication information. Required when users with a private profile are queried.

        Returns:
            The model which is returned by bungie. [General endpoint information.](https://bungie-net.github.io/multi/index.html)
        """

        response = await self._client.http.get_trending_entry_detail(
            identifier=identifier, trending_entry_type=trending_entry_type, auth=auth
        )
        return TrendingDetail.from_dict(data=response, client=self._client)
