from bs4 import BeautifulSoup
import json
import logging
from flask import Response, request, Flask, jsonify
import requests
from utils import response, dateFormatter


def searchNews(parameter):
    urlWho = "https://brazilian.report/?s=" + parameter + "&wordsMode=AllWords"
    page = requests.get(urlWho)
    soup = BeautifulSoup(page.text, 'html.parser')
    
    headNewsWho = soup.find_all(class_='heading')

    dateNewsWho = soup.find_all(class_='date')

    textNewsWho = soup.find_all(class_='text-underline')

    linksWho = soup.find_all(class_='link-container')

    list = {"news": []}
    
    for i in range(0, len(headNewsWho)):
        list["news"].append(
            {
            'title': headNewsWho[i].text,
            'text': textNewsWho[i].text,
            'link': linksWho[i].get('href'),
            'date': dateFormatter.formatDateWHO(dateNewsWho[i]),
            'language': 'eng',
            'font': 'who'
            }
        )
    return list
