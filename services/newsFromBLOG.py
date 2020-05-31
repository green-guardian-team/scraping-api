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
    
    headNewsblog = soup.find_all(class_='heading')

    dateNewsblog = soup.find_all(class_='ml-5')

    textNewsblog = soup.find_all(class_='title mb-4')

    linksblog = soup.find_all(class_='title mb-4')

    list = {"news": []}
    
    for i in range(0, len(headNewsWho)):
        list["news"].append(
            {
            'title': headNewsblog[i].text,
            'text': textNewsblog[i].text,
            'link': str(linksblog[i].parent.get('href')),
            'date': dateFormatter.formatDateblog(dateNewsblog[i]),
            'language': 'eng',
            'font': 'who'
            }
        )
    return list