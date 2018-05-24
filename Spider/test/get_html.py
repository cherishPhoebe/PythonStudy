from urllib.request import urlopen

html = urlopen('http://jr.jd.com')
print(html.read())
html.close()
