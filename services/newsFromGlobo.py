from bs4 import BeautifulSoup
import json
import logging
from flask import Response, request, Flask, jsonify
import requests
from utils import response, dateFormatter


def searchNews(parameter):
    urlGlobo = "https://g1.globo.com/busca/?q="+parameter
    page = requests.get(urlGlobo)
    soup = BeautifulSoup(page.text, 'html.parser')
    
    headNewsGlobo = soup.find_all(class_='widget--info__title product-color')
        
    dateNewsGlobo = soup.find_all(class_='widget--info__meta')

    textNewsGlobo = soup.find_all(class_='widget--info__description')

    linksGlobo = soup.find_all(class_='widget--info__title product-color')

    fontFromGlobo = soup.find_all(class_='widget--info__header')

    list = []
    
    for i in range(0, len(headNewsGlobo)):

        list.append(
            {
            'title': headNewsGlobo[i].text,
            'text': textNewsGlobo[i].text,
            'link': str(linksGlobo[i].parent.get('href')),
            'date': dateNewsGlobo[i].text,
            'language': 'pt',
            'font': fontFromGlobo[i].text
            }
        )
    return list
