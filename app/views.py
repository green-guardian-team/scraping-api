from app import app
import requests
from bs4 import BeautifulSoup
import json
from flask import Response


@app.route('/')
def home():
    page = requests.get('https://web.archive.org/web/20121007172955/https://www.nga.gov/collection/anZ1.htm')
    soup = BeautifulSoup(page.text, 'html.parser')

    artist_name_list = soup.find(class_='BodyText')
    artist_name_list_items = artist_name_list.find_all('a')
    list = []
    for artist_name in artist_name_list_items:
        list.append(artist_name.prettify())
        
    return json.dumps(list)
