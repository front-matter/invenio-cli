# SPDX-FileCopyrightText: 2020 CERN.
# SPDX-License-Identifier: MIT

"""Invenio module to ease the creation and management of applications."""

import click


class InvenioCLIConfigError(click.UsageError):
    """Exception when reading/writing from the configuration file."""
