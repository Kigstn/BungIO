import attr

from bungio.models.mixins import DestinyClanMixin

__all__ = ("DestinyClan",)


@attr.define
class DestinyClan(DestinyClanMixin):
    """
    A representation of a Destiny 2 clan

    Attributes:
        group_id: The clan's id
    """

    group_id: int = attr.field()
