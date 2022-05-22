# Python
from os import urandom
from wtforms.fields import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired
import unittest

# Flask
from ensurepip import bootstrap
from flask import (
    Flask,
    Response,
    escape,
    flash,
    make_response,
    redirect,
    request,
    render_template,
    session,
    url_for
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
app.config['WTF_CSRF_ENABLED']= False


todos = ['Buy Coffee', 'Make a video', 'Study at platzi']

@app.cli.command()
def test():
    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner().run(tests)


@app.errorhandler(404)
def not_found(error):
    return render_template('404.html', error=error)


@app.errorhandler(500)
def server_error(error):
    return render_template('500.html', error=error)


@app.route('/')
def index() -> Response:
    user_ip: str | None = request.remote_addr

    response: Response = make_response(redirect('/home'))
    session['user_ip'] = user_ip

    return response


@app.route('/home', methods=['GET', 'POST'])
def home():
    user_ip = session.get('user_ip')
    login_form = LoginForm()
    username = session.get('username')

    context = {
        'user_ip': user_ip,
        'todos': todos,
        'login_form': login_form,
        'username': username
    }

    if login_form.validate_on_submit():
        username = login_form.username.data
        session['username'] = username

        flash('Username registed successfully')

        return redirect(url_for('index'))

    return render_template('home.html', **context)


if __name__ == '__main__':
    app.run(port = 5000, debug = True)