import mysql.connector
import sqlite3

try:
    connection=mysql.connector.connect(
        host="localhost",
        port=3306,
        user="root",
        password="Leoren",
        db="Trebas_schedule",
        auth_plugin='mysql_native_password'
    )
    if connection.is_connected():
        print("Connection succesfull")
        info_server=connection.get_server_info()
        print(info_server)
        cursor=connection.cursor()
        cursor.execute("SELECT DATABASE()")
        row=cursor.fetchone()
except Exception as ex:
    print(ex)

cursor.execute("INSERT INTO ROOMS VALUES (500,'500')")
connection.commit();

