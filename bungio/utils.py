import datetime
import importlib
from typing import Callable, Type

from bungio.models.base import MISSING, BaseEnum, UnknownEnumValue

__all__ = ("get_now_with_tz", "enum_converter")


def get_now_with_tz() -> datetime.datetime:
    """
    Returns the timezone aware current datetime

    Returns:
        Timezone aware datetime
    """

    return datetime.datetime.now(tz=datetime.timezone.utc)


def enum_converter(enum_name: str) -> Callable:
    """
    Return a callable that can be used in attr converters to convert values to enums

    Args:
        enum_name: The name of the enum the value has

    Returns:
        A callable converter
    """

    def converter(
        value: int | str | list[int | str],
    ) -> BaseEnum | UnknownEnumValue | list[BaseEnum | UnknownEnumValue]:
        if isinstance(value, list):
            return [converter(v) for v in value]

        elif isinstance(value, BaseEnum | UnknownEnumValue | type(MISSING)):
            return value

        imp = importlib.import_module("bungio.models")
        enum_class = getattr(imp, enum_name)
        return enum_class(value)

    return converter


# all this does is allow objs to be asynchronously iterable, which does "fix" this bug https://bugs.python.org/issue33346
class AllowAsyncIteration:
    def __init__(self, obj):
        self._it = iter(obj)

    def __aiter__(self):
        return self

    async def __anext__(self):
        try:
            value = next(self._it)
        except StopIteration:
            raise StopAsyncIteration
        return value
