#!/usr/bin/env python
# -*- coding: utf-8 -*-

from datetime import datetime

from flask.ext.script import Manager
from flask.ext.migrate import MigrateCommand

from myapp import app_factory
from myapp.extensions import db


manager = Manager(app_factory)


if __name__ == '__main__':

    # commands
    manager.add_command("db", MigrateCommand)

    try:
        manager.run()
    except KeyboardInterrupt:
        pass
