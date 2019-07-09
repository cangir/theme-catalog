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

    def get_item_by_id(id):
        item = db.session.query(Category) \
            .filter_by(id=id).one_or_none()
        return item

    def get_item_by_slug(slug):
        item = db.session.query(Category) \
            .filter_by(slug=slug).one_or_none()
        return item

    def get_items():
        items = db.session.query(Category).all()
        return items

    def add(name, slug, description, count=0):
        item = Category(
            name=name,
            slug=slug,
            description=description,
            count=count)
        db.session.add(item)
        db.session.commit()

    def update(name, slug, description, count):
        item = Category(
            name=name,
            slug=slug,
            description=description,
            count=count)
        db.session.add(item)
        db.session.commit()


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
