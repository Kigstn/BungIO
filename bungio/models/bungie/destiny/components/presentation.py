from typing import TYPE_CHECKING

import attr

from bungio.models.base import BaseModel

if TYPE_CHECKING:
    from bungio.models import (
        DestinyObjectiveProgress,
        DestinyPresentationNodeDefinition,
        DestinyPresentationNodeState,
    )


@attr.define
class DestinyPresentationNodesComponent(BaseModel):
    """
    _No description given by bungie_

    Attributes:
        nodes: _No description given by bungie_
    """

    nodes: "DestinyPresentationNodeDefinition" = attr.field()


@attr.define
class DestinyPresentationNodeComponent(BaseModel):
    """
    _No description given by bungie_

    Attributes:
        state: _No description given by bungie_
        objective: An optional property: presentation nodes MAY have objectives, which can be used to infer more human readable data about the progress. However, progressValue and completionValue ought to be considered the canonical values for progress on Progression Nodes.
        progress_value: How much of the presentation node is considered to be completed so far by the given character/profile.
        completion_value: The value at which the presentation node is considered to be completed.
        record_category_score: If available, this is the current score for the record category that this node represents.
    """

    state: "DestinyPresentationNodeState" = attr.field()
    objective: "DestinyObjectiveProgress" = attr.field()
    progress_value: int = attr.field()
    completion_value: int = attr.field()
    record_category_score: int = attr.field()
