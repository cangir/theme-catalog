#!/usr/bin/python3
from flask_login import UserMixin
from app import db


class User(UserMixin, db.Model):
    """Create users table"""

    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), nullable=False)
    email = db.Column(db.String(250), nullable=False, unique=True)
    avatar = db.Column(db.String(250))

    def __init__(self, name, email, avatar):
        self.name = name
        self.email = email
        self.avatar = avatar

    def __repr__(self):
        return "<User {0}>".format(self)

    @property
    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "email": self.email,
            "avatar": self.avatar
        }

    def get_users():
        items = db.session.query(User) \
            .order_by(User.name).all()
        return items
