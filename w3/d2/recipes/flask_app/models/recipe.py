from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
class Recipe:
    @classmethod
    def save(cls, data ):
        query = "INSERT INTO recipes ( name , description , instructions, date_made, under, posted_by, user_id , created_at, updated_at) VALUES ( %(name)s , %(description)s , %(instructions)s , %(date_made)s ,%(under)s, %(posted_by)s , %(user_id)s, NOW() , NOW());"
        return connectToMySQL('recipes').query_db( query, data )
    def __init__( self , data ):
        self.id = data['id']
        self.name = data['name']
        self.description = data['description']
        self.instructions = data['instructions']
        self.date_made = data['date_made']
        self.under = data['under']
        self.posted_by = data['posted_by']
        self.user_id = data['user_id']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
    # Now we use class methods to query our database
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM recipes;"
        # make sure to call the connectToMySQL function with the schema you are targeting.
        results = connectToMySQL('recipes').query_db(query)
        # Create an empty list to append our instances of friends
        recipes = []
        # Iterate over the db results and create instances of friends with cls.
        for recipe in results:
            recipes.append( cls(recipe) )
        return recipes
    @classmethod
    def get_one(cls, data):
        query = "SELECT * FROM recipes WHERE id = %(reid)s"
        recipe = connectToMySQL('recipes').query_db(query, data)
        return recipe
    @classmethod
    def update(cls, data):
        query = "UPDATE recipes SET name = %(name)s, description = %(description)s, instructions = %(instructions)s, date_made = %(date_made)s, under = %(under)s WHERE id = %(reid)s;"
        return connectToMySQL('recipes').query_db( query, data )
    @classmethod
    def delete(cls, data):
        query = "DELETE FROM recipes WHERE id = %(reid)s"
        return connectToMySQL('recipes').query_db( query, data )
    @staticmethod
    def validate_entry(cls):
        is_valid = True
        if len(cls['name']) < 3:
            flash("Name must be at least 3 characters", "cre")
            is_valid = False
        if len(cls['desc']) < 3:
            flash("Description must be at least 3 characters", "cre")
            is_valid = False
        if len(cls['instr']) < 3:
            flash("Instructions must be at least 3 characters", "cre")
            is_valid = False
        return is_valid