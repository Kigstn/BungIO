# DO NOT CHANGE ANY CODE BELOW
# This file is generated automatically by `generate_api_schema.py` and will be overwritten
# Instead, change functions / models by subclassing them in the `./overwrites/` folder. They will be used instead.

from typing import Optional, TYPE_CHECKING

from bungio.models.base import BaseModel, custom_define, custom_field


if TYPE_CHECKING:
    from bungio.models import DestinyGuardianRankConstantsDefinition
    from bungio.models import DestinyFireteamFinderConstantsDefinition
    from bungio.models import DestinyPresentationNodeDefinition
    from bungio.models import DestinySeasonDefinition
    from bungio.models import EmailSettings
    from bungio.models import DestinyLoadoutConstantsDefinition
    from bungio.models import DestinyVendorDefinition


@custom_define()
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
        default_group_theme: _No description given by bungie._
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

    clan_banner_decal_colors: list["CoreSetting"] = custom_field(metadata={"type": """list[CoreSetting]"""})
    clan_banner_decals: list["CoreSetting"] = custom_field(metadata={"type": """list[CoreSetting]"""})
    clan_banner_gonfalon_colors: list["CoreSetting"] = custom_field(metadata={"type": """list[CoreSetting]"""})
    clan_banner_gonfalon_detail_colors: list["CoreSetting"] = custom_field(metadata={"type": """list[CoreSetting]"""})
    clan_banner_gonfalon_details: list["CoreSetting"] = custom_field(metadata={"type": """list[CoreSetting]"""})
    clan_banner_gonfalons: list["CoreSetting"] = custom_field(metadata={"type": """list[CoreSetting]"""})
    clan_banner_standards: list["CoreSetting"] = custom_field(metadata={"type": """list[CoreSetting]"""})
    default_group_theme: "CoreSetting" = custom_field()
    destiny2_core_settings: "Destiny2CoreSettings" = custom_field()
    destiny_membership_types: list["CoreSetting"] = custom_field(metadata={"type": """list[CoreSetting]"""})
    email_settings: "EmailSettings" = custom_field()
    environment: str = custom_field()
    fireteam_activities: list["CoreSetting"] = custom_field(metadata={"type": """list[CoreSetting]"""})
    forum_categories: list["CoreSetting"] = custom_field(metadata={"type": """list[CoreSetting]"""})
    group_avatars: list["CoreSetting"] = custom_field(metadata={"type": """list[CoreSetting]"""})
    ignore_reasons: list["CoreSetting"] = custom_field(metadata={"type": """list[CoreSetting]"""})
    recruitment_activities: list["CoreSetting"] = custom_field(metadata={"type": """list[CoreSetting]"""})
    recruitment_misc_tags: list["CoreSetting"] = custom_field(metadata={"type": """list[CoreSetting]"""})
    recruitment_platform_tags: list["CoreSetting"] = custom_field(metadata={"type": """list[CoreSetting]"""})
    system_content_locales: list["CoreSetting"] = custom_field(metadata={"type": """list[CoreSetting]"""})
    systems: dict[str, "CoreSystem"] = custom_field(metadata={"type": """dict[str, CoreSystem]"""})
    user_content_locales: list["CoreSetting"] = custom_field(metadata={"type": """list[CoreSetting]"""})


@custom_define()
class CoreSystem(BaseModel):
    """
    _No description given by bungie._

    None
    Attributes:
        enabled: _No description given by bungie._
        parameters: _No description given by bungie._
    """

    enabled: bool = custom_field()
    parameters: dict[str, str] = custom_field(metadata={"type": """dict[str, str]"""})


@custom_define()
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

    child_settings: list["CoreSetting"] = custom_field(metadata={"type": """list[CoreSetting]"""})
    display_name: str = custom_field()
    identifier: str = custom_field()
    image_path: str = custom_field()
    is_default: bool = custom_field()
    summary: str = custom_field()


