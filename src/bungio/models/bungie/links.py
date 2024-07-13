# DO NOT CHANGE ANY CODE BELOW
# This file is generated automatically by `generate_api_schema.py` and will be overwritten
# Instead, change functions / models by subclassing them in the `./overwrites/` folder. They will be used instead.


from bungio.models.base import BaseModel, custom_define, custom_field


@custom_define()
class HyperlinkReference(BaseModel):
    """
    _No description given by bungie._

    None
    Attributes:
        title: _No description given by bungie._
        url: _No description given by bungie._
    """

    title: str = custom_field()
    url: str = custom_field()
