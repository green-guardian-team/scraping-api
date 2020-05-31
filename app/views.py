from app import app
import requests
from bs4 import BeautifulSoup
import json
from flask import Response


@app.route('/news/<parameter>')
def news(parameter):
    url = "https://www.who.int/news-room/detail/search-results?indexCatalogue=genericsearchindex1&searchQuery=" + parameter + "e&wordsMode=AllWords"
    return url
    page = requests.get(url)
    soup = BeautifulSoup(page.text, 'html.parser')

    artist_name_list = soup.find(class_='BodyText')
    artist_name_list_items = artist_name_list.find_all('a')
    list = []
    for artist_name in artist_name_list_items:
        list.append(artist_name.prettify())
        
    return json.dumps(list)
