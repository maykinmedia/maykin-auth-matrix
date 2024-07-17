==========
Quickstart
==========

Requirements
============

This application makes use of the AbstractBaseUser model from django.
Generally, you should be able to use this application with any Django project 
that uses the default User model.
If you are using a custom User model, you will need to make sure that it is 
compatible with the AbstractBaseUser model.
Otherwise you can customize things through the username and email properties on 
your custom user model.

Installation
============

1. Install from PyPI with pip:

   .. code-block:: bash

      pip install maykin-auth-matrix

2. Add ``maykin-auth-matrix`` to ``INSTALLED_APPS`` in
   your Django project's ``settings.py``:

   .. code-block:: python

      INSTALLED_APPS = (
          "django.contrib.admin",
          ...,
          "auth_matrix",
      )

3. Run ``python manage.py migrate`` to create the necessary database tables.

4. Add the URL to your Django project's ``urls.py``:

   .. code-block:: python

      from django.contrib import admin
      from django.urls import path, include

      from auth_matrix.views import AuthMatrixView

      urlpatterns = [
          path(
              "admin/auth_matrix/",
              include(("auth_matrix.admin_urls", "auth_matrix"), namespace="auth_matrix"),
          ),
      ]

Usage
=====

To use this with your project you need to follow these steps:

#. Display the Authorization Matrix

.. image:: images/authorization_matrix.png
    :alt: Authorization Matrix

Navigate to the Groups admin page and click on the "Authorization Matrix" link
to view the matrix.

.. image:: images/authorization_button.png
    :alt: Show Authorization Matrix Button

#. Export the Authorization Matrix

On the top right corner of the Groups admin page, you can choose to export the
matrix to different formats.

Click the EXPORT button and chose the format you want to export the matrix to.

.. image:: images/export_matrix.png
    :alt: Export Authorization Matrix Button 

You can pick between two resources:
    - UserGroupResource : exports the matrix with users as rows and groups as columns
    - GroupPermissionsResource : exports the matrix with permissions as rows and groups as columns

.. image:: images/export_matrix_format.png
    :alt: Export Authorization Matrix Formats