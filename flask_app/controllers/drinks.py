from flask_app import app
from flask_app.models.drink import Drink
from flask import render_template, redirect, request, session, url_for

# CREATE, f=form function, r=render template function
@app.route('/create', methods=['POST'])
def f_create_drink():
    if not Drink.validate_drink(request.form):
        return redirect('/create/drink')
    Drink.save(request.form)
    return redirect('/dashboard')

@app.route('/create/drink')
def r_new_drink():
    if 'user_id' not in session:
        return redirect('/log_out')
    return render_template('create.html')

#SHOW a specific drink
@app.route('/show/<int:id>')
def r_show_one_drink(id):
    if 'user_id' not in session:
        return (redirect('/log_out'))
    return render_template('show.html', user = session['user_id'], drink = Drink.get_one_drink({'id': id}))

#DELETE 
@app.route('/delete/<int:id>')
def rd_delete_one_drink(id):
    if 'user_id' not in session:
        return redirect('/log_out')
    Drink.delete_drinks({'id': id})
    return redirect('/dashboard')

#EDIT 
@app.route('/edit/<int:id>')
def r_edit_drink(id):
    if 'user_id' not in session:
        return redirect('/log_out')
    return render_template('edit.html', user = session['user_id'], drink = Drink.get_one_drink({'id':id}))

@app.route('/edit/drink', methods=['POST'])
def f_process_drink_update():
    if 'user_id' not in session:
        return redirect('/log_out')
    if not Drink.validate_drink(request.form):
        return redirect(url_for('r_edit_drink', id = request.form['id']))
    Drink.update_drink(request.form)
    return redirect('/dashboard')