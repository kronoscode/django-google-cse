django-google-cse
============

A reusable Django app that add to your site google custom search

Installation
------------

To get the latest stable release from PyPi

.. code-block:: bash

    pip install django-google-cse

To get the latest commit from GitHub

.. code-block:: bash

    pip install -e git+git://https://github.com/kronoscode/django-google-cse.git#egg=google_cse

TODO: Describe further installation steps (edit / remove the examples below):

Add ``google_cse`` to your ``INSTALLED_APPS``

.. code-block:: python

    INSTALLED_APPS = (
        ...,
        'google_cse',
    )

Add the ``google_cse`` URLs to your ``urls.py``

.. code-block:: python

    urlpatterns = patterns('',
        ...
        url(r'^search/', include('google_cse.urls')),
    )

Before your tags/filters are available in your templates, load them by using

.. code-block:: html

	{% load google_cse_tags %}


Don't forget to migrate your database

.. code-block:: bash

    ./manage.py migrate google_cse


Usage
-----

TODO: Describe usage or point to docs. Also describe available settings and
templatetags.


Contribute
----------

If you want to contribute to this project, please perform the following steps

.. code-block:: bash

    # Fork this repository
    # Clone your fork
    mkvirtualenv -p python2.7 django-google-cse
    make develop

    git co -b feature_branch master
    # Implement your feature and tests
    git add . && git commit
    git push -u origin feature_branch
    # Send us a pull request for your feature branch

In order to run the tests, simply execute ``tox``. This will install two new
environments (for Django 1.6 and Django 1.7) and run the tests against both
environments.
