from ..config.mysqlconnection import connectToMySQL
from flask import flash

class Dojo:

    def __init__( self , data ):
        self.id = data['id']
        self.name = data['name']
        self.location = data['location']
        self.language = data['language']
        self.comment = data['comment']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def save(cls, data ):
        query = "INSERT INTO dojos (name , location, language, comment) VALUES (%(name)s, %(location)s, %(language)s, %(comment)s);"
        return connectToMySQL('dojo_survey_schema').query_db( query, data )

#! cool query that the instructor used to pull the information from the last person to fill out the form
    # @classmethod
    # def get_last(cls):
    #     query = "SELECT * FROM dojos ORDER BY dojos.id DESC LIMIT 1;"
    #     results = connectToMySQL('dojo_survey_schema').query_db(query)
    #     return Dojo(results[0])

    @classmethod
    def get_by_id(cls, data):
        query = "SELECT * FROM dojos WHERE id = %(id)s"
        results = connectToMySQL('dojo_survey_schema').query_db(query, data)
        print(results)
        return Dojo(results[0])

    @staticmethod
    def is_valid(dojo):
        is_valid = True
        if len(dojo['name']) < 2:
            is_valid = False
            flash("Name must be at least 2 characters.")
        if len(dojo['location']) < 1:
            is_valid = False
            flash("A location must be selected.")
        if len(dojo['language']) < 1:
            is_valid = False
            flash("A language must be selected.")
        if len(dojo['comment']) < 3:
            is_valid = False
            flash("Comments must be at least 3 characters.")
        return is_valid