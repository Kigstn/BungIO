from typing import TYPE_CHECKING

import attr

if TYPE_CHECKING:
    from bungio.models.auth import AuthData


@attr.s
class BungIOException(Exception):
    pass


@attr.s
class HttpException(BungIOException):
    pass


@attr.s
class BungieException(HttpException):
    error: str
    message: str
    code: int
    data: dict


@attr.s
class _InvalidAuthentication(HttpException):
    pass


@attr.s
class InvalidAuthentication(HttpException):
    auth: "AuthData"


@attr.s
class NotFound(HttpException):
    pass


@attr.s
class BadRequest(HttpException):
    pass


@attr.s
class AuthenticationTooSlow(HttpException):
    pass


@attr.s
class BungieDead(HttpException):
    pass


@attr.s
class _RouteError(HttpException):
    route: str


@attr.s
class TimeoutException(HttpException):
    pass
