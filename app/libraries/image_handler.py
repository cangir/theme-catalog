#!/usr/bin/python3

# Image Handler
#
# author: Ahmet Cangir
# github: https://github.com/cangir
# license: https://github.com/cangir/theme-catalog/blob/master/LICENSE

import os
import json
import urllib
from datetime import datetime
import requests
from slugify import slugify
from flask import abort, flash, jsonify
from flask import redirect, render_template, request, session, url_for
from flask_login import login_required
from werkzeug.utils import secure_filename

from app import app, db, md
from app.models.user import User
from app.models.category import Category
from app.models.category import CategoryRelation
from app.models.tag import Tag
from app.models.tag import TagRelation
from app.models.license_type import LicenseType
from app.models.theme import Theme
from app.models.theme_author import ThemeAuthor
from config import Config


class ImageHandler():

    def allowed_file(filename):
        return '.' in filename and \
            filename.rsplit('.', 1)[1].lower(
            ) in app.config['ALLOWED_EXTENSIONS']

    def rename_file(filename, new_filename):
        return new_filename + '.jpg'

    def upload_theme_image(item, file, image_type):
        filename = ImageHandler.allowed_file(file.filename)
        theme_author_upload_folder = os.path.join(
            app.config['UPLOAD_FOLDER'],
            item.theme_author.slug)
        theme_upload_folder = os.path.join(
            theme_author_upload_folder,
            item.slug
        )
        filename_old = item.slug + '-' + image_type + '.jpg'
        filename_old = os.path.join(
            theme_upload_folder,
            filename_old)
        filename = ImageHandler.rename_file(
            ImageHandler.allowed_file(file.filename),
            item.slug + '-' + image_type)
        if os.path.isfile(filename_old):
            os.unlink(filename_old)
        os.makedirs(theme_upload_folder, exist_ok=True)
        file.save(os.path.join(theme_upload_folder, filename))

    def theme_image_url(item, image_type):
        theme_author_upload_folder = os.path.join(
            app.config['UPLOAD_FOLDER'],
            item.theme_author.slug)
        theme_upload_folder = os.path.join(
            theme_author_upload_folder,
            item.slug
        )
        filename = os.path.join(theme_upload_folder,
                                item.slug + '-' + image_type + '.jpg')
        return filename

    def img_preview_exists(item):
        img_preview_url = ImageHandler.theme_image_url(item, 'preview')
        img_preview_exists = os.path.isfile(img_preview_url)
        return img_preview_exists

    def img_screenshot_exists(item):
        img_screenshot_url = ImageHandler.theme_image_url(item, 'screenshot')
        img_screenshot_exists = os.path.isfile(img_screenshot_url)
        return img_screenshot_exists
