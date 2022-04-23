..
    Copyright (C) 2022 GEO Secretariat.

    geo-assets is free software; you can redistribute it and/or modify it
    under the terms of the MIT License; see LICENSE file for more details.

===========
 GEO Assets
===========

.. .. image:: https://img.shields.io/pypi/dm/geo-assets.svg
..         :target: https://pypi.python.org/pypi/geo-assets

.. .. image:: https://readthedocs.org/projects/geo-assets/badge/?version=latest
..         :target: https://geo-assets.readthedocs.io/en/latest/
..         :alt: Documentation Status

.. image:: https://github.com/geo-knowledge-hub/geo-assets/workflows/CI/badge.svg
        :target: https://github.com/geo-knowledge-hub/geo-assets/actions?query=workflow%3ACI

.. image:: https://img.shields.io/badge/code%20style-black-000000.svg
   :target: https://github.com/psf/black

.. image:: https://img.shields.io/badge/lifecycle-maturing-blue.svg
        :target: https://www.tidyverse.org/lifecycle/#maturing
        :alt: Software Life Cycle

.. image:: https://img.shields.io/github/license/geo-knowledge-hub/geo-assets.svg
        :target: https://github.com/geo-knowledge-hub/geo-assets/blob/master/LICENSE

.. image:: https://img.shields.io/github/tag/geo-knowledge-hub/geo-assets.svg
        :target: https://github.com/geo-knowledge-hub/geo-assets/releases

.. image:: https://img.shields.io/discord/730739436551143514?logo=discord&logoColor=ffffff&color=7389D8
        :target: https://discord.com/channels/730739436551143514#
        :alt: Join us at Discord

Custom assets for the GEO Knowledge Hub.

Development
===========

Install
-------

Install the package with the `docs` dependencies:

.. code-block:: console

    pip install -e .[docs]


Tests
-----

After installing the package and its dependencies, if you want to test the code, install the `tests` dependencies:

.. code-block:: console

    pip install -e .[tests]

Now, you can run the tests:

.. code-block:: console

    ./run-tests.sh
