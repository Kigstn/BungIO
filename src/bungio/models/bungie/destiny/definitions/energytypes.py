# DO NOT CHANGE ANY CODE BELOW
# This file is generated automatically by `generate_api_schema.py` and will be overwritten
# Instead, change functions / models by subclassing them in the `./overwrites/` folder. They will be used instead.

from typing import Optional, Union, TYPE_CHECKING

from bungio.utils import enum_converter
from bungio.models.base import HashObject, ManifestModel, custom_define, custom_field


if TYPE_CHECKING:
    from bungio.models import DestinyStatDefinition
    from bungio.models import DestinyEnergyType
    from bungio.models import DestinyDisplayPropertiesDefinition


@custom_define()
class DestinyEnergyTypeDefinition(ManifestModel, HashObject):
    """
    Represents types of Energy that can be used for costs and payments related to Armor 2.0 mods.

    Tip: Manifest Information
        This model has some attributes which can be filled with additional information found in the manifest (`manifest_...`).
        Without additional work, these attributes will be `None`, since they require additional requests and database lookups.

        To fill the manifest dependent attributes, either:

        - Run `await ThisClass.fetch_manifest_information()`, see [here](/API Reference/Models/base)
        - Set `Client.always_return_manifest_information` to `True`, see [here](/API Reference/client)

    Attributes:
        capacity_stat_hash: If this Energy Type can be used for determining the Type of Energy that an item can consume, this is the hash for the DestinyInvestmentStatDefinition that represents the stat which holds the Capacity for that energy type. (Note that this is optional because "Any" is a valid cost, but not valid for Capacity - an Armor must have a specific Energy Type for determining the energy type that the Armor is restricted to use)
        cost_stat_hash: If this Energy Type can be used as a cost to pay for socketing Armor 2.0 items, this is the hash for the DestinyInvestmentStatDefinition that stores the plug's raw cost.
        display_properties: The description of the energy type, icon etc...
        enum_value: We have an enumeration for Energy types for quick reference. This is the current definition's Energy type enum value.
        hash: The unique identifier for this entity. Guaranteed to be unique for the type of entity, but not globally. When entities refer to each other in Destiny content, it is this hash that they are referring to.
        index: The index of the entity as it was found in the investment tables.
        redacted: If this is true, then there is an entity with this identifier/type combination, but BNet is not yet allowed to show it. Sorry!
        show_icon: If TRUE, the game shows this Energy type's icon. Otherwise, it doesn't. Whether you show it or not is up to you.
        transparent_icon_path: A variant of the icon that is transparent and colorless.
        manifest_capacity_stat_hash: Manifest information for `capacity_stat_hash`
        manifest_cost_stat_hash: Manifest information for `cost_stat_hash`
    """

    capacity_stat_hash: int = custom_field()
    cost_stat_hash: int = custom_field()
    display_properties: "DestinyDisplayPropertiesDefinition" = custom_field()
    enum_value: Union["DestinyEnergyType", int] = custom_field(converter=enum_converter("DestinyEnergyType"))
    index: int = custom_field()
    redacted: bool = custom_field()
    show_icon: bool = custom_field()
    transparent_icon_path: str = custom_field()
    manifest_capacity_stat_hash: Optional["DestinyStatDefinition"] = custom_field(default=None)
    manifest_cost_stat_hash: Optional["DestinyStatDefinition"] = custom_field(default=None)
