from flask_app import app, bcrypt
from flask_app.models.user import User
from flask_app.models.drink import Drink
from flask import render_template, request, redirect, session
# app.routes 

@app.route('/')
def r_home_page():
    return render_template('login.html')

@app.route('/register')
def r_register_page():
    return render_template('register.html')

@app.route('/register/user', methods=['POST'])
def f_register_user():
    if User.validate_user_register(request.form):
        data = {
        'first_name': request.form.get('first_name'),
        'last_name': request.form.get('last_name'),
        'email': request.form.get('email'),
        'password': bcrypt.generate_password_hash(request.form.get('password'))
        }
        User.save(data)
        user_in_db = User.get_one_for_login(data)
        session['user_id'] = user_in_db[0] #steps in to just grab dict:object from list,hench [0]
        return redirect('/dashboard')
    return redirect('/register')

@app.route('/login/user', methods = ['POST'])
def f_login_user():
    if not User.validate_user_login(request.form):
        return redirect('/')
    data = {
        'email': request.form.get('email')
    }
    user_in_db = User.get_one_for_login(data)
    session['user_id'] = user_in_db[0]
    return redirect('/dashboard')

@app.route('/dashboard')
def r_dashboard():
    if 'user_id' not in session:
        return redirect('/log_out')
    return render_template('dashboard.html', user = session['user_id'], drinks = Drink.get_all_drinks())

@app.route('/account')
def r_account():
    if 'user_id' not in session:
        return redirect('/log_out')
    data = {
        'id': session['user_id']['id']
    }
    return render_template('account.html', user = session['user_id'], drinks = Drink.get_all_users_drinks(data))

@app.route('/account/update')
def r_account_update():
    if 'user_id' not in session:
        return redirect('/log_out')
    return render_template('user_updated.html', user = session['user_id'])

@app.route('/account/update/user', methods=['POST'])
def f_rd_user_account_update():
    if User.validate_user_update(request.form):
        data = {
        'id': request.form.get('id'),
        'first_name': request.form.get('first_name'),
        'last_name': request.form.get('last_name'),
        'password': bcrypt.generate_password_hash(request.form.get('password')),
        'updated_at': None
        }
        User.update_user(data)
        return redirect('/dashboard')
    return render_template('/user_updated.html')

@app.route('/user/<int:id>')
def r_user_account(id):
    data = {
        'id': id
    }
    return render_template('all_user_drinks.html', drinks = Drink.get_all_users_drinks(data))

@app.route('/log_out')
def rd_log_out():
    session.clear()
    return redirect('/')