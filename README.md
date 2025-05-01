[![](https://img.shields.io/pypi/v/bungio?label=Version&logo=pypi)](https://pypi.org/project/bungio/)
[![](https://img.shields.io/pypi/dm/bungio?label=Downloads&logo=pypi)](https://pypi.org/project/bungio/)
[![](https://img.shields.io/readthedocs/bungio?label=Docs&logo=readthedocs)](https://bungio.readthedocs.io/en/latest/)
![](https://img.shields.io/badge/Python-3.10+-1081c1?logo=python)
[![](https://img.shields.io/github/actions/workflow/status/Kigstn/BungIO/ruff_formating.yml?branch=master&logo=github&label=Ruff%20Formatting)](https://github.com/Kigstn/BungIO/actions/workflows/ruff_formating.yml)
[![](https://img.shields.io/github/actions/workflow/status/Kigstn/BungIO/ruff_linting.yml?branch=master&logo=github&label=Ruff%20Linting)](https://github.com/Kigstn/BungIO/actions/workflows/ruff_linting.yml)

<h1 align="center">
    <p>
        <img src="https://raw.githubusercontent.com/Kigstn/BungIO/master/docs/src/images/favicon.png" alt="BungIO Logo">
    </p>
    BungIO
</h1>

---

BungIO is a modern and pythonic wrapper for Bungies Destiny 2 API.

- [X] Python 3.10+
- [X] Asynchronous
- [X] 100% typed and raw api coverage
- [X] Ratelimit compliant
- [X] Manifest support
- [X] OAuth2 support
- [X] Easily used in combination with other libraries like FastApi

Click [here](https://bungio.readthedocs.io/en/latest/installation) to get started or visit
the [guides](https://bungio.readthedocs.io/en/latest/Guides/basic)
or [api reference](https://bungio.readthedocs.io/en/latest/API%20Reference/client/).

## Why BungIO?

What sets this library apart from other projects is that it has full api coverage - every single route is fully typed and returns fully typed python classes! And better yet, the api is automatically generated from the api spec bungie publishes. This means when there is an update to the api, it needs literally one button click from me to update the library to the latest api version with the new shiny features.

This means that all api features are fully supported and support for new API feature is added in seconds. This has the downside, that everything follows the Bungie API spec - so if there is an error in the published spec, the same error will be in this library.

#### Destiny Manifest Support

The manifest is where bungie defines all their data: activities, emblems, items, etc. Normally you need to constantly look up data from the api in the manifest, because the api only returns basic info / ids.

For example: You want to look up what activity your user has done last. So you call the correct api route which returns an activity id. You then have to download the manifest and look up that activity id in the correct manifest location. Only then you get additional information like the activity name, light level, location, etc. As you can probably imagine, this gets annoying veeeery quickly.

BungIO provides helper functions to make manifest lookups stupidly easy. Take a look at the manifest guide for more information :) 

## Basic Example

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
---

## Dev Setup

#### Install Dependencies
- [Install uv](https://docs.astral.sh/uv/getting-started/installation/)
- `uv sync --all-extras`

#### Run Tests
- `uv run pytest .`

#### Run Docs
- `uv run mkdocs serve`
