import datetime
from typing import TYPE_CHECKING, Any, Optional

import attr

from bungio.models.base import BaseEnum, BaseModel


@attr.define
class ContentTypeDescription(BaseModel):
    """
    Not specified.

    Attributes:
        c_type: Not specified.
        name: Not specified.
        content_description: Not specified.
        preview_image: Not specified.
        priority: Not specified.
        reminder: Not specified.
        properties: Not specified.
        tag_metadata: Not specified.
        tag_metadata_items: Not specified.
        usage_examples: Not specified.
        show_in_content_editor: Not specified.
        type_of: Not specified.
        bind_identifier_to_property: Not specified.
        bound_regex: Not specified.
        force_identifier_binding: Not specified.
        allow_comments: Not specified.
        auto_english_property_fallback: Not specified.
        bulk_uploadable: Not specified.
        previews: Not specified.
        suppress_cms_path: Not specified.
        property_sections: Not specified.
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
    Not specified.

    Attributes:
        name: Not specified.
        root_property_name: Not specified.
        readable_name: Not specified.
        value: Not specified.
        property_description: Not specified.
        localizable: Not specified.
        fallback: Not specified.
        enabled: Not specified.
        order: Not specified.
        visible: Not specified.
        is_title: Not specified.
        required: Not specified.
        max_length: Not specified.
        max_byte_length: Not specified.
        max_file_size: Not specified.
        regexp: Not specified.
        validate_as: Not specified.
        rss_attribute: Not specified.
        visible_dependency: Not specified.
        visible_on: Not specified.
        datatype: Not specified.
        attributes: Not specified.
        child_properties: Not specified.
        content_type_allowed: Not specified.
        bind_to_property: Not specified.
        bound_regex: Not specified.
        representation_selection: Not specified.
        default_values: Not specified.
        is_external_allowed: Not specified.
        property_section: Not specified.
        weight: Not specified.
        entitytype: Not specified.
        is_combo: Not specified.
        suppress_property: Not specified.
        legal_content_types: Not specified.
        representation_validation_string: Not specified.
        min_width: Not specified.
        max_width: Not specified.
        min_height: Not specified.
        max_height: Not specified.
        is_video: Not specified.
        is_image: Not specified.
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
    datatype: int = attr.field()
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
    Not specified.
    """

    NONE = 0
    """Not specified. """
    PLAINTEXT = 1
    """Not specified. """
    HTML = 2
    """Not specified. """
    DROPDOWN = 3
    """Not specified. """
    LIST = 4
    """Not specified. """
    JSON = 5
    """Not specified. """
    CONTENT = 6
    """Not specified. """
    REPRESENTATION = 7
    """Not specified. """
    SET = 8
    """Not specified. """
    FILE = 9
    """Not specified. """
    FOLDER_SET = 10
    """Not specified. """
    DATE = 11
    """Not specified. """
    MULTILINE_PLAINTEXT = 12
    """Not specified. """
    DESTINY_CONTENT = 13
    """Not specified. """
    COLOR = 14
    """Not specified. """


@attr.define
class ContentTypeDefaultValue(BaseModel):
    """
    Not specified.

    Attributes:
        when_clause: Not specified.
        when_value: Not specified.
        default_value: Not specified.
    """

    when_clause: str = attr.field()
    when_value: str = attr.field()
    default_value: str = attr.field()


@attr.define
class TagMetadataDefinition(BaseModel):
    """
    Not specified.

    Attributes:
        description: Not specified.
        order: Not specified.
        items: Not specified.
        datatype: Not specified.
        name: Not specified.
        is_required: Not specified.
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
    Not specified.

    Attributes:
        description: Not specified.
        tag_text: Not specified.
        groups: Not specified.
        is_default: Not specified.
        name: Not specified.
    """

    description: str = attr.field()
    tag_text: str = attr.field()
    groups: list[str] = attr.field()
    is_default: bool = attr.field()
    name: str = attr.field()


@attr.define
class ContentPreview(BaseModel):
    """
    Not specified.

    Attributes:
        name: Not specified.
        path: Not specified.
        item_in_set: Not specified.
        set_tag: Not specified.
        set_nesting: Not specified.
        use_set_id: Not specified.
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
    Not specified.

    Attributes:
        name: Not specified.
        readable_name: Not specified.
        collapsed: Not specified.
    """

    name: str = attr.field()
    readable_name: str = attr.field()
    collapsed: bool = attr.field()
