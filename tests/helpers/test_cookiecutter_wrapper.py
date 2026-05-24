# SPDX-FileCopyrightText: 2019-2020 CERN.
# SPDX-FileCopyrightText: 2019-2020 Northwestern University.
# SPDX-License-Identifier: MIT

"""Module cookiecutter wrapper tests."""

from invenio_cli.helpers.cookiecutter_wrapper import CookiecutterWrapper


def test_constructor():
    cookiecutter = CookiecutterWrapper("RDM", checkout="master")

    assert cookiecutter.tmp_file is None
    assert cookiecutter.flavour == "RDM"
    assert (
        cookiecutter.template
        == "https://github.com/inveniosoftware/cookiecutter-invenio-rdm.git"
    )
    assert cookiecutter.template_name == "cookiecutter-invenio-rdm"
    assert cookiecutter.checkout == "master"


def test_extract_template_name_git_url():
    tpl_name = CookiecutterWrapper.extract_template_name(
        "https://github.com/inveniosoftware/cookiecutter-invenio-rdm.git"
    )

    assert tpl_name == "cookiecutter-invenio-rdm"


def test_extract_template_name_path():
    tpl_name = CookiecutterWrapper.extract_template_name(
        "~/dev/cookiecutter-invenio-rdm/"
    )

    assert tpl_name == "cookiecutter-invenio-rdm"
