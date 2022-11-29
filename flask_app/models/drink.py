from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models.user import User
from flask import flash

db = 'cocktail_haven'
class Drink:
    def __init__(self, data):
        self.id = data['id']
        self.spirit = data['spirit']
        self.ingredient = data['ingredient']
        self.picture = data['picture']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.user = None

    @staticmethod
    def validate_drink(form_data:dict):
        is_valid = True

        if form_data.get('spirit') == None:
            flash("Please choose a main spirit of this cocktail", 'drink')
            is_valid = False

        if len(form_data.get('ingredient')) <= 0:
            flash("Please list all the ingredient's needed for this cocktail", 'drink')
            is_valid = False

        if form_data.get('picture') == None:
            flash("Please upload a picture of this drink!", 'drink')
            # not sure if this is correct way to do this with this data type in mysql
            is_valid = False

    @classmethod
    def save(cls, data):
        query = """
        INSERT INTO drinks (spirit, ingredient, picture, created_at, updated_at, user_id)
        VALUES (%(spirit)s, %(ingredient)s, %(picture)s, NOW(), NOW(), %(user_id)s)
        """
        return connectToMySQL(db).query_db(query, data)

    @classmethod
    def get_one_drink(cls, data):
        query = """
        SELECT * 
        FROM drinks 
        JOIN users
        ON drinks.user_id = users.id
        WHERE drinks.id = %(id)s;
        """
        result = connectToMySQL(db).query_db(query, data)
        single_drink = cls(result[0])
        return single_drink

    @classmethod
    def get_all_drinks(cls):
        query = """
        SELECT *
        FROM drinks
        JOIN users
        ON users.id 
        WHERE drinks.user_id = users.id;
        """
        results = connectToMySQL(db).query_db(query)
        drinks = []
        for drink in results:
            one_drink = cls(drink)
            data = {
                'id': drink['users.id'],
                'first_name': drink['first_name'],
                'last_name': drink['last_name'],
                'email': drink['email'],
                'created_at': drink['users.created_at'],
                'updated_at': drink['users.updated_at']
            }
            one_drink.user = User(data)
            drinks.append(one_drink)
        return drinks

    @classmethod
    def update_drinks(cls, data):
        query = """
        UPDATE drinks
        SET spirit = %(spirit)s, ingredient = %(ingredient)s, picture = %(picture)s, updated_at = NOW()
        WHERE id = %(id)s;
        """
        return connectToMySQL(db).query_db(query, data)

    @classmethod
    def delete_drinks(cls, data):
        query = """
        DELETE FROM drinks
        WHERE id = %(id)s;
        """
        return connectToMySQL(db).query_db(query, data)