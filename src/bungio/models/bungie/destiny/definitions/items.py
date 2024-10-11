# DO NOT CHANGE ANY CODE BELOW
# This file is generated automatically by `generate_api_schema.py` and will be overwritten
# Instead, change functions / models by subclassing them in the `./overwrites/` folder. They will be used instead.

from typing import TYPE_CHECKING, Optional, Union

from bungio.models.base import BaseModel, HashObject, ManifestModel, custom_define, custom_field
from bungio.utils import enum_converter

if TYPE_CHECKING:
    from bungio.models import (
        DestinyDisplayPropertiesDefinition,
        DestinyEnergyType,
        DestinyEnergyTypeDefinition,
        DestinyInventoryItemDefinition,
        DestinyMaterialRequirementSetDefinition,
        PlugAvailabilityMode,
        PlugUiStyles,
    )


@custom_define()
class DestinyItemTierTypeDefinition(ManifestModel, HashObject):
    """
    Defines the tier type of an item. Mostly this provides human readable properties for types like Common, Rare, etc... It also provides some base data for infusion that could be useful.

    None
    Attributes:
        display_properties: _No description given by bungie._
        hash: The unique identifier for this entity. Guaranteed to be unique for the type of entity, but not globally. When entities refer to each other in Destiny content, it is this hash that they are referring to.
        index: The index of the entity as it was found in the investment tables.
        infusion_process: If this tier defines infusion properties, they will be contained here.
        redacted: If this is true, then there is an entity with this identifier/type combination, but BNet is not yet allowed to show it. Sorry!
    """

    display_properties: "DestinyDisplayPropertiesDefinition" = custom_field()
    index: int = custom_field()
    infusion_process: "DestinyItemTierTypeInfusionBlock" = custom_field()
    redacted: bool = custom_field()


@custom_define()
class DestinyItemTierTypeInfusionBlock(BaseModel):
    """
    _No description given by bungie._

    None
    Attributes:
        base_quality_transfer_ratio: The default portion of quality that will transfer from the infuser to the infusee item. (InfuserQuality - InfuseeQuality) * baseQualityTransferRatio = base quality transferred.
        minimum_quality_increment: As long as InfuserQuality > InfuseeQuality, the amount of quality bestowed is guaranteed to be at least this value, even if the transferRatio would dictate that it should be less. The total amount of quality that ends up in the Infusee cannot exceed the Infuser's quality however (for instance, if you infuse a 300 item with a 301 item and the minimum quality increment is 10, the infused item will not end up with 310 quality)
    """

    base_quality_transfer_ratio: float = custom_field()
    minimum_quality_increment: int = custom_field()


@custom_define()
class DestinyDerivedItemCategoryDefinition(BaseModel):
    """
    A shortcut for the fact that some items have a "Preview Vendor" - See DestinyInventoryItemDefinition.preview.previewVendorHash - that is intended to be used to show what items you can get as a result of acquiring or using this item. A common example of this in Destiny 1 was Eververse "Boxes," which could have many possible items. This "Preview Vendor" is not a vendor you can actually see in the game, but it defines categories and sale items for all of the possible items you could get from the Box so that the game can show them to you. We summarize that info here so that you don't have to do that Vendor lookup and aggregation manually.

    None
    Attributes:
        category_description: The localized string for the category title. This will be something describing the items you can get as a group, or your likelihood/the quantity you'll get.
        items: This is the list of all of the items for this category and the basic properties we'll know about them.
    """

    category_description: str = custom_field()
    items: list["DestinyDerivedItemDefinition"] = custom_field(
        metadata={"type": """list[DestinyDerivedItemDefinition]"""}
    )


@custom_define()
class DestinyDerivedItemDefinition(BaseModel):
    """
    This is a reference to, and summary data for, a specific item that you can get as a result of Using or Acquiring some other Item (For example, this could be summary information for an Emote that you can get by opening an an Eververse Box) See DestinyDerivedItemCategoryDefinition for more information.

    None
    Attributes:
        icon_path: An icon for the item.
        item_description: A brief description of the item.
        item_detail: Additional details about the derived item, in addition to the description.
        item_hash: The hash for the DestinyInventoryItemDefinition of this derived item, if there is one. Sometimes we are given this information as a manual override, in which case there won't be an actual DestinyInventoryItemDefinition for what we display, but you can still show the strings from this object itself.
        item_name: The name of the derived item.
        vendor_item_index: If the item was derived from a "Preview Vendor", this will be an index into the DestinyVendorDefinition's itemList property. Otherwise, -1.
    """

    icon_path: str = custom_field()
    item_description: str = custom_field()
    item_detail: str = custom_field()
    item_hash: int = custom_field()
    item_name: str = custom_field()
    vendor_item_index: int = custom_field()


