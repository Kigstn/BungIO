from typing import TYPE_CHECKING

import attr

from bungio.models.base import BaseModel

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


@attr.define
class DestinyChecklistDefinition(BaseModel):
    """
    By public demand, Checklists are loose sets of "things to do/things you have done" in Destiny that we were actually able to track. They include easter eggs you find in the world, unique chests you unlock, and other such data where the first time you do it is significant enough to be tracked, and you have the potential to "get them all". These may be account-wide, or may be per character. The status of these will be returned in related "Checklist" data coming down from API requests such as GetProfile or GetCharacter. Generally speaking, the items in a checklist can be completed in any order: we return an ordered list which only implies the way we are showing them in our own UI, and you can feel free to alter it as you wish. Note that, in the future, there will be something resembling the old D1 Record Books in at least some vague form. When that is created, it may be that it will supercede much or all of this Checklist data. It remains to be seen if that will be the case, so for now assume that the Checklists will still exist even after the release of D2: Forsaken.

    Attributes:
        display_properties: _No description given by bungie_
        view_action_string: A localized string prompting you to view the checklist.
        scope: Indicates whether you will find this checklist on the Profile or Character components.
        entries: The individual checklist items. Gotta catch 'em all.
        hash: The unique identifier for this entity. Guaranteed to be unique for the type of entity, but not globally. When entities refer to each other in Destiny content, it is this hash that they are referring to.
        index: The index of the entity as it was found in the investment tables.
        redacted: If this is true, then there is an entity with this identifier/type combination, but BNet is not yet allowed to show it. Sorry!
    """

    display_properties: "DestinyDisplayPropertiesDefinition" = attr.field()
    view_action_string: str = attr.field()
    scope: "DestinyScope" = attr.field()
    entries: list["DestinyChecklistEntryDefinition"] = attr.field()
    hash: int = attr.field()
    index: int = attr.field()
    redacted: bool = attr.field()


@attr.define
class DestinyChecklistEntryDefinition(BaseModel):
    """
    The properties of an individual checklist item. Note that almost everything is optional: it is *highly* variable what kind of data we'll actually be able to return: at times we may have no other relationships to entities at all. Whatever UI you build, do it with the knowledge that any given entry might not actually be able to be associated with some other Destiny entity.

    Attributes:
        hash: The identifier for this Checklist entry. Guaranteed unique only within this Checklist Definition, and not globally/for all checklists.
        display_properties: Even if no other associations exist, we will give you *something* for display properties. In cases where we have no associated entities, it may be as simple as a numerical identifier.
        destination_hash: _No description given by bungie_
        location_hash: _No description given by bungie_
        bubble_hash: Note that a Bubble's hash doesn't uniquely identify a "top level" entity in Destiny. Only the combination of location and bubble can uniquely identify a place in the world of Destiny: so if bubbleHash is populated, locationHash must too be populated for it to have any meaning. You can use this property if it is populated to look up the DestinyLocationDefinition's associated .locationReleases[].activityBubbleName property.
        activity_hash: _No description given by bungie_
        item_hash: _No description given by bungie_
        vendor_hash: _No description given by bungie_
        vendor_interaction_index: _No description given by bungie_
        scope: The scope at which this specific entry can be computed.
    """

    hash: int = attr.field()
    display_properties: "DestinyDisplayPropertiesDefinition" = attr.field()
    destination_hash: "DestinyDestinationDefinition" = attr.field()
    location_hash: "DestinyLocationDefinition" = attr.field()
    bubble_hash: int = attr.field()
    activity_hash: "DestinyActivityDefinition" = attr.field()
    item_hash: "DestinyInventoryItemDefinition" = attr.field()
    vendor_hash: "DestinyVendorDefinition" = attr.field()
    vendor_interaction_index: int = attr.field()
    scope: "DestinyScope" = attr.field()
