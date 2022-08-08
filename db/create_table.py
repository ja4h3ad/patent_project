import mysql.connector as mysql
from mysql.connector import Error
# this is the python script to create my initial table for patent data

import pandas as pd # read the csv file into a dataframe
df = pd.read_csv("../docs/nw_patents_seed.csv", index_col=False, delimiter=',')

try:
    conn = mysql.connect(host='localhost', user='root', port='33000',
                        password='root', database='patents')  # port = 33000 local
    if conn.is_connected():
        cursor = conn.cursor()
        cursor.execute("select database();")
        record = cursor.fetchone()
        print("You're connected to database: ", record)
        cursor.execute('DROP TABLE IF EXISTS patentData;')
        print('Creating table....')
# table creation command:
        # in the below line we pass the table creation statement
        cursor.execute(
            "CREATE TABLE patentData(id INT NOT NULL AUTO_INCREMENT, pID VARCHAR (50),title VARCHAR (500),"
            "inventor VARCHAR (500), abstract VARCHAR (2000), "
            "publicationDate date, resultLink VARCHAR (100),PRIMARY KEY (id))")
        # feedback loop :-)
        print("Table is created....")
        #loop through the data frame
        for i,row in df.iterrows():
            #here %S means string values
            sql = "INSERT INTO patents.patentData (pID,title,inventor,abstract,publicationDate, resultLink) " \
                  "VALUES (%s,%s,%s,%s,%s,%s)"
            cursor.execute(sql, tuple(row))
            print("Record inserted")
            # the connection is not auto committed by default, so we must commit to save our changes
            conn.commit()
except Error as e:
            print("Error while connecting to MySQL", e)