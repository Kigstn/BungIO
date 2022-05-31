import attr

from bungio.models.base import BaseModel


@attr.define
class ClanBannerDecal(BaseModel):
    """
    _No description given by bungie_

    Attributes:
        identifier: _No description given by bungie_
        foreground_path: _No description given by bungie_
        background_path: _No description given by bungie_
    """

    identifier: str = attr.field()
    foreground_path: str = attr.field()
    background_path: str = attr.field()
