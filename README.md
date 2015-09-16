# Inspektor
Inspektor helps users analyze the HTML of a URL without using the developer console. Simply enter a URL to be parsed and the underlying HTML will be displayed along with a table containing the frequency of each element.

### Technologies
- Python
- Flask
- [LXML](http://lxml.de/lxmlhtml.html)
- Bootstrap

### Parsing HTML
To fetch and parse HTML I used a combination of the requests library and lxml.html. In particular, lxml.html has a method called fromstring(), which I used to pass in html. fromstring() returns a tree object containing each HTML element as a node. From here, I iterated through the tree to build my historgram.
