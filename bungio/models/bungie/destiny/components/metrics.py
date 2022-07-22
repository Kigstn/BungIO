# DO NOT CHANGE ANY CODE BELOW
# This file is generated automatically by `generate_api_schema.py` and will be overwritten
# Instead, change functions / models by subclassing them in the `./overwrites/` folder. They will be used instead.

from typing import TYPE_CHECKING, Optional

import attr

from bungio.models.base import BaseModel

if TYPE_CHECKING:
    from bungio.models import (
        DestinyObjectiveProgress,
        DestinyPresentationNodeDefinition,
    )


@attr.define
class DestinyMetricsComponent(BaseModel):
    """
    _No description given by bungie._

    Tip: Manifest Information
        This model has some attributes which can be filled with additional information found in the manifest (`manifest_...`).
        Without additional work, these attributes will be `None`, since they require additional requests and database lookups.

        To fill the manifest dependent attributes, either:

        - Run `await ThisClass.fetch_manifest_information()`, see [here](/API Reference/Models/base)
        - Set `Client.always_return_manifest_information` to `True`, see [here](/API Reference/client)

    Attributes:
        metrics: _No description given by bungie._
        metrics_root_node_hash: _No description given by bungie._
        manifest_metrics_root_node_hash: Manifest information for `metrics_root_node_hash`
    """

    metrics: dict[int, "DestinyMetricComponent"] = attr.field(
        metadata={"type": """dict[int, DestinyMetricComponent]"""}
    )
    metrics_root_node_hash: int = attr.field()
    manifest_metrics_root_node_hash: Optional["DestinyPresentationNodeDefinition"] = attr.field(default=None)


@attr.define
class DestinyMetricComponent(BaseModel):
    """
    _No description given by bungie._

    None
    Attributes:
        invisible: _No description given by bungie._
        objective_progress: _No description given by bungie._
    """

    invisible: bool = attr.field()
    objective_progress: "DestinyObjectiveProgress" = attr.field()
