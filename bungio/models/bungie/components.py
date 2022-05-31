import attr

from bungio.models.base import BaseEnum, BaseModel


@attr.define
class ComponentResponse(BaseModel):
    """
    The base class for any component-returning object that may need to indicate information about the state of the component being returned.

    Attributes:
        privacy: _No description given by bungie_
        disabled: If true, this component is disabled.
    """

    privacy: int = attr.field()
    disabled: bool = attr.field()


class ComponentPrivacySetting(BaseEnum):
    """
    A set of flags for reason(s) why the component populated in the way that it did. Inspect the individual flags for the reasons.
    """

    NONE = 0
    """_No description given by bungie_ """
    PUBLIC = 1
    """_No description given by bungie_ """
    PRIVATE = 2
    """_No description given by bungie_ """
