from uuid import UUID
from flask_login import UserMixin

# firestore
from .firestore_service import get_user_by_id

class UserData:
    def __init__(self):
        self._username: str = ''
        self._password: str = ''
        self.first_name: str = ''
        self.last_name: str = ''

    @property
    def username(self) -> str:
        return self._username

    @username.setter
    def username(self, username: str) -> str:
        if len(username) > 40:
            raise ValueError("Sorry, select a short username")
        self._username = username

    @property
    def password(self) -> str:
        return self._username

    @username.setter
    def password(self, password) -> str:
        if len(password) > 8:
            raise ValueError('Min password\'s length is 8')
        self.password = password

    @property
    def first_name(self):
        return self.first_name

    @first_name.setter
    def first_name(self, first_name):
        self.first_name = first_name

    @property
    def last_name(self):
        return self.last_name

    @last_name.setter
    def last_name(self, last_name):
        self.last_name = last_name


class UserModel(UserMixin):
    """
        User Model

        User Model Class Creates an object
    
        params:
        user_data: UserData
    """
    def __init__(self, user_data):
        self.id = UUID(bytes=40)
        self._password = user_data._password

    @staticmethod
    def query(user_id):
        user_doc = get_user_by_id(user_id)
        user_data = UserData(
            user_id=user_doc.id,
            password=user_doc.to_dict()['password']
        )

        return UserModel(user_data)