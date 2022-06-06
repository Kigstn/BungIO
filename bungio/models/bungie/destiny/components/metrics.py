from typing import TYPE_CHECKING, Any

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
    _No description given by bungie_

    Attributes:
        metrics: _No description given by bungie_
        metrics_root_node_hash: _No description given by bungie_
    """

    metrics: Any = attr.field()
    metrics_root_node_hash: "DestinyPresentationNodeDefinition" = attr.field()


@attr.define
class DestinyMetricComponent(BaseModel):
    """
    _No description given by bungie_

    Attributes:
        invisible: _No description given by bungie_
        objective_progress: _No description given by bungie_
    """

    invisible: bool = attr.field()
    objective_progress: "DestinyObjectiveProgress" = attr.field()
