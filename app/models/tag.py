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
