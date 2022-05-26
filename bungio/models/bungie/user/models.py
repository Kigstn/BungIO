import datetime
from typing import TYPE_CHECKING, Any, Optional

import attr

from bungio.models.base import BaseEnum, BaseModel


@attr.define
class GetCredentialTypesForAccountResponse(BaseModel):
    """
    Not specified.

    Attributes:
        credential_type: Not specified.
        credential_display_name: Not specified.
        is_public: Not specified.
        credential_as_string: Not specified.
    """

    credential_type: int = attr.field()
    credential_display_name: str = attr.field()
    is_public: bool = attr.field()
    credential_as_string: str = attr.field()
