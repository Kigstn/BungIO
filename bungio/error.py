from typing import TYPE_CHECKING

import attr

if TYPE_CHECKING:
    from bungio.models.auth import AuthData

__all__ = (
    "BungIOException",
    "HttpException",
    "BungieException",
    "InvalidAuthentication",
    "NotFound",
    "BadRequest",
    "AuthenticationTooSlow",
    "BungieDead",
    "TimeoutException",
)


@attr.define
class BungIOException(Exception):
    """
    The base exception.
    """

    pass


@attr.define
class HttpException(BungIOException):
    """
    The base http exception.
    """

    pass


@attr.define
class BungieException(HttpException):
    """
    An exception raised by bungie

    Attributes:
        error: The exception bungie raised
        message: The message bungie returned
        code: The code of the exception
        data: The data of the exception
    """

    error: str = attr.field()
    message: str = attr.field()
    code: int = attr.field()
    data: dict = attr.field()


@attr.define
class _InvalidAuthentication(HttpException):
    pass


@attr.define
class InvalidAuthentication(HttpException):
    """
    Raised if the passed authentication is invalid

    Attributes:
        auth: The passed authentication
    """

    auth: "AuthData"


@attr.define
class NotFound(HttpException):
    """
    Raised if the resource was not found (404)
    """

    pass


@attr.define
class BadRequest(HttpException):
    """
    Raised if the resource returned a generic error (400)
    """

    pass


@attr.define
class AuthenticationTooSlow(HttpException):
    """
    Raised if the authentication grant expired
    """

    pass


@attr.define
class BungieDead(HttpException):
    """
    Raised if bungie is down. Usually this mean maintenance, see their [twitter](https://twitter.com/BungieHelp) for more info
    """

    pass


@attr.define
class _RouteError(HttpException):
    route: str


@attr.define
class TimeoutException(HttpException):
    """
    If the requests failed multiple times in a row without a specific exception
    """

    pass
