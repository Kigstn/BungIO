# DO NOT CHANGE ANY CODE BELOW
# This file is generated automatically by `generate_api_schema.py` and will be overwritten
# Instead, change functions / models by subclassing them in the `./overwrites/` folder. They will be used instead.

from typing import Any, Optional

from bungio.models import (
    ContentItemPublicContract,
    ContentTypeDescription,
    NewsArticleRssResponse,
    SearchResultOfContentItemPublicContract,
)
from bungio.models.auth import AuthData
from bungio.models.base import ClientMixin, custom_define


@custom_define()
class ContentRouteInterface(ClientMixin):
    async def get_content_type(self, type: str, auth: Optional[AuthData] = None) -> ContentTypeDescription:
        """
        Gets an object describing a particular variant of content.

        Args:
            type:
            auth: Authentication information. Required when users with a private profile are queried, or when Bungie feels like it

        Returns:
            The model which is returned by bungie. [General endpoint information.](https://bungie-net.github.io/multi/index.html)
        """

        response = await self._client.http.get_content_type(type=type, auth=auth)
        return await ContentTypeDescription.from_dict(data=response, client=self._client, type=type, auth=auth)

    async def get_content_by_id(
        self, id: int, locale: str, head: Optional[bool] = None, auth: Optional[AuthData] = None
    ) -> ContentItemPublicContract:
        """
        Returns a content item referenced by id

        Args:
            id:
            locale:
            head: false
            auth: Authentication information. Required when users with a private profile are queried, or when Bungie feels like it

        Returns:
            The model which is returned by bungie. [General endpoint information.](https://bungie-net.github.io/multi/index.html)
        """

        response = await self._client.http.get_content_by_id(
            id=id, locale=locale, head=head if head is not None else None, auth=auth
        )
        return await ContentItemPublicContract.from_dict(
            data=response, client=self._client, id=id, locale=locale, head=head, auth=auth
        )

    async def get_content_by_tag_and_type(
        self, locale: str, tag: str, type: str, head: Optional[bool] = None, auth: Optional[AuthData] = None
    ) -> ContentItemPublicContract:
        """
        Returns the newest item that matches a given tag and Content Type.

        Args:
            locale:
            tag:
            type:
            head: Not used.
            auth: Authentication information. Required when users with a private profile are queried, or when Bungie feels like it

        Returns:
            The model which is returned by bungie. [General endpoint information.](https://bungie-net.github.io/multi/index.html)
        """

        response = await self._client.http.get_content_by_tag_and_type(
            locale=locale, tag=tag, type=type, head=head if head is not None else None, auth=auth
        )
        return await ContentItemPublicContract.from_dict(
            data=response, client=self._client, locale=locale, tag=tag, type=type, head=head, auth=auth
        )

    async def search_content_with_text(
        self,
        locale: str,
        ctype: Optional[str] = None,
        currentpage: Optional[int] = None,
        head: Optional[bool] = None,
        searchtext: Optional[str] = None,
        source: Optional[str] = None,
        tag: Optional[str] = None,
        auth: Optional[AuthData] = None,
    ) -> SearchResultOfContentItemPublicContract:
        """
        Gets content based on querystring information passed in. Provides basic search and text search capabilities.

        Args:
            locale:
            ctype: Content type tag: Help, News, etc. Supply multiple ctypes separated by space.
            currentpage: Page number for the search results, starting with page 1.
            head: Not used.
            searchtext: Word or phrase for the search.
            source: For analytics, hint at the part of the app that triggered the search. Optional.
            tag: Tag used on the content to be searched.
            auth: Authentication information. Required when users with a private profile are queried, or when Bungie feels like it

        Returns:
            The model which is returned by bungie. [General endpoint information.](https://bungie-net.github.io/multi/index.html)
        """

        response = await self._client.http.search_content_with_text(
            locale=locale,
            ctype=ctype if ctype is not None else None,
            currentpage=currentpage if currentpage is not None else None,
            head=head if head is not None else None,
            searchtext=searchtext if searchtext is not None else None,
            source=source if source is not None else None,
            tag=tag if tag is not None else None,
            auth=auth,
        )
        return await SearchResultOfContentItemPublicContract.from_dict(
            data=response,
            client=self._client,
            locale=locale,
            ctype=ctype,
            currentpage=currentpage,
            head=head,
            searchtext=searchtext,
            source=source,
            tag=tag,
            auth=auth,
        )

    async def search_content_by_tag_and_type(
        self,
        locale: str,
        tag: str,
        type: str,
        currentpage: Optional[int] = None,
        head: Optional[bool] = None,
        itemsperpage: Optional[int] = None,
        auth: Optional[AuthData] = None,
    ) -> SearchResultOfContentItemPublicContract:
        """
        Searches for Content Items that match the given Tag and Content Type.

        Args:
            locale:
            tag:
            type:
            currentpage: Page number for the search results starting with page 1.
            head: Not used.
            itemsperpage: Not used.
            auth: Authentication information. Required when users with a private profile are queried, or when Bungie feels like it

        Returns:
            The model which is returned by bungie. [General endpoint information.](https://bungie-net.github.io/multi/index.html)
        """

        response = await self._client.http.search_content_by_tag_and_type(
            locale=locale,
            tag=tag,
            type=type,
            currentpage=currentpage if currentpage is not None else None,
            head=head if head is not None else None,
            itemsperpage=itemsperpage if itemsperpage is not None else None,
            auth=auth,
        )
        return await SearchResultOfContentItemPublicContract.from_dict(
            data=response,
            client=self._client,
            locale=locale,
            tag=tag,
            type=type,
            currentpage=currentpage,
            head=head,
            itemsperpage=itemsperpage,
            auth=auth,
        )

    async def search_help_articles(self, searchtext: str, size: str, auth: Optional[AuthData] = None) -> Any:
        """
        Search for Help Articles.

        Args:
            searchtext:
            size:
            auth: Authentication information. Required when users with a private profile are queried, or when Bungie feels like it

        Returns:
            The model which is returned by bungie. [General endpoint information.](https://bungie-net.github.io/multi/index.html)
        """

        response = await self._client.http.search_help_articles(searchtext=searchtext, size=size, auth=auth)
        return response["Response"]

    async def rss_news_articles(
        self,
        page_token: str,
        categoryfilter: Optional[str] = None,
        includebody: Optional[bool] = None,
        auth: Optional[AuthData] = None,
    ) -> NewsArticleRssResponse:
        """
        Returns a JSON string response that is the RSS feed for news articles.

        Args:
            page_token: Zero-based pagination token for paging through result sets.
            categoryfilter: Optionally filter response to only include news items in a certain category.
            includebody: Optionally include full content body for each news item.
            auth: Authentication information. Required when users with a private profile are queried, or when Bungie feels like it

        Returns:
            The model which is returned by bungie. [General endpoint information.](https://bungie-net.github.io/multi/index.html)
        """

        response = await self._client.http.rss_news_articles(
            page_token=page_token,
            categoryfilter=categoryfilter if categoryfilter is not None else None,
            includebody=includebody if includebody is not None else None,
            auth=auth,
        )
        return await NewsArticleRssResponse.from_dict(
            data=response,
            client=self._client,
            page_token=page_token,
            categoryfilter=categoryfilter,
            includebody=includebody,
            auth=auth,
        )
