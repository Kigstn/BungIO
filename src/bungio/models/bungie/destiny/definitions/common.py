# DO NOT CHANGE ANY CODE BELOW
# This file is generated automatically by `generate_api_schema.py` and will be overwritten
# Instead, change functions / models by subclassing them in the `./overwrites/` folder. They will be used instead.

from typing import TYPE_CHECKING, Optional

from bungio.models.base import BaseModel, HashObject, ManifestModel, custom_define, custom_field

if TYPE_CHECKING:
    from bungio.models import (
        DestinyEventCardDefinition,
        DestinyIconDefinition,
        DestinyItemFilterDefinition,
        DestinyPlugSetDefinition,
        DestinyPresentationNodeDefinition,
    )


@custom_define()
class DestinyDisplayPropertiesDefinition(BaseModel):
    """
    Many Destiny*Definition contracts - the "first order" entities of Destiny that have their own tables in the Manifest Database - also have displayable information. This is the base class for that display information.

    Tip: Manifest Information
        This model has some attributes which can be filled with additional information found in the manifest (`manifest_...`).
        Without additional work, these attributes will be `None`, since they require additional requests and database lookups.

        To fill the manifest dependent attributes, either:

        - Run `await ThisClass.fetch_manifest_information()`, see [here](/API Reference/Models/base)
        - Set `Client.always_return_manifest_information` to `True`, see [here](/API Reference/client)

    Attributes:
        description: _No description given by bungie._
        has_icon: _No description given by bungie._
        high_res_icon: If this item has a high-res icon (at least for now, many things won't), then the path to that icon will be here.
        icon: Note that "icon" is sometimes misleading, and should be interpreted in the context of the entity. For instance, in Destiny 1 the DestinyRecordBookDefinition's icon was a big picture of a book. But usually, it will be a small square image that you can use as... well, an icon. They are currently represented as 96px x 96px images.
        icon_hash: _No description given by bungie._
        icon_sequences: _No description given by bungie._
        name: _No description given by bungie._
        manifest_icon_hash: Manifest information for `icon_hash`
    """

    description: str = custom_field()
    has_icon: bool = custom_field()
    high_res_icon: str = custom_field()
    icon: str = custom_field()
    icon_hash: int = custom_field()
    icon_sequences: list["DestinyIconSequenceDefinition"] = custom_field(
        metadata={"type": """list[DestinyIconSequenceDefinition]"""}
    )
    name: str = custom_field()
    manifest_icon_hash: Optional["DestinyIconDefinition"] = custom_field(default=None)


@custom_define()
class DestinyIconSequenceDefinition(BaseModel):
    """
    _No description given by bungie._

    None
    Attributes:
        frames: _No description given by bungie._
    """

    frames: list[str] = custom_field(metadata={"type": """list[str]"""})


@custom_define()
class DestinyPositionDefinition(BaseModel):
    """
    _No description given by bungie._

    None
    Attributes:
        x: _No description given by bungie._
        y: _No description given by bungie._
        z: _No description given by bungie._
    """

    x: int = custom_field()
    y: int = custom_field()
    z: int = custom_field()


