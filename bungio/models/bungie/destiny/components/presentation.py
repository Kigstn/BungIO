from typing import TYPE_CHECKING, Any

import attr

from bungio.models.base import BaseModel

if TYPE_CHECKING:
    from bungio.models import DestinyObjectiveProgress


@attr.define
class DestinyPresentationNodesComponent(BaseModel):
    """
    _No description given_

    Attributes:
        nodes: _No description given_
    """

    nodes: Any = attr.field()


@attr.define
class DestinyPresentationNodeComponent(BaseModel):
    """
    _No description given_

    Attributes:
        state: _No description given_
        objective: An optional property: presentation nodes MAY have objectives, which can be used to infer more human readable data about the progress. However, progressValue and completionValue ought to be considered the canonical values for progress on Progression Nodes.
        progress_value: How much of the presentation node is considered to be completed so far by the given character/profile.
        completion_value: The value at which the presentation node is considered to be completed.
        record_category_score: If available, this is the current score for the record category that this node represents.
    """

    state: int = attr.field()
    objective: "DestinyObjectiveProgress" = attr.field()
    progress_value: int = attr.field()
    completion_value: int = attr.field()
    record_category_score: int = attr.field()
