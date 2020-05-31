from bs4 import BeautifulSoup
import json
import logging
from flask import Response, request, Flask, jsonify
import requests
from app import app
from utils import response, dateFormatter
<<<<<<< HEAD
from services import newsFromWHO, newsFromGlobo, NewFromGOV
=======
from services import newsFromWHO
>>>>>>> parent of 31d9b66... Merge pull request #4 from green-guardian-team/develop/news

@app.route('/api/news/', methods=['GET'])
def news():
    try:
        parameter =  request.args.get('parameter', 'covid')
        
        resultWHO = newsFromWHO.searchNews(parameter)
<<<<<<< HEAD
        resultGlobo = newsFromGlobo.searchNews(parameter)
        resultGOV = NewFromGOV.searchNews(parameter)
=======
>>>>>>> parent of 31d9b66... Merge pull request #4 from green-guardian-team/develop/news

        list = {"news": []}

        for i in range(0, len(resultWHO)):
            list["news"].append(resultWHO[i])


        for i in range(0, len(resultGOV)):
            list["news"].append(resultGOV[i])



        return response.response(list)
        

    except Exception as e:
        return str(e)