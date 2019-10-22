from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import random

base_url = 'https://baike.baidu.com'
# his = ['/item/%E7%BD%91%E7%BB%9C%E7%88%AC%E8%99%AB']
his = ['/item/%E5%BC%B9%E7%B0%A7%E6%8C%AF%E5%AD%90']

for i in range(20):
    url = base_url + his[-1]

    html = urlopen(url).read().decode()
    soup = BeautifulSoup(html, features='lxml')
    print(soup.find('h1').get_text(), '    url:', his[-1])

    sub_urls = soup.find_all('a', {'target': '_blank', 'href': re.compile(r'^/item/(%.{2})+$')})

    if len(sub_urls) != 0:
        his.append(random.sample(sub_urls, 1)[0]['href'])
    else:
        his.pop()

