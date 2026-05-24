# SPDX-FileCopyrightText: 2020 CERN.
# SPDX-FileCopyrightText: 2020 Northwestern University.
# SPDX-License-Identifier: MIT

"""Invenio CLI environment helper."""

import contextlib
import os


@contextlib.contextmanager
def env(**environ):
    """Context manager to temporarily set environment variables.

    :param environ: Environment variables to set
    """
    old = {}
    for k, v in dict(environ).items():
        old[k] = os.environ.get(k, None)
        os.environ[k] = v
    try:
        yield
    finally:
        for k, v in old.items():
            if v is None:
                del os.environ[k]
            else:
                os.environ[k] = v
