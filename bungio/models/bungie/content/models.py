from typing import Any

import attr

from bungio.models.base import BaseEnum, BaseModel


@attr.define
class ContentTypeDescription(BaseModel):
    """
    _No description given by bungie_

    Attributes:
        c_type: _No description given by bungie_
        name: _No description given by bungie_
        content_description: _No description given by bungie_
        preview_image: _No description given by bungie_
        priority: _No description given by bungie_
        reminder: _No description given by bungie_
        properties: _No description given by bungie_
        tag_metadata: _No description given by bungie_
        tag_metadata_items: _No description given by bungie_
        usage_examples: _No description given by bungie_
        show_in_content_editor: _No description given by bungie_
        type_of: _No description given by bungie_
        bind_identifier_to_property: _No description given by bungie_
        bound_regex: _No description given by bungie_
        force_identifier_binding: _No description given by bungie_
        allow_comments: _No description given by bungie_
        auto_english_property_fallback: _No description given by bungie_
        bulk_uploadable: _No description given by bungie_
        previews: _No description given by bungie_
        suppress_cms_path: _No description given by bungie_
        property_sections: _No description given by bungie_
    """

    c_type: str = attr.field()
    name: str = attr.field()
    content_description: str = attr.field()
    preview_image: str = attr.field()
    priority: int = attr.field()
    reminder: str = attr.field()
    properties: list["ContentTypeProperty"] = attr.field()
    tag_metadata: list["TagMetadataDefinition"] = attr.field()
    tag_metadata_items: Any = attr.field()
    usage_examples: list[str] = attr.field()
    show_in_content_editor: bool = attr.field()
    type_of: str = attr.field()
    bind_identifier_to_property: str = attr.field()
    bound_regex: str = attr.field()
    force_identifier_binding: bool = attr.field()
    allow_comments: bool = attr.field()
    auto_english_property_fallback: bool = attr.field()
    bulk_uploadable: bool = attr.field()
    previews: list["ContentPreview"] = attr.field()
    suppress_cms_path: bool = attr.field()
    property_sections: list["ContentTypePropertySection"] = attr.field()


@attr.define
class ContentTypeProperty(BaseModel):
    """
    _No description given by bungie_

    Attributes:
        name: _No description given by bungie_
        root_property_name: _No description given by bungie_
        readable_name: _No description given by bungie_
        value: _No description given by bungie_
        property_description: _No description given by bungie_
        localizable: _No description given by bungie_
        fallback: _No description given by bungie_
        enabled: _No description given by bungie_
        order: _No description given by bungie_
        visible: _No description given by bungie_
        is_title: _No description given by bungie_
        required: _No description given by bungie_
        max_length: _No description given by bungie_
        max_byte_length: _No description given by bungie_
        max_file_size: _No description given by bungie_
        regexp: _No description given by bungie_
        validate_as: _No description given by bungie_
        rss_attribute: _No description given by bungie_
        visible_dependency: _No description given by bungie_
        visible_on: _No description given by bungie_
        datatype: _No description given by bungie_
        attributes: _No description given by bungie_
        child_properties: _No description given by bungie_
        content_type_allowed: _No description given by bungie_
        bind_to_property: _No description given by bungie_
        bound_regex: _No description given by bungie_
        representation_selection: _No description given by bungie_
        default_values: _No description given by bungie_
        is_external_allowed: _No description given by bungie_
        property_section: _No description given by bungie_
        weight: _No description given by bungie_
        entitytype: _No description given by bungie_
        is_combo: _No description given by bungie_
        suppress_property: _No description given by bungie_
        legal_content_types: _No description given by bungie_
        representation_validation_string: _No description given by bungie_
        min_width: _No description given by bungie_
        max_width: _No description given by bungie_
        min_height: _No description given by bungie_
        max_height: _No description given by bungie_
        is_video: _No description given by bungie_
        is_image: _No description given by bungie_
    """

    name: str = attr.field()
    root_property_name: str = attr.field()
    readable_name: str = attr.field()
    value: str = attr.field()
    property_description: str = attr.field()
    localizable: bool = attr.field()
    fallback: bool = attr.field()
    enabled: bool = attr.field()
    order: int = attr.field()
    visible: bool = attr.field()
    is_title: bool = attr.field()
    required: bool = attr.field()
    max_length: int = attr.field()
    max_byte_length: int = attr.field()
    max_file_size: int = attr.field()
    regexp: str = attr.field()
    validate_as: str = attr.field()
    rss_attribute: str = attr.field()
    visible_dependency: str = attr.field()
    visible_on: str = attr.field()
    datatype: "ContentPropertyDataTypeEnum" = attr.field()
    attributes: Any = attr.field()
    child_properties: list["ContentTypeProperty"] = attr.field()
    content_type_allowed: str = attr.field()
    bind_to_property: str = attr.field()
    bound_regex: str = attr.field()
    representation_selection: Any = attr.field()
    default_values: list["ContentTypeDefaultValue"] = attr.field()
    is_external_allowed: bool = attr.field()
    property_section: str = attr.field()
    weight: int = attr.field()
    entitytype: str = attr.field()
    is_combo: bool = attr.field()
    suppress_property: bool = attr.field()
    legal_content_types: list[str] = attr.field()
    representation_validation_string: str = attr.field()
    min_width: int = attr.field()
    max_width: int = attr.field()
    min_height: int = attr.field()
    max_height: int = attr.field()
    is_video: bool = attr.field()
    is_image: bool = attr.field()


