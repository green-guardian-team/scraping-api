import flask
import json

def response(content):
    resp = flask.Response(json.dumps(content))
    resp.headers["Access-Control-Allow-Origin"] = "*"
    return resp