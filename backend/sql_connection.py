__cnx = None
import mysql.connector

def get_sql_connection():
    global __cnx
    if __cnx==None:
        __cnx = mysql.connector.connect(user='root',password='sathish',host='127.0.0.1',database='grocery_store')
    
    return __cnx
