from os import urandom
from decouple import config


class Config:
    SECRET_KEY = urandom(40)
    PRESERVE_CONTEXT_ON_EXCEPTION = False
    FLASK_APP="main.py"
    GOOGLE_CLOUD_PROJECT='my-flask-to-do-list'


class DevelopmentConfig(Config):
    DEBUG = True
    FLASK_DEBUG=1
    

class ProductionConfig(Config):
    DEBUG = False
    FLASK_DEBUG=0

config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig
}