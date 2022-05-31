from typing import Any

import attr

from bungio.models.base import BaseModel


@attr.define
class DestinyStringVariablesComponent(BaseModel):
    """
    _No description given_

    Attributes:
        integer_values_by_hash: _No description given_
    """

    integer_values_by_hash: Any = attr.field()
