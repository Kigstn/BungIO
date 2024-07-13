import logging
import os
from importlib.metadata import version as _v

__all__ = ("ROOT_DIR", "BASE_ROUTE", "LOGGER_NAME", "DEFAULT_LOGGER", "__version__", "__repo_url__", "__author__")

ROOT_DIR = os.path.split(os.path.dirname(os.path.abspath(__file__)))[0]
BASE_ROUTE = "https://www.bungie.net/Platform"
LOGGER_NAME = "BungIO"
DEFAULT_LOGGER = logging.getLogger(LOGGER_NAME)
DEFAULT_LOGGER.setLevel(logging.WARNING)

try:
    __version__ = _v("bungio")
except Exception:
    __version__ = "0.0.0"
__repo_url__ = "https://github.com/Kigstn/BungIO"
__author__ = "Kigstn"
