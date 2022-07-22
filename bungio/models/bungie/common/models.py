# DO NOT CHANGE ANY CODE BELOW
# This file is generated automatically by `generate_api_schema.py` and will be overwritten
# Instead, change functions / models by subclassing them in the `./overwrites/` folder. They will be used instead.

from typing import TYPE_CHECKING, Optional

import attr

from bungio.models.base import BaseModel

if TYPE_CHECKING:
    from bungio.models import (
        DestinyPresentationNodeDefinition,
        DestinySeasonDefinition,
        DestinyVendorDefinition,
        EmailSettings,
    )


@attr.define
class CoreSettingsConfiguration(BaseModel):
    """
    _No description given by bungie._

    None
    Attributes:
        clan_banner_decal_colors: _No description given by bungie._
        clan_banner_decals: _No description given by bungie._
        clan_banner_gonfalon_colors: _No description given by bungie._
        clan_banner_gonfalon_detail_colors: _No description given by bungie._
        clan_banner_gonfalon_details: _No description given by bungie._
        clan_banner_gonfalons: _No description given by bungie._
        clan_banner_standards: _No description given by bungie._
        destiny2_core_settings: _No description given by bungie._
        destiny_membership_types: _No description given by bungie._
        email_settings: _No description given by bungie._
        environment: _No description given by bungie._
        fireteam_activities: _No description given by bungie._
        forum_categories: _No description given by bungie._
        group_avatars: _No description given by bungie._
        ignore_reasons: _No description given by bungie._
        recruitment_activities: _No description given by bungie._
        recruitment_misc_tags: _No description given by bungie._
        recruitment_platform_tags: _No description given by bungie._
        system_content_locales: _No description given by bungie._
        systems: _No description given by bungie._
        user_content_locales: _No description given by bungie._
    """

    clan_banner_decal_colors: list["CoreSetting"] = attr.field(metadata={"type": """list[CoreSetting]"""})
    clan_banner_decals: list["CoreSetting"] = attr.field(metadata={"type": """list[CoreSetting]"""})
    clan_banner_gonfalon_colors: list["CoreSetting"] = attr.field(metadata={"type": """list[CoreSetting]"""})
    clan_banner_gonfalon_detail_colors: list["CoreSetting"] = attr.field(metadata={"type": """list[CoreSetting]"""})
    clan_banner_gonfalon_details: list["CoreSetting"] = attr.field(metadata={"type": """list[CoreSetting]"""})
    clan_banner_gonfalons: list["CoreSetting"] = attr.field(metadata={"type": """list[CoreSetting]"""})
    clan_banner_standards: list["CoreSetting"] = attr.field(metadata={"type": """list[CoreSetting]"""})
    destiny2_core_settings: "Destiny2CoreSettings" = attr.field()
    destiny_membership_types: list["CoreSetting"] = attr.field(metadata={"type": """list[CoreSetting]"""})
    email_settings: "EmailSettings" = attr.field()
    environment: str = attr.field()
    fireteam_activities: list["CoreSetting"] = attr.field(metadata={"type": """list[CoreSetting]"""})
    forum_categories: list["CoreSetting"] = attr.field(metadata={"type": """list[CoreSetting]"""})
    group_avatars: list["CoreSetting"] = attr.field(metadata={"type": """list[CoreSetting]"""})
    ignore_reasons: list["CoreSetting"] = attr.field(metadata={"type": """list[CoreSetting]"""})
    recruitment_activities: list["CoreSetting"] = attr.field(metadata={"type": """list[CoreSetting]"""})
    recruitment_misc_tags: list["CoreSetting"] = attr.field(metadata={"type": """list[CoreSetting]"""})
    recruitment_platform_tags: list["CoreSetting"] = attr.field(metadata={"type": """list[CoreSetting]"""})
    system_content_locales: list["CoreSetting"] = attr.field(metadata={"type": """list[CoreSetting]"""})
    systems: dict[str, "CoreSystem"] = attr.field(metadata={"type": """dict[str, CoreSystem]"""})
    user_content_locales: list["CoreSetting"] = attr.field(metadata={"type": """list[CoreSetting]"""})


