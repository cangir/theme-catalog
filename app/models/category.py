#!/usr/bin/python3
# -*- coding: utf-8 -*-

# Category Model
#
# author: Ahmet Cangir
# github: https://github.com/cangir
# license: https://github.com/cangir/theme-catalog/blob/master/LICENSE

from app import db
from app.models.theme import Theme


class Category(db.Model):
    __tablename__ = "categories"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), unique=True)
    slug = db.Column(db.String(250), unique=True)
    description = db.Column(db.String(250), default="")
    count = db.Column(db.Integer, default=0)

    def __init__(self, name, slug, description, count):
        self.name = name
        self.slug = slug
        self.description = description
        self.count = count

    def __repr__(self):
        return "<Category {0}>".format(self)

    @property
    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "slug": self.slug,
            "description": self.description,
            "count": self.count
        }

    def get_item_by_id(id):
        """Get one category item by id or None

        Argument:

            id {integer}

        Return:

            Category item or None
        """
        item = db.session.query(Category) \
            .filter_by(id=id).one_or_none()
        return item

    def get_item_by_slug(slug):
        """Get item by slug or None

        Argument:

            slug {string}

        Return:

            Category item or None
        """
        item = db.session.query(Category) \
            .filter_by(slug=slug).one_or_none()
        return item

    def get_item_or_404(slug):
        """Get item by slug or 404

        Argument:

            slug {string}

        Return:

            Category item or 404
        """
        item = db.session.query(Category) \
            .filter_by(slug=slug).first_or_404()
        return item

    def get_items():
        """Get and return all categories"""
        items = db.session.query(Category) \
            .order_by(Category.slug).all()
        return items

    def add(name, slug, description, count=0):
        """Add category item

        Arguments:
            name {string} -- Title
            slug {string} -- Slug
            description {string} -- Description

        Keyword Arguments:
            count {int} -- Count related items (default: {0})
        """
        item = Category(
            name=name,
            slug=slug,
            description=description,
            count=count)
        db.session.add(item)
        db.session.commit()

        return item


class CategoryRelation(db.Model):
    """
    This is a relation table between categories and themes.
    There's no need to declare id column.
    But both category_id and theme_id columns will be defined as primary key.
    """

    __tablename__ = "category_relation"

    category_id = db.Column(db.Integer, db.ForeignKey(
        "categories.id"), primary_key=True)
    theme_id = db.Column(db.Integer, db.ForeignKey(
        "themes.id"), primary_key=True)

    category = db.relationship(Category, foreign_keys=category_id)
    theme = db.relationship(Theme, foreign_keys=theme_id)

    def __init__(self, category_id, theme_id):
        self.category_id = category_id
        self.theme_id = theme_id

    def __repr__(self):
        return "<CategoryRelation {0}>".format(self)

    @property
    def serialize(self):
        return {
            "category_id": self.category_id,
            "theme_id": self.theme_id
        }

    def get_items_by_category_id(category_id):
        items = db.session.query(CategoryRelation) \
            .filter_by(category_id=category_id).all()
        return items
