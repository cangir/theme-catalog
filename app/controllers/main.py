#!/usr/bin/python3
# -*- coding: utf-8 -*-

# Main controller
#
# author: Ahmet Cangir
# github: https://github.com/cangir
# license: https://github.com/cangir/theme-catalog/blob/master/LICENSE

import os
import json
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
from app.libraries.image_handler import ImageHandler as img
from config import Config


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
    items = db.session.query(Theme).all()
    return render_template(
        "home.html",
        items=items)


@app.route("/test")
def test():
    items = db.session.query(Theme).all()
    return jsonify(themes=[item.serialize for item in items])
    # return jsonify(themes=[item.serialize for item in items])


@app.route('/category/add', methods=['GET', 'POST'])
@login_required
def category_add():
    """Register new category"""

    if request.method == "POST":
        # Define variables
        name = request.form.get('name')
        slug = request.form.get('slug')
        if slug == "":
            slug = slugify(name)
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
    """Edit category"""
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


@app.route("/category/<string:slug>", methods=["GET", "POST"])
def category(slug):
    """Retrieve items of the category"""
    category = Category.get_item_or_404(slug)
    categories = Category.get_items()
    items = CategoryRelation.get_items_by_category_id(category.id)

    return render_template("category/category.html",
                           categories=categories,
                           category=category,
                           items=items
                           )


@app.route('/tag/add', methods=['GET', 'POST'])
@login_required
def tag_add():
    """Register new tag"""

    if request.method == "POST":
        # Define variables
        name = request.form.get('name')
        slug = request.form.get('slug')
        if slug == "":
            slug = slugify(name)

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
    """Edit Tag"""
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


@app.route("/tag/<string:slug>", methods=["GET", "POST"])
def tag(slug):
    """Retrieve items of the tag"""
    tag = Tag.get_item_by_slug(slug)
    items = TagRelation.get_items_by_tag_id(tag.id)
    tags = Tag.get_items()

    return render_template("tag/tag.html",
                           tags=tags,
                           tag=tag,
                           items=items
                           )


@app.route('/license-type/add', methods=['GET', 'POST'])
@login_required
def license_type_add():
    """Register new license_type"""

    if request.method == "POST":
        # Define variables
        name = request.form.get('name')
        slug = request.form.get('slug')
        if slug == "":
            slug = slugify(name)

        license_type_exists = LicenseType.get_item_by_slug(slug) is not None
        if not license_type_exists:
            # Add new item to database
            item = LicenseType.add(name,
                                   slug)
            # Redirect to add license_type page
            return redirect(url_for("license_type_add"))
        else:
            flash('LicenseType already exists.')

    # Render license_type-add.html and serve page
    return render_template("license-type/license-type-add.html",
                           license_types=LicenseType.get_items()
                           )


@app.route('/license-type/<int:license_type_id>/edit', methods=['GET', 'POST'])
@login_required
def license_type_edit(license_type_id):
    """Edit license type"""
    license_type = LicenseType.get_item_by_id(license_type_id)
    if license_type is None:
        abort(404)
    else:
        if request.method == "POST":
            license_type.name = request.form["name"]
            license_type.slug = request.form["slug"]

            db.session.add(license_type)
            db.session.commit()

        return render_template("license-type/license-type-edit.html",
                               license_type=license_type,
                               license_types=LicenseType.get_items()
                               )


@app.route("/license-type/<string:slug>", methods=["GET", "POST"])
def license_type(slug):
    """Retrieve items of the license_type"""
    license_type = LicenseType.get_item_or_404(slug)
    license_types = LicenseType.get_items()
    items = Theme.get_items_by_license_type_id(license_type.id)

    return render_template("license-type/license-type.html",
                           license_types=license_types,
                           license_type=license_type,
                           items=items
                           )


@app.route('/theme-author/add', methods=['GET', 'POST'])
@login_required
def theme_author_add():
    """Register a new theme_author"""
    if request.method == "POST":
        # Define variables
        name = request.form.get('name')
        slug = request.form.get('slug')
        if slug == "":
            slug = slugify(name)
        github_username = request.form.get('github_username')

        theme_author_exists = ThemeAuthor.get_item_by_slug(slug) is not None
        if not theme_author_exists:
            # Add new item to database
            item = ThemeAuthor.add(name,
                                   slug,
                                   github_username)
            # Redirect to add theme_author page
            return redirect(url_for("theme_author_add"))
        else:
            flash('ThemeAuthor already exists.')

    # Render theme_author-add.html and serve page
    return render_template("theme-author/theme-author-add.html",
                           theme_authors=ThemeAuthor.get_items()
                           )


