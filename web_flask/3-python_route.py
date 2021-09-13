#!/usr/bin/python3
"""
This module contains a class FLask
"""
from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def display_hello():
    """ Prints 'Hello HBNB!' """
    return ('Hello HBNB!')


@app.route('/hbnb', strict_slashes=False)
def display_hbnb():
    """ Prints 'HBNB' """
    return ('HBNB')


@app.route('/c/<text>', strict_slashes=False)
def display_Cisfun(text):
    """ Prints Cisfun """
    return ('C {}'.format(text.replace('_', ' ')))


@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def display_python(text='is cool'):
    """ Prints python """
    return ('Python {}'.format(text.replace('_', ' ')))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
