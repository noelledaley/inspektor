import requests
import lxml.html
input_url = 'http://docs.python-guide.org/en/latest/scenarios/scrape/'

# Fetch HTML of input url and store as unicode
page = requests.get(input_url)

# Convert HTML unicode to Tree
tree = lxml.html.fromstring(page.text)

def count_elements(tree):
    """Given an HTML Tree, count number of elements."""
    count = {}

    for element in tree.iter():
        count[element.tag] = count.setdefault(element.tag, 0) + 1

    return count
