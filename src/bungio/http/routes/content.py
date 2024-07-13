from typing import Callable, Coroutine, Optional

from bungio.http.route import Route
from bungio.models.auth import AuthData


class ContentRouteHttpRequests:
    request: Callable[..., Coroutine]

    async def get_content_type(self, type: str, auth: Optional[AuthData] = None, *args, **kwargs) -> dict:
        """
        Gets an object describing a particular variant of content.

        Args:
            type:
            auth: Authentication information. Required when users with a private profile are queried, or when Bungie feels like it

        Raises:
            NotFound: 404 request
            BadRequest: 400 request
            InvalidAuthentication: If authentication is invalid
            TimeoutException: If no connection could be made
            BungieDead: Servers are down
            AuthenticationTooSlow: The authentication key has expired
            BungieException: Relaying the bungie error

        Returns:
            The json response
        """

        return await self.request(Route(path=f"/Content/GetContentType/{type}/", method="GET", auth=auth))

    async def get_content_by_id(
        self, id: int, locale: str, head: Optional[bool] = None, auth: Optional[AuthData] = None, *args, **kwargs
    ) -> dict:
        """
        Returns a content item referenced by id

        Args:
            id:
            locale:
            head: false
            auth: Authentication information. Required when users with a private profile are queried, or when Bungie feels like it

        Raises:
            NotFound: 404 request
            BadRequest: 400 request
            InvalidAuthentication: If authentication is invalid
            TimeoutException: If no connection could be made
            BungieDead: Servers are down
            AuthenticationTooSlow: The authentication key has expired
            BungieException: Relaying the bungie error

        Returns:
            The json response
        """

        return await self.request(
            Route(path=f"/Content/GetContentById/{id}/{locale}/", method="GET", head=head, auth=auth)
        )

    async def get_content_by_tag_and_type(
        self,
        locale: str,
        tag: str,
        type: str,
        head: Optional[bool] = None,
        auth: Optional[AuthData] = None,
        *args,
        **kwargs,
    ) -> dict:
        """
        Returns the newest item that matches a given tag and Content Type.

        Args:
            locale:
            tag:
            type:
            head: Not used.
            auth: Authentication information. Required when users with a private profile are queried, or when Bungie feels like it

        Raises:
            NotFound: 404 request
            BadRequest: 400 request
            InvalidAuthentication: If authentication is invalid
            TimeoutException: If no connection could be made
            BungieDead: Servers are down
            AuthenticationTooSlow: The authentication key has expired
            BungieException: Relaying the bungie error

        Returns:
            The json response
        """

        return await self.request(
            Route(path=f"/Content/GetContentByTagAndType/{tag}/{type}/{locale}/", method="GET", head=head, auth=auth)
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
        *args,
        **kwargs,
    ) -> dict:
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

        Raises:
            NotFound: 404 request
            BadRequest: 400 request
            InvalidAuthentication: If authentication is invalid
            TimeoutException: If no connection could be made
            BungieDead: Servers are down
            AuthenticationTooSlow: The authentication key has expired
            BungieException: Relaying the bungie error

        Returns:
            The json response
        """

        return await self.request(
            Route(
                path=f"/Content/Search/{locale}/",
                method="GET",
                ctype=ctype,
                currentpage=currentpage,
                head=head,
                searchtext=searchtext,
                source=source,
                tag=tag,
                auth=auth,
            )
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
        *args,
        **kwargs,
    ) -> dict:
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

        Raises:
            NotFound: 404 request
            BadRequest: 400 request
            InvalidAuthentication: If authentication is invalid
            TimeoutException: If no connection could be made
            BungieDead: Servers are down
            AuthenticationTooSlow: The authentication key has expired
            BungieException: Relaying the bungie error

        Returns:
            The json response
        """

        return await self.request(
            Route(
                path=f"/Content/SearchContentByTagAndType/{tag}/{type}/{locale}/",
                method="GET",
                currentpage=currentpage,
                head=head,
                itemsperpage=itemsperpage,
                auth=auth,
            )
        )

    async def search_help_articles(
        self, searchtext: str, size: str, auth: Optional[AuthData] = None, *args, **kwargs
    ) -> dict:
        """
        Search for Help Articles.

        Args:
            searchtext:
            size:
            auth: Authentication information. Required when users with a private profile are queried, or when Bungie feels like it

        Raises:
            NotFound: 404 request
            BadRequest: 400 request
            InvalidAuthentication: If authentication is invalid
            TimeoutException: If no connection could be made
            BungieDead: Servers are down
            AuthenticationTooSlow: The authentication key has expired
            BungieException: Relaying the bungie error

        Returns:
            The json response
        """

        return await self.request(
            Route(path=f"/Content/SearchHelpArticles/{searchtext}/{size}/", method="GET", auth=auth)
        )

    async def rss_news_articles(
        self,
        page_token: str,
        categoryfilter: Optional[str] = None,
        includebody: Optional[bool] = None,
        auth: Optional[AuthData] = None,
        *args,
        **kwargs,
    ) -> dict:
        """
        Returns a JSON string response that is the RSS feed for news articles.

        Args:
            page_token: Zero-based pagination token for paging through result sets.
            categoryfilter: Optionally filter response to only include news items in a certain category.
            includebody: Optionally include full content body for each news item.
            auth: Authentication information. Required when users with a private profile are queried, or when Bungie feels like it

        Raises:
            NotFound: 404 request
            BadRequest: 400 request
            InvalidAuthentication: If authentication is invalid
            TimeoutException: If no connection could be made
            BungieDead: Servers are down
            AuthenticationTooSlow: The authentication key has expired
            BungieException: Relaying the bungie error

        Returns:
            The json response
        """

        return await self.request(
            Route(
                path=f"/Content/Rss/NewsArticles/{page_token}/",
                method="GET",
                categoryfilter=categoryfilter,
                includebody=includebody,
                auth=auth,
            )
        )
