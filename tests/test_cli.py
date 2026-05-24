# SPDX-FileCopyrightText: 2020 CERN.
# SPDX-FileCopyrightText: 2020 Northwestern University.
# SPDX-License-Identifier: MIT

"""Pytest fixtures."""

from os.path import exists

import pytest
from click.testing import CliRunner

from invenio_cli.cli import cli


@pytest.fixture()
def runner():
    """Click CLI runner."""
    runner = CliRunner()
    with runner.isolated_filesystem():
        yield runner


@pytest.mark.skip()
def test_init(runner):
    """Test init command."""
    result = runner.invoke(cli, ["init"])
    assert result.exit_code == 0
    assert exists("my-site")
    assert exists("my-site/.invenio")


@pytest.mark.skip()
def test_init_with_arg(runner):
    """Test init command."""
    result = runner.invoke(cli, ["init", "rdm"])
    assert result.exit_code == 0
    assert exists("my-site")
    assert exists("my-site/.invenio")
