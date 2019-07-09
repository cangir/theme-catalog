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
    return render_template("home.html", users=User.get_users())


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


@app.route('/category/edit', methods=['GET', 'POST'])
@login_required
def category_edit():
    """Edit a category"""

    return render_template("home.html", users=users)
