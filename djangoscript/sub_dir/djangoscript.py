#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = "Guy-Yann VECTOL"
__credits__ = ["Guy-Yann VECTOL"]
__Lisence__ = "BSD"
__maintainer__ = "Guy-Yann VECTOL"
__email__ = "guyyann.vectol@gmail.com"
__status__ = "Development"
__version__ = "0.0.1"

# Default python packages
import logging
import os
import time


class Djangoscript:
    """Class that allows the developper to use Transcript with ease"""

    def __init__(self, conf_path=os.path.join(os.path.expanduser("~"),
                                              ".work_login.conf")):
        """Saves config file location"""

        self.conf_path = conf_path

    def configure(self):
        """Creates all the required files and folders"""

        # Configures config file if not done so already
        if not os.path.exists(self.conf_path):
            pass
        # Opens a terminal
        os.system("gnome-terminal")
        time.sleep(1)
        with open(self.conf_path, "r") as f:
            for cmd in f:
                self._run_cmd(cmd)

if __name__ == "__main__":
    Djangoscript().configure()
    