# DO NOT CHANGE ANY CODE BELOW
# This file is generated automatically by `generate_api_schema.py` and will be overwritten
# Instead, change functions / models by subclassing them in the `./overwrites/` folder. They will be used instead.

from typing import TYPE_CHECKING, Optional

from bungio.models.base import BaseModel, custom_define, custom_field

if TYPE_CHECKING:
    from bungio.models import (
        DestinyActivityDefinition,
        DestinyInventoryItemDefinition,
        DestinyLocationDefinition,
        DestinyObjectiveDefinition,
    )


@custom_define()
class DestinyEnvironmentLocationMapping(BaseModel):
    """
    _No description given by bungie._

    Tip: Manifest Information
        This model has some attributes which can be filled with additional information found in the manifest (`manifest_...`).
        Without additional work, these attributes will be `None`, since they require additional requests and database lookups.

        To fill the manifest dependent attributes, either:

        - Run `await ThisClass.fetch_manifest_information()`, see [here](/API Reference/Models/base)
        - Set `Client.always_return_manifest_information` to `True`, see [here](/API Reference/client)

    Attributes:
        activation_source: A hint that the UI uses to figure out how this location is activated by the player.
        activity_hash: If this is populated, this is the activity you have to be playing in order to see this location appear because of this mapping. (theoretically, a location can have multiple mappings, and some might require you to be in a specific activity when others don't)
        item_hash: If this is populated, it is the item that you must possess for this location to be active because of this mapping. (theoretically, a location can have multiple mappings, and some might require an item while others don't)
        location_hash: The location that is revealed on the director by this mapping.
        objective_hash: If this is populated, this is an objective related to the location.
        manifest_activity_hash: Manifest information for `activity_hash`
        manifest_item_hash: Manifest information for `item_hash`
        manifest_location_hash: Manifest information for `location_hash`
        manifest_objective_hash: Manifest information for `objective_hash`
    """

    activation_source: str = custom_field()
    activity_hash: int = custom_field()
    item_hash: int = custom_field()
    location_hash: int = custom_field()
    objective_hash: int = custom_field()
    manifest_activity_hash: Optional["DestinyActivityDefinition"] = custom_field(default=None)
    manifest_item_hash: Optional["DestinyInventoryItemDefinition"] = custom_field(default=None)
    manifest_location_hash: Optional["DestinyLocationDefinition"] = custom_field(default=None)
    manifest_objective_hash: Optional["DestinyObjectiveDefinition"] = custom_field(default=None)
