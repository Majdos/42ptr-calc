class ExpressionError(Exception):
    def __init__(self, message: str):
        super(ExpressionError, self).__init__(message)
