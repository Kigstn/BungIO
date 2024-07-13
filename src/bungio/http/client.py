import asyncio
from asyncio import Semaphore
from typing import TYPE_CHECKING, Optional
from urllib.parse import urlencode

from aiohttp import (
    ClientConnectorCertificateError,
    ClientOSError,
    ClientResponse,
    ClientSession,
    DummyCookieJar,
    ServerDisconnectedError,
)

from bungio.error import (
    AuthenticationTooSlow,
    BadRequest,
    BungieDead,
    BungieException,
    InvalidAuthentication,
    NotFound,
    TimeoutException,
    _InvalidAuthentication,
    _RouteError,
)
from bungio.http.auth import AuthHttpRequests
from bungio.http.ratelimiting import RateLimiter
from bungio.http.route import Route
from bungio.http.routes import AllRouteHttpRequests
from bungio.models.auth import AuthData
from bungio.models.base import MISSING, ClientMixin, custom_define, custom_field
from bungio.singleton import Singleton

if TYPE_CHECKING:
    from aiohttp_client_cache import CachedSession

__all__ = ("HttpClient",)


@custom_define(init=False)
class HttpClient(AllRouteHttpRequests, AuthHttpRequests, ClientMixin, Singleton):
    """
    The singleton http client doing all communication with bungie

    Attributes:
        bungie_headers: Headers to use for bungie requests
        bungie_auth_headers: Headers to use for bungie auth requests
        max_attempts: Max retries before failure
    """

    _bungie_headers: dict[str, str] = custom_field()
    _bungie_auth_headers: dict[str, str] = custom_field()
    _max_attempts: int = custom_field(default=5)

    ratelimiter: RateLimiter = custom_field(init=False, default=RateLimiter())
    semaphore: Semaphore = custom_field(init=False, default=Semaphore(100))
    _session: "CachedSession | ClientSession" = custom_field(init=False, default=None)

    _initialised: bool = custom_field(init=False, default=False)

    def __init__(self, *args, **kwargs):
        if not getattr(self, "_initialised", False):
            self.__attrs_init__(*args, **kwargs)
        self._initialised = True

    def __del__(self):
        # clean up the session
        if self._session is not None:
            # noinspection PyProtectedMember
            self._session._connector.close()

    @property
    def session(self) -> "CachedSession | ClientSession":
        """Get the aiohttp session"""

        if not self._session:
            self.__setup_session()
        return self._session

    async def request(self, route: Route) -> dict:
        """
        Handle all web requests.

        Args:
            route: The route / method / params the request should have

        Raises:
            NotFound: 404 request
            BadRequest: 400 request
            InvalidAuthentication: If authentication is invalid
            TimeoutException: If no connection could be made
            BungieDead: Servers are down
            AuthenticationTooSlow: The authentication key has expired
            BungieException: Relaying the bungie error

        Returns:
            The json response
        """

        # make sure all is set up
        if not hasattr(self, "_client"):
            raise ValueError("You have to instantiate the `bungio.Client` before using this")

        headers = self._bungie_headers if not route.auth else await self._get_auth_headers(auth=route.auth)

        async with self.semaphore:
            return await self._request(
                route=route.path,
                method=route.method,
                headers=headers,
                params=route.params,
                data=route.data,
                auth=route.auth,
                use_ratelimiter=True,
            )

    async def _request(
        self,
        route: str,
        method: str,
        headers: dict,
        params: Optional[dict] = None,
        data: Optional[dict | list] = None,
        form_data: Optional[dict] = None,
        auth: Optional[AuthData] = None,
        use_ratelimiter: bool = True,
    ) -> dict:
        """
        Internal request function. Use HttpClient.request() instead!

        Args:
            route: The route
            method: The method
            headers: The headers
            params: The query params
            data: The body data
            form_data: The form data
            use_ratelimiter: If the ratelimiter should be used

        Raises:
            NotFound: 404 request
            BadRequest: 400 request
            InvalidAuthentication: If authentication is invalid
            TimeoutException: If no connection could be made
            BungieDead: Servers are down
            AuthenticationTooSlow: The authentication key has expired
            BungieException: Relaying the bungie error
            _RouteError: Getting redirected to a different url

        Returns:
            The json response.
        """

        route_with_params = f"{route}?{urlencode(params or {})}"

        for attempt in range(self._max_attempts):
            # wait for a token
            if use_ratelimiter:
                await self.ratelimiter.wait_for_token()

            try:
                async with self.session.request(
                    method=method,
                    url=route,
                    headers=headers,
                    params=params,
                    json=data,
                    data=form_data,
                ) as response:
                    self._client.logger.debug(f"[{response.status}] - {route_with_params}")

                    # cached responses do not have the content type field
                    content_type = getattr(response, "content_type", None) or response.headers.get(
                        "Content-Type", "NOT SET"
                    )

                    # get the json
                    content = (
                        await response.json(loads=self._client.json_loads) if "application/json" in content_type else {}
                    )

                    # make sure the response is not None
                    if content.get("Response", MISSING) is None:
                        content["Response"] = {}

                    if not await self._handle_response(
                        route_with_params=route_with_params, response=response, content=content
                    ):
                        continue

                    return content

            except _RouteError as e:
                route = e.route

            except _InvalidAuthentication:
                # noinspection PyProtectedMember
                self._client._invalidate_token(auth=auth)
                raise InvalidAuthentication(auth=auth)

            except (
                asyncio.exceptions.TimeoutError,
                ConnectionResetError,
                ServerDisconnectedError,
                ClientConnectorCertificateError,
                ClientOSError,
            ):
                self._client.logger.debug(
                    f"Retrying... - Timeout error for `{route}?{urlencode({} if params is None else params)}`"
                )
                await asyncio.sleep(2 + attempt * 3)
                continue

        self._client.logger.exception(
            f"{route_with_params}- Aborting. Failed {self._max_attempts} times. Infos: {method=} | {auth=} | {data=} | {form_data=}"
        )
        raise TimeoutException

    async def _handle_response(self, route_with_params: str, response: ClientResponse, content: dict) -> bool:
        """
        Handle the response returned by bungie

        Args:
            route_with_params: The full route for logging’s sake
            response: The response
            content: The json content returned or an empty dict

        Raises:
            NotFound: 404 request
            BadRequest: 400 request
            BungieDead: Servers are down
            AuthenticationTooSlow: The authentication key has expired
            BungieException: Relaying the bungie error
            _InvalidAuthentication: If authentication is invalid
            _RouteError: Getting redirected to a different url

        Returns:
            If the response was OK
        """

        # get the bungie errors from the json
        if (error := content.get("error", None)) is None:
            error = content.get("ErrorStatus", "MISSING")
            error_message = content.get("Message", "MISSING")
        else:
            # auth routes have different error code locations which are undocumented
            error_message = content.get("error_description", "MISSING")
            if error == "server_error":
                error = content.get("error_description", error)

        error_code = content.get("ErrorCode", -1)
        error_data = content.get("MessageData", {})

        match (response.status, error):
            case (_, "SystemDisabled"):
                raise BungieDead

            case (_, "invalid_grant"):
                # unauthorized
                self._client.logger.warning(
                    f"`{response.status} - {error} | {error_code}`: Unauthorized (too slow, user fault) request for `{route_with_params}`\n{content=}"
                )
                raise AuthenticationTooSlow

            case (200, _):
                # make sure we got a json
                if not content:
                    self._client.logger.warning(f"Wrong content type returned text: '{await response.text()}'")
                    await asyncio.sleep(3)
                    return False
                return True

            case (301, _):
                # this is issued with a 301 when bungie is of the opinion that resource this moved
                # just retrying fixes it with the new url fixes it
                new_route = response.headers.get("Location")
                self._client.logger.debug(
                    f"Wrong location, retrying with the correct one: `{response.url}` -> `{new_route}`"
                )
                raise _RouteError(route=new_route)

            case (502, _):
                # bad gateway
                self._client.logger.warning(
                    f"Retrying... - `{response.status}` Bad gateway error for `{route_with_params}`"
                )
                await asyncio.sleep(5)

            case (524, _):
                # cloudflare error, retry
                self._client.logger.warning(
                    f"Retrying... - `{response.status}` Cloudflare error for `{route_with_params}`"
                )
                await asyncio.sleep(2)

            case (429, _) | (_, "PerEndpointRequestThrottleExceeded" | "DestinyDirectBabelClientTimeout"):
                # we are getting throttled (should never be called in theory)
                self._client.logger.warning(
                    f"`{response.status} - {error} | {error_code}`: Retrying... - Getting throttled for `{route_with_params}`\n{content=}"
                )

                throttle_seconds = content["ThrottleSeconds"]

                # reset the ratelimit giver
                self.ratelimiter.tokens = 0
                await asyncio.sleep(max(throttle_seconds, 2))

            case (_, "DestinyDirectBabelClientTimeout"):
                # timeout
                self._client.logger.warning(
                    f"`{response.status} - {error} | {error_code}`: Retrying... - Getting timeouts for `{route_with_params}`\n{content=}"
                )
                await asyncio.sleep(60)

            case (_, "DestinyServiceFailure" | "DestinyInternalError" | "UnhandledException"):
                # timeout
                self._client.logger.warning(
                    f"`{response.status} - {error} | {error_code}`: Retrying... - Bungie is having problems `{route_with_params}`\n{content=}"
                )
                await asyncio.sleep(60)

            case (
                _,
                "AuthorizationRecordRevoked"
                | "AuthorizationRecordExpired",
            ):
                # users tokens are no longer valid
                raise _InvalidAuthentication()

            case (404, _):
                # not found
                self._client.logger.warning(
                    f"`{response.status} - {error} | {error_code}`: Not found for `{route_with_params}`\n{content=}"
                )

                if error != "MISSING":
                    raise BungieException(error=error, message=error_message, code=error_code, data=error_data)
                else:
                    raise NotFound

            case ((400 | 401), _):
                # generic bad request, such as wrong format
                self._client.logger.warning(
                    f"`{response.status} - {error} | {error_code}`: Generic bad request for `{route_with_params}`\n{content=}"
                )

                if error != "MISSING":
                    raise BungieException(error=error, message=error_message, code=error_code, data=error_data)
                else:
                    raise BadRequest

            case (503, _):
                self._client.logger.warning(
                    f"`{response.status} - {error} | {error_code}`: Retrying... - Server is overloaded for `{route_with_params}`\n{content=}"
                )
                await asyncio.sleep(10)

            case (status, _):
                # retry if we didn't get an error message
                retry = error == "Success"

                # catch the rest
                self._client.logger.warning(
                    f"`{status} - {error} | {error_code}` - Request failed for `{route_with_params}` - `{error_message}`"
                )

                if retry:
                    await asyncio.sleep(2)
                else:
                    raise BungieException(error=error, message=error_message, code=error_code, data=error_data)

        return False

    async def _get_auth_headers(self, auth: AuthData) -> dict:
        """
        Update the auth headers to include a working token. Raise an error if that doesn't exist

        Args:
            auth: The potentially old authentication info.

        Raises:
            InvalidAuthentication: If authentication is invalid

        Returns:
            User specific headers
        """

        headers = self._bungie_headers.copy()

        # get a working token or abort
        await self._client.get_working_auth(auth=auth)

        headers.update(
            {
                "Authorization": f"Bearer {auth.token}",
            }
        )

        return headers

    def __setup_session(self) -> None:
        """
        Sets up the session to use for http requests
        """

        try:
            from aiohttp_client_cache import CachedSession

            self._session = CachedSession(
                json_serialize=self._client.json_dumps, cookie_jar=DummyCookieJar(), cache=self._client.cache
            )
        except ModuleNotFoundError:
            self._session = ClientSession(json_serialize=self._client.json_dumps, cookie_jar=DummyCookieJar())
