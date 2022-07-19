from typing import TYPE_CHECKING, Union

import attr

from bungio.models.mixins import DestinyCharacterMixin
from bungio.utils import enum_converter

if TYPE_CHECKING:
    from bungio.models import BungieMembershipType

__all__ = ("DestinyCharacter",)


@attr.define
class DestinyCharacter(DestinyCharacterMixin):
    """
    A representation of a Destiny 2 character

    Attributes:
        membership_id: The user's id
        membership_type: The user's type, aka platform
        membership_type: The character's id
    """

    membership_id: int = attr.field()
    membership_type: Union["BungieMembershipType", int] = attr.field(converter=enum_converter("BungieMembershipType"))
    character_id: int = attr.field()
