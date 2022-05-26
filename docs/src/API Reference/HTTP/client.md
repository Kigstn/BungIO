# HTTP Client

!!! Tip "Singleton"
    This is a singleton, so simply import this wherever you need to do API calls yourself.


This should be used for all communication with the bungie.net api, since it implements correct rate limiting and error handling.

There is 100% raw api coverage, so you should always use the routes defined in the [Bungie Routes](/API Reference/HTTP/Bungie Routes/_auth) folder.

::: bungio.http.client
