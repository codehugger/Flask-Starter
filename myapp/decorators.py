# -*- coding: utf-8 -*-

from functools import wraps

from flask import request, abort


def json_service(func):
    '''Verifies that the incoming request is a JSON request'''

    @wraps(func)
    def decorated_view(*args, **kwargs):
        if request.json is None:
            return abort(406)
        return func(*args, **kwargs)
    return decorated_view
