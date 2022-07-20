# Authentication And Protected Resources

To get access to a protected resources, or access to any data for users which have private profile, you need the user to authenticate with your app.

This is a bit more tricky, but there are some good tutorials on how this process works [here](https://github.com/Bungie-net/api/wiki/OAuth-Documentation) and [here](https://lowlidev.com.au/destiny/authentication-2).

BungIO helps you by once you have acquired the `code`, anything before that needs to be set up by yourself.

## BungIO and Bungie Authentication
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
from typing import Optional

import fastapi

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
            data[after.destiny_membership_id] = after
            json.dump(data, file)

# instantiate and use both bungio and fastapi
client = MyClient(
    bungie_client_id=os.getenv("bungie_client_id"),
    bungie_client_secret=os.getenv("bungie_client_secret"),
    bungie_token=os.getenv("bungie_token"),
)
app = fastapi.FastAPI()

# saving the auth in a file for this example, in reality this should be replaced by a database
user_auths: dict[int, AuthData]

# call this from your website
@app.get("/auth/{membership_id}/{membership_type}/{code}")
async def authenticate(membership_id: int, membership_type: int, code: str):
    """Receive information from bungie authentication"""

    # generate an access token with the code
    # this will call `Client.on_token_update` we defined above
    await client.generate_auth(membership_type=membership_type, destiny_membership_id=membership_id, code=code)

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
