class ParserError(Exception):
    def __init__(self, message: str):
        super(ParserError, self).__init__(message)
