#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from flask import jsonify, render_template

from app import app, db
from app.models.user import User
from app.models.category import Category
from app.models.category import CategoryRelation
from app.models.tag import Tag
from app.models.tag import TagRelation
from app.models.license_type import LicenseType
from app.models.theme import Theme
from app.models.theme_author import ThemeAuthor


@app.route("/api/v1")
def api_v1():
    return ""


@app.route("/api/v1/users")
def users_json():
    """Return JSON representing all users."""
    items = db.session.query(User).all()
    return jsonify(users=[item.serialize for item in items])


@app.route("/api/v1/themes")
def themes_json():
    """Return JSON representing all themes."""
    items = db.session.query(Theme).all()
    return jsonify(themes=[item.serialize for item in items])


@app.route("/api/v1/categories")
def categories_json():
    """Return JSON representing all categories."""
    items = db.session.query(Category).all()
    return jsonify(categories=[item.serialize for item in items])


@app.route("/api/v1/tags")
def tags_json():
    """Return JSON representing all tags."""
    items = db.session.query(Tag).all()
    return jsonify(tags=[item.serialize for item in items])


@app.route("/api/v1/license-types")
def license_types_json():
    """Return JSON representing all license types."""
    items = db.session.query(LicenseType).all()
    return jsonify(license_types=[item.serialize for item in items])


@app.route("/api/v1/theme-authors")
def theme_authors_json():
    """Return JSON representing all theme authors."""
    items = db.session.query(ThemeAuthor).all()
    return jsonify(theme_authors=[item.serialize for item in items])
