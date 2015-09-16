import requests
import lxml.html
import re
import cgi

input_url = 'http://docs.python-guide.org/en/latest/scenarios/scrape/'

# Fetch HTML of input url, parse, and convert to Tree
tree = lxml.html.parse(input_url)

def encode_html(html):
    """Given string of html, removes <, >, and & and replaces with entities."""

    return cgi.escape(html)


def build_element_histogram(tree):
    """
    Given an HTML Tree, count number of elements and store as histogram.

    Returns dictionary where keys are elements and values are frequency.
    """
    count = {}

    # Iterate through all elements in Tree, depth-first
    for element in tree.iter():
        count[element.tag] = count.setdefault(element.tag, 0) + 1

    return count

sample_html = '<div id="icons"> <ul> <li><a href="mailto:adriannenoelle@gmail.com"> <img src="img/gmail.png" class="icon" alt="gmail logo"></a> </li>'

t = encode_html(sample_html)

def add_spans(decoded_html):

    # Split decoded_html on closing bracket
    elements = decoded_html.split('&gt;')

    spans = []

    for element in elements:
        # Wrap element in span and code tags
        span = '<span class="%s"><code>%s&gt;</code></span>' % (element, element)
        spans.append(span)

    html = "".join(spans)
    # returns HTML as string
    return html

# sub()	Find all substrings where the RE matches, and replace them with a different string
