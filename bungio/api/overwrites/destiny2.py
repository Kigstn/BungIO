from typing import Optional, Type

from bungio.api.bungie import destiny2
from bungio.models.auth import AuthData
from bungio.models.base import ManifestModel, custom_define


@custom_define()
class Destiny2RouteInterface(destiny2.Destiny2RouteInterface):
    async def get_destiny_entity_definition(
        self, entity_type: Type[ManifestModel], hash_identifier: int, auth: Optional[AuthData] = None
    ) -> ManifestModel:
        """
        Returns the static definition of an entity of the given Type and hash identifier. Examine the API Documentation for the Type Names of entities that
        have their own definitions. Note that the return type will always *inherit from* DestinyDefinition, but the specific type returned will be the
        requested entity type if it can be found. Please don't use this as a chatty alternative to the Manifest database if you require large sets of data,
        but for simple and one-off accesses this should be handy.

        Args:
            entity_type: The type of entity for whom you would like results. These correspond to the entity's definition contract name. For instance, if you are looking for items, this property should be 'DestinyInventoryItemDefinition'. PREVIEW: This endpoint is still in beta, and may experience rough edges. The schema is tentatively in final form, but there may be bugs that prevent desirable operation.
            hash_identifier: The hash identifier for the specific Entity you want returned.
            auth: Authentication information. Required when users with a private profile are queried.

        Returns:
            The model which is returned by bungie. [General endpoint information.](https://bungie-net.github.io/multi/index.html)
        """

        response = await self._client.http.get_destiny_entity_definition(
            entity_type=entity_type.__name__, hash_identifier=hash_identifier, auth=auth
        )
        return await entity_type.from_dict(data=response, client=self._client)