@custom_define()
class DestinyItemPlugDefinition(BaseModel):
    """
    If an item is a Plug, its DestinyInventoryItemDefinition.plug property will be populated with an instance of one of these bad boys. This gives information about when it can be inserted, what the plug's category is (and thus whether it is compatible with a socket... see DestinySocketTypeDefinition for information about Plug Categories and socket compatibility), whether it is enabled and other Plug info.

    Tip: Manifest Information
        This model has some attributes which can be filled with additional information found in the manifest (`manifest_...`).
        Without additional work, these attributes will be `None`, since they require additional requests and database lookups.

        To fill the manifest dependent attributes, either:

        - Run `await ThisClass.fetch_manifest_information()`, see [here](/API Reference/Models/base)
        - Set `Client.always_return_manifest_information` to `True`, see [here](/API Reference/client)

    Attributes:
        alternate_plug_style: The alternate plug of the plug: only applies when the item is in states that only the server can know about and control, unfortunately. See AlternateUiPlugLabel for the related label info.
        alternate_ui_plug_label: If the plug meets certain state requirements, it may have an alternative label applied to it. This is the alternative label that will be applied in such a situation.
        enabled_material_requirement_hash: It's not enough for the plug to be inserted. It has to be enabled as well. For it to be enabled, it may require materials. This is the hash identifier for the DestinyMaterialRequirementSetDefinition for those requirements, if there is one.
        enabled_rules: The rules around whether the plug, once inserted, is enabled and providing its benefits. The live data DestinyItemPlugComponent.enableFailIndexes will be an index into this array, so you can pull out the failure strings appropriate for the user.
        energy_capacity: IF not null, this plug provides Energy capacity to the item in which it is socketed. In Armor 2.0 for example, is implemented in a similar way to Masterworks, where visually it's a single area of the UI being clicked on to "Upgrade" to higher energy levels, but it's actually socketing new plugs.
        energy_cost: IF not null, this plug has an energy cost. This contains the details of that cost.
        insertion_material_requirement_hash: If inserting this plug requires materials, this is the hash identifier for looking up the DestinyMaterialRequirementSetDefinition for those requirements.
        insertion_rules: The rules around when this plug can be inserted into a socket, aside from the socket's individual restrictions. The live data DestinyItemPlugComponent.insertFailIndexes will be an index into this array, so you can pull out the failure strings appropriate for the user.
        is_dummy_plug: If TRUE, this plug is used for UI display purposes only, and doesn't have any interesting effects of its own.
        on_action_recreate_self: If you successfully socket the item, this will determine whether or not you get "refunded" on the plug.
        parent_item_override: Do you ever get the feeling that a system has become so overburdened by edge cases that it probably should have become some other system entirely? So do I! In totally unrelated news, Plugs can now override properties of their parent items. This is some of the relevant definition data for those overrides. If this is populated, it will have the override data to be applied when this plug is applied to an item.
        plug_availability: Indicates the rules about when this plug can be used. See the PlugAvailabilityMode enumeration for more information!
        plug_category_hash: The hash for the plugCategoryIdentifier. You can use this instead if you wish: I put both in the definition for debugging purposes.
        plug_category_identifier: The string identifier for the plug's category. Use the socket's DestinySocketTypeDefinition.plugWhitelist to determine whether this plug can be inserted into the socket.
        plug_style: _No description given by bungie._
        preview_item_override_hash: In the game, if you're inspecting a plug item directly, this will be the item shown with the plug attached. Look up the DestinyInventoryItemDefinition for this hash for the item.
        ui_plug_label: Plugs can have arbitrary, UI-defined identifiers that the UI designers use to determine the style applied to plugs. Unfortunately, we have neither a definitive list of these labels nor advance warning of when new labels might be applied or how that relates to how they get rendered. If you want to, you can refer to known labels to change your own styles: but know that new ones can be created arbitrarily, and we have no way of associating the labels with any specific UI style guidance... you'll have to piece that together on your end. Or do what we do, and just show plugs more generically, without specialized styles.
        manifest_enabled_material_requirement_hash: Manifest information for `enabled_material_requirement_hash`
        manifest_insertion_material_requirement_hash: Manifest information for `insertion_material_requirement_hash`
        manifest_preview_item_override_hash: Manifest information for `preview_item_override_hash`
    """

    alternate_plug_style: Union["PlugUiStyles", int] = custom_field(converter=enum_converter("PlugUiStyles"))
    alternate_ui_plug_label: str = custom_field()
    enabled_material_requirement_hash: int = custom_field()
    enabled_rules: list["DestinyPlugRuleDefinition"] = custom_field(
        metadata={"type": """list[DestinyPlugRuleDefinition]"""}
    )
    energy_capacity: "DestinyEnergyCapacityEntry" = custom_field()
    energy_cost: "DestinyEnergyCostEntry" = custom_field()
    insertion_material_requirement_hash: int = custom_field()
    insertion_rules: list["DestinyPlugRuleDefinition"] = custom_field(
        metadata={"type": """list[DestinyPlugRuleDefinition]"""}
    )
    is_dummy_plug: bool = custom_field()
    on_action_recreate_self: bool = custom_field()
    parent_item_override: "DestinyParentItemOverride" = custom_field()
    plug_availability: Union["PlugAvailabilityMode", int] = custom_field(
        converter=enum_converter("PlugAvailabilityMode")
    )
    plug_category_hash: int = custom_field()
    plug_category_identifier: str = custom_field()
    plug_style: Union["PlugUiStyles", int] = custom_field(converter=enum_converter("PlugUiStyles"))
    preview_item_override_hash: int = custom_field()
    ui_plug_label: str = custom_field()
    manifest_enabled_material_requirement_hash: Optional["DestinyMaterialRequirementSetDefinition"] = custom_field(
        default=None
    )
    manifest_insertion_material_requirement_hash: Optional["DestinyMaterialRequirementSetDefinition"] = custom_field(
        default=None
    )
    manifest_preview_item_override_hash: Optional["DestinyInventoryItemDefinition"] = custom_field(default=None)


