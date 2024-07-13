# DO NOT CHANGE ANY CODE BELOW
# This file is generated automatically by `generate_api_schema.py` and will be overwritten
# Instead, change functions / models by subclassing them in the `./overwrites/` folder. They will be used instead.

from typing import Union, TYPE_CHECKING

from bungio.utils import enum_converter
from bungio.models.base import BaseModel, custom_define, custom_field


if TYPE_CHECKING:
    from bungio.models import BungieCredentialType


@custom_define()
class GetCredentialTypesForAccountResponse(BaseModel):
    """
    _No description given by bungie._

    None
    Attributes:
        credential_as_string: _No description given by bungie._
        credential_display_name: _No description given by bungie._
        credential_type: _No description given by bungie._
        is_public: _No description given by bungie._
    """

    credential_as_string: str = custom_field()
    credential_display_name: str = custom_field()
    credential_type: Union["BungieCredentialType", int] = custom_field(converter=enum_converter("BungieCredentialType"))
    is_public: bool = custom_field()
