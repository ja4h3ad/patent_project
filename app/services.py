import db.mysql_repository
import datetime
import app.nlp_utility

class Patent:
    def __init__(self):
        """
        This is the Class that will be used for Service layer abstraction

        """

        self.repo = db.mysql_repository.MysqlRepository
        self.pID = pID
        self.title = title
        self.inventor = inventor
        self.abstract = abstract
        self.publicationDate = publicationDate
        self.resultLink = resultLink


    #  to be used in a later implementation
    # def convert_date(self):
    #     '''This will be used for calculation of expiry at a later date'''
    #     # placeholder for conversion
    #     # print("This patent expires on {}".format(self.expiration))

    def __str__(self):
        return f"{self.patentID} filed by {self.inventor}"




class Services:
    def __init__(self):
        self.repo = db.mysql_repository.MysqlRepository()


    def get_patent_inventory:
        sql = ("SELECT * FROM patents.patentData")
        self.repo.
        cursor.execute(sql)
        # Fetch all the records
        result = cursor.fetchall()

    # use case:  Accept input from UI and store in db
    def accept_ui_input(self):

        self.repo.load_user_input()
        # with user_input accepted, send it the helper to tokenize

    # use case 2 clean data, tokenize and vectorize
    def process_ui_input (self):
        pass

    # use case return documents with nearest similarities:
    def docsim_results(self):
        pass


