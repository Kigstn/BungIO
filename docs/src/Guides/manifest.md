# Incorporating Manifest Information

The destiny manifest holds much information which is not returned directly via the API, like the location of an activity, what modifiers it has, and many, many more.

Manifest information is available if an attribute starting with `manifest_` is present. These attributes are empty by default since providing them takes additional requests and / or processing time.

To view those information and make use of the manifest there are two options. Either manually request the information per model by calling `await model.fetch_manifest_information()` or set `always_return_manifest_information=True` when setting up the `Client`.

All manifest information are downloaded once, and then stored locally in a database. You can pass the database where everything should be stored by passing it to `manifest_storage` when setting up the `Client`.

=== ":one: Manual Request"
    ```py
    client = Client(
        bungie_client_id=os.getenv("BUNGIE_CLIENT_ID"),
        bungie_client_secret=os.getenv("BUNGIE_CLIENT_SECRET"),
        bungie_token=os.getenv("BUNGIE_TOKEN"),
    )

    async def main():
        user = DestinyUser(membership_id=4611686018467765462, membership_type=BungieMembershipType.TIGER_STEAM)
        async for activity in user.yield_activity_history(mode=DestinyActivityModeType.RAID):

            # manifest information is not yet filled
            assert activity.activity_details.manifest_reference_id is None

            # fetch the manifest information
            await activity.fetch_manifest_information()
            assert activity.activity_details.manifest_reference_id is not None

            # print the light level of the activity
            print(activity.activity_details.manifest_reference_id.activity_light_level)

    asyncio.run(main())
    ```


=== ":two: Automatic"
    Be aware that this will fetch the manifest information for every single request you do. The manifest is several hundred MB big if you save everything.

    ```py
    client = Client(
        bungie_client_id=os.getenv("BUNGIE_CLIENT_ID"),
        bungie_client_secret=os.getenv("BUNGIE_CLIENT_SECRET"),
        bungie_token=os.getenv("BUNGIE_TOKEN"),
        always_return_manifest_information=True,    # specify that we always want the manifest information
    )

    async def main():
        user = DestinyUser(membership_id=4611686018467765462, membership_type=BungieMembershipType.TIGER_STEAM)
        async for activity in user.yield_activity_history(mode=DestinyActivityModeType.RAID):

            # manifest information is automatically filled
            assert activity.activity_details.manifest_reference_id is not None

            # print the light level of the activity
            print(activity.activity_details.manifest_reference_id.activity_light_level)

    asyncio.run(main())
    ```
