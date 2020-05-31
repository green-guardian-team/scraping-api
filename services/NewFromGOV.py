from bs4 import BeautifulSoup
import json
import logging
from flask import Response, request, Flask, jsonify
import requests
from utils import response, dateFormatter


def searchNews(parameter):
    urlGOV = "https://www.cdc.gov/coronavirus/2019-ncov/whats-new-all.html"
    page = requests.get(urlGOV)
    soup = BeautifulSoup(page.text, 'html.parser')
    
    headNewsGOV = soup.find_all(class_='syndicate')
        
    dateNewsGOV = soup.find_all(class_='red-color feed-item-date')

    textNewsGOV = soup.find_all(class_='list-bullet feed-item-list')

    linksGOV = soup.find_all(class_='2019coronaviruswhatsnew')


    list = []
    
    for i in range(0, len(headNewsGOV)):

        list.append(
            {
            'title': headNewsGOV[i].text,
            'text': textNewsGOV[i].text,
            'link': str(linksGOV[i].parent.get('href')),
            'date': dateNewsGOV[i].text,
            'language': 'eng',
            'font': "cdc"
            }
        )
    return list
