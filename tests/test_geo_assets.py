# -*- coding: utf-8 -*-
#
# Copyright (C) 2022 GEO Secretariat.
#
# geo-assets is free software; you can redistribute it and/or modify it under
# the terms of the MIT License; see LICENSE file for more details.

"""Module tests."""

from flask import Flask

from geo_assets import GEOAssets


def test_version():
    """Test version import."""
    from geo_assets import __version__

    assert __version__


def test_init():
    """Test extension initialization."""
    app = Flask("testapp")
    ext = GEOAssets(app)
    assert "geo-assets" in app.extensions

    app = Flask("testapp")
    ext = GEOAssets()
    assert "geo-assets" not in app.extensions
    ext.init_app(app)
    assert "geo-assets" in app.extensions
