# DO NOT CHANGE ANY CODE BELOW
# This file is generated automatically by `generate_api_schema.py` and will be overwritten
# Instead, change functions / models by subclassing them in the `./overwrites/` folder. They will be used instead.

from typing import TYPE_CHECKING, Optional, Union

from bungio.models.base import BaseModel, HashObject, ManifestModel, custom_define, custom_field
from bungio.utils import enum_converter

if TYPE_CHECKING:
    from bungio.models import (
        DestinyActivityDefinition,
        DestinyDestinationDefinition,
        DestinyDisplayPropertiesDefinition,
        DestinyInventoryItemDefinition,
        DestinyLocationDefinition,
        DestinyScope,
        DestinyVendorDefinition,
    )


@custom_define()
class DestinyChecklistDefinition(ManifestModel, HashObject):
    """
    By public demand, Checklists are loose sets of "things to do/things you have done" in Destiny that we were actually able to track. They include easter eggs you find in the world, unique chests you unlock, and other such data where the first time you do it is significant enough to be tracked, and you have the potential to "get them all". These may be account-wide, or may be per character. The status of these will be returned in related "Checklist" data coming down from API requests such as GetProfile or GetCharacter. Generally speaking, the items in a checklist can be completed in any order: we return an ordered list which only implies the way we are showing them in our own UI, and you can feel free to alter it as you wish. Note that, in the future, there will be something resembling the old D1 Record Books in at least some vague form. When that is created, it may be that it will supercede much or all of this Checklist data. It remains to be seen if that will be the case, so for now assume that the Checklists will still exist even after the release of D2: Forsaken.

    None
    Attributes:
        display_properties: _No description given by bungie._
        entries: The individual checklist items. Gotta catch 'em all.
        hash: The unique identifier for this entity. Guaranteed to be unique for the type of entity, but not globally. When entities refer to each other in Destiny content, it is this hash that they are referring to.
        index: The index of the entity as it was found in the investment tables.
        redacted: If this is true, then there is an entity with this identifier/type combination, but BNet is not yet allowed to show it. Sorry!
        scope: Indicates whether you will find this checklist on the Profile or Character components.
        view_action_string: A localized string prompting you to view the checklist.
    """

    display_properties: "DestinyDisplayPropertiesDefinition" = custom_field()
    entries: list["DestinyChecklistEntryDefinition"] = custom_field(
        metadata={"type": """list[DestinyChecklistEntryDefinition]"""}
    )
    index: int = custom_field()
    redacted: bool = custom_field()
    scope: Union["DestinyScope", int] = custom_field(converter=enum_converter("DestinyScope"))
    view_action_string: str = custom_field()


@custom_define()
class DestinyChecklistEntryDefinition(BaseModel, HashObject):
    """
    The properties of an individual checklist item. Note that almost everything is optional: it is *highly* variable what kind of data we'll actually be able to return: at times we may have no other relationships to entities at all. Whatever UI you build, do it with the knowledge that any given entry might not actually be able to be associated with some other Destiny entity.

    Tip: Manifest Information
        This model has some attributes which can be filled with additional information found in the manifest (`manifest_...`).
        Without additional work, these attributes will be `None`, since they require additional requests and database lookups.

        To fill the manifest dependent attributes, either:

        - Run `await ThisClass.fetch_manifest_information()`, see [here](/API Reference/Models/base)
        - Set `Client.always_return_manifest_information` to `True`, see [here](/API Reference/client)

    Attributes:
        activity_hash: _No description given by bungie._
        bubble_hash: Note that a Bubble's hash doesn't uniquely identify a "top level" entity in Destiny. Only the combination of location and bubble can uniquely identify a place in the world of Destiny: so if bubbleHash is populated, locationHash must too be populated for it to have any meaning. You can use this property if it is populated to look up the DestinyLocationDefinition's associated .locationReleases[].activityBubbleName property.
        destination_hash: _No description given by bungie._
        display_properties: Even if no other associations exist, we will give you *something* for display properties. In cases where we have no associated entities, it may be as simple as a numerical identifier.
        hash: The identifier for this Checklist entry. Guaranteed unique only within this Checklist Definition, and not globally/for all checklists.
        item_hash: _No description given by bungie._
        location_hash: _No description given by bungie._
        scope: The scope at which this specific entry can be computed.
        vendor_hash: _No description given by bungie._
        vendor_interaction_index: _No description given by bungie._
        manifest_activity_hash: Manifest information for `activity_hash`
        manifest_destination_hash: Manifest information for `destination_hash`
        manifest_item_hash: Manifest information for `item_hash`
        manifest_location_hash: Manifest information for `location_hash`
        manifest_vendor_hash: Manifest information for `vendor_hash`
    """

    activity_hash: int = custom_field()
    bubble_hash: int = custom_field()
    destination_hash: int = custom_field()
    display_properties: "DestinyDisplayPropertiesDefinition" = custom_field()
    item_hash: int = custom_field()
    location_hash: int = custom_field()
    scope: Union["DestinyScope", int] = custom_field(converter=enum_converter("DestinyScope"))
    vendor_hash: int = custom_field()
    vendor_interaction_index: int = custom_field()
    manifest_activity_hash: Optional["DestinyActivityDefinition"] = custom_field(default=None)
    manifest_destination_hash: Optional["DestinyDestinationDefinition"] = custom_field(default=None)
    manifest_item_hash: Optional["DestinyInventoryItemDefinition"] = custom_field(default=None)
    manifest_location_hash: Optional["DestinyLocationDefinition"] = custom_field(default=None)
    manifest_vendor_hash: Optional["DestinyVendorDefinition"] = custom_field(default=None)
