import os
class Config:
    API_PATH='https://newsapi.org/v2/top-headlines?country=us&apiKey={}'
    API_KEY=os.environ.get('API_KEY')
    SECRET_KEY=os.environ.get('SECRET_KEY')
   
class DevConfig(Config):
    
    DEBUG=True
    
class ProdConfig(Config):
    pass

config_options = {
'development':DevConfig,
'production':ProdConfig
}