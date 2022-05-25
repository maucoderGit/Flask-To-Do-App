# Python
import unittest

from app import create_app
from app.forms import LoginForm
from app.firestore_service import get_todos, get_users

# Flask
from flask import (
    Response,
    flash,
    make_response,
    redirect,
    request,
    render_template,
    session,
    url_for
)

app = create_app()

app.config['WTF_CSRF_ENABLED']= False


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


@app.route('/home', methods=['GET'])
def home():
    user_ip = session.get('user_ip')
    username = session.get('username')

    context = {
        'user_ip': user_ip,
        'todos': get_todos(user_id=username),
        'username': username
    }

    users = get_users()

    for user in users:
        print(user.id)
        print(user.to_dict()['password'])

    return render_template('home.html', **context)



if __name__ == '__main__':
    app.run(port = 5000, debug = True)