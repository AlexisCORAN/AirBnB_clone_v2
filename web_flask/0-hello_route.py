#!/usr/bin/python3
"""
This module contains a class FLask
"""
from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def display_name():
    """ Prints 'Hello HBNB!' """
    return ('Hello HBNB!')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
