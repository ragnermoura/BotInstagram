import mysql.connector
import constants


class DBManipulador:
    def __init__(self):
        DBManipulador.HOST = constants.HOST
        DBManipulador.USER = constants.USER
        DBManipulador.DBNAME = constants.DATABASE
        DBManipulador.PASSWORD = constants.PASS
    HOST = constants.HOST
    USER = constants.USER
    DBNAME = constants.DATABASE
    PASSWORD = constants.PASS
    @staticmethod
    def get_mydb():
        if DBManipulador.DBNAME == '':
            constants.init()
        db = DBManipulador()
        mydb = db.connect()
        return mydb

    def connect(self):
        mydb = mysql.connector.connect(
            host=DBManipulador.HOST,
            user=DBManipulador.USER,
            passwd=DBManipulador.PASSWORD,
            database=DBManipulador.DBNAME
        )
        return mydb