@app.route('/theme-author/<int:theme_author_id>/edit', methods=['GET', 'POST'])
@login_required
def theme_author_edit(theme_author_id):
    """Edit theme author"""
    theme_author = ThemeAuthor.get_item_by_id(theme_author_id)
    if theme_author is None:
        abort(404)
    else:
        if request.method == "POST":
            theme_author.name = request.form["name"]
            theme_author.slug = request.form["slug"]
            theme_author.github_username = request.form["github_username"]

            db.session.add(theme_author)
            db.session.commit()

        return render_template("theme-author/theme-author-edit.html",
                               theme_author=theme_author,
                               theme_authors=ThemeAuthor.get_items()
                               )


@app.route("/theme-author/<string:slug>", methods=["GET", "POST"])
def theme_author(slug):
    """Retrieve items of the theme_author"""
    theme_author = ThemeAuthor.get_item_or_404(slug)
    theme_authors = ThemeAuthor.get_items()
    items = Theme.get_items_by_theme_author_id(theme_author.id)

    return render_template("theme-author/theme-author.html",
                           theme_authors=theme_authors,
                           theme_author=theme_author,
                           items=items
                           )


@app.route('/theme/add', methods=['GET', 'POST'])
@login_required
def theme_add():
    """Register new item"""
    if request.method == "POST":
        title = request.form.get('title')
        # Slugify the name if slug is empty
        slug = request.form.get('slug')
        if slug == "":
            slug = slugify(title)

        if db.session.query(Theme).filter_by(slug=slug).count() >= 1:
            flash('Please change slug. The same url exists!')

        if request.form.get('license_type') == "":
            flash('License type can not be empty')

        if request.form.get('theme_author') == "":
            flash('Theme author can not be empty')

        item = Theme.add(
            title=request.form.get('title'),
            slug=slug,
            description=request.form.get('description'),
            content=request.form.get('content'),
            features=request.form.get('features'),
            meta_title=request.form.get('meta_title'),
            meta_description=request.form.get('meta_description'),
            slogan=request.form.get('slogan'),
            preview_url=request.form.get('preview_url'),
            download_url=request.form.get('download_url'),
            github_url=request.form.get('github_url'),
            license_url=request.form.get('license_url'),
            license_type_id=request.form.get('license_type'),
            theme_author_id=request.form.get('theme_author'),
            user_id=session["user_id"]
        )

        # Update Selected Theme's Count
        # Theme.update_theme_author_count(item.theme_author_id)

        # Update Selected Licence Type's count
        # Theme.update_license_type_count(item.license_type_id)

        # check if the post request has the file part
        if 'image_preview' in request.files:
            file = request.files['image_preview']
            if file != '' and img.allowed_file(file.filename):
                img.upload_theme_image(item, file, 'preview')

        # check if the post request has the file part
        if 'image_screenshot' in request.files:
            file = request.files['image_screenshot']
            if file != '' and img.allowed_file(file.filename):
                img.upload_theme_image(item, file, 'screenshot')

        Category.add_or_update_category(
            request.form.getlist('category'),
            item.id)
        Tag.add_or_update_tag(
            request.form.getlist('tag'),
            item.id)

    return render_template("theme/theme-add.html",
                           categories=Category.get_items(),
                           tags=Tag.get_items(),
                           license_types=LicenseType.get_items(),
                           theme_authors=ThemeAuthor.get_items()
                           )


@app.route('/theme/<int:item_id>/edit',
           methods=['GET', 'POST'])
