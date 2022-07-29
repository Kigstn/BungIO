# DO NOT CHANGE ANY CODE BELOW
# This file is generated automatically by `generate_api_schema.py` and will be overwritten
# Instead, change functions / models by subclassing them in the `./overwrites/` folder. They will be used instead.


from bungio.models.base import BaseModel, custom_define, custom_field


@custom_define()
class InterpolationPoint(BaseModel):
    """
    _No description given by bungie._

    None
    Attributes:
        value: _No description given by bungie._
        weight: _No description given by bungie._
    """

    value: int = custom_field()
    weight: int = custom_field()


@custom_define()
class InterpolationPointFloat(BaseModel):
    """
    _No description given by bungie._

    None
    Attributes:
        value: _No description given by bungie._
        weight: _No description given by bungie._
    """

    value: float = custom_field()
    weight: float = custom_field()
