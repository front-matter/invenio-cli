# SPDX-FileCopyrightText: 2020 CERN.
# SPDX-FileCopyrightText: 2020 Northwestern University.
# SPDX-License-Identifier: MIT

"""Test environment variables context manager."""

import os

from invenio_cli.helpers.env import env


def test_env():
    """Test environment variables context manager."""
    assert "SERVER_NAME" not in os.environ
    assert "FLASK_DEBUG" not in os.environ

    os.environ["FLASK_DEBUG"] = "1"
    with env(SERVER_NAME="example.com", FLASK_DEBUG="0"):
        assert os.environ["SERVER_NAME"] == "example.com"
        assert os.environ["FLASK_DEBUG"] == "0"

    assert os.environ["FLASK_DEBUG"] == "1"
    assert "SERVER_NAME" not in os.environ
