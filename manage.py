#!/usr/bin/python3
# -*- coding: utf-8 -*-

# Theme Catalog
#
# author: Ahmet Cangir
# github: https://github.com/cangir
# license: https://github.com/cangir/theme-catalog/blob/master/LICENSE

from app import manager

# Import Models
from app.models.user import User
from app.models.category import Category
from app.models.category import CategoryRelation
from app.models.tag import Tag
from app.models.tag import TagRelation
from app.models.license_type import LicenseType
from app.models.theme import Theme
from app.models.theme_author import ThemeAuthor

# Import Controllers
from app.controllers import auth
from app.controllers import main

# Run manager
if __name__ == "__main__":
    manager.run()
