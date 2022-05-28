# Python
import unittest

from app import create_app
from app.forms import LoginForm, ToDoForm
from app.firestore_service import get_todos, get_users, put_todo

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
from flask_login import current_user, login_required

app = create_app()

app.config['WTF_CSRF_ENABLED'] = False


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
@login_required
def home():
    user_ip = session.get('user_ip')
    username = current_user.id
    todo_form = ToDoForm()

    context = {
        'user_ip': user_ip,
        'todos': get_todos(user_id=username),
        'todo_form': todo_form,
        'username': username
    }

    if todo_form.validate_on_submit():
        put_todo(user_id= username, description=todo_form.description.data)

        flash('Your task was added sucessfully!')

        return redirect(url_for('home'))

    return render_template('home.html', **context)



if __name__ == '__main__':
    app.run(port = 5000, debug = True)