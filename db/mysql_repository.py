import mysql.connector
from mysql.connector import Error


class patentsSQL():

    def __init__(self):
        config = {'host':'db', 'user':'root', 'password':'root', 'port':'33000','database':'patents' }
        self.connection = mysql.connector.connect(**config)
        self.cursor = self.connection.cursor()


    def __del__(self):
        self.connection.close()

    def commit_changes(self):
        self.connection.commit()

    # def load_user_input(self):
    #     try:
    #         self.connection()
    #         if config.is_connected():
    #             self.cursor = conn.cursor()
    #             self.cursor.execute("select database();")
    #             record = cursor.fetchone()
    #             # print("You're connected to database: ", record)
    #             self.cursor.execute('DROP TABLE IF EXISTS webForm;')
    #             # print('Creating table....')
    #             # table creation command:
    #             # in the below line we pass the table creation statement
    #             self.cursor.execute(
    #                 "CREATE TABLE webForm (id INT NOT NULL AUTO_INCREMENT,"
    #                 "original_string VARCHAR (300),tokenized_data VARCHAR (500),"
    #                 "vectors VARCHAR,"
    #                 "CONSTRAINT pk_id PRIMARY KEY(id),"
    #                 "CONSTRAINT fk_wf_id FOREIGN KEY (wf_id)")
    #             # feedback loop :-)
    #             # print("Table is created....")
    #             # loop through the data frame
    #             self.connection.commit()
    #     except Error as e:
    #         print("Error while connecting to MySQL", e)
    #
    #
