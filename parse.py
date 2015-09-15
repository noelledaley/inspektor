import urllib2
import lxml.html
input_url = 'http://noelledaley.github.io/'

# Fetch HTML of input url and store as string
response = urllib2.urlopen(input_url)
html = response.read()

# Convert HTML string to Tree
tree = lxml.html.fromstring(html)

def count_elements(tree):
    """Given an HTML Tree, count number of elements."""
    for element in tree.iter():
        print element.tag
