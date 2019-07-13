#!/usr/bin/python3
# -*- coding: utf-8 -*-

# Theme Catalog
#
# author: Ahmet Cangir
# github: https://github.com/cangir
# license: https://github.com/cangir/theme-catalog/blob/master/LICENSE

from app import manager

# Import Controllers
from app.controllers import auth
from app.controllers import main

# Run manager
if __name__ == "__main__":
    manager.run()
