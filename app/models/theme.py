#!/usr/bin/python3
from app import db
from app.models.user import User  # noqa: E402
import datetime


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


class LicenseType(db.Model):
    __tablename__ = "license_types"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), nullable=False)
    slug = db.Column(db.String(250), nullable=False)
    count = db.Column(db.Integer)

    def __init__(self, name, slug, count):
        self.name = name
        self.slug = slug
        self.count = count

    def __repr__(self):
        return "<LicenseType {0}>".format(self)

    @property
    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "slug": self.slug,
            "count": self.count
        }


class Theme(db.Model):
    __tablename__ = "themes"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), unique=True)
    slug = db.Column(db.String(80), unique=True)
    description = db.Column(db.String(250))
    content = db.Column(db.Text)
    features = db.Column(db.Text)
    meta_title = db.Column(db.String(250))
    meta_description = db.Column(db.String(250))
    slogan = db.Column(db.String(250))
    preview_url = db.Column(db.String(250))
    download_url = db.Column(db.String(250))
    github_url = db.Column(db.String(250))
    license_url = db.Column(db.String(250))
    date = db.Column(db.DateTime, default=datetime.datetime.utcnow)
    last_modified_at = db.Column(
        db.DateTime,
        default=datetime.datetime.utcnow,
        onupdate=datetime.datetime.utcnow)

    license_type_id = db.Column(db.Integer, db.ForeignKey("license_types.id"))
    license_type = db.relationship(LicenseType, foreign_keys=license_type_id)

    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    user = db.relationship(User, foreign_keys=user_id)

    theme_author_id = db.Column(db.Integer, db.ForeignKey("theme_authors.id"))
    theme_author = db.relationship(ThemeAuthor, foreign_keys=theme_author_id)

    def __init__(
            self,
            title,
            slug,
            description,
            content,
            features,
            meta_title,
            meta_description,
            slogan,
            preview_url,
            download_url,
            github_url,
            license_url,
            license_type_id,
            date,
            last_modified_at,
            user_id,
            theme_author_id):
        self.title = title
        self.slug = slug
        self.description = description
        self.content = content
        self.features = features
        self.meta_title = meta_title
        self.meta_description = meta_description
        self.slogan = slogan
        self.preview_url
        self.download_url
        self.github_url
        self.license_url
        self.license_type_id
        self.date = date
        self.last_modified_at = last_modified_at
        self.user_id = user_id
        self.theme_author_id = theme_author_id

    def __repr__(self):
        return "<Theme {0}>".format(self)

    @property
    def serialize(self):
        return {
            "id": self.id,
            "title": self.title,
            "slug": self.slug,
            "description": self.description,
            "content": self.content,
            "features": self.features,
            "meta_title": self.meta_title,
            "meta_description": self.meta_description,
            "slogan": self.slogan,
            "preview_url": self.preview_url,
            "download_url": self.download_url,
            "github_url": self.github_url,
            "license_url": self.license_url,
            "license_type_id": self.license_type_id,
            "date": self.date,
            "last_modified_at": self.last_modified_at,
            "user_id": self.user_id,
            "theme_author_id": self.theme_author_id
        }


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


class CategoryRelation(db.Model):
    __tablename__ = "category_relation"
    """
    This is a relation table between categories and themes.
    There's no need to declare id column.
    But both category_id and theme_id columns will be defined as primary key.
    """
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
