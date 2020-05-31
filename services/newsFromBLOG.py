from bs4 import BeautifulSoup
import json
import logging
from flask import Response, request, Flask, jsonify
import requests
from utils import response, dateFormatter


def searchNews(parameter):
    urlBrazilianReport = "https://brazilian.report/?s="+parameter
    page = requests.get(urlBrazilianReport)
    soup = BeautifulSoup(page.text, 'html.parser')
    
    headNewsBlog = soup.find_all(class_='alm-reveal')

    tags = soup.find_all(class_='title mb-3')

    return str(tags)

    dateNewsblog = soup.find_all(class_='ml-5')

    textNewsblog = soup.find_all(class_='title mb-4')

    linksblog = soup.find_all(class_='title mb-4')

    list = []
    
    for i in range(0, len(headNewsBlog)):
        list.append(
            {
            'title': headNewsBlog[i].text,
            'text': textNewsblog[i].text,
            'link': str(linksblog[i].parent.get('href')),
            'date': dateNewsblog[i].text,
            'language': 'eng',
            'font': 'brazilian report'
            }
        )
    return list