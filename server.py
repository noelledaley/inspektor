from flask import Flask, render_template
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


@app.route('/search')
def fetch_html():

    response = urllib2.urlopen('http://pythonforbeginners.com/')
    html = response.read()

    html_list = html.split(">")

    print html_list[0], html_list[1], html_list[2]

    return html

if __name__ == '__main__':
    app.run()
