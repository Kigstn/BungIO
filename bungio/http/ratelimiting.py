import asyncio
import time

import attr

__all__ = ("RateLimiter",)


@attr.define
class RateLimiter:
    """
    Gives out x tokens for network operations every y seconds

    Attributes:
        max_tokens: How many requests can we save up - bungie limits after 250 in 10s, so the default is 240
        seconds: In how many seconds those requests are allowed
    """

    max_tokens: int = attr.field(default=240)
    seconds: int = attr.field(default=10)

    tokens: float = attr.field(init=False)
    updated_at: float = attr.field(init=False)

    lock: asyncio.Lock = attr.field(init=False, default=asyncio.Lock())

    def __attrs_post_init__(self):
        self.tokens = self.max_tokens

    async def wait_for_token(self):
        """Waits until a token becomes available"""

        async with self.lock:
            if self.tokens == 0:
                current_time = time.time()
                if (missing := current_time - self.updated_at) < self.seconds:
                    await asyncio.sleep(self.seconds - missing)
                self.tokens = self.max_tokens

            if self.tokens == self.max_tokens:
                # the first request is made, start the timer when that should fill back up
                self.updated_at = time.time()

            self.tokens -= 1
