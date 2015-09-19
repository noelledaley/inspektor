from flask import Flask, render_template, request, Markup, redirect, flash
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

    try:
        # Fetch HTML of input url and store as unicode
        page = requests.get(input_url)

    except (requests.exceptions.ConnectionError, requests.exceptions.InvalidURL):
        flash('The URL you entered is either invalid or unavailable. Try again!')
        return redirect('/')

    else:
        html = page.text

        # Replace <, > with HTML entities to display on page
        raw_html = encode_html(html)

        # Add spans to each element so jQuery can select and apply highlight class
        # Have to pass raw_html as Markup object to properly display
        span_html = Markup(add_spans(raw_html))

        # Convert HTML unicode to lxml Tree, build element histogram
        tree = lxml.html.fromstring(page.text)
        frequency = build_element_histogram(tree)

        # Keep track of URL, omitting http:// prefix
        display_url = input_url[7:]

        return render_template('results.html', frequency=frequency, raw_html=span_html, website=display_url)


@app.route('/prototype')
def show_prototype():
    """Display prototype."""

    return render_template('prototype.html')


if __name__ == '__main__':
    PORT = int(os.environ.get("PORT", 5000))
    DEBUG = "NO_DEBUG" not in os.environ

    app.run(debug=DEBUG, host="0.0.0.0", port=PORT)
