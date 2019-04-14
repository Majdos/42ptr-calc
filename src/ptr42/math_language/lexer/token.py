from enum import Enum
from typing import Any


class TokenTypes(Enum):
    INT_TOKEN = 1
    FLOAT_TOKEN = 2
    OPERATOR_TOKEN = 3
    FUNCTION_TOKEN = 4
    LPAREN_TOKEN = 5
    RPAREN_TOKEN = 6
    VARIABLE_TOKEN = 7
    COMMA_TOKEN = 8


max_precedence = 1000


class Token(object):
    def __init__(self, token_type: TokenTypes, value: Any, precedence: int = 1000):
        self.type = token_type
        self.value = value
        self.precedence = precedence

        if precedence > max_precedence:
            raise ValueError(f"Maximalne precedencia je {max_precedence}")

    def __repr__(self):
        return f"{self.type}:{self.value}"
