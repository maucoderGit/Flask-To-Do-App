from flask import flash, redirect, render_template, session, url_for
from flask_login import current_user, login_required, login_user, logout_user

from werkzeug.security import generate_password_hash, check_password_hash

from app.models import UserData, UserModel
from . import auth
from app.forms import Login, SingupForm
from app.firestore_service import get_user_by_id, user_put

@auth.route('/login', methods=['GET','POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
        
    login_form = Login()
    context: dict = {
        'login_form': login_form
    }

    if login_form.validate_on_submit():
        username = login_form.username.data
        password = login_form.password.data

        user_doc = get_user_by_id(username)
        
        if user_doc.to_dict():
            password_from_db = user_doc.to_dict()['password']
            
            if check_password_hash(password_from_db, password):
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


@auth.route('singup', methods=['GET', 'POST'])
def singup():
    singup_form = SingupForm()
    context = {
        'singup_form' : singup_form
    }

    if singup_form.validate_on_submit():
        username: str = singup_form.username.data
        password: str = singup_form.password.data
        first_name: str = singup_form.first_name.data
        last_name: str = singup_form.last_name.data

        user_doc = get_user_by_id(username)

        if user_doc.to_dict():
            flash('This username is already in use')
        else:
            password_hash = generate_password_hash(password)
            user_data = UserData()
            
            user_data._username = username
            user_data._password = password_hash
            user_data.first_name = first_name
            user_data.last_name = last_name

            user_put(user_data)

            user = UserModel(user_data)
            login_user(user)

            flash('Welcome')

            return redirect(url_for('home'))


    return render_template('singup.html', **context)

@auth.route('logout')
@login_required
def logout():
    logout_user()
    flash('See you later, space cowboy')

    return redirect(url_for('auth.login'))