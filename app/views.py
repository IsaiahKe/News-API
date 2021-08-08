from datetime import date
from app.request import get_article, get_by_source
from flask import render_template
from app import app

@app.route('/')
def index():

    message="isaiah morara"
    timeframe= date.today()
    me=get_article('biden')
    return render_template('index.html',message=message,me=me)

@app.route('/source')
def source():
    '''
    define what is to be returned 
    '''
    us=get_by_source()
    return render_template('sources.html',us=us)