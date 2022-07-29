from bungio.models.base import custom_define, custom_field
from bungio.models.mixins import DestinyClanMixin

__all__ = ("DestinyClan",)


@custom_define()
class DestinyClan(DestinyClanMixin):
    """
    A representation of a Destiny 2 clan

    Attributes:
        group_id: The clan's id
    """

    group_id: int = custom_field()
