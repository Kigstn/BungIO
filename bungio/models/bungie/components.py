# DO NOT CHANGE ANY CODE BELOW
# This file is generated automatically by `generate_api_schema.py` and will be overwritten
# Instead, change functions / models by subclassing them in the `./overwrites/` folder. They will be used instead.

from typing import Union

import attr

from bungio.models.base import BaseEnum, BaseModel
from bungio.utils import enum_converter


@attr.define
class ComponentResponse(BaseModel):
    """
    The base class for any component-returning object that may need to indicate information about the state of the component being returned.

    None
    Attributes:
        disabled: If true, this component is disabled.
        privacy: _No description given by bungie._
    """

    disabled: bool = attr.field()
    privacy: Union["ComponentPrivacySetting", int] = attr.field(converter=enum_converter("ComponentPrivacySetting"))


class ComponentPrivacySetting(BaseEnum):
    """
    A set of flags for reason(s) why the component populated in the way that it did. Inspect the individual flags for the reasons.
    """

    NONE = 0
    """_No description given by bungie._ """
    PUBLIC = 1
    """_No description given by bungie._ """
    PRIVATE = 2
    """_No description given by bungie._ """
