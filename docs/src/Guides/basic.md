# Basic Example

```py
import asyncio
import os

from bungio import Client
from bungio.models import BungieMembershipType, DestinyActivityModeType, DestinyUser


# create the client obj with our bungie authentication
client = Client(
    bungie_client_id=os.getenv("BUNGIE_CLIENT_ID"),
    bungie_client_secret=os.getenv("BUNGIE_CLIENT_SECRET"),
    bungie_token=os.getenv("BUNGIE_TOKEN"),
)

async def main():
    # create a user obj using a known bungie id
    user = DestinyUser(membership_id=4611686018467765462, membership_type=BungieMembershipType.TIGER_STEAM)

    # iterate thought the raids that user has played
    async for activity in user.yield_activity_history(mode=DestinyActivityModeType.RAID):

        # print the date of the activity
        print(activity.period)

# bungio is by nature asynchronous, it can only be run in an asynchronous context
asyncio.run(main())
```
