import datetime
from typing import Callable, Coroutine, Optional

from bungio.http.route import Route
from bungio.models.auth import AuthData


class CommunityContentRequests:
    request: Callable[..., Coroutine]

    async def get_community_content(
        self, media_filter: int, page: int, sort: int, auth: Optional[AuthData] = None
    ) -> dict:
        """
        Returns community content.

        Args:
            media_filter: The type of media to get
            page: Zero based page
            sort: The sort mode.
            auth: Authentication information. Required when users with a private profile are queried.

        Returns:
            The json response
        """

        return await self.request(
            Route(path=f"/CommunityContent/Get/{sort}/{media_filter}/{page}/", method="GET", auth=auth)
        )
