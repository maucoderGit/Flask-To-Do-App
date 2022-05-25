import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

credential = credentials.ApplicationDefault()
firebase_admin.initialize_app(credential)

db = firestore.client()

def get_users():
    return db.collection('users').get()


def get_user_by_id(username):
    return db.collection('users').document(username).get()


def get_todos(user_id):
    users = db.collection('users')
    todo = users.document(user_id).collection('To-Do').get()

    return todo