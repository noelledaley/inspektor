import urllib2

response = urllib2.urlopen('http://pythonforbeginners.com/')
html = response.read()

print html
