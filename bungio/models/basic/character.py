import attr

from bungio.models import BungieMembershipType
from bungio.models.mixins import DestinyCharacterMixin


@attr.define
class DestinyCharacter(DestinyCharacterMixin):
    membership_id: int = attr.field()
    membership_type: BungieMembershipType = attr.field()
    character_id: int = attr.field()
