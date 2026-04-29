import mysql.connector

def get_connection():
    conexao = mysql.connector.connect(
        host="localhost",
        user="root",
        password="123456",
        database="petvida"
    )
    return conexao