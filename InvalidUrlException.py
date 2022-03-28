class InvalidUrlException(Exception):

    def __init__(self, message="This url is invalid"):
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return f'InvalidUrl: {self.message}'