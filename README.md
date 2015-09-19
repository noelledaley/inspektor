# Inspektor
Inspektor helps users analyze the HTML of a URL without using the developer console. Simply enter a URL to be parsed and the underlying HTML will be displayed along with a table containing the frequency of each element. Click on the elements in the table to highlight the corresponding elements within the html.

http://inspektor.herokuapp.com/

![Homepage](/static/home.png)
![Results](/static/results.png)

### Technologies
- Python
- Flask
- [LXML](http://lxml.de/lxmlhtml.html)
- [Regular Expressions](https://docs.python.org/2/library/re.html)
- [CGI](https://wiki.python.org/moin/EscapingHtml)
- Bootstrap

### Parsing HTML
To fetch and parse HTML I used a combination of the requests library and lxml.html. In particular, lxml.html has a method called fromstring(), which I used to pass in html. fromstring() returns a tree object containing each HTML element as a node. From here, I iterated through the tree to build my histogram.

Next, to render the raw html on the results page I had to first encode the HTML, removing all opening and closing brackets. From here, I wrapped each element tag in a span using regular expressions. With spans in place I used jQuery to add event listeners to each row in the table and toggle the highlight class accordingly.

### Challenges
The most challenging aspect of this project was determining how to programmatically parse the HTML and add spans containing the element tag. There are a number of different ways to do this. In the few days I spent working on this project, I encountered many potential tools like [LXML](http://lxml.de/lxmlhtml.html), [Beautiful Soup](http://www.crummy.com/software/BeautifulSoup/), [Regular Expressions](https://docs.python.org/2/library/re.html), and the [HTMLParser](https://docs.python.org/2/library/htmlparser.html). However after reading some of the documentation, I decided that LXML and Regular Expressions would be my best option because they were lightweight, efficient, and relatively easy to implement.

#### Future Improvements
- Currently, I'm using 2 different tools to create the histogram and format the html for viewing. If I had more time to expand this project, I'd look more into BeautifulSoup to see if I could use it as my all-in-one solution.
- Only opening element tags are able to be highlighted. Will need to write separate regex search & substitution to handle closing tags.
- Add ability to sort histogram table
