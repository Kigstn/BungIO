from typing import TYPE_CHECKING, Union

from bungio.models.base import custom_define, custom_field
from bungio.models.mixins import DestinyCharacterMixin
from bungio.utils import enum_converter

if TYPE_CHECKING:
    from bungio.models import BungieMembershipType

__all__ = ("DestinyCharacter",)


@custom_define()
class DestinyCharacter(DestinyCharacterMixin):
    """
    A representation of a Destiny 2 character

    Attributes:
        membership_id: The user's id
        membership_type: The user's type, aka platform
        character_id: The character's id
    """

    membership_id: int = custom_field()
    membership_type: Union["BungieMembershipType", int] = custom_field(converter=enum_converter("BungieMembershipType"))
    character_id: int = custom_field()
