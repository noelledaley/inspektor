import urllib2
from flask import Flask, render_template
import os

app = Flask(__name__)
app.secret_key = os.environ['FLASK_TOKEN']

response = urllib2.urlopen('http://pythonforbeginners.com/')
html = response.read()

html_list = html.split(">")

print html_list[0], html_list[1], html_list[2]

# print html

if name if __name__ == '__main__':
