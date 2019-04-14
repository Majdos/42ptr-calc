from ptr42.math_language.lexer.token import Token


class Node(object):
    """
    Abstraktna struktura reprezentujuca vrhcol v AST
    """

    def __init__(self, token: Token):
        """

        :param token: token vrcholu
        """
        self.token = token

    def evaluate(self) -> float:
        """
        Vypocita hodnotu vrcholu

        :return: hodnota vrcholu ako float
        """
        raise NotImplementedError()