@login_required
def theme_edit(item_id):
    """Edit an item"""
    item = db.session.query(Theme) \
        .filter_by(id=item_id).first_or_404()

    if request.method == "POST":
        # Edit item
        if item.title != request.form["title"]:
            item.title = request.form["title"]

        if item.slug != request.form["slug"]:
            # Rename theme image folder
            theme_author_folder = os.path.join(
                app.config['UPLOAD_FOLDER'],
                item.theme_author.slug)
            theme_upload_folder = os.path.join(
                theme_author_folder,
                item.slug)
            theme_upload_new_folder = os.path.join(
                theme_author_folder,
                request.form["slug"])
            image_preview = os.path.join(
                theme_upload_new_folder,
                item.slug + '-preview.jpg')
            image_preview_new = os.path.join(
                theme_upload_new_folder,
                request.form["slug"] + '-preview.jpg')
            image_screenshot = os.path.join(
                theme_upload_new_folder,
                item.slug + '-screenshot.jpg')
            image_screenshot_new = os.path.join(
                theme_upload_new_folder,
                request.form["slug"] + '-screenshot.jpg')

            os.rename(theme_upload_folder, theme_upload_new_folder)
            os.rename(image_preview, image_preview_new)
            os.rename(image_screenshot, image_screenshot_new)

            item.slug = request.form["slug"]

        if item.description != request.form["description"]:
            item.description = request.form["description"]

        if item.content != request.form["content"]:
            item.content = request.form["content"]

        if item.features != request.form["features"]:
            item.features = request.form["features"]

        if item.meta_title != request.form.get('meta_title'):
            item.meta_title = request.form.get('meta_title')

        if item.meta_description != request.form.get('meta_description'):
            item.meta_description = request.form.get('meta_description')

        if item.slogan != request.form.get('slogan'):
            item.slogan = request.form.get('slogan')

        if item.preview_url != request.form.get('preview_url'):
            item.preview_url = request.form.get('preview_url')

        if item.download_url != request.form.get('download_url'):
            item.download_url = request.form.get('download_url')

        if item.github_url != request.form.get('github_url'):
            item.github_url = request.form.get('github_url')

        if item.license_url != request.form.get('license_url'):
            item.license_url = request.form.get('license_url')

        if item.license_type_id != request.form.get('license_type'):
            item.license_type_id = request.form.get('license_type')

        # if item.date != request.form.get('date'):
            # item.date = request.form.get('date')
        # item.date = datetime.datetime.utcnow()
        # if item.last_modified_at != request.form.get('last_modified_at'):
        # item.last_modified_at = datetime.datetime.utcnow()

        # if item.theme_author != request.form.get('theme_author'):
        #     item.theme_author_id = request.form.get('theme_author')
        # item.user_id = session["user_id"]

        db.session.add(item)
        db.session.commit()

        # Update Selected Theme's Count
        Theme.update_theme_author_count(item.theme_author_id)

        # Update Selected Licence Type's count
        Theme.update_license_type_count(item.license_type_id)

        # check if the post request has the file part
        if 'image_preview' in request.files:
            file = request.files['image_preview']
            if file and img.allowed_file(file.filename):
                img.upload_theme_image(item, file, 'preview')

        # check if the post request has the file part
        if 'image_screenshot' in request.files:
            file = request.files['image_screenshot']
            if file and img.allowed_file(file.filename):
                img.upload_theme_image(item, file, 'screenshot')

        Category.add_or_update_category(
            request.form.getlist('category'),
            item_id)
        Tag.add_or_update_tag(
            request.form.getlist('tag'),
            item_id)

    item_categories = db.session.query(CategoryRelation.category_id) \
        .filter_by(theme_id=item_id).all()
    item_tags = db.session.query(TagRelation.tag_id) \
        .filter_by(theme_id=item_id).all()

    return render_template(
        "theme/theme-edit.html",
        item=item,
        categories=Category.get_items(),
        item_categories=json.dumps(item_categories),
        tags=Tag.get_items(),
        item_tags=json.dumps(item_tags),
        theme_authors=ThemeAuthor.get_items(),
        license_types=LicenseType.get_items(),
        img_preview_exists=img.img_preview_exists(item),
        img_screenshot_exists=img.img_screenshot_exists(item))


@app.route('/theme/<int:item_id>/delete', methods=['GET', 'POST'])
@login_required
def theme_delete(item_id):
    """Remove an item"""

    if request.method == "POST":
        item = db.session.query(Theme).filter_by(id=item_id).one()
        if item is not None:
            item_id = item.id
            item_theme_author = item.theme_author_id
            item_license_type = item.license_type_id

            # Update category relations and counts
            Category.remove_category_relation(item_id)

            # Update tag relations and counts
            Tag.remove_tag_relation(item_id)

            # Remove Item
            db.session.delete(item)
            db.session.commit()

            # Update theme author items count
            Theme.update_theme_author_count(item_theme_author)

            # Update license types count
            Theme.update_license_type_count(item_license_type)

            return redirect(url_for("home"))

    return render_template("theme/theme-single.html",
                           term_id=term_id,
                           item_id=item_id,
                           item=item)


@app.route('/theme/<string:slug>')
# @login_required
def theme_single(slug):
    """Return an item"""
    item = db.session.query(Theme).filter_by(slug=slug).one()
    item_categories = db.session.query(CategoryRelation.category) \
        .filter_by(theme_id=item.id).all()
    item_tags = db.session.query(TagRelation.tag) \
        .filter_by(theme_id=item.id).all()

    # flash('You were successfully logged in')
    return render_template("theme/theme-single.html",
                           item=item,
                           item_categories=item_categories,
                           item_tags=item_tags,
                           categories=Category.get_items())


# @app.route('/theme/<int:item_id>/img_preview', methods=['GET', 'POST'])
# def theme_img_preview(item_id):
#     item = Theme.get_item_or_none(item_id)
#     img_url = app.config['IMAGE_NOT_FOUND']
#     if item and img.img_preview_exists(item):
#         img_url = img.theme_image_url(item, 'preview')
#     # Return preview img_url or None
#     return img_url


# @app.route('/theme/<int:item_id>/img_screenshot', methods=['GET', 'POST'])
# def theme_img_screenshot(item_id):
#     item = Theme.get_item_or_none(item_id)
#     if item and img.img_screenshot_exists(item):
#         img_url = img.theme_image_url(item, 'screenshot')
#     else:
#         img_url = app.config['IMAGE_NOT_FOUND']
#     # Return screenshot img_url or None
#     return img_url
