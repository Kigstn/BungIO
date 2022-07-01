from typing import TYPE_CHECKING

import attr

from bungio.models.mixins import DestinyUserMixin

if TYPE_CHECKING:
    from bungio.models import BungieMembershipType


@attr.define
class DestinyUser(DestinyUserMixin):
    membership_id: int = attr.field()
    membership_type: "BungieMembershipType" = attr.field()
