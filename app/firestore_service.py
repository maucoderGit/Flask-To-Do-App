from decouple import config as config_decouple
from app.config import config
import os

import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore


enviroment = config['development']
if config_decouple('PRODUCTION', default=False):
    enviroment = config['production']
    firebase_admin.initialize_app(option=os.environ['GOOGLE_APPLICATION_CREDENTIALS'])
else:
    credential = credentials.ApplicationDefault()
    firebase_admin.initialize_app(credential)

db = firestore.client()

def get_users():
    """
    Get users

    This function Get all users from firestore data base

    Parameters:
    - None

    Returns:
    - Firestore Collection
    """
    return db.collection('users').get()


def get_user_by_id(user_id):
    return db.collection('users').document(user_id).get()


def user_put(user_data):
    user_ref = db.collection('users').document(user_data._username)

    user_ref.set({
        'username': user_data._username,
        'password': user_data._password,
        'first_name': user_data.first_name,
        'last_name': user_data.last_name,
    })


# To-do

def get_todos(user_id: str) -> dict:
    users = db.collection('users')
    todo = users.document(user_id).collection('To-Do').get()

    return todo


def put_todo(user_id: str, description: str) -> None:
    todos_collection_red = db.collection('users')\
        .document(user_id)\
        .collection('To-Do')
    
    todos_collection_red.add({
        'Description': description,
        'done': False
    })


def delete_todo(user_id, todo_id):
    todo_ref = _get_todo_ref(user_id, todo_id)
    todo_ref.delete()

    # todo_ref = db.collection('users').collection('todos').document(todo_id)


def update_todo(user_id, todo_id, done):
    todo_done = not bool(done)
    todo_ref = _get_todo_ref(user_id, todo_id)

    todo_ref.update({
        'done': not done
    })


def _get_todo_ref(user_id, todo_id):
    return db.document(f'users/{user_id}/To-Do/{todo_id}')
