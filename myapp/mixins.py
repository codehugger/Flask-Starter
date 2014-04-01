# -*- coding: utf-8 -*-

from uuid imort uuid4
from datetime import datetime

from myapp.extensions import db


def _uuid_str():
    return str(uuid4())


class IdentifierMixin(object):
    identifier = db.Column(db.String(36), default=_uuid_str)


class TimestampMixin(object):
    created_at = db.Column(db.DateTime, default=datetime.now)
    updated_at = db.Column(db.DateTime, default=datetime.now, onupdate=datetime.now)
