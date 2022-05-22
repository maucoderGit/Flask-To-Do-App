# Python
from os import urandom
from wtforms.fields import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired

# Flask
from ensurepip import bootstrap
from flask import (
    Flask,
    Response,
    escape,
    make_response,
    redirect,
    request,
    render_template,
    session
)
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Send')


app: Flask = Flask(__name__)
bootstrap: Bootstrap = Bootstrap(app)

app.config['SECRET_KEY'] = urandom(20)


todos = ['Buy Coffee', 'Make a video', 'Study at platzi']

@app.errorhandler(404)
def not_found(error):
    return render_template('404.html', error=error)


@app.errorhandler(500)
def server_error(error):
    return render_template('500.html', error=error)


@app.route('/')
def index() -> Response:
    user_ip: str | None = request.remote_addr

    response: Response = make_response(redirect('/hello'))
    session['user_ip'] = user_ip

    return response


@app.route('/hello')
def home() -> str:
    user_ip = session.get('user_ip')
    user_ip = escape(user_ip)

    login_form = LoginForm()
    context: dict = {
        'user_ip': user_ip,
        'todos': todos,
        "title": "Welcome",
        'login_form': login_form
    }

    return render_template('hello.html', **context)


if __name__ == '__main__':
    app.run(port = 5000, debug = True)