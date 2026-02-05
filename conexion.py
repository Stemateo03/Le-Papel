import mysql.connector

def conectar():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="123",   # TU CLAVE REAL
        database="papeleria",
        auth_plugin="mysql_native_password"
    )
