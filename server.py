from flask import Flask, render_template, request
from jinja2 import StrictUndefined
import urllib2
import os

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
    """Given URL, fetch html and render as a string."""

    input_url = request.form.get('input_url')

    response = urllib2.urlopen(input_url)
    html = response.read()

    html_list = html.split(">")

    print html_list[0], html_list[1], html_list[2]

    return render_template('results.html', html=html)


if __name__ == '__main__':
    app.debug = True
    app.run()
