# Flask
from flask import (
    Flask,
    Response,
    escape,
    make_response,
    redirect,
    request,
    render_template
)

app = Flask(__name__)

todos = ['Buy Coffee', 'Make a video', 'Study at platzi']

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