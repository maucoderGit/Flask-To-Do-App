from flask import flash, redirect, render_template, session, url_for
from flask_login import current_user, login_required, login_user, logout_user

from app.models import UserData, UserModel
from . import auth
from app.forms import LoginForm
from app.firestore_service import get_user_by_id

@auth.route('/login', methods=['GET','POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
        
    login_form = LoginForm()
    context: dict = {
        'login_form': login_form
    }

    if login_form.validate_on_submit():
        username = login_form.username.data
        password = login_form.password.data

        user_doc = get_user_by_id(username)
        
        if user_doc.to_dict():
            password_from_db = user_doc.to_dict()['password']
            
            if password == password_from_db:
                user_data = UserData()

                user_data.username = username
                user_data.password = password

                user = UserModel(user_data)

                login_user(user)

                flash('Welcome again')

                redirect(url_for('home'))
            else:
                flash('Username or password is wrong!')
        else:
            flash('This user doesn\'t exist')

    
        return redirect(url_for('index'))

    return render_template('login.html', **context)


@auth.route('logout')
@login_required
def logout():
    logout_user()
    flash('See you later, space cowboy')

    return redirect(url_for('auth.login'))