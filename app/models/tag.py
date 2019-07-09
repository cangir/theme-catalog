#!/usr/bin/python3
from app import db
from app.models.theme import Theme


class Tag(db.Model):
    __tablename__ = "tags"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), unique=True)
    slug = db.Column(db.String(250), unique=True)
    count = db.Column(db.Integer)

    def __init__(self, name, slug, count):
        self.name = name
        self.slug = slug
        self.count = count

    def __repr__(self):
        return "<Term {0}>".format(self)

    @property
    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "slug": self.slug,
            "count": self.count
        }

    def get_item_by_id(id):
        item = db.session.query(Tag) \
            .filter_by(id=id).one_or_none()
        return item

    def get_item_by_slug(slug):
        item = db.session.query(Tag) \
            .filter_by(slug=slug).one_or_none()
        return item

    def get_items():
        items = db.session.query(Tag) \
            .order_by(Tag.slug).all()
        return items

    def add(name, slug, count=0):
        item = Tag(
            name=name,
            slug=slug,
            count=count)
        db.session.add(item)
        db.session.commit()


class TagRelation(db.Model):
    __tablename__ = "tag_relation"
    """
    This is a relation table between tags and themes.
    There's no need to declare id column.
    But both tag_id and theme_id columns will be defined as primary key.
    """
    tag_id = db.Column(db.Integer, db.ForeignKey(
        "tags.id"), primary_key=True)
    theme_id = db.Column(db.Integer, db.ForeignKey(
        "themes.id"), primary_key=True)

    tag = db.relationship(Tag, foreign_keys=tag_id)
    theme = db.relationship(Theme, foreign_keys=theme_id)

    def __init__(self, tag_id, theme_id):
        self.tag_id = tag_id
        self.theme_id = theme_id

    def __repr__(self):
        return "<TagRelation {0}>".format(self)

    @property
    def serialize(self):
        return {
            "tag_id": self.tag_id,
            "theme_id": self.theme_id
        }

    def get_items_by_tag_id(tag_id):
        items = db.session.query(TagRelation) \
            .filter_by(tag_id=tag_id).all()
        return items