@custom_define()
class DestinyPlugRuleDefinition(BaseModel):
    """
    Dictates a rule around whether the plug is enabled or insertable. In practice, the live Destiny data will refer to these entries by index. You can then look up that index in the appropriate property (enabledRules or insertionRules) to get the localized string for the failure message if it failed.

    None
    Attributes:
        failure_message: The localized string to show if this rule fails.
    """

    failure_message: str = custom_field()


@custom_define()
class DestinyParentItemOverride(BaseModel):
    """
    _No description given by bungie._

    None
    Attributes:
        additional_equip_requirements_display_strings: _No description given by bungie._
        pip_icon: _No description given by bungie._
    """

    additional_equip_requirements_display_strings: list[str] = custom_field(metadata={"type": """list[str]"""})
    pip_icon: str = custom_field()


@custom_define()
class DestinyEnergyCapacityEntry(BaseModel):
    """
    Items can have Energy Capacity, and plugs can provide that capacity such as on a piece of Armor in Armor 2.0. This is how much "Energy" can be spent on activating plugs for this item.

    Tip: Manifest Information
        This model has some attributes which can be filled with additional information found in the manifest (`manifest_...`).
        Without additional work, these attributes will be `None`, since they require additional requests and database lookups.

        To fill the manifest dependent attributes, either:

        - Run `await ThisClass.fetch_manifest_information()`, see [here](/API Reference/Models/base)
        - Set `Client.always_return_manifest_information` to `True`, see [here](/API Reference/client)

    Attributes:
        capacity_value: How much energy capacity this plug provides.
        energy_type: The Energy Type for this energy capacity, in enum form for easy use.
        energy_type_hash: Energy provided by a plug is always of a specific type - this is the hash identifier for the energy type for which it provides Capacity.
        manifest_energy_type_hash: Manifest information for `energy_type_hash`
    """

    capacity_value: int = custom_field()
    energy_type: Union["DestinyEnergyType", int] = custom_field(converter=enum_converter("DestinyEnergyType"))
    energy_type_hash: int = custom_field()
    manifest_energy_type_hash: Optional["DestinyEnergyTypeDefinition"] = custom_field(default=None)


@custom_define()
class DestinyEnergyCostEntry(BaseModel):
    """
    Some plugs cost Energy, which is a stat on the item that can be increased by other plugs (that, at least in Armor 2.0, have a "masterworks-like" mechanic for upgrading). If a plug has costs, the details of that cost are defined here.

    Tip: Manifest Information
        This model has some attributes which can be filled with additional information found in the manifest (`manifest_...`).
        Without additional work, these attributes will be `None`, since they require additional requests and database lookups.

        To fill the manifest dependent attributes, either:

        - Run `await ThisClass.fetch_manifest_information()`, see [here](/API Reference/Models/base)
        - Set `Client.always_return_manifest_information` to `True`, see [here](/API Reference/client)

    Attributes:
        energy_cost: The Energy cost for inserting this plug.
        energy_type: The type of energy that this plug costs, in enum form.
        energy_type_hash: The type of energy that this plug costs, as a reference to the DestinyEnergyTypeDefinition of the energy type.
        manifest_energy_type_hash: Manifest information for `energy_type_hash`
    """

    energy_cost: int = custom_field()
    energy_type: Union["DestinyEnergyType", int] = custom_field(converter=enum_converter("DestinyEnergyType"))
    energy_type_hash: int = custom_field()
    manifest_energy_type_hash: Optional["DestinyEnergyTypeDefinition"] = custom_field(default=None)
