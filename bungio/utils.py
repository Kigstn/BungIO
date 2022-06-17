import datetime


def get_now_with_tz() -> datetime.datetime:
    """
    Returns the timezone aware current datetime

    Returns:
        Timezone aware datetime
    """

    return datetime.datetime.now(tz=datetime.timezone.utc)


class AllowAsyncIteration:
    """
    All this does is allow objs to be asynchronously iterable, which does "fix" this bug https://bugs.python.org/issue33346
    """

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
