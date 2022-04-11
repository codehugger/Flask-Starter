# -*- coding: utf-8 -*-

from setuptools import setup


setup(
    name="myapp",
    version='0.0.1-dev',
    description='My Awesome Application',
    author='**INSERT_AUTHOR_NAME**',
    author_email='**INSERT_AUTHOR_EMAIL**',
    packages=[
        'myapp',
        'myapp.blueprints'
    ],
    url='https://www.github.com/codehugger/myapp',
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'Flask==0.10.1',
        'Flask-Migrate==1.2.0',
        'Flask-SQLAlchemy==1.0',
        'Flask-Script==0.6.7',
        'Flask-Testing==0.4.1',
        'Jinja2==2.7.2',
        'Mako==0.9.1',
        'MarkupSafe==0.19',
        'SQLAlchemy==0.9.4',
        'Werkzeug==0.15.3',
        'alembic==0.6.4',
        'itsdangerous==0.24',
        'wsgiref==0.1.2',
    ]
)
