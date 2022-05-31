from typing import TYPE_CHECKING

import attr

from bungio.models.base import BaseModel

if TYPE_CHECKING:
    from bungio.models import PagedQuery


@attr.define
class SearchResult(BaseModel):
    """
    _No description given by bungie_

    Attributes:
        total_results: _No description given by bungie_
        has_more: _No description given by bungie_
        query: _No description given by bungie_
        replacement_continuation_token: _No description given by bungie_
        use_total_results: If useTotalResults is true, then totalResults represents an accurate count. If False, it does not, and may be estimated/only the size of the current page. Either way, you should probably always only trust hasMore. This is a long-held historical throwback to when we used to do paging with known total results. Those queries toasted our database, and we were left to hastily alter our endpoints and create backward- compatible shims, of which useTotalResults is one.
    """

    total_results: int = attr.field()
    has_more: bool = attr.field()
    query: "PagedQuery" = attr.field()
    replacement_continuation_token: str = attr.field()
    use_total_results: bool = attr.field()


@attr.define
class PagedQuery(BaseModel):
    """
    _No description given by bungie_

    Attributes:
        items_per_page: _No description given by bungie_
        current_page: _No description given by bungie_
        request_continuation_token: _No description given by bungie_
    """

    items_per_page: int = attr.field()
    current_page: int = attr.field()
    request_continuation_token: str = attr.field()
