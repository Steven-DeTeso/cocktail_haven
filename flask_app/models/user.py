from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import bcrypt
from flask import flash
import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

db = 'cocktail_haven'
class User:
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.drinks = []

    @staticmethod
    def validate_user_register(form_data:dict) -> bool:
        is_valid = True
        is_valid_email = True

        if len(form_data.get('first_name')) <= 2: 
            flash("Please be sure to fill in your first name!", 'register')
            is_valid = False

        if len(form_data.get('last_name')) <= 2:
            flash("Please be sure to fill in your last name!", 'register')

        if len(form_data.get('email')) <= 0:
            flash("A valid email address is requred!", 'register')
            is_valid = False
            is_valid_email = False
        if not EMAIL_REGEX.match(form_data.get('email')):
            flash("The email you entered is not in the correct format!", 'register')
            is_valid = False
            is_valid_email = False

        if is_valid_email:
            query = """
            SELECT *
            FROM users 
            WHERE email = %(email)s;
            """
            result = connectToMySQL(db).query_db(query, form_data)
            if len(result) >= 1:
                flash("The email you are using is already registered in our system", 'register')
                is_valid = False

        if len(form_data.get('password')) < 8:
            flash("The password you entered isn't long enough, plase make it at least 8 characters!", 'register')
            is_valid = False

        if form_data.get('password') != form_data.get('confirm_password'):
            flash("The confirmed password didn't match the password you entered", 'register')
            is_valid = False

        if form_data.get('radio') != 'verified':
            flash("Please click the button to verify you are indeed a human!", 'register')
            is_valid = False


        return is_valid

    @staticmethod
    def validate_user_login(form_data:dict) -> bool:
        is_valid = True
        is_valid_email = True

    if len(form_data.get('email')) <= 0:
        flash()

    return is_valid