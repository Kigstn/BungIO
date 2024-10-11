# DO NOT CHANGE ANY CODE BELOW
# This file is generated automatically by `generate_api_schema.py` and will be overwritten
# Instead, change functions / models by subclassing them in the `./overwrites/` folder. They will be used instead.

from typing import TYPE_CHECKING, Optional

from bungio.models.base import BaseModel, HashObject, ManifestModel, custom_define, custom_field

if TYPE_CHECKING:
    from bungio.models import DestinyActivityDefinition


@custom_define()
class DestinyActivityInteractableDefinition(ManifestModel, HashObject):
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

    Tip: Manifest Information
        This model has some attributes which can be filled with additional information found in the manifest (`manifest_...`).
        Without additional work, these attributes will be `None`, since they require additional requests and database lookups.

        To fill the manifest dependent attributes, either:

        - Run `await ThisClass.fetch_manifest_information()`, see [here](/API Reference/Models/base)
        - Set `Client.always_return_manifest_information` to `True`, see [here](/API Reference/client)

    Attributes:
        activity_hash: The activity that will trigger when you interact with this interactable.
        manifest_activity_hash: Manifest information for `activity_hash`
    """

    activity_hash: int = custom_field()
    manifest_activity_hash: Optional["DestinyActivityDefinition"] = custom_field(default=None)
