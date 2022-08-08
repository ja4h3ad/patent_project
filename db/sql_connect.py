import mysql.connector as msql
from mysql.connector import Error


try:
    conn = msql.connect(host='localhost', user='root', port='33000',
                        password='root')  # port = 33000 local
    if conn.is_connected():
        cursor = conn.cursor()
        cursor.execute("CREATE DATABASE patents;"
                       "ALTER DATABASE patents CHARACTER SET utf8 COLLATE utf8_unicode_ci; ")
        print("Database is created")
except Error as e:
    print("Error while connecting to MySQL", e)


