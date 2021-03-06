import requests
import lxml.html
import re
import cgi

### Helper functions for Inspektor ###

def encode_html(html):
    """Given string of html, removes <, >, and & and replaces with entities."""

    return cgi.escape(html)


def build_element_histogram(lxml_tree):
    """
    Given an lxml.html Tree, count number of elements and store as histogram.

    Returns dictionary where keys are elements and values are frequency.
    """
    count = {}

    # Iterate through all elements in Tree, depth-first
    for element in lxml_tree.iter():
        count[element.tag] = count.setdefault(element.tag, 0) + 1

    return count


def add_spans(encoded_html):
    """Given string of encoded html, wrap each element with a span and class of element tag.

    e.g. <span class="my-div">&lt;div id='sample'&gt;</span><br>
    """
    # TODO: this only wraps opening element tags in spans.
    # Will need to write separate regex search to handle closing tags.

    def add_span_class(matchobj):
        return "<span class=\"my-{elem}\">&lt;{elem}".format(elem=matchobj.group(1))

    # This is the regex pattern to find the element type: &lt;([A-Z|a-z]+[0-9]*)
    html = re.sub('&lt;([A-Z|a-z]+[0-9]*)', add_span_class, encoded_html)

    html = html.replace("&gt;", "&gt;</span><br>")

    return html


##### Dummy html #####

sample_html = '<div id="icons"> <ul> <li><a href="mailto:adriannenoelle@gmail.com"> <img src="img/gmail.png" class="icon" alt="gmail logo"></a> </li>'

t = encode_html(sample_html)

input_url = 'http://docs.python-guide.org/en/latest/scenarios/scrape/'

# Fetch HTML of input url, parse, and convert to Tree
tree = lxml.html.parse(input_url)
