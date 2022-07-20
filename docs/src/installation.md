# Getting Started


## Installation

=== ":one: With `pip`"
    ```sh
    pip install bungio
    ```

=== ":one: With `poetry`"
    ```sh
    poetry add bungio
    poetry install
    ```

## Getting your Bungie Tokens

1. Visit the [bungie.net](https://www.bungie.net/en) and log in
2. Navigate to the [application page](https://www.bungie.net/en/Application)
3. Click `Create New App` or choose your existing app
4. Give your app a fitting name and click on `Create New App`. You can ignore the settings for now
5. **[Optional]** If you want to use OAuth2, change the `OAuth Client Type` to `Confidential`, and choose the `Scope` you want your app to have
6. Your API keys can be found in `API Keys`

### Bungie API Keys and BungIO

Should there be any confusion, this is how the API keys and the `bungio.Client` arguments correspond.

| Bungie Name         | Client arguments      |
|---------------------|-----------------------|
| API Key             | bungie_token          |
| OAuth client_id     | bungie_client_id      |
| OAuth client_secret | bungie_client_secret  |

## Usage

A basic setup can be found in the [guides](/Guides/basic).
