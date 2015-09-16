import requests
import lxml.html
import re
import cgi

input_url = 'http://docs.python-guide.org/en/latest/scenarios/scrape/'

# Fetch HTML of input url, parse, and convert to Tree
tree = lxml.html.parse(input_url)

def decode_html(html):

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

# sub()	Find all substrings where the RE matches, and replace them with a different string
