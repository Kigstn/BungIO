# Authentication And Protected Resources

To get access to a protected resources, or access to any data for users which have private profile, you need the user to authenticate with your app.

This is a bit more tricky, but there are some good tutorials on how this process works [here](https://github.com/Bungie-net/api/wiki/OAuth-Documentation) and [here](https://lowlidev.com.au/destiny/authentication-2).

BungIO helps you by creating an auth url your users can use and then again once you have acquired the `code`. Handling the redirect you set up with bungie needs to be done by yourself, sadly bungIO cannot help you with that.

## BungIO and Bungie Authentication
- [X] Create a valid bungie authentication url
- [ ] Let the user authenticate with your app to get a code
- [X] Get authentication from a code
- [ ] Store authentication information
- [X] Refresh authentication if outdated (done automatically)
- [X] Dispatch `Client.on_token_update()` when a token is changed

It is highly recommended that you subclass `Client` to overwrite `on_token_update()` and persistently store the authentication information in a database, as shown in the example below.

## Authentication in Action
For this example [FastApi](https://fastapi.tiangolo.com/) is used to demonstrate a common use case of BungIO, especially in combination with authentication.

```py
import json
import os
import secrets
import fastapi

from typing import Optional

from bungio import Client
from bungio.models import AuthData


# overwrite the client to make use of the token events
class MyClient(Client):
    # this gets called when a token gets created / updated
    # use this to save / update your token
    async def on_token_update(self, before: Optional[AuthData], after: AuthData):
        # saving the auth in a file for this example, in reality this should be replaced by a database
        with open("user_auths.json", "r+") as file:
            data = json.load(file)
            data[after.membership_id] = after
            json.dump(data, file)


# instantiate and use both bungio and fastapi
client = MyClient(
    bungie_client_id=os.getenv("BUNGIE_CLIENT_ID"),
    bungie_client_secret=os.getenv("BUNGIE_CLIENT_SECRET"),
    bungie_token=os.getenv("BUNGIE_TOKEN"),
)
app = fastapi.FastAPI()


# generate an auth url with a different state for each request
@app.get("/auth/get_url")
async def auth_url():
    """Generate an auth url"""

    # use a random state which the website can verify after the fact
    state = secrets.token_urlsafe(20)
    url = client.get_auth_url(state=state)
    return {"state": state, "url": url}


# call this from your website
@app.get("/auth/{code}")
async def authenticate(code: str):
    """Receive information from bungie authentication"""

    # generate an access token with the code
    # this will call `Client.on_token_update` we defined above
    auth = await client.generate_auth(code=code)

    return {"membership_id": auth.membership_id}


# example use of the auth data to access a protected route
@app.get("friend_list/{membership_id}/")
async def get_friend_list(membership_id: int):
    """Gets the names of the user bungie friends"""

    # get the auth info from our makeshift database
    with open("user_auths.json", "r") as file:
        data = json.load(file)
        auth: AuthData = data[membership_id]

    # get the users friends
    friends = await client.api.get_friend_list(auth=auth)

    # return the bungie names
    return {"names": [f"{f.bungie_global_display_name}#{f.bungie_global_display_name_code}" for f in friends.friends]}
```

[//]: # "todo test"
