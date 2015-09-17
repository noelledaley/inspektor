from flask import Flask, render_template, request, Markup
from jinja2 import StrictUndefined
from parse import build_element_histogram, encode_html, add_spans
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
    html = page.text

    # Remove HTML entities from html to display on page
    raw_html = encode_html(html)

    # Add spans to each element so jQuery can select and apply highlight class
    # TODO: the span classes currently added have extra information on them.
        # Need to figure out how to strip so only element name is added.
        # e.g. <span class='div id="icons"'><code>&lt;div id="icons"&gt;</code></span>
        # >>> <span class="div"><code>&lt;div id="icons"&gt;</code></span>
    span_html = add_spans(raw_html)

    # Convert HTML unicode to Tree
    tree = lxml.html.fromstring(page.text)

    # Get histogram of element frequencies
    frequency = build_element_histogram(tree)

    return render_template('results.html', frequency=frequency, raw_html=html)


@app.route('/prototype')
def show_prototype():
    """Display prototype."""

    return render_template('prototype.html')


if __name__ == '__main__':
    app.debug = True
    app.run()
