Flask-Starter
=============

A small skeleton to use when starting a new Flask application

Why?
----

I had previously created Flask-Zero and found my self deleting a lot of stuff from there when I was creating web services and smaller web applications. This project is a starting point I created for myself and hopefully others as a nice easy-to-use template for Flask apps.


How?
----

You simply clone the project and remove the .git folder and start hacking away :)

Example on how to get started:

    $> git clone https://github.com/codehugger/Flask-Starter.git awesome_app
    $> cd awesome_app
    $> rm -rf .git

Then to install requirements and run

    $> pip install -e setup.py

What?
-----

In this application skeleton I have included all the nuts and bolts that I find myself using for every small web application or web service I create. They are (excluding Flask itself of course)

* Flask-SqlAlchemy
* Flask-Testing
* Flask-Script
* Flask-Migrate
