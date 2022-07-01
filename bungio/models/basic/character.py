from typing import TYPE_CHECKING

import attr

from bungio.models.mixins import DestinyCharacterMixin

if TYPE_CHECKING:
    from bungio.models import BungieMembershipType


@attr.define
class DestinyCharacter(DestinyCharacterMixin):
    membership_id: int = attr.field()
    membership_type: "BungieMembershipType" = attr.field()
    character_id: int = attr.field()
