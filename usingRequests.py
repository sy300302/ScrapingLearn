import requests
import webbrowser

param = {'wd': '莫烦Python'}
r = requests.get('https://www.baidu.com/s', params=param)
print(r.url)
# webbrowser.open(r.url)

data = {'firstname': '莫烦', 'lastname': '周'}
r = requests.post('http://pythonscraping.com/pages/files/processing.php', data=data)
print(r.text)

file = {'uploadFile': open('./images/Capture.PNG', 'rb')}
r = requests.post('http://pythonscraping.com/pages/files/processing2.php', files=file)
print(r.text)

payload = {'username': 'Morvan', 'password': 'password'}
r = requests.post('http://pythonscraping.com/pages/cookies/welcome.php', data=payload)
print(r.cookies.get_dict())

# this page is not found any more
r = requests.get('http://pythonscraping.com/pages/cookies/profile.php', cookies=r.cookies)
print(r.text)

session = requests.Session()
payload = {'username': 'Morvan', 'password': 'password'}
r = session.post('http://pythonscraping.com/pages/cookies/welcome.php', data=payload)
print(r.cookies.get_dict())

# this page is not found any more
r = session.get('http://pythonscraping.com/pages/cookies/profile.php')
print(r.text)
