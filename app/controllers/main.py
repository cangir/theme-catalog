#!/usr/bin/python3
# -*- coding: utf-8 -*-

from flask import render_template, flash, redirect, url_for, session, request
from flask_login import login_required
from flask import jsonify
from slugify import slugify

from app import app, db
from config import Config
from app.models.user import User
from app.models.theme import Category, CategoryRelation
from app.models.theme import Tag, TagRelation
from app.models.theme import LicenseType
from app.models.theme import Theme
from app.models.theme import ThemeAuthor


def get_categories():
    categories = db.session.query(Category) \
        .order_by(Category.slug).all()
    return categories


def get_users():
    items = db.session.query(User) \
        .order_by(User.name).all()
    return items


@app.route("/")
def home():
    # Render homepage
    return render_template("home.html", users=users)


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
                           categories=get_categories()
                           )


@app.route('/category/edit', methods=['GET', 'POST'])
@login_required
def category_edit():
    """Edit a category"""

    return render_template("home.html", users=users)
