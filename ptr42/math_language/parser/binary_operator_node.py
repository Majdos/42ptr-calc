from ptr42.math_language.lexer.token import Token
from ptr42.math_language.parser.node import Node


class BinaryOperatorNode(Node):
    """
    Trieda reprezentujuca binarnu operaciu v abstraktnom syntaxovom strome (AST)
    """

    def __init__(self, left: Node, operator: Token, right: Node):
        """
        Inicializuje binarny vrchol v AST

        :param left: lavy operand
        :param operator: operator, ktory sa vykona nad lavym a pravym operandom
        :param right: pravy operand
        """

        super(BinaryOperatorNode, self).__init__(operator)
        self.left_node = left
        self.right_node = right

    def __repr__(self):
        return f"({self.left_node}, {self.token}, {self.right_node})"

    def evaluate(self) -> float:
        """
        Vypocita hodnotu aktualneho uzla a uzlov pod tymto uzlom

        :return: vysledok ako float
        """

        return self.token.value.evaluate(self.left_node.evaluate(), self.right_node.evaluate())
