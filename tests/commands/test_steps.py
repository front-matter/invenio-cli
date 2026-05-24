# SPDX-FileCopyrightText: 2021 CERN.
# SPDX-License-Identifier: MIT

"""Module for step tests."""

from invenio_cli.commands.steps import FunctionStep
from invenio_cli.helpers.process import ProcessResponse


def func():
    return ProcessResponse(error="test", output="test", status_code=1, warning=False)


def test_func_step():
    step = FunctionStep(func=func, args={}, message="")
    response = step.execute()

    assert response.status_code == 1
    assert not response.warning


def test_skip_func_step():
    step = FunctionStep(func=func, args={}, message="", skippable=True)
    response = step.execute()

    assert response.status_code == 0
    assert response.warning
