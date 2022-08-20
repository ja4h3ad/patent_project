import pandas as pd

import db.mysql_repository

# get updated information from sql, specifically the title and abstract of the scraped patents
connection = db.mysql_repository.MysqlRepository(patents)
if connection.cursor.

sql = pd.read_sql_query('')
fetch_abs_title = connection.cursor(sql)

try:
    conn = msql.connect(host='localhost', user='root', port='32000',
                        password='root')  # port = 33000 local
    if conn.is_connected():
        cursor = conn.cursor()
        cursor.execute("CREATE DATABASE patents;"
                       "ALTER DATABASE patents CHARACTER SET utf8 COLLATE utf8_unicode_ci; ")
        print("Database is created")
except Error as e:
    print("Error while connecting to MySQL", e)

