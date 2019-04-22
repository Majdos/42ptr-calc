from typing import List

from ptr42.math_language.lexer.function_token import FunctionToken
from ptr42.math_language.parser.expression import Function
from ptr42.math_language.parser.node import Node


class FunctionNode(Node):
    """
    Vrchol reprezentujuci funkcie v abstraktom syntaxovom strome (AST)
    """

    def __init__(self, token: FunctionToken, args_abstract_syntax_tree: List[Node]):
        """
        Inicializuje vrchol funkcie s parsnutymi argumentami

        :param token: token funkcie
        :param args_abstract_syntax_tree: parsnute argumenty z MathParser
        """
        super(FunctionNode, self).__init__(token)
        self.args_abstract_syntax_tree = args_abstract_syntax_tree

    def evaluate(self) -> float:
        """
        Vypocita hodnotu tohoto uzla a hodnoty argumentov

        :return: vysledok ako float
        """
        args = map(lambda node: node.evaluate(), self.args_abstract_syntax_tree)
        func: Function = self.token.value
        func.set_args(*args)
        return func.evaluate()

    def __repr__(self):
        return f"{self.token.type.name}({self.args_abstract_syntax_tree})"
