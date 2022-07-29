from typing import TYPE_CHECKING, Union

from bungio.models.base import custom_define, custom_field
from bungio.models.mixins.user import DestinyUserMixin
from bungio.utils import enum_converter

if TYPE_CHECKING:
    from bungio.models import BungieMembershipType

__all__ = ("DestinyUser",)


@custom_define()
class DestinyUser(DestinyUserMixin):
    """
    A representation of a Destiny 2 user

    Attributes:
        membership_id: The user's id
        membership_type: The user's type, aka platform
    """

    membership_id: int = custom_field()
    membership_type: Union["BungieMembershipType", int] = custom_field(converter=enum_converter("BungieMembershipType"))
