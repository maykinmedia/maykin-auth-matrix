

Welcome to maykin-auth-matrix's documentation!
=================================================

:Version: 0.1.1
:Source: https://github.com/maykinmedia/maykin-auth-matrix
:Keywords: ``<keywords>``
:PythonVersion: 3.10

|build-status| |code-quality| |black| |coverage| |docs|

|python-versions| |django-versions| |pypi-version|

DigiD Compliant Authorization Matrix for the administation of Django projects.

.. contents::

.. section-numbering::

Features
========

* Display a matrix of permissions for the groups
* Display a matrix of groups for the users
* Allows to export the matrix in different formats

Installation
============

Install from PyPI with pip:

.. code-block:: bash

    pip install maykin-auth-matrix


Usage
=====

To use this with your project you need to follow these steps:

#. Add ``maykin-auth-matrix`` to ``INSTALLED_APPS`` in
   your Django project's ``settings.py``.:

   .. code-block:: python

      INSTALLED_APPS = (
          "django.contrib.admin",
          ...,
          "maykin-auth-matrix",
      )

   Note that there is no dash in the module name, only underscores.

#. Create the database tables by performing a database migration:

   .. code-block:: console

      $ python manage.py migrate maykin-auth-matrix


Add the URL to your Django project's ``urls.py``:

.. code-block:: python

    from django.contrib import admin
    from django.urls import path, include
    from auth_matrix.views import AuthMatrixView

    urlpatterns = [
        path(
            "admin/authorization/",
            include("auth_matrix.admin_urls"),
        ),
    ]

#. Display the Authorization Matrix

.. image:: images/authorization_matrix.png
    :alt: Authorization Matrix

Navigate to the Groups admin page and click on the "Authorization Matrix" link to view the matrix.

.. image:: images/authorization_button.png
    :alt: Show Authorization Matrix Button

#. Export the Authorization Matrix

On the top right corner of the Groups admin page, you can choose to export the matrix to different formats.

Click the EXPORT button and chose the format you want to export the matrix to.

.. image:: images/export_matrix.png
    :alt: Export Authorization Matrix Button 

You can pick between two resources:
    - UserGroupResource : exports the matrix with users as rows and groups as columns
    - GroupPermissionsResource : exports the matrix with permissions as rows and groups as columns

.. image:: images/export_matrix_format.png
    :alt: Export Authorization Matrix Formats

============
Contributing
============

We have a strong vision about the scope of this package and the "less is more" principle
resonates here. That being said, we will of course greatly appreciate contributions in
any form, such as suggestions, remarks, documentation improvements, bugfixes... If a
contribution does not solve any of our (Maykin) particular needs, it is unlikely to be
accepted.

That said - if you're a Maykin employee, Open Source enthusiast or just a generally
interested person, we have some guidance on how to get started.

Installing the package and "test" application locally
=====================================================

We recommend setting up a virtualenv or similar. You can then install the library for
local development and/or experimenting:

.. code-block:: bash

    pip install -e .[tests,coverage,docs,release]

Due to some Python path details, we also recommend setting some environment variables:

.. code-block:: bash

    # run in the top-level directory - you can also make this part of your virtualenv
    # activation script
    export PYTHONPATH=$(pwd) DJANGO_SETTINGS_MODULE=testapp.settings

The ``PYTHONPATH`` in particular is needed to avoid import errors due to how Python
discovers modules.

Running tests
=============

Running tests for the current environment:

.. code-block:: bash

    pytest

Running tests against all envs:

.. code-block:: bash

    tox

Running a local development server
==================================

You can use the ``django-admin`` script instead of ``manage.py`` as you might be used to
in projects:

.. code-block:: bash

    django-admin check
    django-admin runserver

Alternatively, you can use ``python -m django <command>``.

Code contributions
==================

Code formatting is checked in the CI pipeline. We make use of the following tools:

* black
* isort
* flake8

You are encouraged to set up a pre-commit hook to apply these, but ultimately this is
your choice!

Commit messages
===============

Commit messages contain the "why" of changes - please practice good commit hygiene:

* reference an issue ID when relevant
* use a short summary line and a more elaborate body explaining why things are done a
  certain way, which references are relevant...
* gitmoji is encouraged, which helps with...
* use atomic commits that describe a single change
* feel free to rebase PR feedback back into their "original" commits

.. include:: ../CHANGELOG.rst



.. |build-status| image:: https://github.com/maykinmedia/maykin-auth-matrix/workflows/Run%20CI/badge.svg
    :alt: Build status
    :target: https://github.com/maykinmedia/maykin-auth-matrix/actions?query=workflow%3A%22Run+CI%22

.. |code-quality| image:: https://github.com/maykinmedia/maykin-auth-matrix/workflows/Code%20quality%20checks/badge.svg
     :alt: Code quality checks
     :target: https://github.com/maykinmedia/maykin-auth-matrix/actions?query=workflow%3A%22Code+quality+checks%22

.. |black| image:: https://img.shields.io/badge/code%20style-black-000000.svg
    :target: https://github.com/psf/black

.. |coverage| image:: https://codecov.io/gh/maykinmedia/maykin-auth-matrix/branch/main/graph/badge.svg
    :target: https://codecov.io/gh/maykinmedia/maykin-auth-matrix
    :alt: Coverage status

.. |docs| image:: https://readthedocs.org/projects/maykin-auth-matrix/badge/?version=latest
    :target: https://maykin-auth-matrix.readthedocs.io/en/latest/?badge=latest
    :alt: Documentation Status

.. |python-versions| image:: https://img.shields.io/pypi/pyversions/maykin-auth-matrix.svg

.. |django-versions| image:: https://img.shields.io/pypi/djversions/maykin-auth-matrix.svg

.. |pypi-version| image:: https://img.shields.io/pypi/v/maykin-auth-matrix.svg
    :target: https://pypi.org/project/maykin-auth-matrix/
