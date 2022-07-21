from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import recipe
from flask import flash
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
PASSWORD_REGEX = re.compile(r'\d.*[A-Z]|[A-Z].*\d')
class User:
    @classmethod
    def save(cls, data ):
        query = "INSERT INTO users ( first_name , last_name , email , password, created_at, updated_at) VALUES ( %(fname)s , %(lname)s , %(email)s , %(pword)s , NOW() , NOW());"
        return connectToMySQL('recipes').query_db( query, data )
    def __init__( self , data ):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.password = data['password']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.recipes = []
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM users LEFT JOIN recipes ON recipes.user_id = users.id;"
        results = connectToMySQL('recipes').query_db(query)
        users = []
        for user in results:
            users.append( cls(user) )
        return users
    @classmethod
    def get_user_with_recipes(cls, data):
        query ="SELECT * FROM users LEFT JOIN recipes ON recipes.user_id = users.id WHERE users.id = %(id)s;"
        results = connectToMySQL('recipes').query_db(query, data)
        user = cls(results[0])
        for row_from_db in results:
            recipe_data = {
                "id" : row_from_db["recipes.id"],
                "name" : row_from_db["name"],
                "description" : row_from_db["description"],
                "instructions" : row_from_db["instructions"],
                "date_made" : row_from_db['date_made'],
                "under" : row_from_db['under'],
                "posted_by" : row_from_db['posted_by'],
                "user_id" : row_from_db["user_id"],
                "created_at" : row_from_db["recipes.created_at"],
                "updated_at" : row_from_db["recipes.updated_at"]
            }
            user.recipes.append(recipe.Recipe(recipe_data))
        return user
    @classmethod
    def get_one(cls, data):
        query = "SELECT * FROM users WHERE id = %(id)s;"
        user = connectToMySQL('recipes').query_db(query, data)
        return user
    @classmethod
    def get_one_by_email(cls, data):
        query = "SELECT * FROM users WHERE email = %(email)s;"
        user = connectToMySQL('recipes').query_db(query, data)
        return user
    @staticmethod
    def validate_register(cls):
        is_valid = True
        if len(cls['fname']) < 1:
            flash("First Name must be at least 2 characters.", "reg")
            is_valid = False
        if len(cls['lname']) < 1:
            flash("Last Name must be at least 2 characters.", "reg")
            is_valid = False
        if len(cls['pword']) < 8:
            flash("Password must be more than 8 characters.", "reg")
            is_valid = False
        if not EMAIL_REGEX.match(cls['email']): 
            flash("Invalid email address!", "reg")
            is_valid = False
        if not PASSWORD_REGEX.match(cls['pword']): 
            flash("Password must contain at least one uppercase letter and one number.", "reg")
            is_valid = False
        if cls['pword'] != cls['pw_confirm']:
            flash("Passwords must match.", "reg")
            is_valid = False
        return is_valid