import requests

src = '/static/img/description/learning_step_flowchart.png'
host = 'https://morvanzhou.github.io'

IMAGE_URL = host+src

r = requests.get(IMAGE_URL, stream=True)
with open('./images/learning_roadmap.png', 'wb') as f:
    for chunk in r.iter_content(chunk_size=32):
        f.write(chunk)
