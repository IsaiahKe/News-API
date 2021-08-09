from datetime import date
from app.request import get_article, get_by_category, get_by_source
from flask import render_template
from app import app

@app.route('/')
def index():

    message="isaiah morara"
    timeframe= date.today()
    me=get_article()
    sources=get_by_source()
    return render_template('index.html',message=message,me=me,sources=sources)

@app.route('/source')
def source():
    '''
    define what is to be returned 
    '''
    us=get_by_source()
    return render_template('sources.html',us=us)

@app.route('/category/<type>')
def category(type):
    category=get_by_category('us',type)
    heading=type
    return render_template('category.html',category=category,heading=heading)