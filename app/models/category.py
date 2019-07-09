#!/usr/bin/python3
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

    # Get all categories
    def get_categories():
        categories = db.session.query(Category) \
            .order_by(Category.slug).all()
        return categories


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
