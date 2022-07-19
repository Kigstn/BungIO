from typing import TYPE_CHECKING, Union

import attr

from bungio.models.base import MISSING, BaseModel
from bungio.utils import enum_converter

if TYPE_CHECKING:
    from bungio.models import GroupDateRange, GroupSortBy, GroupType


@attr.define
class GroupQuery(BaseModel):
    """
    NOTE: GroupQuery, as of Destiny 2, has essentially two totally different and incompatible "modes". If you are querying for a group, you can pass any of the properties below. If you are querying for a Clan, you MUST NOT pass any of the following properties (they must be null or undefined in your request, not just empty string/default values): - groupMemberCountFilter - localeFilter - tagText If you pass these, you will get a useless InvalidParameters error.

    None
    Attributes:
        creation_date: _No description given by bungie._
        current_page: _No description given by bungie._
        group_member_count_filter: _No description given by bungie._
        group_type: _No description given by bungie._
        items_per_page: _No description given by bungie._
        locale_filter: _No description given by bungie._
        name: _No description given by bungie._
        request_continuation_token: _No description given by bungie._
        sort_by: _No description given by bungie._
        tag_text: _No description given by bungie._
    """

    creation_date: Union["GroupDateRange", int] = attr.field(
        converter=enum_converter("GroupDateRange"), metadata={"type": "GroupDateRange"}, default=MISSING
    )
    current_page: int = attr.field(default=MISSING)
    group_member_count_filter: int = attr.field(default=MISSING)
    group_type: Union["GroupType", int] = attr.field(
        converter=enum_converter("GroupType"), metadata={"type": "GroupType"}, default=MISSING
    )
    items_per_page: int = attr.field(default=MISSING)
    locale_filter: str = attr.field(default=MISSING)
    name: str = attr.field(default=MISSING)
    request_continuation_token: str = attr.field(default=MISSING)
    sort_by: Union["GroupSortBy", int] = attr.field(
        converter=enum_converter("GroupSortBy"), metadata={"type": "GroupSortBy"}, default=MISSING
    )
    tag_text: str = attr.field(default=MISSING)
