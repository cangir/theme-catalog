#!/usr/bin/python3
# -*- coding: utf-8 -*-

from flask import abort, flash, redirect, render_template, request
from flask import session, url_for
from flask_login import login_required
from flask import jsonify
from slugify import slugify

from app import app, db
from config import Config
from app.models.user import User
from app.models.category import Category
from app.models.category import CategoryRelation
from app.models.tag import Tag
from app.models.tag import TagRelation
from app.models.license_type import LicenseType
from app.models.theme import Theme
from app.models.theme_author import ThemeAuthor


@app.before_request
def before_request_func():
    """Add Categories object to session"""
    session['session_categories'] = [
        item.serialize for item in Category.get_items()]


@app.errorhandler(404)
def page_not_found(e):
    """Render Error 404 Page"""
    return render_template('error/404.html'), 404


@app.route("/")
def home():
    """Render home page"""
    return render_template("home.html")


@app.route("/category/<string:slug>", methods=["GET", "POST"])
def category(slug):
    """Retrieve items of the category"""
    category = Category.get_item_by_slug(slug)
    if category is not None:
        items = CategoryRelation.get_items_by_category_id(category.id)
        categories = Category.get_items()
    else:
        abort(404)

    return render_template("category/category.html",
                           categories=categories,
                           category=category,
                           items=items
                           )


@app.route('/category/add', methods=['GET', 'POST'])
@login_required
def category_add():
    """Register a new category"""

    if request.method == "POST":
        # Define variables
        name = request.form.get('name')
        slug = request.form.get('slug')
        if request.form.get('slug') == "":
            slug = slugify(request.form.get('name'))
        description = request.form.get('description')

        category_exists = Category.get_item_by_slug(slug) is not None
        if not category_exists:
            # Add new item to database
            item = Category.add_item(name,
                                     slug,
                                     description)
            # Redirect to add category page
            return redirect(url_for("category_add"))
        else:
            flash('Category already exists.')

    # Render category-add.html and serve page
    return render_template("category/category-add.html",
                           categories=Category.get_items()
                           )


@app.route('/category/<int:category_id>/edit', methods=['GET', 'POST'])
@login_required
def category_edit(category_id):
    category = Category.get_item_by_id(category_id)
    if category is None:
        abort(404)
    else:
        if request.method == "POST":
            if request.form["name"]:
                category.name = request.form["name"]
            if request.form["slug"]:
                category.slug = request.form["slug"]
            if request.form["description"]:
                category.description = request.form["description"]

            Category.update(name, slug, description)

        return render_template("category/category-edit.html",
                               category=category,
                               categories=Category.get_items()
                               )


@app.route("/tag/<string:slug>", methods=["GET", "POST"])
def tag(slug):
    return "Return all items of selected tag: " + slug


@app.route('/tag/add', methods=['GET', 'POST'])
@login_required
def tag_add():
    return "Add Tag"


@app.route('/tag/<int:id>/edit', methods=['GET', 'POST'])
@login_required
def tag_edit(slug):
    return "Edit tag: " + slug


@app.route("/theme-author/<string:slug>", methods=["GET", "POST"])
def theme_author(slug):
    return "Return theme author: " + slug


@app.route('/theme-author/add', methods=['GET', 'POST'])
@login_required
def theme_author_add():
    return "Register a new theme author"


@app.route('/theme-author/<int:id>/edit', methods=['GET', 'POST'])
@login_required
def theme_author_edit(slug):
    return "Edit theme author: " + slug


@app.route("/license-type/<string:slug>", methods=["GET", "POST"])
def license_type(slug):
    return "Return License Type: " + slug


@app.route('/license-type/add', methods=['GET', 'POST'])
@login_required
def license_type_add():
    return "Register a new License Type"


@app.route('/license-type/<int:id>/edit', methods=['GET', 'POST'])
@login_required
def license_type_edit(slug):
    return "Edit License Type: " + slug


@app.route('/theme/<string:slug>')
def theme_single(slug):
    return "Return item: " + slug


@app.route('/theme/add', methods=['GET', 'POST'])
@login_required
def theme_add():
    return "Theme Add"


@app.route('/theme/<int:id>/edit', methods=['GET', 'POST'])
@login_required
def theme_edit(slug):
    return "Edit item: " + slug
