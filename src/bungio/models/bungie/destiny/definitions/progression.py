# DO NOT CHANGE ANY CODE BELOW
# This file is generated automatically by `generate_api_schema.py` and will be overwritten
# Instead, change functions / models by subclassing them in the `./overwrites/` folder. They will be used instead.

from typing import TYPE_CHECKING, Optional

from bungio.models.base import HashObject, ManifestModel, custom_define, custom_field

if TYPE_CHECKING:
    from bungio.models import DestinyProgressionDefinition, InterpolationPointFloat


@custom_define()
class DestinyProgressionLevelRequirementDefinition(ManifestModel, HashObject):
    """
    These are pre-constructed collections of data that can be used to determine the Level Requirement for an item given a Progression to be tested (such as the Character's level). For instance, say a character receives a new Auto Rifle, and that Auto Rifle's DestinyInventoryItemDefinition.quality.progressionLevelRequirementHash property is pointing at one of these DestinyProgressionLevelRequirementDefinitions. Let's pretend also that the progressionHash it is pointing at is the Character Level progression. In that situation, the character's level will be used to interpolate a value in the requirementCurve property. The value picked up from that interpolation will be the required level for the item.

    Tip: Manifest Information
        This model has some attributes which can be filled with additional information found in the manifest (`manifest_...`).
        Without additional work, these attributes will be `None`, since they require additional requests and database lookups.

        To fill the manifest dependent attributes, either:

        - Run `await ThisClass.fetch_manifest_information()`, see [here](/API Reference/Models/base)
        - Set `Client.always_return_manifest_information` to `True`, see [here](/API Reference/client)

    Attributes:
        hash: The unique identifier for this entity. Guaranteed to be unique for the type of entity, but not globally. When entities refer to each other in Destiny content, it is this hash that they are referring to.
        index: The index of the entity as it was found in the investment tables.
        progression_hash: The progression whose level should be used to determine the level requirement. Look up the DestinyProgressionDefinition with this hash for more information about the progression in question.
        redacted: If this is true, then there is an entity with this identifier/type combination, but BNet is not yet allowed to show it. Sorry!
        requirement_curve: A curve of level requirements, weighted by the related progressions' level. Interpolate against this curve with the character's progression level to determine what the level requirement of the generated item that is using this data will be.
        manifest_progression_hash: Manifest information for `progression_hash`
    """

    index: int = custom_field()
    progression_hash: int = custom_field()
    redacted: bool = custom_field()
    requirement_curve: list["InterpolationPointFloat"] = custom_field(
        metadata={"type": """list[InterpolationPointFloat]"""}
    )
    manifest_progression_hash: Optional["DestinyProgressionDefinition"] = custom_field(default=None)
