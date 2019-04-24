from ptr42.math_language.lexer.token import Token
from ptr42.math_language.parser.node import Node


class UnaryOperatorNode(Node):
    """
    Vrchol reprezentujuci unarny operator
    """

    def __init__(self, token: Token, value: Node):
        """
        Inicializuje vrhcol unarneho operator

        :param token: token operatora
        :param value: vrchol argumentu
        """
        super(UnaryOperatorNode, self).__init__(token)
        self.value = value

    def __repr__(self):
        return f"({self.token.value}:{self.value})"

    def evaluate(self):
        """
        Aplikuje unarny operator na vrhcol a vrati vysledok

        :return: vysledok ako float
        """
        return self.token.value.unary_func(self.value.evaluate())