@attr.define
class CoreSystem(BaseModel):
    """
    _No description given by bungie._

    None
    Attributes:
        enabled: _No description given by bungie._
        parameters: _No description given by bungie._
    """

    enabled: bool = attr.field()
    parameters: dict[str, str] = attr.field(metadata={"type": """dict[str, str]"""})


@attr.define
class CoreSetting(BaseModel):
    """
    _No description given by bungie._

    None
    Attributes:
        child_settings: _No description given by bungie._
        display_name: _No description given by bungie._
        identifier: _No description given by bungie._
        image_path: _No description given by bungie._
        is_default: _No description given by bungie._
        summary: _No description given by bungie._
    """

    child_settings: list["CoreSetting"] = attr.field(metadata={"type": """list[CoreSetting]"""})
    display_name: str = attr.field()
    identifier: str = attr.field()
    image_path: str = attr.field()
    is_default: bool = attr.field()
    summary: str = attr.field()


@attr.define
class Destiny2CoreSettings(BaseModel):
    """
    _No description given by bungie._

    Tip: Manifest Information
        This model has some attributes which can be filled with additional information found in the manifest (`manifest_...`).
        Without additional work, these attributes will be `None`, since they require additional requests and database lookups.

        To fill the manifest dependent attributes, either:

        - Run `await ThisClass.fetch_manifest_information()`, see [here](/API Reference/Models/base)
        - Set `Client.always_return_manifest_information` to `True`, see [here](/API Reference/client)

    Attributes:
        active_seals_root_node_hash: _No description given by bungie._
        active_triumphs_root_node_hash: _No description given by bungie._
        ammo_type_heavy_icon: _No description given by bungie._
        ammo_type_primary_icon: _No description given by bungie._
        ammo_type_special_icon: _No description given by bungie._
        badges_root_node: _No description given by bungie._
        collection_root_node: _No description given by bungie._
        crafting_root_node_hash: _No description given by bungie._
        current_rank_progression_hashes: _No description given by bungie._
        current_season_hash: _No description given by bungie._
        current_seasonal_artifact_hash: _No description given by bungie._
        exotic_catalysts_root_node_hash: _No description given by bungie._
        future_season_hashes: _No description given by bungie._
        insert_plug_free_blocked_socket_type_hashes: _No description given by bungie._
        insert_plug_free_protected_plug_item_hashes: _No description given by bungie._
        legacy_seals_root_node_hash: _No description given by bungie._
        legacy_triumphs_root_node_hash: _No description given by bungie._
        lore_root_node_hash: _No description given by bungie._
        medals_root_node: _No description given by bungie._
        medals_root_node_hash: _No description given by bungie._
        metrics_root_node: _No description given by bungie._
        past_season_hashes: _No description given by bungie._
        records_root_node: _No description given by bungie._
        seasonal_challenges_presentation_node_hash: _No description given by bungie._
        undiscovered_collectible_image: _No description given by bungie._
        manifest_active_seals_root_node_hash: Manifest information for `active_seals_root_node_hash`
        manifest_active_triumphs_root_node_hash: Manifest information for `active_triumphs_root_node_hash`
        manifest_badges_root_node: Manifest information for `badges_root_node`
        manifest_collection_root_node: Manifest information for `collection_root_node`
        manifest_crafting_root_node_hash: Manifest information for `crafting_root_node_hash`
        manifest_current_season_hash: Manifest information for `current_season_hash`
        manifest_current_seasonal_artifact_hash: Manifest information for `current_seasonal_artifact_hash`
        manifest_exotic_catalysts_root_node_hash: Manifest information for `exotic_catalysts_root_node_hash`
        manifest_legacy_seals_root_node_hash: Manifest information for `legacy_seals_root_node_hash`
        manifest_legacy_triumphs_root_node_hash: Manifest information for `legacy_triumphs_root_node_hash`
        manifest_lore_root_node_hash: Manifest information for `lore_root_node_hash`
        manifest_medals_root_node: Manifest information for `medals_root_node`
        manifest_medals_root_node_hash: Manifest information for `medals_root_node_hash`
        manifest_metrics_root_node: Manifest information for `metrics_root_node`
        manifest_records_root_node: Manifest information for `records_root_node`
        manifest_seasonal_challenges_presentation_node_hash: Manifest information for `seasonal_challenges_presentation_node_hash`
    """

    active_seals_root_node_hash: int = attr.field()
    active_triumphs_root_node_hash: int = attr.field()
    ammo_type_heavy_icon: str = attr.field()
    ammo_type_primary_icon: str = attr.field()
    ammo_type_special_icon: str = attr.field()
    badges_root_node: int = attr.field()
    collection_root_node: int = attr.field()
    crafting_root_node_hash: int = attr.field()
    current_rank_progression_hashes: list[int] = attr.field(metadata={"type": """list[int]"""})
    current_season_hash: int = attr.field()
    current_seasonal_artifact_hash: int = attr.field()
    exotic_catalysts_root_node_hash: int = attr.field()
    future_season_hashes: list[int] = attr.field(metadata={"type": """list[int]"""})
    insert_plug_free_blocked_socket_type_hashes: list[int] = attr.field(metadata={"type": """list[int]"""})
    insert_plug_free_protected_plug_item_hashes: list[int] = attr.field(metadata={"type": """list[int]"""})
    legacy_seals_root_node_hash: int = attr.field()
    legacy_triumphs_root_node_hash: int = attr.field()
    lore_root_node_hash: int = attr.field()
    medals_root_node: int = attr.field()
    medals_root_node_hash: int = attr.field()
    metrics_root_node: int = attr.field()
    past_season_hashes: list[int] = attr.field(metadata={"type": """list[int]"""})
    records_root_node: int = attr.field()
    seasonal_challenges_presentation_node_hash: int = attr.field()
    undiscovered_collectible_image: str = attr.field()
    manifest_active_seals_root_node_hash: Optional["DestinyPresentationNodeDefinition"] = attr.field(default=None)
    manifest_active_triumphs_root_node_hash: Optional["DestinyPresentationNodeDefinition"] = attr.field(default=None)
    manifest_badges_root_node: Optional["DestinyPresentationNodeDefinition"] = attr.field(default=None)
    manifest_collection_root_node: Optional["DestinyPresentationNodeDefinition"] = attr.field(default=None)
    manifest_crafting_root_node_hash: Optional["DestinyPresentationNodeDefinition"] = attr.field(default=None)
    manifest_current_season_hash: Optional["DestinySeasonDefinition"] = attr.field(default=None)
    manifest_current_seasonal_artifact_hash: Optional["DestinyVendorDefinition"] = attr.field(default=None)
    manifest_exotic_catalysts_root_node_hash: Optional["DestinyPresentationNodeDefinition"] = attr.field(default=None)
    manifest_legacy_seals_root_node_hash: Optional["DestinyPresentationNodeDefinition"] = attr.field(default=None)
    manifest_legacy_triumphs_root_node_hash: Optional["DestinyPresentationNodeDefinition"] = attr.field(default=None)
    manifest_lore_root_node_hash: Optional["DestinyPresentationNodeDefinition"] = attr.field(default=None)
    manifest_medals_root_node: Optional["DestinyPresentationNodeDefinition"] = attr.field(default=None)
    manifest_medals_root_node_hash: Optional["DestinyPresentationNodeDefinition"] = attr.field(default=None)
    manifest_metrics_root_node: Optional["DestinyPresentationNodeDefinition"] = attr.field(default=None)
    manifest_records_root_node: Optional["DestinyPresentationNodeDefinition"] = attr.field(default=None)
    manifest_seasonal_challenges_presentation_node_hash: Optional["DestinyPresentationNodeDefinition"] = attr.field(
        default=None
    )
