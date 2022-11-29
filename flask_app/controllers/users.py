from flask_app import app, bcrypt
# from flask_app.models.user import User
from flask import render_template, request, redirect, session
# app.routes 

@app.route('/')
def r_home_page():
    return render_template('login.html')