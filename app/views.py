from bs4 import BeautifulSoup
import json
import logging
from flask import Response, request, Flask, jsonify
import requests
from app import app
from utils import response, dateFormatter
from services import newsFromWHO, newsFromGlobo

@app.route('/api/news/', methods=['GET'])
def news():
    try:
        parameter =  request.args.get('parameter', 'covid')
        
        resultWHO = newsFromWHO.searchNews(parameter)
        resultGlobo = newsFromGlobo.searchNews(parameter)

        list = {"news": []}

        for i in range(0, len(resultWHO)):
            list["news"].append(resultWHO[i])

        for i in range(0, len(resultGlobo)):
            list["news"].append(resultGlobo[i])

        return response.response(list)
        

    except Exception as e:
        return str(e)