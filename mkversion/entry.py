import os
import pathlib
import sys
import tempfile
from typing import Dict

from mkdocs.config import config_options
from mkdocs.plugins import BasePlugin


class Entry(BasePlugin):
    config_scheme = (
        ('version', config_options.Type(str)),
        ('default', config_options.Type(str, default="developing")),
    )

    def on_config(self, config: Dict[str, str], **kwargs) -> Dict[str, str]:
        """
        An event that alters the config in order to prepare it for versioning as well as perform various checks.

        Args:
            config (Dict[str, str]): the user config (usually mkdocs.yml)

        Returns:
            [Dict[str, str]]: the altered config
        """
        # extract the version number
        version_num = self.extract_version_num()

        # changing the site name to include the version number
        if 'extra' in config:
            config['extra']["version"] = version_num
        else:
            config['extra'] = { "version": version_num }

        return config

    def extract_version_num(self) -> str:
        """
        extracts the version "number"

        Returns:
            str: returns the version number as a string
        """
        try:
            version_num = self.config['version']
            default_var = self.config.get('default',"developing")
            return os.environ.get(version_num, default_var)
        except KeyError as e:
            print(e)
            print('Warning: ' +
                  'no version detected in mkdocs.yml.You should specify a version number (ideally) according to '
                  'semantic versioning in mkdocs.yml. exiting')
            sys.exit(1)
