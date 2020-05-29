from app import app
from flask import redirect


@app.route('/')
def home():
    return redirect('http://google.com')