@custom_define()
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
        enabled_fireteam_finder_activity_graph_hashes: _No description given by bungie._
        exotic_catalysts_root_node_hash: _No description given by bungie._
        fireteam_finder_constants_hash: _No description given by bungie._
        future_season_hashes: _No description given by bungie._
        guardian_rank_constants_hash: _No description given by bungie._
        guardian_ranks_root_node_hash: _No description given by bungie._
        insert_plug_free_blocked_socket_type_hashes: _No description given by bungie._
        insert_plug_free_protected_plug_item_hashes: _No description given by bungie._
        legacy_seals_root_node_hash: _No description given by bungie._
        legacy_triumphs_root_node_hash: _No description given by bungie._
        loadout_constants_hash: _No description given by bungie._
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
        manifest_fireteam_finder_constants_hash: Manifest information for `fireteam_finder_constants_hash`
        manifest_guardian_rank_constants_hash: Manifest information for `guardian_rank_constants_hash`
        manifest_guardian_ranks_root_node_hash: Manifest information for `guardian_ranks_root_node_hash`
        manifest_legacy_seals_root_node_hash: Manifest information for `legacy_seals_root_node_hash`
        manifest_legacy_triumphs_root_node_hash: Manifest information for `legacy_triumphs_root_node_hash`
        manifest_loadout_constants_hash: Manifest information for `loadout_constants_hash`
        manifest_lore_root_node_hash: Manifest information for `lore_root_node_hash`
        manifest_medals_root_node: Manifest information for `medals_root_node`
        manifest_medals_root_node_hash: Manifest information for `medals_root_node_hash`
        manifest_metrics_root_node: Manifest information for `metrics_root_node`
        manifest_records_root_node: Manifest information for `records_root_node`
        manifest_seasonal_challenges_presentation_node_hash: Manifest information for `seasonal_challenges_presentation_node_hash`
    """

    active_seals_root_node_hash: int = custom_field()
    active_triumphs_root_node_hash: int = custom_field()
    ammo_type_heavy_icon: str = custom_field()
    ammo_type_primary_icon: str = custom_field()
    ammo_type_special_icon: str = custom_field()
    badges_root_node: int = custom_field()
    collection_root_node: int = custom_field()
    crafting_root_node_hash: int = custom_field()
    current_rank_progression_hashes: list[int] = custom_field(metadata={"type": """list[int]"""})
    current_season_hash: int = custom_field()
    current_seasonal_artifact_hash: int = custom_field()
    enabled_fireteam_finder_activity_graph_hashes: list[int] = custom_field(metadata={"type": """list[int]"""})
    exotic_catalysts_root_node_hash: int = custom_field()
    fireteam_finder_constants_hash: int = custom_field()
    future_season_hashes: list[int] = custom_field(metadata={"type": """list[int]"""})
    guardian_rank_constants_hash: int = custom_field()
    guardian_ranks_root_node_hash: int = custom_field()
    insert_plug_free_blocked_socket_type_hashes: list[int] = custom_field(metadata={"type": """list[int]"""})
    insert_plug_free_protected_plug_item_hashes: list[int] = custom_field(metadata={"type": """list[int]"""})
    legacy_seals_root_node_hash: int = custom_field()
    legacy_triumphs_root_node_hash: int = custom_field()
    loadout_constants_hash: int = custom_field()
    lore_root_node_hash: int = custom_field()
    medals_root_node: int = custom_field()
    medals_root_node_hash: int = custom_field()
    metrics_root_node: int = custom_field()
    past_season_hashes: list[int] = custom_field(metadata={"type": """list[int]"""})
    records_root_node: int = custom_field()
    seasonal_challenges_presentation_node_hash: int = custom_field()
    undiscovered_collectible_image: str = custom_field()
    manifest_active_seals_root_node_hash: Optional["DestinyPresentationNodeDefinition"] = custom_field(default=None)
    manifest_active_triumphs_root_node_hash: Optional["DestinyPresentationNodeDefinition"] = custom_field(default=None)
    manifest_badges_root_node: Optional["DestinyPresentationNodeDefinition"] = custom_field(default=None)
    manifest_collection_root_node: Optional["DestinyPresentationNodeDefinition"] = custom_field(default=None)
    manifest_crafting_root_node_hash: Optional["DestinyPresentationNodeDefinition"] = custom_field(default=None)
    manifest_current_season_hash: Optional["DestinySeasonDefinition"] = custom_field(default=None)
    manifest_current_seasonal_artifact_hash: Optional["DestinyVendorDefinition"] = custom_field(default=None)
    manifest_exotic_catalysts_root_node_hash: Optional["DestinyPresentationNodeDefinition"] = custom_field(default=None)
    manifest_fireteam_finder_constants_hash: Optional["DestinyFireteamFinderConstantsDefinition"] = custom_field(
        default=None
    )
    manifest_guardian_rank_constants_hash: Optional["DestinyGuardianRankConstantsDefinition"] = custom_field(
        default=None
    )
    manifest_guardian_ranks_root_node_hash: Optional["DestinyPresentationNodeDefinition"] = custom_field(default=None)
    manifest_legacy_seals_root_node_hash: Optional["DestinyPresentationNodeDefinition"] = custom_field(default=None)
    manifest_legacy_triumphs_root_node_hash: Optional["DestinyPresentationNodeDefinition"] = custom_field(default=None)
    manifest_loadout_constants_hash: Optional["DestinyLoadoutConstantsDefinition"] = custom_field(default=None)
    manifest_lore_root_node_hash: Optional["DestinyPresentationNodeDefinition"] = custom_field(default=None)
    manifest_medals_root_node: Optional["DestinyPresentationNodeDefinition"] = custom_field(default=None)
    manifest_medals_root_node_hash: Optional["DestinyPresentationNodeDefinition"] = custom_field(default=None)
    manifest_metrics_root_node: Optional["DestinyPresentationNodeDefinition"] = custom_field(default=None)
    manifest_records_root_node: Optional["DestinyPresentationNodeDefinition"] = custom_field(default=None)
    manifest_seasonal_challenges_presentation_node_hash: Optional["DestinyPresentationNodeDefinition"] = custom_field(
        default=None
    )
