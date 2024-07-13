# DO NOT CHANGE ANY CODE BELOW
# This file is generated automatically by `generate_api_schema.py` and will be overwritten
# Instead, change functions / models by subclassing them in the `./overwrites/` folder. They will be used instead.


from bungio.models.base import BaseModel, custom_define, custom_field


@custom_define()
class ClanBannerDecal(BaseModel):
    """
    _No description given by bungie._

    None
    Attributes:
        background_path: _No description given by bungie._
        foreground_path: _No description given by bungie._
        identifier: _No description given by bungie._
    """

    background_path: str = custom_field()
    foreground_path: str = custom_field()
    identifier: str = custom_field()
