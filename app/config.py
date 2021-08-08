class Config:
    API_PATH='https://newsapi.org/v2/everything?q={}&apiKey={}'
    
class DevConfig(Config):
    
    DEBUG=True
class ProdConfig(Config):
    pass