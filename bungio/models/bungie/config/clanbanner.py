import attr

from bungio.models.base import BaseModel


@attr.define
class ClanBannerDecal(BaseModel):
    """
    _No description given_

    Attributes:
        identifier: _No description given_
        foreground_path: _No description given_
        background_path: _No description given_
    """

    identifier: str = attr.field()
    foreground_path: str = attr.field()
    background_path: str = attr.field()
