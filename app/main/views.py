
from instance.config import API_KEY
from ..request import get_article, get_by_category, get_by_source
from flask import render_template
from . import main

@main.route('/')
def index():

    me=get_article()
    sources=get_by_source()
    return render_template('index.html',me=me,sources=sources)

@main.route('/source')
def source():
    '''
    define what is to be returned 
    '''
    us=get_by_source()
    return render_template('sources.html',us=us)

@main.route('/category/<type>')
def category(type):
    category=get_by_category('us',type)
    heading=type
    return render_template('category.html',category=category,heading=heading)