@custom_define()
class DestinyGlobalConstantsDefinition(ManifestModel, HashObject):
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
        armor_archetype_plug_set_hash: _No description given by bungie._
        collection_badges_root_node_hash: _No description given by bungie._
        collections_root_node_hash: _No description given by bungie._
        crafting_root_node_hash: _No description given by bungie._
        destiny_reward_pass_rank_seal_images: _No description given by bungie._
        destiny_seasonal_hub_rank_icon_images: _No description given by bungie._
        exotic_catalysts_root_node_hash: _No description given by bungie._
        featured_items_list_hash: _No description given by bungie._
        guardian_ranks_root_node_hash: _No description given by bungie._
        hash: The unique identifier for this entity. Guaranteed to be unique for the type of entity, but not globally. When entities refer to each other in Destiny content, it is this hash that they are referring to.
        index: The index of the entity as it was found in the investment tables.
        legacy_seals_root_node_hash: _No description given by bungie._
        legacy_triumphs_root_node_hash: _No description given by bungie._
        lore_root_node_hash: _No description given by bungie._
        medals_root_node_hash: _No description given by bungie._
        metrics_root_node_hash: _No description given by bungie._
        order_rewards_unlock_value_hashes_to_reward_item_hashes: _No description given by bungie._
        pathfinder_constants: Assorted constants for Pathfinder objectives
        portal_activity_graph_root_nodes_with_icons: _No description given by bungie._
        quest_item_trait_to_featured_quest_image_path: _No description given by bungie._
        redacted: If this is true, then there is an entity with this identifier/type combination, but BNet is not yet allowed to show it. Sorry!
        seasonal_hub_event_card_hash: _No description given by bungie._
        manifest_active_seals_root_node_hash: Manifest information for `active_seals_root_node_hash`
        manifest_active_triumphs_root_node_hash: Manifest information for `active_triumphs_root_node_hash`
        manifest_armor_archetype_plug_set_hash: Manifest information for `armor_archetype_plug_set_hash`
        manifest_collection_badges_root_node_hash: Manifest information for `collection_badges_root_node_hash`
        manifest_collections_root_node_hash: Manifest information for `collections_root_node_hash`
        manifest_crafting_root_node_hash: Manifest information for `crafting_root_node_hash`
        manifest_exotic_catalysts_root_node_hash: Manifest information for `exotic_catalysts_root_node_hash`
        manifest_featured_items_list_hash: Manifest information for `featured_items_list_hash`
        manifest_guardian_ranks_root_node_hash: Manifest information for `guardian_ranks_root_node_hash`
        manifest_legacy_seals_root_node_hash: Manifest information for `legacy_seals_root_node_hash`
        manifest_legacy_triumphs_root_node_hash: Manifest information for `legacy_triumphs_root_node_hash`
        manifest_lore_root_node_hash: Manifest information for `lore_root_node_hash`
        manifest_medals_root_node_hash: Manifest information for `medals_root_node_hash`
        manifest_metrics_root_node_hash: Manifest information for `metrics_root_node_hash`
        manifest_seasonal_hub_event_card_hash: Manifest information for `seasonal_hub_event_card_hash`
    """

    active_seals_root_node_hash: int = custom_field()
    active_triumphs_root_node_hash: int = custom_field()
    armor_archetype_plug_set_hash: int = custom_field()
    collection_badges_root_node_hash: int = custom_field()
    collections_root_node_hash: int = custom_field()
    crafting_root_node_hash: int = custom_field()
    destiny_reward_pass_rank_seal_images: "DestinyRewardPassRankSealImages" = custom_field()
    destiny_seasonal_hub_rank_icon_images: "DestinySeasonalHubRankIconImages" = custom_field()
    exotic_catalysts_root_node_hash: int = custom_field()
    featured_items_list_hash: int = custom_field()
    guardian_ranks_root_node_hash: int = custom_field()
    index: int = custom_field()
    legacy_seals_root_node_hash: int = custom_field()
    legacy_triumphs_root_node_hash: int = custom_field()
    lore_root_node_hash: int = custom_field()
    medals_root_node_hash: int = custom_field()
    metrics_root_node_hash: int = custom_field()
    order_rewards_unlock_value_hashes_to_reward_item_hashes: dict[int, int] = custom_field(
        metadata={"type": """dict[int, int]"""}
    )
    pathfinder_constants: "DestinyPathfinderConstantsDefinition" = custom_field()
    portal_activity_graph_root_nodes_with_icons: dict[int, str] = custom_field(metadata={"type": """dict[int, str]"""})
    quest_item_trait_to_featured_quest_image_path: dict[int, str] = custom_field(
        metadata={"type": """dict[int, str]"""}
    )
    redacted: bool = custom_field()
    seasonal_hub_event_card_hash: int = custom_field()
    manifest_active_seals_root_node_hash: Optional["DestinyPresentationNodeDefinition"] = custom_field(default=None)
    manifest_active_triumphs_root_node_hash: Optional["DestinyPresentationNodeDefinition"] = custom_field(default=None)
    manifest_armor_archetype_plug_set_hash: Optional["DestinyPlugSetDefinition"] = custom_field(default=None)
    manifest_collection_badges_root_node_hash: Optional["DestinyPresentationNodeDefinition"] = custom_field(
        default=None
    )
    manifest_collections_root_node_hash: Optional["DestinyPresentationNodeDefinition"] = custom_field(default=None)
    manifest_crafting_root_node_hash: Optional["DestinyPresentationNodeDefinition"] = custom_field(default=None)
    manifest_exotic_catalysts_root_node_hash: Optional["DestinyPresentationNodeDefinition"] = custom_field(default=None)
    manifest_featured_items_list_hash: Optional["DestinyItemFilterDefinition"] = custom_field(default=None)
    manifest_guardian_ranks_root_node_hash: Optional["DestinyPresentationNodeDefinition"] = custom_field(default=None)
    manifest_legacy_seals_root_node_hash: Optional["DestinyPresentationNodeDefinition"] = custom_field(default=None)
    manifest_legacy_triumphs_root_node_hash: Optional["DestinyPresentationNodeDefinition"] = custom_field(default=None)
    manifest_lore_root_node_hash: Optional["DestinyPresentationNodeDefinition"] = custom_field(default=None)
    manifest_medals_root_node_hash: Optional["DestinyPresentationNodeDefinition"] = custom_field(default=None)
    manifest_metrics_root_node_hash: Optional["DestinyPresentationNodeDefinition"] = custom_field(default=None)
    manifest_seasonal_hub_event_card_hash: Optional["DestinyEventCardDefinition"] = custom_field(default=None)


@custom_define()
class DestinyPathfinderConstantsDefinition(BaseModel, HashObject):
    """
    _No description given by bungie._

    Tip: Manifest Information
        This model has some attributes which can be filled with additional information found in the manifest (`manifest_...`).
        Without additional work, these attributes will be `None`, since they require additional requests and database lookups.

        To fill the manifest dependent attributes, either:

        - Run `await ThisClass.fetch_manifest_information()`, see [here](/API Reference/Models/base)
        - Set `Client.always_return_manifest_information` to `True`, see [here](/API Reference/client)

    Attributes:
        all_pathfinder_root_node_hashes: Root presentation nodes for all currently valid Pathfinder boards
        hash: The unique identifier for this entity. Guaranteed to be unique for the type of entity, but not globally. When entities refer to each other in Destiny content, it is this hash that they are referring to.
        index: The index of the entity as it was found in the investment tables.
        pathfinder_topology: The topology of the Pathfinder board. The key is the index of the Record in the Pathfinder board, and the value is a list of the indices of Records that are connected to the Key Record. Using this topology, clients can ascertain if a Record can be unlocked, by checking if the objective of any connected Record has been completed and/or claimed.
        pathfinder_tree_tiers: The current shape of Pathfinder boards, where a Pathfinder board is stored as as flat list of Records. The key of this dictionary is the index at which a tier starts, and the value is the total number of objectives in the tier.
        redacted: If this is true, then there is an entity with this identifier/type combination, but BNet is not yet allowed to show it. Sorry!
        the_pale_heart_pathfinder_root_node_hash: Pathfinder root node for The Pale Heart
        manifest_the_pale_heart_pathfinder_root_node_hash: Manifest information for `the_pale_heart_pathfinder_root_node_hash`
    """

    all_pathfinder_root_node_hashes: list[int] = custom_field(metadata={"type": """list[int]"""})
    index: int = custom_field()
    pathfinder_topology: dict[int, list[int]] = custom_field(metadata={"type": """dict[int, list[int]]"""})
    pathfinder_tree_tiers: dict[int, int] = custom_field(metadata={"type": """dict[int, int]"""})
    redacted: bool = custom_field()
    the_pale_heart_pathfinder_root_node_hash: int = custom_field()
    manifest_the_pale_heart_pathfinder_root_node_hash: Optional["DestinyPresentationNodeDefinition"] = custom_field(
        default=None
    )


@custom_define()
class DestinyRewardPassRankSealImages(BaseModel):
    """
    _No description given by bungie._

    None
    Attributes:
        reward_pass_rank_seal_image_path: _No description given by bungie._
        reward_pass_rank_seal_premium_image_path: _No description given by bungie._
        reward_pass_rank_seal_premium_prestige_image_path: _No description given by bungie._
        reward_pass_rank_seal_prestige_image_path: _No description given by bungie._
    """

    reward_pass_rank_seal_image_path: str = custom_field()
    reward_pass_rank_seal_premium_image_path: str = custom_field()
    reward_pass_rank_seal_premium_prestige_image_path: str = custom_field()
    reward_pass_rank_seal_prestige_image_path: str = custom_field()


@custom_define()
class DestinySeasonalHubRankIconImages(BaseModel):
    """
    _No description given by bungie._

    None
    Attributes:
        seasonal_hub_rank_icon_active: _No description given by bungie._
        seasonal_hub_rank_icon_earning: _No description given by bungie._
        seasonal_hub_rank_icon_unearned: _No description given by bungie._
    """

    seasonal_hub_rank_icon_active: str = custom_field()
    seasonal_hub_rank_icon_earning: str = custom_field()
    seasonal_hub_rank_icon_unearned: str = custom_field()
