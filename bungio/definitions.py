import logging
import os

ROOT_DIR = os.path.split(os.path.dirname(os.path.abspath(__file__)))[0]
BASE_ROUTE = "https://www.bungie.net/Platform"
LOGGER_NAME = "BungIO"
DEFAULT_LOGGER = logging.getLogger(LOGGER_NAME)
DEFAULT_LOGGER.setLevel(logging.WARNING)
