import datetime, Tempo
from DBManipulador import *
import constants


# Deleta o usuário
def delete_user(username):
    mydb = DBManipulador.get_mydb()
    cursor = mydb.cursor()
    sql = "DELETE FROM followed_users WHERE username = '{0}'".format( username )
    cursor.execute( sql )
    mydb.commit()


# adiciona novo Usuário
def add_user(username):
    mydb = DBManipulador.get_mydb()
    cursor = mydb.cursor()
    now = datetime.datetime.now().date()
    cursor.execute("INSERT INTO following_users(user_name, data_added) VALUES(%s,%s)", (username, now) )
    mydb.commit()


# Checa as Iformações do Usuário
def check_unfollow_list():
    mydb = DBManipulador.get_mydb()
    cursor = mydb.cursor()
    cursor.execute( "SELECT * FROM following_users" )
    results = cursor.fetchall()
    users_to_unfollow = []
    for r in results:
        d = Tempo.days_since_date( r[1] )
        if d > constants.DAYS_TO_UNFOLLOW:
            users_to_unfollow.append( r[0] )
    return users_to_unfollow


def get_followed_users():
    users = []
    mydb = DBManipulador.get_mydb()
    cursor = mydb.cursor()
    cursor.execute( "SELECT * FROM following_users" )
    results = cursor.fetchall()
    for r in results:
        users.append( r[0] )

    return users
