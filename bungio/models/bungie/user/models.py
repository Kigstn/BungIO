import attr

from bungio.models.base import BaseModel


@attr.define
class GetCredentialTypesForAccountResponse(BaseModel):
    """
    _No description given_

    Attributes:
        credential_type: _No description given_
        credential_display_name: _No description given_
        is_public: _No description given_
        credential_as_string: _No description given_
    """

    credential_type: int = attr.field()
    credential_display_name: str = attr.field()
    is_public: bool = attr.field()
    credential_as_string: str = attr.field()
