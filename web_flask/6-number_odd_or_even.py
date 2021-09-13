#!/usr/bin/python3
"""
This module contains a class Flask
"""
from flask import Flask, render_template
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
    """
    Prints display “C ”, followed by the value
    of the text variable
    (replace underscore _ symbols with a space
    """
    return ('C {}'.format(text.replace('_', ' ')))


@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def display_python(text='is cool'):
    """
    Prints followed by the value
    of the text variable
    (replace underscore _ symbols with a space)
    """
    return ('Python {}'.format(text.replace('_', ' ')))


@app.route('/number/<int:n>', strict_slashes=False)
def display_number(n):
    """ display “n is a number” only if n is an integer """
    return ('{:d} is a number'.format(n))


@app.route('/number_template/<int:n>', strict_slashes=False)
def display_numbertemplate(n):
    """ display a HTML page only if n is an integer """
    return (render_template('5-number.html', n=n))


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def display_numberodd(n):
    """ display a HTML page only if n is an integer """

    if n % 2 == 0:
        evenness = 'even'
    else:
        evenness = 'odd'

    return render_template('6-number_odd_or_even.html', n=n,
                           evenness=evenness)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
