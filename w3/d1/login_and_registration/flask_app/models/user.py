from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
PASSWORD_REGEX = re.compile(r'\d.*[A-Z]|[A-Z].*\d')
class User:
    @classmethod
    def save(cls, data ):
        query = "INSERT INTO users ( first_name , last_name , email , password, created_at, updated_at) VALUES ( %(fname)s , %(lname)s , %(email)s , %(pword)s , NOW() , NOW());"
        return connectToMySQL('login_and_registration').query_db( query, data )
    def __init__( self , data ):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.password = data['password']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM users;"
        results = connectToMySQL('login_and_registration').query_db(query)
        users = []
        for user in results:
            users.append( cls(user) )
        return users
    @classmethod
    def get_one(cls, data):
        query = "SELECT * FROM users WHERE id = %(id)s;"
        user = connectToMySQL('login_and_registration').query_db(query, data)
        return user
    @classmethod
    def get_one_by_email(cls, data):
        query = "SELECT * FROM users WHERE email = %(email)s;"
        user = connectToMySQL('login_and_registration').query_db(query, data)
        return user
    @staticmethod
    def validate_register(cls):
        is_valid = True
        if len(cls['fname']) < 2:
            flash("First Name must be more than 2 characters.", "reg")
            is_valid = False
        if len(cls['lname']) < 2:
            flash("Last Name must be more than 2 characters.", "reg")
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
        if cls['pword'] != cls['pword_confirm']:
            flash("Passwords must match.", "reg")
            is_valid = False
        return is_valid
    @staticmethod
    def validate_login(cls):
        is_valid =True
        if len(cls['email']) < 3:
            flash("Email must be more than 3 characters.", "log")
            is_valid = False
        if len(cls['pword']) < 8:
            flash("Password must be more than 8 characters.", "log")
            is_valid = False
        return is_valid