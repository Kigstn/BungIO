from typing import Callable, Coroutine

from bungio.models.auth import AuthData

__all__ = ("AuthHttpRequests",)


class AuthHttpRequests:
    _request: Callable[..., Coroutine]
    _bungie_auth_headers: dict[str, str]

    async def request_access_token(
        self,
        code: str,
    ) -> dict:
        """
        Authorise with bungie.net by requesting an access token using the code they generated.

        View [the official documentation](https://github.com/Bungie-net/api/wiki/OAuth-Documentation) for more information on how to set this up.

        Args:
            code: The code bungie sent.

        Returns:
            The json response
        """

        data = {
            "grant_type": "authorization_code",
            "code": code,
        }

        return await self._request(
            route="https://www.bungie.net/Platform/App/OAuth/token/",
            method="POST",
            form_data=data,
            headers=self._bungie_auth_headers,
            use_ratelimiter=False,
        )

    async def refresh_access_token(
        self,
        auth: AuthData,
    ) -> dict:
        """
        Refresh a bungie.net token.

        Args:
            auth: The old authentication information.

        Returns:
            The json response
        """

        data = {
            "grant_type": "refresh_token",
            "refresh_token": auth.refresh_token,
        }

        return await self._request(
            route="https://www.bungie.net/Platform/App/OAuth/token/",
            method="POST",
            form_data=data,
            headers=self._bungie_auth_headers,
            use_ratelimiter=False,
        )
