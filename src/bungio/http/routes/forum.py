from typing import Callable, Coroutine, Optional

from bungio.http.route import Route
from bungio.models.auth import AuthData


class ForumRouteHttpRequests:
    request: Callable[..., Coroutine]

    async def get_topics_paged(
        self,
        category_filter: int,
        group: int,
        page: int,
        page_size: int,
        quick_date: int,
        sort: int,
        locales: Optional[str] = None,
        tagstring: Optional[str] = None,
        auth: Optional[AuthData] = None,
        *args,
        **kwargs,
    ) -> dict:
        """
        Get topics from any forum.

        Args:
            category_filter: A category filter
            group: The group, if any.
            page: Zero paged page number
            page_size: Unused
            quick_date: A date filter.
            sort: The sort mode.
            locales: Comma seperated list of locales posts must match to return in the result list. Default 'en'
            tagstring: The tags to search, if any.
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
                path=f"/Forum/GetTopicsPaged/{page}/{page_size}/{group}/{sort}/{quick_date}/{category_filter}/",
                method="GET",
                locales=locales,
                tagstring=tagstring,
                auth=auth,
            )
        )

    async def get_core_topics_paged(
        self,
        category_filter: int,
        page: int,
        quick_date: int,
        sort: int,
        locales: Optional[str] = None,
        auth: Optional[AuthData] = None,
        *args,
        **kwargs,
    ) -> dict:
        """
        Gets a listing of all topics marked as part of the core group.

        Args:
            category_filter: The category filter.
            page: Zero base page
            quick_date: The date filter.
            sort: The sort mode.
            locales: Comma seperated list of locales posts must match to return in the result list. Default 'en'
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
                path=f"/Forum/GetCoreTopicsPaged/{page}/{sort}/{quick_date}/{category_filter}/",
                method="GET",
                locales=locales,
                auth=auth,
            )
        )

    async def get_posts_threaded_paged(
        self,
        get_parent_post: bool,
        page: int,
        page_size: int,
        parent_post_id: int,
        reply_size: int,
        root_thread_mode: bool,
        sort_mode: int,
        showbanned: Optional[str] = None,
        auth: Optional[AuthData] = None,
        *args,
        **kwargs,
    ) -> dict:
        """
        Returns a thread of posts at the given parent, optionally returning replies to those posts as well as the original parent.

        Args:
            get_parent_post:
            page:
            page_size:
            parent_post_id:
            reply_size:
            root_thread_mode:
            sort_mode:
            showbanned: If this value is not null or empty, banned posts are requested to be returned
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
                path=f"/Forum/GetPostsThreadedPaged/{parent_post_id}/{page}/{page_size}/{reply_size}/{get_parent_post}/{root_thread_mode}/{sort_mode}/",
                method="GET",
                showbanned=showbanned,
                auth=auth,
            )
        )

    async def get_posts_threaded_paged_from_child(
        self,
        child_post_id: int,
        page: int,
        page_size: int,
        reply_size: int,
        root_thread_mode: bool,
        sort_mode: int,
        showbanned: Optional[str] = None,
        auth: Optional[AuthData] = None,
        *args,
        **kwargs,
    ) -> dict:
        """
        Returns a thread of posts starting at the topicId of the input childPostId, optionally returning replies to those posts as well as the original parent.

        Args:
            child_post_id:
            page:
            page_size:
            reply_size:
            root_thread_mode:
            sort_mode:
            showbanned: If this value is not null or empty, banned posts are requested to be returned
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
                path=f"/Forum/GetPostsThreadedPagedFromChild/{child_post_id}/{page}/{page_size}/{reply_size}/{root_thread_mode}/{sort_mode}/",
                method="GET",
                showbanned=showbanned,
                auth=auth,
            )
        )

    async def get_post_and_parent(
        self, child_post_id: int, showbanned: Optional[str] = None, auth: Optional[AuthData] = None, *args, **kwargs
    ) -> dict:
        """
        Returns the post specified and its immediate parent.

        Args:
            child_post_id:
            showbanned: If this value is not null or empty, banned posts are requested to be returned
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
            Route(path=f"/Forum/GetPostAndParent/{child_post_id}/", method="GET", showbanned=showbanned, auth=auth)
        )

    async def get_post_and_parent_awaiting_approval(
        self, child_post_id: int, showbanned: Optional[str] = None, auth: Optional[AuthData] = None, *args, **kwargs
    ) -> dict:
        """
        Returns the post specified and its immediate parent of posts that are awaiting approval.

        Args:
            child_post_id:
            showbanned: If this value is not null or empty, banned posts are requested to be returned
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
                path=f"/Forum/GetPostAndParentAwaitingApproval/{child_post_id}/",
                method="GET",
                showbanned=showbanned,
                auth=auth,
            )
        )

    async def get_topic_for_content(self, content_id: int, auth: Optional[AuthData] = None, *args, **kwargs) -> dict:
        """
        Gets the post Id for the given content item's comments, if it exists.

        Args:
            content_id:
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

        return await self.request(Route(path=f"/Forum/GetTopicForContent/{content_id}/", method="GET", auth=auth))

    async def get_forum_tag_suggestions(
        self, partialtag: Optional[str] = None, auth: Optional[AuthData] = None, *args, **kwargs
    ) -> dict:
        """
        Gets tag suggestions based on partial text entry, matching them with other tags previously used in the forums.

        Args:
            partialtag: The partial tag input to generate suggestions from.
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
            Route(path="/Forum/GetForumTagSuggestions/", method="GET", partialtag=partialtag, auth=auth)
        )

    async def get_poll(self, topic_id: int, auth: Optional[AuthData] = None, *args, **kwargs) -> dict:
        """
        Gets the specified forum poll.

        Args:
            topic_id: The post id of the topic that has the poll.
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

        return await self.request(Route(path=f"/Forum/Poll/{topic_id}/", method="GET", auth=auth))

    async def get_recruitment_thread_summaries(
        self, body_data: list[int], auth: Optional[AuthData] = None, *args, **kwargs
    ) -> dict:
        """
        Allows the caller to get a list of to 25 recruitment thread summary information objects.

        Args:
            body_data: _No description given by bungie._
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

        data = body_data

        return await self.request(Route(path="/Forum/Recruit/Summaries/", method="POST", data=data, auth=auth))
