# DO NOT CHANGE ANY CODE BELOW
# This file is generated automatically by `generate_api_schema.py` and will be overwritten
# Instead, change functions / models by subclassing them in the `./overwrites/` folder. They will be used instead.

from typing import TYPE_CHECKING, Union

import attr

from bungio.models.base import BaseModel
from bungio.utils import enum_converter

if TYPE_CHECKING:
    from bungio.models import DestinyObjectiveProgress, DestinyPresentationNodeState


@attr.define
class DestinyPresentationNodesComponent(BaseModel):
    """
    _No description given by bungie._

    None
    Attributes:
        nodes: _No description given by bungie._
    """

    nodes: dict[int, "DestinyPresentationNodeComponent"] = attr.field(
        metadata={"type": """dict[int, DestinyPresentationNodeComponent]"""}
    )


@attr.define
class DestinyPresentationNodeComponent(BaseModel):
    """
    _No description given by bungie._

    None
    Attributes:
        completion_value: The value at which the presentation node is considered to be completed.
        objective: An optional property: presentation nodes MAY have objectives, which can be used to infer more human readable data about the progress. However, progressValue and completionValue ought to be considered the canonical values for progress on Progression Nodes.
        progress_value: How much of the presentation node is considered to be completed so far by the given character/profile.
        record_category_score: If available, this is the current score for the record category that this node represents.
        state: _No description given by bungie._
    """

    completion_value: int = attr.field()
    objective: "DestinyObjectiveProgress" = attr.field()
    progress_value: int = attr.field()
    record_category_score: int = attr.field()
    state: Union["DestinyPresentationNodeState", int] = attr.field(
        converter=enum_converter("DestinyPresentationNodeState")
    )
