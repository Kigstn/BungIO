# DO NOT CHANGE ANY CODE BELOW
# This file is generated automatically by `generate_api_schema.py` and will be overwritten
# Instead, change functions / models by subclassing them in the `./overwrites/` folder. They will be used instead.

from typing import Optional, Union

from bungio.models.base import ClientMixin, custom_define
from bungio.models.auth import AuthData

from bungio.models import ForumTopicsCategoryFiltersEnum
from bungio.models import ForumPostSortEnum
from bungio.models import ForumRecruitmentDetail
from bungio.models import ForumTopicsQuickDateEnum
from bungio.models import TagResponse
from bungio.models import ForumTopicsSortEnum
from bungio.models import PostSearchResponse


@custom_define()
class ForumRouteInterface(ClientMixin):
    async def get_topics_paged(
        self,
        category_filter: Union[ForumTopicsCategoryFiltersEnum, int],
        group: int,
        page: int,
        page_size: int,
        quick_date: Union[ForumTopicsQuickDateEnum, int],
        sort: Union[ForumTopicsSortEnum, int],
        locales: Optional[str] = None,
        tagstring: Optional[str] = None,
        auth: Optional[AuthData] = None,
    ) -> PostSearchResponse:
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

        Returns:
            The model which is returned by bungie. [General endpoint information.](https://bungie-net.github.io/multi/index.html)
        """

        response = await self._client.http.get_topics_paged(
            category_filter=getattr(category_filter, "value", category_filter),
            group=group,
            page=page,
            page_size=page_size,
            quick_date=getattr(quick_date, "value", quick_date),
            sort=getattr(sort, "value", sort),
            locales=locales if locales is not None else None,
            tagstring=tagstring if tagstring is not None else None,
            auth=auth,
        )
        return await PostSearchResponse.from_dict(
            data=response,
            client=self._client,
            category_filter=category_filter,
            group=group,
            page=page,
            page_size=page_size,
            quick_date=quick_date,
            sort=sort,
            locales=locales,
            tagstring=tagstring,
            auth=auth,
        )

    async def get_core_topics_paged(
        self,
        category_filter: Union[ForumTopicsCategoryFiltersEnum, int],
        page: int,
        quick_date: Union[ForumTopicsQuickDateEnum, int],
        sort: Union[ForumTopicsSortEnum, int],
        locales: Optional[str] = None,
        auth: Optional[AuthData] = None,
    ) -> PostSearchResponse:
        """
        Gets a listing of all topics marked as part of the core group.

        Args:
            category_filter: The category filter.
            page: Zero base page
            quick_date: The date filter.
            sort: The sort mode.
            locales: Comma seperated list of locales posts must match to return in the result list. Default 'en'
            auth: Authentication information. Required when users with a private profile are queried, or when Bungie feels like it

        Returns:
            The model which is returned by bungie. [General endpoint information.](https://bungie-net.github.io/multi/index.html)
        """

        response = await self._client.http.get_core_topics_paged(
            category_filter=getattr(category_filter, "value", category_filter),
            page=page,
            quick_date=getattr(quick_date, "value", quick_date),
            sort=getattr(sort, "value", sort),
            locales=locales if locales is not None else None,
            auth=auth,
        )
        return await PostSearchResponse.from_dict(
            data=response,
            client=self._client,
            category_filter=category_filter,
            page=page,
            quick_date=quick_date,
            sort=sort,
            locales=locales,
            auth=auth,
        )

    async def get_posts_threaded_paged(
        self,
        get_parent_post: bool,
        page: int,
        page_size: int,
        parent_post_id: int,
        reply_size: int,
        root_thread_mode: bool,
        sort_mode: Union[ForumPostSortEnum, int],
        showbanned: Optional[str] = None,
        auth: Optional[AuthData] = None,
    ) -> PostSearchResponse:
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

        Returns:
            The model which is returned by bungie. [General endpoint information.](https://bungie-net.github.io/multi/index.html)
        """

        response = await self._client.http.get_posts_threaded_paged(
            get_parent_post=get_parent_post,
            page=page,
            page_size=page_size,
            parent_post_id=parent_post_id,
            reply_size=reply_size,
            root_thread_mode=root_thread_mode,
            sort_mode=getattr(sort_mode, "value", sort_mode),
            showbanned=showbanned if showbanned is not None else None,
            auth=auth,
        )
        return await PostSearchResponse.from_dict(
            data=response,
            client=self._client,
            get_parent_post=get_parent_post,
            page=page,
            page_size=page_size,
            parent_post_id=parent_post_id,
            reply_size=reply_size,
            root_thread_mode=root_thread_mode,
            sort_mode=sort_mode,
            showbanned=showbanned,
            auth=auth,
        )

    async def get_posts_threaded_paged_from_child(
        self,
        child_post_id: int,
        page: int,
        page_size: int,
        reply_size: int,
        root_thread_mode: bool,
        sort_mode: Union[ForumPostSortEnum, int],
        showbanned: Optional[str] = None,
        auth: Optional[AuthData] = None,
    ) -> PostSearchResponse:
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

        Returns:
            The model which is returned by bungie. [General endpoint information.](https://bungie-net.github.io/multi/index.html)
        """

        response = await self._client.http.get_posts_threaded_paged_from_child(
            child_post_id=child_post_id,
            page=page,
            page_size=page_size,
            reply_size=reply_size,
            root_thread_mode=root_thread_mode,
            sort_mode=getattr(sort_mode, "value", sort_mode),
            showbanned=showbanned if showbanned is not None else None,
            auth=auth,
        )
        return await PostSearchResponse.from_dict(
            data=response,
            client=self._client,
            child_post_id=child_post_id,
            page=page,
            page_size=page_size,
            reply_size=reply_size,
            root_thread_mode=root_thread_mode,
            sort_mode=sort_mode,
            showbanned=showbanned,
            auth=auth,
        )

    async def get_post_and_parent(
        self, child_post_id: int, showbanned: Optional[str] = None, auth: Optional[AuthData] = None
    ) -> PostSearchResponse:
        """
        Returns the post specified and its immediate parent.

        Args:
            child_post_id:
            showbanned: If this value is not null or empty, banned posts are requested to be returned
            auth: Authentication information. Required when users with a private profile are queried, or when Bungie feels like it

        Returns:
            The model which is returned by bungie. [General endpoint information.](https://bungie-net.github.io/multi/index.html)
        """

        response = await self._client.http.get_post_and_parent(
            child_post_id=child_post_id, showbanned=showbanned if showbanned is not None else None, auth=auth
        )
        return await PostSearchResponse.from_dict(
            data=response, client=self._client, child_post_id=child_post_id, showbanned=showbanned, auth=auth
        )

    async def get_post_and_parent_awaiting_approval(
        self, child_post_id: int, showbanned: Optional[str] = None, auth: Optional[AuthData] = None
    ) -> PostSearchResponse:
        """
        Returns the post specified and its immediate parent of posts that are awaiting approval.

        Args:
            child_post_id:
            showbanned: If this value is not null or empty, banned posts are requested to be returned
            auth: Authentication information. Required when users with a private profile are queried, or when Bungie feels like it

        Returns:
            The model which is returned by bungie. [General endpoint information.](https://bungie-net.github.io/multi/index.html)
        """

        response = await self._client.http.get_post_and_parent_awaiting_approval(
            child_post_id=child_post_id, showbanned=showbanned if showbanned is not None else None, auth=auth
        )
        return await PostSearchResponse.from_dict(
            data=response, client=self._client, child_post_id=child_post_id, showbanned=showbanned, auth=auth
        )

    async def get_topic_for_content(self, content_id: int, auth: Optional[AuthData] = None) -> int:
        """
        Gets the post Id for the given content item's comments, if it exists.

        Args:
            content_id:
            auth: Authentication information. Required when users with a private profile are queried, or when Bungie feels like it

        Returns:
            The model which is returned by bungie. [General endpoint information.](https://bungie-net.github.io/multi/index.html)
        """

        response = await self._client.http.get_topic_for_content(content_id=content_id, auth=auth)
        return response["Response"]

    async def get_forum_tag_suggestions(
        self, partialtag: Optional[str] = None, auth: Optional[AuthData] = None
    ) -> list[TagResponse]:
        """
        Gets tag suggestions based on partial text entry, matching them with other tags previously used in the forums.

        Args:
            partialtag: The partial tag input to generate suggestions from.
            auth: Authentication information. Required when users with a private profile are queried, or when Bungie feels like it

        Returns:
            The model which is returned by bungie. [General endpoint information.](https://bungie-net.github.io/multi/index.html)
        """

        response = await self._client.http.get_forum_tag_suggestions(
            partialtag=partialtag if partialtag is not None else None, auth=auth
        )
        return [
            await TagResponse.from_dict(data=value, client=self._client, partialtag=partialtag, auth=auth)
            for value in response["Response"]
        ]

    async def get_poll(self, topic_id: int, auth: Optional[AuthData] = None) -> PostSearchResponse:
        """
        Gets the specified forum poll.

        Args:
            topic_id: The post id of the topic that has the poll.
            auth: Authentication information. Required when users with a private profile are queried, or when Bungie feels like it

        Returns:
            The model which is returned by bungie. [General endpoint information.](https://bungie-net.github.io/multi/index.html)
        """

        response = await self._client.http.get_poll(topic_id=topic_id, auth=auth)
        return await PostSearchResponse.from_dict(data=response, client=self._client, topic_id=topic_id, auth=auth)

    async def get_recruitment_thread_summaries(
        self, data: list[int], auth: Optional[AuthData] = None
    ) -> list[ForumRecruitmentDetail]:
        """
        Allows the caller to get a list of to 25 recruitment thread summary information objects.

        Args:
            data: The required data for this request.
            auth: Authentication information. Required when users with a private profile are queried, or when Bungie feels like it

        Returns:
            The model which is returned by bungie. [General endpoint information.](https://bungie-net.github.io/multi/index.html)
        """

        response = await self._client.http.get_recruitment_thread_summaries(
            auth=auth, **data.to_dict(_return_to_bungie_case=False)
        )
        return [
            await ForumRecruitmentDetail.from_dict(data=value, client=self._client, auth=auth)
            for value in response["Response"]
        ]
