import urllib2

response = urllib2.urlopen('http://pythonforbeginners.com/')
html = response.read()

html_list = html.split(">")

print html_list[0], html_list[1], html_list[2]

# print html
