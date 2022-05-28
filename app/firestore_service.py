import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

credential = credentials.ApplicationDefault()
firebase_admin.initialize_app(credential)

db= firestore.client()

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
        'description': description
    })