# DO NOT CHANGE ANY CODE BELOW
# This file is generated automatically by `generate_api_schema.py` and will be overwritten
# Instead, change functions / models by subclassing them in the `./overwrites/` folder. They will be used instead.


from bungio.models.base import HashObject, ManifestModel, custom_define, custom_field


@custom_define()
class DestinyPowerCapDefinition(ManifestModel, HashObject):
    """
    Defines a 'power cap' (limit) for gear items, based on the rarity tier and season of release.

    None
    Attributes:
        hash: The unique identifier for this entity. Guaranteed to be unique for the type of entity, but not globally. When entities refer to each other in Destiny content, it is this hash that they are referring to.
        index: The index of the entity as it was found in the investment tables.
        power_cap: The raw value for a power cap.
        redacted: If this is true, then there is an entity with this identifier/type combination, but BNet is not yet allowed to show it. Sorry!
    """

    index: int = custom_field()
    power_cap: int = custom_field()
    redacted: bool = custom_field()
