#!/usr/bin/python3
# -*- coding: utf-8 -*-

# author: Ahmet Cangir
# github: https://github.com/cangir
# license: https://github.com/cangir/theme-catalog/blob/master/LICENSE

import os
from flask import Flask, session
from flask_sqlalchemy import SQLAlchemy
from flask_script import Manager, Server
from flask_login import LoginManager
from config import Config
from flaskext.markdown import Markdown
from flask_debugtoolbar import DebugToolbarExtension

app = Flask(__name__, template_folder="views")

# Load Config Class
app.config.from_object(Config)

app.debug = app.config['DEBUG']

# Strip whitespaces in Jinja Templates
app.jinja_env.trim_blocks = True
app.jinja_env.lstrip_blocks = True

# Define upload folder
app.config['UPLOAD_FOLDER'] = os.path.join(
    app.config['BASE_DIR'],
    app.config['UPLOAD_FOLDER_PATH']
)

# Load login manager
login_manager = LoginManager(app)
login_manager.login_view = "login"

manager = Manager(app)
manager.add_command("runserver", Server(
    host=app.config['HOST'],
    port=app.config['PORT'])
)

md = Markdown(app)

db = SQLAlchemy(app)

# Debug Toolbar
# toolbar = DebugToolbarExtension(app)
