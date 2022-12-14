from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models.user import User
from flask import flash

db = 'cocktail_haven'
class Drink:
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.spirit = data['spirit']
        self.brief_description = data['brief_description']
        self.ingredient = data['ingredient']
        self.instruction = data['instruction']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.user = None
        self.user_id = None

    @staticmethod
    def validate_drink(form_data:dict):
        is_valid = True

        if len(str(form_data.get('name'))) <= 1:
            flash("Please name your new cocktail", 'drink')
            is_valid = False

        if form_data.get('spirit') == None:
            flash("Please choose a main spirit of this cocktail", 'drink')
            is_valid = False

        if len(str(form_data.get('brief_description'))) <= 1: 
            flash("Please write out a one or two sentence brief description of this cocktail", 'drink')
            is_valid = False

        if len(str(form_data.get('ingredient'))) <= 1:
            flash("Please list all the ingredient's needed for this cocktail", 'drink')
            is_valid = False

        if len(str(form_data.get('instruction'))) <= 1:
            flash("Please write out the instructions for mixing this cocktail", 'drink')
            is_valid = False

        return is_valid

    @classmethod
    def save(cls, data):
        query = """
        INSERT INTO drinks (name, spirit, brief_description, ingredient, instruction, created_at, updated_at, user_id)
        VALUES (%(name)s, %(spirit)s, %(brief_description)s, %(ingredient)s, %(instruction)s, NOW(), NOW(), %(user_id)s)
        """
        print(query)
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
        single_drink.user = result[0]['first_name'] + ' ' + result[0]['last_name']
        single_drink.user_id = result[0]['users.id']
        return single_drink

    @classmethod
    def get_all_drinks(cls):
        query = """
        SELECT *
        FROM drinks
        JOIN users
        ON users.id 
        WHERE drinks.user_id = users.id
        ORDER BY drinks.created_at ASC;
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
    def get_all_users_drinks(cls, data):
        query = """
        SELECT * 
        FROM drinks 
        JOIN users 
        ON users.id = drinks.user_id
        WHERE users.id = %(id)s;
        """
        results = connectToMySQL(db).query_db(query, data)
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
    def update_drink(cls, data):
        query = """
        UPDATE drinks
        SET name = %(name)s, spirit = %(spirit)s, brief_description = %(brief_description)s, ingredient = %(ingredient)s, instruction = %(instruction)s, updated_at = NOW()
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

