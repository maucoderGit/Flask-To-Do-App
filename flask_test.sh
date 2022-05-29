#!/bin/bash

source venv/bin/activate
pip install -r requirements.txt

export FLASK_APP=main.py
export FLASK_DEBUG=1
export FLASK_ENV=development
export GOOGLE_CLOUD_PROJECT='my-flask-to-do-list'

flask run
