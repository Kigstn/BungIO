from typing import TYPE_CHECKING

from bungio.definitions import DEFAULT_LOGGER
from bungio.models.base import MISSING

if TYPE_CHECKING:
    from bungio.client import Client


__all__ = (
    "client",
    "SingletonMetaclass",
)

client: "Client" = MISSING


class SingletonMetaclass(type):
    """
    Singleton metaclass used to only create one instance
    """

    _instances: dict = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(SingletonMetaclass, cls).__call__(*args, **kwargs)
            return cls._instances[cls]
        else:
            found_cls = cls._instances[cls]
            if client is not MISSING:
                logger = client.logger
            else:
                logger = DEFAULT_LOGGER
            logger.warning(
                f"The `{cls.__name__}` can only be defined once, ignoring your inputs and returning the already defined `{cls.__name__}`"
            )
            return found_cls
