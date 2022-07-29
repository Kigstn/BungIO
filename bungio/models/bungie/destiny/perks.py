# DO NOT CHANGE ANY CODE BELOW
# This file is generated automatically by `generate_api_schema.py` and will be overwritten
# Instead, change functions / models by subclassing them in the `./overwrites/` folder. They will be used instead.

from typing import TYPE_CHECKING, Optional

from bungio.models.base import BaseModel, custom_define, custom_field

if TYPE_CHECKING:
    from bungio.models import DestinySandboxPerkDefinition


@custom_define()
class DestinyPerkReference(BaseModel):
    """
    The list of perks to display in an item tooltip - and whether or not they have been activated. Perks apply a variety of effects to a character, and are generally either intrinsic to the item or provided in activated talent nodes or sockets.

    Tip: Manifest Information
        This model has some attributes which can be filled with additional information found in the manifest (`manifest_...`).
        Without additional work, these attributes will be `None`, since they require additional requests and database lookups.

        To fill the manifest dependent attributes, either:

        - Run `await ThisClass.fetch_manifest_information()`, see [here](/API Reference/Models/base)
        - Set `Client.always_return_manifest_information` to `True`, see [here](/API Reference/client)

    Attributes:
        icon_path: The icon for the perk.
        is_active: Whether this perk is currently active. (We may return perks that you have not actually activated yet: these represent perks that you should show in the item's tooltip, but that the user has not yet activated.)
        perk_hash: The hash identifier for the perk, which can be used to look up DestinySandboxPerkDefinition if it exists. Be warned, perks frequently do not have user-viewable information. You should examine whether you actually found a name/description in the perk's definition before you show it to the user.
        visible: Some perks provide benefits, but aren't visible in the UI. This value will let you know if this is perk should be shown in your UI.
        manifest_perk_hash: Manifest information for `perk_hash`
    """

    icon_path: str = custom_field()
    is_active: bool = custom_field()
    perk_hash: int = custom_field()
    visible: bool = custom_field()
    manifest_perk_hash: Optional["DestinySandboxPerkDefinition"] = custom_field(default=None)
