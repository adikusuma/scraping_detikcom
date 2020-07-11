import requests
from bs4 import BeautifulSoup
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('base.html')


@app.route('/detik-popular')
def detik_popular():
    contents = requests.get('https://www.detik.com/terpopuler', params={'tag_from': 'wp_cb_mostPopular_more'})
    soup = BeautifulSoup(contents.text, "html.parser")
    data = soup.find(attrs={'class': 'grid-row list-content'})

    titles = data.findAll(attrs={'class': 'media__title'})
    images = data.findAll(attrs={'class': 'media__image'})

    return render_template('detikscraper.html', images = images)

@app.route('/idr-rates')
def idr_rates():
    source = requests.get('http://www.floatrates.com/daily/idr.json')
    json_data = source.json()
    return render_template('idr-rates.html', datas = json_data.values())


if __name__ == '__main__':
    app.run(debug=True)



