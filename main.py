import requests
from bs4 import BeautifulSoup

contents = requests.get('https://www.detik.com/terpopuler', params={'tag_from':'wp_cb_mostPopular_more'})
soup = BeautifulSoup(contents.text, "html.parser")
data = soup.find(attrs={'class': 'grid-row list-content'})

titles = data.findAll(attrs={'class': 'media__title'})
images = data.findAll(attrs={'class': 'media__image'})


for image in images:
    print(image.find('a').find('img')['title'])