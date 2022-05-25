from flask import flash, redirect, render_template, session, url_for
from . import auth
from app.forms import LoginForm

@auth.route('/login', methods=['GET','POST'])
def login():
    login_form = LoginForm()
    context: dict = {
        'login_form': login_form
    }

    if login_form.validate_on_submit():
        username = login_form.username.data
        session['username'] = username
    
        flash('Username registed successfully')
    
        return redirect(url_for('index'))

    return render_template('login.html', **context)