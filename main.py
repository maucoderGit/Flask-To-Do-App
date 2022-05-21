# Flask
from ensurepip import bootstrap
from flask import (
    Flask,
    Response,
    escape,
    make_response,
    redirect,
    request,
    render_template
)
from flask_bootstrap import Bootstrap

app = Flask(__name__)
bootstrap: Bootstrap = Bootstrap(app)

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
    response.set_cookie('user_ip', user_ip)

    return response


@app.route('/hello')
def home() -> str:
    user_ip = request.cookies.get('user_ip')
    user_ip = escape(user_ip)

    context: dict = {
        'user_ip': user_ip,
        'todos': todos,
        "title": "Welcome"
    }

    return render_template('hello.html', **context)


if __name__ == '__main__':
    app.run(port = 5000, debug = True)