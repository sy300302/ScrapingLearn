from urllib.request import urlopen
import re

# if there is Chinese inside, should decode
html = urlopen('https://morvanzhou.github.io/static/scraping/basic-structure.html').read().decode('utf-8')
print(html)

# find title
res = re.findall(r'<title>(.+?)</title>', html)
print('\nPage title is: ', res[0])

# find paragraph
res = re.findall(r'<p>(.+?)</p>', html, re.DOTALL)
print('\nPage paragraph is:', res[0])

# find links
res = re.findall(r'href="(.+?)"', html)
print('\nPage all links are: \n', res)