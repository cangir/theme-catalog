#!/usr/bin/python3
# -*- coding: utf-8 -*-

# Tag Model
#
# author: Ahmet Cangir
# github: https://github.com/cangir
# license: https://github.com/cangir/theme-catalog/blob/master/LICENSE

from slugify import slugify
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
        """Get one tag item by id or None

        Argument:

            id {integer}

        Return:

            Tag item or None
        """
        item = db.session.query(Tag) \
            .filter_by(id=id).one_or_none()
        return item

    def get_item_by_slug(slug):
        """Get item by slug or None

        Argument:

            slug {string}

        Return:

            Tag item or None
        """
        item = db.session.query(Tag) \
            .filter_by(slug=slug).one_or_none()
        return item

    def get_item_or_404(slug):
        """Get item by slug or 404

        Argument:

            slug {string}

        Return:

            Tag item or 404
        """
        item = db.session.query(Tag) \
            .filter_by(slug=slug).first_or_404()
        return item

    def get_items():
        """Get and return all categories"""
        items = db.session.query(Tag) \
            .order_by(Tag.slug).all()
        return items

    def add(name, slug, count=0):
        """Add tag item

        Arguments:
            name {string} -- Title
            slug {string} -- Slug

        Keyword Arguments:
            count {int} -- Count related items (default: {0})
        """
        item = Tag(
            name=name,
            slug=slug,
            count=count)
        db.session.add(item)
        db.session.commit()

        return item

    def update_tag_count(tag_id):
        """Count items"""
        items_count = db.session.query(TagRelation) \
            .filter_by(tag_id=tag_id).count()

        """Update tag count"""
        tag = db.session.query(Tag).filter_by(id=tag_id).one()
        tag.count = items_count
        db.session.add(tag)
        db.session.commit()

    def add_tag_relation(tag_id, theme_id):
        # Add tag relation
        new_item = TagRelation(
            tag_id=tag_id,
            theme_id=theme_id)
        db.session.add(new_item)
        db.session.commit()

    def remove_tag_relation(item_id):
        item_relations = db.session.query(TagRelation) \
            .filter_by(theme_id=item_id).all()

        for relation in item_relations:
            db.session.delete(relation)
            db.session.commit()
            # Update tag count
            Tag.update_tag_count(relation.tag_id)

    def add_or_update_tag(tags, item_id):
        """Add or update tag and relate with item"""
        # Remove item's tag relations
        Tag.remove_tag_relation(item_id)

        for tag in tags:
            tag_slug = slugify(tag)
            tag_exists = db.session.query(Tag.id) \
                .filter_by(slug=tag_slug).scalar() is not None
            if not tag_exists:
                # Add new tag to database
                new_tag = Tag(
                    name=tag,
                    slug=tag_slug,
                    count=0)
                db.session.add(new_tag)
                db.session.commit()
                tag_id = new_tag.id
            else:
                tag_id = Tag.get_item_by_slug(tag_slug).id
            # Add tag relation
            Tag.add_tag_relation(tag_id, item_id)
            # Update tag count
            Tag.update_tag_count(tag_id)


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
