#!/usr/bin/python3
# -*- coding: utf-8 -*-

# Category Model
#
# author: Ahmet Cangir
# github: https://github.com/cangir
# license: https://github.com/cangir/theme-catalog/blob/master/LICENSE

from slugify import slugify
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
            Category.update_category_count(relation.category_id)

    def add_or_update_category(categories, item_id):
        # Remove item's category relations
        Category.remove_category_relation(item_id)

        for category in categories:
            category_slug = slugify(category)
            category_exists = db.session.query(Category.id) \
                .filter_by(slug=category_slug).scalar() is not None
            if not category_exists:
                # Add new category to database
                new_category = Category(
                    name=category,
                    slug=category_slug,
                    description="",
                    count=0)
                db.session.add(new_category)
                db.session.commit()
                category_id = new_category.id
            else:
                category_id = Category.get_item_by_slug(category_slug).id
            # Add category relation
            Category.add_category_relation(category_id, item_id)
            # Update category count
            Category.update_category_count(category_id)


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


db.create_all()
db.session.commit()
