#!/usr/bin/python3
from app import db
from app.models.user import User  # noqa: E402
from app.models.license_type import LicenseType
from app.models.theme_author import ThemeAuthor
import datetime


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
