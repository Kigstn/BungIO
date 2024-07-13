from typing import TYPE_CHECKING

from bungio.definitions import DEFAULT_LOGGER
from bungio.models.base import MISSING, custom_define

if TYPE_CHECKING:
    from bungio.client import Client


__all__ = (
    "client",
    "Singleton",
)

client: "Client" = MISSING


_instances: dict = {}


@custom_define()
class Singleton:
    """
    Singleton class used to only create one instance
    """

    def __new__(cls, *args, **kwargs):
        if cls not in _instances:
            _instances[cls] = super().__new__(cls)
            return _instances[cls]
        else:
            found_cls = _instances[cls]
            if client is not MISSING:
                logger = client.logger
            else:
                logger = DEFAULT_LOGGER
            logger.warning(
                f"The `{cls.__name__}` can only be defined once, ignoring your inputs and returning the already defined `{cls.__name__}`"
            )
            return found_cls