class ContentPropertyDataTypeEnum(BaseEnum):
    """
    _No description given by bungie_
    """

    NONE = 0
    """_No description given by bungie_ """
    PLAINTEXT = 1
    """_No description given by bungie_ """
    HTML = 2
    """_No description given by bungie_ """
    DROPDOWN = 3
    """_No description given by bungie_ """
    LIST = 4
    """_No description given by bungie_ """
    JSON = 5
    """_No description given by bungie_ """
    CONTENT = 6
    """_No description given by bungie_ """
    REPRESENTATION = 7
    """_No description given by bungie_ """
    SET = 8
    """_No description given by bungie_ """
    FILE = 9
    """_No description given by bungie_ """
    FOLDER_SET = 10
    """_No description given by bungie_ """
    DATE = 11
    """_No description given by bungie_ """
    MULTILINE_PLAINTEXT = 12
    """_No description given by bungie_ """
    DESTINY_CONTENT = 13
    """_No description given by bungie_ """
    COLOR = 14
    """_No description given by bungie_ """


@attr.define
class ContentTypeDefaultValue(BaseModel):
    """
    _No description given by bungie_

    Attributes:
        when_clause: _No description given by bungie_
        when_value: _No description given by bungie_
        default_value: _No description given by bungie_
    """

    when_clause: str = attr.field()
    when_value: str = attr.field()
    default_value: str = attr.field()


@attr.define
class TagMetadataDefinition(BaseModel):
    """
    _No description given by bungie_

    Attributes:
        description: _No description given by bungie_
        order: _No description given by bungie_
        items: _No description given by bungie_
        datatype: _No description given by bungie_
        name: _No description given by bungie_
        is_required: _No description given by bungie_
    """

    description: str = attr.field()
    order: int = attr.field()
    items: list["TagMetadataItem"] = attr.field()
    datatype: str = attr.field()
    name: str = attr.field()
    is_required: bool = attr.field()


@attr.define
class TagMetadataItem(BaseModel):
    """
    _No description given by bungie_

    Attributes:
        description: _No description given by bungie_
        tag_text: _No description given by bungie_
        groups: _No description given by bungie_
        is_default: _No description given by bungie_
        name: _No description given by bungie_
    """

    description: str = attr.field()
    tag_text: str = attr.field()
    groups: list[str] = attr.field()
    is_default: bool = attr.field()
    name: str = attr.field()


@attr.define
class ContentPreview(BaseModel):
    """
    _No description given by bungie_

    Attributes:
        name: _No description given by bungie_
        path: _No description given by bungie_
        item_in_set: _No description given by bungie_
        set_tag: _No description given by bungie_
        set_nesting: _No description given by bungie_
        use_set_id: _No description given by bungie_
    """

    name: str = attr.field()
    path: str = attr.field()
    item_in_set: bool = attr.field()
    set_tag: str = attr.field()
    set_nesting: int = attr.field()
    use_set_id: int = attr.field()


@attr.define
class ContentTypePropertySection(BaseModel):
    """
    _No description given by bungie_

    Attributes:
        name: _No description given by bungie_
        readable_name: _No description given by bungie_
        collapsed: _No description given by bungie_
    """

    name: str = attr.field()
    readable_name: str = attr.field()
    collapsed: bool = attr.field()
