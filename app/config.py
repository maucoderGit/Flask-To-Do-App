from os import urandom

class Config:
    SECRET_KEY = urandom(40)
    PRESERVE_CONTEXT_ON_EXCEPTION = False