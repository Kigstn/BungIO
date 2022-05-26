import datetime
from typing import TYPE_CHECKING, Any, Optional

import attr

from bungio.models.base import BaseEnum, BaseModel


@attr.define
class ComponentResponse(BaseModel):
    """
    The base class for any component-returning object that may need to indicate information about the state of the component being returned.

    Attributes:
        privacy: Not specified.
        disabled: If true, this component is disabled.
    """

    privacy: int = attr.field()
    disabled: bool = attr.field()


class ComponentPrivacySetting(BaseEnum):
    """
    A set of flags for reason(s) why the component populated in the way that it did. Inspect the individual flags for the reasons.
    """

    NONE = 0
    """Not specified. """
    PUBLIC = 1
    """Not specified. """
    PRIVATE = 2
    """Not specified. """
