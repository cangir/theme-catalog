#!/usr/bin/python3
import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_script import Manager, Server
from flask_login import LoginManager
from config import Config

app = Flask(__name__, template_folder="views")

# Load Config Class
app.config.from_object(Config)

# Strip whitespaces in Jinja Templates
app.jinja_env.trim_blocks = True
app.jinja_env.lstrip_blocks = True

# Define upload folder
app.config['UPLOAD_FOLDER'] = os.path.join(
    app.config['BASE_DIR'], app.config['UPLOAD_FOLDER_PATH'])

# Load login manager
login_manager = LoginManager(app)
login_manager.login_view = "login"

manager = Manager(app)
manager.add_command("runserver", Server(
    host=app.config['HOST'], port=app.config['PORT']))

db = SQLAlchemy(app)

from app.models.user import User  # noqa: E402
from app.models.theme import Category, CategoryRelation  # noqa: E402
from app.models.theme import Tag, TagRelation  # noqa: E402
from app.models.theme import LicenseType  # noqa: E402
from app.models.theme import Theme  # noqa: E402
from app.models.theme import ThemeAuthor  # noqa: E402

# import Controllers
from app.controllers import auth  # noqa: E402
from app.controllers import main  # noqa: E402

db.create_all()
db.session.commit()
