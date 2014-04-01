# -*- coding: utf-8 -*-

from myapp.extensions import db
from myapp.mixins import TimestampMixin, IdentifierMixin


class Post(db.Model, TimestampMixin, IdentifierMixin):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(128), nullable=False)
    body = db.Column(db.Text)
