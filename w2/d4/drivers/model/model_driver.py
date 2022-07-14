# import the function that will return an instance of a connection
from unittest import result
from mysqlconnection import connectToMySQL
# model the class after the friend table from our database
class Driver:
    def __init__( self , data ):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.level = data['level']
        self.phone_num = data['phone_num']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.fullname = f"{self.first_name.capitalize} {self.last_name.capitalize}"
        #-C
    @classmethod
    def create(cls, data):
        query = "INSERT INTO drivers(first_name, last_name, email, phone_num) VALUES(%(first_name)s,%(last_name)s, %(email)s, %(phone_num)s);"
        driver_id = connectToMySQL('driver_db').query_db(query,data)
        return driver_id
        #-R
        # Now we use class methods to query our database
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM drivers;"
        # make sure to call the connectToMySQL function with the schema you are targeting.
        results = connectToMySQL('driver_db').query_db(query)
        # Create an empty list to append our instances of friends
        all_drivers = []
        # Iterate over the db results and create instances of friends with cls.
        for driver in results:
            all_drivers.append( cls(driver) )
        return all_drivers
        #-U

        #-D

#-create
#-get_all
#-get_one
#-updat_one
#-update_many
#-delete_one
#-delete_many