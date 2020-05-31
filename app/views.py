  
from bs4 import BeautifulSoup
import json
import logging
from flask import Response, request, Flask, jsonify
import requests
from app import app
from utils import response, dateFormatter
from services import newsFromWHO
from services import newsFromblog

@app.route('/api/news/', methods=['GET'])
def news():
    try:
        parameter =  request.args.get('parameter', 'covid')

        resultWHO = newsFromWHO.searchNews(parameter)

        return response.response(resultWHO)
        

    except Exception as e:
        return str(e)
        

def newsnew():
    try:
        parameterblog =  request.args.get('parameter', 'covid')

        resultblog = newsFromblog.searchNews(parameterblog)

        return response.response(resultblog)
        

    except Exception as e:
        return str(e)