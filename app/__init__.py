from config import config_options
from flask import Flask
from flask_bootstrap import Bootstrap

bootstrap=Bootstrap()

def create_app(config_name):
    #initialize app
    app= Flask(__name__)
    app.config.from_object(config_options[config_name])
    
    #initialize app with bootstrap
    bootstrap.init_app(app)
    
    #register main blue print
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)
    
    #setting configurations
    from .request import config_request
    config_request(app)
    
    return app
    
