#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""CheckMK plugin for baker"""
# ~/local/lib/check_mk/base/cee/plugins/bakery/fail2ban.py

from pathlib import Path
from typing import TypedDict

from .bakery_api.v1 import (
    OS,
    Plugin,
    register,
    FileGenerator,
)

class Fail2BanConfig(TypedDict, total=False):
    """_summary_

    Args:
       TypedDict (_type_): _description_
       total (bool, optional): _description_. Defaults to False.
    """
    interval: float

def get_fail2ban_plugin_files(conf: Fail2BanConfig) -> FileGenerator:
    """defintion what to put in agent

    Args:
       conf (Fail2BanConfig): _description_

    Returns:
       FileGenerator: _description_

    Yields:
       Iterator[FileGenerator]: _description_
    """
    interval = conf.get('interval')

    yield Plugin(
      base_os=OS.LINUX,
      source=Path('fail2ban.sh'),
      target=Path('fail2ban.sh'),
      interval = int(interval),
    )

register.bakery_plugin(
      name="fail2ban",
      files_function=get_fail2ban_plugin_files,
)
