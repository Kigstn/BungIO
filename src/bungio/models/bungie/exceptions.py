# DO NOT CHANGE ANY CODE BELOW
# This file is generated automatically by `generate_api_schema.py` and will be overwritten
# Instead, change functions / models by subclassing them in the `./overwrites/` folder. They will be used instead.


from bungio.models.base import BaseEnum


class PlatformErrorCodes(BaseEnum):
    """
    _No description given by bungie._
    """

    NONE = 0
    """_No description given by bungie._ """
    SUCCESS = 1
    """_No description given by bungie._ """
    TRANSPORT_EXCEPTION = 2
    """_No description given by bungie._ """
    UNHANDLED_EXCEPTION = 3
    """_No description given by bungie._ """
    NOT_IMPLEMENTED = 4
    """_No description given by bungie._ """
    SYSTEM_DISABLED = 5
    """_No description given by bungie._ """
    FAILED_TO_LOAD_AVAILABLE_LOCALES_CONFIGURATION = 6
    """_No description given by bungie._ """
    PARAMETER_PARSE_FAILURE = 7
    """_No description given by bungie._ """
    PARAMETER_INVALID_RANGE = 8
    """_No description given by bungie._ """
    BAD_REQUEST = 9
    """_No description given by bungie._ """
    AUTHENTICATION_INVALID = 10
    """_No description given by bungie._ """
    DATA_NOT_FOUND = 11
    """_No description given by bungie._ """
    INSUFFICIENT_PRIVILEGES = 12
    """_No description given by bungie._ """
    DUPLICATE = 13
    """_No description given by bungie._ """
    UNKNOWN_SQL_RESULT = 14
    """_No description given by bungie._ """
    VALIDATION_ERROR = 15
    """_No description given by bungie._ """
    VALIDATION_MISSING_FIELD_ERROR = 16
    """_No description given by bungie._ """
    VALIDATION_INVALID_INPUT_ERROR = 17
    """_No description given by bungie._ """
    INVALID_PARAMETERS = 18
    """_No description given by bungie._ """
    PARAMETER_NOT_FOUND = 19
    """_No description given by bungie._ """
    UNHANDLED_HTTP_EXCEPTION = 20
    """_No description given by bungie._ """
    NOT_FOUND = 21
    """_No description given by bungie._ """
    WEB_AUTH_MODULE_ASYNC_FAILED = 22
    """_No description given by bungie._ """
    INVALID_RETURN_VALUE = 23
    """_No description given by bungie._ """
    USER_BANNED = 24
    """_No description given by bungie._ """
    INVALID_POST_BODY = 25
    """_No description given by bungie._ """
    MISSING_POST_BODY = 26
    """_No description given by bungie._ """
    EXTERNAL_SERVICE_TIMEOUT = 27
    """_No description given by bungie._ """
    VALIDATION_LENGTH_ERROR = 28
    """_No description given by bungie._ """
    VALIDATION_RANGE_ERROR = 29
    """_No description given by bungie._ """
    JSON_DESERIALIZATION_ERROR = 30
    """_No description given by bungie._ """
    THROTTLE_LIMIT_EXCEEDED = 31
    """_No description given by bungie._ """
    VALIDATION_TAG_ERROR = 32
    """_No description given by bungie._ """
    VALIDATION_PROFANITY_ERROR = 33
    """_No description given by bungie._ """
    VALIDATION_URL_FORMAT_ERROR = 34
    """_No description given by bungie._ """
    THROTTLE_LIMIT_EXCEEDED_MINUTES = 35
    """_No description given by bungie._ """
    THROTTLE_LIMIT_EXCEEDED_MOMENTARILY = 36
    """_No description given by bungie._ """
    THROTTLE_LIMIT_EXCEEDED_SECONDS = 37
    """_No description given by bungie._ """
    EXTERNAL_SERVICE_UNKNOWN = 38
    """_No description given by bungie._ """
    VALIDATION_WORD_LENGTH_ERROR = 39
    """_No description given by bungie._ """
    VALIDATION_INVISIBLE_UNICODE = 40
    """_No description given by bungie._ """
    VALIDATION_BAD_NAMES = 41
    """_No description given by bungie._ """
    EXTERNAL_SERVICE_FAILED = 42
    """_No description given by bungie._ """
    SERVICE_RETIRED = 43
    """_No description given by bungie._ """
    UNKNOWN_SQL_EXCEPTION = 44
    """_No description given by bungie._ """
    UNSUPPORTED_LOCALE = 45
    """_No description given by bungie._ """
    INVALID_PAGE_NUMBER = 46
    """_No description given by bungie._ """
    MAXIMUM_PAGE_SIZE_EXCEEDED = 47
    """_No description given by bungie._ """
    SERVICE_UNSUPPORTED = 48
    """_No description given by bungie._ """
    VALIDATION_MAXIMUM_UNICODE_COMBINING_CHARACTERS = 49
    """_No description given by bungie._ """
    VALIDATION_MAXIMUM_SEQUENTIAL_CARRIAGE_RETURNS = 50
    """_No description given by bungie._ """
    PER_ENDPOINT_REQUEST_THROTTLE_EXCEEDED = 51
    """_No description given by bungie._ """
    AUTH_CONTEXT_CACHE_ASSERTION = 52
    """_No description given by bungie._ """
    EX_PLATFORM_STRING_VALIDATION_ERROR = 53
    """_No description given by bungie._ """
    PER_APPLICATION_THROTTLE_EXCEEDED = 54
    """_No description given by bungie._ """
    PER_APPLICATION_ANONYMOUS_THROTTLE_EXCEEDED = 55
    """_No description given by bungie._ """
    PER_APPLICATION_AUTHENTICATED_THROTTLE_EXCEEDED = 56
    """_No description given by bungie._ """
    PER_USER_THROTTLE_EXCEEDED = 57
    """_No description given by bungie._ """
    PAYLOAD_SIGNATURE_VERIFICATION_FAILURE = 58
    """_No description given by bungie._ """
    INVALID_SERVICE_AUTH_CONTEXT = 59
    """_No description given by bungie._ """
    FAILED_MINIMUM_AGE_CHECK = 60
    """_No description given by bungie._ """
    OBSOLETE_CREDENTIAL_TYPE = 89
    """_No description given by bungie._ """
    UNABLE_TO_UN_PAIR_MOBILE_APP = 90
    """_No description given by bungie._ """
    UNABLE_TO_PAIR_MOBILE_APP = 91
    """_No description given by bungie._ """
    CANNOT_USE_MOBILE_AUTH_WITH_NON_MOBILE_PROVIDER = 92
    """_No description given by bungie._ """
    MISSING_DEVICE_COOKIE = 93
    """_No description given by bungie._ """
    FACEBOOK_TOKEN_EXPIRED = 94
    """_No description given by bungie._ """
    AUTH_TICKET_REQUIRED = 95
    """_No description given by bungie._ """
    COOKIE_CONTEXT_REQUIRED = 96
    """_No description given by bungie._ """
    UNKNOWN_AUTHENTICATION_ERROR = 97
    """_No description given by bungie._ """
    BUNGIE_NET_ACCOUNT_CREATION_REQUIRED = 98
    """_No description given by bungie._ """
    WEB_AUTH_REQUIRED = 99
    """_No description given by bungie._ """
    CONTENT_UNKNOWN_SQL_RESULT = 100
    """_No description given by bungie._ """
    CONTENT_NEED_UNIQUE_PATH = 101
    """_No description given by bungie._ """
    CONTENT_SQL_EXCEPTION = 102
    """_No description given by bungie._ """
    CONTENT_NOT_FOUND = 103
    """_No description given by bungie._ """
    CONTENT_SUCCESS_WITH_TAG_ADD_FAIL = 104
    """_No description given by bungie._ """
    CONTENT_SEARCH_MISSING_PARAMETERS = 105
    """_No description given by bungie._ """
    CONTENT_INVALID_ID = 106
    """_No description given by bungie._ """
    CONTENT_PHYSICAL_FILE_DELETION_ERROR = 107
    """_No description given by bungie._ """
    CONTENT_PHYSICAL_FILE_CREATION_ERROR = 108
    """_No description given by bungie._ """
    CONTENT_PERFORCE_SUBMISSION_ERROR = 109
    """_No description given by bungie._ """
    CONTENT_PERFORCE_INITIALIZATION_ERROR = 110
    """_No description given by bungie._ """
    CONTENT_DEPLOYMENT_PACKAGE_NOT_READY_ERROR = 111
    """_No description given by bungie._ """
    CONTENT_UPLOAD_FAILED = 112
    """_No description given by bungie._ """
    CONTENT_TOO_MANY_RESULTS = 113
    """_No description given by bungie._ """
    CONTENT_INVALID_STATE = 115
    """_No description given by bungie._ """
    CONTENT_NAVIGATION_PARENT_NOT_FOUND = 116
    """_No description given by bungie._ """
    CONTENT_NAVIGATION_PARENT_UPDATE_ERROR = 117
    """_No description given by bungie._ """
    DEPLOYMENT_PACKAGE_NOT_EDITABLE = 118
    """_No description given by bungie._ """
    CONTENT_VALIDATION_ERROR = 119
    """_No description given by bungie._ """
    CONTENT_PROPERTIES_VALIDATION_ERROR = 120
    """_No description given by bungie._ """
    CONTENT_TYPE_NOT_FOUND = 121
    """_No description given by bungie._ """
    DEPLOYMENT_PACKAGE_NOT_FOUND = 122
    """_No description given by bungie._ """
    CONTENT_SEARCH_INVALID_PARAMETERS = 123
    """_No description given by bungie._ """
    CONTENT_ITEM_PROPERTY_AGGREGATION_ERROR = 124
    """_No description given by bungie._ """
    DEPLOYMENT_PACKAGE_FILE_NOT_FOUND = 125
    """_No description given by bungie._ """
    CONTENT_PERFORCE_FILE_HISTORY_NOT_FOUND = 126
    """_No description given by bungie._ """
    CONTENT_ASSET_ZIP_CREATION_FAILURE = 127
    """_No description given by bungie._ """
    CONTENT_ASSET_ZIP_CREATION_BUSY = 128
    """_No description given by bungie._ """
    CONTENT_PROJECT_NOT_FOUND = 129
    """_No description given by bungie._ """
    CONTENT_FOLDER_NOT_FOUND = 130
    """_No description given by bungie._ """
    CONTENT_PACKAGES_INCONSISTENT = 131
    """_No description given by bungie._ """
    CONTENT_PACKAGES_INVALID_STATE = 132
    """_No description given by bungie._ """
    CONTENT_PACKAGES_INCONSISTENT_TYPE = 133
    """_No description given by bungie._ """
    CONTENT_CANNOT_DELETE_PACKAGE = 134
    """_No description given by bungie._ """
    CONTENT_LOCKED_FOR_CHANGES = 135
    """_No description given by bungie._ """
    CONTENT_FILE_UPLOAD_FAILED = 136
    """_No description given by bungie._ """
    CONTENT_NOT_REVIEWED = 137
    """_No description given by bungie._ """
    CONTENT_PERMISSION_DENIED = 138
    """_No description given by bungie._ """
    CONTENT_INVALID_EXTERNAL_URL = 139
    """_No description given by bungie._ """
    CONTENT_EXTERNAL_FILE_CANNOT_BE_IMPORTED_LOCALLY = 140
    """_No description given by bungie._ """
    CONTENT_TAG_SAVE_FAILURE = 141
    """_No description given by bungie._ """
    CONTENT_PERFORCE_UNMATCHED_FILE_ERROR = 142
    """_No description given by bungie._ """
    CONTENT_PERFORCE_CHANGELIST_RESULT_NOT_FOUND = 143
    """_No description given by bungie._ """
    CONTENT_PERFORCE_CHANGELIST_FILE_ITEMS_NOT_FOUND = 144
    """_No description given by bungie._ """
    CONTENT_PERFORCE_INVALID_REVISION_ERROR = 145
    """_No description given by bungie._ """
    CONTENT_UNLOADED_SAVE_RESULT = 146
    """_No description given by bungie._ """
    CONTENT_PROPERTY_INVALID_NUMBER = 147
    """_No description given by bungie._ """
    CONTENT_PROPERTY_INVALID_URL = 148
    """_No description given by bungie._ """
    CONTENT_PROPERTY_INVALID_DATE = 149
    """_No description given by bungie._ """
    CONTENT_PROPERTY_INVALID_SET = 150
    """_No description given by bungie._ """
    CONTENT_PROPERTY_CANNOT_DESERIALIZE = 151
    """_No description given by bungie._ """
    CONTENT_REGEX_VALIDATION_FAIL_ON_PROPERTY = 152
    """_No description given by bungie._ """
    CONTENT_MAX_LENGTH_FAIL_ON_PROPERTY = 153
    """_No description given by bungie._ """
    CONTENT_PROPERTY_UNEXPECTED_DESERIALIZATION_ERROR = 154
    """_No description given by bungie._ """
    CONTENT_PROPERTY_REQUIRED = 155
    """_No description given by bungie._ """
    CONTENT_CANNOT_CREATE_FILE = 156
    """_No description given by bungie._ """
    CONTENT_INVALID_MIGRATION_FILE = 157
    """_No description given by bungie._ """
    CONTENT_MIGRATION_ALTERING_PROCESSED_ITEM = 158
    """_No description given by bungie._ """
    CONTENT_PROPERTY_DEFINITION_NOT_FOUND = 159
    """_No description given by bungie._ """
    CONTENT_REVIEW_DATA_CHANGED = 160
    """_No description given by bungie._ """
    CONTENT_ROLLBACK_REVISION_NOT_IN_PACKAGE = 161
    """_No description given by bungie._ """
    CONTENT_ITEM_NOT_BASED_ON_LATEST_REVISION = 162
    """_No description given by bungie._ """
    CONTENT_UNAUTHORIZED = 163
    """_No description given by bungie._ """
    CONTENT_CANNOT_CREATE_DEPLOYMENT_PACKAGE = 164
    """_No description given by bungie._ """
    CONTENT_USER_NOT_FOUND = 165
    """_No description given by bungie._ """
    CONTENT_LOCALE_PERMISSION_DENIED = 166
    """_No description given by bungie._ """
    CONTENT_INVALID_LINK_TO_INTERNAL_ENVIRONMENT = 167
    """_No description given by bungie._ """
    CONTENT_INVALID_BLACKLISTED_CONTENT = 168
    """_No description given by bungie._ """
    CONTENT_MACRO_MALFORMED_NO_CONTENT_ID = 169
    """_No description given by bungie._ """
    CONTENT_MACRO_MALFORMED_NO_TEMPLATE_TYPE = 170
    """_No description given by bungie._ """
    CONTENT_ILLEGAL_B_NET_MEMBERSHIP_ID = 171
    """_No description given by bungie._ """
    CONTENT_LOCALE_DID_NOT_MATCH_EXPECTED = 172
    """_No description given by bungie._ """
    CONTENT_BABEL_CALL_FAILED = 173
    """_No description given by bungie._ """
    CONTENT_ENGLISH_POST_LIVE_FORBIDDEN = 174
    """_No description given by bungie._ """
    CONTENT_LOCALE_EDIT_PERMISSION_DENIED = 175
    """_No description given by bungie._ """
    CONTENT_STACK_UNKNOWN_ERROR = 176
    """_No description given by bungie._ """
    CONTENT_STACK_NOT_FOUND = 177
    """_No description given by bungie._ """
    CONTENT_STACK_RATE_LIMITED = 178
    """_No description given by bungie._ """
    CONTENT_STACK_TIMEOUT = 179
    """_No description given by bungie._ """
    CONTENT_STACK_SERVICE_ERROR = 180
    """_No description given by bungie._ """
    CONTENT_STACK_DESERIALIZATION_FAILURE = 181
    """_No description given by bungie._ """
    USER_NON_UNIQUE_NAME = 200
    """_No description given by bungie._ """
    USER_MANUAL_LINKING_STEP_REQUIRED = 201
    """_No description given by bungie._ """
    USER_CREATE_UNKNOWN_SQL_RESULT = 202
    """_No description given by bungie._ """
    USER_CREATE_UNKNOWN_SQL_EXCEPTION = 203
    """_No description given by bungie._ """
    USER_MALFORMED_MEMBERSHIP_ID = 204
    """_No description given by bungie._ """
    USER_CANNOT_FIND_REQUESTED_USER = 205
    """_No description given by bungie._ """
    USER_CANNOT_LOAD_ACCOUNT_CREDENTIAL_LINK_INFO = 206
    """_No description given by bungie._ """
    USER_INVALID_MOBILE_APP_TYPE = 207
    """_No description given by bungie._ """
    USER_MISSING_MOBILE_PAIRING_INFO = 208
    """_No description given by bungie._ """
    USER_CANNOT_GENERATE_MOBILE_KEY_WHILE_USING_MOBILE_CREDENTIAL = 209
    """_No description given by bungie._ """
    USER_GENERATE_MOBILE_KEY_EXISTING_SLOT_COLLISION = 210
    """_No description given by bungie._ """
    USER_DISPLAY_NAME_MISSING_OR_INVALID = 211
    """_No description given by bungie._ """
    USER_CANNOT_LOAD_ACCOUNT_PROFILE_DATA = 212
    """_No description given by bungie._ """
    USER_CANNOT_SAVE_USER_PROFILE_DATA = 213
    """_No description given by bungie._ """
    USER_EMAIL_MISSING_OR_INVALID = 214
    """_No description given by bungie._ """
    USER_TERMS_OF_USE_REQUIRED = 215
    """_No description given by bungie._ """
    USER_CANNOT_CREATE_NEW_ACCOUNT_WHILE_LOGGED_IN = 216
    """_No description given by bungie._ """
    USER_CANNOT_RESOLVE_CENTRAL_ACCOUNT = 217
    """_No description given by bungie._ """
    USER_INVALID_AVATAR = 218
    """_No description given by bungie._ """
    USER_MISSING_CREATED_USER_RESULT = 219
    """_No description given by bungie._ """
    USER_CANNOT_CHANGE_UNIQUE_NAME_YET = 220
    """_No description given by bungie._ """
    USER_CANNOT_CHANGE_DISPLAY_NAME_YET = 221
    """_No description given by bungie._ """
    USER_CANNOT_CHANGE_EMAIL = 222
    """_No description given by bungie._ """
    USER_UNIQUE_NAME_MUST_START_WITH_LETTER = 223
    """_No description given by bungie._ """
    USER_NO_LINKED_ACCOUNTS_SUPPORT_FRIEND_LISTINGS = 224
    """_No description given by bungie._ """
    USER_ACKNOWLEDGMENT_TABLE_FULL = 225
    """_No description given by bungie._ """
    USER_CREATION_DESTINY_MEMBERSHIP_REQUIRED = 226
    """_No description given by bungie._ """
    USER_FRIENDS_TOKEN_NEEDS_REFRESH = 227
    """_No description given by bungie._ """
    USER_EMAIL_VALIDATION_UNKNOWN = 228
    """_No description given by bungie._ """
    USER_EMAIL_VALIDATION_LIMIT = 229
    """_No description given by bungie._ """
    TRANSACTION_EMAIL_SEND_FAILURE = 230
    """_No description given by bungie._ """
    MAIL_HOOK_PERMISSION_FAILURE = 231
    """_No description given by bungie._ """
    MAIL_SERVICE_RATE_LIMIT = 232
    """_No description given by bungie._ """
    USER_EMAIL_MUST_BE_VERIFIED = 233
    """_No description given by bungie._ """
    USER_MUST_ALLOW_CUSTOMER_SERVICE_EMAILS = 234
    """_No description given by bungie._ """
    NON_TRANSACTIONAL_EMAIL_SEND_FAILURE = 235
    """_No description given by bungie._ """
    UNKNOWN_ERROR_SETTING_GLOBAL_DISPLAY_NAME = 236
    """_No description given by bungie._ """
    DUPLICATE_GLOBAL_DISPLAY_NAME = 237
    """_No description given by bungie._ """
    ERROR_RUNNING_NAME_VALIDATION_CHECKS = 238
    """_No description given by bungie._ """
    ERROR_DATABASE_GLOBAL_NAME = 239
    """_No description given by bungie._ """
    ERROR_NO_AVAILABLE_NAME_CHANGES = 240
    """_No description given by bungie._ """
    ERROR_NAME_ALREADY_SET_TO_INPUT = 241
    """_No description given by bungie._ """
    USER_DISPLAY_NAME_LESS_THAN_MIN_LENGTH = 242
    """_No description given by bungie._ """
    USER_DISPLAY_NAME_GREATER_THAN_MAX_LENGTH = 243
    """_No description given by bungie._ """
    USER_DISPLAY_NAME_CONTAINS_UNACCEPTABLE_OR_INVALID_CONTENT = 244
    """_No description given by bungie._ """
    EMAIL_VALIDATION_OFFLINE = 245
    """_No description given by bungie._ """
    EMAIL_VALIDATION_FAIL_OLD_CODE = 246
    """_No description given by bungie._ """
    EMAIL_VALIDATION_FAIL_BAD_LINK = 247
    """_No description given by bungie._ """
    EMAIL_UNSUBSCRIBE_FAIL = 248
    """_No description given by bungie._ """
    EMAIL_UNSUBSCRIBE_FAIL_NEW = 249
    """_No description given by bungie._ """
    MESSAGING_UNKNOWN_ERROR = 300
    """_No description given by bungie._ """
    MESSAGING_SELF_ERROR = 301
    """_No description given by bungie._ """
    MESSAGING_SEND_THROTTLE = 302
    """_No description given by bungie._ """
    MESSAGING_NO_BODY = 303
    """_No description given by bungie._ """
    MESSAGING_TOO_MANY_USERS = 304
    """_No description given by bungie._ """
    MESSAGING_CAN_NOT_LEAVE_CONVERSATION = 305
    """_No description given by bungie._ """
    MESSAGING_UNABLE_TO_SEND = 306
    """_No description given by bungie._ """
    MESSAGING_DELETED_USER_FORBIDDEN = 307
    """_No description given by bungie._ """
    MESSAGING_CANNOT_DELETE_EXTERNAL_CONVERSATION = 308
    """_No description given by bungie._ """
    MESSAGING_GROUP_CHAT_DISABLED = 309
    """_No description given by bungie._ """
    MESSAGING_MUST_INCLUDE_SELF_IN_PRIVATE_MESSAGE = 310
    """_No description given by bungie._ """
    MESSAGING_SENDER_IS_BANNED = 311
    """_No description given by bungie._ """
    MESSAGING_GROUP_OPTIONAL_CHAT_EXCEEDED_MAXIMUM = 312
    """_No description given by bungie._ """
    PRIVATE_MESSAGING_REQUIRES_DESTINY_MEMBERSHIP = 313
    """_No description given by bungie._ """
    MESSAGING_SEND_DAILY_THROTTLE = 314
    """_No description given by bungie._ """
    ADD_SURVEY_ANSWERS_UNKNOWN_SQL_EXCEPTION = 400
    """_No description given by bungie._ """
    FORUM_BODY_CANNOT_BE_EMPTY = 500
    """_No description given by bungie._ """
    FORUM_SUBJECT_CANNOT_BE_EMPTY_ON_TOPIC_POST = 501
    """_No description given by bungie._ """
    FORUM_CANNOT_LOCATE_PARENT_POST = 502
    """_No description given by bungie._ """
    FORUM_THREAD_LOCKED_FOR_REPLIES = 503
    """_No description given by bungie._ """
    FORUM_UNKNOWN_SQL_RESULT_DURING_CREATE_POST = 504
    """_No description given by bungie._ """
    FORUM_UNKNOWN_TAG_CREATION_ERROR = 505
    """_No description given by bungie._ """
    FORUM_UNKNOWN_SQL_RESULT_DURING_TAG_ITEM = 506
    """_No description given by bungie._ """
    FORUM_UNKNOWN_EXCEPTION_CREATE_POST = 507
    """_No description given by bungie._ """
    FORUM_QUESTION_MUST_BE_TOPIC_POST = 508
    """_No description given by bungie._ """
    FORUM_EXCEPTION_DURING_TAG_SEARCH = 509
    """_No description given by bungie._ """
    FORUM_EXCEPTION_DURING_TOPIC_RETRIEVAL = 510
    """_No description given by bungie._ """
    FORUM_ALIASED_TAG_ERROR = 511
    """_No description given by bungie._ """
    FORUM_CANNOT_LOCATE_THREAD = 512
    """_No description given by bungie._ """
    FORUM_UNKNOWN_EXCEPTION_EDIT_POST = 513
    """_No description given by bungie._ """
    FORUM_CANNOT_LOCATE_POST = 514
    """_No description given by bungie._ """
    FORUM_UNKNOWN_EXCEPTION_GET_OR_CREATE_TAGS = 515
    """_No description given by bungie._ """
    FORUM_EDIT_PERMISSION_DENIED = 516
    """_No description given by bungie._ """
    FORUM_UNKNOWN_SQL_RESULT_DURING_TAG_ID_RETRIEVAL = 517
    """_No description given by bungie._ """
    FORUM_CANNOT_GET_RATING = 518
    """_No description given by bungie._ """
    FORUM_UNKNOWN_EXCEPTION_GET_RATING = 519
    """_No description given by bungie._ """
    FORUM_RATINGS_ACCESS_ERROR = 520
    """_No description given by bungie._ """
    FORUM_RELATED_POST_ACCESS_ERROR = 521
    """_No description given by bungie._ """
    FORUM_LATEST_REPLY_ACCESS_ERROR = 522
    """_No description given by bungie._ """
    FORUM_USER_STATUS_ACCESS_ERROR = 523
    """_No description given by bungie._ """
    FORUM_AUTHOR_ACCESS_ERROR = 524
    """_No description given by bungie._ """
    FORUM_GROUP_ACCESS_ERROR = 525
    """_No description given by bungie._ """
    FORUM_URL_EXPECTED_BUT_MISSING = 526
    """_No description given by bungie._ """
    FORUM_REPLIES_CANNOT_BE_EMPTY = 527
    """_No description given by bungie._ """
    FORUM_REPLIES_CANNOT_BE_IN_DIFFERENT_GROUPS = 528
    """_No description given by bungie._ """
    FORUM_SUB_TOPIC_CANNOT_BE_CREATED_AT_THIS_THREAD_LEVEL = 529
    """_No description given by bungie._ """
    FORUM_CANNOT_CREATE_CONTENT_TOPIC = 530
    """_No description given by bungie._ """
    FORUM_TOPIC_DOES_NOT_EXIST = 531
    """_No description given by bungie._ """
    FORUM_CONTENT_COMMENTS_NOT_ALLOWED = 532
    """_No description given by bungie._ """
    FORUM_UNKNOWN_SQL_RESULT_DURING_EDIT_POST = 533
    """_No description given by bungie._ """
    FORUM_UNKNOWN_SQL_RESULT_DURING_GET_POST = 534
    """_No description given by bungie._ """
    FORUM_POST_VALIDATION_BAD_URL = 535
    """_No description given by bungie._ """
    FORUM_BODY_TOO_LONG = 536
    """_No description given by bungie._ """
    FORUM_SUBJECT_TOO_LONG = 537
    """_No description given by bungie._ """
    FORUM_ANNOUNCEMENT_NOT_ALLOWED = 538
    """_No description given by bungie._ """
    FORUM_CANNOT_SHARE_OWN_POST = 539
    """_No description given by bungie._ """
    FORUM_EDIT_NO_OP = 540
    """_No description given by bungie._ """
    FORUM_UNKNOWN_DATABASE_ERROR_DURING_GET_POST = 541
    """_No description given by bungie._ """
    FORUM_EXCEEED_MAXIMUM_ROW_LIMIT = 542
    """_No description given by bungie._ """
    FORUM_CANNOT_SHARE_PRIVATE_POST = 543
    """_No description given by bungie._ """
    FORUM_CANNOT_CROSS_POST_BETWEEN_GROUPS = 544
    """_No description given by bungie._ """
    FORUM_INCOMPATIBLE_CATEGORIES = 555
    """_No description given by bungie._ """
    FORUM_CANNOT_USE_THESE_CATEGORIES_ON_NON_TOPIC_POST = 556
    """_No description given by bungie._ """
    FORUM_CAN_ONLY_DELETE_TOPICS = 557
    """_No description given by bungie._ """
    FORUM_DELETE_SQL_EXCEPTION = 558
    """_No description given by bungie._ """
    FORUM_DELETE_SQL_UNKNOWN_RESULT = 559
    """_No description given by bungie._ """
    FORUM_TOO_MANY_TAGS = 560
    """_No description given by bungie._ """
    FORUM_CAN_ONLY_RATE_TOPICS = 561
    """_No description given by bungie._ """
    FORUM_BANNED_POSTS_CANNOT_BE_EDITED = 562
    """_No description given by bungie._ """
    FORUM_THREAD_ROOT_IS_BANNED = 563
    """_No description given by bungie._ """
    FORUM_CANNOT_USE_OFFICIAL_TAG_CATEGORY_AS_TAG = 564
    """_No description given by bungie._ """
    FORUM_ANSWER_CANNOT_BE_MADE_ON_CREATE_POST = 565
    """_No description given by bungie._ """
    FORUM_ANSWER_CANNOT_BE_MADE_ON_EDIT_POST = 566
    """_No description given by bungie._ """
    FORUM_ANSWER_POST_ID_IS_NOT_A_DIRECT_REPLY_OF_QUESTION = 567
    """_No description given by bungie._ """
    FORUM_ANSWER_TOPIC_ID_IS_NOT_A_QUESTION = 568
    """_No description given by bungie._ """
    FORUM_UNKNOWN_EXCEPTION_DURING_MARK_ANSWER = 569
    """_No description given by bungie._ """
    FORUM_UNKNOWN_SQL_RESULT_DURING_MARK_ANSWER = 570
    """_No description given by bungie._ """
    FORUM_CANNOT_RATE_YOUR_OWN_POSTS = 571
    """_No description given by bungie._ """
    FORUM_POLLS_MUST_BE_THE_FIRST_POST_IN_TOPIC = 572
    """_No description given by bungie._ """
    FORUM_INVALID_POLL_INPUT = 573
    """_No description given by bungie._ """
    FORUM_GROUP_ADMIN_EDIT_NON_MEMBER = 574
    """_No description given by bungie._ """
    FORUM_CANNOT_EDIT_MODERATOR_EDITED_POST = 575
    """_No description given by bungie._ """
    FORUM_REQUIRES_DESTINY_MEMBERSHIP = 576
    """_No description given by bungie._ """
    FORUM_UNEXPECTED_ERROR = 577
    """_No description given by bungie._ """
    FORUM_AGE_LOCK = 578
    """_No description given by bungie._ """
    FORUM_MAX_PAGES = 579
    """_No description given by bungie._ """
    FORUM_MAX_PAGES_OLDEST_FIRST = 580
    """_No description given by bungie._ """
    FORUM_CANNOT_APPLY_FORUM_ID_WITHOUT_TAGS = 581
    """_No description given by bungie._ """
    FORUM_CANNOT_APPLY_FORUM_ID_TO_NON_TOPICS = 582
    """_No description given by bungie._ """
    FORUM_CANNOT_DOWNVOTE_COMMUNITY_CREATIONS = 583
    """_No description given by bungie._ """
    FORUM_TOPICS_MUST_HAVE_OFFICIAL_CATEGORY = 584
    """_No description given by bungie._ """
    FORUM_RECRUITMENT_TOPIC_MALFORMED = 585
    """_No description given by bungie._ """
    FORUM_RECRUITMENT_TOPIC_NOT_FOUND = 586
    """_No description given by bungie._ """
    FORUM_RECRUITMENT_TOPIC_NO_SLOTS_REMAINING = 587
    """_No description given by bungie._ """
    FORUM_RECRUITMENT_TOPIC_KICK_BAN = 588
    """_No description given by bungie._ """
    FORUM_RECRUITMENT_TOPIC_REQUIREMENTS_NOT_MET = 589
    """_No description given by bungie._ """
    FORUM_RECRUITMENT_TOPIC_NO_PLAYERS = 590
    """_No description given by bungie._ """
    FORUM_RECRUITMENT_APPROVE_FAIL_MESSAGE_BAN = 591
    """_No description given by bungie._ """
    FORUM_RECRUITMENT_GLOBAL_BAN = 592
    """_No description given by bungie._ """
    FORUM_USER_BANNED_FROM_THIS_TOPIC = 593
    """_No description given by bungie._ """
    FORUM_RECRUITMENT_FIRETEAM_MEMBERS_ONLY = 594
    """_No description given by bungie._ """
    FORUM_REQUIRES_DESTINY2_PROGRESS = 595
    """_No description given by bungie._ """
    FORUM_REQUIRES_DESTINY2_ENTITLEMENT_PURCHASE = 596
    """_No description given by bungie._ """
    GROUP_MEMBERSHIP_APPLICATION_ALREADY_RESOLVED = 601
    """_No description given by bungie._ """
    GROUP_MEMBERSHIP_ALREADY_APPLIED = 602
    """_No description given by bungie._ """
    GROUP_MEMBERSHIP_INSUFFICIENT_PRIVILEGES = 603
    """_No description given by bungie._ """
    GROUP_ID_NOT_RETURNED_FROM_CREATION = 604
    """_No description given by bungie._ """
    GROUP_SEARCH_INVALID_PARAMETERS = 605
    """_No description given by bungie._ """
    GROUP_MEMBERSHIP_PENDING_APPLICATION_NOT_FOUND = 606
    """_No description given by bungie._ """
    GROUP_INVALID_ID = 607
    """_No description given by bungie._ """
    GROUP_INVALID_MEMBERSHIP_ID = 608
    """_No description given by bungie._ """
    GROUP_INVALID_MEMBERSHIP_TYPE = 609
    """_No description given by bungie._ """
    GROUP_MISSING_TAGS = 610
    """_No description given by bungie._ """
    GROUP_MEMBERSHIP_NOT_FOUND = 611
    """_No description given by bungie._ """
    GROUP_INVALID_RATING = 612
    """_No description given by bungie._ """
    GROUP_USER_FOLLOWING_ACCESS_ERROR = 613
    """_No description given by bungie._ """
    GROUP_USER_MEMBERSHIP_ACCESS_ERROR = 614
    """_No description given by bungie._ """
    GROUP_CREATOR_ACCESS_ERROR = 615
    """_No description given by bungie._ """
    GROUP_ADMIN_ACCESS_ERROR = 616
    """_No description given by bungie._ """
    GROUP_PRIVATE_POST_NOT_VIEWABLE = 617
    """_No description given by bungie._ """
    GROUP_MEMBERSHIP_NOT_LOGGED_IN = 618
    """_No description given by bungie._ """
    GROUP_NOT_DELETED = 619
    """_No description given by bungie._ """
    GROUP_UNKNOWN_ERROR_UNDELETING_GROUP = 620
    """_No description given by bungie._ """
    GROUP_DELETED = 621
    """_No description given by bungie._ """
    GROUP_NOT_FOUND = 622
    """_No description given by bungie._ """
    GROUP_MEMBER_BANNED = 623
    """_No description given by bungie._ """
    GROUP_MEMBERSHIP_CLOSED = 624
    """_No description given by bungie._ """
    GROUP_PRIVATE_POST_OVERRIDE_ERROR = 625
    """_No description given by bungie._ """
    GROUP_NAME_TAKEN = 626
    """_No description given by bungie._ """
    GROUP_DELETION_GRACE_PERIOD_EXPIRED = 627
    """_No description given by bungie._ """
    GROUP_CANNOT_CHECK_BAN_STATUS = 628
    """_No description given by bungie._ """
    GROUP_MAXIMUM_MEMBERSHIP_COUNT_REACHED = 629
    """_No description given by bungie._ """
    NO_DESTINY_ACCOUNT_FOR_CLAN_PLATFORM = 630
    """_No description given by bungie._ """
    ALREADY_REQUESTING_MEMBERSHIP_FOR_CLAN_PLATFORM = 631
    """_No description given by bungie._ """
    ALREADY_CLAN_MEMBER_ON_PLATFORM = 632
    """_No description given by bungie._ """
    GROUP_JOINED_CANNOT_SET_CLAN_NAME = 633
    """_No description given by bungie._ """
    GROUP_LEFT_CANNOT_CLEAR_CLAN_NAME = 634
    """_No description given by bungie._ """
    GROUP_RELATIONSHIP_REQUEST_PENDING = 635
    """_No description given by bungie._ """
    GROUP_RELATIONSHIP_REQUEST_BLOCKED = 636
    """_No description given by bungie._ """
    GROUP_RELATIONSHIP_REQUEST_NOT_FOUND = 637
    """_No description given by bungie._ """
    GROUP_RELATIONSHIP_BLOCK_NOT_FOUND = 638
    """_No description given by bungie._ """
    GROUP_RELATIONSHIP_NOT_FOUND = 639
    """_No description given by bungie._ """
    GROUP_ALREADY_ALLIED = 641
    """_No description given by bungie._ """
    GROUP_ALREADY_MEMBER = 642
    """_No description given by bungie._ """
    GROUP_RELATIONSHIP_ALREADY_EXISTS = 643
    """_No description given by bungie._ """
    INVALID_GROUP_TYPES_FOR_RELATIONSHIP_REQUEST = 644
    """_No description given by bungie._ """
    GROUP_AT_MAXIMUM_ALLIANCES = 646
    """_No description given by bungie._ """
    GROUP_CANNOT_SET_CLAN_ONLY_SETTINGS = 647
    """_No description given by bungie._ """
    CLAN_CANNOT_SET_TWO_DEFAULT_POST_TYPES = 648
    """_No description given by bungie._ """
    GROUP_MEMBER_INVALID_MEMBER_TYPE = 649
    """_No description given by bungie._ """
    GROUP_INVALID_PLATFORM_TYPE = 650
    """_No description given by bungie._ """
    GROUP_MEMBER_INVALID_SORT = 651
    """_No description given by bungie._ """
    GROUP_INVALID_RESOLVE_STATE = 652
    """_No description given by bungie._ """
    CLAN_ALREADY_ENABLED_FOR_PLATFORM = 653
    """_No description given by bungie._ """
    CLAN_NOT_ENABLED_FOR_PLATFORM = 654
    """_No description given by bungie._ """
    CLAN_ENABLED_BUT_COULD_NOT_JOIN_NO_ACCOUNT = 655
    """_No description given by bungie._ """
    CLAN_ENABLED_BUT_COULD_NOT_JOIN_ALREADY_MEMBER = 656
    """_No description given by bungie._ """
    CLAN_CANNOT_JOIN_NO_CREDENTIAL = 657
    """_No description given by bungie._ """
    NO_CLAN_MEMBERSHIP_FOR_PLATFORM = 658
    """_No description given by bungie._ """
    GROUP_TO_GROUP_FOLLOW_LIMIT_REACHED = 659
    """_No description given by bungie._ """
    CHILD_GROUP_ALREADY_IN_ALLIANCE = 660
    """_No description given by bungie._ """
    OWNER_GROUP_ALREADY_IN_ALLIANCE = 661
    """_No description given by bungie._ """
    ALLIANCE_OWNER_CANNOT_JOIN_ALLIANCE = 662
    """_No description given by bungie._ """
    GROUP_NOT_IN_ALLIANCE = 663
    """_No description given by bungie._ """
    CHILD_GROUP_CANNOT_INVITE_TO_ALLIANCE = 664
    """_No description given by bungie._ """
    GROUP_TO_GROUP_ALREADY_FOLLOWED = 665
    """_No description given by bungie._ """
    GROUP_TO_GROUP_NOT_FOLLOWING = 666
    """_No description given by bungie._ """
    CLAN_MAXIMUM_MEMBERSHIP_REACHED = 667
    """_No description given by bungie._ """
    CLAN_NAME_NOT_VALID = 668
    """_No description given by bungie._ """
    CLAN_NAME_NOT_VALID_ERROR = 669
    """_No description given by bungie._ """
    ALLIANCE_OWNER_NOT_DEFINED = 670
    """_No description given by bungie._ """
    ALLIANCE_CHILD_NOT_DEFINED = 671
    """_No description given by bungie._ """
    CLAN_CULTURE_ILLEGAL_CHARACTERS = 672
    """_No description given by bungie._ """
    CLAN_TAG_ILLEGAL_CHARACTERS = 673
    """_No description given by bungie._ """
    CLAN_REQUIRES_INVITATION = 674
    """_No description given by bungie._ """
    CLAN_MEMBERSHIP_CLOSED = 675
    """_No description given by bungie._ """
    CLAN_INVITE_ALREADY_MEMBER = 676
    """_No description given by bungie._ """
    GROUP_INVITE_ALREADY_MEMBER = 677
    """_No description given by bungie._ """
    GROUP_JOIN_APPROVAL_REQUIRED = 678
    """_No description given by bungie._ """
    CLAN_TAG_REQUIRED = 679
    """_No description given by bungie._ """
    GROUP_NAME_CANNOT_START_OR_END_WITH_WHITE_SPACE = 680
    """_No description given by bungie._ """
    CLAN_CALLSIGN_CANNOT_START_OR_END_WITH_WHITE_SPACE = 681
    """_No description given by bungie._ """
    CLAN_MIGRATION_FAILED = 682
    """_No description given by bungie._ """
    CLAN_NOT_ENABLED_ALREADY_MEMBER_OF_ANOTHER_CLAN = 683
    """_No description given by bungie._ """
    GROUP_MODERATION_NOT_PERMITTED_ON_NON_MEMBERS = 684
    """_No description given by bungie._ """
    CLAN_CREATION_IN_WORLD_SERVER_FAILED = 685
    """_No description given by bungie._ """
    CLAN_NOT_FOUND = 686
    """_No description given by bungie._ """
    CLAN_MEMBERSHIP_LEVEL_DOES_NOT_PERMIT_THAT_ACTION = 687
    """_No description given by bungie._ """
    CLAN_MEMBER_NOT_FOUND = 688
    """_No description given by bungie._ """
    CLAN_MISSING_MEMBERSHIP_APPROVERS = 689
    """_No description given by bungie._ """
    CLAN_IN_WRONG_STATE_FOR_REQUESTED_ACTION = 690
    """_No description given by bungie._ """
    CLAN_NAME_ALREADY_USED = 691
    """_No description given by bungie._ """
    CLAN_TOO_FEW_MEMBERS = 692
    """_No description given by bungie._ """
    CLAN_INFO_CANNOT_BE_WHITESPACE = 693
    """_No description given by bungie._ """
    GROUP_CULTURE_THROTTLE = 694
    """_No description given by bungie._ """
    CLAN_TARGET_DISALLOWS_INVITES = 695
    """_No description given by bungie._ """
    CLAN_INVALID_OPERATION = 696
    """_No description given by bungie._ """
    CLAN_FOUNDER_CANNOT_LEAVE_WITHOUT_ABDICATION = 697
    """_No description given by bungie._ """
    CLAN_NAME_RESERVED = 698
    """_No description given by bungie._ """
    CLAN_APPLICANT_IN_CLAN_SO_NOW_INVITED = 699
    """_No description given by bungie._ """
    ACTIVITIES_UNKNOWN_EXCEPTION = 701
    """_No description given by bungie._ """
    ACTIVITIES_PARAMETER_NULL = 702
    """_No description given by bungie._ """
    ACTIVITY_COUNTS_DIABLED = 703
    """_No description given by bungie._ """
    ACTIVITY_SEARCH_INVALID_PARAMETERS = 704
    """_No description given by bungie._ """
    ACTIVITY_PERMISSION_DENIED = 705
    """_No description given by bungie._ """
    SHARE_ALREADY_SHARED = 706
    """_No description given by bungie._ """
    ACTIVITY_LOGGING_DISABLED = 707
    """_No description given by bungie._ """
    CLAN_REQUIRES_EXISTING_DESTINY_ACCOUNT = 750
    """_No description given by bungie._ """
    CLAN_NAME_RESTRICTED = 751
    """_No description given by bungie._ """
    CLAN_CREATION_BAN = 752
    """_No description given by bungie._ """
    CLAN_CREATION_TENURE_REQUIREMENTS_NOT_MET = 753
    """_No description given by bungie._ """
    CLAN_FIELD_CONTAINS_RESERVED_TERMS = 754
    """_No description given by bungie._ """
    CLAN_FIELD_CONTAINS_INAPPROPRIATE_CONTENT = 755
    """_No description given by bungie._ """
    ITEM_ALREADY_FOLLOWED = 801
    """_No description given by bungie._ """
    ITEM_NOT_FOLLOWED = 802
    """_No description given by bungie._ """
    CANNOT_FOLLOW_SELF = 803
    """_No description given by bungie._ """
    GROUP_FOLLOW_LIMIT_EXCEEDED = 804
    """_No description given by bungie._ """
    TAG_FOLLOW_LIMIT_EXCEEDED = 805
    """_No description given by bungie._ """
    USER_FOLLOW_LIMIT_EXCEEDED = 806
    """_No description given by bungie._ """
    FOLLOW_UNSUPPORTED_ENTITY_TYPE = 807
    """_No description given by bungie._ """
    NO_VALID_TAGS_IN_LIST = 900
    """_No description given by bungie._ """
    BELOW_MINIMUM_SUGGESTION_LENGTH = 901
    """_No description given by bungie._ """
    CANNOT_GET_SUGGESTIONS_ON_MULTIPLE_TAGS_SIMULTANEOUSLY = 902
    """_No description given by bungie._ """
    NOT_A_VALID_PARTIAL_TAG = 903
    """_No description given by bungie._ """
    TAG_SUGGESTIONS_UNKNOWN_SQL_RESULT = 904
    """_No description given by bungie._ """
    TAGS_UNABLE_TO_LOAD_POPULAR_TAGS_FROM_DATABASE = 905
    """_No description given by bungie._ """
    TAG_INVALID = 906
    """_No description given by bungie._ """
    TAG_NOT_FOUND = 907
    """_No description given by bungie._ """
    SINGLE_TAG_EXPECTED = 908
    """_No description given by bungie._ """
    TAGS_EXCEEDED_MAXIMUM_PER_ITEM = 909
    """_No description given by bungie._ """
    IGNORE_INVALID_PARAMETERS = 1000
    """_No description given by bungie._ """
    IGNORE_SQL_EXCEPTION = 1001
    """_No description given by bungie._ """
    IGNORE_ERROR_RETRIEVING_GROUP_PERMISSIONS = 1002
    """_No description given by bungie._ """
    IGNORE_ERROR_INSUFFICIENT_PERMISSION = 1003
    """_No description given by bungie._ """
    IGNORE_ERROR_RETRIEVING_ITEM = 1004
    """_No description given by bungie._ """
    IGNORE_CANNOT_IGNORE_SELF = 1005
    """_No description given by bungie._ """
    IGNORE_ILLEGAL_TYPE = 1006
    """_No description given by bungie._ """
    IGNORE_NOT_FOUND = 1007
    """_No description given by bungie._ """
    IGNORE_USER_GLOBALLY_IGNORED = 1008
    """_No description given by bungie._ """
    IGNORE_USER_IGNORED = 1009
    """_No description given by bungie._ """
    TARGET_USER_IGNORED = 1010
    """_No description given by bungie._ """
    NOTIFICATION_SETTING_INVALID = 1100
    """_No description given by bungie._ """
    PSN_API_EXPIRED_ACCESS_TOKEN = 1204
    """_No description given by bungie._ """
    P_S_N_EX_FORBIDDEN = 1205
    """_No description given by bungie._ """
    P_S_N_EX_SYSTEM_DISABLED = 1218
    """_No description given by bungie._ """
    PSN_API_ERROR_CODE_UNKNOWN = 1223
    """_No description given by bungie._ """
    PSN_API_ERROR_WEB_EXCEPTION = 1224
    """_No description given by bungie._ """
    PSN_API_BAD_REQUEST = 1225
    """_No description given by bungie._ """
    PSN_API_ACCESS_TOKEN_REQUIRED = 1226
    """_No description given by bungie._ """
    PSN_API_INVALID_ACCESS_TOKEN = 1227
    """_No description given by bungie._ """
    PSN_API_BANNED_USER = 1229
    """_No description given by bungie._ """
    PSN_API_ACCOUNT_UPGRADE_REQUIRED = 1230
    """_No description given by bungie._ """
    PSN_API_SERVICE_TEMPORARILY_UNAVAILABLE = 1231
    """_No description given by bungie._ """
    PSN_API_SERVER_BUSY = 1232
    """_No description given by bungie._ """
    PSN_API_UNDER_MAINTENANCE = 1233
    """_No description given by bungie._ """
    PSN_API_PROFILE_USER_NOT_FOUND = 1234
    """_No description given by bungie._ """
    PSN_API_PROFILE_PRIVACY_RESTRICTION = 1235
    """_No description given by bungie._ """
    PSN_API_PROFILE_UNDER_MAINTENANCE = 1236
    """_No description given by bungie._ """
    PSN_API_ACCOUNT_ATTRIBUTE_MISSING = 1237
    """_No description given by bungie._ """
    PSN_API_NO_PERMISSION = 1238
    """_No description given by bungie._ """
    PSN_API_TARGET_USER_BLOCKED = 1239
    """_No description given by bungie._ """
    PSN_API_JWKS_MISSING = 1240
    """_No description given by bungie._ """
    PSN_API_JWT_MALFORMED_HEADER = 1241
    """_No description given by bungie._ """
    PSN_API_JWT_MALFORMED_PAYLOAD = 1242
    """_No description given by bungie._ """
    XBL_EX_SYSTEM_DISABLED = 1300
    """_No description given by bungie._ """
    XBL_EX_UNKNOWN_ERROR = 1301
    """_No description given by bungie._ """
    XBL_API_ERROR_WEB_EXCEPTION = 1302
    """_No description given by bungie._ """
    XBL_STS_TOKEN_INVALID = 1303
    """_No description given by bungie._ """
    XBL_STS_MISSING_TOKEN = 1304
    """_No description given by bungie._ """
    XBL_STS_EXPIRED_TOKEN = 1305
    """_No description given by bungie._ """
    XBL_ACCESS_TO_THE_SANDBOX_DENIED = 1306
    """_No description given by bungie._ """
    XBL_MSA_RESPONSE_MISSING = 1307
    """_No description given by bungie._ """
    XBL_MSA_ACCESS_TOKEN_EXPIRED = 1308
    """_No description given by bungie._ """
    XBL_MSA_INVALID_REQUEST = 1309
    """_No description given by bungie._ """
    XBL_MSA_FRIENDS_REQUIRE_SIGN_IN = 1310
    """_No description given by bungie._ """
    XBL_USER_ACTION_REQUIRED = 1311
    """_No description given by bungie._ """
    XBL_PARENTAL_CONTROLS = 1312
    """_No description given by bungie._ """
    XBL_DEVELOPER_ACCOUNT = 1313
    """_No description given by bungie._ """
    XBL_USER_TOKEN_EXPIRED = 1314
    """_No description given by bungie._ """
    XBL_USER_TOKEN_INVALID = 1315
    """_No description given by bungie._ """
    XBL_OFFLINE = 1316
    """_No description given by bungie._ """
    XBL_UNKNOWN_ERROR_CODE = 1317
    """_No description given by bungie._ """
    XBL_MSA_INVALID_GRANT = 1318
    """_No description given by bungie._ """
    REPORT_NOT_YET_RESOLVED = 1400
    """_No description given by bungie._ """
    REPORT_OVERTURN_DOES_NOT_CHANGE_DECISION = 1401
    """_No description given by bungie._ """
    REPORT_NOT_FOUND = 1402
    """_No description given by bungie._ """
    REPORT_ALREADY_REPORTED = 1403
    """_No description given by bungie._ """
    REPORT_INVALID_RESOLUTION = 1404
    """_No description given by bungie._ """
    REPORT_NOT_ASSIGNED_TO_YOU = 1405
    """_No description given by bungie._ """
    LEGACY_GAME_STATS_SYSTEM_DISABLED = 1500
    """_No description given by bungie._ """
    LEGACY_GAME_STATS_UNKNOWN_ERROR = 1501
    """_No description given by bungie._ """
    LEGACY_GAME_STATS_MALFORMED_SNEAKER_NET_CODE = 1502
    """_No description given by bungie._ """
    DESTINY_ACCOUNT_ACQUISITION_FAILURE = 1600
    """_No description given by bungie._ """
    DESTINY_ACCOUNT_NOT_FOUND = 1601
    """_No description given by bungie._ """
    DESTINY_BUILD_STATS_DATABASE_ERROR = 1602
    """_No description given by bungie._ """
    DESTINY_CHARACTER_STATS_DATABASE_ERROR = 1603
    """_No description given by bungie._ """
    DESTINY_PV_P_STATS_DATABASE_ERROR = 1604
    """_No description given by bungie._ """
    DESTINY_PV_E_STATS_DATABASE_ERROR = 1605
    """_No description given by bungie._ """
    DESTINY_GRIMOIRE_STATS_DATABASE_ERROR = 1606
    """_No description given by bungie._ """
    DESTINY_STATS_PARAMETER_MEMBERSHIP_TYPE_PARSE_ERROR = 1607
    """_No description given by bungie._ """
    DESTINY_STATS_PARAMETER_MEMBERSHIP_ID_PARSE_ERROR = 1608
    """_No description given by bungie._ """
    DESTINY_STATS_PARAMETER_RANGE_PARSE_ERROR = 1609
    """_No description given by bungie._ """
    DESTINY_STRING_ITEM_HASH_NOT_FOUND = 1610
    """_No description given by bungie._ """
    DESTINY_STRING_SET_NOT_FOUND = 1611
    """_No description given by bungie._ """
    DESTINY_CONTENT_LOOKUP_NOT_FOUND_FOR_KEY = 1612
    """_No description given by bungie._ """
    DESTINY_CONTENT_ITEM_NOT_FOUND = 1613
    """_No description given by bungie._ """
    DESTINY_CONTENT_SECTION_NOT_FOUND = 1614
    """_No description given by bungie._ """
    DESTINY_CONTENT_PROPERTY_NOT_FOUND = 1615
    """_No description given by bungie._ """
    DESTINY_CONTENT_CONFIG_NOT_FOUND = 1616
    """_No description given by bungie._ """
    DESTINY_CONTENT_PROPERTY_BUCKET_VALUE_NOT_FOUND = 1617
    """_No description given by bungie._ """
    DESTINY_UNEXPECTED_ERROR = 1618
    """_No description given by bungie._ """
    DESTINY_INVALID_ACTION = 1619
    """_No description given by bungie._ """
    DESTINY_CHARACTER_NOT_FOUND = 1620
    """_No description given by bungie._ """
    DESTINY_INVALID_FLAG = 1621
    """_No description given by bungie._ """
    DESTINY_INVALID_REQUEST = 1622
    """_No description given by bungie._ """
    DESTINY_ITEM_NOT_FOUND = 1623
    """_No description given by bungie._ """
    DESTINY_INVALID_CUSTOMIZATION_CHOICES = 1624
    """_No description given by bungie._ """
    DESTINY_VENDOR_ITEM_NOT_FOUND = 1625
    """_No description given by bungie._ """
    DESTINY_INTERNAL_ERROR = 1626
    """_No description given by bungie._ """
    DESTINY_VENDOR_NOT_FOUND = 1627
    """_No description given by bungie._ """
    DESTINY_RECENT_ACTIVITIES_DATABASE_ERROR = 1628
    """_No description given by bungie._ """
    DESTINY_ITEM_BUCKET_NOT_FOUND = 1629
    """_No description given by bungie._ """
    DESTINY_INVALID_MEMBERSHIP_TYPE = 1630
    """_No description given by bungie._ """
    DESTINY_VERSION_INCOMPATIBILITY = 1631
    """_No description given by bungie._ """
    DESTINY_ITEM_ALREADY_IN_INVENTORY = 1632
    """_No description given by bungie._ """
    DESTINY_BUCKET_NOT_FOUND = 1633
    """_No description given by bungie._ """
    DESTINY_CHARACTER_NOT_IN_TOWER = 1634
    """Note: This is one of those holdovers from Destiny 1. We didn't change the enum because I am lazy, but in Destiny 2 this would read "DestinyCharacterNotInSocialSpace" """
    DESTINY_CHARACTER_NOT_LOGGED_IN = 1635
    """_No description given by bungie._ """
    DESTINY_DEFINITIONS_NOT_LOADED = 1636
    """_No description given by bungie._ """
    DESTINY_INVENTORY_FULL = 1637
    """_No description given by bungie._ """
    DESTINY_ITEM_FAILED_LEVEL_CHECK = 1638
    """_No description given by bungie._ """
    DESTINY_ITEM_FAILED_UNLOCK_CHECK = 1639
    """_No description given by bungie._ """
    DESTINY_ITEM_UNEQUIPPABLE = 1640
    """_No description given by bungie._ """
    DESTINY_ITEM_UNIQUE_EQUIP_RESTRICTED = 1641
    """_No description given by bungie._ """
    DESTINY_NO_ROOM_IN_DESTINATION = 1642
    """_No description given by bungie._ """
    DESTINY_SERVICE_FAILURE = 1643
    """_No description given by bungie._ """
    DESTINY_SERVICE_RETIRED = 1644
    """_No description given by bungie._ """
    DESTINY_TRANSFER_FAILED = 1645
    """_No description given by bungie._ """
    DESTINY_TRANSFER_NOT_FOUND_FOR_SOURCE_BUCKET = 1646
    """_No description given by bungie._ """
    DESTINY_UNEXPECTED_RESULT_IN_VENDOR_TRANSFER_CHECK = 1647
    """_No description given by bungie._ """
    DESTINY_UNIQUENESS_VIOLATION = 1648
    """_No description given by bungie._ """
    DESTINY_ERROR_DESERIALIZATION_FAILURE = 1649
    """_No description given by bungie._ """
    DESTINY_VALID_ACCOUNT_TICKET_REQUIRED = 1650
    """_No description given by bungie._ """
    DESTINY_SHARD_RELAY_CLIENT_TIMEOUT = 1651
    """_No description given by bungie._ """
    DESTINY_SHARD_RELAY_PROXY_TIMEOUT = 1652
    """_No description given by bungie._ """
    DESTINY_P_G_C_R_NOT_FOUND = 1653
    """_No description given by bungie._ """
    DESTINY_ACCOUNT_MUST_BE_OFFLINE = 1654
    """_No description given by bungie._ """
    DESTINY_CAN_ONLY_EQUIP_IN_GAME = 1655
    """_No description given by bungie._ """
    DESTINY_CANNOT_PERFORM_ACTION_ON_EQUIPPED_ITEM = 1656
    """_No description given by bungie._ """
    DESTINY_QUEST_ALREADY_COMPLETED = 1657
    """_No description given by bungie._ """
    DESTINY_QUEST_ALREADY_TRACKED = 1658
    """_No description given by bungie._ """
    DESTINY_TRACKABLE_QUESTS_FULL = 1659
    """_No description given by bungie._ """
    DESTINY_ITEM_NOT_TRANSFERRABLE = 1660
    """_No description given by bungie._ """
    DESTINY_VENDOR_PURCHASE_NOT_ALLOWED = 1661
    """_No description given by bungie._ """
    DESTINY_CONTENT_VERSION_MISMATCH = 1662
    """_No description given by bungie._ """
    DESTINY_ITEM_ACTION_FORBIDDEN = 1663
    """_No description given by bungie._ """
    DESTINY_REFUND_INVALID = 1664
    """_No description given by bungie._ """
    DESTINY_PRIVACY_RESTRICTION = 1665
    """_No description given by bungie._ """
    DESTINY_ACTION_INSUFFICIENT_PRIVILEGES = 1666
    """_No description given by bungie._ """
    DESTINY_INVALID_CLAIM_EXCEPTION = 1667
    """_No description given by bungie._ """
    DESTINY_LEGACY_PLATFORM_RESTRICTED = 1668
    """_No description given by bungie._ """
    DESTINY_LEGACY_PLATFORM_IN_USE = 1669
    """_No description given by bungie._ """
    DESTINY_LEGACY_PLATFORM_INACCESSIBLE = 1670
    """_No description given by bungie._ """
    DESTINY_CANNOT_PERFORM_ACTION_AT_THIS_LOCATION = 1671
    """_No description given by bungie._ """
    DESTINY_THROTTLED_BY_GAME_SERVER = 1672
    """_No description given by bungie._ """
    DESTINY_ITEM_NOT_TRANSFERRABLE_HAS_SIDE_EFFECTS = 1673
    """_No description given by bungie._ """
    DESTINY_ITEM_LOCKED = 1674
    """_No description given by bungie._ """
    DESTINY_CANNOT_AFFORD_MATERIAL_REQUIREMENTS = 1675
    """_No description given by bungie._ """
    DESTINY_FAILED_PLUG_INSERTION_RULES = 1676
    """_No description given by bungie._ """
    DESTINY_SOCKET_NOT_FOUND = 1677
    """_No description given by bungie._ """
    DESTINY_SOCKET_ACTION_NOT_ALLOWED = 1678
    """_No description given by bungie._ """
    DESTINY_SOCKET_ALREADY_HAS_PLUG = 1679
    """_No description given by bungie._ """
    DESTINY_PLUG_ITEM_NOT_AVAILABLE = 1680
    """_No description given by bungie._ """
    DESTINY_CHARACTER_LOGGED_IN_NOT_ALLOWED = 1681
    """_No description given by bungie._ """
    DESTINY_PUBLIC_ACCOUNT_NOT_ACCESSIBLE = 1682
    """_No description given by bungie._ """
    DESTINY_CLAIMS_ITEM_ALREADY_CLAIMED = 1683
    """_No description given by bungie._ """
    DESTINY_CLAIMS_NO_INVENTORY_SPACE = 1684
    """_No description given by bungie._ """
    DESTINY_CLAIMS_REQUIRED_LEVEL_NOT_MET = 1685
    """_No description given by bungie._ """
    DESTINY_CLAIMS_INVALID_STATE = 1686
    """_No description given by bungie._ """
    DESTINY_NOT_ENOUGH_ROOM_FOR_MULTIPLE_REWARDS = 1687
    """_No description given by bungie._ """
    DESTINY_DIRECT_BABEL_CLIENT_TIMEOUT = 1688
    """_No description given by bungie._ """
    FB_INVALID_REQUEST = 1800
    """_No description given by bungie._ """
    FB_REDIRECT_MISMATCH = 1801
    """_No description given by bungie._ """
    FB_ACCESS_DENIED = 1802
    """_No description given by bungie._ """
    FB_UNSUPPORTED_RESPONSE_TYPE = 1803
    """_No description given by bungie._ """
    FB_INVALID_SCOPE = 1804
    """_No description given by bungie._ """
    FB_UNSUPPORTED_GRANT_TYPE = 1805
    """_No description given by bungie._ """
    FB_INVALID_GRANT = 1806
    """_No description given by bungie._ """
    INVITATION_EXPIRED = 1900
    """_No description given by bungie._ """
    INVITATION_UNKNOWN_TYPE = 1901
    """_No description given by bungie._ """
    INVITATION_INVALID_RESPONSE_STATUS = 1902
    """_No description given by bungie._ """
    INVITATION_INVALID_TYPE = 1903
    """_No description given by bungie._ """
    INVITATION_ALREADY_PENDING = 1904
    """_No description given by bungie._ """
    INVITATION_INSUFFICIENT_PERMISSION = 1905
    """_No description given by bungie._ """
    INVITATION_INVALID_CODE = 1906
    """_No description given by bungie._ """
    INVITATION_INVALID_TARGET_STATE = 1907
    """_No description given by bungie._ """
    INVITATION_CANNOT_BE_REACTIVATED = 1908
    """_No description given by bungie._ """
    INVITATION_NO_RECIPIENTS = 1910
    """_No description given by bungie._ """
    INVITATION_GROUP_CANNOT_SEND_TO_SELF = 1911
    """_No description given by bungie._ """
    INVITATION_TOO_MANY_RECIPIENTS = 1912
    """_No description given by bungie._ """
    INVITATION_INVALID = 1913
    """_No description given by bungie._ """
    INVITATION_NOT_FOUND = 1914
    """_No description given by bungie._ """
    TOKEN_INVALID = 2000
    """_No description given by bungie._ """
    TOKEN_BAD_FORMAT = 2001
    """_No description given by bungie._ """
    TOKEN_ALREADY_CLAIMED = 2002
    """_No description given by bungie._ """
    TOKEN_ALREADY_CLAIMED_SELF = 2003
    """_No description given by bungie._ """
    TOKEN_THROTTLING = 2004
    """_No description given by bungie._ """
    TOKEN_UNKNOWN_REDEMPTION_FAILURE = 2005
    """_No description given by bungie._ """
    TOKEN_PURCHASE_CLAIM_FAILED_AFTER_TOKEN_CLAIMED = 2006
    """_No description given by bungie._ """
    TOKEN_USER_ALREADY_OWNS_OFFER = 2007
    """_No description given by bungie._ """
    TOKEN_INVALID_OFFER_KEY = 2008
    """_No description given by bungie._ """
    TOKEN_EMAIL_NOT_VALIDATED = 2009
    """_No description given by bungie._ """
    TOKEN_PROVISIONING_BAD_VENDOR_OR_OFFER = 2010
    """_No description given by bungie._ """
    TOKEN_PURCHASE_HISTORY_UNKNOWN_ERROR = 2011
    """_No description given by bungie._ """
    TOKEN_THROTTLE_STATE_UNKNOWN_ERROR = 2012
    """_No description given by bungie._ """
    TOKEN_USER_AGE_NOT_VERIFIED = 2013
    """_No description given by bungie._ """
    TOKEN_EXCEEDED_OFFER_MAXIMUM = 2014
    """_No description given by bungie._ """
    TOKEN_NO_AVAILABLE_UNLOCKS = 2015
    """_No description given by bungie._ """
    TOKEN_MARKETPLACE_INVALID_PLATFORM = 2016
    """_No description given by bungie._ """
    TOKEN_NO_MARKETPLACE_CODES_FOUND = 2017
    """_No description given by bungie._ """
    TOKEN_OFFER_NOT_AVAILABLE_FOR_REDEMPTION = 2018
    """_No description given by bungie._ """
    TOKEN_UNLOCK_PARTIAL_FAILURE = 2019
    """_No description given by bungie._ """
    TOKEN_MARKETPLACE_INVALID_REGION = 2020
    """_No description given by bungie._ """
    TOKEN_OFFER_EXPIRED = 2021
    """_No description given by bungie._ """
    R_A_F_EXCEEDED_MAXIMUM_REFERRALS = 2022
    """_No description given by bungie._ """
    R_A_F_DUPLICATE_BOND = 2023
    """_No description given by bungie._ """
    R_A_F_NO_VALID_VETERAN_DESTINY_MEMBERSHIPS_FOUND = 2024
    """_No description given by bungie._ """
    R_A_F_NOT_A_VALID_VETERAN_USER = 2025
    """_No description given by bungie._ """
    R_A_F_CODE_ALREADY_CLAIMED_OR_NOT_FOUND = 2026
    """_No description given by bungie._ """
    R_A_F_MISMATCHED_DESTINY_MEMBERSHIP_TYPE = 2027
    """_No description given by bungie._ """
    R_A_F_UNABLE_TO_ACCESS_PURCHASE_HISTORY = 2028
    """_No description given by bungie._ """
    R_A_F_UNABLE_TO_CREATE_BOND = 2029
    """_No description given by bungie._ """
    R_A_F_UNABLE_TO_FIND_BOND = 2030
    """_No description given by bungie._ """
    R_A_F_UNABLE_TO_REMOVE_BOND = 2031
    """_No description given by bungie._ """
    R_A_F_CANNOT_BOND_TO_SELF = 2032
    """_No description given by bungie._ """
    R_A_F_INVALID_PLATFORM = 2033
    """_No description given by bungie._ """
    R_A_F_GENERATE_THROTTLED = 2034
    """_No description given by bungie._ """
    R_A_F_UNABLE_TO_CREATE_BOND_VERSION_MISMATCH = 2035
    """_No description given by bungie._ """
    R_A_F_UNABLE_TO_REMOVE_BOND_VERSION_MISMATCH = 2036
    """_No description given by bungie._ """
    R_A_F_REDEEM_THROTTLED = 2037
    """_No description given by bungie._ """
    NO_AVAILABLE_DISCOUNT_CODE = 2038
    """_No description given by bungie._ """
    DISCOUNT_ALREADY_CLAIMED = 2039
    """_No description given by bungie._ """
    DISCOUNT_CLAIM_FAILURE = 2040
    """_No description given by bungie._ """
    DISCOUNT_CONFIGURATION_FAILURE = 2041
    """_No description given by bungie._ """
    DISCOUNT_GENERATION_FAILURE = 2042
    """_No description given by bungie._ """
    DISCOUNT_ALREADY_EXISTS = 2043
    """_No description given by bungie._ """
    TOKEN_REQUIRES_CREDENTIAL_XUID = 2044
    """_No description given by bungie._ """
    TOKEN_REQUIRES_CREDENTIAL_PSNID = 2045
    """_No description given by bungie._ """
    OFFER_REQUIRED = 2046
    """_No description given by bungie._ """
    UNKNOWN_EVERVERSE_HISTORY_ERROR = 2047
    """_No description given by bungie._ """
    MISSING_EVERVERSE_HISTORY_ERROR = 2048
    """_No description given by bungie._ """
    BUNGIE_REWARD_EMAIL_STATE_INVALID = 2049
    """_No description given by bungie._ """
    BUNGIE_REWARD_NOT_YET_CLAIMABLE = 2050
    """_No description given by bungie._ """
    MISSING_OFFER_CONFIG = 2051
    """_No description given by bungie._ """
    R_A_F_QUEST_ENTITLEMENT_REQUIRES_BNET = 2052
    """_No description given by bungie._ """
    R_A_F_QUEST_ENTITLEMENT_TRANSPORT_FAILURE = 2053
    """_No description given by bungie._ """
    R_A_F_QUEST_ENTITLEMENT_UNKNOWN_FAILURE = 2054
    """_No description given by bungie._ """
    R_A_F_VETERAN_REWARD_UNKNOWN_FAILURE = 2055
    """_No description given by bungie._ """
    R_A_F_TOO_EARLY_TO_CANCEL_BOND = 2056
    """_No description given by bungie._ """
    LOYALTY_REWARD_ALREADY_REDEEMED = 2057
    """_No description given by bungie._ """
    UNCLAIMED_LOYALTY_REWARD_ENTRY_NOT_FOUND = 2058
    """_No description given by bungie._ """
    PARTNER_OFFER_PARTIAL_FAILURE = 2059
    """_No description given by bungie._ """
    PARTNER_OFFER_ALREADY_CLAIMED = 2060
    """_No description given by bungie._ """
    PARTNER_OFFER_SKU_NOT_FOUND = 2061
    """_No description given by bungie._ """
    PARTNER_OFFER_SKU_EXPIRED = 2062
    """_No description given by bungie._ """
    PARTNER_OFFER_PERMISSION_FAILURE = 2063
    """_No description given by bungie._ """
    PARTNER_OFFER_NO_DESTINY_ACCOUNT = 2064
    """_No description given by bungie._ """
    PARTNER_OFFER_APPLY_DATA_NOT_FOUND = 2065
    """_No description given by bungie._ """
    API_EXCEEDED_MAX_KEYS = 2100
    """_No description given by bungie._ """
    API_INVALID_OR_EXPIRED_KEY = 2101
    """_No description given by bungie._ """
    API_KEY_MISSING_FROM_REQUEST = 2102
    """_No description given by bungie._ """
    APPLICATION_DISABLED = 2103
    """_No description given by bungie._ """
    APPLICATION_EXCEEDED_MAX = 2104
    """_No description given by bungie._ """
    APPLICATION_DISALLOWED_BY_SCOPE = 2105
    """_No description given by bungie._ """
    AUTHORIZATION_CODE_INVALID = 2106
    """_No description given by bungie._ """
    ORIGIN_HEADER_DOES_NOT_MATCH_KEY = 2107
    """_No description given by bungie._ """
    ACCESS_NOT_PERMITTED_BY_APPLICATION_SCOPE = 2108
    """_No description given by bungie._ """
    APPLICATION_NAME_IS_TAKEN = 2109
    """_No description given by bungie._ """
    REFRESH_TOKEN_NOT_YET_VALID = 2110
    """_No description given by bungie._ """
    ACCESS_TOKEN_HAS_EXPIRED = 2111
    """_No description given by bungie._ """
    APPLICATION_TOKEN_FORMAT_NOT_VALID = 2112
    """_No description given by bungie._ """
    APPLICATION_NOT_CONFIGURED_FOR_BUNGIE_AUTH = 2113
    """_No description given by bungie._ """
    APPLICATION_NOT_CONFIGURED_FOR_O_AUTH = 2114
    """_No description given by bungie._ """
    O_AUTH_ACCESS_TOKEN_EXPIRED = 2115
    """_No description given by bungie._ """
    APPLICATION_TOKEN_KEY_ID_DOES_NOT_EXIST = 2116
    """_No description given by bungie._ """
    PROVIDED_TOKEN_NOT_VALID_REFRESH_TOKEN = 2117
    """_No description given by bungie._ """
    REFRESH_TOKEN_EXPIRED = 2118
    """_No description given by bungie._ """
    AUTHORIZATION_RECORD_INVALID = 2119
    """_No description given by bungie._ """
    TOKEN_PREVIOUSLY_REVOKED = 2120
    """_No description given by bungie._ """
    TOKEN_INVALID_MEMBERSHIP = 2121
    """_No description given by bungie._ """
    AUTHORIZATION_CODE_STALE = 2122
    """_No description given by bungie._ """
    AUTHORIZATION_RECORD_EXPIRED = 2123
    """_No description given by bungie._ """
    AUTHORIZATION_RECORD_REVOKED = 2124
    """_No description given by bungie._ """
    AUTHORIZATION_RECORD_INACTIVE_API_KEY = 2125
    """_No description given by bungie._ """
    AUTHORIZATION_RECORD_API_KEY_MATCHING = 2126
    """_No description given by bungie._ """
    PARTNERSHIP_INVALID_TYPE = 2200
    """_No description given by bungie._ """
    PARTNERSHIP_VALIDATION_ERROR = 2201
    """_No description given by bungie._ """
    PARTNERSHIP_VALIDATION_TIMEOUT = 2202
    """_No description given by bungie._ """
    PARTNERSHIP_ACCESS_FAILURE = 2203
    """_No description given by bungie._ """
    PARTNERSHIP_ACCOUNT_INVALID = 2204
    """_No description given by bungie._ """
    PARTNERSHIP_GET_ACCOUNT_INFO_FAILURE = 2205
    """_No description given by bungie._ """
    PARTNERSHIP_DISABLED = 2206
    """_No description given by bungie._ """
    PARTNERSHIP_ALREADY_EXISTS = 2207
    """_No description given by bungie._ """
    COMMUNITY_STREAMING_UNAVAILABLE = 2300
    """_No description given by bungie._ """
    TWITCH_NOT_LINKED = 2500
    """_No description given by bungie._ """
    TWITCH_ACCOUNT_NOT_FOUND = 2501
    """_No description given by bungie._ """
    TWITCH_COULD_NOT_LOAD_DESTINY_INFO = 2502
    """_No description given by bungie._ """
    TWITCH_COULD_NOT_REGISTER_USER = 2503
    """_No description given by bungie._ """
    TWITCH_COULD_NOT_UNREGISTER_USER = 2504
    """_No description given by bungie._ """
    TWITCH_REQUIRES_RELINKING = 2505
    """_No description given by bungie._ """
    TWITCH_NO_PLATFORM_CHOSEN = 2506
    """_No description given by bungie._ """
    TWITCH_DROP_HISTORY_PERMISSION_FAILURE = 2507
    """_No description given by bungie._ """
    TWITCH_DROPS_REPAIR_PARTIAL_FAILURE = 2508
    """_No description given by bungie._ """
    TWITCH_NOT_AUTHORIZED = 2509
    """_No description given by bungie._ """
    TWITCH_UNKNOWN_AUTHORIZATION_FAILURE = 2510
    """_No description given by bungie._ """
    TRENDING_CATEGORY_NOT_FOUND = 2600
    """_No description given by bungie._ """
    TRENDING_ENTRY_TYPE_NOT_SUPPORTED = 2601
    """_No description given by bungie._ """
    REPORT_OFFENDER_NOT_IN_PGCR = 2700
    """_No description given by bungie._ """
    REPORT_REQUESTOR_NOT_IN_PGCR = 2701
    """_No description given by bungie._ """
    REPORT_SUBMISSION_FAILED = 2702
    """_No description given by bungie._ """
    REPORT_CANNOT_REPORT_SELF = 2703
    """_No description given by bungie._ """
    AWA_TYPE_DISABLED = 2800
    """_No description given by bungie._ """
    AWA_TOO_MANY_PENDING_REQUESTS = 2801
    """_No description given by bungie._ """
    AWA_THE_FEATURE_REQUIRES_A_REGISTERED_DEVICE = 2802
    """_No description given by bungie._ """
    AWA_REQUEST_WAS_UNANSWERED_FOR_TOO_LONG = 2803
    """_No description given by bungie._ """
    AWA_WRITE_REQUEST_MISSING_OR_INVALID_TOKEN = 2804
    """_No description given by bungie._ """
    AWA_WRITE_REQUEST_TOKEN_EXPIRED = 2805
    """_No description given by bungie._ """
    AWA_WRITE_REQUEST_TOKEN_USAGE_LIMIT_REACHED = 2806
    """_No description given by bungie._ """
    STEAM_WEB_API_ERROR = 2900
    """_No description given by bungie._ """
    STEAM_WEB_NULL_RESPONSE_ERROR = 2901
    """_No description given by bungie._ """
    STEAM_ACCOUNT_REQUIRED = 2902
    """_No description given by bungie._ """
    STEAM_NOT_AUTHORIZED = 2903
    """_No description given by bungie._ """
    CLAN_FIRETEAM_NOT_FOUND = 3000
    """_No description given by bungie._ """
    CLAN_FIRETEAM_ADD_NO_ALTERNATES_FOR_IMMEDIATE = 3001
    """_No description given by bungie._ """
    CLAN_FIRETEAM_FULL = 3002
    """_No description given by bungie._ """
    CLAN_FIRETEAM_ALT_FULL = 3003
    """_No description given by bungie._ """
    CLAN_FIRETEAM_BLOCKED = 3004
    """_No description given by bungie._ """
    CLAN_FIRETEAM_PLAYER_ENTRY_NOT_FOUND = 3005
    """_No description given by bungie._ """
    CLAN_FIRETEAM_PERMISSIONS = 3006
    """_No description given by bungie._ """
    CLAN_FIRETEAM_INVALID_PLATFORM = 3007
    """_No description given by bungie._ """
    CLAN_FIRETEAM_CANNOT_ADJUST_SLOT_COUNT = 3008
    """_No description given by bungie._ """
    CLAN_FIRETEAM_INVALID_PLAYER_PLATFORM = 3009
    """_No description given by bungie._ """
    CLAN_FIRETEAM_NOT_READY_FOR_INVITES_NOT_ENOUGH_PLAYERS = 3010
    """_No description given by bungie._ """
    CLAN_FIRETEAM_GAME_INVITES_NOT_SUPPORT_FOR_PLATFORM = 3011
    """_No description given by bungie._ """
    CLAN_FIRETEAM_PLATFORM_INVITE_PREQ_FAILURE = 3012
    """_No description given by bungie._ """
    CLAN_FIRETEAM_INVALID_AUTH_CONTEXT = 3013
    """_No description given by bungie._ """
    CLAN_FIRETEAM_INVALID_AUTH_PROVIDER_PSN = 3014
    """_No description given by bungie._ """
    CLAN_FIRETEAM_PS4_SESSION_FULL = 3015
    """_No description given by bungie._ """
    CLAN_FIRETEAM_INVALID_AUTH_TOKEN = 3016
    """_No description given by bungie._ """
    CLAN_FIRETEAM_SCHEDULED_FIRETEAMS_DISABLED = 3017
    """_No description given by bungie._ """
    CLAN_FIRETEAM_NOT_READY_FOR_INVITES_NOT_SCHEDULED_YET = 3018
    """_No description given by bungie._ """
    CLAN_FIRETEAM_NOT_READY_FOR_INVITES_CLOSED = 3019
    """_No description given by bungie._ """
    CLAN_FIRETEAM_SCHEDULED_FIRETEAMS_REQUIRE_ADMIN_PERMISSIONS = 3020
    """_No description given by bungie._ """
    CLAN_FIRETEAM_NON_PUBLIC_MUST_HAVE_CLAN = 3021
    """_No description given by bungie._ """
    CLAN_FIRETEAM_PUBLIC_CREATION_RESTRICTION = 3022
    """_No description given by bungie._ """
    CLAN_FIRETEAM_ALREADY_JOINED = 3023
    """_No description given by bungie._ """
    CLAN_FIRETEAM_SCHEDULED_FIRETEAMS_RANGE = 3024
    """_No description given by bungie._ """
    CLAN_FIRETEAM_PUBLIC_CREATION_RESTRICTION_EXTENDED = 3025
    """_No description given by bungie._ """
    CLAN_FIRETEAM_EXPIRED = 3026
    """_No description given by bungie._ """
    CLAN_FIRETEAM_INVALID_AUTH_PROVIDER = 3027
    """_No description given by bungie._ """
    CLAN_FIRETEAM_INVALID_AUTH_PROVIDER_XUID = 3028
    """_No description given by bungie._ """
    CLAN_FIRETEAM_THROTTLE = 3029
    """_No description given by bungie._ """
    CLAN_FIRETEAM_TOO_MANY_OPEN_SCHEDULED_FIRETEAMS = 3030
    """_No description given by bungie._ """
    CLAN_FIRETEAM_CANNOT_REOPEN_SCHEDULED_FIRETEAMS = 3031
    """_No description given by bungie._ """
    CLAN_FIRETEAM_JOIN_NO_ACCOUNT_SPECIFIED = 3032
    """_No description given by bungie._ """
    CLAN_FIRETEAM_MIN_DESTINY2_PROGRESS_FOR_CREATION = 3033
    """_No description given by bungie._ """
    CLAN_FIRETEAM_MIN_DESTINY2_PROGRESS_FOR_JOIN = 3034
    """_No description given by bungie._ """
    CLAN_FIRETEAM_S_M_S_OR_PURCHASE_REQUIRED_CREATE = 3035
    """_No description given by bungie._ """
    CLAN_FIRETEAM_PURCHASE_REQUIRED_CREATE = 3036
    """_No description given by bungie._ """
    CLAN_FIRETEAM_S_M_S_OR_PURCHASE_REQUIRED_JOIN = 3037
    """_No description given by bungie._ """
    CLAN_FIRETEAM_PURCHASE_REQUIRED_JOIN = 3038
    """_No description given by bungie._ """
    FIRETEAM_FINDER_INVALID_MEMBERSHIP_TYPE = 3100
    """_No description given by bungie._ """
    FIRETEAM_FINDER_INVALID_MEMBERSHIP_ID = 3101
    """_No description given by bungie._ """
    FIRETEAM_FINDER_INVALID_CHARACTER_ID = 3102
    """_No description given by bungie._ """
    FIRETEAM_FINDER_INVALID_LISTING_OPTIONS = 3103
    """_No description given by bungie._ """
    FIRETEAM_FINDER_INVALID_REQUEST_DATA = 3104
    """_No description given by bungie._ """
    FIRETEAM_FINDER_LISTING_APPLICATION_FAILED = 3105
    """_No description given by bungie._ """
    FIRETEAM_FINDER_LISTING_AUTO_JOIN_FAILED = 3106
    """_No description given by bungie._ """
    FIRETEAM_FINDER_PLAYER_APPLICATIONS_PARSING_FAILED = 3107
    """_No description given by bungie._ """
    FIRETEAM_FINDER_JOIN_LOBBY_HOST_FAILED = 3108
    """_No description given by bungie._ """
    FIRETEAM_FINDER_PLAYER_NOT_IN_GAME = 3109
    """_No description given by bungie._ """
    FIRETEAM_FINDER_ACTIVATION_FAILED = 3110
    """_No description given by bungie._ """
    FIRETEAM_FINDER_APPLICATION_NOT_FOUND = 3111
    """_No description given by bungie._ """
    FIRETEAM_FINDER_USER_ALREADY_APPLIED_TO_LISTING = 3112
    """_No description given by bungie._ """
    FIRETEAM_FINDER_APPLICATION_CLOSED_FOR_UPDATES = 3113
    """_No description given by bungie._ """
    FIRETEAM_FINDER_LISTING_AT_MAX_OPEN_APPLICATIONS_LIMIT = 3114
    """_No description given by bungie._ """
    FIRETEAM_FINDER_USER_NOT_IN_APPLICATION = 3115
    """_No description given by bungie._ """
    FIRETEAM_FINDER_APPLICATION_USER_ALREADY_LISTING_OWNER = 3116
    """_No description given by bungie._ """
    FIRETEAM_FINDER_OFFER_NOT_FOUND = 3117
    """_No description given by bungie._ """
    FIRETEAM_FINDER_OFFER_CLOSED_FOR_UPDATES = 3118
    """_No description given by bungie._ """
    FIRETEAM_FINDER_OFFER_USER_NOT_TARGET = 3119
    """_No description given by bungie._ """
    FIRETEAM_FINDER_LOBBY_NOT_FOUND = 3120
    """_No description given by bungie._ """
    FIRETEAM_FINDER_LISTING_NOT_FOUND = 3121
    """_No description given by bungie._ """
    FIRETEAM_FINDER_LOBBY_FULL = 3122
    """_No description given by bungie._ """
    FIRETEAM_FINDER_USER_NOT_LISTING_OWNER = 3123
    """_No description given by bungie._ """
    FIRETEAM_FINDER_USER_NOT_LOBBY_OWNER = 3124
    """_No description given by bungie._ """
    FIRETEAM_FINDER_LOBBY_CLOSED_FOR_UPDATES = 3125
    """_No description given by bungie._ """
    FIRETEAM_FINDER_USER_NOT_IN_LOBBY = 3126
    """_No description given by bungie._ """
    FIRETEAM_FINDER_DISABLED_SETTINGS_VALUE = 3127
    """_No description given by bungie._ """
    FIRETEAM_FINDER_OWNER_IN_ACTIVE_LOBBY = 3128
    """_No description given by bungie._ """
    FIRETEAM_FINDER_APPLICATION_CLOSED_TO_OFFLINE_PLAYERS = 3129
    """_No description given by bungie._ """
    FIRETEAM_FINDER_USER_NOT_APPLICATION_OWNER = 3130
    """_No description given by bungie._ """
    FIRETEAM_FINDER_INVITE_VALIDATION_FAILED = 3131
    """_No description given by bungie._ """
    FIRETEAM_FINDER_OWNER_NOT_IN_GAME = 3132
    """_No description given by bungie._ """
    FIRETEAM_FINDER_PLAYER_AT_MAX_LOBBY_LIMIT = 3133
    """_No description given by bungie._ """
    FIRETEAM_FINDER_LOBBY_TOO_FAR_IN_THE_FUTURE = 3134
    """_No description given by bungie._ """
    FIRETEAM_FINDER_RESPONSE_UNDEFINED = 3150
    """_No description given by bungie._ """
    FIRETEAM_FINDER_RESPONSE_MOVED = 3151
    """_No description given by bungie._ """
    FIRETEAM_FINDER_RESPONSE_LOGGING_IN = 3152
    """_No description given by bungie._ """
    FIRETEAM_FINDER_RESPONSE_BAD_REQUEST = 3153
    """_No description given by bungie._ """
    FIRETEAM_FINDER_RESPONSE_UNAUTHORIZED = 3154
    """_No description given by bungie._ """
    FIRETEAM_FINDER_RESPONSE_FORBIDDEN = 3155
    """_No description given by bungie._ """
    FIRETEAM_FINDER_RESPONSE_NOT_FOUND = 3156
    """_No description given by bungie._ """
    FIRETEAM_FINDER_INTERNAL_SERVER_ERROR = 3157
    """_No description given by bungie._ """
    FIRETEAM_FINDER_SERVICE_UNAVAILABLE = 3158
    """_No description given by bungie._ """
    FIRETEAM_FINDER_INTERNAL_SERVER_ERROR_NON_FATAL = 3159
    """_No description given by bungie._ """
    CROSS_SAVE_OVERRIDDEN_ACCOUNT_NOT_FOUND = 3200
    """_No description given by bungie._ """
    CROSS_SAVE_TOO_MANY_OVERRIDDEN_PLATFORMS = 3201
    """_No description given by bungie._ """
    CROSS_SAVE_NO_OVERRIDDEN_PLATFORMS = 3202
    """_No description given by bungie._ """
    CROSS_SAVE_PRIMARY_ACCOUNT_NOT_FOUND = 3203
    """_No description given by bungie._ """
    CROSS_SAVE_REQUEST_INVALID = 3204
    """_No description given by bungie._ """
    CROSS_SAVE_BUNGIE_ACCOUNT_VALIDATION_FAILURE = 3206
    """_No description given by bungie._ """
    CROSS_SAVE_OVERRIDDEN_PLATFORM_NOT_ALLOWED = 3207
    """_No description given by bungie._ """
    CROSS_SAVE_THRESHOLD_EXCEEDED = 3208
    """_No description given by bungie._ """
    CROSS_SAVE_INCOMPATIBLE_MEMBERSHIP_TYPE = 3209
    """_No description given by bungie._ """
    CROSS_SAVE_COULD_NOT_FIND_LINKED_ACCOUNT_FOR_MEMBERSHIP_TYPE = 3210
    """_No description given by bungie._ """
    CROSS_SAVE_COULD_NOT_CREATE_DESTINY_PROFILE_FOR_MEMBERSHIP_TYPE = 3211
    """_No description given by bungie._ """
    CROSS_SAVE_ERROR_CREATING_DESTINY_PROFILE_FOR_MEMBERSHIP_TYPE = 3212
    """_No description given by bungie._ """
    CROSS_SAVE_CANNOT_OVERRIDE_SELF = 3213
    """_No description given by bungie._ """
    CROSS_SAVE_RECENT_SILVER_PURCHASE = 3214
    """_No description given by bungie._ """
    CROSS_SAVE_SILVER_BALANCE_NEGATIVE = 3215
    """_No description given by bungie._ """
    CROSS_SAVE_ACCOUNT_NOT_AUTHENTICATED = 3216
    """_No description given by bungie._ """
    ERROR_ONE_ACCOUNT_ALREADY_ACTIVE = 3217
    """_No description given by bungie._ """
    ERROR_ONE_ACCOUNT_DESTINY_RESTRICTION = 3218
    """_No description given by bungie._ """
    CROSS_SAVE_MUST_MIGRATE_TO_STEAM = 3219
    """_No description given by bungie._ """
    CROSS_SAVE_STEAM_ALREADY_PAIRED = 3220
    """_No description given by bungie._ """
    CROSS_SAVE_CANNOT_PAIR_JUST_STEAM_AND_BLIZZARD = 3221
    """_No description given by bungie._ """
    CROSS_SAVE_CANNOT_PAIR_STEAM_ALONE_BEFORE_SHADOWKEEP = 3222
    """_No description given by bungie._ """
    AUTH_VERIFICATION_NOT_LINKED_TO_ACCOUNT = 3300
    """_No description given by bungie._ """
    P_C_MIGRATION_MISSING_BLIZZARD = 3400
    """_No description given by bungie._ """
    P_C_MIGRATION_MISSING_STEAM = 3401
    """_No description given by bungie._ """
    P_C_MIGRATION_INVALID_BLIZZARD = 3402
    """_No description given by bungie._ """
    P_C_MIGRATION_INVALID_STEAM = 3403
    """_No description given by bungie._ """
    P_C_MIGRATION_UNKNOWN_FAILURE = 3404
    """_No description given by bungie._ """
    P_C_MIGRATION_UNKNOWN_EXCEPTION = 3405
    """_No description given by bungie._ """
    P_C_MIGRATION_NOT_LINKED = 3406
    """_No description given by bungie._ """
    P_C_MIGRATION_ACCOUNTS_ALREADY_USED = 3407
    """_No description given by bungie._ """
    P_C_MIGRATION_STEP_FAILED = 3408
    """_No description given by bungie._ """
    P_C_MIGRATION_INVALID_BLIZZARD_CROSS_SAVE_STATE = 3409
    """_No description given by bungie._ """
    P_C_MIGRATION_DESTINATION_BANNED = 3410
    """_No description given by bungie._ """
    P_C_MIGRATION_DESTINY_FAILURE = 3411
    """_No description given by bungie._ """
    P_C_MIGRATION_SILVER_TRANSFER_FAILED = 3412
    """_No description given by bungie._ """
    P_C_MIGRATION_ENTITLEMENT_TRANSFER_FAILED = 3413
    """_No description given by bungie._ """
    P_C_MIGRATION_CANNOT_STOMP_CLAN_FOUNDER = 3414
    """_No description given by bungie._ """
    UNSUPPORTED_BROWSER = 3500
    """_No description given by bungie._ """
    STADIA_ACCOUNT_REQUIRED = 3600
    """_No description given by bungie._ """
    ERROR_PHONE_VALIDATION_TOO_MANY_USES = 3702
    """_No description given by bungie._ """
    ERROR_PHONE_VALIDATION_NO_ASSOCIATED_PHONE = 3703
    """_No description given by bungie._ """
    ERROR_PHONE_VALIDATION_CODE_INVALID = 3705
    """_No description given by bungie._ """
    ERROR_PHONE_VALIDATION_BANNED = 3706
    """_No description given by bungie._ """
    ERROR_PHONE_VALIDATION_CODE_TOO_RECENTLY_SENT = 3707
    """_No description given by bungie._ """
    ERROR_PHONE_VALIDATION_CODE_EXPIRED = 3708
    """_No description given by bungie._ """
    ERROR_PHONE_VALIDATION_INVALID_NUMBER_TYPE = 3709
    """_No description given by bungie._ """
    ERROR_PHONE_VALIDATION_CODE_TOO_RECENTLY_CHECKED = 3710
    """_No description given by bungie._ """
    ERROR_PHONE_VALIDATION_RECENTLY_PLAYED_DESTINY2_ACCOUNT_REQUIRED = 3711
    """_No description given by bungie._ """
    APPLE_PUSH_ERROR_UNKNOWN = 3800
    """_No description given by bungie._ """
    APPLE_PUSH_ERROR_NULL = 3801
    """_No description given by bungie._ """
    APPLE_PUSH_ERROR_TIMEOUT = 3802
    """_No description given by bungie._ """
    APPLE_PUSH_BAD_REQUEST = 3803
    """_No description given by bungie._ """
    APPLE_PUSH_FAILED_AUTH = 3804
    """_No description given by bungie._ """
    APPLE_PUSH_THROTTLED = 3805
    """_No description given by bungie._ """
    APPLE_PUSH_SERVICE_UNAVAILABLE = 3806
    """_No description given by bungie._ """
    NOT_AN_IMAGE_OR_VIDEO = 3807
    """_No description given by bungie._ """
    ERROR_BUNGIE_FRIENDS_BLOCK_FAILED = 3900
    """_No description given by bungie._ """
    ERROR_BUNGIE_FRIENDS_AUTO_REJECT = 3901
    """_No description given by bungie._ """
    ERROR_BUNGIE_FRIENDS_NO_REQUEST_FOUND = 3902
    """_No description given by bungie._ """
    ERROR_BUNGIE_FRIENDS_ALREADY_FRIENDS = 3903
    """_No description given by bungie._ """
    ERROR_BUNGIE_FRIENDS_UNABLE_TO_REMOVE_REQUEST = 3904
    """_No description given by bungie._ """
    ERROR_BUNGIE_FRIENDS_UNABLE_TO_REMOVE = 3905
    """_No description given by bungie._ """
    ERROR_BUNGIE_FRIENDS_IDENTICAL_SOURCE_TARGET = 3906
    """_No description given by bungie._ """
    ERROR_BUNGIE_FRIENDS_SELF = 3907
    """_No description given by bungie._ """
    ERROR_BUNGIE_BLOCK_SELF = 3908
    """_No description given by bungie._ """
    ERROR_BUNGIE_FRIENDS_LIST_FULL = 3910
    """_No description given by bungie._ """
    ERROR_BUNGIE_BLOCK_LIST_FULL = 3911
    """_No description given by bungie._ """
    ERROR_BUNGIE_FRIEND_NOT_FOUND = 3912
    """_No description given by bungie._ """
    ERROR_BUNGIE_FRIEND_INVALID_MEMBERSHIP_TYPE = 3913
    """_No description given by bungie._ """
    ERROR_EGS_UNKNOWN = 4000
    """_No description given by bungie._ """
    ERROR_EGS_BAD_REQUEST = 4001
    """_No description given by bungie._ """
    ERROR_EGS_NOT_AUTHORIZED = 4002
    """_No description given by bungie._ """
    ERROR_EGS_FORBIDDEN = 4003
    """_No description given by bungie._ """
    ERROR_EGS_ACCOUNT_NOT_FOUND = 4004
    """_No description given by bungie._ """
    ERROR_EGS_WEB_EXCEPTION = 4005
    """_No description given by bungie._ """
    ERROR_EGS_UNAVAILABLE = 4006
    """_No description given by bungie._ """
    ERROR_EGS_JWKS_MISSING = 4007
    """_No description given by bungie._ """
    ERROR_EGS_JWT_MALFORMED_HEADER = 4008
    """_No description given by bungie._ """
    ERROR_EGS_JWT_MALFORMED_PAYLOAD = 4009
    """_No description given by bungie._ """
