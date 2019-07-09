#!/usr/bin/python3
# -*- coding: utf-8 -*-

# License Type Model
#
# author: Ahmet Cangir
# github: https://github.com/cangir
# license: https://github.com/cangir/theme-catalog/blob/master/LICENSE

from app import db


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

    def get_item_by_id(id):
        """Get one license_type item by id or None

        Argument:

            id {integer}

        Return:

            LicenseType item or None
        """
        item = db.session.query(LicenseType) \
            .filter_by(id=id).one_or_none()
        return item

    def get_item_by_slug(slug):
        """Get item by slug or None

        Argument:

            slug {string}

        Return:

            LicenseType item or None
        """
        item = db.session.query(LicenseType) \
            .filter_by(slug=slug).one_or_none()
        return item

    def get_item_or_404(slug):
        """Get item by slug or 404

        Argument:

            slug {string}

        Return:

            LicenseType item or 404
        """
        item = db.session.query(LicenseType) \
            .filter_by(slug=slug).first_or_404()
        return item

    def get_items():
        """Get and return all categories"""
        items = db.session.query(LicenseType) \
            .order_by(LicenseType.slug).all()
        return items

    def add(name, slug, count=0):
        """Add license type item

        Arguments:
            name {string} -- Title
            slug {string} -- Slug
            description {string} -- Description

        Keyword Arguments:
            count {int} -- Count related items (default: {0})
        """
        item = LicenseType(
            name=name,
            slug=slug,
            count=count)
        db.session.add(item)
        db.session.commit()
