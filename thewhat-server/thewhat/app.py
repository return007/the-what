#!/usr/bin/env python
"""
Server to expose theWHATs
"""

from flask import Flask, render_template
from thewhat.content import give_one


application = Flask(__name__)


@application.route("/")
def index():
    return render_template("index.html")


@application.route('/random')
def random():
    return give_one()


def main():
    application.run("0.0.0.0")


if __name__ == "__main__":
    main()
