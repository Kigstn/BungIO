from typing import TYPE_CHECKING

from bungio.models.base import custom_define, custom_field

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


@custom_define()
class BungIOException(Exception):
    """
    The base exception.
    """

    pass


@custom_define()
class HttpException(BungIOException):
    """
    The base http exception.
    """

    pass


@custom_define()
class BungieException(HttpException):
    """
    An exception raised by bungie

    Attributes:
        error: The exception bungie raised
        message: The message bungie returned
        code: The code of the exception
        data: The data of the exception
    """

    error: str = custom_field()
    message: str = custom_field()
    code: int = custom_field()
    data: dict = custom_field()


@custom_define()
class _InvalidAuthentication(HttpException):
    pass


@custom_define()
class InvalidAuthentication(HttpException):
    """
    Raised if the passed authentication is invalid

    Attributes:
        auth: The passed authentication
    """

    auth: "AuthData"


@custom_define()
class NotFound(HttpException):
    """
    Raised if the resource was not found (404)
    """

    pass


@custom_define()
class BadRequest(HttpException):
    """
    Raised if the resource returned a generic error (400)
    """

    pass


@custom_define()
class AuthenticationTooSlow(HttpException):
    """
    Raised if the authentication grant expired
    """

    pass


@custom_define()
class BungieDead(HttpException):
    """
    Raised if bungie is down. Usually this mean maintenance, see their [twitter](https://twitter.com/BungieHelp) for more info
    """

    pass


@custom_define()
class _RouteError(HttpException):
    route: str


@custom_define()
class TimeoutException(HttpException):
    """
    If the requests failed multiple times in a row without a specific exception
    """

    pass
