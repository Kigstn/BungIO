import datetime
from typing import TYPE_CHECKING, Any, Optional

import attr

from bungio.models.base import BaseEnum, BaseModel


@attr.define
class DestinyMetricsComponent(BaseModel):
    """
    Not specified.

    Attributes:
        metrics: Not specified.
        metrics_root_node_hash: Not specified.
    """

    metrics: Any = attr.field()
    metrics_root_node_hash: int = attr.field()


@attr.define
class DestinyMetricComponent(BaseModel):
    """
    Not specified.

    Attributes:
        invisible: Not specified.
        objective_progress: Not specified.
    """

    invisible: bool = attr.field()
    objective_progress: "DestinyObjectiveProgress" = attr.field()
