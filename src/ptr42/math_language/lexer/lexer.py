from copy import deepcopy
from string import ascii_letters
from typing import Dict, Optional, List, ValuesView, Iterable

from ptr42.math_language.lexer.expression_error import ExpressionError
from ptr42.math_language.lexer.function_token import FunctionToken
from ptr42.math_language.lexer.token import TokenTypes, Token
from ptr42.math_language.parser.expression import Operator, Function

DIGITS = "0123456789"


class MathLexer(object):
    """
        Lexer urceny specialne pre matematicky vyrazy. Podporuje funkcie, premenne a operatory. Operatory momentalne
        mozu by len 1 znakove
    """

    def __init__(self, expression: str):
        self._text = expression
        self._pos: int = -1
        self._current_char: Optional[str] = None
        self._operators: Dict[str, Operator] = dict()
        self._functions: Dict[str, Function] = dict()
        self._variables: Dict[str, float] = dict()
        self._current_identifier: Optional[str] = None
        self._in_function: bool = False
        self._paren_stack: List[str] = list()
        self._next()

    def add_operator(self, name: str, operator: Operator) -> None:
        """
        Prida operator pod menom 'name' medzi podporovane operatory.

        :param name: meno operator (max 1 znak)
        :param operator: trieda reprezentujuca operator
        """

        if not name or len(name) != 1:
            raise NotImplemented(f"Operatori o velikosti {len(name)} nie su podporovane!")
        self._operators[name] = operator

    def add_function(self, name: str, function: Function) -> None:
        """
        Prida operator pod menom 'name' medzi podporovane operatory.

        :param name: meno funkcie (iba ascii znaky, case sensitive)
        :param function: trieda funkciu
        """

        self._functions[name] = function

    def add_variable(self, name: str, value: float) -> None:
        """
        Prida premennu pod menom 'name' medzi zoznam premien.

        :param name: meno premennej (iba ascii znaky, case sensitive)
        :param value: hodnota premennej
        """

        self._variables[name] = value

    def get_operators(self) -> ValuesView[Operator]:
        """

        :return: Vrati vsetky podporvane operatory ako tridy reprezentujuce operator
        """
        return self._operators.values()

    def _next(self) -> str:
        self._pos += 1
        self._current_char = self._text[self._pos] if self._pos < len(self._text) else None
        return self._current_char

    def _tokenize_sub_text(self, start: int, end: int, in_function: bool = False) -> List[Token]:
        sub_lexer = MathLexer(self._text[start:end])
        sub_lexer._operators = self._operators
        sub_lexer._functions = self._functions
        sub_lexer._variables = self._variables
        sub_lexer._in_function = in_function
        return list(sub_lexer.generate_tokens())

    def generate_tokens(self) -> Iterable[Token]:
        """
        Vrati generator, ktory bude generovat tokeny

        :return: generator tokenov
        """

        while self._current_char is not None:
            if self._current_identifier is not None:
                if self._current_char == "(":
                    yield self._make_function()
                elif self._current_char not in DIGITS:
                    yield self._make_variable()
                else:
                    raise ExpressionError(_("Nespravny identifikator na pozicii %d") % self._pos)

            elif self._current_char == ",":
                if self._in_function:
                    self._current_identifier = None
                    self._next()
                    yield Token(TokenTypes.COMMA_TOKEN, None)
                else:
                    raise ExpressionError(_("Nespravne umiestnena ciarka"))

            elif self._current_char in " \t":
                self._current_identifier = None
                self._next()

            elif self._current_char in ascii_letters:
                self._current_identifier = self._make_identifier()

            elif self._current_char in DIGITS:
                yield self._make_number()

            elif self._current_char in self._operators.keys():
                yield Token(TokenTypes.OPERATOR_TOKEN, self._operators[self._current_char],
                            self._operators[self._current_char].precedence)
                self._next()

            elif self._current_char == "(":
                self._paren_stack.append(self._current_char)
                yield Token(TokenTypes.LPAREN_TOKEN, None)
                self._next()

            elif self._current_char == ")":
                if not self._paren_stack:
                    raise ExpressionError(_("Nezhodne zatvorky"))

                self._paren_stack.pop()
                yield Token(TokenTypes.RPAREN_TOKEN, None)
                self._next()

            else:
                raise ExpressionError(_("Neznamy znak '%c'") % self._current_char)

        if self._current_identifier is not None:
            yield self._make_variable()

        if self._paren_stack:
            raise ExpressionError(_("Nezhodne zatvorky"))

    def _make_number(self) -> Token:
        number_string = ""
        has_dot = False

        while self._current_char is not None and self._current_char in (DIGITS + "."):
            if self._current_char in DIGITS:
                number_string += self._current_char
            elif not has_dot:
                number_string += "."
                has_dot = True
            else:
                raise ExpressionError(_("Cislo uz ma desatinnu ciarku!"))

            self._next()

        if has_dot:
            return Token(TokenTypes.FLOAT_TOKEN, float(number_string))
        else:
            return Token(TokenTypes.INT_TOKEN, int(number_string))

    def _make_identifier(self) -> str:
        identifier = ""
        while self._current_char is not None and self._current_char in ascii_letters:
            identifier += self._current_char
            self._next()
        return identifier

    def _make_variable(self) -> Token:
        try:
            token = Token(TokenTypes.VARIABLE_TOKEN, self._variables[self._current_identifier])
            self._current_identifier = None
            return token
        except KeyError:
            raise ExpressionError(_("Premenna '%s' neexistuje!") % self._current_identifier)

    def _make_function(self) -> FunctionToken:
        args_tokens = list()

        if self._current_identifier not in self._functions.keys():
            raise ExpressionError(_("Funkcia '%s' neexistuje!") % self._current_identifier)

        # self.current_char musi byt (, tak ho ignorujem
        self._next()
        start = self._pos
        stack = ["("]

        while self._current_char is not None and stack:
            if self._current_char == "(":
                stack.append(self._current_char)
            elif self._current_char == ")":
                stack.pop()

            self._next()

        if self._current_char is None and stack:
            raise ExpressionError(_("Funkcia '%s' nie je spravne uzatvorkovana") % self._current_identifier)

        end = self._pos - 1

        if start != end:
            args_tokens = self._tokenize_sub_text(start, end, in_function=True)

        function = deepcopy(self._functions[self._current_identifier])
        self._next()
        self._current_identifier = None
        return FunctionToken(function, args_tokens)
