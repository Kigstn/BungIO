# Why BungIO?

What sets this library apart from other projects is that it has full api coverage - every single route is fully typed and returns fully typed python classes! And better yet, the api is automatically generated from the api spec bungie publishes. This means when there is an update to the api, it needs literally one button click from me to update the library to the latest api version with the new shiny features.

This means that all api features are fully supported and support for new API feature is added in seconds. This has the downside, that everything follows the Bungie API spec - so if there is an error in the published spec, the same error will be in this library.

## Destiny Manifest Support

The manifest is where bungie defines all their data: activities, emblems, items, etc. Normally you need to constantly look up data from the api in the manifest, because the api only returns basic info / ids.

For example: You want to look up what activity your user has done last. So you call the correct api route which returns an activity id. You then have to download the manifest and look up that activity id in the correct manifest location. Only then you get additional information like the activity name, light level, location, etc. As you can probably imagine, this gets annoying veeeery quickly.

BungIO provides helper functions to make manifest lookups stupidly easy. Take a look at the manifest guide for more information :) 
