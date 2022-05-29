from os import urandom
from decouple import config


class Config:
    SECRET_KEY = urandom(40)
    PRESERVE_CONTEXT_ON_EXCEPTION = False


class DevelopmentConfig(Config):
    DEBUG = True
    FLASK_APP="main.py"
    FLASK_DEBUG=1
    GOOGLE_CLOUD_PROJECT='my-flask-to-do-list'

class ProductionConfig(Config):
    DEBUG = False
    FLASK_DEBUG=0
    GOOGLE_CLOUD_PROJECT='my-flask-to-do-list'

config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig
}