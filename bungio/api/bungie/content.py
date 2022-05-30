import datetime
from typing import Any, Optional

import attr

from bungio.models.auth import AuthData
from bungio.models.base import BaseModel
from bungio.models.bungie.content import ContentItemPublicContract
from bungio.models.bungie.content.models import ContentTypeDescription


@attr.define
class ContentRouteInterface(BaseModel):
    async def get_content_type(self, type: str, auth: Optional[AuthData] = None) -> ContentTypeDescription:
        """
        Gets an object describing a particular variant of content.

        Args:
            type: Not specified.
            auth: Authentication information. Required when users with a private profile are queried.

        Returns:
            The [model](/API Reference/Models/Bungie API Models/content.models/#bungio.models.bungie.content.models.ContentTypeDescription) which is returned by bungie.
            Click [here](https://bungie-net.github.io/multi/index.html) for general endpoint information.
        """

        response = await self._client.http.get_content_type(type=type, auth=auth)
        return ContentTypeDescription.from_dict(data=response, client=self._client)

    async def get_content_by_id(
        self, id: int, locale: str, head: Optional[bool] = None, auth: Optional[AuthData] = None
    ) -> ContentItemPublicContract:
        """
        Returns a content item referenced by id

        Args:
            id: Not specified.
            locale: Not specified.
            head: false
            auth: Authentication information. Required when users with a private profile are queried.

        Returns:
            The [model](/API Reference/Models/Bungie API Models/content/#bungio.models.bungie.content.ContentItemPublicContract) which is returned by bungie.
            Click [here](https://bungie-net.github.io/multi/index.html) for general endpoint information.
        """

        response = await self._client.http.get_content_by_id(id=id, locale=locale, head=head, auth=auth)
        return ContentItemPublicContract.from_dict(data=response, client=self._client)

    async def get_content_by_tag_and_type(
        self, locale: str, tag: str, type: str, head: Optional[bool] = None, auth: Optional[AuthData] = None
    ) -> ContentItemPublicContract:
        """
        Returns the newest item that matches a given tag and Content Type.

        Args:
            locale: Not specified.
            tag: Not specified.
            type: Not specified.
            head: Not used.
            auth: Authentication information. Required when users with a private profile are queried.

        Returns:
            The [model](/API Reference/Models/Bungie API Models/content/#bungio.models.bungie.content.ContentItemPublicContract) which is returned by bungie.
            Click [here](https://bungie-net.github.io/multi/index.html) for general endpoint information.
        """

        response = await self._client.http.get_content_by_tag_and_type(
            locale=locale, tag=tag, type=type, head=head, auth=auth
        )
        return ContentItemPublicContract.from_dict(data=response, client=self._client)

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
    ) -> dict:
        """
        Gets content based on querystring information passed in. Provides basic search and text search capabilities.

        Args:
            locale: Not specified.
            ctype: Content type tag: Help, News, etc. Supply multiple ctypes separated by space.
            currentpage: Page number for the search results, starting with page 1.
            head: Not used.
            searchtext: Word or phrase for the search.
            source: For analytics, hint at the part of the app that triggered the search. Optional.
            tag: Tag used on the content to be searched.
            auth: Authentication information. Required when users with a private profile are queried.

        Returns:
            The [model](/API Reference/Models/Bungie API Models//#.dict) which is returned by bungie.
            Click [here](https://bungie-net.github.io/multi/index.html) for general endpoint information.
        """

        response = await self._client.http.search_content_with_text(
            locale=locale,
            ctype=ctype,
            currentpage=currentpage,
            head=head,
            searchtext=searchtext,
            source=source,
            tag=tag,
            auth=auth,
        )
        return response["Result"]

    async def search_content_by_tag_and_type(
        self,
        locale: str,
        tag: str,
        type: str,
        currentpage: Optional[int] = None,
        head: Optional[bool] = None,
        itemsperpage: Optional[int] = None,
        auth: Optional[AuthData] = None,
    ) -> dict:
        """
        Searches for Content Items that match the given Tag and Content Type.

        Args:
            locale: Not specified.
            tag: Not specified.
            type: Not specified.
            currentpage: Page number for the search results starting with page 1.
            head: Not used.
            itemsperpage: Not used.
            auth: Authentication information. Required when users with a private profile are queried.

        Returns:
            The [model](/API Reference/Models/Bungie API Models//#.dict) which is returned by bungie.
            Click [here](https://bungie-net.github.io/multi/index.html) for general endpoint information.
        """

        response = await self._client.http.search_content_by_tag_and_type(
            locale=locale, tag=tag, type=type, currentpage=currentpage, head=head, itemsperpage=itemsperpage, auth=auth
        )
        return response["Result"]

    async def search_help_articles(self, searchtext: str, size: str, auth: Optional[AuthData] = None) -> Any:
        """
        Search for Help Articles.

        Args:
            searchtext: Not specified.
            size: Not specified.
            auth: Authentication information. Required when users with a private profile are queried.

        Returns:
            The [model](/API Reference/Models/Bungie API Models//#.Any) which is returned by bungie.
            Click [here](https://bungie-net.github.io/multi/index.html) for general endpoint information.
        """

        response = await self._client.http.search_help_articles(searchtext=searchtext, size=size, auth=auth)
        return response["Result"]
