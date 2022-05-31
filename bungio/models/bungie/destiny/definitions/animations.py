import attr

from bungio.models.base import BaseModel


@attr.define
class DestinyAnimationReference(BaseModel):
    """
    _No description given by bungie_

    Attributes:
        anim_name: _No description given by bungie_
        anim_identifier: _No description given by bungie_
        path: _No description given by bungie_
    """

    anim_name: str = attr.field()
    anim_identifier: str = attr.field()
    path: str = attr.field()
