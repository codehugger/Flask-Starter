# -*- coding: utf-8 -*-

import json
import datetime

from flask import make_response

from myapp.extensions import db


class JSONAppEncoder(json.JSONEncoder):

    def default(self, obj):
        if isinstance(obj, datetime.datetime):
            return obj.isoformat()
        elif isinstance(obj, db.Model):
            return obj.serialize()
        elif isinstance(obj, set):
            return list(obj)

        return json.JSONEncoder.default(self, obj)


def json_response(data, status=200, headers=None):
    if headers is None:
        headers = dict()

    headers['Content-Type'] = 'application/json'
    data = json.dumps(data, cls=JSONAppEncoder)

    return make_response(data, status, headers)
