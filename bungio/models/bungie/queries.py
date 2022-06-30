# DO NOT CHANGE ANY CODE BELOW
# This file is generated automatically by `generate_api_schema.py` and will be overwritten
# Instead, change functions / models by subclassing them in the `./overwrites/` folder. They will be used instead.

import attr

from bungio.models.base import BaseModel


@attr.define
class SearchResult(BaseModel):
    """
    _No description given by bungie._

    None
    Attributes:
        has_more: _No description given by bungie._
        query: _No description given by bungie._
        replacement_continuation_token: _No description given by bungie._
        total_results: _No description given by bungie._
        use_total_results: If useTotalResults is true, then totalResults represents an accurate count. If False, it does not, and may be estimated/only the size of the current page. Either way, you should probably always only trust hasMore. This is a long-held historical throwback to when we used to do paging with known total results. Those queries toasted our database, and we were left to hastily alter our endpoints and create backward- compatible shims, of which useTotalResults is one.
    """

    has_more: bool = attr.field()
    query: "PagedQuery" = attr.field()
    replacement_continuation_token: str = attr.field()
    total_results: int = attr.field()
    use_total_results: bool = attr.field()


@attr.define
class PagedQuery(BaseModel):
    """
    _No description given by bungie._

    None
    Attributes:
        current_page: _No description given by bungie._
        items_per_page: _No description given by bungie._
        request_continuation_token: _No description given by bungie._
    """

    current_page: int = attr.field()
    items_per_page: int = attr.field()
    request_continuation_token: str = attr.field()
