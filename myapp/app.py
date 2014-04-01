# -*- coding: utf-8 -*-

from flask import Flask, make_response

from myapp.extensions import db, migrate
from myapp.blueprints import api, frontend


def app_factory(config=None):

    app = Flask(__name__)

    # Config

    app.config.from_envvar('MYAPP_CONFIG', silent=False)

    if config is not None:
        app.config.from_object(config)

    # Extensions

    db.init_app(app)
    migrate.init_app(app, db)

    # Blueprints

    app.register_blueprint(api, url_prefix='/api')
    app.register_blueprint(frontend)

    # Routes (DEBUG only)

    @app.route("/routes/")
    def routes():
        if app.config['DEBUG'] is not True:
            return "routes display is only available in development mode"
        rules = []
        for rule in app.url_map.iter_rules():
            rules.append("{0:64} => {1}".format(rule.rule, rule.endpoint))
        resp = make_response("\n".join(sorted(rules)))
        resp.headers['Content-Type'] = 'text/plain'
        return resp

    return app
