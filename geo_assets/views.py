# -*- coding: utf-8 -*-
#
# Copyright (C) 2022 GEO Secretariat.
#
# geo-assets is free software; you can redistribute it and/or modify it under
# the terms of the MIT License; see LICENSE file for more details.

"""GEO Assets views."""

from flask import Blueprint
from flask_babelex import gettext as _

blueprint = Blueprint(
    "geo_assets",
    __name__,
    static_folder="static",
)
