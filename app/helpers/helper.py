#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from app import app, db
from app.models.model import Theme
from app.models.model import ThemeAuthor
from app.models.model import Category
from app.models.model import CategoryRelation
from app.models.model import Tag
from app.models.model import TagRelation
from app.models.model import LicenseType
from config import Config


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower(
           ) in app.config['ALLOWED_EXTENSIONS']


def rename_file(filename, new_filename):
    return new_filename + '.' + filename.rsplit('.', 1)[1].lower()


def get_categories():
    categories = db.session.query(Category) \
        .order_by(Category.slug).all()
    return categories


def get_tags():
    tags = db.session.query(Tag) \
        .order_by(Tag.slug).all()
    return tags


def get_theme_authors():
    theme_authors = db.session.query(ThemeAuthor).all()
    return theme_authors


def get_theme_author_by_id(theme_author_id):
    item = db.session.query(ThemeAuthor).filter_by(id=theme_author_id).one()
    return item


def update_theme_author_count(theme_author_id):
    """Count items"""
    items_count = db.session.query(Theme) \
        .filter_by(theme_author_id=theme_author_id).count()

    """Update category count"""
    item = db.session.query(ThemeAuthor).filter_by(id=theme_author_id).one()
    item.count = items_count
    db.session.add(item)
    db.session.commit()


def get_license_types():
    items = db.session.query(LicenseType).all()
    return items


def update_license_type_count(license_type_id):
    """Count items"""
    items_count = db.session.query(Theme) \
        .filter_by(license_type_id=license_type_id).count()

    """Update category count"""
    item = db.session.query(LicenseType).filter_by(id=license_type_id).one()
    item.count = items_count
    db.session.add(item)
    db.session.commit()


def get_all_items():
    items = db.session.query(CategoryRelation) \
        .group_by(CategoryRelation.theme_id).all()
    return items


def get_items_by_category(category_id):
    items = db.session.query(CategoryRelation) \
        .filter_by(category_id=category_id).all()
    return items


def get_items_by_tag(tag_id):
    items = db.session.query(TagRelation) \
        .filter_by(tag_id=tag_id).all()
    return items


def get_items_by_theme_author(theme_author_id):
    items = db.session.query(Themes) \
        .filter_by(theme_author_id=theme_author_id).all()
    return items


def get_theme_by_slug(slug):
    item = db.session.query(Theme).filter_by(slug=slug).one()
    return item


def get_theme_by_id(id):
    item = db.session.query(Theme).filter_by(id=id).one()
    return item


def get_category_by_slug(slug):
    item = db.session.query(Category).filter_by(slug=slug).one()
    return item


def update_category_count(category_id):
    """Count items"""
    items_count = db.session.query(CategoryRelation) \
        .filter_by(category_id=category_id).count()

    """Update category count"""
    category = db.session.query(Category).filter_by(id=category_id).one()
    category.count = items_count
    db.session.add(category)
    db.session.commit()


def add_category_relation(category_id, theme_id):
    """Update category count"""
    new_category_relation = CategoryRelation(
        category_id=category_id,
        theme_id=theme_id)
    db.session.add(new_category_relation)
    db.session.commit()


def remove_category_relation(item_id):
    item_relations = db.session.query(CategoryRelation) \
        .filter_by(theme_id=item_id).all()

    for relation in item_relations:
        db.session.delete(relation)
        db.session.commit()
        # Update category count
        update_category_count(relation.category_id)


def get_tag_by_slug(slug):
    item = db.session.query(Tag).filter_by(slug=slug).one()
    return item


def update_tag_count(tag_id):
    """Count items"""
    items_count = db.session.query(TagRelation) \
        .filter_by(tag_id=tag_id).count()

    """Update tag count"""
    tag = db.session.query(Tag).filter_by(id=tag_id).one()
    tag.count = items_count
    db.session.add(tag)
    db.session.commit()


def add_tag_relation(tag_id, theme_id):
    # Add tag relation
    new_item = TagRelation(
        tag_id=tag_id,
        theme_id=theme_id)
    db.session.add(new_item)
    db.session.commit()


def remove_tag_relation(item_id):
    item_relations = db.session.query(TagRelation) \
        .filter_by(theme_id=item_id).all()

    for relation in item_relations:
        db.session.delete(relation)
        db.session.commit()
        # Update tag count
        update_tag_count(relation.tag_id)
