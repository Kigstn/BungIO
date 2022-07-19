from typing import TYPE_CHECKING, Union

import attr

from bungio.models.mixins.user import DestinyUserMixin
from bungio.utils import enum_converter

if TYPE_CHECKING:
    from bungio.models import BungieMembershipType

__all__ = ("DestinyUser",)


@attr.define
class DestinyUser(DestinyUserMixin):
    """
    A representation of a Destiny 2 user

    Attributes:
        membership_id: The user's id
        membership_type: The user's type, aka platform
    """

    membership_id: int = attr.field()
    membership_type: Union["BungieMembershipType", int] = attr.field(converter=enum_converter("BungieMembershipType"))
