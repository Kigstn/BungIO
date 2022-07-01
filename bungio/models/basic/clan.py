import attr

from bungio.models.mixins import DestinyClanMixin


@attr.define
class DestinyClan(DestinyClanMixin):
    group_id: int = attr.field()
