# -*- coding: utf-8 -*-

from keystore.extensions import db


def create_db():
    db.create_all()


def drop_db():
    db.drop_all()


def seed_db():
    pass
