# DO NOT CHANGE ANY CODE BELOW
# This file is generated automatically by `generate_api_schema.py` and will be overwritten
# Instead, change functions / models by subclassing them in the `./overwrites/` folder. They will be used instead.


from bungio.models.base import BaseModel, HashObject, custom_define, custom_field


@custom_define()
class DestinyActivityInteractableDefinition(BaseModel, HashObject):
    """
    There are times in every Activity's life when interacting with an object in the world will result in another Activity activating. Well, not every Activity. Just certain ones. Anyways, this defines a set of interactable components, the activities that they spawn when you interact with them, and the conditions under which they can be interacted with. Sadly, we don't get any *really* good data for them, like positional data... yet. I have hopes for future data that we could put on this.

    None
    Attributes:
        entries: The possible interactables in this activity interactable definition.
        hash: The unique identifier for this entity. Guaranteed to be unique for the type of entity, but not globally. When entities refer to each other in Destiny content, it is this hash that they are referring to.
        index: The index of the entity as it was found in the investment tables.
        redacted: If this is true, then there is an entity with this identifier/type combination, but BNet is not yet allowed to show it. Sorry!
    """

    entries: list["DestinyActivityInteractableEntryDefinition"] = custom_field(
        metadata={"type": """list[DestinyActivityInteractableEntryDefinition]"""}
    )
    index: int = custom_field()
    redacted: bool = custom_field()


@custom_define()
class DestinyActivityInteractableEntryDefinition(BaseModel):
    """
    Defines a specific interactable and the action that can occur when triggered.

    None
    Attributes:
        activity_hash: The activity that will trigger when you interact with this interactable.
    """

    activity_hash: int = custom_field()
