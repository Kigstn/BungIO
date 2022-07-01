import attr

from bungio.models import BungieMembershipType
from bungio.models.mixins import DestinyUserMixin


@attr.define
class DestinyUser(DestinyUserMixin):
    membership_id: int = attr.field()
    membership_type: BungieMembershipType = attr.field()
