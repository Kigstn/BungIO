# DO NOT CHANGE ANY CODE BELOW
# This file is generated automatically by `generate_api_schema.py` and will be overwritten
# Instead, change functions / models by subclassing them in the `./overwrites/` folder. They will be used instead.

from typing import Union

from bungio.utils import enum_converter
from bungio.models.base import BaseModel, BaseEnum, custom_define, custom_field


@custom_define()
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

    allow_comments: bool = custom_field()
    auto_english_property_fallback: bool = custom_field()
    bind_identifier_to_property: str = custom_field()
    bound_regex: str = custom_field()
    bulk_uploadable: bool = custom_field()
    c_type: str = custom_field()
    content_description: str = custom_field()
    force_identifier_binding: bool = custom_field()
    name: str = custom_field()
    preview_image: str = custom_field()
    previews: list["ContentPreview"] = custom_field(metadata={"type": """list[ContentPreview]"""})
    priority: int = custom_field()
    properties: list["ContentTypeProperty"] = custom_field(metadata={"type": """list[ContentTypeProperty]"""})
    property_sections: list["ContentTypePropertySection"] = custom_field(
        metadata={"type": """list[ContentTypePropertySection]"""}
    )
    reminder: str = custom_field()
    show_in_content_editor: bool = custom_field()
    suppress_cms_path: bool = custom_field()
    tag_metadata: list["TagMetadataDefinition"] = custom_field(metadata={"type": """list[TagMetadataDefinition]"""})
    tag_metadata_items: dict[str, "TagMetadataItem"] = custom_field(metadata={"type": """dict[str, TagMetadataItem]"""})
    type_of: str = custom_field()
    usage_examples: list[str] = custom_field(metadata={"type": """list[str]"""})


@custom_define()
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

    attributes: dict[str, str] = custom_field(metadata={"type": """dict[str, str]"""})
    bind_to_property: str = custom_field()
    bound_regex: str = custom_field()
    child_properties: list["ContentTypeProperty"] = custom_field(metadata={"type": """list[ContentTypeProperty]"""})
    content_type_allowed: str = custom_field()
    datatype: Union["ContentPropertyDataTypeEnum", int] = custom_field(
        converter=enum_converter("ContentPropertyDataTypeEnum")
    )
    default_values: list["ContentTypeDefaultValue"] = custom_field(
        metadata={"type": """list[ContentTypeDefaultValue]"""}
    )
    enabled: bool = custom_field()
    entitytype: str = custom_field()
    fallback: bool = custom_field()
    is_combo: bool = custom_field()
    is_external_allowed: bool = custom_field()
    is_image: bool = custom_field()
    is_title: bool = custom_field()
    is_video: bool = custom_field()
    legal_content_types: list[str] = custom_field(metadata={"type": """list[str]"""})
    localizable: bool = custom_field()
    max_byte_length: int = custom_field()
    max_file_size: int = custom_field()
    max_height: int = custom_field()
    max_length: int = custom_field()
    max_width: int = custom_field()
    min_height: int = custom_field()
    min_width: int = custom_field()
    name: str = custom_field()
    order: int = custom_field()
    property_description: str = custom_field()
    property_section: str = custom_field()
    readable_name: str = custom_field()
    regexp: str = custom_field()
    representation_selection: dict[str, str] = custom_field(metadata={"type": """dict[str, str]"""})
    representation_validation_string: str = custom_field()
    required: bool = custom_field()
    root_property_name: str = custom_field()
    rss_attribute: str = custom_field()
    suppress_property: bool = custom_field()
    validate_as: str = custom_field()
    value: str = custom_field()
    visible: bool = custom_field()
    visible_dependency: str = custom_field()
    visible_on: str = custom_field()
    weight: int = custom_field()


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


@custom_define()
class ContentTypeDefaultValue(BaseModel):
    """
    _No description given by bungie._

    None
    Attributes:
        default_value: _No description given by bungie._
        when_clause: _No description given by bungie._
        when_value: _No description given by bungie._
    """

    default_value: str = custom_field()
    when_clause: str = custom_field()
    when_value: str = custom_field()


@custom_define()
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

    datatype: str = custom_field()
    description: str = custom_field()
    is_required: bool = custom_field()
    items: list["TagMetadataItem"] = custom_field(metadata={"type": """list[TagMetadataItem]"""})
    name: str = custom_field()
    order: int = custom_field()


@custom_define()
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

    description: str = custom_field()
    groups: list[str] = custom_field(metadata={"type": """list[str]"""})
    is_default: bool = custom_field()
    name: str = custom_field()
    tag_text: str = custom_field()


@custom_define()
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

    item_in_set: bool = custom_field()
    name: str = custom_field()
    path: str = custom_field()
    set_nesting: int = custom_field()
    set_tag: str = custom_field()
    use_set_id: int = custom_field()


@custom_define()
class ContentTypePropertySection(BaseModel):
    """
    _No description given by bungie._

    None
    Attributes:
        collapsed: _No description given by bungie._
        name: _No description given by bungie._
        readable_name: _No description given by bungie._
    """

    collapsed: bool = custom_field()
    name: str = custom_field()
    readable_name: str = custom_field()
