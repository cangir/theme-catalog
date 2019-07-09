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
            item = Category.add(name,
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
            category.name = request.form["name"]
            category.slug = request.form["slug"]
            category.description = request.form["description"]

            db.session.add(category)
            db.session.commit()

        return render_template("category/category-edit.html",
                               category=category,
                               categories=Category.get_items()
                               )


@app.route("/tag/<string:slug>", methods=["GET", "POST"])
def tag(slug):
    """Retrieve items of the tag"""
    tag = Tag.get_item_by_slug(slug)
    if tag is not None:
        items = TagRelation.get_items_by_tag_id(tag.id)
        tags = Tag.get_items()
    else:
        abort(404)

    return render_template("tag/tag.html",
                           tags=tags,
                           tag=tag,
                           items=items
                           )


@app.route('/tag/add', methods=['GET', 'POST'])
@login_required
def tag_add():
    """Register a new tag"""

    if request.method == "POST":
        # Define variables
        name = request.form.get('name')
        slug = request.form.get('slug')
        if request.form.get('slug') == "":
            slug = slugify(request.form.get('name'))

        tag_exists = Tag.get_item_by_slug(slug) is not None
        if not tag_exists:
            # Add new item to database
            item = Tag.add(name,
                           slug)
            # Redirect to add tag page
            return redirect(url_for("tag_add"))
        else:
            flash('Tag already exists.')

    # Render tag-add.html and serve page
    return render_template("tag/tag-add.html",
                           tags=Tag.get_items()
                           )


@app.route('/tag/<int:tag_id>/edit', methods=['GET', 'POST'])
@login_required
def tag_edit(tag_id):
    tag = Tag.get_item_by_id(tag_id)
    if tag is None:
        abort(404)
    else:
        if request.method == "POST":
            tag.name = request.form["name"]
            tag.slug = request.form["slug"]

            db.session.add(tag)
            db.session.commit()

        return render_template("tag/tag-edit.html",
                               tag=tag,
                               tags=Tag.get_items()
                               )


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
