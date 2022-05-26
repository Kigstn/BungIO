import datetime
from typing import TYPE_CHECKING, Any, Optional

import attr

from bungio.models.base import BaseEnum, BaseModel


@attr.define
class SearchResult(BaseModel):
    """
        Not specified.

        Attributes:
            total_results: Not specified.
            has_more: Not specified.
            query: Not specified.
            replacement_continuation_token: Not specified.
            use_total_results: If useTotalResults is true, then totalResults represents an accurate count.

    If False, it does not, and may be estimated/only the size of the current page.

    Either way, you should probably always only trust hasMore.

    This is a long-held historical throwback to when we used to do paging with known total results. Those queries toasted our database, and we were left to hastily alter our endpoints and create backward- compatible shims, of which useTotalResults is one.
    """

    total_results: int = attr.field()
    has_more: bool = attr.field()
    query: "PagedQuery" = attr.field()
    replacement_continuation_token: str = attr.field()
    use_total_results: bool = attr.field()


@attr.define
class PagedQuery(BaseModel):
    """
    Not specified.

    Attributes:
        items_per_page: Not specified.
        current_page: Not specified.
        request_continuation_token: Not specified.
    """

    items_per_page: int = attr.field()
    current_page: int = attr.field()
    request_continuation_token: str = attr.field()
