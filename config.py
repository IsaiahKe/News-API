
class Config:
    API_PATH='https://newsapi.org/v2/top-headlines?country=us&apiKey={}'
    
class DevConfig(Config):
    
    DEBUG=True
    
class ProdConfig(Config):
    pass

config_options={
    'develpoment':DevConfig,
    'production':ProdConfig
}