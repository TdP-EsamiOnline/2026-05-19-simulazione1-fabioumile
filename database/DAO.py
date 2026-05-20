from database.DB_connect import DBConnect
from model.Genere import Genere

class DAO():
    def __init__(self):
        pass

    @staticmethod
    def getAllGeneri():
        cnx = DBConnect.get_connection()
        cursor = cnx.cursor(dictionary=True)
        query = """select *  from genre g"""
        cursor.execute(query)
        res = []
        for row in cursor:
            res.append(Genere(**row))

        cursor.close()
        cnx.close()
        return res
