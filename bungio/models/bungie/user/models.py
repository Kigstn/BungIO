# DO NOT CHANGE ANY CODE BELOW
# This file is generated automatically by `generate_api_schema.py` and will be overwritten
# Instead, change functions / models by subclassing them in the `./overwrites/` folder. They will be used instead.

from typing import TYPE_CHECKING

import attr

from bungio.models.base import BaseModel

if TYPE_CHECKING:
    from bungio.models import BungieCredentialType


@attr.define
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

    credential_as_string: str = attr.field()
    credential_display_name: str = attr.field()
    credential_type: "BungieCredentialType" = attr.field()
    is_public: bool = attr.field()
