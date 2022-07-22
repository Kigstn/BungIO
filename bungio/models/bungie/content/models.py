# DO NOT CHANGE ANY CODE BELOW
# This file is generated automatically by `generate_api_schema.py` and will be overwritten
# Instead, change functions / models by subclassing them in the `./overwrites/` folder. They will be used instead.

from typing import Union

import attr

from bungio.models.base import BaseEnum, BaseModel
from bungio.utils import enum_converter


@attr.define
class ContentTypeDescription(BaseModel):
    """
    _No description given by bungie._

    None
    Attributes:
        allow_comments: _No description given by bungie._
        auto_english_property_fallback: _No description given by bungie._
        bind_identifier_to_property: _No description given by bungie._
        bound_regex: _No description given by bungie._
        bulk_uploadable: _No description given by bungie._
        c_type: _No description given by bungie._
        content_description: _No description given by bungie._
        force_identifier_binding: _No description given by bungie._
        name: _No description given by bungie._
        preview_image: _No description given by bungie._
        previews: _No description given by bungie._
        priority: _No description given by bungie._
        properties: _No description given by bungie._
        property_sections: _No description given by bungie._
        reminder: _No description given by bungie._
        show_in_content_editor: _No description given by bungie._
        suppress_cms_path: _No description given by bungie._
        tag_metadata: _No description given by bungie._
        tag_metadata_items: _No description given by bungie._
        type_of: _No description given by bungie._
        usage_examples: _No description given by bungie._
    """

    allow_comments: bool = attr.field()
    auto_english_property_fallback: bool = attr.field()
    bind_identifier_to_property: str = attr.field()
    bound_regex: str = attr.field()
    bulk_uploadable: bool = attr.field()
    c_type: str = attr.field()
    content_description: str = attr.field()
    force_identifier_binding: bool = attr.field()
    name: str = attr.field()
    preview_image: str = attr.field()
    previews: list["ContentPreview"] = attr.field(metadata={"type": """list[ContentPreview]"""})
    priority: int = attr.field()
    properties: list["ContentTypeProperty"] = attr.field(metadata={"type": """list[ContentTypeProperty]"""})
    property_sections: list["ContentTypePropertySection"] = attr.field(
        metadata={"type": """list[ContentTypePropertySection]"""}
    )
    reminder: str = attr.field()
    show_in_content_editor: bool = attr.field()
    suppress_cms_path: bool = attr.field()
    tag_metadata: list["TagMetadataDefinition"] = attr.field(metadata={"type": """list[TagMetadataDefinition]"""})
    tag_metadata_items: dict[str, "TagMetadataItem"] = attr.field(metadata={"type": """dict[str, TagMetadataItem]"""})
    type_of: str = attr.field()
    usage_examples: list[str] = attr.field(metadata={"type": """list[str]"""})


@attr.define
class ContentTypeProperty(BaseModel):
    """
    _No description given by bungie._

    None
    Attributes:
        attributes: _No description given by bungie._
        bind_to_property: _No description given by bungie._
        bound_regex: _No description given by bungie._
        child_properties: _No description given by bungie._
        content_type_allowed: _No description given by bungie._
        datatype: _No description given by bungie._
        default_values: _No description given by bungie._
        enabled: _No description given by bungie._
        entitytype: _No description given by bungie._
        fallback: _No description given by bungie._
        is_combo: _No description given by bungie._
        is_external_allowed: _No description given by bungie._
        is_image: _No description given by bungie._
        is_title: _No description given by bungie._
        is_video: _No description given by bungie._
        legal_content_types: _No description given by bungie._
        localizable: _No description given by bungie._
        max_byte_length: _No description given by bungie._
        max_file_size: _No description given by bungie._
        max_height: _No description given by bungie._
        max_length: _No description given by bungie._
        max_width: _No description given by bungie._
        min_height: _No description given by bungie._
        min_width: _No description given by bungie._
        name: _No description given by bungie._
        order: _No description given by bungie._
        property_description: _No description given by bungie._
        property_section: _No description given by bungie._
        readable_name: _No description given by bungie._
        regexp: _No description given by bungie._
        representation_selection: _No description given by bungie._
        representation_validation_string: _No description given by bungie._
        required: _No description given by bungie._
        root_property_name: _No description given by bungie._
        rss_attribute: _No description given by bungie._
        suppress_property: _No description given by bungie._
        validate_as: _No description given by bungie._
        value: _No description given by bungie._
        visible: _No description given by bungie._
        visible_dependency: _No description given by bungie._
        visible_on: _No description given by bungie._
        weight: _No description given by bungie._
    """

    attributes: dict[str, str] = attr.field(metadata={"type": """dict[str, str]"""})
    bind_to_property: str = attr.field()
    bound_regex: str = attr.field()
    child_properties: list["ContentTypeProperty"] = attr.field(metadata={"type": """list[ContentTypeProperty]"""})
    content_type_allowed: str = attr.field()
    datatype: Union["ContentPropertyDataTypeEnum", int] = attr.field(
        converter=enum_converter("ContentPropertyDataTypeEnum")
    )
    default_values: list["ContentTypeDefaultValue"] = attr.field(metadata={"type": """list[ContentTypeDefaultValue]"""})
    enabled: bool = attr.field()
    entitytype: str = attr.field()
    fallback: bool = attr.field()
    is_combo: bool = attr.field()
    is_external_allowed: bool = attr.field()
    is_image: bool = attr.field()
    is_title: bool = attr.field()
    is_video: bool = attr.field()
    legal_content_types: list[str] = attr.field(metadata={"type": """list[str]"""})
    localizable: bool = attr.field()
    max_byte_length: int = attr.field()
    max_file_size: int = attr.field()
    max_height: int = attr.field()
    max_length: int = attr.field()
    max_width: int = attr.field()
    min_height: int = attr.field()
    min_width: int = attr.field()
    name: str = attr.field()
    order: int = attr.field()
    property_description: str = attr.field()
    property_section: str = attr.field()
    readable_name: str = attr.field()
    regexp: str = attr.field()
    representation_selection: dict[str, str] = attr.field(metadata={"type": """dict[str, str]"""})
    representation_validation_string: str = attr.field()
    required: bool = attr.field()
    root_property_name: str = attr.field()
    rss_attribute: str = attr.field()
    suppress_property: bool = attr.field()
    validate_as: str = attr.field()
    value: str = attr.field()
    visible: bool = attr.field()
    visible_dependency: str = attr.field()
    visible_on: str = attr.field()
    weight: int = attr.field()


