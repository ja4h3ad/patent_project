class Patent:
    def __init__(self, patentID: str, title: str, inventor: str, publicationDate: datetime):
        """

        :type inventor: string
        """
        self.patentID = patentID
        self.title = title
        self.inventor = inventor
        self.publicationDate = publicationDate

    # feedback loop :-)
    def convert_date(self):
        '''This will be used for calculation of expiry at a later date'''
        # placeholder for conversion
        # print("This patent expires on {}".format(self.expiration))

    def __str__(self):
        return f"{self.patentID} filed by {self.inventor}"
