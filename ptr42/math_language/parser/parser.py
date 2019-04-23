from typing import Callable, Set, List, Optional

from ptr42.math_language.lexer.expression_error import ExpressionError
from ptr42.math_language.lexer.token import Token, TokenTypes
from ptr42.math_language.parser.binary_operator_node import BinaryOperatorNode
from ptr42.math_language.parser.expression import Operator
from ptr42.math_language.parser.function_node import FunctionNode
from ptr42.math_language.parser.node import Node
from ptr42.math_language.parser.number_node import NumberNode
from ptr42.math_language.parser.parser_error import ParserError
from ptr42.math_language.parser.unary_operator_node import UnaryOperatorNode


# Postup evaluacie
# OPERATOR: TERM (op) TERM)
# FACTOR: NUMBER
#         (+-)NUMBER
#         LPAREN(EXPR)RPAREN
#         func(ARGS)


class MathParser(object):
    """
        Matematicky parser, ktory pomocou tokenov zostroji abstraktny syntaxovi strom (AST). Pomocou AST sa dokaze
        vypocitat celkovy matematicky vyraz.
    """

    def __init__(self, tokens: List[Token], operators: Set[Operator]):
        """
        Inicializuje parser na zakladne hodnoty a skontroluje ci tokeny nie su prazdne

        :param tokens: tokeny na parsnutie
        :param operators: operatory, podla ktorych sa zostavi AST. Priority su urcene precedenciou (atribut triedy
        Operator)
        """

        if not tokens:
            raise ValueError("Tokens cannot by empty")

        self._tokens = tokens
        self._token_index = -1
        self._curr_token = None
        self._operator_precedences = sorted(list(map(lambda op: op.precedence, operators)))
        self._next()

    def _get_sub_parser(self, tokens: List[Token]):
        sub_parser = MathParser(tokens, set())
        sub_parser._operator_precedences = self._operator_precedences
        return sub_parser

    def _next(self) -> Optional[Token]:
        self._token_index += 1
        if self._token_index < len(self._tokens):
            self._curr_token = self._tokens[self._token_index]
        else:
            return None

        return self._curr_token

    def _factor(self) -> Optional[Node]:
        token = self._curr_token

        if token.type == TokenTypes.FUNCTION_TOKEN:
            self._next()
            ast = list()
            for arg in token.arguments():
                ast.append(self._get_sub_parser(arg).parse())
            return FunctionNode(token, ast)

        elif token.type == TokenTypes.OPERATOR_TOKEN:
            if token.value.unary_func is None:
                raise ExpressionError(_("Unary operator %s does not exist") % token.value)

            self._next()

            if self._curr_token.type == TokenTypes.OPERATOR_TOKEN:
                raise ExpressionError(_("Duplicate operator %s") % token.value)

            factor = self._factor()

            if factor is not None:
                return UnaryOperatorNode(token, factor)
            else:
                raise ExpressionError(_("Invalid factor"))

        elif token.type in (TokenTypes.INT_TOKEN, TokenTypes.FLOAT_TOKEN, TokenTypes.VARIABLE_TOKEN):
            self._next()
            return NumberNode(token)

        elif token.type == TokenTypes.LPAREN_TOKEN:
            self._next()
            expr = self._expr()

            if self._curr_token.type == TokenTypes.RPAREN_TOKEN:
                self._next()
                return expr
            else:
                raise ExpressionError(_("Mismatched parenthesis"))

        elif token is not None:
            raise ParserError(f"Cannot consume token - {self._curr_token}")

        return None

    def _binary_operator(self, func: Callable[[], Node], precedence: int) -> Node:
        left = func()

        while self._curr_token.type == TokenTypes.OPERATOR_TOKEN and self._curr_token.precedence == precedence:
            op = self._curr_token
            self._next()
            right = func()
            left = BinaryOperatorNode(left, op, right)

        return left

    def _term(self, index: int) -> Node:
        if index == -1:
            return self._factor()

        return self._binary_operator(lambda: self._term(index - 1), self._operator_precedences[index])

    def _expr(self) -> Node:
        return self._term(len(self._operator_precedences) - 1)

    def parse(self) -> Node:
        """
        Vrati korenovy vrchol z AST, podla ktoreho sa da dalej vypocitat vyraz

        :return: korenovy vrchol
        """
        return self._expr()
