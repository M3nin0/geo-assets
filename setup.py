# -*- coding: utf-8 -*-
#
# Copyright (C) 2022 GEO Secretariat.
#
# geo-assets is free software; you can redistribute it and/or modify it under
# the terms of the MIT License; see LICENSE file for more details.

"""GEO Knowledge Hub assets"""

import os

from setuptools import find_packages, setup

readme = open("README.rst").read()
history = open("CHANGES.rst").read()

tests_require = [
    "pytest-mock>=1.6.0",
    "pytest-invenio>=1.4.0",
    "invenio-app>=1.3.1,<2.0.0",
]

extras_require = {
    "docs": [
        "sphinx>=4.2.0,<5",
    ],
    "tests": tests_require,
}

extras_require["all"] = []
for name, reqs in extras_require.items():
    extras_require["all"].extend(reqs)

setup_requires = [
    "Babel>=2.8",
    "pytest-runner>=3.0.0,<5",
]

install_requires = [
    "invenio-i18n>=1.2.0",
]
packages = find_packages()


# Get the version string. Cannot be done with import!
g = {}
with open(os.path.join("geo_assets", "version.py"), "rt") as fp:
    exec(fp.read(), g)
    version = g["__version__"]

setup(
    name="geo-assets",
    version=version,
    description=__doc__,
    long_description=readme + "\n\n" + history,
    keywords="invenio TODO",
    license="MIT",
    author="GEO Secretariat",
    author_email="geokhub@geosec.org",
    url="https://github.com/geo-knowledge-hub/geo-assets",
    packages=packages,
    zip_safe=False,
    include_package_data=True,
    platforms="any",
    entry_points={
        "invenio_base.apps": [
            "geo_assets = geo_assets:GEOAssets",
        ],
        "invenio_config.module": [
            "geo_assets = geo_assets.config",
        ],
        "invenio_base.blueprints": [
            "geo_assets = geo_assets.views:blueprint",
        ],
        "invenio_i18n.translations": [
            "messages = geo_assets",
        ],
        # TODO: Edit these entry points to fit your needs.
        # 'invenio_access.actions': [],
        # 'invenio_admin.actions': [],
        # 'invenio_assets.bundles': [],
        # 'invenio_base.api_apps': [],
        # 'invenio_base.api_blueprints': [],
        # 'invenio_base.blueprints': [],
        # 'invenio_celery.tasks': [],
        # 'invenio_db.models': [],
        # 'invenio_pidstore.minters': [],
        # 'invenio_records.jsonresolver': [],
    },
    extras_require=extras_require,
    install_requires=install_requires,
    setup_requires=setup_requires,
    tests_require=tests_require,
    classifiers=[
        "Environment :: Web Environment",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Topic :: Internet :: WWW/HTTP :: Dynamic Content",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Development Status :: 1 - Planning",
    ],
)
