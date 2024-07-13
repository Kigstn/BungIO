# DO NOT CHANGE ANY CODE BELOW
# This file is generated automatically by `generate_api_schema.py` and will be overwritten
# Instead, change functions / models by subclassing them in the `./overwrites/` folder. They will be used instead.


from bungio.models.base import BaseModel, custom_define, custom_field


@custom_define()
class DestinySocialCommendationsComponent(BaseModel):
    """
    _No description given by bungie._

    None
    Attributes:
        commendation_node_percentages_by_hash: The percentage for each commendation type out of total received
        commendation_node_scores_by_hash: _No description given by bungie._
        commendation_scores_by_hash: _No description given by bungie._
        score_detail_values: _No description given by bungie._
        total_score: _No description given by bungie._
    """

    commendation_node_percentages_by_hash: dict[int, int] = custom_field(metadata={"type": """dict[int, int]"""})
    commendation_node_scores_by_hash: dict[int, int] = custom_field(metadata={"type": """dict[int, int]"""})
    commendation_scores_by_hash: dict[int, int] = custom_field(metadata={"type": """dict[int, int]"""})
    score_detail_values: list[int] = custom_field(metadata={"type": """list[int]"""})
    total_score: int = custom_field()
