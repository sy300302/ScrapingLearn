from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen('https://morvanzhou.github.io/static/scraping/list.html').read().decode('utf-8')
print(html)

soup = BeautifulSoup(html, features='lxml')
month = soup.find_all('li', {'class': 'month'})
for m in month:
    print(m.get_text())

jan = soup.find('ul', {'class': 'jan'})
d_jan = jan.find_all('li')
for d in d_jan:
    print(d.get_text())
