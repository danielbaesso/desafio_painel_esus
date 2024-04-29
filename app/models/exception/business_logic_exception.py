class BusinessLogicException(Exception):
    def __init__(self, message="Business Logic Exception."):
        self.message = message
        super().__init__(self.message)