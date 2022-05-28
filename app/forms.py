from uuid import uuid4
from flask_wtf import FlaskForm
from wtforms.fields import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])

class SingupForm(LoginForm):
    first_name = StringField('First name', validators=[DataRequired()])
    last_name = StringField('Last_name', validators=[DataRequired()])
    submit = SubmitField('Send')

class Login(LoginForm):
    submit = SubmitField('Send')

class ToDoForm(FlaskForm):
    Description: str = StringField('Description', validators=[DataRequired()])
    submit = SubmitField('Add')

class DeleteTodoForm(FlaskForm):
    submit = SubmitField('Delete')