class ContentPropertyDataTypeEnum(BaseEnum):
    """
    _No description given by bungie._
    """

    NONE = 0
    """_No description given by bungie._ """
    PLAINTEXT = 1
    """_No description given by bungie._ """
    HTML = 2
    """_No description given by bungie._ """
    DROPDOWN = 3
    """_No description given by bungie._ """
    LIST = 4
    """_No description given by bungie._ """
    JSON = 5
    """_No description given by bungie._ """
    CONTENT = 6
    """_No description given by bungie._ """
    REPRESENTATION = 7
    """_No description given by bungie._ """
    SET = 8
    """_No description given by bungie._ """
    FILE = 9
    """_No description given by bungie._ """
    FOLDER_SET = 10
    """_No description given by bungie._ """
    DATE = 11
    """_No description given by bungie._ """
    MULTILINE_PLAINTEXT = 12
    """_No description given by bungie._ """
    DESTINY_CONTENT = 13
    """_No description given by bungie._ """
    COLOR = 14
    """_No description given by bungie._ """


@attr.define
class ContentTypeDefaultValue(BaseModel):
    """
    _No description given by bungie._

    None
    Attributes:
        default_value: _No description given by bungie._
        when_clause: _No description given by bungie._
        when_value: _No description given by bungie._
    """

    default_value: str = attr.field()
    when_clause: str = attr.field()
    when_value: str = attr.field()


@attr.define
class TagMetadataDefinition(BaseModel):
    """
    _No description given by bungie._

    None
    Attributes:
        datatype: _No description given by bungie._
        description: _No description given by bungie._
        is_required: _No description given by bungie._
        items: _No description given by bungie._
        name: _No description given by bungie._
        order: _No description given by bungie._
    """

    datatype: str = attr.field()
    description: str = attr.field()
    is_required: bool = attr.field()
    items: list["TagMetadataItem"] = attr.field(metadata={"type": """list[TagMetadataItem]"""})
    name: str = attr.field()
    order: int = attr.field()


@attr.define
class TagMetadataItem(BaseModel):
    """
    _No description given by bungie._

    None
    Attributes:
        description: _No description given by bungie._
        groups: _No description given by bungie._
        is_default: _No description given by bungie._
        name: _No description given by bungie._
        tag_text: _No description given by bungie._
    """

    description: str = attr.field()
    groups: list[str] = attr.field(metadata={"type": """list[str]"""})
    is_default: bool = attr.field()
    name: str = attr.field()
    tag_text: str = attr.field()


@attr.define
class ContentPreview(BaseModel):
    """
    _No description given by bungie._

    None
    Attributes:
        item_in_set: _No description given by bungie._
        name: _No description given by bungie._
        path: _No description given by bungie._
        set_nesting: _No description given by bungie._
        set_tag: _No description given by bungie._
        use_set_id: _No description given by bungie._
    """

    item_in_set: bool = attr.field()
    name: str = attr.field()
    path: str = attr.field()
    set_nesting: int = attr.field()
    set_tag: str = attr.field()
    use_set_id: int = attr.field()


@attr.define
class ContentTypePropertySection(BaseModel):
    """
    _No description given by bungie._

    None
    Attributes:
        collapsed: _No description given by bungie._
        name: _No description given by bungie._
        readable_name: _No description given by bungie._
    """

    collapsed: bool = attr.field()
    name: str = attr.field()
    readable_name: str = attr.field()
