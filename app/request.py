from datetime import date
from app import app
from .models import article
from .models import source
import urllib.request,json

Article=article.Article
Source=source.Source
api_key=app.config['API_KEY']
path= app.config['API_PATH']
#source_path='https://newsapi.org/v2/top-headlines?sources={}&apiKey={}'
headline='https://newsapi.org/v2/top-headlines?country={}&apiKey={}'
all='https://newsapi.org/v2/top-headlines/sources?apiKey={}'
def get_article(content):
    get_url=path.format(content,api_key)
    with urllib.request.urlopen(get_url) as url:
      get_article_data=url.read()
      get_response=json.loads(get_article_data)
      
      get_results=None
      if get_response['articles']:
          get_response_list=get_response['articles']
          get_results=process_data(get_response_list)
          
    return get_results
          
def process_data(response):
    article_results=[]
    for article in response:
        source=article.get('source')
        title=article.get('title')
        author=article.get('author')
        description= article.get('description')
        url=article.get('url')
        content=article.get('content')
        publishedat=article.get('publishedAt')
        urltoimage=article.get('urlToImage')
        
        if urltoimage:
            article_object=Article(source,author,title,description,url,urltoimage,content,publishedat)
            article_results.append(article_object)
            
    return article_results
def get_by_source():
    get_url=all.format(api_key)
    with urllib.request.urlopen(get_url) as url:
        json_response=url.read()
        response=json.loads(json_response)
        
        get_data=None
        
        if response['sources']:
            get_sources=response['sources']
            get_data=maptosource(get_sources)
        
    return get_data
def maptosource(datamap):
    source_data=[]
    for source in datamap:
        id=source.get('id')
        name=source.get('name')
        description=source.get('description')
        url=source.get('url')
        category=source.get('category')
        language=source.get('language')
        country=source.get('country')
        
        if id:
            new_source=Source(id,name,description,url,category,language,country)
            source_data.append(new_source)
        
    return source_data