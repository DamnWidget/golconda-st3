import yaml

from os import path
from os import environ as env
from os import name as os_name

import logging
import logging.config

import sublime

from libconda.settings import get

from .lib.capabilities import Capabilities
from .lib.plugins import ConflictingPlugins

with open(path.join(path.dirname(__file__), 'logging.yml', 'r')) as cfg_file:
    logging.config.dictConfig(yaml.load(cfg_file))

logger = logging.getLogger(__name__)


def plugin_loaded() -> None:
    """Called by Sublime Text 3 on plugin load
    """

    Capabilities.detect()
    ConflictingPlugins.detect()


def plugin_unloaded() -> None:
    """Called by Sublime Text 3 on plugin unload
    """


def construct_handler_by_os(loader, node):
    """Return back the right handler for DEBUG logging log level
    """

    return ['syslog'] if os_name == 'posix' else ['ntlog']
