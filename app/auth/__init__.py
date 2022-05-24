from flask import Blueprint

# app

auth = Blueprint('auth', __name__, url_prefix='/auth')

from . import views