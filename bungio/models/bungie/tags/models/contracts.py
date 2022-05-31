from typing import TYPE_CHECKING

import attr

from bungio.models.base import BaseModel

if TYPE_CHECKING:
    from bungio.models import IgnoreResponse


@attr.define
class TagResponse(BaseModel):
    """
    _No description given by bungie_

    Attributes:
        tag_text: _No description given by bungie_
        ignore_status: _No description given by bungie_
    """

    tag_text: str = attr.field()
    ignore_status: "IgnoreResponse" = attr.field()
