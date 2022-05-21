# Flask
from flask import Flask, Response, escape, make_response, redirect, request

app = Flask(__name__)

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

    return f'Hello World, This IP is {user_ip}'


if __name__ == '__main__':
    app.run(port = 5000, debug = True)