#!/usr/bin/python3
from app import db


class ThemeAuthor(db.Model):
    __tablename__ = "theme_authors"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), nullable=False)
    slug = db.Column(db.String(250), nullable=False)
    github_username = db.Column(db.String(250), nullable=False)
    count = db.Column(db.Integer)

    def __init__(self, name, slug, github_username, count):
        self.name = name
        self.slug = slug
        self.github_username = github_username
        self.count = count

    def __repr__(self):
        return "<ThemeAuthor {0}>".format(self)

    @property
    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "slug": self.slug,
            "github_username": self.github_username,
            "count": self.count
        }

    def get_item_by_id(id):
        item = db.session.query(ThemeAuthor) \
            .filter_by(id=id).first_or_404()
        return item

    def get_item_by_slug(slug):
        item = db.session.query(ThemeAuthor) \
            .filter_by(slug=slug).first_or_404()
        return item

    def get_items():
        items = db.session.query(ThemeAuthor) \
            .order_by(ThemeAuthor.slug).all()
        return items

    def add(name, slug, github_username, count=0):
        item = ThemeAuthor(
            name=name,
            slug=slug,
            github_username=github_username,
            count=count)
        db.session.add(item)
        db.session.commit()
