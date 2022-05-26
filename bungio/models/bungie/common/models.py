import datetime
from typing import TYPE_CHECKING, Any, Optional

import attr

from bungio.models.base import BaseEnum, BaseModel


@attr.define
class CoreSettingsConfiguration(BaseModel):
    """
    Not specified.

    Attributes:
        environment: Not specified.
        systems: Not specified.
        ignore_reasons: Not specified.
        forum_categories: Not specified.
        group_avatars: Not specified.
        destiny_membership_types: Not specified.
        recruitment_platform_tags: Not specified.
        recruitment_misc_tags: Not specified.
        recruitment_activities: Not specified.
        user_content_locales: Not specified.
        system_content_locales: Not specified.
        clan_banner_decals: Not specified.
        clan_banner_decal_colors: Not specified.
        clan_banner_gonfalons: Not specified.
        clan_banner_gonfalon_colors: Not specified.
        clan_banner_gonfalon_details: Not specified.
        clan_banner_gonfalon_detail_colors: Not specified.
        clan_banner_standards: Not specified.
        destiny2_core_settings: Not specified.
        email_settings: Not specified.
        fireteam_activities: Not specified.
    """

    environment: str = attr.field()
    systems: Any = attr.field()
    ignore_reasons: list["CoreSetting"] = attr.field()
    forum_categories: list["CoreSetting"] = attr.field()
    group_avatars: list["CoreSetting"] = attr.field()
    destiny_membership_types: list["CoreSetting"] = attr.field()
    recruitment_platform_tags: list["CoreSetting"] = attr.field()
    recruitment_misc_tags: list["CoreSetting"] = attr.field()
    recruitment_activities: list["CoreSetting"] = attr.field()
    user_content_locales: list["CoreSetting"] = attr.field()
    system_content_locales: list["CoreSetting"] = attr.field()
    clan_banner_decals: list["CoreSetting"] = attr.field()
    clan_banner_decal_colors: list["CoreSetting"] = attr.field()
    clan_banner_gonfalons: list["CoreSetting"] = attr.field()
    clan_banner_gonfalon_colors: list["CoreSetting"] = attr.field()
    clan_banner_gonfalon_details: list["CoreSetting"] = attr.field()
    clan_banner_gonfalon_detail_colors: list["CoreSetting"] = attr.field()
    clan_banner_standards: list["CoreSetting"] = attr.field()
    destiny2_core_settings: "Destiny2CoreSettings" = attr.field()
    email_settings: "EmailSettings" = attr.field()
    fireteam_activities: list["CoreSetting"] = attr.field()


@attr.define
class CoreSystem(BaseModel):
    """
    Not specified.

    Attributes:
        enabled: Not specified.
        parameters: Not specified.
    """

    enabled: bool = attr.field()
    parameters: Any = attr.field()


@attr.define
class CoreSetting(BaseModel):
    """
    Not specified.

    Attributes:
        identifier: Not specified.
        is_default: Not specified.
        display_name: Not specified.
        summary: Not specified.
        image_path: Not specified.
        child_settings: Not specified.
    """

    identifier: str = attr.field()
    is_default: bool = attr.field()
    display_name: str = attr.field()
    summary: str = attr.field()
    image_path: str = attr.field()
    child_settings: list["CoreSetting"] = attr.field()


@attr.define
class Destiny2CoreSettings(BaseModel):
    """
    Not specified.

    Attributes:
        collection_root_node: Not specified.
        badges_root_node: Not specified.
        records_root_node: Not specified.
        medals_root_node: Not specified.
        metrics_root_node: Not specified.
        active_triumphs_root_node_hash: Not specified.
        active_seals_root_node_hash: Not specified.
        legacy_triumphs_root_node_hash: Not specified.
        legacy_seals_root_node_hash: Not specified.
        medals_root_node_hash: Not specified.
        exotic_catalysts_root_node_hash: Not specified.
        lore_root_node_hash: Not specified.
        crafting_root_node_hash: Not specified.
        current_rank_progression_hashes: Not specified.
        insert_plug_free_protected_plug_item_hashes: Not specified.
        insert_plug_free_blocked_socket_type_hashes: Not specified.
        undiscovered_collectible_image: Not specified.
        ammo_type_heavy_icon: Not specified.
        ammo_type_special_icon: Not specified.
        ammo_type_primary_icon: Not specified.
        current_seasonal_artifact_hash: Not specified.
        current_season_hash: Not specified.
        seasonal_challenges_presentation_node_hash: Not specified.
        future_season_hashes: Not specified.
        past_season_hashes: Not specified.
    """

    collection_root_node: int = attr.field()
    badges_root_node: int = attr.field()
    records_root_node: int = attr.field()
    medals_root_node: int = attr.field()
    metrics_root_node: int = attr.field()
    active_triumphs_root_node_hash: int = attr.field()
    active_seals_root_node_hash: int = attr.field()
    legacy_triumphs_root_node_hash: int = attr.field()
    legacy_seals_root_node_hash: int = attr.field()
    medals_root_node_hash: int = attr.field()
    exotic_catalysts_root_node_hash: int = attr.field()
    lore_root_node_hash: int = attr.field()
    crafting_root_node_hash: int = attr.field()
    current_rank_progression_hashes: list[int] = attr.field()
    insert_plug_free_protected_plug_item_hashes: list[int] = attr.field()
    insert_plug_free_blocked_socket_type_hashes: list[int] = attr.field()
    undiscovered_collectible_image: str = attr.field()
    ammo_type_heavy_icon: str = attr.field()
    ammo_type_special_icon: str = attr.field()
    ammo_type_primary_icon: str = attr.field()
    current_seasonal_artifact_hash: int = attr.field()
    current_season_hash: int = attr.field()
    seasonal_challenges_presentation_node_hash: int = attr.field()
    future_season_hashes: list[int] = attr.field()
    past_season_hashes: list[int] = attr.field()
