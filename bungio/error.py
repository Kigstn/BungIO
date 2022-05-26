from typing import TYPE_CHECKING

import attr

if TYPE_CHECKING:
    from bungio.models.auth import AuthData


@attr.define
class BungIOException(Exception):
    pass


@attr.define
class HttpException(BungIOException):
    pass


@attr.define
class BungieException(HttpException):
    error: str
    message: str
    code: int
    data: dict


@attr.define
class _InvalidAuthentication(HttpException):
    pass


@attr.define
class InvalidAuthentication(HttpException):
    auth: "AuthData"


@attr.define
class NotFound(HttpException):
    pass


@attr.define
class BadRequest(HttpException):
    pass


@attr.define
class AuthenticationTooSlow(HttpException):
    pass


@attr.define
class BungieDead(HttpException):
    pass


@attr.define
class _RouteError(HttpException):
    route: str


@attr.define
class TimeoutException(HttpException):
    pass
