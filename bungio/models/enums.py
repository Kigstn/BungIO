from enum import Enum

__all__ = ("BungieLanguage",)


class BungieLanguage(Enum):
    """
    Set your preferred language. This will impact the language of the manifest
    """

    ENGLISH = "en"
    FRENCH = "fr"
    SPANISH = "es"
    MEXICAN = "es-mx"
    GERMAN = "de"
    ITALIAN = "it"
    JAPANESE = "ja"
    PORTUGUESE = "pt-br"
    RUSSIAN = "ru"
    POLISH = "pl"
    KOREAN = "ko"
    CHINESE_TRADITIONAL = "zh-cht"
    CHINESE_SIMPLIFIED = "zh-chs"
