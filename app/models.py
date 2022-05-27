from uuid import uuid4
from flask_login import UserMixin

# firestore
from .firestore_service import get_user_by_id

class UserData:
    def __init__(self):
        self._username: str
        self._password: str
        self._first_name: str
        self._last_name: str

    @property
    def username(self) -> str:
        return self._username

    @username.setter
    def username(self, value: str) -> str:
        if len(value) > 40:
            raise ValueError("Sorry, select a short username")
        self._username = value

    @property
    def password(self) -> str:
        return self._password

    @username.setter
    def password(self, value) -> str:
        if len(value) < 8:
            raise ValueError('Min password\'s length is 8')
        self._password = value

    @property
    def first_name(self):
        return self._first_name

    @first_name.setter
    def first_name(self, value):
        self._first_name = value

    @property
    def last_name(self):
        return self._last_name

    @last_name.setter
    def last_name(self, value):
        self._last_name = value


class UserModel(UserMixin):
    """
        User Model

        User Model Class Creates an object
    
        params:
        user_data: UserData
    """
    def __init__(self, user_data):
        self.id = user_data._username
        self._password = user_data._password

    @staticmethod
    def query(user_id):
        user_doc = get_user_by_id(user_id)
        user_data = UserData()

        user_data._username = user_doc.id
        user_data._password = user_doc.to_dict()['password']

        return UserModel(user_data)