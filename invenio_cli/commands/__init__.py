# SPDX-FileCopyrightText: 2020-2021 CERN.
# SPDX-License-Identifier: MIT

"""Invenio module to ease the creation and management of applications."""

from .assets import AssetsCommands
from .commands import Commands
from .containers import ContainersCommands
from .install import InstallCommands
from .local import LocalCommands
from .packages import PackagesCommands
from .requirements import RequirementsCommands
from .services import ServicesCommands
from .translations import TranslationsCommands
from .upgrade import UpgradeCommands

__all__ = (
    "AssetsCommands",
    "Commands",
    "ContainersCommands",
    "InstallCommands",
    "LocalCommands",
    "PackagesCommands",
    "RequirementsCommands",
    "ServicesCommands",
    "TranslationsCommands",
    "UpgradeCommands",
)
