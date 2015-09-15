from flask import Flask, render_template, request
from jinja2 import StrictUndefined
from parse import build_element_histogram
import os
import requests
import lxml.html

app = Flask(__name__)
app.secret_key = os.environ['FLASK_TOKEN']
app.jinja_env.undefined = StrictUndefined


### Routes ###

@app.route('/')
def index():
    """Return index page."""

    return render_template('index.html')


@app.route('/results', methods=['POST'])
def fetch_html():
    """Given URL, fetch html, parse it, and store elements and frequencies as a Python dictionary."""

    input_url = request.form.get('input_url')

    # Fetch HTML of input url and store as unicode
    page = requests.get(input_url)
    raw_html = page.text

    # Convert HTML unicode to Tree
    tree = lxml.html.fromstring(page.text)

    # Get histogram of element frequencies
    frequency = build_element_histogram(tree)

    return render_template('results.html', frequency=frequency, raw_html=raw_html)


if __name__ == '__main__':
    app.debug = True
    app.run()
