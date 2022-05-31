from typing import TYPE_CHECKING, Any

import attr

from bungio.models.base import BaseModel

if TYPE_CHECKING:
    from bungio.models import CoreSetting, Destiny2CoreSettings, EmailSettings


@attr.define
class CoreSettingsConfiguration(BaseModel):
    """
    _No description given_

    Attributes:
        environment: _No description given_
        systems: _No description given_
        ignore_reasons: _No description given_
        forum_categories: _No description given_
        group_avatars: _No description given_
        destiny_membership_types: _No description given_
        recruitment_platform_tags: _No description given_
        recruitment_misc_tags: _No description given_
        recruitment_activities: _No description given_
        user_content_locales: _No description given_
        system_content_locales: _No description given_
        clan_banner_decals: _No description given_
        clan_banner_decal_colors: _No description given_
        clan_banner_gonfalons: _No description given_
        clan_banner_gonfalon_colors: _No description given_
        clan_banner_gonfalon_details: _No description given_
        clan_banner_gonfalon_detail_colors: _No description given_
        clan_banner_standards: _No description given_
        destiny2_core_settings: _No description given_
        email_settings: _No description given_
        fireteam_activities: _No description given_
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
    _No description given_

    Attributes:
        enabled: _No description given_
        parameters: _No description given_
    """

    enabled: bool = attr.field()
    parameters: Any = attr.field()


@attr.define
class CoreSetting(BaseModel):
    """
    _No description given_

    Attributes:
        identifier: _No description given_
        is_default: _No description given_
        display_name: _No description given_
        summary: _No description given_
        image_path: _No description given_
        child_settings: _No description given_
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
    _No description given_

    Attributes:
        collection_root_node: _No description given_
        badges_root_node: _No description given_
        records_root_node: _No description given_
        medals_root_node: _No description given_
        metrics_root_node: _No description given_
        active_triumphs_root_node_hash: _No description given_
        active_seals_root_node_hash: _No description given_
        legacy_triumphs_root_node_hash: _No description given_
        legacy_seals_root_node_hash: _No description given_
        medals_root_node_hash: _No description given_
        exotic_catalysts_root_node_hash: _No description given_
        lore_root_node_hash: _No description given_
        crafting_root_node_hash: _No description given_
        current_rank_progression_hashes: _No description given_
        insert_plug_free_protected_plug_item_hashes: _No description given_
        insert_plug_free_blocked_socket_type_hashes: _No description given_
        undiscovered_collectible_image: _No description given_
        ammo_type_heavy_icon: _No description given_
        ammo_type_special_icon: _No description given_
        ammo_type_primary_icon: _No description given_
        current_seasonal_artifact_hash: _No description given_
        current_season_hash: _No description given_
        seasonal_challenges_presentation_node_hash: _No description given_
        future_season_hashes: _No description given_
        past_season_hashes: _No description given_
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
