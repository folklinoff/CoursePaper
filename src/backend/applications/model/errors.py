class UnprocessableEntityError(BaseException):
    def __init__(self, message) -> None:
        self.message = message