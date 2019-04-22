from ptr42.math_language.lexer.token import Token
from ptr42.math_language.parser.node import Node


class NumberNode(Node):
    """
    Trieda reprezentujuca ciselny, konstantny vrchol
    """

    def __init__(self, token: Token):
        """

        :param token: token vrcholu
        """
        super(NumberNode, self).__init__(token)

    def __repr__(self):
        return f"{self.token.type.name}:{self.token.value}"

    def evaluate(self) -> float:
        """
        Vrati ciselnu hodnotu vrcholu

        :return: ciselna hodnota vrcholu ako float
        """
        return self.token.value
