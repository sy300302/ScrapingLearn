from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen('https://morvanzhou.github.io/static/scraping/basic-structure.html').read().decode('utf-8')
print(html)

soup = BeautifulSoup(html, features='lxml')
print(soup.h1)
print(soup.p)

all_a = soup.find_all('a')
all_href = [a['href'] for a in all_a]
print(all_href)
