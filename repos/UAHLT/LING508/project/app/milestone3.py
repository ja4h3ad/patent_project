class Patent:
    def __init__(self, patent: str, inventor: str, status: str, anticipatedExpiration: str):
        """

        :type inventor: string
        """
        self.status = status
        self.patent = patent
        self.inventor = inventor
        self.anticipatedExpiration = anticipatedExpiration

    def convert_date(self):
        '''This will be used for calculation of expiry at a later date'''
        self.date = self.anticipatedExpiration
        print("This patent expires on {}".format(self.anticipatedExpiration))

    def __str__(self):
        return f"{self.patent} filed by {self.inventor}, status is {self.status} with expiration of {self.anticipatedExpiration}"

