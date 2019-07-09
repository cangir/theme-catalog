#!/usr/bin/python3
# -*- coding: utf-8 -*-

from flask import render_template, flash, redirect, url_for, session, request
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


@app.route("/")
def home():
    # Render homepage
    return render_template("home.html", users=helper.get_users())


@app.route("/category/<string:slug>", methods=["GET", "POST"])
def category(slug):
    return "Return Category Page"


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

        category_exists = db.session.query(Category.id) \
            .filter_by(slug=slug).scalar() is not None
        if not category_exists:
            # Add new item to database
            new_item = Category(
                name=name,
                slug=slug,
                description=description,
                count=0)
            db.session.add(new_item)
            db.session.commit()

        # Redirect to add category page after inserting item
        return redirect(url_for("category_add"))

    # Render category-add.html and serve page
    return render_template("category/category-add.html",
                           categories=Category.get_categories()
                           )


@app.route('/category/<int:id>/edit', methods=['GET', 'POST'])
@login_required
def category_edit(id):
    return "Edit Category: " + str(id)


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
